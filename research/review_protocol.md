---
title: "Protocole minimal de revue ciblée"
subtitle: "Éviter les erreurs d’aiguillage et transformer les objections en décisions"
status: "method note — protocol"
version: "0.1"
date: "2026-06-18"
author: "Jean Hugues Noël Robert"
license: "CC BY 4.0"
language: "fr"
corpus_role: "review protocol"
related_documents:
  - "research/second_method.md"
  - "research/case_studies/cas_edf_pipeline_retour_experience.md"
  - "JeanHuguesRobert/cogentia/research/pipeline.md"
ai_assisted_by:
  - "ChatGPT"
  - "Grok"
  - "Claude"
human_validation_required: true
---

# Protocole minimal de revue ciblée

## 1. Objet

Ce protocole définit le format minimal d’une revue externe ou assistée par IA portant sur un document du corpus.

Il répond à un problème observé dans le cas `cas_edf.md` / `cas_edf_blogpost.md` : plusieurs revues avaient été transmises avec un mauvais aiguillage, c’est-à-dire qu’elles portaient en réalité sur un autre document.

Le but est simple :

> **Une revue non routée ne doit pas être intégrée.**

## 2. Principe

Une revue n’est pas une autorité.

Elle est un artefact critique destiné à produire :

- des objections ;
- des corrections ;
- des niveaux de gravité ;
- des recommandations ;
- des points à arbitrer humainement.

La décision finale appartient à l’auteur humain.

## 3. Frontmatter obligatoire d’une revue

Toute revue devrait commencer par un bloc de ciblage explicite.

```yaml
review_target:
  repository: "JeanHuguesRobert/barons-Mariani"
  files:
    - "cas_edf.md"
    - "cas_edf_blogpost.md"
  reviewed_version: "v0.4"
  reviewed_commit: "local draft ou commit sha"
  review_scope: "technical / public / both"
  requested_by: "Jean Hugues Noël Robert"
  reviewer: "Grok / Claude / ChatGPT / humain"
  review_date: "YYYY-MM-DD"
  human_validation_required: true
```

Sans ce bloc, la revue peut être lue, mais elle doit être classée :

```text
status = non_integrable_until_routed
```

## 4. Questions de routage

Avant intégration, vérifier :

1. Le fichier cible est-il le bon ?
2. La version cible est-elle la bonne ?
3. La revue porte-t-elle sur le fond, la forme, le droit, les chiffres, la méthode, ou tout cela ?
4. Les objections sont-elles bloquantes, fortes, moyennes ou stylistiques ?
5. L’auteur a-t-il arbitré ce qui est retenu, rejeté ou différé ?

## 5. Typologie des objections

| Niveau | Signification | Effet par défaut |
|---|---|---|
| Bloquante | Risque de discrédit public, juridique ou factuel majeur | Corriger avant publication |
| Forte | Risque sérieux mais non fatal | Corriger ou justifier explicitement |
| Moyenne | Amélioration utile | Intégrer si coût faible |
| Stylistique | Préférence de formulation | Arbitrage libre |
| Hors cible | Ne concerne pas le document | Ne pas intégrer, sauf méthode générale |

## 6. Table d’intégration obligatoire

Toute intégration de revue devrait produire une table :

| Objection | Source | Gravité | Décision | Effet |
|---|---|---:|---|---|
| Projection par famille | Grok/Claude | Bloquante | Intégrée | Supprimée |
| Conflit d’intérêts | Grok/Claude | Bloquante | Intégration partielle | Déclaration d’intérêts |
| Hypothèse non sourcée | Grok/Claude | Moyenne | Intégrée | Marquée comme hypothèse |

Cette table devient la mémoire de l’arbitrage.

## 7. Statuts possibles après revue

```text
draft               = document exploratoire
reviewed            = revu, objections reçues
revised             = corrigé après revue
release_candidate   = plateau atteint, corrections factuelles seulement
published           = publié
superseded          = remplacé par une version ultérieure
deprecated_claim    = affirmation abandonnée ou corrigée
```

## 8. Règles de plateau

Un document atteint le plateau quand les nouvelles critiques répètent principalement des objections déjà traitées, ou quand les modifications proposées réduisent plus la force du texte qu’elles n’en améliorent la solidité.

À partir du plateau :

- corrections factuelles : oui ;
- corrections juridiques : oui ;
- corrections de sources : oui ;
- simplifications mineures : oui ;
- refonte doctrinale : non, sauf nouvelle information majeure.

Formule :

> **Au plateau, on ne cherche plus le texte idéal ; on protège le texte suffisamment solide.**

## 9. Source / produit dérivé

Pour les sujets sensibles, séparer :

```text
source.md              # dossier technique / corpus anchor
public_product.md      # blogpost, Facebook, LinkedIn, Instagram
review.md              # critique adverse
integration_report.md  # décisions prises après revue
```

Le produit public peut être plus émotionnel, mais il doit rester traçable au document source.

## 10. Déclaration d’intérêts

Quand un projet personnel, économique ou politique est lié au dossier, il ne faut pas le masquer.

Règle :

1. déclarer l’intérêt ;
2. expliquer la gouvernance ;
3. distinguer intérêt général local et revenu commercial ;
4. éviter que le produit public paraisse être une publicité ;
5. conserver la déclaration complète dans le document technique.

## 11. Modèle de demande à un reviewer

```markdown
Tu es reviewer critique adverse, non décisionnel.

Documents cibles :
- <fichier 1>
- <fichier 2>

Versions :
- <version ou commit>

Objectif :
- identifier les objections bloquantes ;
- distinguer risques factuels, juridiques, rhétoriques et politiques ;
- proposer des corrections actionnables ;
- ne pas réécrire tout le document ;
- laisser l’arbitrage final à l’auteur humain.

Format attendu :
1. Synthèse de la thèse.
2. Test de symétrie.
3. Concepts stabilisés.
4. Concepts fragiles.
5. Risques de dérive.
6. Objections fortes converties en actions.
7. Rapport signal/bruit.
8. Recommandations structurelles.
9. Continuation.
```

## 12. Formule finale

> Une revue utile ne remplace pas le jugement humain. Elle rend les objections adressables, les risques visibles et les décisions traçables.
