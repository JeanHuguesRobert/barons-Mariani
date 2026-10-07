---
title: "Sénatoriales Haute-Corse 2026 — manifeste du paquet de dépôt"
author: "Jean Hugues Noël Robert"
date: "2026-10-07"
status: "pre-filing — materialization control"
language: "fr"
document_role: "operational"
document_kind: "filing-package-manifest"
visibility: "public"
lifecycle_state: "active"
related:
  - "filing-package-2026-10-07.yml"
  - "requete-conseil-constitutionnel.md"
  - "bordereau-pieces-requete-conseil-constitutionnel.md"
---

# Manifeste du paquet de dépôt

## 1. Noyau documentaire

| Objet | Version courante | État |
|---|---|---|
| Requête | v0.30 — chemin canonique `requete-conseil-constitutionnel.md` | candidate de dépôt ; non déposée ; gel matériel encore requis |
| Bordereau | v0.12 | cohérent jusqu’à P-46 ; non déposé |
| Annexe chronologique | v0.1 évolutive | **à annexer au paquet de requête** ; geler au moment du dépôt |
| Annexe documentation | v0.1 évolutive | **à annexer** comme couche pédagogique grand public / expert ; distincte des pièces P-xx |
| Inventaire probatoire | v1.8 | outil interne ; ne pas annexer par défaut |
| Checklist | v0.51 | outil interne ; ne pas annexer par défaut |

## 1 bis. Annexe chronologique obligatoire

Le paquet doit comprendre `investigation/annexe-chronologie-detaillee-requete-cc-2026-10-07.md` sous une représentation figée et lisible.

Cette annexe doit être gelée **au même instant logique** que la requête et le bordereau. Toute évolution postérieure reste dans le Corpus mais ne doit pas être confondue avec la chronologie effectivement remise.

## 1 ter. Documentation grand public / experts

Le paquet comprend également :
`investigation/annexe-documentation-double-lecture-2026-10-07.md`.

Cette annexe n'est pas une preuve primaire P-xx. Elle explique le dossier selon deux niveaux cohérents :
- grand public : narration, contexte, concepts, finalités et enchaînement des actes ;
- experts : compression référencée, textes, jurisprudence, pièces et qualifications.

L'audit historique `../reviews/audit-double-lecture-requete-v0.23-2026-10-07.md` conclut **PASS** pour la v0.23 sur la double lecture et la séparation data plane / control plane. La requête canonique a depuis évolué jusqu'à la v0.30 ; cet audit reste une trace de contrôle antérieure et ne vaut pas, à lui seul, certification intégrale de la v0.30. Le blocage restant est notamment matériel : pièces, concordance, pagination, SHA-256, gel et preuve de réception.

## 2. Production A proposée

Les pièces actuellement classées **A — production proposée** dans le bordereau sont :

~~~text
P-04 P-05 P-06
P-09 P-10 P-11 P-12 P-13 P-14 P-15 P-16 P-17
P-19 P-20 P-22
P-27
P-29 P-30 P-31 P-32 P-33
P-39 P-40
P-44 P-45
~~~

Statut de ce manifeste :

> la présence d'une pièce dans cette liste signifie qu'elle est **candidate prioritaire à la production** ; elle ne certifie pas encore que son fichier final, sa lisibilité, son occultation, sa pagination ou son impression ont été contrôlés.

## 3. Pièces à arbitrer / minimiser

- **P-18** : sensible ; produire seulement si nécessaire à l'argument d'accessibilité, avec minimisation.
- **P-41** : soutien contextuel ; après vérification des principales URLs et affirmations, **ne pas joindre par défaut** sauf décision expresse de soutenir la branche influence.
- **P-42** : diligence Défenseur des droits ; réserve/soutien, pas nécessaire au noyau de recevabilité.
- **P-43** : correspondance privée ; ne produire que les messages strictement nécessaires, sous forme native ou lisible, avec occultation des données non nécessaires.

### P-45 — chaîne intégrale de courriels

À produire comme pièce A composite :
- P-45.a — courriel du 26/09 ;
- P-45.b — courriel du 28/09 à la Sous-préfecture de Corte ;
- P-45.c — courriel intégral du 01/10 ;
- P-45.d — courriel intégral du 02/10.

Pour chacun : représentation lisible complète + en-têtes utiles + export natif si possible + SHA-256 du fichier produit.

Index public : `investigation/sources/chaine-silence-etat-modalites-depot-2026-09-26-10-02.md`.

## 4. Chaîne TA

Index de lecture : `investigation/chaine-ta-p29-p33-2026-10-06.md`.

La séquence P-29 à P-33 doit être matérialisée comme une chaîne intelligible :

~~~text
P-29 — 16/09 demande d'inventaire / vérifications
P-30 — 16/09 réponse du greffe
P-31 — 21/09 nouvelle réponse / disponibilité annoncée
P-32 — 25/09 six questions résiduelles
P-33 — 01/10 refus de commentaires complémentaires + invitation au CC
~~~

La requête doit distinguer :

- demande établie ;
- réponse reçue ;
- document non communiqué ;
- absence de réponse retrouvée ;
- absence de document prouvée, qui est une proposition plus forte et ne doit pas être inférée sans source.

## 4 bis. Paquet électronique canonique

Voir `note-depot-dematerialise-requete-cc-2026-10-07.md`.

Le paquet numérique gelé doit permettre de reconstruire exactement le data plane remis :
- fichiers PDF ;
- natifs utiles ;
- manifeste ;
- SHA-256 ;
- empreinte de l'archive globale ;
- date/heure de gel ;
- copie EML/MIME des envois électroniques ;
- AR/AE/DSN reçus.

Le paquet papier et le paquet électronique doivent correspondre au même état logique de la requête.



## 4 ter. Contrat machine d'assemblage et Release immuable

Le contrat machine courant est :

`filing-package-2026-10-07.yml`

Il est interprété par l'outil générique Ubikia `filing-package`. Le contrat versionne **l'ordre, les sources, les attentes de matérialisation et l'identité de l'artefact final** ; les PDF intermédiaires restent hors Git.

Invariant de production :

~~~text
sources versionnées + contrat versionné
→ builds locaux jetables
→ aucun PDF candidat dans Git
→ validation d'un seul candidat
→ GitHub Release en brouillon
→ upload + retéléchargement + égalité SHA-256
→ publication séparée
→ Release immuable
~~~

Release cible :

- dépôt : `JeanHuguesRobert/barons-Mariani` ;
- tag : `senatoriales-2026-cc-depot-2026-10-07` ;
- asset : `requete-conseil-constitutionnel-haute-corse-2026.pdf` ;
- exigence : **Immutable Releases activé** ; publication seulement après validation humaine terminale.

Le `plan` doit échouer tant qu'une pièce requise n'a pas de fichier final matérialisé. Une ligne de bordereau ne vaut jamais, à elle seule, matérialisation de la pièce.

## 5. Contrôle final obligatoire

Pour chaque pièce effectivement annexée, renseigner avant gel :

| N° | fichier / original | pages | lisible | occultation | annexé | SHA si utile |
|---|---|---:|---|---|---|---|
| P-xx | À renseigner | — | [ ] | [ ] | [ ] | — |

Ce tableau doit être remplacé ou complété par l'état réel au moment du gel.

## 6. Invariant

~~~text
Corpus source
≠ bordereau candidat
≠ paquet matériel
≠ paquet effectivement remis
~~~

Le post-filing snapshot devra identifier le quatrième objet sans ambiguïté.
