---
title: "DIASPORA — journal du Reality Test"
date: "2026-09-30"
language: "fr"
document_role: "journal"
visibility: "public"
status: "working"
---

# Reality Test — 30 septembre 2026

```text
T0:
  timestamp: 2026-09-30T22:31:58+02:00
  declared_by: Principal, GitHub issue 96
  benchmark: two hours, experimental, not a permission to fake completeness
  state: no durable prototype available to a cold handler
  capabilities available: corpus, public web, static files, one coding agent
  records: 0 in this repository
  external monetary spend: 0
```

## Milestone — repository slice

```text
timestamp: 2026-09-30T23:22:37+02:00
elapsed wall-clock from T0: 50 minutes 39 seconds
state: partial
baseline before this slice: f7d30c8cff5b42da0b4ef656c1a3d5c2df52b111

records published: 30 entities, of which
  people: 0
  organizations: 4
  projects: 2
  places: 4
  skills: 5
  offers: 7
  needs: 2
  sources: 6
  relations: 28
countries of presence: 1 (France)
corsican communes sourced: Bastia, Corte
contributions awaiting review inside the seed: 0
offers with open_to_help true: 1 (the correction offer of this project)

external monetary spend: 0
infrastructure: local workstation, public HTTP reads, no new host, no DNS change
human actions: Principal opened issue 96 and asked to resume it
agent actions: cold read of issue 96 (no later comments), fetch of main, bounded Suna search, public-source reads, implementation, node checks
tests: node scripts/validate-seed.js
failures: none in that check
limitations:
  - not a worldwide directory
  - diaspora.acorsica.org not deployed
  - Suna primary source not found
  - 1996-1997 prototype not corroborated
  - map tiles unverified if the CDN is blocked
  - phone layout not checked on a device
  - adversarial review written by the same handler
  - no legal opinion
next discriminating step: human decision on publishing the static projection, or a sourced addition of public organizations, or recovery of a Suna primary source
```

Counts above are the ones printed by the validator against `data/seed.json`. They are not a second handwritten census.

The two-hour mark is 2026-10-01T00:31:58+02:00. This milestone is inside that window. Being inside the window does not make the worldwide hypothesis true.

## Jalon — publication du nom

Ce jalon ne corrige pas le constat de 23:22. À cette heure-là, le nom n'était pas publié. La publication vient après.

```text
date: 2026-10-01
place: after the two-hour mark 2026-10-01T00:31:58+02:00
state: partial
authorization: the Principal wrote "ok, let's do it" after issue comment 5920634253
scope of that phrase: publish the existing static tree at diaspora.acorsica.org
not included: a frozen edition, a new seed, personal records, a Suna text, DNS for any other name
public url: https://diaspora.acorsica.org/
redirect: / -> /web/index.html
seed: /data/seed.json schema diaspora.seed.v0, 30 entities, 0 people
source commit: 6de2f1689db351321967fdabc2025adca62a426d
release: /srv/www/diaspora/current -> releases/2026-10-01-6de2f16
rollback release left in place: releases/2026-10-01-82c261c
dns: DNS-only CNAME diaspora.acorsica.org to fracta.fractavolta.com, TTL 300
edge: Fracta TLS reverse_proxy to http://100.84.109.87:80
origin: Fracta2 HTTP file server, no new public ingress
checks: 302, 200 on the home page, seed schema and count, sibling sites still 200
validator: node scripts/validate-seed.js passed before 6de2f16
external monetary spend: 0
later workstation check: the name resolved to 82.70.234.207 and the home page returned 200
earlier NXDOMAIN: Wi-Fi resolver 10.198.17.11 had a negative cache at the first public check; authoritative DNS and 8.8.8.8 already answered
local port: 127.0.0.1:8765 stays occupied by the nssm-supervised Node process; do not stop it
operium note: JeanHuguesRobert/operium docs/diaspora-acorsica-static.md
issue receipt: https://github.com/JeanHuguesRobert/barons-Mariani/issues/96#issuecomment-5921089658
```

Le résultat reste partiel. Quatre organisations, deux projets, aucune personne. La source primaire de l'appel Suna et le prototype SQL/Tcl de 1996-1997 restent ouverts. Les pages françaises sont une projection, pas la doctrine canonique.

Prochaine action reprenable : ajouter une organisation ou un projet public seulement avec une source publique en main. Ne pas refaire l'échafaudage, le repli de port, ni cette publication.

## Jalon — enrichissement sourcé du graphe et 5 faces du Livre Vivant

```text
date: 2026-10-05
state: partial
scope: issues #96 et #109 (enrichissement sourcé du graphe, 5 faces du Livre Vivant)
not included: personnes individuelles, modification DNS/serveur, gel d'édition

records published: 59 entities, of which
  people: 0
  organizations: 9
  projects: 3
  places: 8
  skills: 10
  offers: 13
  needs: 3
  sources: 13
  relations: 58
countries of presence: 1 (France)
corsican communes sourced: Ajaccio, Bastia, Corte
contributions awaiting review: 0
offers with open_to_help true: 3 (correction DIASPORA, accompagnement retour Vultà)

queries checked:
  query A (mobilité retour Vultà): pass, open_to_help true
  query B (coordination Bouches-du-Rhône): pass, Fédération Marseille
  query C (solidarité Alpes-Maritimes): pass, Anima Corsa Nice
  query D (anti-hallucination répondant): pass, holder is not helper

5 faces complétées:
  1. Livre: manuscript/, web/book.html, annexes
  2. Magazine: magazine/, web/magazine.html (3 numéros)
  3. Site: index.html, directory.html, map.html, match.html, entity.html, privacy.html
  4. Guide conversationnel: guide.html, guide.js, guide-profile.yml (8 invariants)
  5. Collecte engageante: contribute.html (schéma diaspora.contribution.v0)

validator: node scripts/validate-seed.js passed (all checks passed)
```

Le graphe intègre désormais des fonctions collectives différenciées (réseau professionnel, programme opérationnel de retour insulaire, coordination territoriale, solidarité éducative, sociabilité diasporique) tout en maintenant l'interdiction d'ingérer des profils individuels et le conservatisme d'open_to_help.

