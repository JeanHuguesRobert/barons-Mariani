---
canonical_url: https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/musee-mariani/plan-museal.md
author: Jean Hugues Noël Robert, baron Mariani
affiliation: Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica
license: CC BY-SA 4.0
last_stamped_at: 2026-06-26T00:00:00.000Z
title: Plan muséal provisoire du Musée Mariani
date: '2026-06-26'
status: draft
document_role: source
document_kind: museum-plan
visibility: public
lifecycle_state: working
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


# Plan muséal provisoire du Musée Mariani

Ce document fixe une première architecture pour le futur Musée Mariani. Il ne décrit pas encore une scénographie définitive. Il sert à ordonner les dossiers, les objets, les parcours et les futures publications.

## 1. Parcours possibles

### 1.1 Minesteggio : domaine, maison, jardins, eau, agriculture

Axe d'ancrage territorial. Minesteggio doit être présenté comme un lieu stratifié : domaine agricole, maison remarquable, jardins, hydraulique de l'Orta, traces anciennes, usages futurs.

Objectif : faire comprendre que le musée part d'un lieu, non d'une abstraction.

### 1.2 Les Mariani : Corse, Empire, République

Axe historique et généalogique. Il rassemble les figures familiales dont la trajectoire croise les institutions françaises et corses : noblesse impériale ou post-impériale, administration, armée, parlementarisme, alliances.

Objectif : utiliser la famille comme observatoire de l'État et de ses transformations.

### 1.3 Musée uchronique : bifurcations historiques contraintes

Axe expérimental. Il prolonge le document `research/uchronian_museum.md` : le musée n'expose pas seulement ce qui a eu lieu, mais aussi les bifurcations plausibles qui permettent de mieux comprendre les contraintes du réel.

Objectif : transformer l'histoire en espace d'inférence, non en fiction arbitraire.

### 1.4 Colonies, protectorat et zones de contact

Axe critique. Le dossier prototype est Louis-Thomas Mariani et Tahiti. La mention fragile de « prince en Tahiti » permet d'interroger les relations entre officiers français, souverainetés locales, titres honorifiques, récits familiaux et expansion coloniale.

Objectif : ne pas glorifier, ne pas effacer ; qualifier, enquêter, transmettre.

### 1.5 Objets, traces, preuves

Axe matériel. Il regroupe les objets susceptibles d'exposition : archives, mobilier, objets familiaux, documents, photographies, plans, traces agricoles, objets symboliques.

Objectif : relier chaque objet à un degré de preuve, un récit, une incertitude et une possibilité de médiation.

### 1.6 Transmission et Fonds de dotation

Axe institutionnel. Il explique pourquoi le patrimoine est destiné à une structure de conservation et d'intérêt général plutôt qu'à une simple logique successorale privée.

Objectif : faire comprendre le passage de l'héritage familial à l'infrastructure de transmission.

## 2. Typologie documentaire

Chaque dossier muséal devrait idéalement suivre le modèle suivant :

```text
# Titre du dossier

## Résumé public
## Statut documentaire
## Ce qui est établi
## Ce qui est probable
## Ce qui reste à vérifier
## Sources connues
## Sources à rechercher
## Interprétation muséale
## Risques de surinterprétation
## Cartel court
## Cartel long
## Pistes d'exposition
```

## 3. Critères de passage vers un dépôt dédié

Le dépôt `musee-mariani` devra être créé lorsque plusieurs conditions seront réunies :

| Condition | Justification |
|---|---|
| Plusieurs dossiers muséaux stabilisés | éviter un dépôt vide ou décoratif |
| Des cartels publics exploitables | passage du corpus source à la médiation |
| Des images ou objets avec droits suivis | besoin de gestion documentaire spécifique |
| Un site ou une exposition autonome | séparation fonctionnelle du dépôt familial |
| Des contributeurs extérieurs | périmètre de travail moins personnel |

Avant ce seuil, le sous-corpus `musee-mariani/` dans `barons-Mariani` respecte mieux la règle d'Occam.

## 4. Dossiers prioritaires

| Dossier | Statut | Fonction |
|---|---|---|
| Louis-Thomas Mariani et Tahiti | prototype ouvert | histoire coloniale et méthode critique |
| Minesteggio | à structurer | ancrage territorial du musée |
| Chaise à porteur | à documenter | objet matériel, transport, statut social, scénographie |
| Blés anciens / écomusée agricole | à documenter | agriculture, transmission, autonomie alimentaire |
| Napoléon / bicorne / uchronie | à stabiliser | bifurcation historique contrôlée |
| Fonds de dotation | à articuler | institution de transmission |

## 5. Construction matérielle et financement : la Boutique Mobile du Musée

*Orientation déclarée par le porteur le 26 octobre 2026 ; dispositif en construction. Cette section distingue les intentions de vente des produits réellement disponibles, de leurs coûts et de leurs recettes, encore à vérifier.*

Le Musée Mariani des Possibles entend commencer sa construction matérielle **par l'activité de sa Boutique Mobile**. La vente de produits n'est pas une activité accessoire ajoutée à un musée achevé : elle est envisagée comme un premier moyen de **financer la constitution progressive du Musée**, d'entrer en relation avec ses publics et de mettre en circulation des objets porteurs de connaissances ou de missions.

Trois familles de produits sont envisagées au départ :

| Famille | Nature envisagée | Relation au Musée | À instruire avant commercialisation |
| --- | --- | --- | --- |
| **Exemplaires uniques de Livres Vivants** | Exemplaires matériels singuliers et identifiés d'ouvrages évolutifs | Transmission éditoriale, collection, contribution et, selon le cas, « Bouteille à la mer » | Fabrication, coût, identité d'exemplaire, droits, prix, commande, livraison |
| **Produits liés aux huiles essentielles** | Produits issus de l'activité autour des plantes aromatiques et des huiles essentielles ; assortiment exact à préciser | Support matériel de l'[Atelier Huiles essentielles](ateliers/atelier_huiles_essentielles.md) et financement de la transmission | Nature et destination des produits, sécurité, conformité, étiquetage, responsabilité et conditions de vente |
| **Bleus de Chine vintage ou modernes** | Vêtements de travail, exemplaires uniques par identification et éventuellement personnalisation | Patrimoine textile et expérimentation d'une [« Bouteille à la mer »](methodes/bouteille_a_la_mer.md) associée à une mission, par exemple l'Annuaire de la Diaspora Corse | Provenance et état des pièces vintage, approvisionnement moderne, personnalisation, coût, droits, identifiant durable, vie privée |

**Collaboration envisagée pour les Bleus de Chine :** Ange, *tragulinu*, connaît particulièrement bien ces vêtements et souhaite recentrer son activité sur eux. Son concours constitue une ressource humaine et commerciale identifiée par le porteur du projet. Les modalités exactes de collaboration (stock, achats, consignation, personnalisation, répartition des recettes, responsabilité envers les acheteurs) restent à formaliser ; ne pas présenter un accord contractuel comme déjà établi.

### Deux boucles complémentaires

```text
Boucle économique :
approvisionnement / création
→ description et conformité
→ offre / vente
→ recettes et coûts constatés
→ financement documenté du Musée

Boucle muséale :
objet identifié
→ histoire et mission éventuelle
→ circulation
→ contribution volontaire / traces
→ qualification
→ enrichissement documentaire et transmission
```

Un produit peut contribuer à la première boucle sans participer à la seconde. Inversement, la réussite d'une « Bouteille à la mer » ne présume d'aucun profit. Les deux résultats doivent rester mesurés séparément.

### Règles d'effectivité et de provenance

- Distinguer **projet, prototype, stock disponible, annonce publique et vente effectivement réalisée** ; aucune recette ou marge n'est présumée.
- Identifier la **structure juridique vendeuse**, la propriété des objets et du stock, les obligations fiscales, de consommation, d'assurance et de sécurité propres à chaque famille.
- Suivre pour chaque vente prix encaissé, coût complet, éventuelle rémunération des partenaires, frais, résultat net et affectation au financement du Musée.
- Conserver pour chaque exemplaire unique une identité stable, indépendante de son détenteur, de sa mission et de ses contributions ; ne pas transformer un QR code en mécanisme de surveillance des porteurs.
- Les produits liés aux huiles essentielles exigent une instruction spécifique selon leurs usages ; ne pas confondre démonstration, production, cosmétique, alimentaire et allégation thérapeutique.
- Le musée peut coopérer avec des artisans et des commerçants, mais une coopération annoncée ne doit pas être présentée comme conclue sans accord.

Le [gabarit commun des ateliers](methodes/template_fiche_possible.md) décrit la transmission des capacités ; **la Boutique Mobile est la fonction transversale de financement, de distribution et de mise en circulation**. Un atelier et une ligne de produits peuvent se correspondre sans être la même chose.

## 6. Principe de médiation

Chaque dossier doit être lisible à deux niveaux :

1. **niveau visiteur** : récit clair, cartel, images, objets, contexte ;
2. **niveau corpus** : preuves, sources, incertitudes, variantes, statut de validation.

Le musée doit donc assumer une double nature : exposition publique et interface vers un corpus source versionné.
