---
title: "Contrôle de fidélité ciblé — manuscrit v1.2 vers v2.5"
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A."
date: "2026-10-23"
license: "CC BY-SA 4.0"
language: fr
version: "0.1"
status: "partial-comparative-audit"
document_role: operational
document_kind: semantic-preservation-audit
update_policy: UP-DEFAULT-REVIEWED
provenance:
  origin_type: repository
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "https://github.com/JeanHuguesRobert/barons-Mariani/commit/befe0b5676c3c4ee96f06453993f943191227e81"
  origin_date: "2026-10-21"
  derived_from:
    - "https://github.com/JeanHuguesRobert/barons-Mariani/issues/150"
review:
  status: internal-only
  reviewed_by: []
---

# Audit comparatif v1.2 → v2.5 : vérifications ciblées

**Source immuable :** [draft v1.2 revu par Grok](https://github.com/JeanHuguesRobert/barons-Mariani/blob/befe0b5676c3c4ee96f06453993f943191227e81/research/devise_republicaine/histoire_devise_effectivite_autonomie_review_draft_2026-10-21.md).

**Destination examinée :** [manuscrit v2.5](histoire_devise_double_lecture_consolidation_v2_5.md), blob GitHub `d664b7cf9f81e4d223558efca9caf296ec0c77e9`. Il s'agit d'un contrôle spécifique de cette version, indépendant de tout remaniement ultérieur.

## Contrôles effectivement réalisés

| Test | Résultat | Portée |
| --- | --- | --- |
| Présence des 16 chapitres | PASS | Structure, pas équivalence de tous les paragraphes |
| Volume (caractères) | v1.2 : 134 615 ; v2.5 : 160 508 | Indicateur de volume, **pas** de fidélité |
| URL externes et absolues Markdown | 54 destinations uniques initiales ; 58 dans v2.5 | 53/54 destinations v1.2 conservées littéralement |
| Différence URL | `https://github.com/JeanHuguesRobert/barons-Mariani/issues/146` seule absente de v2.5 | Issue de **revue interne**, lien de provenance à restaurer explicitement |
| Vérification par marqueurs | Présence maintenue de 72 demandes / 13 évolutions, 57 saisines / 4 suites favorables / 3 rejets, décisions QPC 2018, CGCT L. 4422-16/17, DDHC art. 16, 1793/1892/1904, etc. | Vérifie seulement l'existence de notions, **pas leur attribution, exactitude ni leur portée** |
| Marqueurs auteurs et jurisprudence | Sen, Nussbaum, Ostrom, Habermas, Rosanvallon ; Mathieu-Mohin, Mugemangango, Grosaru, Bompard | Aucune disparition de ces marqueurs détectée |
| Blocs de code / citations en retrait | Même nombre de délimiteurs de blocs de code (zéro) ; quatre lignes commençant par `>` dans chaque document | Contrôle formel restreint |

**Précaution cruciale :** le test de présence d'un nom, d'une date ou d'une URL **ne démontre pas** la conservation de la proposition associée. Le nombre de liens conservés ne certifie ni leur résolution actuelle ni la pertinence de leur usage. Les tableaux comparatifs, les restrictions, les critiques et les nuances doivent faire l'objet de confrontations de sens plus fines.

## Correction FBF localisée

Restaurer dans le manuscrit v2.5 un lien explicite vers [l'issue #146 — revue interne](https://github.com/JeanHuguesRobert/barons-Mariani/issues/146), en la distinguant nettement de la revue externe Grok du draft v1.2. **Ne pas réattribuer** à Grok la relecture de la v2.5.

## Gates encore ouverts

1. Échantillonnage critique **par proposition et degré de certitude** de chacun des seize chapitres, notamment VII, IX à XVI : où sont passés les arguments, contre-exemples, réserves et sources ?
2. Vérification sémantique inverse : quelles idées nouvelles sont scénarios, synthèses pédagogiques ou propositions doctrinales et non résultats historiques ou juridiques ?
3. Résolution indépendante des URLs institutionnelles principales et examen des citations verbatim ; archives du XIXe siècle pour 1880.
4. Vérification Cogentia frontmatter CLI ; revue froide par exécuteur distinct de la v2.5.

**Verdict provisoire :** aucun effacement massif de références vérifié ; **non-perte sémantique exhaustive UNKNOWN**, et non PASS. Le libellé de l'amendement v0.7 n'a pas été modifié par cet audit.
