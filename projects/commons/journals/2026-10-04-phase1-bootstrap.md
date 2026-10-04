---
title: "Commons — Journal de reprise et bootstrap Phase 1"
description: "Audit de réemploi, revue adverse interne, cartographie d'amitié et synthèse de bootstrap pour l'issue 108."
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-04"
version: "0.1"
status: "working-note"
license: "CC BY-SA 4.0"
language: "fr"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/commons/journals/2026-10-04-phase1-bootstrap.md"
document_role: "journal"
document_kind: "resumption-note"
visibility: "public"
lifecycle_state: "working"
update_policy: "UP-DEFAULT-REVIEWED"
ai_assisted_by:
  - "Antigravity — handler, 2026-10-04"
provenance:
  origin_type: "issue-continuation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "https://github.com/JeanHuguesRobert/barons-Mariani/issues/108"
  origin_date: "2026-10-04"
---

# Journal de reprise — Issue 108 — 4 octobre 2026

**Handler** : Antigravity (Google DeepMind), opérant dans le workspace `C:\tweesic\barons-Mariani`.  
**Baseline commit** : `aa2bc06d03adf8b8a122f8a92fc95c7d2c06117d` (commit de bootstrap de PrivAI, issue 107).  
**Issue** : JeanHuguesRobert/barons-Mariani#108 — « Commons — bootstrap du Livre Vivant « Des communaux au cloud » ».

---

## 1. Audit de réemploi (Reuse Audit)

| Classe | Éléments | Décision & Justification |
|---|---|---|
| **GENERIC** | Grammaire du Livre Vivant (`research/livre_vivant.md`) ; modèle des trois Machines (Empêcher, Explorer, Rendre Capable) et couple Révélateur/Stabilisateur ; surface web statique sans framework lourd (HTML5 sémantique, CSS accessible avec mode sombre automatique) ; formats `llms.txt`, `robots.txt`, `sitemap.xml` | Réemployés directement depuis les patterns éprouvés de *PrivAI*, *DIASPORA* et *Rise & Fall*. |
| **PARAMETRIC** | `corpus.yml` ; `projections/n1-working.yml` ; `site/styles.css` ; pages de contribution et de mentions légales ; schéma conceptuel minimal à 14 descripteurs | Paramétrés pour le projet *Commons* et son identité cible `commons.acorsica.org`. |
| **PROJECT-SPECIFIC** | Les quatre mouvements du manuscrit n°1 (`01-heritages.md`, `02-captures-et-enclosures.md`, `03-renaissances.md`, `04-futurs-possibles.md`) ; cartographie méthodique des sources primaires et secondaires ; 8 fiches d'études de cas complètes ; frise chronologique détaillée « Des communaux au cloud » | Rédigés ex nihilo à partir des sources canoniques du Corpus et de l'historiographie de référence. |
| **MISSING** | Enregistrement d'un profil de Guide dédié ; résolutions DNS actives pour `commons.acorsica.org` ; édition gelée v1.0 formelle | Laissés ouverts conformément aux portes d'autorisation du mandat. |
| **DO NOT REBUILD** | Moteur de rendu dynamique ; système d'authentification utilisateur ; pile RAG ad-hoc ; duplication inutile de la plateforme *Cogentia Commons* | Exclus du périmètre : respect strict du principe de frugalité et de non-duplication. |

---

## 2. Délimitation cardinale : Commons vs Cogentia Commons

L'ambiguïté a été résolue et verrouillée dans tous les documents du projet :
- **Commons** est le grand Livre Vivant généraliste dédié à l'histoire, au présent et aux avenirs possibles des biens communs sous tous leurs substrats (terres, eaux, forêts, code, savoirs, énergie, calcul, cognition).
- **Cogentia Commons** (spécifié dans `research/Cogentia_Commons_Working_Paper.md`) est un cas contemporain précis — un commun cognitif d'exploration possibiliste et de traçabilité épistémique sous contrainte scientifique (Layer 4 du cadre DHITL).
- *Commons* n'est pas *Cogentia Commons*. *Cogentia Commons* est l'une des études de cas analysées au sein du Mouvement IV de *Commons*.

---

## 3. Résultats de l'Épreuve de l'Ouvert-Possible (*Open-Possible Check*)

Cinq questions critiques ont été instruites et formalisées dans le manuscrit (chapitre IV) et la surface publique :

1. **Propriété vs Gouvernance** : Les biens communs sont définis comme des faisceaux de droits d'usage et d'obligations de soin (*governance and stewardship*), et non comme une forme amoindrie de copropriété marchande.
2. **Rivalité physique vs Non-rivalité numérique** : Refus explicite de la fausse symétrie entre les biens de la nature (rivaux, épuisables, nécessitant des règles strictes de rationnement de prélèvement) et les biens d'information (non-rivaux, cumulatifs, où le rationnement d'accès détruit la valeur). Le calcul matériel (*compute*) et l'énergie réintroduisent toutefois de la rivalité physique au cœur du monde numérique.
3. **Souveraineté individuelle et intime** : Rejet de la « mise en commun naïve » des données personnelles. Les données intimes relèvent de la souveraineté inaliénable de l'individu ; seuls les flux agrégés ou impersonnels forment des communs légitimes. Le droit au secret, à la discrétion et à la sécession individuelle reste sanctuarisé.
4. **Le risque du commun capturant** : Reconnaissance historique que des communautés gérant des communs peuvent dégénérer en oligarchies fermées excluant les minorités ou les nouveaux venus. Nécessité de règles de transparence, de garanties de sortie (*exit*) et de voies de recours non violentes.
5. **Abaissement des coûts de coordination par l'IA** : L'intelligence artificielle distribuée permet pour la première fois de surveiller de manière impartiale et sans frais bureaucratiques prohibitifs des règles complexes à grande échelle, ouvrant la voie à des communs territoriaux et mondiaux polycentriques viables.

---

## 4. Revue adverse interne (*Internal Adverse Review*)

*Note méthodologique : Cette revue est rédigée par le même agent handler que celui ayant constitué la tranche de bootstrap. Elle ne constitue pas une revue externe indépendante.*

Objections et fragilités documentées :

1. **Asymétrie de documentation entre histoire et prospective** : Les Mouvements I, II et III s'appuient sur une historiographie éprouvée (Ostrom, Bloch, Thompson, Polanyi, Stallman). Le Mouvement IV repose sur des scénarios, des hypothèses de travail et des prototypes du Corpus (FractaVolta, Cogentia Commons). Cette hétérogénéité épistémique doit rester explicitement signalée aux lecteurs.
2. **L'obstacle capitalistique du compute** : Prôner un « commun du calcul » face à des infrastructures d'entraînement coûtant des centaines de millions d'euros par modèle relève pour l'instant d'une aspiration prospective. Aucun mécanisme de financement public ou coopératif n'atteint aujourd'hui cette échelle hors des géants de la tech.
3. **Risque de romantisme agraire** : Décrire les communaux médiévaux et modernes ne doit pas faire oublier la dureté des disettes, la précarité paysanne et les conflits violents inter-villages qui jalonnaient l'Ancien Régime. Le commun rural n'était pas un paradis bucolique, mais une technique défensive de survie collective sous forte contrainte de rareté.
4. **Vérification du nom de domaine** : Un contrôle DNS local effectué le 4 octobre 2026 confirme que `commons.acorsica.org` ne résout pas. Aucun fichier `CNAME` n'a été inséré dans le dépôt et aucune altération DNS n'a été opérée.
5. **Absence de profil de Guide enregistré** : Comme pour *PrivAI*, le Guide interactif n'est pas branché vers une API externe afin de ne pas présenter une capacité de dialogue non encore configurée.
6. **Maintenance bénévole des communs numériques** : La fragilité du travail bénévole mise en lumière par les crises OpenSSL ou XZ Utils montre que le modèle pur du don sans réciprocité économique atteint des limites structurelles de résilience.
7. **Divergence potentielle entre site web et manuscrit** : En cas de désaccord entre le texte HTML public et les fichiers markdown du manuscrit, la primauté normative appartient au manuscrit git-tracké.

---

## 5. Suite résumable

1. Examen et validation humaine de la présente tranche de bootstrap.
2. Réalisation éventuelle d'une revue externe indépendante du manuscrit n°1.
3. Décision institutionnelle sur la configuration d'un profil de Guide pour Commons.
4. Décision d'infrastructure et d'autorisation expresse pour la configuration DNS et le déploiement public de `commons.acorsica.org`.
