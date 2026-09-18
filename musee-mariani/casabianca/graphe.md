# Graphe généalogique Casabianca

Ce dossier sépare les **personnes** des **relations** afin que l'arbre puisse être traité comme un graphe par des agents, scripts ou projections.

## Fichiers

- `personnes.tsv` : un nœud par personne ;
- `relations.tsv` : une arête par relation ;
- `sources.md` : registre critique des sources.

## Règles

1. Un identifiant est stable et ne dépend pas de l'affichage du nom.
2. Une relation `parent_de` est orientée parent → enfant.
3. `conjoint_de` est symétrique mais n'est enregistrée qu'une fois.
4. `statut=rapporte` signifie que l'information est donnée par la source secondaire familiale, sans prétendre qu'une source primaire a déjà été contrôlée.
5. `documente_dans_source` signifie que Moussia fournit elle-même une référence documentaire identifiable ; cela ne vaut pas encore vérification indépendante de cette pièce.
6. Les pages renvoient au PDF `CASABIANCA-2010-MOUSSIA`.
7. Les incertitudes ne sont jamais silencieusement résolues : elles vont dans `questions-ouvertes.md`.

## Portée initiale

La première tranche encode la ligne Rinuccio → Marguerite de Casabianca (1861) → Marie-Louise Mariani, ainsi que la bifurcation Pierre (1859) → François-Marie III → Rose-Marie « Moussia ».

Le graphe sera étendu incrémentalement aux collatéraux et aux générations contemporaines, avec priorité aux relations utiles à l'histoire familiale et aux projections du Corpus.
