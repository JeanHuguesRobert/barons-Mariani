---
title: "2026-6589 SEN — Production Quarto sur Fracta2 via Ubikia et Operium"
author: "Jean Hugues Noël Robert"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-21"
status: "working-paper"
version: "0.1"
license: "CC BY-SA 4.0"
language: "fr"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/senatoriales-2026/complement-2026-6589-sen/rendu-ubikia-operium-fracta2.md"
document_role: "operational"
document_kind: "rendering-contract"
visibility: "public"
update_policy: "UP-DEFAULT-REVIEWED"
provenance:
  origin_type: "repository"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "https://github.com/JeanHuguesRobert/barons-Mariani/issues/133"
  origin_date: "2026-10-21"
  derived_from:
    - "https://github.com/JeanHuguesRobert/ubikia/blob/main/docs/reactive-products-v0.md"
    - "https://github.com/JeanHuguesRobert/operium/blob/main/docs/suicide-corse-preview-gateway.md"
review:
  status: "unreviewed"
  reviewed_by: []
---

# Réutilisation du pipeline documentaire existant

## Décision architecturale

**Ne pas créer un autre moteur PDF.** Utiliser Ubikia pour la projection Markdown canonique vers Quarto/QMD puis PDF et manifeste, Operium pour l'exécution sur le FractaNode Fracta2. Le script local `scripts/sen-2026-6589-build.py` est une première expérimentation non encore validée ; le réduire à une **composition** du triptyque et une projection texte brut, ou le retirer si le moteur Ubikia peut satisfaire directement ce besoin.

Quarto demeure un backend, pas une autorité sémantique du Corpus.

## Sources souveraines

1. `texte-maitre-travail-v0.1.md` : consolidation et renvois by reference vers les QPC.
2. `../qpc/memoire-qpc-l299-formalisme-candidature-empechement-remplacant.md` : QPC L.299 autonome.
3. `../qpc/memoire-qpc-l303-garanties-juridictionnelles.md` : QPC L.303 autonome.

Les copies de travail, QMD et PDF sont exclusivement des **projections**. Les frontmatters canoniques restent dans les sources. Les deux mémoires QPC sont reproduits **intégralement dans le PDF englobant** et existent **chacun en PDF autonome**. Les mêmes versions des sources alimentent ces trois PDF et le corps textuel du courriel.

## Pipeline de sortie

```text
3 Markdown canoniques à commit identifié
     ↓ composition par référence et validation des ancres
1 Markdown consolidé temporaire + 2 sources QPC
     ↓ Ubikia Reactive Products (quarto-book backend)
PDF consolidé + PDF QPC L.299 + PDF QPC L.303
     ↓ contrôle du texte brut intégral, des titres et des pièces
texte du courriel + 3 PDF + manifestes par version
```

Un **manifest agrégé** rattache chaque PDF au même jeu de trois sources versionnées, aux contrats de projection et à la version du renderer. Les SHA-256 doivent porter sur les **artefacts réels**, et non sur leur nom supposé.

**Point d'intégration à tester :** Ubikia v0 accepte des chapitres Markdown avec frontmatter mais n'effectue pas lui-même une inclusion arbitraire de section « by reference ». La composition du Markdown consolidé demeure une étape amont explicite, dont le résultat temporaire doit figurer au manifeste comme dérivé ; ne jamais le promouvoir en source souveraine.

## Réutilisation prouvée par le Corpus

- [Ubikia Reactive Products](https://github.com/JeanHuguesRobert/ubikia/blob/main/docs/reactive-products-v0.md) : `npm run render -- --corpus ... --projection ...`, QMD généré, Quarto, `manifest.json` comprenant hashes et révisions. Rend uniquement un **brouillon**, sans publication.
- [Operium Fracta2](https://github.com/JeanHuguesRobert/operium/blob/main/docs/suicide-corse-preview-gateway.md) : version historique observée de Quarto : **1.10.18** à `/usr/local/bin/quarto`, TinyTeX/XeLaTeX à `/home/ubuntu/.TinyTeX/bin/aarch64-linux/xelatex`, observation du 28 septembre 2026. Existence actuelle **à revérifier**, ne pas confondre trace historique et disponibilité.
- [Contrat de publication Ubikia](https://github.com/JeanHuguesRobert/ubikia/blob/main/docs/suicide-corse-preview-publication.md) : séparation dry-run/apply/commit/push, checkouts propres et absence de promotion publique automatique.
- [Fracta2 publication Operium](https://github.com/JeanHuguesRobert/operium/blob/main/docs/fracta2-github-static-release.md) : une capacité SSH GitHub à large portée **n'autorise pas** à elle seule push, publication ou envoi au greffe.

## Premier Reality Test sur Fracta2 — sans effet externe

Utiliser une **arborescence temporaire propre** et indépendante des checkouts permanents ; ne jamais reset/stash les modifications locales préexistantes.

```sh
set -eu
command -v node
command -v quarto
quarto --version
test -x /home/ubuntu/.TinyTeX/bin/aarch64-linux/xelatex
git -C /srv/cogentia/repos/ubikia status --short
git -C /srv/cogentia/repos/barons-Mariani status --short
```

Vérifier les versions et permissions ; ensuite effectuer **un rendu draft isolé** depuis les sources Git gelées dans un worktree temporaire, avec une projection Ubikia respectant son schéma actuel. Conserver le manifeste, les journaux de tests et la liste des artefacts. Ne pas modifier un site, un symlink `current`, un domaine ou un dépôt d'édition.

## Contrôles avant tout usage contentieux

1. Trois sources souveraines et leur commit exact enregistrés ; frontmatters vérifiés avec l'outil Cogentia.
2. Les QPC apparaissent **intégralement**, sans copier les frontmatters techniques dans le document à remettre.
3. Courriel : texte brut intégral et **trois PDF joints**, explicitement annoncés : PDF englobant contenant les deux QPC intégrales, PDF autonome L.299 et PDF autonome L.303. Si une limite de taille empêche ce lot, signaler le blocage sans omission silencieuse.
4. TransfertPro : **quatre fichiers**, soit les trois mêmes PDF et la vidéo P-13 ; conserver chaque preuve de dépôt/réception séparément.
5. Chacun des **trois PDF du courriel** est **identique octet pour octet** à son homologue sur TransfertPro ; comparer les trois paires de SHA-256. Vérifier aussi la concordance intégrale de version des QPC incluses dans le PDF englobant avec les sources de leurs PDF autonomes.
6. URLs GitHub absolues et commit du triptyque identiques dans texte et PDFs ; contrôler les liens et les caractères accentués.
7. Revue juridique et éditoriale de double lecture, absence de nouveau grief électoral, distinctions entre preuve et formalisme L.299.
8. **STOP** : aucun envoi ni publication sans autorisation explicite du requérant.

## État

**CONTRAT DOCUMENTÉ — REALITY TEST NON EXÉCUTÉ SUR FRACTA2**. Les trois PDF de procédure restent à produire. Ne pas annoncer la chaîne comme validée au seul motif que son usage existe déjà pour Suicide Corse.
