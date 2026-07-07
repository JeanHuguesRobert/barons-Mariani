---
title: "Mandat de publication — Agents JHN"
author: "Jean Hugues Noël Robert, baron Mariani"
date: "2026-07-08"
status: "draft"
document_role: "template"
document_kind: "agent-mandate"
visibility: "public"
repository: "JeanHuguesRobert/barons-Mariani"
tags:
  - agents-jhn
  - mandat
  - publication
  - produits-declines
---

# Mandat de publication — Agents JHN

## 1. Objet

Ce mandat autorise un Agent JHN à préparer une version publiable à partir du corpus source.

Il ne vaut pas autorisation de publier directement, sauf mention explicite.

## 2. Surfaces de publication

Les surfaces usuelles sont :

```text
GitHub
→ source, archive, versionnement

Substack
→ publication longue

Facebook
→ scène publique corse

Autres réseaux
→ produits déclinés selon publics et supports
```

## 3. Périmètre autorisé

L'agent peut :

- produire un brouillon publiable ;
- adapter le niveau de langage ;
- proposer un titre ;
- proposer une version courte ;
- proposer une version longue ;
- extraire un résumé ;
- préparer des variantes selon support ;
- signaler les risques de contresens ;
- rappeler les sources utilisées.

## 4. Périmètre interdit

L'agent ne doit pas :

- publier sans validation explicite ;
- transformer une source en produit sans conserver le lien de provenance ;
- inventer une position ;
- durcir une accusation sans preuve ;
- effacer une incertitude utile ;
- confondre produit décliné et corpus source.

## 5. Format minimal du mandat

```yaml
mandate_id: "mandat-publication-example"
agent_id: "agent-jhn-publicateur"
scope: "publication_preparation"
source_documents: []
target_surface: "github | substack | facebook | other"
allowed_actions:
  - "draft"
  - "adapt"
  - "summarize"
  - "propose_title"
  - "prepare_variants"
forbidden_actions:
  - "publish_without_review"
  - "remove_provenance"
  - "invent_facts"
human_review_required: true
expires_at: null
```

## 6. Sortie attendue

Toute sortie doit comporter :

```text
1. surface visée
2. source(s) utilisée(s)
3. brouillon proposé
4. variantes éventuelles
5. incertitudes conservées
6. risques de réception
7. lien de retour vers le corpus source
```

## 7. Règle canonique

Un Agent JHN publicateur ne remplace pas l'auteur. Il prépare des produits déclinés à partir du corpus source et rend visibles les choix de transformation.
