# Préparation automatique des Livres Vivants — 9 octobre 2026

## Dernière version consultable — 13 novembre 2026

La [candidate Capable n°1](2026-10-28-projection-candidate-n1.md) a été actualisée au 13 novembre. La Factory produit une [projection HTML consultable en ligne](https://jeanhuguesrobert.github.io/barons-Mariani/previews/en-preparation/capable.html), un [PDF](https://raw.githubusercontent.com/JeanHuguesRobert/barons-Mariani/main/previews/en-preparation/capable.pdf), un [EPUB](https://raw.githubusercontent.com/JeanHuguesRobert/barons-Mariani/main/previews/en-preparation/capable.epub) et leurs [empreintes vérifiables](../../../previews/en-preparation/capable-formats.json). Ils sont **en préparation — non gelés**, distincts du Livre durable hébergé sur le site.

Les formats dérivent du **même HTML**, lui-même assemblé depuis les 23 sources identifiées dans le [manifeste](../../../previews/en-preparation/manifest.json). La conversion est implémentée par [l'adaptateur de formats](../../../scripts/build-living-books-working-formats.py), sans second compositeur doctrinal. La publication directe sur GitHub ne vaut pas déploiement de l'URL `/candidate.html` sur Fracta2.

Le fichier [workflow GitHub Actions](../../../.github/workflows/living-books-news-previews.yml) déclenche sur les changements apportés à l'Observatoire de l'autonomie ou aux plans d'éditions de **Capable**, **Suicide Corse** et **1755**.

Il exécute [le générateur](../../../scripts/build-living-books-news-previews.py), qui vérifie l'existence des documents sources, calcule leurs SHA-256, puis produit quatre aperçus **en préparation**, accompagnés d'un `manifest.json` avec le commit source, l'horodatage UTC et les empreintes. Les résultats sont conservés comme artefacts Actions 30 jours ; ils ne sont ni une édition gelée ni une promotion sur le site public ; pour Capable, les formats PDF et EPUB sont également produits comme artefacts de travail.

**Limite volontaire** : l'outil compose des paquets documentaires traçables depuis les plans éditoriaux existants. Il ne réécrit pas automatiquement le corps du Livre, ne vérifie pas de nouvelles sources externes, ne transcrit pas l'audition ministérielle, et ne promet pas un déploiement site. Le « quasi temps réel » dépend des commits qui déclenchent le workflow.

**Promotion** : une personne autorisée vérifie les sources, la cohérence de chaque face (Livre, Magazine, Annexes, Site, Guide), les objections et les traces avant de demander la production d'une édition candidate complète puis son éventuel gel. Aucun workflow ici n'effectue cette promotion.

Voir :
- [Capable, état en préparation](2026-10-09-en-preparation.md)
- [Suicide Corse n°4](../../suicide-corse/editions/2026-10-09-n4-en-preparation.md)
- [1755 RC1](../../1755/editions/2026-10-09-rc1-en-preparation.md)
- [Observatoire](../../../research/autonomia/observatoire_processus_autonomie_corse.md)
