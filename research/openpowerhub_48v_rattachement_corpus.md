---
title: "OpenPowerHub 48V — rattachement au corpus et cahier de validation"
subtitle: "Kit pédagogique de désynchronisation énergétique domestique, solaire, V2L et pilotage ouvert"
author: "Jean Hugues Noël Robert"
affiliation: "Mariani School of Autonomy — Institut Mariani / C.O.R.S.I.C.A."
date: "2026-11-19"
status: "working-draft — architecture et coûts non validés"
language: fr
document_role: source
document_kind: research-paper
visibility: public
lifecycle_state: working
license: CC BY-SA 4.0
update_policy: UP-DEFAULT-REVIEWED
corpus_hierarchy:
  level: source_note
  role: "cadrage de l'objet pédagogique OpenPowerHub et cartographie des sources antérieures"
  derived_from:
    - "Manifeste et dossier de projet OpenPowerHub 48V communiqué le 2026-11-19"
    - "research/ecole_mariani_autonomie.md"
    - "research/homeostasie_habitat.md"
    - "JeanHuguesRobert/FractaVolta: docs/energy-packets.md"
related_documents:
  - research/ecole_mariani_autonomie.md
  - research/ecole_mariani_autonomie_terminologie.md
  - research/ecole_mariani_autonomie_terrains_pilotes.md
  - research/homeostasie_habitat.md
  - research/cas_maison_urbaine_corte_autonomie.md
  - research/noyau_doctrinal_rendre_capable.md
  - research/serenia_autonomie_assistee_ia.md
  - https://github.com/JeanHuguesRobert/FractaVolta/blob/main/docs/energy-packets.md
  - https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/LE_RESEAU_INCONSCIENT.md
  - https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/generalized_packet_networks.md
  - https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/fractanet.md
  - https://github.com/JeanHuguesRobert/cogentia/blob/main/research/campaign/fiches_maires/fiche_02_fractavolta_energie_villageoise.md
related_projects:
  - C.O.R.S.I.C.A.
  - Institut Mariani
  - The Mariani School of Autonomy
  - FractaVolta
  - Cogentia
  - Fractanet
  - Musée Mariani des Possibles
  - Corsica 2038
---

# OpenPowerHub 48V — rattachement au corpus et cahier de validation

## 1. Statut de ce document

Le manifeste OpenPowerHub 48V décrit **une proposition d'architecture** et non un kit homologué, un produit existant validé ou une promesse de performances démontrées. Les chiffres de prix, rendement, durée d'autonomie, puissance continue/crête, composants, conformité et sécurité sont des **objectifs à qualifier par nomenclature, calcul, mesures et essais**.

Ce document est un **satellite** de la source canonique de l'École Mariani, et non un nouveau manifeste doctrinal. Il préserve la provenance du descriptif communiqué le 19 novembre 2026 ; il en explicite les liens et ses hypothèses à vérifier.

## 2. Thèse : de l'indépendance à l'autonomie de capacité

L'École Mariani enseigne que « l'autonomie ne s'installe pas : elle s'apprend ». L'objectif d'OpenPowerHub est que le foyer puisse **comprendre, mesurer, choisir, maintenir, réparer, remplacer, transmettre et quitter** une dépendance, plutôt que remplacer une boîte noire par une autre.

La **désynchronisation** est ici d'abord une séparation des contraintes de fréquence et de puissance instantanée : les producteurs et les consommateurs domestiques sont couplés **par un stockage et une conversion contrôlée**, non par une connexion directe synchrone au réseau. Elle ne signifie ni suppression du réseau, ni absence de réglementation. L'**isolation galvanique** est une propriété électrique distincte, à établir matériellement composant par composant.

Le réseau extérieur devient une source optionnelle, avec un coût et une disponibilité explicites ; le photovoltaïque est une autre source ; le véhicule compatible V2L constitue une réserve mobile possible ; le stockage local constitue un tampon décisionnel.

## 3. Relations de priorité avec le corpus existant

| Source déjà existante | Relation exacte avec OpenPowerHub |
| --- | --- |
| [École Mariani de l'Autonomie](ecole_mariani_autonomie.md) | Produit pédagogique du module 4 (habitat, énergie) et du module 5 (courant continu, énergie en packets), support des parcours de facilitateurs |
| [Terminologie de l'École](ecole_mariani_autonomie_terminologie.md) | Un *participant* apprend ; un *autonomy practitioner* démontre sa capacité ; un *autonomy facilitator* accompagne ; un *steward* protège le commun et la documentation |
| [Homéostasie de l'habitat](homeostasie_habitat.md) | Continuité des fonctions essentielles, diagnostic, retour manuel, modes dégradés en cas de panne de l'IA, du solaire, du V2L, du stockage ou du réseau |
| [Terrains pilotes](ecole_mariani_autonomie_terrains_pilotes.md) | Minesteggio, La Maison Blanche à La Gaude, maison individuelle urbaine de Corte (anonymisée) et cas introductif de l'eau chaude |
| [Maison urbaine de Corte](cas_maison_urbaine_corte_autonomie.md) | Cas préexistant de coupure EDF réversible et véhicule comme « packet mobile » ; éviter de présenter OpenPowerHub comme solution universelle |
| [FractaVolta / Energy packets](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/docs/energy-packets.md) | Unité opérationnelle : source → mesure → stockage → routage → usage → trace ; le réseau public est un pair/appoint plutôt qu'un destinataire obligatoire |
| [Le Réseau Inconscient](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/LE_RESEAU_INCONSCIENT.md) | Instanciation stationnaire et domestique du *store-and-forward*, distincte de la logistique de batteries mobiles à l'échelle territoriale |
| [Generalized Packet Networks](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/generalized_packet_networks.md) | Tampon et arbitrage énergie/puissance : ordonnancement des usages, occupation des ressources, pertes, durée et priorité |
| [Fractanet](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/fractanet.md) | Contrôle vs plan de données : l'EMS planifie sous contraintes physiques ; les contrôleurs électriques exécutent selon un domaine de sûreté |
| [Cogentia](https://github.com/JeanHuguesRobert/cogentia) | Agents de diagnostic, simulations de charges, maintenance, journaux de décisions, traçabilité des actions et transmission de méthodes sous mandat |
| [FractaVolta énergie villageoise](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/campaign/fiches_maires/fiche_02_fractavolta_energie_villageoise.md) | Voie de passage possible du foyer au bâtiment public, puis au collectif, sous étude indépendante des règles de raccordement et d'autoconsommation |
| [Rendre capable](noyau_doctrinal_rendre_capable.md) | Autonomie individuelle → capacités transférables → autonomie collective ; prévention de la capture commerciale et maintien du droit de sortie |

**Échelle :** logement (micro-hub) → bâtiment (démonstrateur) → quartier/village (coopération de nœuds) → territoire (FractaVolta / Corsica 2038). L'équivalence entre ces échelles est une **hypothèse architecturale**, pas une autorisation de transposer la même installation électrique à toutes les échelles.

## 4. Architecture envisagée : invariants et frontières

- **Sources** : photovoltaïque via MPPT, appoint réseau via chargeur AC/DC adapté, sortie V2L uniquement des véhicules effectivement compatibles, avec puissance/terre/protections vérifiées.
- **Stockage** : bus DC nominal « 48 V » et batteries LFP **compatibles entre elles et avec le BMS** ; ne jamais présumer l'interchangeabilité de n'importe quelle batterie du marché.
- **Consommation** : usages DC prioritaires lorsque leur alimentation et leur rendement sont compatibles ; sortie AC pour les charges requises.
- **Contrôle de sécurité** : protections indépendantes du système IA et arrêt sûr lors d'erreurs de commande, de communication, d'isolement, de surintensité ou de surchauffe.
- **Intelligence et supervision** : l'EMS arbitre seulement les actions admissibles, dans un contrat d'interface clair ; un agent IA peut expliquer/proposer/simuler, pas neutraliser les limites de sécurité.
- **Observabilité** : chaque scénario d'énergie mesure les Wh réellement entrants et sortants, les pertes, les pointes, l'état de charge, l'occupation des sources et les transitions de mode.

### Une précision conceptuelle

Le courant continu sur un bus 48 V n'est pas en lui-même un *packet*. La packetisation correspond ici à **des allocations mesurables, bornées et gouvernées** de puissance/énergie dans le temps, ou à des batteries physiquement transportables. Éviter l'analogie littérale avec les paquets IP.

## 5. Vérifications techniques impératives avant communication publique de chiffres

1. **Puissance et énergie** : 410 Wh / 6 000 W = **4,1 minutes idéales** à 6 kW, avant pertes et limites de décharge. Un tampon de 410 Wh n'est pas une batterie permettant une alimentation continue de 6 kW. À environ 48 V, 6 kW imposent déjà quelque **125 A**, hors pertes et pointes ; le dimensionnement doit partir des courants, températures, cellules, câbles, connexions, BMS, protections et cycles.
2. **Abonnement 3 kVA** : réduire la puissance réseau souscrite ne crée pas d'énergie. Il faut établir un budget de puissance **et** d'énergie selon le profil du foyer, et vérifier le coût effectif des pertes de double conversion.
3. **V2L** : tous les véhicules électriques ne disposent pas du V2L ; la puissance disponible, les limites de décharge, la compatibilité de la liaison neutre/terre et les modes de charge diffèrent. L'emploi d'un V2L comme appoint doit être validé pour le modèle concerné ; pas de connexion sauvage au tableau.
4. **AC / DC / AC** : la non-injection et l'absence de synchronisation en sortie **ne valent pas dispense générale** de règles d'installation, de protection ou de déclaration. La conformité française doit être évaluée pour chaque configuration ; en Corse, interlocuteur réseau **EDF SEI** (et non Enedis).
5. **Galvanique et « safety by design »** : un chargeur AC/DC n'assure une isolation galvanique que si sa conception la fournit. Un STM32 n'empêche pas magiquement tout dommage par bug ; la sécurité demande des protections matérielles, une analyse de défaillance et des essais indépendants.
6. **Port batterie « hot-swap »** : fonction à démontrer avec précharge, sectionnement, coupure de défaut, compatibilité chimie/BMS et régime de défaut. « Vissé sans soudure » ne signifie pas « sans risques ».
7. **Rendements / 230 V éteint** : les allégations « 20 % économisés » et « >95 % » exigent des courbes de rendement mesurées aux charges réelles. L'arrêt nocturne du 230 V n'est possible que pour les circuits dont le service peut effectivement être interrompu ; réfrigération, sécurité et autres fonctions doivent être conservées.
8. **Coûts** : le « cœur à 250 € » et le « tout compris à moins de 900 € TTC » sont des objectifs non certifiés, sans BOM publique consolidée ni coûts connus de conformité, essais, assurance, protections, boîtier, transport et SAV.
9. **Logiciel** : les interfaces MQTT, REST, Matter et l'accès distant sécurisé sont des options de conception ; leur présence, leur compatibilité et leur fiabilité ne sont pas encore démontrées. Le fonctionnement local sécurisé doit rester autonome du cloud, du VPS et de la disponibilité d'un modèle IA.

Démarche recommandée : qualifier un **banc pédagogique sécurisé** puis un prototype hors réseau, avant toute intégration à une installation domestique existante avec conception et contrôle conformes.

Références réglementaires de point de départ (à réexaminer selon architecture) :
- [EDF SEI Corse — autoconsommation jusqu'à 36 kVA](https://corse.edf.fr/producteur/l-autoconsommation/l-autoconsommation-pour-la-production-a-36-kva)
- [EDF SEI Corse — référentiels techniques](https://corse.edf.fr/producteur/se-raccorder/les-referentiels-techniques-applicables-3)
- [CONSUEL — dossiers techniques](https://www.consuel.com/dossiers-techniques/)

## 6. Programme pédagogique proposé (extension du cursus existant)

1. **Comprendre** : W, Wh, VA, courant, tension, pertes, dynamique des charges, principe d'un découplage.
2. **Mesurer** : lecture des consommations, courbes, puissance de pointe, besoins essentiels.
3. **Simuler** : soleil, budget d'énergie, limites V2L, capacité du tampon, coût complet, vieillissement.
4. **Observer sans danger** : démonstrateur basse tension et contrôle/trace des transitions entre sources.
5. **Exercer le mode dégradé** : IA indisponible, source absente, batterie faible, panne de capteur, arrêt sûr.
6. **Construire et faire vérifier** : distinguer tâches pédagogiques et actes réservés à des professionnels compétents.
7. **Documenter et transmettre** : tutoriel, composants, interfaces, tests, incidents et corrections ; progression de *participant* à *facilitator* selon les compétences attestées.

**Principe de l'École** : le but n'est pas de transformer l'apprenant en électricien supposé certifié en un week-end, mais de le rendre effectivement plus compétent, y compris pour commander, comprendre et contrôler les travaux spécialisés.

## 6 bis. Quatrième cas d'usage : station énergétique portable embarquée dans un véhicule (19 novembre 2026)

**Décision conceptuelle :** OpenPowerHub doit également pouvoir exister en **station énergétique portable**, que l'utilisateur **déplace avec lui-même**, éventuellement en la transportant dans un véhicule. Ce mode d'usage ne constitue **ni un quatrième site immobilier** ni une quatrième étape obligatoire de déploiement. Il doit rester compatible avec la séquence de pilotes fixes décidée par ailleurs. Un même dispositif pourrait, selon son architecture et sa masse, être déplacé pour assurer plusieurs démonstrations.

La station emporte son **propre tampon et ses interfaces énergétiques** ; son utilité ne doit pas dépendre de sa présence permanente dans un bâtiment. Une fois immobilisée en un lieu sûr, elle peut fournir de l'énergie à des outils, appareils numériques, éclairages et équipements pédagogiques compatibles, dans les limites réellement vérifiées de ses protections, de sa puissance et de son énergie.

### Distinguer trois situations

1. **Station portable transportée dans un véhicule** : le véhicule sert d'abord à **déplacer le générateur de services énergétiques** ; la batterie et les sorties appartiennent à la station.
2. **Véhicule électrique alimentant la station par V2L** : possibilité **supplémentaire et optionnelle**, réservée aux modèles dont la sortie V2L et la protection sont compatibles et vérifiées ; la puissance est limitée par le véhicule, le chargeur et la station.
3. **Station rechargée depuis le véhicule** : possibilité à étudier **séparément**, uniquement par une interface DC/DC ou AC/DC conçue et protégée pour la source, le régime moteur et la batterie du véhicule ; ne pas présumer qu'une prise 12 V d'accessoires ou l'alternateur acceptent les puissances envisagées. Ne jamais raccorder directement les batteries.

Le fonctionnement **transporté**, le fonctionnement **en stationnement** et une éventuelle alimentation **pendant la circulation** ont des contraintes de sécurité distinctes ; la présente note n'autorise pas ce dernier usage. Il est également interdit de présumer qu'une station portable peut alimenter le réseau intérieur d'un immeuble par simple branchement sur une prise : aucune injection ou rétroalimentation non protégée.

### Contraintes propres à la portabilité

- **Masse et encombrement** : seuils de manutention réels, poignée/châssis, centre de gravité, fixation résistante aux freinages et chocs ; éventuellement modules séparables plutôt qu'une seule caisse de 6 kW.
- **Électricité** : à 48 V nominaux, 6 kW correspondent à environ 125 A avant pertes, rendant les connexions, câbles, fusibles, BMS, échauffements et isolements critiques ; la puissance portable continue doit être **dimensionnée et testée**, pas copiée du manifeste.
- **Conditions d'emploi** : vibrations, poussières, humidité, pluie, ventilation et chaleur d'un véhicule fermé ; prévention des courts-circuits, dommages mécaniques, surchauffe et incendie.
- **Interfaces** : entrées solaire / réseau limité / V2L compatibles, sorties DC et AC protégées, mise à la terre / neutre / différentiel adaptés aux modes et usages réels, connecteurs identifiables et verrouillables si nécessaire.
- **Autonomie vérifiable** : distinguer Wh stockés, W disponibles, durée réelle à charge donnée, pertes à vide, recharge et limitation automatique lors de tension ou température anormales.
- **Mode dégradé** : absence de réseau, absence de véhicule V2L, soleil indisponible, IA absente, déplacement ou batterie faible ; maintien des fonctions DC essentielles quand le 230 V est délesté, sous contraintes de sécurité.

### Intérêt pédagogique et rapport à FractaVolta

La version portable devient un **démonstrateur itinérant** de la Mariani School of Autonomy : test du kit dans différents lieux, démonstration du **store-and-forward** par déplacement physique du stockage, mesure des entrées/sorties et des contraintes d'usage. Elle rejoint les travaux de FractaVolta sur les **paquets d'énergie mobiles**, sans affirmer qu'une station transportée correspond déjà à un système logistique de batteries interchangeables, ni que la mobilité résout le bilan énergétique.

**Conception privilégiée :** un **Core et des surfaces cohérents** entre variantes fixes et portable, mais **une enveloppe électrique/mécanique et des performances propres** à chaque variante. Le budget nul actuel demeure : la portabilité se spécifie et se simule avant tout achat, essai routier ou montage matériel.

---

## 6 ter. Locataire, droit de sortie et by-pass externe — exigence de conception (19 novembre 2026)

**Décision d'architecture :** le kit ne doit pas présupposer que l'utilisateur est **propriétaire de son logement**. Un **locataire** doit pouvoir acheter/utiliser sa station, la déconnecter au départ et **l'emporter en fin de bail**, sans sacrifice de son investissement ni dépendance à une infrastructure propriétaire laissée sur place. Cette réversibilité est un critère d'**Autonomie de Capacité** et de **non-capture**, pas un avantage accessoire.

### Frontières matérielles et responsabilités

**A — Station OpenPowerHub autonome / amovible (composant utilisateur).** Stockage, pilotage et conversions énergétiques avec entrées/sorties standardisées, sans nécessité de connexion fixe au tableau du logement ; elle fournit directement des appareils ou un sous-ensemble mobile clairement identifié. Elle doit fonctionner sans l'interface de by-pass.

**B — By-pass / sélecteur de sources EXTERNE, facultatif, dissociable de la station.** Accessoire distinct pouvant assurer, selon sa variante, le choix entre réseau et station, le transfert sûr et le retour à l'alimentation normale. Deux sous-cas à **ne pas confondre** :
- **B1 : sélecteur côté charges, lui-même portable**, alimentant uniquement des appareils branchés directement ; il n'intervient pas dans les circuits fixes du logement. Contrôler les protections, la continuité de service si exigée et l'absence de mise en parallèle des sources.
- **B2 : interface de transfert raccordée à des circuits fixes** : modification de l'installation du bâtiment, relevant des exigences de conception, de protection, de vérification et, selon le cas, d'autorisation écrite du propriétaire. Cette interface peut être matériellement distincte et éventuellement déposée en fin de bail, mais pas présumée « portable » sur le plan juridique ou technique.

Il ne faut **jamais** relier la sortie 230 V de la station à une prise murale pour réalimenter le logement. Le dispositif de transfert doit rendre impossible une réalimentation dangereuse du réseau ou une mise en parallèle accidentelle, prévoir les protections adaptées et traiter correctement neutre, terre, différentiels, surveillance de défauts et transition de source. La logique de sécurité ne doit pas dépendre de Cogentia.

### Interposition en tête de tableau : implantation et deux rythmes de réversibilité

**Hypothèse d'usage formulée par le porteur le 19 novembre 2026 :** une *petite intervention réversible* dans l'alimentation **de toute la distribution du logement**, en insérant une **interface externe entre le point de livraison et le tableau de répartition**, puis restitution fonctionnelle de l'état initial au départ du locataire. Une variante plus mobile permet de **retirer et remettre fréquemment la station** sans modifier chaque fois l'installation de puissance.

**Emplacement correct :** ne pas intervenir sur les bornes du compteur Linky ni sur le circuit scellé du distributeur. En configuration courante, le point de livraison est situé aux **bornes de sortie aval du disjoncteur de branchement** (Code de l'énergie D342-1 et guide EDF SEI). L'interface privative se place *en aval* de ce point, sur une installation conçue pour recevoir une source de secours. Dans certaines configurations (branchement type 2, compteur éloigné, tableau séparé), un appareil de coupure générale est présent en plus dans le bâtiment : l'implantation exacte reste à étudier **sur place** et ne se déduit pas de la présence d'un Linky.

**Rythme R1 — fixation de longue durée :** pose/contrôle initial de l'interface de transfert et de ses raccordements au bâti, station amovible utilisée pendant le bail, puis dépose de l'interface et remise en état vérifiée au départ si l'accord et la configuration le prévoient.

**Rythme R2 — station fréquemment mobile :** interface de transfert **fixe côté tableau** avec liaison **dédiée, protégée et prévue pour des connexions répétées** côté station. Quand la station est absente, l'interface doit fournir un chemin réseau normal et sûr par défaut ; le déplacement ordinaire de la station **ne doit jamais impliquer de rouvrir le tableau ni de déconnecter des conducteurs de puissance**. Connecteurs, séquence de coupure, absence de mise en parallèle et retour au réseau doivent être validés pour le régime électrique envisagé.

**Deux topologies à ne pas mélanger :** (1) système de transfert *réseau OU sortie station* (sources alternatives, interverrouillées) ; (2) alimentation découplée du logement *en permanence par l'onduleur*, avec le réseau utilisé uniquement pour recharger en AC/DC et un **by-pass de secours externe** permettant le retour direct réseau lorsque la station est retirée ou arrêtée. La seconde reflète plus directement le manifeste « désynchronisation permanente », mais demande des vérifications distinctes (temps de commutation, comportement au défaut, surcharge, capacité des protections). L'interface ne doit pas permettre de retour d'énergie au branchement public ; les protections contre la surcharge, les défauts d'isolement, le régime de neutre et la coupure d'urgence doivent être dimensionnés par une personne compétente.

**Hypothèse juridique raisonnable, non conclusion :** la loi du 6 juillet 1989 protège les simples aménagements (art. 6 d) mais soumet les transformations d'équipements loués à l'accord écrit du bailleur (art. 7 f). La **réversibilité**, le faible impact, l'absence de dégradation, le retour à l'état initial et la restauration fonctionnelle **constituent des arguments en faveur d'un simple aménagement**, mais **ne suffisent pas à garantir cette qualification** lorsqu'on modifie le câblage d'arrivée générale. La nature de l'acte prime sur son nom ; pour la variante câblée B2, obtenir un accord écrit est le chemin à faible risque de litige jusqu'à clarification juridique spécifique. Le langage historique « bon père de famille » ne fait pas exception à l'article 7 f. Références : [loi du 6 juillet 1989](https://www.legifrance.gouv.fr/loda/id/LEGITEXT000006069108/), [notice d'information locative 2026](https://www.legifrance.gouv.fr/eli/arrete/2026/10/9/VLOL2619452A/jo/texte), [Code de l'énergie D342-1](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031749079/), [guide EDF SEI Corse](https://corse.edf.fr/sites/sei_corse/files/2026-01/2026-guide_raccordement_sei.pdf) et [Promotelec, protection multi-sources](https://www.promotelec.com/professionnels/fiche/protection-dune-installation-alimentee-par-plusieurs-sources/).

**Reality Test distinct :** temps/coût/risque d'installation, fréquence de retrait de station, fréquence d'intervention sur le tableau (cible : zéro en régime R2), fonctionnement réseau lorsque la station est absente, restitution vérifiable des circuits et **portabilité réelle du capital technique**. Pas de dépense ni chantier enclenchés par cette proposition.

### But de la séparation externe : périmètre réglementaire proportionné, pas exemption automatique

**Hypothèse architecturale recherchée par le porteur :** ne pas transformer artificiellement le cœur portable en onduleur de réseau ou équipement intégré au bâtiment à cause d'un by-pass incorporé en permanence. Les responsabilités de la station et de l'interface propre au logement sont contractuellement, fonctionnellement et physiquement distinctes.

**Réserve déterminante :** la simple localisation externe du by-pass **ne soustrait pas** la station aux exigences qui lui sont propres. Un équipement qui fournit du **230 V AC** peut relever de la [directive 2014/35/UE](https://eur-lex.europa.eu/legal-content/fr/TXT/?uri=CELEX%3A32014L0035) malgré son bus 48 V DC ; la CEM, les batteries, les modules radio et la sécurité du produit exigent leurs propres évaluations selon les usages et la mise sur le marché. Le choix de normes techniques d'essai et l'obligation légale de conformité sont à distinguer. La qualification UPS, station mobile, convertisseur et/ou stockage stationnaire doit résulter des **fonctions réelles et de l'usage annoncé**, jamais d'un jeu de désignation commerciale.

**Droit locatif :** l'article [7 f) de la loi du 6 juillet 1989](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000509310/2026-10-07) soumet en principe les transformations des locaux et équipements loués à l'**accord écrit du bailleur**, sous réserve des exceptions prévues par le texte. L'installation d'un sélecteur dans le tableau doit être examinée en conséquence ; l'usage d'une station autonome sans modification fixe offre le plus faible coût de sortie.

### Réversibilité mesurable : protocole de départ

1. L'usager conserve la propriété et la maîtrise de la station, ses données, sa configuration et ses modules de stockage.
2. La déconnexion ne laisse aucune alimentation dangereuse et ne requiert aucun compte cloud ni licence.
3. Dans le scénario **B1**, l'utilisateur débranche les appareils et part avec la station et son sélecteur, sans toucher au tableau du logement.
4. Dans le scénario **B2**, le retour à l'installation d'origine et l'éventuelle dépose du by-pass sont **planifiés et réalisés/vérifiés** conformément au droit, à l'accord du bailleur et aux règles techniques ; le locataire ne doit pas croire qu'il peut déposer lui-même n'importe quel équipement câblé au tableau.
5. Test de réussite : temps, coût, gestes, interventions professionnelles et pertes matérielles nécessaires pour **quitter le logement sans perdre son autonomie énergétique**.

**Priorité produit révisée (19 novembre 2026) :** conserver **A** autonome et **B1** pour l'usage sans travaux, mais étudier **B2 comme scénario cible à part entière**, puisqu'il permet au locataire d'alimenter l'installation domestique complète par interposition d'une interface réversible en tête de tableau. L'objectif n'est plus de cantonner B2 à une possibilité marginale : il faut en chiffrer la version « installation unique au début / restitution en fin de bail » et la version « interface restant en place / station mobile connectée ou retirée fréquemment ». Chacune doit conserver la sécurité électrique et faire l'objet de la qualification locative appropriée.

---

## 7. Terrains et niveaux de maturité

- **1, cours Paoli, Corte — premier site retenu pour le test grandeur nature** : local de référence de C.O.R.S.I.C.A. / Institut Mariani ; test réel de l'architecture dans un lieu déjà utilisé, sous réserve d'audit de l'installation électrique, des usages, des droits d'intervention, des exigences de sécurité et du financement. Il ne faut pas le confondre avec le cas de la maison urbaine de Corte, qui demeure anonymisé.
- **Minesteggio — deuxième ou troisième site grandeur nature (ordre à déterminer)** : vitrine pédagogique patrimoniale ; étude du solaire et éventuellement de la ressource hydraulique locale, sous réserve d'autorisations, de relevés et de contraintes patrimoniales. À considérer dans les conditions d'accès au réseau très contraint : 1 kW disponible ou aucun réseau, selon configuration à préciser.
- **La Maison Blanche, La Gaude — deuxième ou troisième site grandeur nature (ordre à déterminer)** : terrain d'essai reproductible pour une habitation individuelle, avec expérimentation d'une alimentation réseau plafonnée à 1 kW ou absente, selon la configuration réellement disponible.
- **Maison urbaine de Corte** : cas préexistant, **anonymisé**, de désengagement réversible du réseau et véhicule comme stockage mobile ; ne pas lever l'anonymat.
- **Musée Mariani des Possibles** : démonstrateur visible, expérimentation, ateliers et transmission, non site de certification présumée.
- **Commune / FractaVolta** : horizon coopératif ultérieur, distinct du kit individuel.


### Décision de terrain et contrainte de moyens (19 novembre 2026)

**Décision de principe du porteur du projet :** le premier **test grandeur nature** d'OpenPowerHub 48V aura lieu au **local du 1, cours Paoli à Corte** (et non à Minesteggio ni dans le cas-pilote anonymisé de maison urbaine). Ce choix désigne un **site cible**, pas une installation réalisée ni une promesse de calendrier.

**Séquence des tests grandeur nature (19 novembre 2026) :** **1, cours Paoli → [Minesteggio, La Maison Blanche]**, ces deux derniers sites étant envisagés après le premier **sans ordre arrêté**. La **station portable embarquée** est un **quatrième cas d'usage transversal**, et non un site supplémentaire dans cette chronologie. Le critère commun à tester est un **accès très limité au réseau public**, avec deux régimes de conception possibles : **appoint limité à environ 1 kW** ou **aucun raccordement utilisable**. La correspondance précise entre site et régime reste **à vérifier** ; ne pas attribuer d'office l'un des deux régimes à un lieu. La valeur de 1 kW est une **puissance**, pas une réserve énergétique ni une consommation journalière ; elle doit être vérifiée comme puissance réellement accessible, et distinguée du contrat en kVA et de la production hydroélectrique locale éventuelle.

**Hypothèses de test complémentaires :** régime *grid-limited* : charge lente du tampon depuis le réseau sous plafond physique de puissance ; régime *off-grid* : énergie solaire et stockage avec gestion explicite des épisodes sans production ; dans les deux cas, délestage sûr, priorisation des fonctions essentielles, calcul d'autonomie et retour au mode dégradé. Ne pas conclure à la faisabilité avant relevé de la demande et de la production. L'absence actuelle de budget demeure la contrainte de calendrier.

**État actuel : aucun budget disponible pour lancer l'expérimentation.** Le démarrage matériel est donc **ajourné, sans date** ; aucune commande, aucun achat et aucune modification électrique ne sont autorisés par cette décision. Ne pas convertir ce site cible en projet immédiatement opérationnel dans les communications publiques.

**Phase zéro sans dépenses nouvelles**, réalisable au fil de l'eau si les données sont disponibles : inventorier les équipements et circuits existants, compiler les relevés de consommation et de puissance accessibles, définir les fonctions essentielles du local, établir les contraintes d'installation (propriété, autorisations, sécurité, assurance), simuler les profils d'énergie avec des données réelles, tenir une nomenclature indicative distinguant matériel possédé / prêt possible / achat requis, et établir des critères de réussite mesurables. Aucune intervention sur le tableau ou raccordement expérimental sans compétence et vérification appropriées.

**Condition de passage au prototype :** financement identifié, architecture de sûreté revue, coût complet chiffré et risques réglementaires clarifiés. Le pilote grandeur nature vient **après** les essais de banc et de prototype hors réseau. Les autres terrains demeurent des cas complémentaires ou de réplication ultérieure.

### Jalons proposés

- **M0 — Documentation** : schéma fonctionnel, BOM chiffrée et sourcée, hypothèses, matrice de dangers, modèle économique.
- **M1 — Banc DC** : mesure des performances, pertes, sécurité et fonctionnement en mode dégradé sans modification d'une installation domestique.
- **M2 — Banc intégré supervisé** : MPPT, chargeur, stockage, V2L compatible, onduleur certifié ; essais de commutation et documentation.
- **M3 — Installation pilote conforme** : revue indépendante électrique, réglementaire, assurance et garanties.
- **M4 — Kit de formation** : guides ouverts, programme de facilitateurs, essais reproductibles et registre de retours.

## 8. Gouvernance du commun et frontière des métiers

C.O.R.S.I.C.A. / Institut Mariani : **doctrine, recherche, expérimentation et gouvernance du commun**.  
École Mariani : **pédagogie, parcours, formation des facilitateurs et cas-écoles**.  
FractaVolta : **architecture et protocoles énergie, mesure, stockage, routage et éventuelle industrialisation**.  
Cogentia : **couche cognitive, agents mandatés, diagnostic, documentation et traces**.  
FabLabs et praticiens : **adaptation locale, apprentissage, assemblages autorisés, contrôle et maintenance**, selon leurs qualifications effectives.  
Usager : **principal des choix domestiques** ; il doit pouvoir travailler sans la plateforme, changer de fournisseur ou d'accompagnateur et conserver ses données.

Un logiciel ouvert et un kit vendu « à prix coûtant » ne neutralisent ni les obligations de sécurité, ni la responsabilité du fabricant, ni les exigences éventuelles de mise sur le marché. Les licences proposées (CERN-OHL-S, GPLv3, CC BY-SA) sont à confirmer par sous-ensemble et compatibilité, plutôt qu'à déclarer effectives avant publication des sources correspondantes.

## 9. Question centrale pour le Reality Test

**Combien d'autonomie effective le kit apporte-t-il à un foyer, pour quel coût complet, pour quelles fonctions garanties, avec quelle réparabilité, quelle dépendance résiduelle et quelle compétence transférée ?**

Mesures minimales : coût TTC complet, heures d'autonomie par niveau de service, puissance soutenable, disponibilité des fonctions essentielles, pertes mesurées, incidents, facilité du retour à un fonctionnement sûr, nombre d'opérations que la personne sait reproduire et absence de dépendance durable à l'accompagnateur.

Ce test fait d'OpenPowerHub **un objet de l'Autonomie de Capacité**, et non une simple nouvelle électronique domestique.
