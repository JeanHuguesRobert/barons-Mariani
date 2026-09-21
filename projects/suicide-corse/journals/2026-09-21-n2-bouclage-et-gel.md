---
title: "Journal de campagne — numéro 2, bouclage et gel du 21 septembre 2026"
author: "Jean Hugues Noël Robert"
date: "2026-09-21"
status: published
language: fr
license: CC BY-SA 4.0
document_role: source
document_kind: journal-entry
visibility: public
lifecycle_state: working
canonical_url: https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/suicide-corse/journals/2026-09-21-n2-bouclage-et-gel.md
update_policy: UP-DEFAULT-REVIEWED
provenance:
  origin_type: generated
  origin_repository: JeanHuguesRobert/barons-Mariani
  origin_ref: unknown
  origin_date: "2026-09-21"
  derived_from:
    - "GitHub issue #81"
    - "GitHub issue #83"
    - projects/suicide-corse/editions/index.md
    - projects/suicide-corse/editions/2026-09-20-n2-freeze.md
    - projects/suicide-corse/manuscript/16-continuations.md
review:
  status: unreviewed
  reviewed_by: []
affiliation: Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica
---


# Journal de campagne contre l'impossible — 21 septembre 2026

## D'où partions-nous ?

Le repère précédent est le numéro spécial anniversaire, gelé le 18 septembre
2026 ([`editions/2026-09-17-freeze.md`](../editions/2026-09-17-freeze.md)).
Le chapitre 16 (« Continuations ») listait alors, entre autres, une revue
contradictoire indépendante non encore menée, un rythme hebdomadaire à
établir, et une candidature de réintégration de Marie-Louise à la Villa Arson
encore non totalement stabilisée dans son statut documentaire.

## Qu'est-ce qui est entré dans le Corpus ?

Une quarantaine de commits ont porté le Corpus du snapshot du 17 septembre
(`5ffa320`) au commit de gel du numéro 2 (`da5ff97`), sous le pilotage des
issues [#81](https://github.com/JeanHuguesRobert/barons-Mariani/issues/81) et
[#83](https://github.com/JeanHuguesRobert/barons-Mariani/issues/83) :
chronologie et annuaire des témoins de Marie-Louise étendus, le lien avec le
« Reality Case » sénatorial ajouté à l'architecture, un ours (masthead)
rédigé, une « double hélice » et des couches magazine encodées pour la
structure éditoriale du numéro, un writing brief puis une projection dédiés
au numéro 2, et les décisions éditoriales D1 à D9 formalisées et propagées
dans le brief.

## Qu'avons-nous appris ?

La percée principale de ce numéro est doctrinale plutôt que factuelle :
**D9**, la règle de gradation des contrefactuels forts. Elle tranche une
tension que le numéro 1 laissait ouverte — comment traiter un possible fermé
(le rejet de la candidature de réintégration à la Villa Arson) sans tomber
dans deux excès symétriques : la causalité certaine du suicide, ou
l'aplatissement en un `UNKNOWN` uniforme qui neutraliserait la question.
Appliquée au cas Marie-Louise / Villa Arson, elle permet de dire à la fois
que le retour à la Villa Arson en cas d'admission était très probable, que la
suite des mois aurait été profondément modifiée, et que l'hypothèse d'une
probabilité de survie plus élevée reste une hypothèse forte et légitime à
examiner — jamais un fait établi.

## Qu'avons-nous corrigé ?

Deux corrections mécaniques, documentées dans la
[déclaration de gel du numéro 2](../editions/2026-09-20-n2-freeze.md) :

- `16-continuations.md` décrivait encore la candidature de réintégration à la
  Villa Arson comme entièrement `UNKNOWN`, et l'édition anniversaire comme
  une préversion en attente d'un gel déjà décidé le 18 septembre. Les deux
  formulations ont été mises à jour sans rouvrir D1–D9 ni le snapshot gelé
  (commit `230b6ad`).
- `corpus.yml` référençait sept sources par un chemin de répertoire ; le
  renderer Ubikia ne lit que des fichiers et échouait (`EISDIR`) avant tout
  rendu. Chaque entrée a été repointée vers le fichier réel qu'elle contient
  déjà, sans changement de contenu source (commit `f061abb`). Le bug
  renderer lui-même a été signalé en amont :
  [ubikia#33](https://github.com/JeanHuguesRobert/ubikia/issues/33).

Côté surface de publication (dépôt
[`JeanHuguesRobert/suicide-corse`](https://github.com/JeanHuguesRobert/suicide-corse),
distinct de ce Corpus source), la page d'accueil affichait encore le numéro 2
comme « en rédaction » alors qu'il était déjà rendu et promu ; elle a été
corrigée, réordonnée pour présenter la dernière édition en premier, et
reformulée en langage accessible plutôt que technique. Des mentions légales
complètes (éditeur, hébergeur Oracle France SAS vérifié par registre public,
droit de réponse, RGPD) et un jeu de fichiers de référencement (`robots.txt`,
`sitemap.xml`, `llms.txt`) ont été ajoutés sans toucher aux éditions gelées
elles-mêmes.

## Qu'a répondu le Réel ?

Rien encore de matériel : les six sondes préparées (Sylvain Lizon, Damien
Ruvet, Villa Arson, Céline Christmann Brillais, Maëva Guillery, Maéva Lecoq)
restent des continuations post-publication, non envoyées à la date de ce
journal, et ne bloquaient pas le gel du numéro 2. La date et le motif exacts
du rejet de la candidature à la Villa Arson, ainsi que la confirmation
institutionnelle primaire de ce rejet, restent `UNKNOWN`. Aucune revue
contradictoire indépendante n'a encore eu lieu.

## Qu'est-ce qui reste UNKNOWN ?

Le chapitre 16 du manuscrit reste la liste de référence, à jour à cette
date : décryptage de 2009 introuvable, note testamentaire rapportée non
authentifiée, été 2024 non reconstruit semaine par semaine, date/motif/effet
exacts du rejet Villa Arson, motivation exacte du départ pour Nantes en
2017, registre conflictuel de 2018 et 2021 non traité, voix directe de
Marie-Louise sur la Corse et la politique encore mince, œuvres et artefacts
non retrouvés, stage de l'été 2019 non documenté, résultat de l'Act
territorial `#1755-01` non exécuté, mécanisme exact du rejet administratif
du 27 septembre 2024.

## Qu'est-ce qui devient possible ?

Le correctif renderer profite à tout projet du Corpus utilisant des sources
en répertoire optionnelles, pas seulement à *Suicide Corse*. Le jeu de
fichiers de référencement côté publication (`llms.txt` notamment) ouvre la
possibilité que des agents tiers citant ce travail préservent la gradation
épistémique du texte plutôt que de l'aplatir. Cette entrée valide aussi, pour
la deuxième fois, que le contrat `journal-weekly.yml` (v1) peut produire une
entrée fidèle à sa fonction sans être un simple changelog Git.

## Qu'avons-nous volontairement différé ?

Restent des continuations explicites, non des oublis : la revue
contradictoire indépendante par un tiers ; l'envoi effectif des six sondes
préparées ; l'établissement réel du rythme hebdomadaire (la prochaine
campagne, ci-dessous) ; le traitement encadré du registre conflictuel de
2018–2021 ; les trois proverbes réservés à haute sensibilité ; l'extension du
test d'invariance capacitaire au-delà des deux cas actuellement appariés.

## Prochaine campagne

Front prioritaire : amorcer effectivement la cadence hebdomadaire du lundi
matin annoncée ici, sans figer par avance le contenu ou le titre d'un
numéro 3 — ce numéro 2 n'a lui-même hérité ni du sommaire ni de l'ordre du
numéro 1. Front documentaire prioritaire : obtenir la confirmation
institutionnelle primaire du rejet de la candidature Villa Arson, seule
pièce manquante pour clore cette Continuation précise sans en forcer le
statut.
