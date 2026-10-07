---
title: "Dépôt dématérialisé de la requête — analyse juridique et probatoire"
author: "Jean Hugues Noël Robert"
date: "2026-10-07"
version: "1.0"
status: "active — pre-filing legal analysis"
language: "fr"
document_role: "operational-legal-note"
document_kind: "dematerialized-filing-analysis"
visibility: "public"
lifecycle_state: "active"
---

# Dépôt dématérialisé — analyse juridique et probatoire

## 1. Point de départ : article 34

L'article 34 de l'ordonnance n° 58-1067 dispose que le Conseil constitutionnel ne peut être saisi que par une **requête écrite adressée** :
- au secrétariat général du Conseil constitutionnel ;
- ou au représentant de l'État.

Le texte n'emploie pas les termes « papier », « original papier » ou « remise physique ».

Il prévoit en outre que le représentant de l'État, lorsqu'il est saisi, **avise par voie électronique** le secrétaire général et assure la transmission de la requête.

Source :
https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000006529992

## 2. CRPA — saisine électronique d'une administration

L'article L.112-8 du code des relations entre le public et l'administration prévoit qu'une personne identifiée peut adresser à une administration, par voie électronique, une demande, déclaration, document ou information, et que l'administration est alors régulièrement saisie sous les conditions du code.

L'article L.112-9 précise que, lorsqu'un téléservice réservé existe pour une démarche, son usage peut s'imposer.

L'article R.112-9-2 prévoit qu'à défaut d'information sur un téléservice, le public peut saisir l'administration par **tout type d'envoi électronique**.

L'article L.112-10 permet cependant que certaines démarches soient exclues par décret.

Sources :
- https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031367348
- https://www.legifrance.gouv.fr/codes/id/LEGISCTA000031367346/

## 3. Accusé électronique et traçabilité

L'article L.112-11 du CRPA prévoit qu'un envoi électronique à une administration fait l'objet d'un accusé de réception électronique ou, lorsque celui-ci n'est pas instantané, d'un accusé d'enregistrement électronique.

L'article R.112-11-1 prévoit notamment que l'accusé comporte la **date de réception** et la désignation du service chargé du dossier.

Sources :
- https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033219980
- https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033288138

## 4. Qualification prudente

Le faisceau textuel permet de soutenir sérieusement :

> qu'une requête adressée électroniquement au **représentant de l'État**, dans un format écrit identifiable et via un canal électronique institutionnel recevable, peut relever du droit général de saisine électronique de l'administration.

Mais ce point n'est pas traité ici comme acquis définitivement pour le contentieux électoral de l'article 34, pour trois raisons :

1. l'article 34 est une procédure contentieuse organique spéciale ;
2. aucune procédure officielle trouvée à ce stade ne dit expressément « le dépôt article 34 peut être effectué par email ou SVE » ;
3. il faut vérifier qu'aucune exclusion réglementaire ou modalité de téléservice spécifique ne s'applique.

Conclusion opérationnelle :

> **mobiliser le canal électronique comme redondance forte et traçable, mais ne pas en faire l'unique canal de dépôt tant qu'une confirmation institutionnelle ou jurisprudentielle explicite manque.**

## 5. Canaux électroniques à mobiliser

### A. Préfecture — SVE / téléservice officiel

La préfecture de Haute-Corse publie une rubrique « Saisir l'administration par voie électronique ».

Priorité : utiliser le téléservice / formulaire officiel correspondant aux services de l'État si un chemin approprié permet de viser le représentant de l'État.

### B. Préfecture — adresses institutionnelles déjà actives

Les adresses institutionnelles déjà utilisées dans le dossier ont émis des accusés automatiques et humains.

Si utilisées pour le dépôt :
- objet explicite ;
- identité complète ;
- mention « requête article 34 » ;
- paquet figé en pièces jointes ou lien institutionnel stable si limite de taille ;
- demande expresse d'accusé comportant date/heure et identification du service ;
- envoi parallèle à plusieurs boîtes institutionnelles pertinentes ;
- conservation du MIME/EML complet et des DSN/AR.

### C. Conseil constitutionnel

À ce stade, aucun téléservice officiel spécifique de dépôt dématérialisé des contestations parlementaires n'a été identifié dans les recherches effectuées.

Un courriel direct au Conseil, s'il est possible, doit donc être qualifié **copie de traçabilité / tentative de remise électronique**, sauf confirmation explicite du secrétariat général qu'il vaut saisine.

## 6. Paquet électronique canonique

Le paquet numérique doit être aussi, voire plus, traçable que le papier :

- PDF de la requête ;
- PDF de l'annexe chronologique ;
- bordereau ;
- pièces ;
- manifeste ;
- fichiers natifs utiles ;
- SHA-256 de chaque fichier ;
- manifeste global SHA-256 ;
- date/heure de gel ;
- version ;
- éventuellement archive ZIP/TAR contenant exactement le paquet ;
- empreinte de l'archive ;
- conservation du message EML d'envoi ;
- conservation de tout AR/AE/DSN.

Invariant :

~~~text
support dématérialisé
≠ preuve plus faible

si
identité + intégrité + horodatage + réception + contenu exact
sont mieux documentés.
~~~

## 7. Doctrine de traçabilité

Le choix du numérique n'est pas seulement pratique.

Il permet de documenter séparément :
- ce qui a été produit ;
- quand ;
- sous quelle version ;
- avec quelle empreinte ;
- par quel canal ;
- ce que le destinataire a effectivement reçu ou accusé ;
- quelles transformations ont eu lieu.

Cette architecture est cohérente avec la doctrine de **Traçabilité des actes** : rendre l'acte engageant vérifiable sans transformer la personne en objet de surveillance.

## 8. Stratégie recommandée

Utiliser en parallèle :
1. remise physique préfecture ;
2. saisine électronique préfecture / SVE ;
3. envoi électronique aux boîtes institutionnelles déjà actives ;
4. si confirmé, remise électronique directe au secrétariat général ;
5. remise physique redondante à Paris si possible.

Tous ces canaux doivent transporter le **même paquet figé**.

## 9. Chronologie critique du 7 octobre 2026 — existence du document et disponibilité du lien

Pour l'analyse probatoire du dépôt, quatre événements doivent être distingués sans les confondre :

1. **Le PDF de la requête existait matériellement avant 18 h.** Il avait été produit et matérialisé dans GitHub sous forme de snapshot REVIEW avant les envois institutionnels.
2. **Les envois de saisine / transmission ont été effectués avant 18 h**, entre 17:48:42 et 17:49:25 CEST.
3. **Deux réceptions institutionnelles sont positivement attestées avant 18 h** : la Préfecture de la Haute-Corse et son Bureau des élections ont chacun émis à 17:49:24 CEST un accusé indiquant explicitement que « le présent accusé de réception atteste de la réception de votre saisine ».
4. **Le résolveur public communiqué dans les courriels a connu une défaillance temporaire distincte.** Entre 17:58:20 et 18:01:21 CEST, l'URL
   `https://jhn.baronsmariani.org/cc/requete-conseil-constitutionnel-haute-corse-2026.pdf`
   répondait HTTP 200 mais retournait encore la page HTML du site. Après réactivation des builds Netlify et nouveau déploiement, cette même URL a été vérifiée à **18:05:05 CEST** comme servant effectivement un PDF valide :
   - HTTP 200 ;
   - `Content-Type: application/pdf` ;
   - signature initiale `%PDF-` ;
   - taille 200935 octets ;
   - SHA-256 `2968cbe0a5de0f5e279e70d28c0769d4a8dbf8ca8f6f7e4571864333ecaa02a0`.

### Qualification probatoire

La panne temporaire du chemin HTTP public **ne doit pas être reformulée comme une inexistence de la requête avant 18 h**.

Elle affecte un **mécanisme d'accès** à un document qui existait déjà matériellement. La chronologie doit donc conserver quatre catégories indépendantes :

~~~text
existence matérielle du document
≠ envoi
≠ réception de la saisine
≠ disponibilité correcte du résolveur HTTP
~~~

Cette distinction est essentielle pour toute analyse ultérieure de la preuve du dépôt et de sa transmission.

