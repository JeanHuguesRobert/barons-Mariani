# Capable — architecture du Livre Vivant

## 1. Objet

Capable observe l'écart entre **droit formel**, **capacité annoncée**, **capacité effectivement accessible** et **effet réel**.

Le premier terrain suivi en continu est la **Campagne du Réel**, issue du contentieux électoral 2026, avec profondeur historique 2017–2026.

## 2. Couches

### Traces
Courriels, décisions, accusés de réception, journaux, bordereaux, procès-verbaux, pièces et chronologies.

### Matrice
Chaque question est indexée par acteur, demande, première date, dernière relance, déclencheur, ancienneté, détenteur probable, autorité de décision, routage, réponse observable, effet sur la capacité de recours et statut probatoire.

### Qualification
La qualification est séparée du fait :

`fait → trace → contradiction éventuelle → qualification → voie d'action`

et non :

`qualification présupposée → sélection des faits`.

## 3. Dimension acteur

La matrice peut représenter simultanément :

- Préfecture de Haute-Corse ;
- Bureau des élections ;
- Sous-préfecture de Corte ;
- Tribunal administratif de Bastia ;
- Défenseur des droits / délégation territoriale ;
- Conseil constitutionnel — contentieux électoral ;
- Conseil d'État — notamment filtre QPC dans l'ordre administratif ;
- Conseil constitutionnel — QPC ;
- CADA ;
- CNIL ;
- CEDH ;
- Comité des ministres du Conseil de l'Europe, au stade éventuel d'exécution.

Chaque acteur reçoit un état : `CURRENT`, `IMMINENT`, `CONDITIONAL`, `PROSPECTIVE`, `TERMINAL`.

## 4. Temps et déclencheurs

Une relance n'est pas comptée isolément lorsqu'un événement nouveau en modifie la nécessité.

Exemple canonique :

- 11 septembre 2026 : transmission de la déclaration vidéo ;
- 14 septembre : demande de versement si absente du dossier ;
- 15 septembre : demande explicite de traçabilité ;
- 1er octobre : invitation du TA à saisir le Conseil constitutionnel ;
- 2 octobre : relance et numérotation des demandes rendues immédiatement utiles par ce nouveau contexte procédural.

La matrice enregistre donc **le déclencheur**, et pas seulement la fréquence des messages.

## 5. Profondeur historique

Capable peut rapprocher des épisodes distincts sans les confondre.

Pour la branche électorale :

- 2017 : décision électorale définitive ; niveau d'examen à documenter ;
- 2024 : décision électorale définitive ; niveau d'examen à documenter ;
- 2026 : cycle en cours.

Une dimension `precedent_personnel` permet de tester la récurrence sans conclure prématurément à une pratique générale.

## 6. Publication ouverte

Le plan de campagne est public.

Toute personne ou institution peut proposer une correction, une contradiction, une source primaire, une meilleure formulation d'une demande, un acteur manquant, une voie procédurale oubliée ou une objection à la méthode.

Les objections sont des objets de premier rang.

## 7. Projection éditoriale

Le Livre Vivant pourra produire :

- **Livre** : récit intelligible au grand public ;
- **Journal** : campagne documentée en direct ;
- **Annexes** : pièces, matrices et détails techniques ;
- **Site** : navigation, recherche, chronologie, acteurs, demandes et réponses ;
- **Données** : exports YAML/JSON issus des registres publics.

## 8. Principe cardinal

> Le plan peut être public sans que le résultat soit connu d'avance.

Capable ne cherche pas à cacher la manœuvre. Il cherche à rendre ses hypothèses falsifiables et ses erreurs corrigeables.

## 9. Campagnes et grammaire réutilisable

La **Campagne du Réel** désigne historiquement la première grande campagne documentée, liée aux Sénatoriales 2026.

Elle fournit progressivement une grammaire réutilisable :

```text
trace
→ Révélateur
→ écart
→ exploration
→ Reality Test / Act
→ mesure
→ Stabilisateur
→ nouvelle confrontation au Réel
```

La présidentielle 2027 constitue une autre instance, à une autre échelle. Elle peut réemployer cette grammaire sans effacer la provenance de la première campagne.

Documents de travail :

- [Architecture des campagnes](campaign/architecture-des-campagnes.md)
- [Marche du Soleil](campaign/marche-du-soleil.md)
- [Observatoire des Présentations 2027](campaign/observatoire-presentations-2027.md)

La règle de symétrie s'applique : les Révélateurs construits par Capable doivent pouvoir révéler les propres écarts de Capable.

---

## Registre de préparation éditoriale — 9 octobre 2026

La [préparation courante](editions/2026-10-09-en-preparation.md) distingue trace parlementaire, interprétation et projection éditoriale. Une entrée actualisée ne crée aucun nouvel acte institutionnel ; elle appelle la validation des sources primaires et la correction de la chronologie lorsque des comptes rendus paraissent.
