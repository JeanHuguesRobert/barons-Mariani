# Préparation automatique des Livres Vivants — 9 octobre 2026

Le fichier [workflow GitHub Actions](../../../.github/workflows/living-books-news-previews.yml) déclenche sur les changements apportés à l'Observatoire de l'autonomie ou aux plans d'éditions de **Capable**, **Suicide Corse** et **1755**.

Il exécute [le générateur](../../../scripts/build-living-books-news-previews.py), qui vérifie l'existence des documents sources, calcule leurs SHA-256, puis produit trois aperçus **en préparation**, accompagnés d'un `manifest.json` avec le commit source, l'horodatage UTC et les empreintes. Les résultats sont conservés comme artefacts Actions 30 jours ; ils ne sont pas une édition, ni une publication durable, ni un gel, ni un PDF/EPUB.

**Limite volontaire** : l'outil compose des paquets documentaires traçables depuis les plans éditoriaux existants. Il ne réécrit pas automatiquement le corps du Livre, ne vérifie pas de nouvelles sources externes, ne transcrit pas l'audition ministérielle, et ne promet pas un déploiement site. Le « quasi temps réel » dépend des commits qui déclenchent le workflow.

**Promotion** : une personne autorisée vérifie les sources, la cohérence de chaque face (Livre, Magazine, Annexes, Site, Guide), les objections et les traces avant de demander la production d'une édition candidate complète puis son éventuel gel. Aucun workflow ici n'effectue cette promotion.

Voir :
- [Capable, état en préparation](2026-10-09-en-preparation.md)
- [Suicide Corse n°4](../../suicide-corse/editions/2026-10-09-n4-en-preparation.md)
- [1755 RC1](../../1755/editions/2026-10-09-rc1-en-preparation.md)
- [Observatoire](../../../research/autonomia/observatoire_processus_autonomie_corse.md)
