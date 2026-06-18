---
title: "Retour d’expérience pipeline — Note de Campagne n°3 : le cas EDF"
subtitle: "Double document, revue adverse, arbitrage humain et stabilisation versionnée"
status: "method note — case study"
version: "0.1"
date: "2026-06-18"
author: "Jean Hugues Noël Robert"
license: "CC BY 4.0"
language: "fr"
corpus_role: "pipeline feedback"
related_documents:
  - "cas_edf.md"
  - "cas_edf_blogpost.md"
  - "research/review_protocol.md"
  - "research/second_method.md"
  - "JeanHuguesRobert/cogentia/research/pipeline.md"
ai_assisted_by:
  - "ChatGPT"
  - "Grok"
  - "Claude"
human_validation_required: true
---

# Retour d’expérience pipeline — Note de Campagne n°3 : le cas EDF

## 1. Objet

Ce document conserve le retour d’expérience méthodologique issu de la production de la **Note de Campagne n°3 : le cas EDF**.

L’objectif n’est pas de redire le fond du dossier EDF, Calacuccia, Ricanto ou FractaVolta. L’objectif est de documenter la pipeline réellement pratiquée : exploration, stabilisation technique, produit public, revue adverse, arbitrage humain, correction, publication GitHub.

Ce cas est important parce qu’il porte sur un sujet politiquement sensible, économiquement massif et juridiquement risqué. Il montre donc assez bien ce qu’une pipeline doit savoir faire quand l’enjeu n’est pas seulement littéraire ou conceptuel.

## 2. Séquence observée

La séquence réelle a été :

```text
intuition politique
→ cadrage révélateur / stabilisateur
→ recherche des chiffres et sources
→ dossier technique cas_edf.md
→ blogpost grand public cas_edf_blogpost.md
→ revue adverse Grok / Claude
→ arbitrage humain
→ corrections bloquantes
→ v0.4 release candidate
→ publication GitHub partielle
```

Cette séquence confirme que la pipeline n’est pas un circuit linéaire. Elle se comporte comme un réseau de transformation de paquets cognitifs : chiffres, images, objections, formules, sources, demandes politiques et contraintes juridiques circulent entre plusieurs formes.

## 3. Artefacts produits

### 3.1 Document source technique

`cas_edf.md`

Fonction : document source, fond technique, sources, calculs, niveaux de preuve, objections, demandes institutionnelles.

Rôle : préserver la structure profonde du raisonnement et éviter que le produit public ne devienne le seul porteur du dossier.

### 3.2 Produit public dérivé

`cas_edf_blogpost.md`

Fonction : article Substack / campagne, registre émotionnel, pouvoir d’achat, image de la manne solaire, vulgarisation de l’Autonomie de Capacité.

Rôle : rendre le dossier lisible pour un public non technique sans porter toute la charge probatoire.

### 3.3 Revue adverse

La revue Grok / Claude a identifié les vulnérabilités principales de la version grand public :

- projections par famille trop exposées ;
- exposition excessive de FractaVolta ;
- section FUD trop imputable à EDF ;
- vocabulaire d’intention ;
- extrapolation hydraulique trop spectaculaire ;
- nécessité de fourchettes et de prudence sur les hypothèses.

### 3.4 Version stabilisée

La v0.4 a intégré les corrections essentielles :

- suppression des projections par famille ;
- remplacement du chiffre unique Calacuccia par une fourchette ;
- suppression du terme FUD dans le blogpost ;
- déplacement de FractaVolta en déclaration d’intérêts ;
- clarification technique MW pilotable / MW de pompage / MWh stockés ;
- vérification volumétrique de la STEP 1 GWh ;
- conservation de l’impact politique sans surjouer l’accusation d’intention.

## 4. Ce qui a bien fonctionné

### 4.1 Double forme source / dérivé

La séparation entre dossier technique et blogpost a été décisive.

```text
document source = fond, sources, objections, niveaux de preuve
produit dérivé = forme publique, image, circulation, mobilisation
```

Sans cette distinction, le texte aurait probablement été soit trop lourd pour le public, soit trop vulnérable aux critiques techniques.

### 4.2 Revue adverse

La revue adverse a fonctionné comme test anti-boomerang.

Elle n’a pas seulement corrigé le style. Elle a identifié les points que l’adversaire aurait pu utiliser pour discréditer l’ensemble du dossier.

### 4.3 Arbitrage humain

Le rôle des agents est resté non souverain.

```text
Grok / Claude critiquent
ChatGPT restructure
Jean Hugues arbitre
GitHub stabilise
```

Ce schéma est conforme à la seconde méthode : les agents produisent des objections et des transformations possibles ; l’auteur décide.

### 4.4 Passage au plateau

Le plateau a été atteint quand les objections nouvelles sont devenues principalement répétitives ou déjà traitées.

À ce stade, la bonne règle est :

```text
corrections factuelles oui
réécriture doctrinale non
```

Le document entre alors en release candidate.

## 5. Ce qui a moins bien fonctionné

### 5.1 Erreur d’aiguillage des revues

Deux fichiers de revue transmis au cours du processus portaient sur un autre document du corpus.

Effet : bruit, perte d’attention, risque d’intégration hors sujet.

Correction méthodologique : toute revue doit désormais déclarer explicitement ses documents cibles, versions cibles et portée.

### 5.2 Risque de commit prématuré

Le processus a rappelé une règle de prudence : ne pas publier sur GitHub avant autorisation explicite lorsque le document est encore en revue.

Protocole retenu :

```text
draft local
→ revue
→ arbitrage
→ lien de téléchargement
→ autorisation explicite
→ commit GitHub
```

### 5.3 Exposition du conflit d’intérêts

La présence de FractaVolta dans le blogpost créait un risque politique : l’adversaire pouvait dire que le dossier EDF servait à placer une société privée.

Arbitrage :

- FractaVolta reste explicitée dans le document technique ;
- le blogpost garde une déclaration d’intérêts ;
- le récit public parle d’abord d’architecture territoriale.

## 6. Objections et décisions

| Objection | Gravité | Décision | Effet |
|---|---:|---|---|
| Projections par famille | Bloquante | Intégrée | Supprimées du blogpost |
| FractaVolta trop visible | Bloquante | Intégration partielle | Déplacée en déclaration d’intérêts |
| Section FUD | Bloquante | Intégrée | Supprimée / remplacée par retournement du sens technique |
| « Confisquée » / « scandale » | Forte | Intégrée | Remplacé par vocabulaire moins intentionnel |
| Calacuccia 146 M€/an trop haut | Forte | Intégrée | Fourchette 70–146 M€/an |
| Parc hydraulique extrapolé trop brutalement | Forte | Intégrée | Présenté comme gisement théorique à expertiser |
| 56,8 MW à sourcer | Moyenne | Partielle | Marqué comme hypothèse / référence de calcul |
| MW pilotable vs MW pompage | Moyenne | Intégrée | Clarification technique ajoutée |

## 7. Règles extraites

### Règle 1 — Toujours séparer source et dérivé

Un sujet sensible doit avoir au minimum :

```text
source.md
blogpost.md
review.md
integration_report.md ou retour_experience.md
```

### Règle 2 — Toute revue doit être routée

Une revue sans cible explicite n’est pas intégrable.

Champs minimaux :

```yaml
review_target:
  repository:
  files:
  reviewed_version:
  reviewed_commit:
  review_scope:
```

### Règle 3 — Les objections doivent devenir des décisions

Une bonne revue ne suffit pas. Il faut une table :

```text
objection → gravité → décision → effet
```

### Règle 4 — Le plateau est un statut méthodologique

Le plateau n’est pas la vérité finale. C’est le moment où la réécriture commence à produire moins de valeur que le risque de dilution.

À partir du plateau :

- corrections factuelles ;
- corrections juridiques ;
- corrections de source ;
- pas de refonte doctrinale sans nouvelle information majeure.

### Règle 5 — Le conflit d’intérêts se traite par architecture, pas par silence

Quand un projet personnel est impliqué, il faut :

- déclarer l’intérêt ;
- séparer le récit public et la note technique ;
- expliciter la gouvernance anti-capture ;
- montrer que la solution sert d’abord l’intérêt territorial.

## 8. Formule méthodologique

> La pipeline a fonctionné parce qu’elle a articulé exploration, double production, critique adverse, arbitrage humain et stabilisation versionnée. Son principal défaut opérationnel observé est l’absence initiale de contrôle d’aiguillage des revues. Son amélioration prioritaire est donc un protocole minimal de review ciblée.

## 9. Continuation

Actions utiles :

1. créer ou maintenir `research/review_protocol.md` ;
2. envisager une référence à ce cas dans `cogentia/research/pipeline.md` lors d’une future v0.5 ;
3. créer éventuellement des Issues GitHub pour :
   - expertiser STEP Calacuccia 1 GWh ;
   - vérifier cadre juridique autorité concédante / EDF ;
   - produire visuel Ricanto vs Calacuccia-STEP ;
   - produire fiche « 3 demandes concrètes ».

## 10. Statut final

Ce retour d’expérience est un artefact méthodologique, non un document de campagne.

Il sert à conserver la trace de la méthode appliquée, afin que les prochains dossiers sensibles ne repartent pas de zéro.
