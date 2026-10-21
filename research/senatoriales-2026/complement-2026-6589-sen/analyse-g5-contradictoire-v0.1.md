---
title: "2026-6589 SEN — Analyse contradictoire du grief G5"
author: "Jean Hugues Noël Robert"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-21"
version: "0.1"
status: "working-paper — contribution candidate"
license: "CC BY-SA 4.0"
language: "fr"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/senatoriales-2026/complement-2026-6589-sen/analyse-g5-contradictoire-v0.1.md"
document_role: "operational"
document_kind: "legal-analysis"
target_audience: ["grand public", "spécialistes du contentieux électoral"]
visibility: "public"
update_policy: "UP-DEFAULT-REVIEWED"
provenance:
  origin_type: "repository"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "https://github.com/JeanHuguesRobert/barons-Mariani/issues/130"
  origin_date: "2026-10-21"
  derived_from:
    - "research/senatoriales-2026/requete-conseil-constitutionnel.md"
    - "research/senatoriales-2026/complement-2026-6589-sen/texte-maitre-travail-v0.1.md"
review:
  status: "unreviewed"
  reviewed_by: []
---

# Grief G5 — La candidature exclue pouvait-elle changer le déroulement du scrutin ?

## La question, en termes simples

Une candidature supplémentaire ne garantit pas un second tour. Mais il ne suffit pas non plus de constater que le vainqueur a obtenu une large majorité au premier tour pour démontrer que l'exclusion de cette candidature était nécessairement sans conséquence. Ces deux affirmations doivent être distinguées.

Le requérant n'affirme pas connaître les choix que les grands électeurs auraient effectués si sa candidature avait été enregistrée. Il demande que la discussion sur l'incidence possible de l'exclusion ne soit pas remplacée par une certitude contrefactuelle non démontrée.

## Les données certaines du scrutin observé

Haute-Corse, 27 septembre 2026 : **616 inscrits**, **606 votants**, **530 exprimés**, **36 blancs**, **40 nuls**, **442 suffrages** pour le candidat proclamé élu et **88** pour son concurrent. Les 76 blancs et nuls ne sont pas des voix automatiquement disponibles pour une autre candidature.

Les dix inscrits qui n'ont pas voté ne doivent pas non plus être assimilés à des personnes disposées à voter pour un troisième candidat.

## Les conditions mathématiques, et uniquement elles

Dans un scénario contrefactuel borné, on note :

- `x` : voix précédemment attribuées au candidat élu qui ne le seraient plus ;
- `z` : suffrages jusque-là non exprimés devenant des suffrages valables.

Avec un nombre total de suffrages exprimés `530 + z`, le candidat initialement élu perdrait la majorité absolue des suffrages exprimés si :

```text
442 - x <= floor((530 + z) / 2)
```

Cette formulation ne suffit pas à tester toutes les conditions légales propres au scrutin sénatorial ; elle borne uniquement l'une d'elles. Dans le scrutin observé, la majorité relative aux inscrits est également une condition à considérer séparément.

| Hypothèse illustrative | z | x minimum pour perdre la majorité absolue des exprimés |
|---|---:|---:|
| Aucun suffrage nouveau | 0 | 177 |
| Les 36 blancs seulement deviennent valables | 36 | 159 |
| Les 40 nuls seulement deviennent valables | 40 | 157 |
| Les 76 blancs et nuls deviennent valables | 76 | 139 |
| Les 86 non-exprimés (dont les 10 non-votants) deviennent valables | 86 | 134 |

**Attention au sens des nombres** : ce sont des bornes minimales dans des hypothèses mathématiques, ni une estimation du soutien au requérant ni une probabilité qu'un second tour ait eu lieu.

## Le meilleur argument contraire

L'écart observé est considérable : **442 voix contre 88**. Une candidature exclue n'a pas été mesurée dans le scrutin réel ; aucune distribution des préférences des grands électeurs ne peut être déduite des blancs, des nuls, de leur présence ou de leur comportement antérieur. Les scénarios de report ne sont donc pas des éléments de preuve d'un basculement effectivement probable.

La comparaison avec la Corse-du-Sud ne transfère pas automatiquement les résultats d'un département à l'autre et ne peut servir à attribuer des votes secrets.

Ces objections sont substantielles et doivent être maintenues dans le mémoire.

## Portée recevable de la démonstration

La simulation ne démontre **ni** que le candidat proclamé élu aurait perdu, **ni** qu'un second tour aurait eu lieu, **ni** que l'élection devrait être annulée pour ce seul motif. Elle montre seulement que l'affirmation « l'exclusion n'aurait nécessairement rien changé » n'est pas une conséquence mécanique du résultat observé.

L'appréciation juridique appartient au Conseil constitutionnel : celui-ci devra, dans le cadre des griefs recevablement soulevés, déterminer si l'irrégularité alléguée d'exclusion et les circonstances de l'élection ont pu affecter la sincérité du scrutin. La simulation n'est qu'un élément de ce raisonnement, sans inversion de la charge de la preuve.

## Limites / contrôles avant intégration

1. Vérifier sur les textes applicables toutes les conditions exactes de majorité au premier tour, et ne pas confondre simple échec du seuil de majorité absolue des exprimés et preuve complète de la nécessité d'un second tour.
2. Vérifier le procès-verbal et les chiffres observés sur la source officielle ou la pièce communiquée.
3. Ne pas introduire de grief électoral supplémentaire : rattachement exclusif au grief G5 de la requête enregistrée.
4. Conserver la distinction **fait observé / hypothèse contrefactuelle / inférence / demande au juge**.
5. Laisser expressément la probabilité et la causalité électorales en statut **UNKNOWN** en l'absence de preuves spécifiques.

**Statut : contribution contradictoire candidate, non intégrée automatiquement au mémoire prêt à déposer.**
