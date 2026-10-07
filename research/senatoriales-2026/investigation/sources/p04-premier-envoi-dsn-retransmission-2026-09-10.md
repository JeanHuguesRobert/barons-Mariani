---
title: "P-04 — premier envoi du 10 septembre 2026, échecs de livraison et retransmission allégée"
author: "Jean Hugues Noël Robert"
date: "2026-10-07"
status: "verified-against-gmail"
language: "fr"
document_role: "evidence-index"
document_kind: "email-delivery-chain"
visibility: "public"
lifecycle_state: "active"
inventory_id: "P-04"
---

# P-04 — chaîne technique du premier envoi à la préfecture

## Séquence vérifiée

- **17:01:56 CEST** — premier courriel de candidature au Bureau des élections.
- **17:02:59 CEST env.** — premier DSN d'échec de livraison.
- **17:03:34 CEST env.** — deuxième DSN d'échec.
- **17:04:35 CEST env.** — troisième DSN d'échec.
- Les DSN indiquent que le message était trop volumineux pour le destinataire.
- **17:54:50 CEST** — retransmission allégée explicitant le rejet du premier envoi et le code `552 5.3.4 Message size exceeds fixed limit`.
- **17:56:53 CEST** — accusé automatique du Bureau des élections, conservé comme P-05.

## Portée

Cette chaîne établit :
- la tentative initiale de transmission ;
- l'échec technique pour taille ;
- la réaction du candidat par retransmission allégée ;
- la réception électronique de cette retransmission.

Elle n'établit pas, à elle seule, la conformité juridique du dépôt ni l'inventaire physique présenté le lendemain.

## Production

Pour P-04, conserver dans le dossier de travail :
- le premier message ;
- les trois DSN ;
- la retransmission allégée ;
- idéalement les messages natifs EML/RFC822 et une représentation lisible ;
- SHA-256 des fichiers effectivement produits.

Les identifiants Gmail précis sont conservés dans le registre d'audit Gmail pré-dépôt et n'ont pas besoin d'être répliqués ici.
