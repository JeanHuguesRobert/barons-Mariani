---
title: "Marie-Louise — réception gouvernée des contributions"
author: Jean Hugues Noël Robert
status: working-paper
date: '2026-09-18'
document_role: operational
document_kind: intake-protocol
visibility: public
lifecycle_state: active
update_policy: UP-DEFAULT-REVIEWED
license: CC BY-SA 4.0
affiliation: Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica
language: fr
review:
  status: unreviewed
  reviewed_by: []
provenance:
  origin_type: repository
  origin_repository: JeanHuguesRobert/barons-Mariani
  origin_ref: memory/marie-louise/witnesses/METHOD.md
  origin_date: '2026-09-18'
  derived_from:
    - memory/marie-louise/witnesses/METHOD.md
    - projects/suicide-corse/manuscript/17-appel-a-temoignages.md
---

# Réception gouvernée des contributions

Ce protocole gouverne la réception des réponses à l'appel à témoignages de
*Suicide Corse*. Il ne constitue ni un dépôt de témoignages, ni une autorisation
de publier une contribution.

## Frontière publique / privée

Le dépôt `barons-Mariani` est public. Il ne doit donc contenir ni message reçu,
ni pièce jointe, ni coordonnée privée, ni identifiant de boîte mail, ni nom d'un
contributeur non déjà publié avec un motif légitime.

Une contribution reçue est conservée dans un espace privé autorisé. Le présent
document ne permet que d'en conserver publiquement la méthode, jamais le
contenu ou les métadonnées identifiantes.

## Emplacement privé d'intake (Phase 1)

Le registre privé d'intake vit dans le dépôt privé `JeanHuguesRobert/registre-mariani`,
sous `twin/marie-louise-robert/intake/` (index `registry.yml` + une fiche par
contribution dans `fiches/<intake_id>.yml`). L'outil de création assisté est
`scripts/intake/create-intake.mjs` dans ce même dépôt privé. Ce document
public ne référence que l'emplacement et la méthode, jamais son contenu.

## Réception minimale

À l'arrivée d'une contribution, créer dans le registre privé un identifiant
interne non signifiant. Enregistrer au minimum :

```text
intake_id
received_at
channel
source_object_private_reference
initial_confidentiality = confidential
initial_qualification = unreviewed
publication_consent = unknown
```

`intake_id` ne doit pas contenir le nom, l'adresse, le numéro de téléphone ou
un autre identifiant personnel du contributeur.

Conserver le message ou la pièce d'origine sans le réécrire. S'il est nécessaire
de créer une transcription, une note ou une extraction, la relier à l'objet
source privé en distinguant clairement l'original de la dérivation.

## Quatre décisions distinctes

```text
réception
≠ conservation
≠ exploitation dans l'enquête
≠ publication
```

La transmission ne vaut pas consentement à une citation, à une anonymisation
publique, à un contact ultérieur, ni à une publication. Toute demande ou tout
accord doit être daté, attribué, limité par son objet et révisable lorsque la
personne concernée le demande.

## Qualification initiale

Avant toute utilisation, distinguer au moins :

- document ou trace matérielle ;
- parole directe attribuée ;
- témoignage direct ;
- information rapportée par un tiers ;
- souvenir reconstruit ;
- interprétation ;
- hypothèse ;
- information insuffisamment qualifiable.

Une contribution peut contredire une trace déjà connue. Elle ne devient pas
pour autant un fait stabilisé, et elle ne doit pas être rejetée parce qu'elle
contrarie l'hypothèse de travail.

## Traitement et sécurité

Ne pas ouvrir, relayer ou publier mécaniquement une pièce jointe. Préserver son
origine, inspecter son type et son intégrité dans un environnement approprié,
et limiter son accès aux personnes autorisées. Ne pas recopier des éléments
sensibles dans des issues, commits ou commentaires publics.

Un accusé de réception éventuel doit rester sobre : il confirme la réception,
non l'authenticité, l'usage futur, la publication, ni une réponse dans un délai
déterminé.

## Passage éventuel vers le Corpus public

Une information ne peut apparaître dans une projection publique qu'après une
décision séparée qui documente :

1. le besoin éditorial ou documentaire ;
2. le niveau de qualification atteint ;
3. les risques pour les personnes vivantes et la vie privée ;
4. la forme de minimisation, anonymisation ou attribution retenue ;
5. le consentement applicable, s'il est requis ;
6. le relecteur humain responsable de la décision.

En l'absence de cette décision, l'information demeure privée et `unreviewed`.
