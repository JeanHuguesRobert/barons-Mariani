---
title: VIGILIA
subtitle: Système distribué d'évitement des collisions, de signalement et de perception territoriale
version: 1.3
date: 2026-05-12
author: Jean Hugues Noël Robert, baron Mariani
address: 1 cours Paoli, F-20250 Corte
contact: jeanhuguesrobert@gmail.com
license: CC BY-SA 4.0
spdx-license-identifier: CC-BY-SA-4.0
status: Document de conception ouvert
repository: github.com/JeanHuguesRobert/barons-Mariani
predecessor: vigilia.md v1.2 (2026-05-12), v1.1 (2026-05-12), v1.0 (2026-04-17)
canonical_url: https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/vigilia.md
last_stamped_at: 2026-05-15
---

# VIGILIA

## Système distribué d'évitement des collisions, de signalement et de perception territoriale

**Version : 1.3**
**Auteur : Jean Hugues Noël Robert**, baron Mariani — 1 cours Paoli, F-20250 Corte
**Contact :** jeanhuguesrobert@gmail.com
**Contexte : Déploiement rural — Corse (phase pilote)**
**Date : 2026-05-12**

---

## Note sur le nom

*Vigilia* — du latin, veille, garde de nuit. Le nom marque l'intention : **veiller, non surveiller**. Le système éclaire des situations dangereuses ; il ne classe pas des comportements humains.

---

# 1. Résumé exécutif (lecture double)

## Lecture politique (élus ruraux)

VIGILIA est un système léger, non intrusif et peu coûteux permettant de réduire significativement les accidents entre véhicules et animaux en zone rurale, sans recourir à des clôtures systématiques, infrastructures lourdes ou mesures de contrainte généralisée.

Il transforme la mobilité quotidienne des habitants, des visiteurs et des services publics en réseau de vigilance partagé.

La version 1.1 a ajouté une couche de signalement humain : un usager peut signaler un danger lié à la présence d'un animal potentiellement en divagation, demander un renseignement local ou transmettre une observation utile, y compris depuis un téléphone simple ou ancien.

La version 1.2 ajoute :

* un cas d'usage **lutte contre le vol de bétail**, qui retourne le rapport de force politique avec les éleveurs ;
* un **modèle adversaire** explicite ;
* un **mode dégradé** garantissant que la panne du système ne dégrade pas le territoire en dessous de son état antérieur ;
* un positionnement clair vis-à-vis du corpus FractaVolta / MareNostrum / DHITL.

VIGILIA ne se substitue ni aux services d'urgence, ni aux pouvoirs de police du maire, ni aux forces de sécurité. Il ajoute une couche de qualification, d'accessibilité et de transmission locale.

---

## Lecture technique (ingénieurs)

VIGILIA est une architecture de capteurs distribués basée sur deux familles de signaux :

1. des signaux automatiques, issus de balises LoRaWAN basse consommation portées par des animaux ou des ressources mobiles ;
2. des signaux humains, issus de signalements vocaux, SMS, interfaces web légères, bornes locales ou passerelles GSM expérimentales.

La couche automatique exploite des mesures de puissance de signal (RSSI) et de mobilité GPS pour reconstruire des champs probabilistes de présence par mise à jour bayésienne légère.

La couche humaine ajoute des observations explicites, qualifiées par un mécanisme de triage : urgence, signalement non urgent ou renseignement local.

Le système est **conçu pour échouer doucement** : la perte de n'importe quel composant fait revenir le territoire à son état antérieur, pas en dessous.

---

# 2. Problématique territoriale (Corse)

Les territoires ruraux présentent un problème structurel multidimensionnel :

* divagation animale (bovins, ovins, caprins, équins, ânes, chiens) ;
* **vol de bétail** — chronique, sous-déclaré, en hausse ;
* visibilité limitée sur les routes secondaires ;
* routes étroites, sinueuses ou de montagne ;
* coûts élevés des infrastructures de protection (clôtures, passages canadiens, ouvrages fixes) ;
* tension entre usage agricole, circulation routière, présence touristique et vie quotidienne ;
* responsabilité juridique souvent diffuse en pratique entre propriétaires, communes, usagers et services de l'État, alors qu'elle est en droit assez claire (CGCT art. L2212-2 et L2213-2 ; Code rural et de la pêche maritime, articles L211-19-1 et suivants).

Les solutions actuelles sont :

* coûteuses ;
* statiques ;
* localisées ;
* parfois socialement conflictuelles ;
* peu adaptées aux situations mouvantes ou récurrentes ;
* inopérantes face au vol nocturne.

VIGILIA propose une approche complémentaire : produire une information territoriale dynamique, progressive et partagée, exploitable à la fois par les autorités, les éleveurs et les usagers de la route.

---

# 3. Principe général de VIGILIA

VIGILIA repose sur une idée simple :

> Transformer des signaux faibles, radio ou humains, en information de sécurité exploitable.

Le système ne cherche pas nécessairement à localiser précisément les animaux. Il cherche à détecter leur présence probable ou constatée dans une zone critique.

**VIGILIA-AUTO** détecte les présences probables.

**VIGILIA-SIGNAL** recueille les présences constatées.

Ensemble, ils produisent une perception territoriale distribuée, orientée vers la sécurité, la prévention et la coordination locale.

## 3.1 Positionnement dans le corpus

VIGILIA prolonge une question centrale, posée à plusieurs échelles dans le corpus de l'auteur : *comment des agents autonomes coordonnent-ils leur action sans centre capturable ?*

La balise animale, le téléphone du signaleur, le véhicule récepteur, la borne communale, le PC de crise sont des nœuds de pair égal. Aucun n'est indispensable. Le système se reconstruit par redondance et par mobilité. Cette logique relie VIGILIA :

* à l'architecture **N2N** des réseaux énergétiques de FractaVolta (nœud-à-nœud, indifférent au type) ;
* au principe **DHITL** (Democratic Humans In The Loop) du corpus MareNostrum ;
* à la doctrine **store-and-forward** des réseaux mesh de crise.

VIGILIA est donc, dans ce corpus, l'instance la plus tangible et la moins théorique : un cas d'usage rural où la coordination sans centre n'est ni un slogan ni un papier, mais un service rendu à des communes confrontées à des problèmes concrets.

---

# 4. Architecture système

## 4.1 Vue d'ensemble

```text
                 ┌──────────────────────────┐
                 │        VIGILIA           │
                 │ perception territoriale  │
                 └─────────────┬────────────┘
                               │
        ┌──────────────────────┴──────────────────────┐
        │                                             │
┌───────▼────────┐                          ┌─────────▼─────────┐
│ VIGILIA-AUTO   │                          │ VIGILIA-SIGNAL    │
│ capteurs radio │                          │ signalement humain│
└───────┬────────┘                          └─────────┬─────────┘
        │                                             │
balises LoRa animales                         téléphone / SMS / GSM hérité
véhicules capteurs                            appel vocal / DTMF
RSSI + GPS                                    signalement danger
champ probabiliste                            renseignement local
        │                                             │
        └──────────────────────┬──────────────────────┘
                               ▼
                      carte de risque locale
                               │
                               ▼
                 PC de crise / mairie / gendarmerie
                               │
                               ▼
                    réseau mesh store-and-forward
```

---

## 4.2 Couche animale (balises LoRaWAN)

Chaque animal équipé porte une balise :

* technologie : LoRa / LoRaWAN ;
* ultra basse consommation ;
* émission périodique d'un identifiant **anonyme et tournant** (rolling ID cryptographique) ;
* autonomie longue durée (multi-annuelle) ;
* coût cible : faible (~10–20 €).

Fonction :

* émission de signaux radio intermittents ;
* contribution passive à un champ de présence probabiliste ;
* preuve de présence opposable en cas de litige ou de vol.

Le mapping `identifiant tournant → animal → propriétaire` est connu uniquement du propriétaire et, sur requête légale, des autorités. Il n'est pas exposé au public ni aux véhicules récepteurs.

---

## 4.3 Couche véhicule (récepteurs embarqués)

Chaque véhicule volontaire devient un capteur mobile :

* smartphone (GPS + calcul + réseau) ;
* ou module USB LoRa compatible ;
* ou récepteur embarqué léger ;
* réception passive des signaux animaux ;
* mesure RSSI (intensité du signal).

Aucun matériel lourd embarqué requis.

---

## 4.4 Couche signalement humain (VIGILIA-SIGNAL)

VIGILIA-SIGNAL ajoute une interface humaine multi-canal :

* appel vocal classique ;
* SMS ;
* interface web légère ;
* QR code local ;
* borne communale ;
* téléphone GSM ancien avec SIM ;
* passerelle GSM héritée expérimentale (cf. §10) ;
* opérateur humain en PC de crise.

Cette couche permet de recueillir :

* un danger immédiat ;
* une présence animale constatée ;
* une présence récurrente ;
* une demande de renseignement local ;
* un signalement non urgent ;
* une **anomalie d'éleveur** (animal disparu, signal perdu, soupçon de vol).

---

## 4.5 Couche réseau (agrégation distribuée)

Les véhicules, bornes et points d'accès transmettent :

* timestamp ;
* position GPS ou localisation déclarée ;
* intensité du signal radio lorsqu'elle existe ;
* identifiant anonymisé de balise détectée ;
* type de signalement humain ;
* niveau de priorité ;
* statut de traitement.

Ces données sont agrégées dans un backend léger, local ou hybride.

---

## 4.6 Couche d'inférence

Le système reconstruit :

* zones de probabilité de présence animale ;
* gradients de proximité ;
* évolution temporelle des risques ;
* zones de récurrence ;
* points noirs routiers ;
* signaux faibles de crise locale ;
* **anomalies** : disparitions brutales, déplacements incompatibles avec la marche d'un animal.

Il ne s'agit pas d'un GPS animal généralisé, mais d'un champ de présence probabiliste enrichi par des observations humaines.

---

## 4.7 Mode dégradé (graceful degradation)

VIGILIA est conçu pour échouer doucement. Aucune panne ne doit faire passer le territoire **en dessous** de son état antérieur.

```text
Panne                          | Comportement attendu
-------------------------------|------------------------------------------------
Couverture LoRa réduite        | Champ de présence vieillit, alertes par historique
Backend central indisponible   | Véhicules mesurent localement, sync différée
PC de crise injoignable        | Mesh store-and-forward vers commune voisine
Internet rompu                 | Mode local autonome, voix + SMS opérateur
Réseau GSM rompu               | Bornes communales, mesh véhicules
Brouillage radio               | VIGILIA-SIGNAL humain continue
Panne totale du système        | Retour au baseline territorial, pas en dessous
```

Principe : **VIGILIA n'introduit aucune dépendance nouvelle dont la perte rendrait le territoire plus vulnérable qu'avant son installation.**

---

# 5. Modèle de fonctionnement (lecture ingénieur)

## 5.1 Signal automatique

Chaque véhicule mesure :

* RSSI(t) ;
* variation de RSSI sur trajectoire ;
* corrélation avec mouvement GPS ;
* horodatage ;
* position du récepteur.

---

## 5.2 Formulation probabiliste minimale

Pour chaque cellule spatiale `c` et chaque identifiant balise `a`, le système maintient une probabilité de présence :

```text
P(a ∈ c | o₁..oₙ) ∝ P(a ∈ c) × ∏ᵢ P(oᵢ | a ∈ c)
```

avec :

* `P(a ∈ c)` : prior spatial (zones d'habitude, saison, heure, météo) ;
* `P(oᵢ | a ∈ c)` : modèle de propagation RSSI, fonction décroissante de la distance et des obstacles ;
* `oᵢ = (RSSIᵢ, pᵢ, tᵢ)` : observation i-ème (mesure, position du récepteur, temps).

Aucun de ces termes n'est connu précisément en milieu rural montagneux. C'est pourquoi le système ne produit **pas de positions**, mais des **zones de présence probable**, mises à jour à chaque passage de véhicule équipé.

C'est aussi pourquoi la performance s'améliore non linéairement avec le nombre de véhicules : chaque trajectoire transverse à une zone réduit la variance du champ.

---

## 5.3 Exploitation du mouvement

Le déplacement du véhicule transforme un signal faible en information exploitable :

* variation spatiale du signal ;
* effets d'ombre et de diffusion ;
* convergence multi-observateurs ;
* reconstruction progressive d'un champ local.

---

## 5.4 Fusion multi-véhicules

Plusieurs véhicules équipés permettent :

* triangulation probabiliste ;
* réduction de variance ;
* amélioration non linéaire de la précision ;
* mise à jour dynamique de la carte de risque.

---

## 5.5 Signal humain

Un signalement humain est traité comme une observation explicite :

```text
observateur humain
→ canal d'entrée
→ triage
→ fiche événement
→ intégration dans la carte de risque
→ transmission éventuelle au PC de crise
```

Exemple de fiche, format JSON minimal et stable :

```json
{
  "event_id": "DIV-2026-05-12-0042",
  "timestamp": "2026-05-12T14:32:11Z",
  "source": {
    "type": "human_voice",
    "channel": "voice_gsm_legacy",
    "callback_requested": false
  },
  "location": {
    "commune": "Corte",
    "declared": "route D14 km 3, virage de la chapelle",
    "coordinates": null
  },
  "subject": {
    "category": "animal_divagation",
    "species": "bovin",
    "count": 3,
    "danger_to_circulation": true
  },
  "priority": "urgent",
  "status": "transmitted_mairie_gendarmerie",
  "history": [
    { "at": "2026-05-12T14:32:11Z", "action": "received" },
    { "at": "2026-05-12T14:32:18Z", "action": "triaged_urgent" },
    { "at": "2026-05-12T14:32:25Z", "action": "transmitted_pc_crise" }
  ]
}
```

Ce schéma est volontairement plat, exportable en CSV, compatible Git, conçu pour rester lisible sans outillage.

---

## 5.6 Sortie système

Le système produit :

* cartes de risque dynamiques ;
* alertes locales embarquées ;
* zones de vigilance renforcée ;
* journal des signalements ;
* fiche événement qualifiée ;
* informations publiques locales ;
* flux prioritaire vers PC de crise ;
* notifications privées au propriétaire en cas d'anomalie sur ses animaux.

---

# 6. Principe de performance

La performance dépend de :

* densité de véhicules équipés ;
* densité de balises animales ;
* régularité de circulation ;
* densité des signalements humains ;
* qualité du triage ;
* capacité de transmission locale ou différée.

Propriété clé :

> le système s'améliore avec l'usage.

Chaque passage de véhicule, chaque signal faible, chaque observation humaine utile améliore la perception territoriale.

---

# 7. Cas d'usage 1 — Évitement des collisions

## Objectif

Réduire les collisions entre véhicules et animaux en divagation ou proches d'une route.

## Fonctionnement

* détection d'une balise à proximité ;
* variation du signal avec mouvement du véhicule ;
* estimation d'une zone de présence probable ;
* alerte conducteur (visuelle / sonore).

## Effet attendu

* réduction des accidents ;
* adaptation préventive de la vitesse ;
* diminution des conflits d'usage du territoire ;
* meilleure connaissance des zones récurrentes ;
* documentation cartographique pour gestionnaires de voirie.

---

# 8. Cas d'usage 2 — Suivi distribué de ressources mobiles

## Objectif

Assurer la visibilité de ressources mobiles critiques :

* batteries de véhicules électriques ;
* conteneurs énergétiques mobiles (paquets AC du réseau FractaVolta) ;
* équipements logistiques circulants ;
* matériels de crise ;
* ressources mobiles en réseau Energy Packet.

## Fonctionnement

* chaque ressource possède un identifiant radio ;
* les véhicules et infrastructures détectent ces signaux ;
* reconstruction de trajectoires probabilistes ;
* absence de dépendance à une infrastructure centralisée unique.

## Effet attendu

* meilleure coordination logistique ;
* réduction des pertes et incertitudes ;
* robustesse en zones rurales ou déconnectées ;
* compatibilité avec une logique de réseau store-and-forward.

---

# 9. Cas d'usage 3 — Signalement humain des dangers liés à la divagation animale

## Objectif

Permettre à tout usager, même sans smartphone ou sans accès Internet, de signaler la présence d'un animal potentiellement en divagation lorsqu'elle crée un danger.

## Catégories de signalement

```text
1. Urgence immédiate
   accident, personne blessée, animal sur route, danger direct

2. Signalement non urgent
   animal vu, présence récurrente, divagation sans danger immédiat

3. Renseignement local
   consignes, état des signalements, météo, routes, abris, contacts utiles
```

## Doctrine de triage

Principe central :

> Dans le doute → urgence.

En l'absence de doute :

```text
1 = urgence
2 = renseignement
3 = signalement non urgent
```

Le système ne déclare jamais seul qu'une situation n'est pas urgente. Il accepte seulement la déclaration explicite et confirmée de l'usager.

## Menu vocal type

```text
Vous êtes connecté au service local de signalement des dangers.

Si une personne est blessée, si un accident vient d'avoir lieu,
ou si un animal menace directement des personnes ou la circulation,
appuyez sur 1.

Pour demander un renseignement local non urgent,
appuyez sur 2.

Pour signaler un animal en divagation sans danger immédiat,
appuyez sur 3.

En l'absence de choix clair, votre appel sera traité comme une urgence potentielle.
```

## Effet attendu

* réduction du délai de signalement ;
* meilleure qualification des dangers ;
* aide aux communes ;
* documentation des zones récurrentes ;
* diminution des conflits entre automobilistes, éleveurs, habitants et autorités ;
* réemploi de terminaux simples dans une logique d'économie circulaire.

---

# 10. Cas d'usage 4 — Lutte contre le vol de bétail

## Pourquoi ce cas d'usage change la donne politique

Le vol de bétail est en Corse un problème chronique, sous-déclaré et coûteux pour les éleveurs. Les animaux sont chargés de nuit dans des véhicules ; les enquêtes aboutissent rarement.

Tant que VIGILIA est perçu comme un outil d'observation des animaux, les éleveurs y voient une contrainte ou une surveillance. **Le cas anti-vol retourne ce rapport de force** : VIGILIA devient un instrument **au service** de l'éleveur, contre une menace réelle.

Ce retournement est politique avant d'être technique. Il transforme les éleveurs de sceptiques en alliés du déploiement.

## Fonctionnement

Pour un cheptel volontairement équipé :

* chaque animal porte une balise à identifiant tournant cryptographique ;
* seul l'éleveur (et sur réquisition légale, les autorités) connaît la table `id → animal` ;
* le réseau de véhicules récepteurs et de bornes locales constitue un champ d'observation passif, 24h/24, sans coût supplémentaire pour l'éleveur ;
* l'éleveur reçoit une **alerte d'anomalie** lors :
  * d'une disparition brutale du signal d'un animal ;
  * d'un déplacement à vitesse incompatible avec la marche (animal en véhicule) ;
  * d'un franchissement de zone définie (clôture virtuelle légère).

## Preuve de diligence

Au-delà de l'anti-vol, le système fournit à l'éleveur **une preuve horodatée de présence et de mouvement** de ses animaux. Cette preuve est utile :

* en cas d'accusation de divagation ;
* en cas de litige avec un voisin ou un usager ;
* en cas de contestation administrative ou d'assurance ;
* pour appuyer une demande d'indemnisation après prédation ou catastrophe.

## Effet attendu

* dissuasion du vol par augmentation du risque pour le voleur ;
* élucidation accélérée des vols commis ;
* renforcement de la position juridique des éleveurs diligents ;
* alliance politique éleveurs / élus / VIGILIA, au lieu d'un front éleveurs contre tout dispositif.

---

# 11. Accès robuste par téléphones simples ou GSM hérités

## Principe

Un vieux téléphone GSM n'est pas seulement un déchet électronique. Dans une infrastructure de crise, il peut devenir un terminal humain minimal :

* voix, clavier, écran, autonomie, robustesse, simplicité d'usage.

VIGILIA peut accepter des signalements par plusieurs canaux, dont une **passerelle GSM héritée expérimentale** destinée aux situations de faible connectivité, de crise ou de réemploi de terminaux anciens.

## Phasage : ce qui est nécessaire et ce qui ne l'est pas

> **La passerelle GSM héritée n'est pas un prérequis de la v1.x.**

La preuve par l'usage peut et doit commencer sans elle :

* numéro vocal classique pris en charge par un opérateur ;
* SMS via numéro court opérateur ;
* formulaire web léger ;
* QR codes locaux ;
* opérateur humain au PC de crise.

La passerelle GSM héritée est une **ambition v2+** qui ouvre l'usage de terminaux anciens sans abonnement, mais qui demande un travail réglementaire dédié (cf. §11.3 et §20.4).

## Rôle exact de l'accès GSM hérité

L'accès GSM hérité n'est pas le cœur de VIGILIA. C'est une interface d'accessibilité robuste de moyen terme.

```text
Service principal  : signalement divagation animale + anti-vol
Canal moderne      : web / smartphone / QR / SMS opérateur
Canal robuste      : appel vocal / vieux GSM / cellule locale
Transport de crise : mesh
Destinataire       : PC communal ou intercommunal de crise
```

## Position réglementaire de principe

La passerelle GSM expérimentale doit être conçue comme un élément optionnel et encadré :

* pas de réseau mobile commercial ;
* pas de publicité ;
* pas d'accès Internet général ;
* pas de substitution au 112, 15, 17, 18 ou 114 ;
* pas d'émission radio hors cadre autorisé ;
* expérimentation préalable en cage RF avant toute demande extérieure ;
* demande d'autorisation temporaire d'utilisation de fréquences (ANFR / ARCEP) si émission publique.

---

# 12. Information locale non commerciale

VIGILIA-SIGNAL peut fournir un service local d'information publique, strictement non commercial.

**Services acceptables :** météo locale, état des routes, points d'eau, abris ouverts, consignes municipales, présence médicale, heures de permanence, risques incendie, état du réseau électrique, état du réseau mesh, messages officiels (mairie, préfecture, PC de crise), signalement d'un animal perdu ou dangereux.

**Services exclus :** publicité, promotion commerciale, vente, démarchage, profilage, collecte de données inutile, réseau social généraliste, messagerie privée non liée à la crise ou à la sécurité locale.

Principe :

> Le canal local non urgent n'est pas un média commercial. C'est un service minimal d'information publique en mode normal ou dégradé.

---

# 13. Coûts et déploiement

## Ordres de grandeur

* balise animale : ~10 à 20 € ;
* module véhicule : ~50 à 100 € (optionnel) ;
* backend logiciel : faible à modéré (cloud léger ou local) ;
* point d'accès local : variable selon technologie ;
* passerelle GSM héritée : prototype expérimental, coût à préciser après phase 1.

## Stratégie de déploiement

* phase 1 : commune pilote, MVP sans radio ;
* phase 2 : couche LoRa pilote sur cheptel partenaire ;
* phase 3 : extension intercommunale + mesh + PC de crise ;
* phase 4 : passerelle GSM héritée (expérimentation autorisée) ;
* phase 5 : généralisation territoriale.

---

# 14. Architecture conceptuelle

VIGILIA s'intègre dans une architecture plus large de perception territoriale :

* signaux physiques → données ;
* observations humaines → événements ;
* données + événements → inférences probabilistes ;
* inférences → décisions locales ;
* décisions → action publique, prévention, information.

Formule synthétique :

> VIGILIA transforme la mobilité, les signaux faibles et les observations humaines en perception territoriale partagée.

---

# 15. Lecture politique (élus)

VIGILIA permet :

* réduction des coûts d'infrastructure ;
* diminution des accidents routiers ;
* approche **non conflictuelle** avec les activités agricoles ;
* solution évolutive et progressive ;
* meilleure documentation des problèmes récurrents ;
* outil d'aide aux communes ;
* information publique locale non commerciale ;
* articulation possible avec un PC de crise ;
* **outil pour les éleveurs** contre le vol de bétail et pour la preuve de diligence ;
* **alliance possible** entre éleveurs, élus, usagers et services de l'État.

Principe central :

> améliorer la sécurité sans transformer le territoire en zone contrainte.

VIGILIA ne vise pas à surveiller indistinctement les éleveurs ou les habitants. Il vise à qualifier les situations dangereuses, orienter le bon signal vers le bon acteur et réduire les risques pour les personnes comme pour les animaux.

---

# 16. Lecture technique (ingénieurs)

VIGILIA est :

* un réseau LoRa opportuniste mobile ;
* un système de fusion bayésienne de signaux faibles (RSSI + observations humaines) ;
* une architecture de localisation probabiliste distribuée ;
* un système edge + backend léger ;
* un problème de reconstruction de champ de présence dynamique ;
* une couche de signalement humain multi-canal ;
* un système de triage urgence / renseignement / signalement ;
* une passerelle potentielle vers réseau mesh store-and-forward ;
* un système conçu pour échouer doucement (cf. §4.7).

---

# 17. Limites connues

* dépendance à la densité de participants ;
* incertitude inhérente (non déterminisme) ;
* précision inférieure à un GPS classique (par conception) ;
* nécessité d'adoption progressive ;
* besoin de gouvernance locale claire ;
* risque de faux signalements ;
* nécessité de distinguer urgence, renseignement et conflit de voisinage ;
* complexité réglementaire de toute passerelle GSM expérimentale ;
* exposition à un modèle adversaire non trivial (cf. §18).

---

# 18. Modèle adversaire (threat model)

Un système qui traite des positions probables d'animaux et des signalements humains en milieu rural tendu doit identifier ses adversaires plausibles **avant** son déploiement, pas après.

## 18.1 Voleurs de bétail

**Capacité :** tentent de capturer, rejouer ou brouiller les émissions LoRa pour masquer un vol.

**Mitigations :**

* identifiant tournant cryptographique côté balise (non rejouable) ;
* mapping `id → animal → propriétaire` connu uniquement du propriétaire ;
* alerte d'anomalie automatique sur disparition de signal ou mouvement véhiculaire ;
* journalisation immuable côté backend.

## 18.2 Voisins en conflit

**Capacité :** signalements de mauvaise foi pour nuire à un éleveur ou un riverain.

**Mitigations :**

* triage humain et corroboration multi-sources avant action ;
* identité du signaleur enregistrée (mais non publiée) pour traçabilité ;
* refus du système de qualifier seul une situation comme « non urgente » ou « malveillante » : la qualification finale est humaine et tracée.

## 18.3 Spéculateurs et promoteurs

**Capacité :** demandent des données agrégées pour argumenter qu'une terre est « inutilisée » et justifier un changement d'usage.

**Mitigations :**

* publication ouverte uniquement à grain temporel et spatial assez large pour empêcher la réidentification ;
* refus de publier des cartes d'absence comme telles (seules des cartes de présence sont publiées) ;
* clause de finalité dans la licence d'usage des données.

## 18.4 Acteurs étatiques curieux hors cadre

**Capacité :** requêtes en volume hors finalité initiale (sécurité publique, divagation, anti-vol).

**Mitigations :**

* rétention minimale : événements bruts ~30 jours, agrégats ~2 ans, anonymisés au-delà ;
* clause de finalité explicite ;
* refus des requêtes en bloc hors procédure légale individualisée ;
* journal des demandes consultable par l'autorité communale.

## 18.5 Brouilleurs et saboteurs

**Capacité :** émission radio pour saturer la bande LoRa, ou destruction physique des bornes.

**Mitigations :**

* mode dégradé (cf. §4.7) : VIGILIA-SIGNAL humain continue ;
* redondance mesh ;
* détection du brouillage comme événement et alerte automatique.

## 18.6 Signaleur malveillant en masse

**Capacité :** générer du bruit pour saturer le triage humain.

**Mitigations :**

* limite de débit par numéro / source ;
* corroboration requise pour escalade automatique ;
* identification du signaleur tracée mais non publiée.

---

# 19. Gouvernance et responsabilité

VIGILIA doit respecter quelques règles simples :

* minimisation des données ;
* finalité explicite : sécurité publique, anti-vol, information locale ;
* transparence du fonctionnement (code ouvert, doctrine publiée) ;
* absence de publicité ;
* absence de profilage commercial ;
* supervision humaine pour les cas ambigus ;
* escalade par défaut en cas de doute ;
* traçabilité des événements significatifs ;
* opt-in explicite des propriétaires d'animaux (aucune balise sans accord) ;
* opt-out toujours disponible ;
* rétention courte (30 jours bruts, 2 ans agrégés, anonymisation ensuite).

## 19.1 Chaîne de responsabilité opérationnelle

La responsabilité opérationnelle doit être clarifiée localement :

* mairie : autorité de proximité, supervision du PC communal ;
* intercommunalité : mutualisation des moyens, supervision technique ;
* PC de crise : opérations courantes et crise ;
* gendarmerie : suites pénales (vol de bétail, accidents) ;
* SDIS : urgences ;
* services vétérinaires ou agricoles : situations sanitaires ;
* propriétaires ou détenteurs d'animaux : opt-in, accès aux données privées sur leurs animaux.

## 19.2 Question ouverte : qui staffe le PC communal ?

En milieu rural, la disponibilité humaine est la ressource la plus rare du système. Trois modèles à examiner :

* **agent communal existant** (secrétariat de mairie, agent technique) avec délégation de fonction ;
* **astreinte mutualisée intercommunale** ;
* **bénévolat encadré** (corps de réservistes communaux, gardes-champêtres, agents de surveillance bénévoles).

Cette question est le **goulot d'étranglement principal** du déploiement et doit être tranchée commune par commune avant tout passage à l'échelle.

---

# 20. Continuation — phases de travail

La continuation s'organise en cinq phases. Chaque phase doit être livrable indépendamment.

## 20.1 Phase 0 — MVP sans radio (preuve par l'usage)

* formulaire web simple ;
* QR codes locaux ;
* numéro vocal opérateur + SMS opérateur ;
* opérateur humain ;
* fiche événement JSON ;
* carte locale de signalements ;
* doctrine de triage opérationnelle ;
* journal exportable Git / CSV.

**Objectif :** prouver la chaîne fonctionnelle, sans complexité radio ni réglementaire. Une commune pilote suffit.

## 20.2 Phase 1 — Couche LoRa pilote

* balises sur un cheptel partenaire (anti-vol motivé) ;
* véhicules volontaires équipés (smartphone ou module USB) ;
* champ de présence reconstruit ;
* alerte d'anomalie côté éleveur ;
* alerte conducteur à proximité de zone à risque.

**Objectif :** prouver la fusion automatique + humain et la valeur du cas anti-vol.

## 20.3 Phase 2 — Mesh et PC de crise communal

* réseau mesh store-and-forward entre véhicules, bornes et PC ;
* résilience en cas de coupure Internet ou GSM ;
* articulation avec FractaVolta (énergie autonome du PC, edge computing).

**Objectif :** prouver la robustesse en mode dégradé réel.

## 20.4 Phase 3 — Passerelle GSM héritée

* banc d'essai en cage RF avec terminaux anciens ;
* serveur vocal local ;
* dossier ANFR / ARCEP d'autorisation temporaire ;
* expérimentation territoriale encadrée.

**Objectif :** ouvrir l'usage de terminaux simples sans abonnement.

## 20.5 Phase 4 — Articulation politique et version anglaise

* identification de communes pilotes au-delà de la première ;
* articulation avec FractaVolta, Institut Mariani, MareNostrum ;
* version anglaise : *VIGILIA — Distributed Animal-Vehicle Collision Avoidance, Human Signaling and Territorial Perception System* ;
* contribution open source ouverte.

**Objectif :** dépasser le pilote, atteindre la lisibilité internationale, ouvrir le code.

## 20.6 Doctrine de croissance

> Un signalement utile entre, il est qualifié, il apparaît sur une carte, il est transmis au bon acteur, puis il laisse une trace exploitable.

Tant que cette chaîne n'est pas démontrée bout en bout en commune pilote, aucune phase supérieure ne se déploie. C'est la condition d'engagement.

---

# 21. Position conceptuelle

VIGILIA est :

> un système de perception territoriale probabiliste basé sur signaux radio faibles, mobilité des observateurs et signalements humains qualifiés.

Son objectif n'est pas de remplacer l'action publique, mais de la rendre plus informée, plus rapide et plus proportionnée.

La divagation animale ne doit pas être traitée seulement comme un désordre à réprimer. Elle peut aussi être comprise comme un symptôme d'un défaut d'infrastructure, d'identification, de responsabilité et de médiation.

Le vol de bétail ne doit pas être traité seulement comme un délit isolé. Il peut aussi être compris comme un signal d'une fragilité collective des éleveurs, à laquelle un dispositif distribué peut répondre.

VIGILIA propose une réponse structurée :

```text
voir plus tôt
qualifier mieux
transmettre au bon acteur
agir proportionnellement
mémoriser les zones récurrentes
prévenir plutôt que subir
```

---

# 22. Conclusion

VIGILIA propose une alternative aux infrastructures lourdes :

> transformer la mobilité quotidienne, les signaux faibles et les observations humaines en réseau de vigilance partagé, capable de réduire les collisions, qualifier les dangers, protéger les éleveurs contre le vol et améliorer la sécurité locale sans contrainte physique généralisée sur le territoire.

La version 1.2 consolide :

* perception automatique (VIGILIA-AUTO) ;
* signalement humain (VIGILIA-SIGNAL) ;
* robustesse territoriale (mode dégradé) ;
* alliance politique (cas anti-vol) ;
* sûreté (modèle adversaire explicite) ;
* phasage clair (MVP sans radio d'abord).

Sa force est de combiner six choses rarement réunies :

```text
perception automatique
+ signalement humain
+ robustesse territoriale
+ alliance avec les éleveurs
+ sûreté assumée
+ déploiement progressif sans dépendance critique
```

VIGILIA-AUTO détecte.

VIGILIA-SIGNAL qualifie.

Le territoire devient plus lisible, donc plus sûr.

---

# 23. Licence

```text
SPDX-License-Identifier: CC-BY-SA-4.0
© 2026 Jean Hugues Noël Robert, baron Mariani
```

Document publié sous licence **Creative Commons Attribution — Partage dans les Mêmes Conditions 4.0 International (CC BY-SA 4.0)**.

Attribution requise :

**Jean Hugues Noël Robert — VIGILIA v1.3 (2026)**

---

# 24. Changelog

* **v1.0** (2026-04-17) — version initiale, couche automatique LoRa, cas collision et suivi de ressources mobiles.
* **v1.1** (2026-05-12) — ajout de VIGILIA-SIGNAL (signalement humain multi-canal), passerelle GSM héritée, information locale non commerciale, doctrine de triage.
* **v1.2** (2026-05-12) — cas d'usage anti-vol ; modèle adversaire explicite ; mode dégradé formalisé ; positionnement dans le corpus (N2N, DHITL, FractaVolta) ; formulation bayésienne minimale ; schéma JSON d'événement ; phasage 5 phases ; license CC BY-SA 4.0 explicite avec SPDX ; harmonisation du nom de l'auteur.
* **v1.3** (2026-05-12) — remplacement systématique du terme juridique « abigeat » par « vol de bétail » pour accessibilité aux destinataires non-spécialistes (élus, agents communaux, usagers) ; mise à jour du contact courriel.
