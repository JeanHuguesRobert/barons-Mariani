---
title: "Rise & Fall of the Mariani Family — Architecture d'enquête"
subtitle: "Méthodologie en deux passes, grammaire capacitaire familiale et analyse causale des interactions avec l'État"
author: "Jean Hugues Noël Robert"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-09-30"
last_modified_at: "2026-09-30"
version: "0.1"
status: "working-paper"
language: "fr"
license: "CC BY-SA 4.0"
document_role: "project-architecture"
document_kind: "working-note"
visibility: "public"
lifecycle_state: "working"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/rise-and-fall/architecture.md"
update_policy: "UP-DEFAULT-REVIEWED"
provenance:
  origin_type: "issue-continuation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "GitHub issue #94"
  origin_date: "2026-09-29"
  derived_from:
    - "projects/suicide-corse/architecture.md"
    - "research/second_method.md"
    - "research/potentics.md"
    - "research/rational_odysseys_the_possible.md"
    - "musee-mariani/doctrine_musee_mariani_des_possibles.md"
    - "musee-mariani/notes-critiques/preuves-et-incertitudes.md"
review:
  status: "unreviewed"
  reviewed_by: []
---

# Rise & Fall of the Mariani Family — Architecture d'enquête

## 0. Statut et objet

Cette note formalise l'**architecture d'enquête** du projet *Rise & Fall of the Mariani Family*.

Elle gouverne la méthode d'investigation historique, le modèle causal, la grammaire capacitaire et les protocoles de vérification contradictoire appliqués à l'étude de la famille Mariani.

Elle ne constitue ni un récit prédéterminé, ni une table des matières littéraire figée.

Son rôle est d'assurer que l'enquête fonctionne comme un dispositif scientifique et falsifiable, capable d'être surpris, contredit ou réorienté par les découvertes d'archives.

## 0.1. Changement d'échelle revendiqué : famille ↔ Corse

*Rise & Fall* est à l'échelle de la **famille Mariani** ce que *Suicide Corse* est à l'échelle de **Marie-Louise** : dans les deux cas, une petite échelle fortement documentée est mise en dialogue avec la grande échelle corse.

```text
Suicide Corse
Marie-Louise / individu      ↔ Corse

Rise & Fall
famille / générations        ↔ Corse
```

Ce parallélisme est méthodologique, non causal. Il sert à tester la robustesse des invariants capacitaires lors d'un changement de résolution.

La circulation entre les deux projets doit être explicite et bidirectionnelle :

- [Architecture de *Suicide Corse*](../suicide-corse/architecture.md) ;
- [Point d'entrée de *Suicide Corse*](../suicide-corse/README.md) ;
- pivot électoral déjà matérialisé : [1863 ↔ 2026](investigation/notes/2026-09-30-echo-electoral-1863-2026.md).

Les objets communs restent des **ponts**, jamais des fusions de dossiers. À ce jour :

1. **capacité politique / contestation électorale** ;
2. **capacité patrimoniale / conserver et transmettre ce qui est déjà acquis**.

Pour le second objet, *Rise & Fall* doit instruire comme épisodes distincts les expropriations ou pertes patrimoniales rapportées aux générations successives de la famille, tandis que *Suicide Corse* examine le cas contemporain du 53 rue Séguier et des œuvres/archives de Marie-Louise. Le changement d'échelle vers la Corse porte ensuite sur le foncier, le logement, les usages du sol et les formes documentées de dépossession territoriale.

La discipline reste :

```text
petite échelle
→ mécanisme documenté
→ invariant candidat
→ test à grande échelle
→ différences et objections
→ retour à la petite échelle
```

et non :

```text
histoire familiale
→ généralisation automatique à la Corse
```


---

## 1. La question de recherche : Attrition institutionnelle vs Hypothèse nulle

### 1.1. L'hypothèse de travail
Le point de départ de l'enquête est formulé ainsi :

> **Dans quelle mesure, par quels mécanismes institutionnels précis, et avec quels contrefactuels plausibles l'État français et ses émanations ont-ils contribué à la perte progressive de capacité économique, patrimoniale, juridique, sociale ou intergénérationnelle de la famille Mariani ?**

### 1.2. L'impératif de l'hypothèse nulle
Pour éviter l'écueil classique du biais de confirmation (chercher uniquement les traces qui accusent la puissance publique), l'architecture impose d'évaluer à chaque étape l'**hypothèse nulle** :

> *« L'évolution observée de la famille Mariani relève de la sociologie ordinaire des élites provinciales françaises aux XIXe et XXe siècles (partage égalitaire du Code civil, fiscalité successorale de droit commun, dispersion professionnelle, exode vers les métropoles continentales, désaffection de la rente foncière agricole), sans captation, hostilité ou dysfonctionnement spécifique de l'appareil d'État. »*

La valeur du projet réside précisément dans sa capacité à mesurer l'écart réel entre cette hypothèse nulle et les éventuels mécanismes institutionnels singuliers mis au jour.

---

## 2. Méthodologie en deux passes

L'enquête refuse le récit rétrospectif continu qui reconstruit l'histoire à partir de sa fin connue. Elle impose une discipline en deux mouvements symétriques :

```text
                                PASS A : ARCHÉOLOGIE RÉGRESSIVE
                      (Partir du présent vers les conditions antérieures)
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  État actuel │ ──> │ Verrou t(n)  │ ──> │ Décret t(n-1)│ ──> │ Fait t(n-2)  │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
       ▲                                                              │
       │                                                              ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                       CONFRONTATION & DISCRIMINATION                        │
└─────────────────────────────────────────────────────────────────────────────┘
       ▲                                                              │
       │               PASS B : RECONSTITUTION DES POSSIBLES          │
       │              (Rejouer la chronologie depuis l'origine)       ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Issue t(n)  │ <── │ Événement t2 │ <── │Bifurcation t1│ <── │   État t0    │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
```

### 2.1. Pass A — Archéologie régressive (du présent vers le passé)
Pour chaque perte de capacité, contrainte légale, aliénation patrimoniale ou blocage contemporain constaté :
1. identifier l'état présent observable et documenté ;
2. rechercher la cause directe et immédiate (acte de vente, jugement, imposition, désaccord d'indivision) ;
3. remonter à la condition juridique ou matérielle antérieure ayant rendu cet acte inévitable ou possible ;
4. poursuivre jusqu'à atteindre un état de capacité plein et documenté.

*Risque de la Pass A seul :* illusion téléologique et causalité imaginaire (post hoc ergo propter hoc).

### 2.2. Pass B — Reconstitution prospective des Possibles (du passé vers le présent)
Repartir de l'état initial documenté (Antoine Dominique Mariani au Premier Empire, 1776–1815) et dérouler la chronologie dans le sens ordinaire du temps :
1. cartographier les capacités effectives et les portes ouvertes à la date $t$ ;
2. identifier l'événement, la décision ou le choc intervenu ;
3. enregistrer les possibles fermés, les capacités dégradées, mais aussi les capacités préservées ou réouvertes ;
4. identifier les alternatives alors effectivement praticables (contrefactuels admissibles) ;
5. passer à la bifurcation suivante $t+1$.

### 2.3. Règle de convergence
Une hypothèse causale issue de la Pass A n'est validée que si elle résiste au déroulement de la Pass B sans nécessiter de chaîne magique ou d'omission d'alternatives disponibles.

---

## 3. Grammaire capacitaire appliquée à la famille

Le projet adapte la grammaire multi-échelle $X_s(t) = (R_s, \Phi_s, C_s, A_s, Q_s, B_s, T_s)$ formalisée dans *Suicide Corse* au substrat de la famille Mariani :

### 3.1. Les composantes
- **$R$ (Ressources) :**  
  Domaines fonciers (Minesteggio, Venzolasca, Corte, Bastia), biens bâtis (château, chapelle, maisons), liquidités, rentes, titres nobiliaires et distinctions, capital relationnel et d'influence politique.
- **$\Phi$ (Facteurs de conversion) :**  
  Régimes matrimoniaux, droit des successions (Code civil vs droit coutumier), fiscalité (droits de mutation, enregistrement), règles d'accès aux fonctions publiques, juridictions compétentes, transports continent-Corse.
- **$C$ (Capacités effectives) :**  
  Capacité d'exploiter la terre, de construire, d'entretenir les bâtiments, de transmettre le patrimoine intact à la génération suivante, de se faire élire, de peser sur les décisions administratives, d'ester en justice avec succès.
- **$A$ (Actions accessibles et exercées) :**  
  Dépôt de candidature, achat/vente de parcelles, dons aux collectivités (ex. don de 1924), procédures judiciaires, choix de carrières (militaires, médicales, artistiques).
- **$Q$ (Charges, frictions et contraintes) :**  
  Droits de succession élevés, litiges d'indivision, dettes hypothécaires, contestations de limites cadastrales, refus d'autorisations administratives, éloignement géographique.
- **$B$ (Bifurcations et routes alternatives) :**  
  Voies non empruntées mais documentées (ex. recours, arbitrage successoral alternatif, conservation intégrale sous fiducie ou fondation).
- **$T$ (Traces et preuves) :**  
  Actes notariés, registres d'état civil, minutes judiciaires, registres cadastraux, rôles d'imposition, correspondances privées, articles de presse d'époque.

### 3.2. Invariants d'observation
- `OPEN ≠ CAPACITY` : Le fait que la loi reconnaisse le droit de propriété ne garantit pas la capacité financière et administrative d'empêcher la dégradation du domaine.
- `FRICTION ≠ CLOSE` : Une taxe élevée ou une formalité lourde ralentit l'action sans fermer définitivement la possibilité de transmission.
- `LOAD ≠ PREPONDERANCE` : Une dette privée contractée par un membre de la famille peut peser plus lourdement qu'une taxe publique sur le destin d'un bien.

---

## 4. Typologie des mécanismes et décomposition de « l'État »

L'enquête interdit formellement d'employer le mot « l'État » comme un bloc monolithique doté d'une volonté univoque.

Toute interaction doit identifier l'émanation institutionnelle exacte :

```text
                                L'APPAREIL PUBLIC
                                       │
        ┌──────────────┬───────────────┼───────────────┬──────────────┐
        ▼              ▼               ▼               ▼              ▼
  État central    Préfecture     Juridictions     Fiscalité      Communes
  (Ministères,   (Sous-préfet,   (Judiciaire,    (Enregistrement, (Maires,
  Législateur,    Gendarmerie,   Administratif,  Hypothèques,     Conseil
  Régime pol.)    Police)        Contentieux)    Cadastre)        municipal)
```

### Classes d'attribution causale obligatoire
Chaque dossier d'investigation doit classer le mécanisme observé parmi les catégories suivantes :

1. **Contribution publique directe ciblée :** Décision d'une autorité visant ou frappant spécifiquement les biens ou les personnes Mariani (ex. expropriation, refus ciblé d'enregistrement, procès d'État).
2. **Contribution publique indirecte ou d'inertie :** Lenteur administrative, défaut de protection de l'ordre public, blocage cadastral, absence de voies de recours efficaces.
3. **Application neutre de la loi générale :** Mesure frappant l'ensemble des propriétaires ou citoyens sans discrimination (ex. taux général des droits de succession, application des règles d'urbanisme).
4. **Décision privée et familiale endogène :** Arbitrage d'investissement désavantageux, conflit entre cohéritiers, choix de délaisser la gestion agricole, dépenses somptuaires, mésentente conjugale.
5. **Mécanisme économique de marché :** Chute des cours agricoles, dévaluation monétaire, hausse des coûts des matériaux, crise financière générale.
6. **Aléa biologique ou contingent :** Décès prématuré d'un gestionnaire clé, absence de descendance masculine directe, maladie.
7. **Causalité indéterminée / `UNKNOWN` :** Données insuffisantes pour trancher entre plusieurs explications concurrentes.

---

## 5. Le Musée des Possibles : formalisation des contrefactuels

Au sein du **Musée Mariani des Possibles**, la mémoire ne se borne pas à enregistrer ce qui a eu lieu ; elle reconstitue les avenirs qui étaient matériellement à portée de main à chaque carrefour.

### 5.1. Discipline du contrefactuel admissible
Un contrefactuel n'est pas une fiction libre. Il n'est recevable dans l'enquête que s'il respecte les quatre conditions suivantes :
1. **Ancrage temporel strict :** La bifurcation doit partir d'une date et d'un état réels attestés ($t_0$).
2. **Faisabilité matérielle :** Les ressources, les compétences et le droit positif du moment devaient rendre l'alternative concrètement praticable.
3. **Explicitation des hypothèses :** Chaque condition nécessaire à la bifurcation doit être listée (ex. : « Si l'emprunt X avait été souscrit », « Si la transaction amiable Y avait été signée »).
4. **Calcul de distance causale :** La confiance décroît avec le temps. Un contrefactuel immédiat ($t+1$) est beaucoup plus probant qu'une projection à 50 ans ($t+50$).

---

## 6. Règles de preuve et d'éthique

1. **Application de la grille critique du Musée :**  
   Tout fait mentionné reçoit un code de preuve explicite :
   - **E** (Établi par source primaire ou acte authentique) ;
   - **P** (Probable / forte convergence documentaire) ;
   - **S** (Source secondaire ou généalogique non recoupée) ;
   - **D** (Données discordantes entre sources) ;
   - **O** (Question ouverte / blanc d'archive).
2. **Neutralité vis-à-vis des personnes vivantes :**  
   Protection absolue de la vie privée. Aucune pièce confidentielle relative aux successions contemporaines ou aux personnes vivantes ne doit être publiée.
3. **Audit adverse continu :**  
   Chaque monographie d'enquête fait l'objet d'un examen contradictoire préalable identifiant les objections possibles avant toute publication ou gel éditorial.
