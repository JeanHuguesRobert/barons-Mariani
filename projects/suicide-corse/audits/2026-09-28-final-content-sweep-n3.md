---
title: "Suicide Corse n°3 — audit exhaustif final de contenu avant freeze"
author: "Jean Hugues Noël Robert"
date: "2026-09-28"
status: "completed"
language: fr
license: "CC BY-SA 4.0"
document_role: "editorial-audit"
document_kind: "final-content-sweep"
visibility: public
lifecycle_state: active
update_policy: UP-DERIVED-SOURCE-LOCKED
provenance:
  origin_type: corpus-delta-review
  origin_repository: JeanHuguesRobert/barons-Mariani
  origin_ref: main
  baseline_commit: f061abb2484dc5ee973d81865db5c9d3b5854d58
  derived_from:
    - projects/suicide-corse/projections/book-n3-working.yml
    - projects/suicide-corse/audits/2026-09-27-pre-freeze-n3.md
    - projects/suicide-corse/audits/2026-09-28-reader-audit-n3.md
    - projects/suicide-corse/journals/2026-09-23-n3-construction.md
    - GitHub issue #84
    - GitHub issue #89
review:
  status: assistant-reviewed
  reviewed_by:
    - GPT-5.6 Sol
---

# Suicide Corse n°3 — audit exhaustif final de contenu avant freeze

## Méthode

Baseline : gel du n°2, commit `f061abb2484dc5ee973d81865db5c9d3b5854d58`.

Le delta jusqu'au 28 septembre représente plus de 300 commits. L'audit ne sélectionne donc pas tout ce qui a changé dans le dépôt : il teste chaque famille de changements contre trois critères cumulatifs :

1. postérieure au n°2 ;
2. matériellement nouvelle pour l'enquête ou sa méthode ;
3. utile au lecteur du n°3 sans transformer ce numéro en agrégat de tout le Corpus.

## A — À intégrer avant freeze

### A1 — Capable : naissance publique et baseline contradictoire

Le pré-freeze audit avait explicitement admis une projection courte :

- annonce publique le 27 septembre ;
- lien déclaré avec le Principe d'effectivité, Liberté–Égalité–Fraternité effectives, Autonomie de Capacité et #Suvranu ;
- baseline contradictoire fixé immédiatement ;
- Capable traité comme objet de Reality Test, non comme validation du Corpus.

Constat : cette matière était présente dans le chapitre monolithique `18-le-reel-repond`, mais a disparu lors du passage au Magazine modulaire.

Décision : **réintroduire brièvement dans le Magazine**, sans programme, score, classement ni rétro-étiquetage de Marie-Louise ou des candidatures antérieures.

### A2 — Capacité électorale de Marie-Louise 2017–2024

Le Corpus a consolidé après le n°2 une matrice longitudinale et des traces nouvelles sur 2022 :

- rôle titulaire ;
- participation administrative directe ;
- transmission de deux états successifs du collector depuis ses comptes ;
- distinction entre participation matérielle établie et auteur physique de Photoshop / autoportrait encore inconnu ;
- VOICE directe retrouvée en 2024.

Constat : le Livre mentionne déjà la séquence, mais le delta documentaire 2022 est sous-représenté dans le Magazine.

Décision : **ajouter une synthèse courte dans Nouvelles traces / Point de l'enquête**, pas un nouveau long chapitre.

### A3 — Acts institutionnels exécutés en fin de fenêtre

Le Corpus documente désormais :

- saisine initiale du Défenseur des droits le 26 septembre, sous angle d'effectivité / continuité administrative ;
- demande de consultation du procès-verbal et des bulletins nuls envoyée le 28 septembre ;
- demande à la Sous-Préfecture de Corte envoyée le 28 septembre pour vérifier un canal de remise d'une éventuelle requête au Conseil constitutionnel ;
- projet de requête `v0.2` existant mais encore `working-draft — for human review`.

Décision : **mettre à jour le Reality Case et les Continuations avec leurs statuts exacts** :
`SENT / WAITING` pour les demandes effectivement parties ;
`WORKING-DRAFT` pour la requête non déposée.

### A4 — Annexes rendues mais temporellement en retard

Quatre annexes importantes ne reflètent pas encore complètement l'état au bouclage :

- `chronologie.md` : s'arrête essentiellement au 23 septembre ;
- `annuaire.md` : état campagne au 24 septembre ;
- `questions-ouvertes.md` : état au 23 septembre ;
- `08-hypotheses-non-resolues.md` : intitulé et contenu encore datés du 21 septembre, avec plusieurs références d'ancien sommaire et un état sénatorial dépassé.

Décision : **mettre à niveau au 28 septembre**, sans réécrire les parties historiques.

### A5 — Registre exhaustif des Continuations

`16-continuations.md` contient déjà Grasse et les témoins tardifs, mais pas encore :

- Défenseur des droits ;
- consultation PV / bulletins ;
- vérification du canal Sous-Préfecture ;
- requête constitutionnelle comme draft à finaliser / déposer ou abandonner ;
- Capable comme Reality Test de ses propres critères.

Décision : **ajouter ces continuations**, en conservant une condition de clôture explicite.

### A6 — Manifeste de Corpus

`corpus.yml` est encore daté du 27 septembre et ne référence pas nominativement certains produits désormais décisifs pour le n°3 :

- matrice de capacité électorale 2017–2024 ;
- supplément d'œuvres post-n°2 ;
- Reality Case Capable Test / Marie-Louise 2024 ;
- demande PV du 28 septembre ;
- demande Sous-Préfecture du 28 septembre ;
- projet de requête v0.2 ;
- audit lecteur du n°3.

Décision : **actualiser le manifeste** pour la provenance, sans rendre ces sources toutes obligatoires.

## B — Déjà suffisamment représenté

### B1 — Réponses témoins post-n°2

Déjà projetées de manière adaptée :
- Maëva Guillery ;
- Maéva Lecoq ;
- Jean-Joseph Albertini ;
- Camille Gérard ;
- Damien Ruvet ;
- Valérie Roy / Thierry Parmentelat ;
- Louis-Marie Charreteur ;
- refus explicite de contact ;
- témoignage adverse privé.

Règle inchangée : existence / provenance / effet documentaire publics, contenu privé non reproduit sans décision séparée.

### B2 — Grasse

Référence parquet 25252000129 et Bureau d'ordre déjà présents dans le Magazine et les Continuations.

### B3 — DPO ministère de l'Intérieur

Déjà projeté comme différence entre retrait de la surface visible et rectification / traçabilité.

### B4 — DRAC / Minesteggio

La confirmation de signature de l'arrêté est déjà projetée. La copie, date exacte et publication restent des continuations.

### B5 — Résultats sénatoriaux

Les résultats observés sont déjà présents avec le garde-fou correct :
36 blancs + 40 nuls = fait ; motivations / allocation contrefactuelle = inconnues.

## C — À ne pas ajouter au n°3 avant freeze

### C1 — Enquête hydro-toponymique Minesteghju / Panate

Travail public nouveau et substantiel, mais son objet principal est patrimoine / hydrologie / toponymie / domaine de Minesteggio. Il ne constitue pas un delta nécessaire à l'enquête Marie-Louise ni à la logique centrale du n°3.

Décision : **hors n°3** ; peut nourrir Musée Mariani / futur numéro si un lien éditorial clair apparaît.

### C2 — Développement complet de Capable

Doctrines `principe_effectivite`, `egalite_effective`, `fraternite_effective`, tensions LEF, programme et études de cas : matériau important, mais le n°3 ne doit pas devenir le manifeste de Capable.

Décision : **mention du fait public + baseline seulement** ; renvoi au Corpus pour le reste.

### C3 — Programme constitutionnel / autonomie détaillé

Amendement 72-5, statut de résident, #1755, analyses institutionnelles et autres documents d'autonomie restent des sources / Reality Cases du Corpus.

Décision : **ne pas ajouter de développement doctrinal supplémentaire au Livre**. Le chapitre Corse est déjà suffisamment dense.

### C4 — Détail de la requête constitutionnelle

Le projet v0.2 est un document juridique spécialisé et encore non déposé.

Décision : **ne pas reproduire ses moyens dans le n°3** ; dire seulement qu'un projet existe et reste à l'état de travail.

### C5 — Reality Case Capable Test / Marie-Louise 2024

Le document est utile comme analyse dérivée et contrôle méthodologique, mais il reprend en profondeur la matière du Livre et introduirait une nouvelle couche conceptuelle tardive.

Décision : **référencer dans le Corpus, pas ajouter comme chapitre au n°3**.

### C6 — Généalogie : nouvelles structures de dossiers

Les README Casabianca / Mariani / d'Angelis consolident surtout l'architecture documentaire. Ils ne produisent pas, dans l'état observé, un fait généalogique nouveau qui exige une modification urgente du chapitre `17-genealogie.md`.

Décision : **pas de nouvelle matière avant freeze**.

## D — Risques de dernière minute

1. Une source produite le 28 septembre après le dernier rendu doit être explicitement soit absorbée, soit laissée comme continuation.
2. Toute nouvelle réponse privée reçue avant freeze ne doit pas déclencher automatiquement une réécriture du livre.
3. Les documents juridiques en travail ne doivent pas être décrits comme déposés.
4. Les doctrines politiques ne doivent pas absorber l'enquête ni attribuer une continuité politique posthume à Marie-Louise.
5. Toute correction de rendu doit être rerendue et relue avant freeze.

## Conclusion

Le n°3 ne souffre plus d'un manque de matière. Les derniers besoins sont des **mises à niveau de delta et de provenance**, pas un nouvel élargissement doctrinal.

Après application des items A1–A6 et un dernier rendu propre, le Corpus ne montre pas d'autre famille de contenu qui doive raisonnablement bloquer le freeze.
