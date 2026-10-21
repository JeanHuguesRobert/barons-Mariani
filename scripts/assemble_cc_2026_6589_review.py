#!/usr/bin/env python3
"""Deterministic local assembly of the 2026-6589 SEN review text; never sends."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "research/senatoriales-2026/complement-2026-6589-sen/"
SOURCES = [
 BASE+"texte-maitre-travail-v0.1.md",
 BASE+"notice-g1-p06-p09-double-fonction.md",
 BASE+"notice-g2-g3-p13-p17-p19-double-fonction.md",
 BASE+"notice-g4-provenance-pertinence-p12-p46.md",
 *[BASE+f"notice-n{i}-{suffix}-double-fonction.md" for i,suffix in [
 (1,"p04-p05-p07-p08"),(2,"p10-p11-p12"),(3,"p15-p16"),
 (4,"sources-procedurales"),(5,"g5-scrutin"),(6,"p42-p43")]],
 BASE+"notice-provenance-p46-courriels-verification-p12-p13-2026-10-21.md",
 BASE+"doctrine-notices-double-fonction-suite-demande-greffe-2026-10-21.md",
 BASE+"notice-programme-amendement-devise-indivisibilite-2026-10-21.md",
 BASE+"notice-continuite-revolutions-corses-1729-2026.md",
 BASE+"notice-calendrier-senat-motif-candidature-2026-10-21.md",
 "research/senatoriales-2026/qpc/memoire-qpc-l299-formalisme-candidature-empechement-remplacant.md",
 "research/senatoriales-2026/qpc/memoire-qpc-l303-garanties-juridictionnelles.md",
 "research/autonomia/amendement_effectivite_article_72-5.md",
 "research/autonomia/genese_probatoire_amendement_effectivite_2026.md",
 "research/devise_republicaine/histoire_devise_effectivite_autonomie.md",
]
def sha(data): return hashlib.sha256(data).hexdigest()
def main():
    a=argparse.ArgumentParser()
    a.add_argument("--out",default="/tmp/cc-2026-6589-sen-review")
    args=a.parse_args()
    out=Path(args.out); out.mkdir(parents=True,exist_ok=True)
    parts=["BROUILLON DE RELECTURE, NE PAS ENVOYER.\n"
           "Ceci est une CONCATENATION REPRODUCTIBLE de sources de travail, "
           "pas encore le mémoire éditorial final. Les sources contiennent "
           "des instructions internes et des recouvrements à éliminer. "
           "Les originaux privés ne sont pas inclus.\n"]
    manifest=[]
    for item in SOURCES:
        p=ROOT/item
        if not p.is_file(): raise SystemExit("MISSING SOURCE: "+str(p))
        raw=p.read_bytes()
        try: content=raw.decode("utf-8")
        except UnicodeDecodeError: raise SystemExit("NOT UTF8: "+str(p))
        manifest.append({"path":item,"bytes":len(raw),"sha256":sha(raw)})
        parts.append("\n\n"+"="*60+"\nSOURCE INTÉGRALE: "+item+
                     "\n"+"="*60+"\n\n"+content)
    data="".join(parts).encode("utf-8")
    (out/"gmail-review-UNSENT.txt").write_bytes(data)
    meta={"status":"REVIEW_ONLY_NOT_FOR_SENDING","source_count":len(SOURCES),
          "output_bytes":len(data),"output_sha256":sha(data),
          "sources":manifest,
          "excluded":"Private native evidence, EML volume, MP4, PDFs; require manifest and separate review"}
    (out/"manifest-review.json").write_text(json.dumps(meta,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({"output":str(out/"gmail-review-UNSENT.txt"),
                      "source_count":len(SOURCES),"bytes":len(data),
                      "sha256":sha(data),"filing_ready":False},ensure_ascii=False))
if __name__=="__main__": main()
