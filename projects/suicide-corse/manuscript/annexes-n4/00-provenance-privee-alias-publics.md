---
title: "Provenance privée, référence publique"
author: "Jean Hugues Noël Robert"
date: "2026-10-18"
status: preparation
language: fr
license: CC BY-SA 4.0
document_role: derived
document_kind: annex-method-note
visibility: public
lifecycle_state: working
source_documents:
  - "../../../memory/marie-louise/sources/public.yml"
  - "../../../projects/suicide-corse/architecture.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/docs/plural-source-provenance-contract.md"
---

# Provenance privée, référence publique

Une enquête peut avoir besoin de rester vérifiable sans publier les chemins qui donnent accès à des sources privées.

Depuis le 17 octobre, le Corpus de Marie-Louise applique explicitement cette séparation.

~~~text
source réelle
→ locator privé
→ source canonique privée
→ alias public opaque ML-PUB-*
→ carte / matrice / chapitre / édition
~~~

## Ce qu'un alias public établit

Un identifiant de la forme `ML-PUB-xxxxxx` établit qu'une source canonique existe dans le domaine privé gouverné et qu'elle est reliée au rôle probatoire déclaré dans le Corpus.

Il permet de conserver une référence stable dans les projections publiques sans exposer :

- identifiant Gmail ou Drive ;
- chemin privé ;
- provider ;
- adresse ou identifiant permettant de retrouver directement la source ;
- information sensible contenue dans le nom même du locator.

## Ce qu'il n'établit pas

~~~text
alias public
≠ contenu rendu public
≠ preuve automatiquement suffisante
≠ fait automatiquement vrai
≠ causalité établie
~~~

La distinction est essentielle pour *Suicide Corse*.

Une source peut être authentique et néanmoins soutenir seulement une proposition limitée.

Une trace peut documenter une date sans documenter une intention.

Un témoignage peut documenter une perception sans établir la totalité d'une séquence.

La confidentialité de la source n'allège donc jamais la charge épistémique.

## Vérifiable sans être exposé

Le principe permet de dissocier deux exigences souvent confondues :

~~~text
traçabilité
≠ divulgation intégrale
~~~

La vérifiabilité publique peut porter sur :

- l'existence d'une source canonique ;
- sa classe ;
- son statut de divulgation ;
- le rôle précis qu'elle joue dans une proposition publique ;
- les transformations qui conduisent de la source à la projection.

Le contenu brut peut rester privé.

Cette architecture rend également possible une revue autorisée dans le domaine privé sans faire de l'accès privé une condition de lecture du Livre.

## Une frontière, pas un trou noir

L'opacité du locator ne doit pas devenir une immunité contre la contradiction.

La règle reste :

> **ce qu'une source privée permet d'affirmer publiquement doit rester formulé de manière suffisamment précise pour pouvoir être contesté.**

Lorsque la contestation exige l'examen de la source elle-même, cet examen doit suivre le régime d'accès approprié ; il ne faut ni publier automatiquement la pièce, ni prétendre qu'elle n'existe pas parce qu'elle n'est pas publique.

## Effet éditorial

Cette évolution ne demande pas de réécrire l'histoire de Marie-Louise.

Elle améliore la manière dont les Annexes et le Corpus peuvent soutenir le Livre :

~~~text
Livre
→ proposition intelligible

Annexes
→ référence publique, niveau de preuve, limite

Corpus privé autorisé
→ provenance et source réelle
~~~

Les éditions gelées antérieures ne sont pas réécrites silencieusement. Les futures projections utilisent la nouvelle frontière de provenance.
