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
| P0 | P-13 vidéo | G2/G3/G4, consentement et preuve contemporaine | **RÉSOLU le 13/11** : copie Drive ID `1P0AIJ-FzX69xkd4-kQyujbJg2nGqRbtC` récupérée en binaire, 79 663 474 octets, SHA-256 recalculé `aaac3d97801f57185e38cb3c26f9ec4597aee52188a494f63a81874e1fb1a7d8` (identique au repère historique) ; durée ffprobe 58,137778 s. Production au CC et validité du canal UNKNOWN. |
| P0 | P-12 et P-43.a | G2/G4, chronologie et demande d'assistance | Extraire les originaux privés, dater précisément émission/éventuelle réception ; minimiser les adresses et les liens secrets |
| P0 | P-17 et P-18 | G2/G3, acte manuscrit et handicap | Recontrôler originaux, sélectionner extraits utiles, expurger les données de santé non nécessaires ; AAH ≠ preuve automatique de l'empêchement précis |
| P1 | P-06/P-09/P-10/P-11 | G1/G4, formalisme et guichet | Identifier copies effectivement citées/reproduites dans la requête et doublons ; limiter la remise aux éléments indispensables |
| P1 | P-14/P-19/P-20/P-29 à P-33 | G3/G4, procédure TA | Inventorier copies TA et courriels, comparer les versions, éviter le renvoi intégral de dossiers privés redondants |
| P1 | P-44 à P-46 | G4, correspondances et demandes | Sélectionner épisodes probants, masquer identifiants d'accès, ne pas multiplier les mêmes messages |
| P2 | P-27/P-39 à P-41 | G5, incidence électorale | Garder comme pièces du grief initial, sans attribuer de vote individuel ni présumer un second tour probable |

Les références non énumérées ici restent dans la matrice initiale : **pas d'exclusion définitive sans confrontation des références P citées à la requête v0.34**. Pour chaque sélection, exiger une source localisée et un artefact final réellement présent, avec `reference_originale / page_requete / grief / source / date / taille / SHA / minimisation / canal / statut`. Tout manquant est UNKNOWN/BLOCKED, jamais READY.

## Constat matériel nouveau : accès à P-13 et permissions (13 novembre 2026)
- Accès ciblé par identifiant Drive historique, qui résout le faux négatif de la recherche par nom du 10 novembre. Fichier `VID_20260911_174455.mp4`, créé sur Drive le 11 septembre 2026 à 15:52:17Z, modifié à 15:53:33Z (horaires de stockage, **pas** métadonnées de prise de vue).
- Binaire complet téléchargé depuis Drive connecté dans l'environnement de traitement ; taille effectivement mesurée = **79 663 474 octets** ; SHA-256 effectivement recalculé = `aaac3d97801f57185e38cb3c26f9ec4597aee52188a494f63a81874e1fb1a7d8`. `ffprobe` identifie MP4, durée **58,137778 s**. Résultat **PASS pour identité de la copie Drive avec l'empreinte historique**, pas pour réception administrative ou conformité L.299.
- Visibilité retournée par Drive : `shared=true`, permission `anyone/commenter`, `allowFileDiscovery=false`. Ce **n'est pas un partage strictement privé** ; peut tenir au lien utilisé en septembre. Décider du maintien ou changement de permission selon conservation de la preuve, accès existant des destinataires et confidentialité : ne pas modifier automatiquement.
- Les dossiers TA 2601714 et 2601715 existent sur Drive, non partagés, tailles respectives **12 000 594** et **12 219 819** octets (métadonnées à date ; pas de rehash de ces deux PDF).
- Le fichier natif téléchargé reste hors du dépôt GitHub public ; ne pas y inscrire de lien d'accès temporaire ni d'informations sensibles supplémentaires.

## Distinctions juridiques à maintenir
1. L.299 (acceptation, mention, signature), L.301 (deux exemplaires), R.99 (« papier libre ») et R.149 ne se confondent pas. Ne pas prétendre que le droit électoral exclut toute référence au papier ; ne pas déduire automatiquement de « papier libre » l'obligation ou la dispense de présentation d'un original physique.
2. Séparer création de l'acceptation, consentement, original manuscrit, numérisation, impression, transport Ajaccio–Bastia, remise matérielle et preuve de réception. La vidéo peut corroborer un fait antérieur sans régulariser ipso facto une formalité antérieure.
3. Handicaps et aménagement raisonnable : documenter la difficulté fonctionnelle *concrète*, distinguer signature/mention et acheminement, minimiser les données privées.
4. Finalité probatoire et proportionnalité de l'exclusion : développement conditionnel à rattacher aux passages exacts de G1/G2 déposés ; ne pas créer tardivement un moyen distinct sans décision.
5. Pouvoir d'instruction du Conseil ≠ obligation automatique de réclamer P-13. La demande générale du greffe du 7 octobre pour « requête et pièces », l'accusé du 8 octobre et l'absence de demande spécifique ne démontrent ni examen ni refus d'examiner la vidéo.
6. Les contacts avec le Sénat autour de Beauvau et Capable relèvent du contexte institutionnel, pas du lot probatoire juridictionnel sans rattachement électoral démontré.

## Séquence exécutable et dépendances
1. **#131** : produire une sélection active **nouvelle**, séparée du CSV historique, à partir de toutes les citations de la requête initiale ; vérifier doublons et sources privées. Avant d'y inscrire READY, vérifier les artefacts finaux.
2. **#132** : localisation et SHA P-13 **PASS le 13/11** ; prochaine action : vérifier chronologie d'origine et conditions de dépôt applicables à date, sans présumer validité de l'ancien TransfertPro.
3. **#133** : produire un bref courrier de communication de pièces, bordereau exact des fichiers prêts et manifeste ; **pas** de QPC ni mémoire argumentatif ajoutés par le mode historique.
4. **#134** : contrôle adverse des fichiers, de leur confidentialité, des SHA finaux, de la correspondance avec le courrier et des canaux ; contrôle de l'existence éventuelle d'une décision déjà rendue.
5. **#127** : soumettre au Principal le lot vérifié et les seules décisions substantielles restantes, puis STOP avant toute communication externe.

## Vérification additionnelle Gmail et recherche de décision (13 novembre)
- Recherche Gmail `"2026-6589" after:2026/10/08` : seuls les deux brouillons du 8/21 octobre et la réponse du greffe du **8 octobre** ressortent dans les messages correspondants. Recherche `from:(conseil-constitutionnel.fr) after:2026/10/08` : même réponse du 8 octobre. **Aucune notification ultérieure retrouvée dans ces recherches**, ce qui ne démontre pas l'absence de décision ou de notification par une autre voie.
- Recherche publique du numéro de dossier le 13 novembre : **pas de décision directement identifiée** dans les résultats consultés ; contrôle exhaustif du registre des décisions toujours UNKNOWN. Ne jamais écrire « affaire pendante établie » sur cette seule base.

## Gates de reprise
| Gate | Statut au 13 novembre |
|---|---|
| Mandat actif identifié et séparé du plan historique | PASS |
| Inventaire GitHub historique identifié | PASS |
| Sélection actuelle exhaustive et sans doublons | UNKNOWN |
| P-13 actuel localisé et SHA recalculé | **PASS** (Drive ID historique ; binaire téléchargé le 13/11 ; 79 663 474 octets ; SHA-256 confirmé) |
| Autres copies privées finales produites et expurgées | UNKNOWN |
| Décision du Conseil et validité actuelle du canal vérifiées | UNKNOWN |
| Manifeste SHA des fichiers finaux | BLOCKED |
| Lettre et bordereau concordants prêts à lire | BLOCKED |
| Revue juridique du dépôt complémentaire | UNKNOWN |
| Envoi ou réception de ce nouveau lot | NON ATTESTÉ |

**Conclusion : `filing_ready=false`.** Ne pas convertir les inconnues en empêchements définitifs ; résoudre d'abord l'accès aux pièces natives et refaire le contrôle matériel.
