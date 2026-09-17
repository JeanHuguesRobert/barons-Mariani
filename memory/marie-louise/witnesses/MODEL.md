---
title: "Marie-Louise — modèle conceptuel du registre des témoins potentiels"
status: working-paper
date: 2026-09-17
document_role: research
document_kind: data-model
visibility: public
lifecycle_state: active
update_policy: UP-DEFAULT-REVIEWED
review:
  status: unreviewed
  reviewed_by: []
---

# Modèle conceptuel du registre des témoins potentiels

## 1. Position

Ce document définit un modèle conceptuel minimal pour le registre des témoins potentiels de Marie-Louise.

Il ne définit pas une ontologie relationnelle finale et n'impose pas de schéma SQL. La représentation actuelle peut rester distribuée dans des fichiers Markdown et d'autres objets du Corpus tant que cela reste le support le plus simple et utile.

Le modèle doit permettre une migration ou projection ultérieure vers SQL sans exiger de réécriture conceptuelle majeure.

## 2. Objets principaux

### Witness

Représente une personne physique, une personne morale ou une personne encore partiellement identifiée susceptible d'apporter une information, une trace, un document ou un chemin vers d'autres témoins.

Champs conceptuels minimaux :

- identifiant stable ;
- type ;
- nom ou désignation provisoire ;
- statut d'identification ;
- périodes pertinentes ;
- contextes ;
- motifs de sollicitation ;
- catégories de relation ;
- sources de découverte ;
- état de traitement.

### ContactMethod

Représente un moyen de joindre ou retrouver un témoin.

Champs conceptuels :

- identifiant ;
- témoin concerné ;
- type de canal ;
- valeur ou référence protégée ;
- source ;
- date d'observation ;
- statut de validité ;
- dernière vérification ;
- caractère direct ou indirect ;
- contraintes de confidentialité.

Le modèle doit permettre d'indiquer qu'un canal existe sans publier nécessairement sa valeur.

### Source

Représente la provenance d'une affirmation ou d'une piste.

Exemples :

- message Gmail ;
- fichier du Corpus ;
- document administratif ;
- photographie ;
- témoignage ;
- source publique ;
- assertion de Jean Hugues Robert ;
- résultat de recherche négatif borné.

Une source n'est pas automatiquement un fait.

### Relationship

Représente une relation entre deux objets du registre ou entre un témoin et un contexte.

Exemples :

- `knew` ;
- `lived_with` ;
- `studied_with` ;
- `worked_with` ;
- `handled_case_for` ;
- `can_introduce_to` ;
- `member_of` ;
- `possible_same_person_as` ;
- `witness_for_event` ;
- `holds_document_about`.

Chaque relation peut avoir :

- une période ;
- une source ;
- un niveau de certitude ;
- une note factuelle ;
- une ou plusieurs contradictions.

### Outreach

Représente une tentative de sollicitation.

Champs conceptuels :

- identifiant ;
- témoin ;
- date ;
- canal ;
- objet de la sollicitation ;
- campagne éventuelle ;
- statut ;
- réponse ou absence de réponse ;
- suivi ;
- provenance de la trace de contact.

Une personne peut faire l'objet de plusieurs sollicitations au cours du temps.

### Contribution

Représente ce qu'une sollicitation ou une source apporte effectivement à l'enquête.

Exemples :

- témoignage ;
- document ;
- photographie ;
- identification d'un tiers ;
- correction ;
- contradiction ;
- confirmation ;
- information négative bornée.

Une Contribution doit rester liée à sa Source et ne devient pas automatiquement un fait stabilisé.

### KnowledgeGap

Représente une lacune ou question ouverte du futur Digital Twin.

Champs conceptuels :

- identifiant stable ;
- question ;
- période ou contexte ;
- état ;
- éléments déjà connus ;
- éléments inconnus ;
- témoins candidats ;
- sources candidates ;
- contributions pertinentes ;
- date de dernière réévaluation.

Exemple :

```yaml
id: gap:nantes:colocation-2019
question: "Qui vivait avec Marie-Louise à Nantes au printemps 2019 ?"
status: partial
candidate_witnesses:
  - witness:person:camille-gerard
  - witness:unknown:juliette-nantes
```

## 3. Identifiants stables

Les identifiants ne doivent pas dépendre du nom de fichier.

Exemples :

```text
witness:person:camille-gerard
witness:org:beaux-arts-nantes
witness:unknown:juliette-nantes
contact:...
source:...
outreach:...
contribution:...
gap:...
```

Une stratégie plus opaque ou numérique pourra être adoptée ultérieurement si les collisions, renommages ou contraintes de confidentialité le justifient.

Le principe à préserver est la stabilité référentielle, pas une syntaxe particulière.

## 4. États minimaux

### Identification

```text
unknown
partial
probable
confirmed
```

### Joignabilité

```text
unknown
to_find
partial
known
obsolete
unreachable
```

### Pertinence documentaire

La pertinence doit être décrite par des motifs et des liens vers les Knowledge Gaps plutôt que réduite trop tôt à un score unique.

Lorsque des priorités opérationnelles sont nécessaires, elles doivent être présentées comme ordre de recherche ou de sollicitation, non comme jugement sur la crédibilité personnelle.

### Outreach

```text
to_prepare
ready
contacted
response_received
no_response
refused
invalid_channel
follow_up_possible
closed
```

## 5. Relations et cardinalités

Le modèle ne présume pas des cardinalités rigides, mais doit supporter au minimum :

```text
Witness 1..n ContactMethod
Witness n..n Witness via Relationship
Witness n..n Source
Witness n..n KnowledgeGap
Witness 1..n Outreach
Outreach 0..n Contribution
Contribution 1..n Source
KnowledgeGap n..n Contribution
```

Une organisation est un Witness de type `organization`, afin d'éviter une séparation prématurée qui compliquerait inutilement les chemins de contact et les relations.

## 6. Assertions et contradictions

Le modèle doit pouvoir conserver plusieurs assertions incompatibles sans forcer une résolution prématurée.

Une information importante doit pouvoir être associée à :

- une source ;
- un auteur ou émetteur lorsque connu ;
- une date ;
- un contexte ;
- un statut épistémique ;
- une éventuelle assertion contradictoire.

Le Digital Twin peut représenter plusieurs versions concurrentes d'un même événement jusqu'à ce qu'une qualification suffisante soit possible.

## 7. Projections

Les fichiers Markdown actuels sont des projections humaines du modèle.

D'autres projections pourront apparaître :

- YAML ;
- index générés ;
- graphes ;
- vue chronologique ;
- vue par Knowledge Gap ;
- base SQL ;
- API ou interface Cogentia.

Aucune projection ne doit détruire une information présente dans une représentation plus riche.

## 8. Optimistic Schema

Ne pas définir à l'avance toutes les colonnes, tables ou contraintes d'un futur schéma relationnel.

Règle :

```text
préserver un objet riche et traçable
→ projeter seulement les propriétés actuellement utiles
→ observer les requêtes et frictions réelles
→ promouvoir en structure relationnelle les propriétés qui deviennent réellement structurantes
```

Une future projection SQL doit rester compatible avec les données et traces qui ne sont pas encore promues dans le schéma relationnel.

## 9. Compatibilité avec Packet-Backed Projection

Lorsque le registre sera projeté vers SQL ou un autre stockage structuré, le Pattern Cogentia `Packet-Backed Projection` peut servir de référence : la projection relationnelle ne doit pas devenir l'unique détenteur de la richesse sémantique et historique.

Principe :

```text
Packet / objet riche = enveloppe de vérité et provenance
projection structurée = vue opérationnelle minimale
```

Une écriture via une projection structurée ne doit modifier que les propriétés qu'elle représente et doit préserver les informations hors projection.

## 10. Optimistic Locking

Les mises à jour doivent être conçues pour la collaboration incrémentale entre humains et agents.

Séquence minimale :

```text
1. lire l'objet ou la révision courante ;
2. conserver l'identité de cette révision lorsque l'interface le permet ;
3. calculer le plus petit changement suffisant ;
4. appliquer uniquement ce changement ;
5. si la précondition de version n'est plus vraie, ne pas écraser ;
6. relire l'état courant ;
7. réconcilier ou recalculer ;
8. réessayer avec le plus petit périmètre suffisant ;
9. signaler les conflits non résolus.
```

Pour les fichiers Git, le commit, le diff et l'historique fournissent une partie de cette mécanique. Pour SQL, utiliser des versions, timestamps, hashes ou conditions `WHERE` appropriées lorsque la projection le justifie.

## 11. Évolution du modèle

Ce modèle est une base de travail volontairement minimale.

Ajouter un nouvel objet, champ ou statut seulement lorsqu'un besoin concret apparaît suffisamment souvent pour que la spécialisation améliore réellement :

- la recherche ;
- la déduplication ;
- la traçabilité ;
- la collaboration ;
- la protection de la confidentialité ;
- la réduction des Knowledge Gaps ;
- l'intégration au Digital Twin.

Le changement de modèle doit être traçable et corrigeable. Une structure antérieure imparfaite n'est pas une erreur à effacer : elle constitue une étape de l'apprentissage du Corpus.
