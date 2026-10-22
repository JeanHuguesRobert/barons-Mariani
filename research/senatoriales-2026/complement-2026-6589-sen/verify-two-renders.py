#!/usr/bin/env python3
"""Validation du texte maître CC : compilation stricte à deux rendus, sans émission."""
import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
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
    require(q1 in master, "QPC L.299 intégrale absente / version différente")
    require(q2 in master, "QPC L.303 intégrale absente / version différente")
    require(master.count("## VIII ter. Index vérifiable de P-46 (reproduction des métadonnées, pas des corps)") == 1,
            "Index P-46 manquant / dupliqué")
    found=set(re.findall(r"\|\s*\*\*P-46\.(\d{2})\*\*",master))
    require(found == {f"{i:02}" for i in range(1,47)}, "46 identifiants P-46 incomplets")
    require("ce tableau n'est donc PAS le recueil intégral P-46 promis par le bordereau" in master,
            "Avertissement sur la non-production intégrale P-46 manquant")
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
    print("PREVIEW ONLY - not for filing. P-46 selection is not exhaustive; attachments remain separate.")
    a.output.mkdir(parents=True,exist_ok=True)
    suffix = "-preview" if a.preview else ""
    txt=a.output/f"memoire-complementaire{suffix}.txt"
    pdf=a.output/f"memoire-complementaire{suffix}.pdf"
    pandoc = str(a.pandoc) if a.pandoc else shutil.which("pandoc")
    if not pandoc and os.environ.get("LOCALAPPDATA"):
        local_candidate = Path(os.environ["LOCALAPPDATA"]) / "Pandoc" / "pandoc.exe"
        if local_candidate.is_file():
            pandoc = str(local_candidate)
    require(bool(pandoc) and Path(pandoc).is_file(), "Pandoc executable not found")
    pdftotext = shutil.which("pdftotext")
    require(pdftotext is not None, "pdftotext is required to inspect rendered PDF text")

    processor = Path(__file__).with_name("preprocess-document.py")
    with tempfile.TemporaryDirectory(prefix="sen-2026-6589-projection-") as tmp:
        projection = Path(tmp) / "institutional-projection.md"
        subprocess.run([sys.executable,str(processor),str(a.master.resolve()),
                        "--target","institutional","--output",str(projection)],check=True)
        projected_text = projection.read_text(encoding="utf-8")
        require_no_internal_markers(projected_text,"institutional Markdown projection")
        require(q1 in projected_text, "QPC L.299 missing from institutional projection")
        require(q2 in projected_text, "QPC L.303 missing from institutional projection")

        subprocess.run([pandoc,str(projection),"-f","markdown+yaml_metadata_block","-t","plain",
                        "--wrap=auto","--columns=88","-o",str(txt)],check=True)
        pdf_command=[pandoc,str(projection),"-f","markdown+yaml_metadata_block",
                     "--pdf-engine",a.pdf_engine]
        if a.pdf_engine == "typst":
            require(a.typst_header.is_file(), "en-tête Typst de pagination absent")
            pdf_command.extend(["--include-in-header",str(a.typst_header)])
        pdf_command.extend(["-o",str(pdf)])
        subprocess.run(pdf_command,check=True)

    txt_text = txt.read_text(encoding="utf-8")
    require_no_internal_markers(txt_text,"rendered TXT")
    extracted_pdf = subprocess.run([pdftotext,str(pdf),"-"],check=True,
                                   capture_output=True).stdout.decode("utf-8",errors="replace")
    require_no_internal_markers(extracted_pdf,"extracted PDF text")
    print("Projection, TXT and PDF text marker checks PASS.")
    for p in [txt,pdf]:
        print(p,p.stat().st_size,hashlib.sha256(p.read_bytes()).hexdigest())

if __name__=="__main__":
    main()
