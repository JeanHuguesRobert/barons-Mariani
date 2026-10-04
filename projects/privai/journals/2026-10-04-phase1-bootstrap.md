---
title: PrivAI — reprise du 4 octobre 2026
description: Audit de réemploi, formulation institutionnelle retenue, revue adverse et suite de déploiement.
author: Jean Hugues Noël Robert, baron Mariani
affiliation: Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica
date: '2026-10-04'
language: fr
status: working-note
license: CC BY-SA 4.0
document_role: journal
document_kind: resumption-note
visibility: public
lifecycle_state: working
update_policy: UP-DEFAULT-REVIEWED
ai_assisted_by:
- Grok 4.7 — handler, 2026-10-04
provenance:
  origin_type: issue-continuation
  origin_repository: JeanHuguesRobert/barons-Mariani
  origin_ref: https://github.com/JeanHuguesRobert/barons-Mariani/issues/107
  origin_date: '2026-10-04'
---

# Reprise — issue 107 — 4 octobre 2026

Handler : Grok, dans le checkout `C:\tweesic\barons-Mariani`.
Baseline avant cette tranche : `49cb660006d4f1ac781dacf97fc15a2217acf067` (fast-forward depuis `03befd3`, trois commits Capable sans rapport avec PrivAI).
Issue : aucun commentaire antérieur. Le corps du paquet restait l'état de travail.

## Audit de réemploi

| Classe | Quoi | Décision |
| --- | --- | --- |
| GENERIC | Grammaire Livre Vivant ; page statique sans framework, comme Rise & Fall et DIASPORA ; `llms.txt` ; registre d'éditions vide | réemployé |
| PARAMETRIC | `corpus.yml` ; page de contribution ; mentions ; projection `n1-working.yml` | adapté |
| PROJECT-SPECIFIC | Question de souveraineté, sommaire du n°1, tension entre le Livre et l'initiative | écrit comme projection, pas comme doctrine nouvelle |
| MISSING | Profil de Guide `privai` ; DNS ; édition gelée ; Reality Case ; relecture des statuts | laissés ouverts |
| DO NOT REBUILD | Charte, profils, contrats, conformance de `acorsica/privai` ; pile RAG ; authentification | non repris dans ce dépôt |

Le Guide de Rise & Fall appelle `https://cogentia.fractavolta.com` avec un profil. Brancher le même appel sous le nom `privai` sans profil enregistré aurait affiché une capacité absente. La page Guide de cette tranche explique l'écart et n'appelle pas le service.

## Formulation institutionnelle

Sources lues :

- `acorsica/privai` @ `f7fe0c03e718bef1deb6c6f8beb2b3af84e39e55` : les liens ne valent pas portage juridique ; développement dans le périmètre de C.O.R.S.I.C.A. et de l'Institut Mariani ; Cogentia ne s'auto-certifie pas.
- `research/acorsica-institut-mariani.md` : « portage juridique automatique ». Le portage transitoire de cette note vise la préfiguration du fonds Barons Mariani.
- note Cogentia homonyme : « ni portage juridique ».
- `projects/privai/institutional-status.md` et le README du 4 octobre : proposition d'une PrivAI Foundation portée juridiquement par C.O.R.S.I.C.A.

Formulation publique retenue, la plus étroite déjà publiée par l'initiative : périmètre de développement, pas portage juridique. La phrase sur la Foundation reste une candidate non vérifiée sur les statuts. Les notes de juin et de septembre n'ont pas été réécrites.

Contrôle DNS du poste, le 4 octobre 2026 : `privai.acorsica.org` ne résolvait pas. Aucune modification DNS ni serveur.

## Revue adverse

La même main a écrit la projection et cette revue. Ce n'est pas une revue indépendante.

Objections conservées :

1. Trois emplois du nom coexistent : initiative (`acorsica/privai`), protocole de profils cognitifs (*Democratic AI Safety*, §12.2), Livre (ce dossier). Les confondre créerait une organisation imaginaire.
2. Le §13 de `research/livre_vivant.md` ne liste pas encore PrivAI parmi les Livres Vivants. Cette tranche ne l'y a pas ajouté.
3. Plusieurs sources de la thèse sont en anglais. La projection française peut durcir un « may » ou un « hypothesis ». Les claims C1–C7 restent qualifiés dans la projection.
4. L'Autonomie de Capacité est une grammaire politique territoriale. Son usage comme chapitre d'AI Safety est un rapprochement, pas une conséquence déjà écrite.
5. Aucun Reality Case local ne mesure encore une capacité rendue à une personne.
6. Le HTML et le markdown peuvent diverger. Le markdown gagne.
7. `acorsica/institut-mariani` et les statuts n'ont pas été ouverts.

Aucune occurrence utile de `PrivaAI` n'a été trouvée hors la consigne de recherche elle-même.

## Suite

Le prochain pas utile, hors de cette tranche : enregistrer un profil de Guide borné par les sources de ce manifeste, ou geler une édition seulement après revue humaine. Le déploiement du nom demande une autorisation séparée.
