---
title: "2026-6589 SEN — checkpoint de reprise et sélection probatoire"
date: "2026-11-13"
status: "working — no filing authorized"
document_role: operational
document_kind: evidence-delivery-checkpoint
visibility: public
lifecycle_state: working
filing_ready: false
language: fr
---
# Reprise opérationnelle du paquet #127 — 13 novembre 2026

## Autorité et limites
Le checkpoint du 1er novembre de [#127](https://github.com/JeanHuguesRobert/barons-Mariani/issues/127) gouverne **la prochaine émission éventuelle** : communication des seules pièces déjà citées dans la requête du 7 octobre 2026, accompagnées de notices bornées à provenance, intégrité et rattachement aux griefs G1–G5. Les commentaires du 13 novembre enrichissent la **revue contradictoire** de la thèse handicap / original matériel / finalité probatoire, mais ne constituent pas à eux seuls une autorisation de substituer au lot de pièces un mémoire argumentatif et deux QPC. Toute modification de la portée de la prochaine communication est un arbitrage humain explicite.

**Aucun courriel ni dépôt TransfertPro n'est autorisé par ce document.** Les états PREPARED, STAGED, SENT, RECEIVED, EXAMINED doivent être indépendants.

## État confirmé par lecture de GitHub
- [Audit du 10 novembre](audit-reprise-lot-pieces-2026-11-10.md) : CSV historique de 54 lignes (43 JOIN / 6 RESERVE / 5 CITE), 53 artefacts marqués non prêts, 54 NOT_SENT ; ces statuts reflètent un inventaire historique, **non une sélection active**.
- [CSV historique](bordereau-production-propose.csv) : P-13 porte `ready=true` et un SHA natif ancien, mais la copie actuelle **n'a pas été relocalisée et re-hachée dans cette reprise**. Ne pas réutiliser le drapeau historique comme preuve de préparation.
- [Notes de provenance](notes-provenance-v0.1.md) : P-17 et les copies TA 2601714/2601715 sont historiquement acquises ; les versions finales expurgées, les doublons et les statuts de remise restent à établir.
- [#115](https://github.com/JeanHuguesRobert/barons-Mariani/issues/115) : conserver le PDF exact de la note déjà transmise, sans le régénérer sous une fausse identité binaire.

## Sélection de travail priorisée (PAS un bordereau d'envoi)
| Priorité | Référence | Rôle déjà invoqué | Action / obstacle |
|---|---|---|---|
| P0 | P-13 vidéo | G2/G3/G4, consentement et preuve contemporaine | Retrouver en privé `VID_20260911_174455.mp4` ; vérifier taille et SHA natifs, sans recompression ; ancien repère : 79 663 474 octets / `aaac3d97801f57185e38cb3c26f9ec4597aee52188a494f63a81874e1fb1a7d8` ; chaîne de détention et canal actuel UNKNOWN |
| P0 | P-12 et P-43.a | G2/G4, chronologie et demande d'assistance | Extraire les originaux privés, dater précisément émission/éventuelle réception ; minimiser les adresses et les liens secrets |
| P0 | P-17 et P-18 | G2/G3, acte manuscrit et handicap | Recontrôler originaux, sélectionner extraits utiles, expurger les données de santé non nécessaires ; AAH ≠ preuve automatique de l'empêchement précis |
| P1 | P-06/P-09/P-10/P-11 | G1/G4, formalisme et guichet | Identifier copies effectivement citées/reproduites dans la requête et doublons ; limiter la remise aux éléments indispensables |
| P1 | P-14/P-19/P-20/P-29 à P-33 | G3/G4, procédure TA | Inventorier copies TA et courriels, comparer les versions, éviter le renvoi intégral de dossiers privés redondants |
| P1 | P-44 à P-46 | G4, correspondances et demandes | Sélectionner épisodes probants, masquer identifiants d'accès, ne pas multiplier les mêmes messages |
| P2 | P-27/P-39 à P-41 | G5, incidence électorale | Garder comme pièces du grief initial, sans attribuer de vote individuel ni présumer un second tour probable |

Les références non énumérées ici restent dans la matrice initiale : **pas d'exclusion définitive sans confrontation des références P citées à la requête v0.34**. Pour chaque sélection, exiger une source localisée et un artefact final réellement présent, avec `reference_originale / page_requete / grief / source / date / taille / SHA / minimisation / canal / statut`. Tout manquant est UNKNOWN/BLOCKED, jamais READY.

## Distinctions juridiques à maintenir
1. L.299 (acceptation, mention, signature), L.301 (deux exemplaires), R.99 (« papier libre ») et R.149 ne se confondent pas. Ne pas prétendre que le droit électoral exclut toute référence au papier ; ne pas déduire automatiquement de « papier libre » l'obligation ou la dispense de présentation d'un original physique.
2. Séparer création de l'acceptation, consentement, original manuscrit, numérisation, impression, transport Ajaccio–Bastia, remise matérielle et preuve de réception. La vidéo peut corroborer un fait antérieur sans régulariser ipso facto une formalité antérieure.
3. Handicaps et aménagement raisonnable : documenter la difficulté fonctionnelle *concrète*, distinguer signature/mention et acheminement, minimiser les données privées.
4. Finalité probatoire et proportionnalité de l'exclusion : développement conditionnel à rattacher aux passages exacts de G1/G2 déposés ; ne pas créer tardivement un moyen distinct sans décision.
5. Pouvoir d'instruction du Conseil ≠ obligation automatique de réclamer P-13. La demande générale du greffe du 7 octobre pour « requête et pièces », l'accusé du 8 octobre et l'absence de demande spécifique ne démontrent ni examen ni refus d'examiner la vidéo.
6. Les contacts avec le Sénat autour de Beauvau et Capable relèvent du contexte institutionnel, pas du lot probatoire juridictionnel sans rattachement électoral démontré.

## Séquence exécutable et dépendances
1. **#131** : produire une sélection active **nouvelle**, séparée du CSV historique, à partir de toutes les citations de la requête initiale ; vérifier doublons et sources privées. Avant d'y inscrire READY, vérifier les artefacts finaux.
2. **#132** : retrouver les octets actuels P-13, vérifier SHA et description non sensible ; obtenir les conditions de dépôt applicables à date, sans présumer validité de l'ancien TransfertPro.
3. **#133** : produire un bref courrier de communication de pièces, bordereau exact des fichiers prêts et manifeste ; **pas** de QPC ni mémoire argumentatif ajoutés par le mode historique.
4. **#134** : contrôle adverse des fichiers, de leur confidentialité, des SHA finaux, de la correspondance avec le courrier et des canaux ; contrôle de l'existence éventuelle d'une décision déjà rendue.
5. **#127** : soumettre au Principal le lot vérifié et les seules décisions substantielles restantes, puis STOP avant toute communication externe.

## Gates de reprise
| Gate | Statut au 13 novembre |
|---|---|
| Mandat actif identifié et séparé du plan historique | PASS |
| Inventaire GitHub historique identifié | PASS |
| Sélection actuelle exhaustive et sans doublons | UNKNOWN |
| P-13 actuel localisé et SHA recalculé | UNKNOWN |
| Autres copies privées finales produites et expurgées | UNKNOWN |
| Décision du Conseil et validité actuelle du canal vérifiées | UNKNOWN |
| Manifeste SHA des fichiers finaux | BLOCKED |
| Lettre et bordereau concordants prêts à lire | BLOCKED |
| Revue juridique du dépôt complémentaire | UNKNOWN |
| Envoi ou réception de ce nouveau lot | NON ATTESTÉ |

**Conclusion : `filing_ready=false`.** Ne pas convertir les inconnues en empêchements définitifs ; résoudre d'abord l'accès aux pièces natives et refaire le contrôle matériel.
