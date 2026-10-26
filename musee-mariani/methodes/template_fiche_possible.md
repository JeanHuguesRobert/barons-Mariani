---
canonical_url: https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/musee-mariani/methodes/template_fiche_possible.md
author: Jean Hugues Noël Robert, baron Mariani
affiliation: Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica
license: CC BY-SA 4.0
title: Gabarit de fiche de possible
subtitle: Modèle d'instruction d'un atelier du Musée Mariani des Possibles
date: '2026-06-27'
version: '0.3'
status: draft
document_role: source
document_kind: fiche-template
visibility: public
lifecycle_state: working
related_documents:
  - musee-mariani/doctrine_musee_mariani_des_possibles.md
  - musee-mariani/methodes/indice_friction_administrative.md
  - musee-mariani/methodes/indice_capacite_retrouvee.md
  - musee-mariani/methodes/grille_remise_en_service.md
language: fr
update_policy: UP-DEFAULT-REVIEWED
review:
  status: unreviewed
  reviewed_by: []
provenance:
  origin_type: unknown
  origin_repository: unknown
  origin_ref: unknown
  origin_date: unknown
  derived_from: []
---


# Gabarit de fiche de possible

## Modèle d'instruction d'un atelier du Musée Mariani des Possibles

> **Statut.** Première version (v0.1). Ce gabarit fixe la forme commune à toutes les fiches d'atelier. Chaque atelier en est une instance ; tant qu'une fiche n'a pas été instruite, ses rubriques portent la mention *à instruire*.

Ce document est la clé de voûte méthodologique du Musée Mariani des Possibles. Il décrit la forme que prend toute enquête sur un possible — qu'il s'agisse de distiller, de presser une huile, de cuire un pain ou d'accueillir des visiteurs sous tente. La doctrine en a posé le principe (§30) ; ce gabarit en donne la version travaillée, avec, pour chaque rubrique, ce qu'elle doit contenir et l'erreur qu'elle sert à éviter.

Une fiche de possible n'est pas un dossier administratif de plus. C'est l'unité de base du corpus : un cas autonome, daté, sourcé, transmissible, que d'autres pourront reprendre sans repartir de zéro. Elle se lit à deux niveaux — une version visiteur, claire et brève, et une version corpus, complète et justifiée.

---

## Comment remplir une fiche

Chaque rubrique répond à une question précise. On ne cherche pas l'exhaustivité du premier coup : une fiche de v0.1 a le droit d'être lacunaire, à condition que ses lacunes soient nommées. La règle est de distinguer toujours quatre choses — ce qui est établi, ce qui est probable, ce qui reste à vérifier, ce que cela rend pensable — et de ne jamais présenter une hypothèse comme un fait.

Les rubriques juridiques, en particulier, ne tranchent pas le droit : elles l'exposent, repèrent les points de friction, et désignent ce qui devra relever de l'administration ou du juge. Lorsqu'une fiche d'atelier rencontre une vraie difficulté de droit, elle ouvre un dossier juridique distinct selon le gabarit dédié, et s'y réfère.

---

## Structure de la fiche

```text
# Atelier : [nom]

## Résumé public
Trois à six phrases lisibles par tout visiteur. Ce que l'on montre, ce que
l'on apprend, ce que l'atelier permet de comprendre.

## Question de possibilité
La question centrale, formulée comme une enquête : « Peut-on, aujourd'hui,
dans un écomusée, faire X — et à quelles conditions ? »

## Hypothèse initiale
La réponse provisoire de départ, assumée comme révisable.

## Ce qui était possible historiquement
Le geste, l'activité, son contexte technique, social et économique passé.

## Ce qui est techniquement possible aujourd'hui
L'état de l'art, les outils, les matériaux, les contraintes physiques.

## Ce qui est juridiquement possible aujourd'hui
Le cadre applicable, sans trancher : régimes, seuils, statuts, distinctions
décisives (démonstration / production / vente). Renvoyer au dossier juridique
si une difficulté réelle apparaît.

## Ce qui est économiquement possible aujourd'hui
Coûts, revenus possibles, seuils de viabilité, modèle d'exploitation.

## Ce qui est pédagogiquement possible aujourd'hui
Ce que l'atelier transmet, à quels publics, sous quelle forme.

## Empêchements identifiés
La liste ordonnée des obstacles, en distinguant leur nature : technique,
juridique, fiscale, sanitaire, assurantielle, foncière, économique,
administrative, sociale.

## Normes applicables
Les textes et référentiels en jeu, avec leur niveau de certitude.

## Administrations concernées
Les interlocuteurs réels (douanes, DDPP/DDETSPP, INAO, DGCCRF, mairie,
préfecture, etc.).

## Autorisations nécessaires
Déclarations, agréments, licences, et qui doit les porter.

## Régimes de sous-traitance possibles
Qui peut exploiter à la place du musée, et selon quel contrat.

## Risques
Sanitaires, juridiques, financiers, réputationnels, et leur traitement.

## Stabilisateur proposé
Le livrable qui transforme l'expérience en ressource transmissible :
protocole, convention type, modèle économique, fiche de conformité.

## Décision administrative obtenue
Réponses écrites de l'administration, datées et archivées.

## Décision judiciaire éventuelle
Le cas échéant, la décision et ce qu'elle précise du possible.

## Version visiteur
Le cartel long, destiné au public.

## Version corpus
Les preuves, sources, variantes et incertitudes.

## Objections
Les contradictions sérieuses, conservées et traitées.

## Prochaines étapes
Ce qui reste à instruire, par qui, dans quel ordre.
```

---

## Indices associés

Deux indicateurs accompagnent chaque fiche et permettent de comparer les ateliers entre eux : l'**indice de friction administrative**, qui mesure le coût et la complexité de la mise en conformité, et l'**indice de capacité retrouvée**, qui mesure ce que l'atelier rend effectivement possible. Leur calcul fait l'objet de fiches méthode dédiées.

Lorsqu'un atelier porte sur la réactivation d'un savoir-faire empêché, on lui adjoint la **grille de remise en service**, qui identifie le composant d'accès manquant — prestataire, autorisation, pièce, procédure — et la manière de le restaurer.

## Dépendances, autonomie opérationnelle et instanciation générative

Une fiche ne suffit pas à faire fonctionner un atelier. Le cadre générique doit distinguer **la capacité déjà détenue**, **la capacité empruntée ou dépendante d'un tiers**, **la capacité encore à construire**, et **la capacité effectivement transmissible au public**. Ne pas confondre propriété d'une ressource, compétence, autorisation d'usage et capacité à accueillir des visiteurs.

Chaque atelier renseigne au minimum :

- **Ressources ancrées** : lieu, matériel, supports vivants, témoignages, compétences disponibles et preuves de leur disponibilité.
- **Dépendances** : partenaires, semences, fournisseurs, intervenants qualifiés, accès au terrain, autorisations ou services nécessaires ; statut (confirmé, sollicité, supposé, manquant).
- **Autonomie opérationnelle** : ce qui peut être pratiqué immédiatement, ce qui suppose un tiers, et le repli possible si ce tiers manque.
- **Contraintes propres au domaine** : sécurité des participants, protection du vivant et du milieu, réglementation, responsabilité et assurance, sans généraliser le protocole d'un atelier à un autre.
- **Transmission** : compétences visées, expérience effectivement accessible, conditions d'encadrement, observations et preuves de capacité retrouvée.
- **Cycle** : hypothèse → préparation → test prudent → documentation → évaluation → révision de l'instance et, si généralisable, du gabarit.

### Deux instances pilotes opérationnelles contrastées (octobre 2026)

| Dimension | Culture du Blé — Minesteggio | Culture de l'Âne — Rossignol et milieu urbain |
| --- | --- | --- |
| Point de départ | Semis et moissons rapportés en 2019 et 2024 | Présence et expérience quotidienne avec Rossignol ; campagne « Retour de l'âne corse en milieu urbain » en cours |
| Dépendance structurante | Association U Granu Anticu pour l'accès à des semences et à des savoir-faire, selon le porteur ; disponibilité future à confirmer | Ressource animale déjà présente ; dépendances portant surtout sur conditions d'accueil, soins, espace, sécurité, obligations applicables et acceptabilité urbaine |
| Premier travail d'instruction | Qualifier les lots, compétences disponibles, concours du partenaire et calendrier d'une nouvelle campagne | Reconstituer les observations réelles, les conditions de bien-être, les interactions avec des tiers et le cadre pratique/juridique |
| Écueil à éviter | Présenter l'association comme partenaire engagé sans confirmation | Réduire l'animal à un matériel de démonstration ou présenter une campagne comme validation de son modèle |
| Première sortie pédagogique possible | Histoire des céréales et documentation de cultures passées, sans promettre immédiatement un semis participatif | Histoire des ânes, observations du comportement et relation respectueuse, sans promettre un accueil ou des interactions publiques non évalués |

Ces deux instances constituent le premier banc d'essai opérationnel, mais ne sont pas les seuls ateliers envisagés. Elles ne définissent pas un ordre de priorité définitif : **la disponibilité d'une ressource centrale ne signifie pas que toutes les conditions de démonstration ou d'accueil sont satisfaites**. Les deux ateliers serviront à éprouver la capacité du framework à générer des dossiers adaptés, à détecter les dépendances et à transmettre sans perdre les différences de domaine.

### Règle de convergence

Une amélioration issue d'un atelier ne remonte dans le gabarit que si elle est applicable à d'autres instances. Les données de terrain, les relations avec les partenaires et les exigences spécialisées demeurent dans les dossiers propres à chaque atelier. Cette discipline évite de confondre un framework génératif avec un modèle rigide ou une doctrine supplémentaire.

## Portefeuille d'ateliers : quatre instances, maturités différentes (octobre 2026)

Le GGF doit gérer un **portefeuille évolutif** : deux pilotes plus avancés (Blé, Âne), deux ateliers moins avancés (Huiles essentielles, Bleus de Chine). Les états de maturité sont qualitatifs, liés aux preuves disponibles et aux dépendances à lever ; ce ne sont ni des classements de valeur, ni des promesses d'ouverture au public.

| Atelier | Point d'appui existant | Dépendance ou obstacle à instruire | Sortie générative prioritaire |
| --- | --- | --- | --- |
| **Culture du Blé** | Cultures/moissons historiques à Minesteggio et [notice existante](../ateliers/ble_minesteggio_2019_2027.md) | Savoir-faire, identification des semences, concours effectif d'U Granu Anticu, saison et accueil | Protocole de campagne, mémoire longue, parcours pédagogique |
| **Culture de l'Âne** | Rossignol, observation quotidienne et campagne de retour de l'âne corse en milieu urbain | Bien-être de l'animal, sécurisation des situations, responsabilités et acceptabilité urbaine | Journal probatoire et médiation respectueuse du vivant ; aucun contact public présumé autorisé |
| **Huiles essentielles** | [Fiche de possible déjà disponible](../ateliers/atelier_huiles_essentielles.md) et étude de la distillation | Matières premières, équipements, opérateurs compétents, sécurité, usages et cadres réglementaires distincts | Scénario de démonstration sans allégation thérapeutique, matrice de conformité par destination |
| **Bleus de Chine** | [Recherche patrimoniale sur les textiles bleus](../../research/patrimoine/bleu_chine_denim_nimes_corse_v0.2.md) et [protocole « Bouteille à la mer »](bouteille_a_la_mer.md) | Fabrication/personnalisation des exemplaires uniques, marquage durable, consentement des porteurs, droits et maintenance du dispositif numérique | Spécification d'un objet textile singulier, identifié et associé à une mission documentée |

### Spécificité de l'Atelier Bleus de Chine

L'objet n'est pas seulement de reproduire ou personnaliser un vêtement de travail traditionnel. Un **exemplaire unique identifié** devient potentiellement le **substrat matériel d'une « Bouteille à la mer »** : il porte une identité stable et une mission, circule, invite à une contribution volontaire et peut recevoir des traces documentaires. **L'Annuaire de la Diaspora Corse** est une mission possible parmi d'autres, non une obligation attachée à chaque exemplaire.

Ne jamais confondre :

```text
identité de l'exemplaire ≠ identité du porteur
identité de l'exemplaire ≠ mission (modifiable et historisable)
mission ≠ contribution
contribution ≠ fait vérifié
port du vêtement ≠ consentement à la géolocalisation ou à la publication
```

Séparer la couche textile (coupe, matière, fabrication, singularisation et conservation) de la couche documentaire (identifiant, biographie d'objet, mission et protocole de contribution). Un code QR peut ouvrir un point d'entrée, mais ne doit pas devenir l'unique moyen de conserver l'identité ni prétendre prouver l'authenticité du porteur. Toute contribution concernant des personnes, notamment pour l'annuaire de la diaspora, reste volontaire et soumise aux règles de vie privée du projet concerné.

### Conséquence pour le générateur

Le moteur commun génère en fonction du niveau de maturité : **fiche d'idée et dépendances** pour un atelier naissant ; **protocole de test** lorsqu'un terrain existe ; **fiche visiteur et conditions d'accueil** seulement lorsque la pratique est suffisamment instruite ; **bilan et propagation** après observation. Il n'invente ni partenaire confirmé, ni résultat de campagne, ni objet fabriqué, ni activité ouverte au public.

Le banc d'essai de généricité comprend désormais quatre familles : **végétal cultivé**, **animal vivant**, **transformation de matières végétales**, **objet artisanal singulier porteur d'une mission**. Chaque famille conserve ses règles spécialisées ; seules les méthodes réellement communes remontent au framework.
