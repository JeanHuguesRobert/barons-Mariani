#!/usr/bin/env python3
"""Validation du texte maître CC : compilation stricte à deux rendus, sans émission."""
import argparse
import hashlib
import re
import subprocess
from pathlib import Path

def require(check, message):
    if not check:
        raise SystemExit("FAIL: " + message)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("master", type=Path)
    ap.add_argument("--qpc-l299", type=Path, required=True)
    ap.add_argument("--qpc-l303", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    a = ap.parse_args()
    master=a.master.read_text(encoding="utf-8")
    def body(p):
        t=p.read_text(encoding="utf-8")
        return re.sub(r"\\A---\\n[\\s\\S]*?\\n---\\n", "", t).strip()
    q1=body(a.qpc_l299)
    q2=body(a.qpc_l303)
    require(q1 in master, "QPC L.299 intégrale absente / version différente")
    require(q2 in master, "QPC L.303 intégrale absente / version différente")
    require(master.count("## VIII ter. Index des 46 courriels") == 1, "Index P-46 manquant / dupliqué")
    found=set(re.findall(r"\\|\\s*\\*\\*P-46\\.(\\d{2})\\*\\*",master))
    require(found == {f"{i:02}" for i in range(1,47)}, "46 identifiants P-46 incomplets")
    require("P-46 a été matériellement communiqué dans sa totalité" in master,
            "Avertissement sur la non-production intégrale P-46 manquant")
    # Aucun rendu final tant que des instructions éditoriales subsistent.
    markers = ["## X. Contrôle avant émission — NON SATISFAIT",
               "NE PAS ENVOYER", "filing_ready=false"]
    if any(x in master for x in markers):
        print("NOT FILING READY: source contains editorial blockers; no production deliverable.")
        print("QPC integrity PASS; P-46 index PASS; P-46 message bodies NOT PROVIDED.")
        return
    a.output.mkdir(parents=True,exist_ok=True)
    txt=a.output/"memoire-complementaire.txt"
    pdf=a.output/"memoire-complementaire.pdf"
    subprocess.run(["pandoc",str(a.master),"-f","markdown+yaml_metadata_block","-t","plain",
                    "--wrap=auto","--columns=88","-o",str(txt)],check=True)
    subprocess.run(["pandoc",str(a.master),"-f","markdown+yaml_metadata_block","-o",str(pdf)],check=True)
    for p in [txt,pdf]:
        print(p,p.stat().st_size,hashlib.sha256(p.read_bytes()).hexdigest())

if __name__=="__main__":
    main()
