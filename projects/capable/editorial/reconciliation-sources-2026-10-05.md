---
title: "Capable — concordance des sources historiques du 5 octobre 2026"
date: "2026-11-15"
document_role: operational
document_kind: reconciliation-register
visibility: public
lifecycle_state: working
status: working-paper
related_issue: "https://github.com/JeanHuguesRobert/barons-Mariani/issues/152"
---

# Capable — concordance du commit historique fc6f6bcb

**Périmètre :** 17 chemins présents dans le dossier projects/capable/ du commit archivé fc6f6bcb (snapshot du 10 octobre) mais absents sous leur ancien nom dans main. Le dossier de récupération demeure conservé sur Fracta2. Une disparition de chemin n'est ni une perte de contenu ni une preuve de convergence.

Ce registre est une **preuve de qualification, pas une attestation d'édition gelée, de publication ou de disponibilité d'un ancien site**. Il ne remplace pas la projection en préparation.

| Chemin historique (préfixe projects/capable/) | Disposition et source actuelle |
| --- | --- |
| cases/case-01-parrainages-presidentielle-2027.md | Remplacé par [Cas 02 : parrainages](../cases/case-02-parrainages-presidentiels-verrou-rural.md), plus détaillé, non relu |
| cases/case-02-effectivite-service-public-rural.md | Remplacé par [Cas 05 : dématérialisation rurale](../cases/case-05-dematerialisation-service-public-rural.md), non relu |
| deploy/README.md | Ancienne configuration capable.lepp.fr, non à réinstaller telle quelle ; voir [édition en préparation](../editions/2026-10-09-en-preparation.md) |
| editions/index.md | Ancien registre remplacé par [registre actuel](../editions/README.md) et [candidate n°1](../editions/2026-10-28-projection-candidate-n1.md) |
| editorial-architecture.md | Principes repris dans [doctrine des Livres Vivants](../../../research/livre_vivant.md) et [candidate actuelle](../editions/2026-10-28-projection-candidate-n1.md) |
| living-book.yml | Ancien manifeste et ancien domaine, remplacés par [projection n°1](../projections/n1-working.yml) et [registre actuel](../editions/README.md) |
| magazine/2026-10-02-n1-lancement-campagne-presidentielle.md | Source conservée dans [magazine historique](../magazine/historique/2026-10-02-n1-lancement-campagne-presidentielle.md) |
| magazine/2026-10-05-jalon-p1-p18-matrice-eim.md | Source conservée dans [magazine historique](../magazine/historique/2026-10-05-jalon-p1-p18-matrice-eim.md) |
| magazine/2026-10-05-lancement-du-mouvement-capable.md | Source conservée dans [magazine historique](../magazine/historique/2026-10-05-lancement-du-mouvement-capable.md) |
| magazine/federated/privai-2026-10-04-illusion-electeur-synthetique.json | **Syndication Capable non démontrée.** [Source PrivAI](../../privai/magazine/2026-10-04-illusion-electeur-synthetique.md) conservée, [projection Commons](../../commons/magazine/federated/privai-2026-10-04-illusion-electeur-synthetique.json) présente ; ancienne qualification « established » non réaffirmée |
| magazine/federated/school-2026-10-04-ouverture-mariani-school-of-autonomy.json | **Syndication Capable non démontrée.** [Article source School](../../school/magazine/2026-10-04-ouverture-mariani-school-of-autonomy.md) conservé ; ancien titre « ouverture » non assimilable à un service vérifié |
| press/profile.yml | **Profil propre à Capable non réconcilié** : A5, lot de 100, zone QR ; ancienne cible QR vers un domaine abandonné, attribution institutionnelle à confirmer avant publication |
| projections/preview.epub | Ancien artefact binaire supplanté par les [formats en préparation](../editions/README.md) |
| projections/preview.pdf | Ancien artefact binaire supplanté par les [formats en préparation](../editions/README.md) |
| projections/preview.yml | Ancien manifeste remplacé par [preview.yml actuel](../projections/preview.yml) |
| site/book.epub | Ancien artefact binaire ; [édition vivante actuelle](../editions/README.md) |
| site/book.pdf | Ancien artefact binaire ; [édition vivante actuelle](../editions/README.md) |

## Travail restant

1. Décider si les deux événements originaux PrivAI et School doivent être syndiqués aujourd'hui dans le Magazine Capable, à date et qualification actualisées, sans masquer leur origine.
2. Reconstituer le profil d'impression Capable à partir de ses paramètres utiles en choisissant une destination QR actuelle et une attribution institutionnelle non équivoque.
3. Conserver la notice du manifeste historique comme provenance, sans recréer la configuration de déploiement abandonnée.

Ce rapprochement distingue les sources originales, les sorties générées et les relations de syndication. Aucune édition gelée n'est modifiée. Paquets propriétaires : [Capable #152](https://github.com/JeanHuguesRobert/barons-Mariani/issues/152) et [Cogentia #309](https://github.com/JeanHuguesRobert/cogentia/issues/309).
