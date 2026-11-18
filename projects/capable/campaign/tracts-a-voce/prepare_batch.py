#!/usr/bin/env python3
"""A Voce / Capable: offline, traceable print-batch preparation.

This tool DOES NOT register 3Codes, publish a resolver, send messages, or
record endorsements. Every generated 3Code remains unregistered unless a
separate, independently evidenced registrar operation occurs.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import secrets
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote, urlsplit

ALPHABET = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"
FIELDS = ["copy_id", "three_code", "mission_id", "three_code_status", "url_status", "issuance_status"]
MISSION = "CAPABLE-PRESENTATIONS-2027"
COPY_PREFIX = "AV27"
MAX_COUNT = 1_000_000


def normalize_3code(raw: str) -> str:
    """Canonical 3XX-XXX-XXX: 3 + 8 Crockford Base32 characters."""
    compact = re.sub(r"[-\s]", "", raw.upper()).replace("O", "0").replace("I", "1").replace("L", "1")
    if len(compact) != 9 or compact[0] != "3" or any(c not in ALPHABET for c in compact[1:]):
        raise ValueError("3Code invalide : format attendu 3XX-XXX-XXX")
    return f"{compact[:3]}-{compact[3:6]}-{compact[6:9]}"


def code_for(seed: bytes, index: int, attempt: int = 0) -> str:
    if len(seed) != 32 or index <= 0 or attempt < 0:
        raise ValueError("Graine (32 octets), index et tentative invalides")
    digest = hashlib.sha256(b"capable-a-voce-3code-v1\0" + seed + index.to_bytes(8, "big") + attempt.to_bytes(4, "big")).digest()
    n = int.from_bytes(digest[:5], "big")
    suffix = "".join(ALPHABET[(n >> (5 * j)) & 31] for j in range(7, -1, -1))
    return normalize_3code("3" + suffix)


def manifest_rows(seed: bytes, count: int, mission: str = MISSION):
    if not 1 <= count <= MAX_COUNT:
        raise ValueError(f"count doit être compris entre 1 et {MAX_COUNT}")
    seen = set()
    for index in range(1, count + 1):
        attempt = 0
        while True:
            code = code_for(seed, index, attempt)
            if code not in seen:
                seen.add(code)
                break
            attempt += 1  # Collision *dans ce lot* : rééchantillonnage local seulement.
        yield {
            "copy_id": f"{COPY_PREFIX}-{index:05d}",
            "three_code": code,
            "mission_id": mission,
            "three_code_status": "unregistered",
            "url_status": "inactive",
            "issuance_status": "not_issued",
        }


def write_manifest(out: Path, count: int, seed: bytes, mission: str = MISSION):
    out = Path(out)
    if out.exists() or out.with_suffix(".json").exists():
        raise FileExistsError("Fichier de sortie existant : refus d'écraser un lot/registre")
    out.parent.mkdir(parents=True, exist_ok=True)
    try:
        with out.open("x", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(manifest_rows(seed, count, mission))
        digest = hashlib.sha256(out.read_bytes()).hexdigest()
        meta = {
            "schema": "a-voce-tract-manifest-v1",
            "status": "generated-not-printed-or-issued",
            "batch_count": count,
            "mission_id": mission,
            "generated_at_utc": datetime.now(timezone.utc).isoformat(),
            "generator_seed_hex": seed.hex(),
            "seed_is_not_an_authentication_secret": True,
            "manifest_sha256": digest,
            "3code_registry_status": "not-registered",
            "qr_route_status": "not-verified",
            "note": "Un copy_id ou 3Code ne prouve ni détention, ni consentement, ni présentation électorale.",
        }
        out.with_suffix(".json").write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    except Exception:
        if out.exists():
            out.unlink()
        raise
    return meta


def is_valid_public_url(url: str) -> bool:
    try:
        parts = urlsplit(url)
    except ValueError:
        return False
    return (parts.scheme == "https" and bool(parts.hostname) and not parts.username and not parts.password
            and not parts.fragment and parts.hostname not in {"example.org", "example.com", "example.net"}
            and not parts.hostname.endswith(".invalid"))


def validated_url(template: str | None, copy_id: str | None, verified: bool) -> str | None:
    if not template:
        return None
    if not verified:
        raise ValueError("URL fournie : --verified-url requis, après recette HTTP externe réelle")
    if template.count("{copy_id}") > 1:
        raise ValueError("{copy_id} ne peut apparaître qu'une fois")
    url = template.replace("{copy_id}", quote(copy_id or "", safe=""))
    if not is_valid_public_url(url):
        raise ValueError("URL HTTPS publique invalide")
    return url


def register_fonts():
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    choices = [
        ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
        ("/usr/local/share/fonts/DejaVuSans.ttf", "/usr/local/share/fonts/DejaVuSans-Bold.ttf"),
    ]
    for normal, bold in choices:
        if Path(normal).exists() and Path(bold).exists():
            pdfmetrics.registerFont(TTFont("AVRegular", normal))
            pdfmetrics.registerFont(TTFont("AVBold", bold))
            pdfmetrics.registerFontFamily("AVRegular", normal="AVRegular", bold="AVBold")
            return "AVRegular", "AVBold"
    raise RuntimeError("Polices DejaVu Sans absentes : nécessaire pour les accents dans le PDF")


def draw_qr(canvas, x, y, side, data):
    from reportlab.graphics.barcode import qr
    widget = qr.QrCodeWidget(data)
    bounds = widget.getBounds()
    from reportlab.graphics.shapes import Drawing
    from reportlab.graphics import renderPDF
    scale = side / max(bounds[2] - bounds[0], bounds[3] - bounds[1])
    drawing = Drawing(side, side, transform=[scale, 0, 0, scale, 0, 0])
    drawing.add(widget)
    renderPDF.draw(drawing, canvas, x, y)


def render_master(output: Path, url_template: str | None = None, verified: bool = False):
    """One identical one-sided A4 master; no individual copy identity claimed."""
    from reportlab.pdfgen.canvas import Canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.platypus import Paragraph
    from reportlab.lib.styles import ParagraphStyle
    regular, bold = register_fonts()
    url = validated_url(url_template, None, verified)
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas = Canvas(str(output), pagesize=A4, pageCompression=1)
    w, h = A4
    def txt(x, y, text, size=12, is_bold=False):
        canvas.setFont(bold if is_bold else regular, size)
        canvas.drawString(x, y, text)
    def paragraph(x, y, width, text, size=12, leading=17):
        style = ParagraphStyle("p", fontName=regular, fontSize=size, leading=leading)
        p = Paragraph(text, style)
        pw, ph = p.wrap(width, 200)
        p.drawOn(canvas, x, y - ph)
        return y - ph
    canvas.setStrokeColorRGB(0, 0, 0)
    canvas.setLineWidth(1)
    canvas.rect(15*mm, 15*mm, w-30*mm, h-30*mm)
    txt(23*mm, h-37*mm, "A VOCE", 22, True)
    txt(23*mm, h-50*mm, "CAPABLE", 31, True)
    txt(23*mm, h-62*mm, "AUTONOMIE DE CAPACITÉ, PAS DE PAPIER", 10, True)
    canvas.line(23*mm, h-69*mm, w-23*mm, h-69*mm)
    y = h-84*mm
    y = paragraph(23*mm, y, w-46*mm,
                  "<b>La présidentielle 2027 exige 500 présentations d’élus habilités.</b> "
                  "Il ne s’agit pas de 500 signatures de citoyens. Le choix de présenter "
                  "un candidat appartient librement à chaque élu.", 12, 18) - 14*mm
    txt(23*mm, y, "UNE BOUTEILLE À LA MER", 14, True)
    y -= 8*mm
    y = paragraph(23*mm, y, w-46*mm,
                  "Ce tract peut circuler, recevoir une remarque, une question ou une "
                  "contribution volontaire, puis être transmis à quelqu’un d’autre. "
                  "Il est conçu comme un support de discussion sur les capacités "
                  "réelles des citoyens et des territoires.", 12, 17) - 13*mm
    txt(23*mm, y, "TROIS GESTES POSSIBLES", 13, True)
    y -= 9*mm
    for msg in [
        "1. Lire, questionner ou contredire librement.",
        "2. Transmettre ce document à une personne intéressée.",
        "3. Signaler volontairement une piste publique concernant un élu habilité.",
    ]:
        txt(23*mm, y, msg, 9.6)
        y -= 9*mm
    canvas.line(23*mm, 61*mm, w-23*mm, 61*mm)
    if url:
        draw_qr(canvas, w-66*mm, 19*mm, 35*mm, url)
        txt(23*mm, 47*mm, "ACCÈS À L'INFORMATION", 9, True)
        txt(23*mm, 39*mm, "QR : page vérifiée par l'opérateur", 8)
        txt(23*mm, 30*mm, url[:41], 7)
    else:
        canvas.rect(w-65*mm, 20*mm, 34*mm, 34*mm)
        txt(w-62*mm, 38*mm, "QR À ACTIVER", 7, True)
        txt(23*mm, 47*mm, "PROTOTYPE — PAS POUR DISTRIBUTION", 9, True)
        txt(23*mm, 37*mm, "Lien et mentions électorales à valider", 8)
        txt(23*mm, 29*mm, "avant toute impression publique.", 8)
    canvas.showPage()
    canvas.save()


def render_labels(manifest: Path, output: Path, limit: int = 24, url_template: str | None = None,
                  verified: bool = False):
    """24 labels per A4; no publication or online registry action."""
    from reportlab.pdfgen.canvas import Canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    normal, bold = register_fonts()
    if limit < 1 or limit > MAX_COUNT:
        raise ValueError("limit invalide")
    if url_template:
        validated_url(url_template, "AV27-00001", verified)
    output.parent.mkdir(parents=True, exist_ok=True)
    c = Canvas(str(output), pagesize=A4, pageCompression=1)
    w, h = A4
    cols, rows = 3, 8
    margin_x, margin_y = 8*mm, 8*mm
    cell_w = (w - 2 * margin_x) / cols
    cell_h = (h - 2 * margin_y) / rows
    count = 0
    with manifest.open("r", encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        if set(reader.fieldnames or []) != set(FIELDS):
            raise ValueError("Schéma CSV inconnu")
        for r in reader:
            if count >= limit:
                break
            pos = count % (cols * rows)
            if count and pos == 0:
                c.showPage()
            col = pos % cols
            row = pos // cols
            x = margin_x + col * cell_w
            y = h - margin_y - (row + 1) * cell_h
            c.setStrokeColorRGB(0.35, 0.35, 0.35)
            c.setLineWidth(0.35)
            c.rect(x, y, cell_w, cell_h)
            c.setFillColorRGB(0, 0, 0)
            c.setFont(bold, 8)
            c.drawString(x + 3*mm, y + cell_h - 7*mm, r["copy_id"])
            c.setFont(normal, 9)
            c.drawString(x + 3*mm, y + cell_h - 14*mm, r["three_code"])
            url = validated_url(url_template, r["copy_id"], verified) if url_template else None
            if url:
                draw_qr(c, x + cell_w - 22*mm, y + 3*mm, 19*mm, url)
                c.setFont(normal, 5.3)
                c.drawString(x + 3*mm, y + 3.3*mm, "3Code non enregistré")
            else:
                c.setFont(normal, 6.3)
                c.drawString(x + 3*mm, y + 5*mm, "3Code NON ENREGISTRÉ")
                c.drawString(x + 3*mm, y + 2*mm, "QR inactif / essai")
            count += 1
    if count == 0:
        raise ValueError("Manifest vide")
    c.showPage()
    c.save()
    return count


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)
    m = sub.add_parser("manifest", help="Générer un lot manifest CSV + JSON, sans effet réseau")
    m.add_argument("--count", type=int, default=40000)
    m.add_argument("--out", type=Path, required=True)
    m.add_argument("--seed-hex", help="64 chiffres hex pour reproduction stricte ; sinon aléatoire")
    f = sub.add_parser("master", help="Tract maître A4 N&B d'une page")
    f.add_argument("--out", type=Path, required=True)
    l = sub.add_parser("labels", help="Étiquettes optionnelles 3 colonnes x 8, N&B")
    l.add_argument("--manifest", type=Path, required=True)
    l.add_argument("--out", type=Path, required=True)
    l.add_argument("--limit", type=int, default=24)
    for p in (f, l):
        p.add_argument("--url-template", help="HTTPS réel ; {copy_id} permis dans labels seulement")
        p.add_argument("--verified-url", action="store_true", help="L'opérateur atteste une recette HTTP réelle")
    args = parser.parse_args(argv)
    if args.cmd == "manifest":
        seed = bytes.fromhex(args.seed_hex) if args.seed_hex else secrets.token_bytes(32)
        meta = write_manifest(args.out, args.count, seed)
        print(json.dumps({"manifest": str(args.out), "count": args.count, "sha256": meta["manifest_sha256"]}, ensure_ascii=False))
    elif args.cmd == "master":
        if args.url_template and "{copy_id}" in args.url_template:
            parser.error("Le tract maître ne peut contenir de QR individuel")
        render_master(args.out, args.url_template, args.verified_url)
        print(str(args.out))
    elif args.cmd == "labels":
        n = render_labels(args.manifest, args.out, args.limit, args.url_template, args.verified_url)
        print(json.dumps({"labels": n, "path": str(args.out)}))


if __name__ == "__main__":
    main()