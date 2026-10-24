#!/usr/bin/env python3
"""Validation du texte maître CC : compilation stricte à deux rendus, sans émission."""
import argparse
import hashlib
import importlib.util
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path

def require(check, message):
    if not check:
        raise SystemExit("FAIL: " + message)

def require_no_internal_markers(text, label):
    markers = [
        r"<!--\s*#pragma\b",
        r"<!--\s*INTERNAL-(?:TODO|META)\b",
        r"\bNE PAS ENVOYER\b",
        r"\bNON SATISFAIT\b",
        r"\bfiling_ready\s*=",
        r"\bProjet de travail v0\.1\b",
        r"\bPaquet #\d+\b",
        r"Contrôle avant émission",
    ]
    leaked = [pattern for pattern in markers if re.search(pattern, text, re.I)]
    require(not leaked, f"internal construction marker leaked into {label}: {leaked}")

def without_heading_depth(text):
    """Compare embedded Markdown sources while allowing intentional nesting."""
    return re.sub(r"(?m)^(#{1,6})[ \t]+", "", text)

def split_markdown_table_row(line):
    cells = re.split(r"(?<!\\)\|", line.strip())
    if cells and cells[0].strip() == "":
        cells = cells[1:]
    if cells and cells[-1].strip() == "":
        cells = cells[:-1]
    return [cell.replace(r"\|", "|").strip() for cell in cells]

def is_markdown_table_separator(line):
    cells = split_markdown_table_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)

def tables_as_records(markdown):
    """Render pipe tables as labeled records so fixed-width TXT stays readable."""
    lines = markdown.splitlines()
    output = []
    index = 0
    while index < len(lines):
        if (index + 1 < len(lines) and lines[index].lstrip().startswith("|")
                and lines[index + 1].lstrip().startswith("|")
                and is_markdown_table_separator(lines[index + 1])):
            headers = split_markdown_table_row(lines[index])
            index += 2
            while index < len(lines) and lines[index].lstrip().startswith("|"):
                values = split_markdown_table_row(lines[index])
                if not is_markdown_table_separator(lines[index]):
                    for column in range(max(len(headers), len(values))):
                        header = headers[column] if column < len(headers) else f"Column {column + 1}"
                        value = values[column] if column < len(values) else ""
                        output.append(f"{header}: {value}" if value else f"{header}:")
                    output.append("")
                index += 1
            continue
        output.append(lines[index])
        index += 1
    return "\n".join(output) + "\n"

def paginate_rfc_text(text, columns, page_lines):
    pages = []
    for segment in text.split("\f"):
        lines = segment.splitlines()
        current = []
        index = 0

        def wrap_line(line):
            if len(line) <= columns:
                return [line.rstrip()]
            indent = len(line) - len(line.lstrip())
            return textwrap.wrap(
                line.strip(), width=columns, initial_indent=" " * indent,
                subsequent_indent=" " * indent, break_long_words=True,
                break_on_hyphens=False, replace_whitespace=False,
            ) or [""]

        while index < len(lines):
            if lines[index].lstrip().startswith("[COMMENTAIRE DE PILOTAGE"):
                block = []
                while index < len(lines):
                    line = lines[index]
                    block.extend(wrap_line(line))
                    index += 1
                    if line.lstrip().startswith("[FIN DU COMMENTAIRE"):
                        break
                while current and not current[-1]:
                    current.pop()
                if len(block) > page_lines:
                    raise ValueError("pilotage comment exceeds one RFC text page")
                if current and len(current) + len(block) > page_lines:
                    pages.append(current)
                    current = []
                current.extend(block)
                continue

            current.extend(wrap_line(lines[index]))
            index += 1
            while len(current) >= page_lines:
                pages.append(current[:page_lines])
                current = current[page_lines:]
        while current and not current[-1]:
            current.pop()
        if current:
            pages.append(current)
    return "\r\n\f\r\n".join("\r\n".join(page) for page in pages)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("master", type=Path)
    ap.add_argument("--qpc-l299", type=Path, required=True)
    ap.add_argument("--qpc-l303", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--pdf-engine", default="typst",
                    help="Pandoc PDF engine (default: typst)")
    ap.add_argument("--pandoc", type=Path,
                    help="Pandoc executable (auto-detected on PATH and in LOCALAPPDATA otherwise)")
    ap.add_argument("--typst-header", type=Path,
                    default=Path(__file__).with_name("typst-pagination-header.typ"),
                    help="Typst header that makes long table figures breakable")
    ap.add_argument("--preview", action="store_true", help="Produce non-filing draft TXT/PDF even while review blockers remain")
    a = ap.parse_args()
    master=a.master.read_text(encoding="utf-8")
    content=re.sub(r"\A---\n[\s\S]*?\n---\n", "", master, count=1)
    require(not re.search(r"(?m)^---\n(?:title|author|authors):",content),
            "frontmatter d'un document incorporé : risque d'écraser les métadonnées du maître")
    def body(p):
        t=p.read_text(encoding="utf-8")
        return re.sub(r"\A---\n[\s\S]*?\n---\n", "", t).strip()
    q1=body(a.qpc_l299)
    q2=body(a.qpc_l303)
    require(without_heading_depth(q1) in without_heading_depth(master),
            "QPC L.299 intégrale absente / version différente")
    require(without_heading_depth(q2) in without_heading_depth(master),
            "QPC L.303 intégrale absente / version différente")
    processor = Path(__file__).with_name("preprocess-document.py")
    spec = importlib.util.spec_from_file_location("document_processor", processor)
    document_processor = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(document_processor)
    format_spec = document_processor.read_format_spec(a.master)
    def institutional_qpc_body(p):
        projected = document_processor.transform(p, "institutional")
        return re.sub(r"\A---\n[\s\S]*?\n---\n", "", projected, count=1).strip()
    q1_projected = institutional_qpc_body(a.qpc_l299)
    q2_projected = institutional_qpc_body(a.qpc_l303)
    require(len(re.findall(r"(?m)^#{1,6} VIII ter\. Index vérifiable de P-46\b", master)) == 1,
            "Index P-46 manquant / dupliqué")
    found=set(re.findall(r"\|\s*\*\*P-46\.(\d{2})\*\*",master))
    require(found == {f"{i:02}" for i in range(1,47)}, "46 identifiants P-46 incomplets")
    require("Ni cet index ni cette sélection ne constituent la reproduction intégrale des 46 messages annoncés au bordereau" in master,
            "Limite documentaire sur la reproduction partielle de P-46 manquante")
    # Aucun rendu final tant que des instructions éditoriales subsistent.
    markers = ["## X. Contrôle avant émission — NON SATISFAIT",
               "NE PAS ENVOYER", "filing_ready=false"]
    blocked=any(x in master for x in markers)
    if blocked and not a.preview:
        print("BLOCKED: editorial review flags remain. Use --preview for a clearly NON-FILING draft.")
        print("QPC integrity PASS; P-46 index PASS; P-46 bodies NOT INCLUDED.")
        raise SystemExit(2)
    if not blocked:
        raise SystemExit("BLOCKED: removing editorial flags is not a legal or evidentiary sign-off.")
    print("APERÇU DE TRAVAIL — NON PRÊT POUR TRANSMISSION. P-46 n'est pas reproduit intégralement ; les pièces jointes restent séparées.")
    a.output.mkdir(parents=True,exist_ok=True)
    suffix = "-preview" if a.preview else ""
    txt=a.output/f"complements-information{suffix}.txt"
    pdf=a.output/f"complements-information{suffix}.pdf"
    pandoc = str(a.pandoc) if a.pandoc else shutil.which("pandoc")
    if not pandoc and os.environ.get("LOCALAPPDATA"):
        local_candidate = Path(os.environ["LOCALAPPDATA"]) / "Pandoc" / "pandoc.exe"
        if local_candidate.is_file():
            pandoc = str(local_candidate)
    require(bool(pandoc) and Path(pandoc).is_file(), "Pandoc executable not found")
    pdftotext = shutil.which("pdftotext")
    require(pdftotext is not None, "pdftotext is required to inspect rendered PDF text")

    with tempfile.TemporaryDirectory(prefix="sen-2026-6589-projection-") as tmp:
        projection = Path(tmp) / "institutional-projection.md"
        projection_target = "preview" if a.preview else "institutional"
        subprocess.run([sys.executable,str(processor),str(a.master.resolve()),
                        "--target",projection_target,"--output",str(projection)],check=True)
        projected_text = projection.read_text(encoding="utf-8")
        require_no_internal_markers(projected_text,"rendered Markdown projection")
        has_pilotage = "COMMENTAIRE DE PILOTAGE" in projected_text
        require(has_pilotage == a.preview,
                "pilotage comments must appear only in the explicitly marked preview")
        require(without_heading_depth(q1_projected) in without_heading_depth(projected_text),
                "QPC L.299 missing from institutional projection")
        require(without_heading_depth(q2_projected) in without_heading_depth(projected_text),
                "QPC L.303 missing from institutional projection")

        plain_projection = Path(tmp) / "plain-text-projection.md"
        plain_projection.write_text(tables_as_records(projected_text), encoding="utf-8")
        subprocess.run([pandoc,str(plain_projection),"-f","markdown+yaml_metadata_block","-t","plain",
                        "--standalone",
                        "--toc",f"--toc-depth={format_spec['plain_text']['toc_depth']}",
                        "--metadata=toc-title=Sommaire","--wrap=none","-o",str(txt)],check=True)
        raw_txt = txt.read_text(encoding="utf-8")
        toc_start = re.search(r"(?m)^- ", raw_txt)
        require(toc_start is not None, "Pandoc plain-text TOC was not generated")
        raw_txt = raw_txt[:toc_start.start()] + "Sommaire\n\n" + raw_txt[toc_start.start():]
        main_title = "Compléments d’information — dossier 2026-6589 SEN"
        body_start = re.search(r"(?m)^" + re.escape(main_title) + r"$", raw_txt)
        require(body_start is not None, "main document title missing after plain-text TOC")
        raw_txt = raw_txt[:body_start.start()] + "\f\n" + raw_txt[body_start.start():]
        txt.write_text(raw_txt, encoding="utf-8")
        pdf_projection = Path(tmp) / "pdf-projection.md"
        pdf_projection.write_text(re.sub(
            r"\A---\r?\n[\s\S]*?\r?\n---\r?\n",
            lambda match: match.group(0) + "\n```{=typst}\n#pagebreak()\n```\n\n",
            projected_text, count=1,
        ), encoding="utf-8")
        pdf_command=[pandoc,str(pdf_projection),"-f","markdown+yaml_metadata_block",
                     "--toc",f"--toc-depth={format_spec['pdf']['toc_depth']}",
                     "--metadata=lang=fr","--pdf-engine",a.pdf_engine]
        if a.pdf_engine == "typst":
            require(a.typst_header.is_file(), "en-tête Typst de pagination absent")
            pdf_command.extend(["--include-in-header",str(a.typst_header)])
        pdf_command.extend(["-o",str(pdf)])
        subprocess.run(pdf_command,check=True)

    raw_txt = txt.read_text(encoding="utf-8")
    paginated_txt = paginate_rfc_text(
        raw_txt, format_spec["plain_text"]["columns"],
        format_spec["plain_text"]["page_lines"],
    )
    txt.write_bytes(b"\xef\xbb\xbf" + paginated_txt.encode("utf-8"))
    txt_text = txt.read_text(encoding="utf-8-sig")
    require_no_internal_markers(txt_text,"rendered TXT")
    require("Sommaire" in txt_text, "table of contents missing from rendered TXT")
    require(txt.read_bytes().startswith(b"\xef\xbb\xbf"), "RFC text UTF-8 BOM missing")
    text_pages = txt_text.split("\f")
    require(all(len(page.strip("\r\n").splitlines()) <= format_spec["plain_text"]["page_lines"]
                for page in text_pages), "RFC text page exceeds configured line count")
    require(all(len(line) <= format_spec["plain_text"]["columns"]
                for page in text_pages for line in page.splitlines()),
            "RFC text line exceeds configured column count")
    extracted_pdf = subprocess.run([pdftotext,str(pdf),"-"],check=True,
                                   capture_output=True).stdout.decode("utf-8",errors="replace")
    require_no_internal_markers(extracted_pdf,"extracted PDF text")
    require(re.search(r"(?i)(?:sommaire|table des matières)", extracted_pdf) is not None,
            "table of contents missing from rendered PDF")
    print("Projection, TXT and PDF text marker checks PASS.")
    for p in [txt,pdf]:
        print(p,p.stat().st_size,hashlib.sha256(p.read_bytes()).hexdigest())

if __name__=="__main__":
    main()
