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


### Périmètre des personnes et structures juridiques (déclaration du 26 octobre 2026)

La Boutique Mobile, ses produits et le Musée s'inscrivent dans un **écosystème de cinq acteurs ou qualités juridiques à distinguer**, dont deux structures déclarées existantes dotées chacune d'un numéro SIREN selon le porteur :

| Acteur / qualité | État déclaré | Rôle envisageable, sans affectation décidée |
| --- | --- | --- |
| Association **C.O.R.S.I.C.A.** | Existante, SIREN propre | Activités associatives, médiation, actions collectives, éventuellement ventes selon objet/statuts et fiscalité |
| **Casa Mariani**, entreprise agricole unipersonnelle | Existante, second SIREN | Production ou valorisation agricole, huiles essentielles ; activité de vente et périmètre d'immatriculation à vérifier |
| Fonds de dotation **Barons Mariani** | En cours de création | Conservation, portage patrimonial et financement d'intérêt général, sous réserve de constitution effective et de statuts |
| Fonds de dotation **Les Amis de Malou** | En cours de création | Mission autonome à respecter ; tout concours au Musée doit être compatible avec son objet et ses futurs statuts, sans affectation présumée |
| **Personne physique** du porteur | Existante | Création, détention initiale de certains biens et droits, contributions ou contrats personnels ; distinguer gestion privée et activité professionnelle |

**Précision juridique :** si Casa Mariani est une entreprise individuelle agricole (EI), elle ne constitue pas une personne morale distincte de l'entrepreneur ; son SIREN identifie l'entreprise exercée en nom propre. La qualification exacte (« entreprise agricole unipersonnelle » pouvant renvoyer à des statuts différents) doit être établie sur l'extrait d'immatriculation, sans la confondre avec une EURL, société dotée de personnalité morale. Ne pas attribuer un nouveau SIREN à la personne physique pour ses activités privées. L'association demeure une personne morale distincte et dotée de son propre SIREN.

**Séparation opérationnelle indispensable :** pour chaque produit ou opération, identifier séparément **créateur/propriétaire**, **fabricant ou fournisseur**, **vendeur et émetteur de facture**, **encaissant**, **bénéficiaire économique**, **porteur de la mission muséale** et, s'il y a lieu, **destinataire des dons**. Ces rôles ne se déduisent ni du nom « Musée » ni du logo de la boutique. Une affectation au Musée nécessite une trace comptable et, pour les transferts entre personnes ou entités, des actes adaptés.

Les fonds en cours de création ne doivent pas être présentés comme déjà capables de contracter ou d'encaisser au titre de leur personnalité juridique propre. L'association peut avoir une activité économique mais doit tenir compte de ses statuts et de ses obligations fiscales. La Boutique Mobile n'est pas en elle-même une nouvelle personne morale : elle peut être une enseigne ou un dispositif partagé, avec vendeur identifié pour chaque vente.

## 6. Casa Mariani : la Maison et son signe M — double lecture

### Lecture publique — La Maison

**Casa Mariani**, c'est une maison au sens plein : un lieu, une famille, une histoire et tout ce qui se transmet. La Maison ne se limite pas aux murs de Minesteggio ni aux seules personnes qui portent le nom Mariani. Elle rassemble un patrimoine, des savoirs, des objets et des projets, et peut accueillir ceux qui souhaitent les faire vivre et les transmettre.

Son signe est simplement **M**. Sous la marque Casa Mariani, la Boutique Mobile se construit autour de trois familles envisagées : des exemplaires uniques de Livres Vivants, des produits liés aux huiles essentielles et des Bleus de Chine anciens ou modernes. Leur disponibilité commerciale reste à établir produit par produit. Le Musée Mariani des Possibles est la vocation de transmission et d'exploration que ces activités contribuent à construire et à financer.

**Une Maison conserve ce qu'elle reçoit et cherche à rendre possible ce qu'elle transmet.**

### Lecture approfondie — Maison, parenté, patrimoine et institution

Le terme *casa* renvoie d'abord à la demeure et au foyer ; son rapprochement avec *casata* rappelle la famille et son inscription sociale. Dans l'usage français, « maison » désigne également une famille, une lignée ou une dynastie : « Maison de France » n'est pas le nom d'un bâtiment. Les sens ne sont pas identiques selon les langues et les époques ; l'analogie sert ici à expliciter l'étendue de la notion, non à postuler une forme unique d'organisation familiale corse.

L'anthropologie des « sociétés à maisons », notamment associée aux travaux de Claude Lévi-Strauss, fournit un instrument comparatif : la Maison peut se comprendre comme un principe de continuité de biens matériels et immatériels, de noms, de mémoires et de relations, transmis par des mécanismes qui excèdent parfois la stricte filiation biologique. **Casa Mariani est ici une proposition institutionnelle contemporaine inspirée de cette problématique, et non un cas ethnographique démontré de « société à maisons ».**

Distinguer quatre plans, qui peuvent se recouvrir sans s'identifier : (1) **territorial et matériel** — Minesteggio et les lieux ; (2) **familial et mémoriel** — noms, alliances, récits et héritages ; (3) **patrimonial et cognitif** — collections, objets, Livres Vivants et savoir-faire ; (4) **collectif et prospectif** — artisans, partenaires, contributeurs, missions et capacités à transmettre. Cette extension aux non-parents est un choix explicite du projet, non une assertion sur toutes les familles corses.

Le monogramme **M** est un signe de marque et de provenance, non un titre dynastique ni une personne juridique. L'inspiration d'un monogramme réduit à une initiale, comme le N napoléonien, n'établit aucune équivalence institutionnelle ou historique. La marque commune ne fait pas disparaître les distinctions entre association, entreprise, fonds de dotation et personne physique, ni leurs obligations respectives.

### Règle éditoriale de Double Lecture

La Double Lecture n'est pas la juxtaposition d'un résumé promotionnel et d'une dissertation. C'est la **même proposition à deux résolutions**, avec une correspondance vérifiable des assertions :

1. **Lecture profane** : un texte autonome, concret et intelligible, sans jargon ni prérequis ; il explique d'abord ce que désigne la Maison et ce qu'elle rend possible.
2. **Lecture savante** : les définitions, comparaisons, provenances, limites des analogies, distinctions juridiques, objections et références, sans changer le sens du premier texte.
3. **Invariance sémantique** : toute affirmation de la lecture publique doit pouvoir être défendue et localisée dans la lecture approfondie ; celle-ci peut ajouter des distinctions mais ne doit pas contredire silencieusement le propos public.
4. **Statut des énoncés** : séparer attestations historiques, analyses anthropologiques, intentions du porteur et projets encore conditionnels ; aucune métaphore n'est une preuve juridique ou historique.
5. **Lecture dans les deux sens** : un spécialiste doit pouvoir proposer une correction sans rendre la version publique illisible ; un lecteur non spécialiste doit pouvoir interroger la version savante sans changer de récit.
6. **Épreuve du réel** : vérifier l'intelligibilité auprès de lecteurs profanes et la solidité auprès de lecteurs compétents ; documenter les objections et faire évoluer les deux versions ensemble.

La Double Lecture est applicable aux cartels, ateliers, fiches produit, Livres Vivants et propositions de partenariat. Elle est distincte des *formats* de diffusion : Livre, Annexe scientifique, Magazine, site contributif et agent conversationnel peuvent chacun mobiliser les deux niveaux selon leur objet.

### Dogfooding et Skin in the Game : protocole d'épreuve de la Double Lecture

La méthode se teste d'abord sur **nos propres productions**, là où les défauts d'une formulation ont des conséquences concrètes. Deux principes complémentaires :

- **Dogfooding** : utiliser réellement notre texte et nos outils dans les opérations du Musée (présentation de Casa Mariani, étiquettes, fiches produits, discussions avec Ange, partenaires, visiteurs), plutôt que les valider seulement par lecture interne.
- **Skin in the Game** : celui qui affirme et publie doit rester exposé aux conséquences pertinentes de l'affirmation : correction publique, temps passé, coûts, obligations assumées et réputation. Ne pas transférer silencieusement le risque à un partenaire, un acheteur ou un animal ; l'exposition au risque ne dispense jamais des protections nécessaires.

**Cycle minimal** : formuler → publier ou éprouver dans un usage limité → relever incompréhensions, objections et coûts → comparer aux sources → corriger les deux niveaux → archiver la différence et l'effet. Une validation par le seul auteur n'est pas un test indépendant.

#### Premier essai contradictoire : « Casa Mariani, la Maison »

| Proposition publique | Risque de contresens | Vérification et correction |
| --- | --- | --- |
| « La Maison ne se limite pas à la famille » | Faire croire que chacun en devient membre ou ayant droit | Clarifier participation, accueil et droits ; ne pas promettre une affiliation juridique |
| « La marque Casa Mariani » | Faire penser qu'une seule entité vend tous les produits | Identifier le vendeur réel sur chaque fiche et document commercial |
| « La Boutique Mobile propose… » | Faire croire à un stock et à une vente déjà ouverts | Préférer « se construit autour de trois familles envisagées » jusqu'à vérification de la mise en vente |
| « M » comme signe commun | Faire croire que le monogramme suffit à identifier un exemplaire unique | Distinguer marque commune M et identifiant individuel de chaque objet |
| « Maison » au sens anthropologique | Assimiler abusivement Casa Mariani aux sociétés à maisons décrites par l'ethnologie | Présenter l'analogie comme heuristique, non comme preuve historique ou statut juridique |
| « Financer le Musée » | Confondre prix de vente, chiffre d'affaires et financement disponible | Comptabiliser coûts, recettes nettes et affectations effectives, séparément |

**Critères d'effectivité** : capacité d'un lecteur à reformuler correctement ce qu'est Casa Mariani ; absence d'ambiguïté sur le vendeur, l'état du produit et le destinataire des recettes ; objections réellement tracées ; corrections propagées aux supports dérivés ; baisse de l'effort requis pour produire des textes conformes aux deux niveaux. Ne pas déclarer ce test « réussi » avant des observations indépendantes ou des opérations documentées.

Le **premier dogfooding interne** a identifié une phrase prématurée sur la disponibilité des produits ; sa correction a été propagée dans le texte public de la présente section. La publication constitue un premier essai de cohérence, pas encore une validation par des clients ni une activité commerciale constatée.

## 7. Principe de médiation

Chaque dossier doit être lisible à deux niveaux :

1. **niveau visiteur** : récit clair, cartel, images, objets, contexte ;
2. **niveau corpus** : preuves, sources, incertitudes, variantes, statut de validation.

Le musée doit donc assumer une double nature : exposition publique et interface vers un corpus source versionné.


## 8. Présentation de Casa Mariani et coopération potentielle avec le Musée de la Corse

**Jalon connu :** deuxième réunion du Comité des usagers du Musée de la Corse, le **26 novembre 2026** à Corte. Une opportunité de coopération peut se présenter plus tôt ; la présentation doit donc rester réutilisable et ne pas dépendre de la date.

### Lecture publique — version courte de présentation

**Casa Mariani est une Maison au sens plein : un lieu, une histoire familiale, un patrimoine et un projet ouvert de transmission.** À Minesteggio, près de Corte, le Musée Mariani des Possibles entend relier objets, documents, savoir-faire et expériences contemporaines pour comprendre ce qui fut possible, ce qui l'est encore et ce qui pourrait le redevenir. Sa construction matérielle commence par la Boutique Mobile, sous la marque Casa Mariani et le monogramme M, avec trois familles de produits envisagées : exemplaires singuliers de Livres Vivants, produits liés aux huiles essentielles et Bleus de Chine anciens ou modernes. Quatre ateliers structurent l'exploration : blé, âne, huiles essentielles et Bleus de Chine. Ils ont des maturités différentes et ne sont pas tous ouverts au public.

**Une Maison conserve ce qu'elle reçoit et cherche à rendre possible ce qu'elle transmet.**

### Lecture approfondie — coopération sans confusion des institutions

Le Musée Mariani des Possibles est un projet privé en construction, distinct du **Musée de la Corse**, institution publique. Une éventuelle coopération est à **explorer**, sans accord, validation scientifique, droit d'accès aux collections ou accueil des ateliers présumés.

- **Apports potentiels de Casa Mariani** : expériences agricoles de Minesteggio (blé 2019/2024), observation et campagne autour de Rossignol, recherche et pratique autour des huiles essentielles, histoire et remise en circulation des Bleus de Chine, Livres Vivants à double lecture, expérimentation de transmission par objets singuliers.
- **Intérêt muséal à évaluer avec l'institution** : documentation contradictoire, témoignages, transmission de gestes et d'usages, ateliers pilotes proportionnés aux conditions réelles, médiation entre musée et territoires.
- **Principe de réciprocité** : rechercher un besoin effectivement formulé par le Musée de la Corse et co-construire un test borné, plutôt que solliciter une caution générale pour Casa Mariani.
- **Précautions** : respect du projet scientifique et culturel du Musée de la Corse, rôles distincts du Comité des usagers et des instances décisionnaires, sécurité et bien-être animal, droits des sources et des objets, absence de confusion entre vente privée et mission publique.

### Support initial et test du réel

Préparer une présentation publique **d'une page**, complétée d'une **annexe de preuves et de statuts** : réalisé / en cours / envisagé / dépendant d'un partenaire. Les deux niveaux doivent préserver le même sens. Tester d'abord l'intelligibilité et la possibilité d'identifier une expérimentation réellement pertinente pour l'institution. **Ne pas ouvrir un chantier technique ou un dépôt supplémentaire** pour ce support.

**Échéance :** document utilisable avant le 26 novembre 2026 et amendable selon les échanges ; le 26 novembre est un jalon, pas une date imposée de publication ou une promesse de partenariat.
