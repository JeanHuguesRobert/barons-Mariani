---
canonical_url: https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/musee-mariani/methodes/notices_famille_etendue.md
title: Notices — famille étendue Mariani et alliances
description: Méthode et feuille de route pour créer des notices généalogiques augmentées, sourcées et évolutives sur la famille Mariani et ses alliances.
author: Jean Hugues Noël Robert, baron Mariani
affiliation: Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica
ai_assisted_by:
  - ChatGPT
date: '2026-09-12'
last_modified_at: '2026-10-07'
version: '0.5'
status: working paper — public research roadmap
language: fr
license: CC BY-SA 4.0
visibility: public
lifecycle_state: working
document_role: source
document_kind: genealogical-research-method
update_policy: UP-DEFAULT-REVIEWED
source_scope:
  - famille Mariani
  - famille de Casabianca
  - famille d’Angelis
  - famille Arrighi de Casanova
  - autres alliances documentées par Meurgey 1933
related_documents:
  - musee-mariani/notes-critiques/preuves-et-incertitudes.md
  - musee-mariani/sources/bibliographie.md
  - musee-mariani/dossiers/louis-thomas-mariani-tahiti.md
  - research/relevement_nom_dangelis.md
provenance:
  origin_type: conversation
  origin_date: '2026-09-12'
  derived_from:
    - échanges Jean Hugues Noël Robert / ChatGPT du 12 septembre 2026
    - note privée de travail /Famille/Mariani/notices_famille_etendue_todo.md
  origin_repository: unknown
  origin_ref: unknown
review:
  status: human-directed publication
  reviewed_by:
    - Jean Hugues Noël Robert
  reviewed_at: '2026-09-12'
classification_source: manual
classification_version: '1'
classification_rule: public-genealogical-research-method
classification_confidence: strong
---


# Notices — famille étendue Mariani / de Casabianca / d’Angelis

## Objet

Créer progressivement une **notice standardisée pour chaque membre documentable de la famille étendue**, en ne réduisant pas la généalogie à un arbre de filiations.

Chaque notice doit pouvoir rendre compte à la fois de la personne, de ses liens familiaux, de sa trajectoire dans le temps et dans l’espace, et du niveau de preuve attaché à chaque information.

Cette méthode prolonge directement la grille critique du Musée Mariani : [`Preuves et incertitudes`](../notes-critiques/preuves-et-incertitudes.md).

## 0 bis. Périmètre extensible

Le périmètre n'est plus limité aux trois branches initiales Mariani / de Casabianca / d’Angelis.

Le dépouillement de Meurgey 1933 démontre que le suivi par les femmes et par changement de patronyme est indispensable. Toute alliance peut donc obtenir un sous-corpus canonique lorsqu'elle devient un objet d'enquête substantiel.

Premier cas ajouté : [Arrighi de Casanova](../arrighi-de-casanova/README.md).

Règle :

```text
alliance ponctuelle
→ simple relation dans le graphe

alliance avec descendance / patrimoine / trajectoire propre significative
→ sous-corpus dédié
```
## 1. Contenu minimal d’une notice

Chaque notice doit distinguer strictement :

- faits établis par sources primaires ;
- sources secondaires ;
- mémoire orale familiale ;
- hypothèses à vérifier ;
- liens avec Corte / Corse / continent ;
- trajectoire patrimoniale, professionnelle, politique ou militaire ;
- sources iconographiques ;
- liens avec les autres membres de la famille ;
- degré de maintien, d’éloignement ou de réactivation du lien corse lorsque cela est documentable.

La notice n’est donc pas seulement une fiche d’identité. Elle doit permettre de reconstruire un **parcours relationnel et territorial**.

## 1 bis. Dimension territoriale et transitions d'ancrage

Pour les branches étudiées dans le chantier [Meurgey 1933 → 2026](../../projects/rise-and-fall/investigation/notes/2026-10-04-meurgey-diaspora-impinzutimentu.md), les notices doivent permettre de suivre des **transitions territoriales** plutôt que de coller une étiquette définitive à une personne.

Champs candidats, à remplir seulement lorsque les sources le permettent :

```yaml
birth_place:
education_places:
career_places:
residence_periods:
departure_from_corsica:
return_to_corsica:
corsican_links:
patrimony_in_corsica:
patrimony_changes:
territorial_state:
territorial_state_period:
territorial_evidence:
```

États de travail :

- **demeuré** : centre de vie documenté en Corse ;
- **parti mais relié** : centre de vie extérieur avec liens corses substantiels documentés ;
- **désancré** : lien matériel ou territorial devenu faible ou principalement mémoriel ;
- **revenu / réancré** : retour ou reconstruction d'un ancrage effectif ;
- **inconnu** : documentation insuffisante.

Ces catégories sont analytiques et révisables. Elles ne constituent ni un jugement de valeur ni une identité culturelle. Le terme `impinzutimentu`, utilisé dans le chantier transversal comme étiquette heuristique, doit rester séparé de ces champs factuels tant que son emploi précis et son histoire lexicale ne sont pas stabilisés.

Pour une personne vivante, ne publier aucune adresse privée ni localisation fine obtenue par recoupement indirect. La localisation publique doit rester au niveau minimal nécessaire à la question de recherche.

## 2. Premier cas pilote : Albert Mariani et la génération Hyacinthe

Premier cas à traiter : **Albert Antoine Joseph Louis Mariani (1872–1963)**, avec remontée à son père **Hyacinthe Joseph Louis Mariani (1827–1894)**.

Question de recherche :

> Le déplacement durable du centre de gravité familial hors de Corse commence-t-il dès la génération d’Hyacinthe, plutôt qu’avec Albert lui-même ?

Cette hypothèse doit être testée par les lieux de naissance, résidence, mariage, carrière et décès, mais aussi par les réseaux familiaux, les actes patrimoniaux, la correspondance et les traces de relation effective avec Corte.

## 3. Règle probatoire

Ne pas transformer un souvenir familial ou une inférence sociologique en fait biographique sans source.

Les souvenirs doivent cependant être **conservés comme pistes de recherche**, avec leur provenance et leur statut. Une mémoire familiale fragile peut conduire à une pièce décisive ; elle ne doit ni être effacée ni être promue abusivement au rang de preuve.

La grille générale est celle de [`Preuves et incertitudes`](../notes-critiques/preuves-et-incertitudes.md) : fait établi, fait probable, tradition familiale ou généalogique, hypothèse historique, interprétation.

Le dossier [`Relèvement du nom d’Angelis`](../../research/relevement_nom_dangelis.md) constitue déjà un exemple concret de cette séparation entre actes, sources secondaires, témoignages familiaux et maillons de filiation à fermer.

## 4. Contexte culturel corse

Dans le cas corse, cette approche est particulièrement pertinente : l’attachement aux lignées, aux parentés, aux villages d’origine et à la mémoire familiale constitue un objet historique et ethnographique bien attesté.

Ce constat général doit néanmoins être documenté explicitement avant tout usage académique fort. Une notice familiale ne doit jamais transformer un trait culturel général en explication automatique d’un comportement individuel.

La question du **lien à la Corse** doit donc être étudiée comme une variable biographique : maintien, éloignement, déplacement du centre de gravité, retour, réactivation ou recomposition selon les générations.

## 5. Ce que l’IA change dans la pratique généalogique

La généalogie ne doit plus être réduite à un arbre statique.

Avec l’IA, elle peut devenir une **enquête vivante** reliant :

```text
personnes
+ filiations
+ lieux
+ périodes
+ métiers
+ alliances
+ patrimoine
+ correspondances
+ migrations
+ mémoire orale
+ sources iconographiques
+ degré de preuve
```

L’IA permet notamment :

- de rapprocher des variantes de noms et de dates ;
- de repérer des incohérences entre sources ;
- de relier des carrières à des lieux et institutions ;
- de suivre les déplacements du centre de gravité d’une branche familiale ;
- de rechercher les documents qui manquent pour fermer une chaîne probatoire ;
- de maintenir une carte explicite des incertitudes et des pistes ouvertes.

Mais elle ne diminue jamais l’exigence de preuve.

> **L’IA augmente la capacité de recoupement ; elle n’abaisse pas le seuil de preuve.**

Une hypothèse relationnelle ou biographique produite par l’IA reste une hypothèse tant qu’elle n’est pas fermée par les sources appropriées.

## 6. Architecture documentaire proposée

À mesure que les notices seront créées, le sous-corpus pourra évoluer vers une structure de ce type :

```text
musee-mariani/
  personnes/
    README.md
    mariani-albert-antoine-joseph-louis.md
    mariani-hyacinthe-joseph-louis.md
    mariani-louis-thomas.md
    ...
```

Chaque notice individuelle devra renvoyer :

- aux personnes directement liées ;
- aux sources primaires correspondantes ;
- aux dossiers thématiques pertinents ;
- aux hypothèses ou vérifications encore ouvertes.

Le dossier [`Louis-Thomas Mariani et Tahiti`](../dossiers/louis-thomas-mariani-tahiti.md) constitue déjà un prototype partiel de notice critique centrée sur une personne et une tradition familiale à vérifier.

## 7. Sources et enrichissement continu

La liste de travail [`Bibliographie et sources à dépouiller`](../sources/bibliographie.md) fournit le réservoir documentaire général du Musée Mariani.

Les notices de personnes doivent progressivement transformer cette bibliographie générale en un réseau de sources attachées à des affirmations précises.

Le principe est :

```text
source générale
→ personne concernée
→ affirmation précise
→ niveau de preuve
→ source primaire recherchée ou retrouvée
→ correction éventuelle
```

## 8. Principe de publication

Une notice publique ne doit pas publier automatiquement tout ce qui existe dans la mémoire familiale privée.

Avant publication, distinguer :

```text
mémoire privée utile à l’enquête
≠
fait biographique publiable
```

Les informations concernant des personnes vivantes, des conflits familiaux, des successions ou des appréciations personnelles doivent faire l’objet d’une prudence supplémentaire.

Le but du sous-corpus n’est pas de fabriquer une légende familiale, mais de produire une **généalogie inspectable, corrigible et documentée**, capable de montrer aussi bien les continuités que les ruptures.
