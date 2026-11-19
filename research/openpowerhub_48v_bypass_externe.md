---
title: "OpenPowerHub 48V — by-pass externe, réversible et station amovible"
subtitle: "Étude préliminaire d'un inverseur de sources simple en tête de tableau monophasé"
author: "Jean Hugues Noël Robert"
affiliation: "Mariani School of Autonomy / C.O.R.S.I.C.A. / Institut Mariani"
date: "2026-11-19"
status: "working-draft — conception de principe non installable en l'état"
language: fr
visibility: public
lifecycle_state: working
document_role: source
document_kind: research-paper
license: CC BY-SA 4.0
related_documents:
  - research/openpowerhub_48v_rattachement_corpus.md
  - research/ecole_mariani_autonomie.md
  - research/ecole_mariani_autonomie_terrains_pilotes.md
  - research/homeostasie_habitat.md
  - https://github.com/JeanHuguesRobert/FractaVolta/blob/main/docs/energy-packets.md
related_projects:
  - OpenPowerHub 48V
  - FractaVolta
  - The Mariani School of Autonomy
  - C.O.R.S.I.C.A.
---

# OpenPowerHub 48V — by-pass externe, réversible et station amovible

## 1. Résultat de l'étude (19 novembre 2026)

**Hypothèse de référence : installation privative monophasée 230 V, point de livraison identifié, accès à la liaison de tête de tableau, protections existantes recensées, onduleur capable d'alimenter des circuits fixes.** Sous ces conditions, **un inverseur de sources manuel bipolaire à coupure intermédiaire I–0–II et calibre adapté**, dans un petit coffret externe, est une solution simple déjà industrielle. Il n'est pas nécessaire d'ajouter un microcontrôleur, deux relais indépendants artisanaux ni un logiciel de supervision au by-pass. L'inverseur est **un dispositif de transfert électromécanique**, distinct de l'EMS et du Core OpenPowerHub.

Il s'agit toutefois d'une **étude de faisabilité**, et non d'un schéma exécutable. La vérification du neutre et des protections en mode onduleur est un **prérequis bloquant**. Le caractère réversible de l'intervention ne dispense pas de ses obligations électriques ni, automatiquement, de l'accord du bailleur.

## 2. Architecture conceptuelle recommandée : « by-pass séparé, station déplaçable »

```text
  RÉSEAU PUBLIC / LINKY / DISJONCTEUR DE BRANCHEMENT
                         |
                côté privatif aval
                         |
          [Répartition/protection adaptée]
                 /                 \
    Voie RESEAU pour I            Appoint AC/DC dédié à la station
                 |                 (ex. plafond 1 kW, réglable et protégé)
                 |
                 v
           +-----------------------------+
           | COFFRET BY-PASS EXTERNE     |
           | Inverseur 2P I -- 0 -- II  |
           |  I   = réseau direct       |
           |  0   = isolement sortie    |
           |  II  = station             |<-- connectique AC dédiée
           +-----------------------------+        ^
                         |                       |
          Tableau de répartition existant         |
          et ses protections / circuits          |
                                              OpenPowerHub
                                       onduleur AC 230 V monophasé
```

Note : figure **fonctionnelle**, ni schéma de câblage ni plan de mise en œuvre. Un appareil à deux pôles coupe les conducteurs actifs phase et neutre ; la **terre de protection ne se commute pas**. L'alimentation du chargeur depuis le réseau doit être prise **en amont de l'inverseur**, sur un circuit spécialement protégé : jamais en aval du tableau alimenté par l'onduleur, afin d'éviter de charger la batterie depuis sa propre sortie. La dérivation ne doit pas consister à coincer plusieurs conducteurs non autorisés sous une borne du disjoncteur de branchement.

**Deux modes à ne pas confondre :**
- **Mode simple de transfert** : réseau direct (I), station (II), position hors tension (0). Toute bascule **interrompt brièvement** l'alimentation.
- **Mode désynchronisation habituelle** : station en position II pour alimenter les charges ; réseau vu comme **chargeur AC/DC plafonné** ; I constitue le **by-pass direct de secours** en cas de retrait, panne ou maintenance de la station. L'inverseur n'a pas besoin de convertir l'énergie.

Le dispositif est **non automatique** dans la version initiale. Lorsque la station est retirée, l'utilisateur bascule manuellement vers I ; l'absence de station n'impose aucun travail dans le tableau. La commutation peut couper temporairement les équipements : les appareils qui ne tolèrent aucune coupure conservent leur propre réserve locale, à étudier séparément.

## 3. Deux rythmes d'utilisation

**R1 — Longue durée locative.** L'interface est posée une fois, OpenPowerHub reste raccordé, et en fin de bail l'interface peut être retirée par intervention appropriée et la continuité/protection de la distribution d'origine rétablie, contrôlée et documentée.

**R2 — Station mobile fréquente.** L'interface de tête reste en place ; **seule la connexion de la station** est défaite et rétablie. Le connecteur d'entrée source doit être prévu pour ce cycle : protection de toute partie active au toucher, interdiction de la déconnexion en charge hors matériel expressément dimensionné, procédure de sélection de source et protection contre tout retour réseau. La connectique ne doit **jamais** impliquer l'utilisation de deux fiches mâles reliées par câble ou la réalimentation d'une prise domestique.

Une solution industrielle candidate pour la liaison station → coffret est une **entrée d'appareil P17 / IEC 60309 230 V bleu 2P+T, calibre 32 A**, à valider avec la fonction de sectionnement et la sortie onduleur. Le câble de liaison, l'arrimage et la protection mécanique restent à dimensionner.

## 4. Composants candidats du commerce — non validés comme ensemble

| Élément | Exemple vérifié | Rôle | Ordre de grandeur TTC |
|---|---|---|---|
| Inverseur manuel | [Hager SF263 2P 63 A I–0–II](https://hager.com/fr/catalogue/produits/sf263-inverseur-2-poles-63a-i-0-ii) | Transfert électromécanique de deux sources | **48 €** prix constaté chez [Domomat](https://www.domomat.com/53569-inverseur-2p-63a-i-0-ii-hager-sf263.html), novembre 2026 |
| Coffret externe | [Hager VE110F IP55, 8+2 modules](https://hager.com/fr/catalogue/produits/ve110f-coffret-etanche-ip-55-8-10-modules) | Enveloppe isolante, rail DIN et capot | **48 €** chez [Blanc Habitat](https://www.blanc-habitat.com/hager/308600-coffret-etanche-vector-ip55-1-rangee-82-modules-h-210mm-l-237mm-hager-ve110f) |
| Connectique station | [Legrand P17 230 V 2P+T 32 A](https://www.legrand.fr/pro/catalogue/socle-de-tableau-a-entraxe-reduit-p17-2pt-32a-230v) | Branchement/débranchement de la source portable | **30–100 € estimés** pour les deux extrémités et le câble, selon références/longueur |
| Répartition, protections, raccordement | Composants conformes au dimensionnement réel | Disjoncteur de branche station, dérivation chargeur, borniers, câbles, presse-étoupes, signalétique | **60–180 € estimés**, hors éventuelle remise à niveau des différentiels |

**Estimation indicative des seuls matériels : environ 180–380 € TTC**, si l'installation initiale est saine et les protections aval adaptées. Ajouter un coût de pose, contrôle et éventuelle dépose/remise en état. Une enveloppe **environ 450–1 100 € installé** n'est qu'une **hypothèse budgétaire**, non un devis, et peut être dépassée si le tableau doit être repris. Un matériel additionnel peut être exigé par l'analyse de défaut, le schéma de liaison à la terre, la limitation de puissance ou les exigences du lieu. L'interface externe n'est pas comprise dans l'objectif non démontré de kit OpenPowerHub « complet < 900 € ».

**Attention au calibre :** pour un abonnement et disjoncteur de branchement pouvant délivrer 60 A, la **voie réseau** et le transfert en tête de toute la distribution exigent un calibre compatible, d'où l'intérêt d'un inverseur 63 A. En **mode station**, 6 kW / 230 V ≈ **26,1 A** : liaison de source candidat 32 A **avec protection adaptée**, jamais 63 A sans limitation de la voie station. La puissance disponible ne peut être supérieure aux capacités réelles de l'onduleur et de la batterie. Si l'appoint réseau n'offre qu'**1 kW**, le by-pass direct ne crée **aucune puissance supplémentaire**.

## 5. Ce qui est simple et ce qui ne l'est pas

Le **mécanisme** de bascule I–0–II est standard, éprouvé, simple et peu coûteux. Les points techniques réellement discriminants résident ailleurs :

1. **Implantation et monophasé/triphasé.** À placer sur la **partie privative en aval du disjoncteur de branchement**, non sur les bornes du Linky ni sur des équipements scellés. Si l'habitation est **triphasée**, le schéma 2P ne s'applique pas ; la prise 230 V monophasée de la station ne remplace pas à elle seule un réseau triphasé. L'accessibilité réelle, la propriété des composants et les éventuelles parties communes doivent être vérifiées.
2. **Réseau et station ne doivent jamais se mettre en parallèle**, même lors d'une panne ou d'un branchement erroné. Choisir un appareil spécifiquement destiné au **transfert de sources**, à coupure intermédiaire mécanique éprouvée, plutôt que deux contacteurs indépendants sans interverrouillage.
3. **Protection des personnes en mode onduleur.** Le différentiel présent sur l'installation ne doit pas être supposé fonctionnel avec un onduleur à sortie flottante. Il faut étudier le régime du neutre et de la terre de **chacune des sources** et la coordination avec les DDR 30 mA, la coupure sur défaut, les protections contre surintensité et les courants de court-circuit limités de certains onduleurs. Exemple industriel : [Victron MultiPlus-II 230 V, installation](https://www.victronenergy.com/media/pg/MultiPlus-II_230V/fr/installation.html), documentant un relais de terre/neutre en mode onduleur et la présence obligatoire de protections aval adaptées. Ce n'est **pas** une recette de liaison N–PE artisanale.
4. **Prise de station et mobilité.** Connecteur conçu pour la puissance, la température, l'humidité et les cycles de connexion ; parties accessibles protégées, aucun connecteur mâle laissé sous tension, pas de branchement sur une prise murale de retour. La terre de protection doit rester continue selon les exigences du système.
5. **Contrôle des puissances.** En mode I, le réseau peut autoriser une puissance bien supérieure à celle de la station. En mode II, la sortie de la station doit s'interrompre ou délester avant surcharge, y compris à l'appel de courant de moteurs. Un tampon de 410 Wh ne fournit 6 kW que **4,1 minutes théoriques**, avant pertes.
6. **Transfert et disponibilité.** Le mode manuel est une coupure brève, et non une ASI sans coupure. L'automatisme éventuel peut être ajouté plus tard sur spécification réelle ; il n'est pas nécessaire à la réversibilité. L'IA et le cloud n'ont aucune autorité de sécurité électrique.
7. **Conformité ciblée.** La [NF C 15-100](https://www.promotelec.com/faq/particuliers/toute-installation-realisee-anterieurement-a-la-date-dhomologation-dune-norme-doit-elle-etre-systematiquement-revisee-selon-les-nouveaux-textes-reglementaires/) doit être prise en compte pour la partie modifiée ; une modification n'oblige pas automatiquement à rénover **tout** un logement ancien. Les prescriptions applicables au coffret assemblé et éventuellement vendu, à sa protection et à l'installation doivent être identifiées selon le mode de diffusion réel.
8. **Locataire.** La [loi du 6 juillet 1989 (art. 7 f)](https://www.legifrance.gouv.fr/loda/id/LEGITEXT000006069108) n'autorise pas à qualifier d'office ce changement de l'alimentation générale de « simple aménagement » du seul fait qu'il est réversible. La faible ampleur et la restauration intégrale sont des arguments sérieux, mais une mise en place câblée dans le tableau peut être une transformation ; l'**accord écrit du bailleur** est la voie de précaution jusqu'à qualification précise.

## 6. Tests préalables requis (en banc puis par compétence électrique)

**Test V0 :** mode I, logement alimenté par réseau ; station absente ; aucune partie accessible dangereuse. **V1 :** position 0, tous conducteurs actifs isolés comme prévu ; impossibilité de coupler les deux sources. **V2 :** mode II, réseau indépendant de l'onduleur, aucune réalimentation du branchement public. **V3 :** chargeur réseau activé depuis dérivation amont indépendante sans boucle via tableau. **V4 :** station défaillante, surchargée, batterie vide, différentiel ou surcharge simulée ; mise en sécurité et restauration manuelle depuis I. **V5 :** connexion/déconnexion répétée de la station sans ouverture du tableau. **V6 :** contrôle des DDR, terre, neutre et temps de coupure à partir de mesures adaptées aux deux sources. **V7 :** départ locataire : restitution fonctionnelle et électrique contrôlée.

Pour **1, cours Paoli** : avant toute nomenclature définitive, mesurer ou obtenir une photographie lisible du type d'alimentation (mono/tri), du DB, de l'arrivée au tableau, de la puissance souscrite et disponible, de l'état des protections et de l'espace libre. **Aucune intervention sur les circuits sous tension.** Pas de budget et pas d'achat à ce stade ; la phase suivante reste documentaire.

## 7. Décision de conception proposée

Retenir comme **référence M0** le coffret **OpenPowerHub Transfer Box — Manual 63A 2P** :
- inverseur **I–0–II** mécanique éprouvé, sans logique programmable ;
- liaison de station par connecteur dédié courant 32 A si 6 kW réel, avec protection adaptée et absence de connecteurs exposés sous tension ;
- départ chargeur réseau indépendant et plafonné, lorsque l'architecture choisit le mode « onduleur permanent » ;
- séparation matérielle du cœur OpenPowerHub, permettant d'emporter la station ;
- validation impérative du schéma terre/neutre/protections avant qu'aucun bâtiment ne soit raccordé ;
- automatisme, commutation sans coupure, supervision et produits triphasés **hors périmètre initial**.

**Évaluation synthétique :** faisabilité **forte** de l'inverseur externe simple ; **coût matériel limité**, mais coût de pose non nul ; **risque technique principal** : protections en mode onduleur et qualification de l'interface bâtiment ; **risque juridique** : qualification de la modification locative. La simplicité mécanique n'est pas une dispense de sécurité.

## 8. Sources consultées

- [Hager SF263 — inverseur 2P 63 A I–0–II](https://hager.com/fr/catalogue/produits/sf263-inverseur-2-poles-63a-i-0-ii) ; [prix TTC constaté](https://www.domomat.com/53569-inverseur-2p-63a-i-0-ii-hager-sf263.html).
- [Hager VE110F — coffret IP55](https://hager.com/fr/catalogue/produits/ve110f-coffret-etanche-ip-55-8-10-modules).
- [Legrand P17 — connectique industrielle 230 V 32 A](https://www.legrand.fr/pro/catalogue/socle-de-tableau-a-entraxe-reduit-p17-2pt-32a-230v).
- [Victron MultiPlus-II — installation et relais de terre](https://www.victronenergy.com/media/pg/MultiPlus-II_230V/fr/installation.html).
- [Promotelec — protection d'une installation multi-source](https://www.promotelec.com/professionnels/fiche/protection-dune-installation-alimentee-par-plusieurs-sources/).
- [Promotelec — modifications et application des normes aux installations anciennes](https://www.promotelec.com/faq/particuliers/toute-installation-realisee-anterieurement-a-la-date-dhomologation-dune-norme-doit-elle-etre-systematiquement-revisee-selon-les-nouveaux-textes-reglementaires/).
- [Légifrance — loi du 6 juillet 1989](https://www.legifrance.gouv.fr/loda/id/LEGITEXT000006069108).
