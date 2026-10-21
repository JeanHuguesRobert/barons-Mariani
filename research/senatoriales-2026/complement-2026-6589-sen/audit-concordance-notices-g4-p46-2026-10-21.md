# Audit de concordance préalable à l'assemblage — notices G4 et P-46

**21 octobre 2026 — contrôle parallèle à l'issue #131.** Document de revue destiné aux handlers #131, #133 et #134. Aucun dépôt auprès du Conseil n'a eu lieu ; `filing_ready=false`.

## 1. Ancrages documentaires confirmés

La requête historique désigne **P-12, P-13, P-14, P-22, P-29 à P-33, P-45 et P-46**. La notice [G4, à double fonction](notice-g4-provenance-pertinence-p12-p46.md) et la [notice de série P-46](notice-provenance-p46-courriels-verification-p12-p13-2026-10-21.md) utilisent ces références, sans les renuméroter.

**Point de concordance à surveiller :** la requête initiale **annonce** que la « chaîne complète » des courriels est reproduite dans P-46. L'[audit structurel du PDF initial](audit-pdf-initial.json), rappelé au [checkpoint](checkpoint-provenance-2026-10-21.md), n'a pas retrouvé les 46 identifiants détaillés dans le PDF effectivement analysé. Il est incorrect d'écrire qu'une production intégrale de P-46 au greffe est matériellement établie au dépôt initial. La nouvelle notice et le volume constituent des **productions documentaires complémentaires**, et non une régularisation rétroactive silencieuse.

## 2. Matrice des quatre prétentions distinctes

| Prétention contrôlée | Support pertinent | État documentaire actuellement soutenable | Interdit logique |
|---|---|---|---|
| P-12 expédié à 17:57:55 | Message envoyé, EML et ses en-têtes | Émission documentée | En déduire réception par l'infrastructure de la préfecture avant 18h |
| P-12 ou lien inclus au dépôt initial TA | Inventaire Télérecours 2601715, 18:16, 16 entrées | Pas explicitement nommé dans cet inventaire | En déduire absence de toute pièce ou communication ultérieure |
| P-13 matériellement existant et stable | Vidéo source, empreinte, métadonnées | Copie MP4 contrôlée dans le corpus | En déduire visionnage par le TA ou conformité formelle de candidature |
| Diligences de vérification A/B/C | Courriels P-22/P-29/P-45/P-46 et réponses | Demandes répétées et réponses à apprécier message par message | En déduire intention de dissimulation ou admission du contenu par silence |

## 3. Contrôles FBF lors de l'intégration

1. **Authenticité ≠ thèse.** Chaque notice comporte le support exact, l'identifiant stable, le rôle probatoire et la meilleure objection. Un hachage n'atteste que l'intégrité des octets comparés.
2. **Exhaustivité de la production.** Rapprocher les 18 courriels candidats de l'index historique de 46 messages et des fils entrants, en documentant les critères d'inclusion, les exclusions motivées et l'éventuelle nouvelle sélection. Ne jamais qualifier d'« exhaustif » un volume non réconcilié.
3. **Version/source.** Conserver les EML natifs en espace privé avec tailles et SHA réelles ; établir un PDF lisible et fidèle, en distinguant transcription, reformatage et source brute.
4. **Non-duplication.** Un courriel déjà identifié dans une P historique reçoit un renvoi croisé ; ne pas le présenter deux fois comme deux faits distincts. Les réponses institutionnelles sont produites même lorsqu'elles contredisent ou relativisent la thèse.
5. **Chronologie.** Normaliser les heures en Europe/Paris depuis les en-têtes et conserver heure source, timezone et fuseau converti ; distinguer heure d'envoi et de réception.
6. **Destinations probatoires.** Vérifier que chaque sous-annexe du volume a une entrée au bordereau, une mention dans la notice concernée et une justification limitée à G3/G4 ou à d'autres griefs historiques effectivement cités.
7. **Règle de procédure.** Le rattachement aux P historiques ne garantit pas la recevabilité automatique des sous-annexes. Ne pas présenter un complément postérieur comme déjà déposé ; réserver l'appréciation au Conseil.
8. **Identité multi-canal.** Respecter le contrat : même Markdown souverain, courriel en texte intégral et 3 PDF joints ; TransfertPro avec les mêmes 3 PDF, plus la vidéo P-13. Hash de chaque PDF identique sur les deux canaux ; preuves d'expédition, acceptation, réception et examen séparées.
9. **Version figée.** La section IV/G4 du maître doit renvoyer aux notices **sans les contredire** ; vérifier l'actualisation après chaque nouveau commit de #131. Ne pas intégrer des marqueurs techniques, TODO ou données privées dans le rendu destiné au greffe.

## 4. Revue critique à demander à Codex

- La pièce P-46 historique annonçait-elle uniquement un index, ou prétendait-elle reproduire tous les messages ? Répondre en séparant **formulation de la requête** et **présence dans le PDF binaire**.
- Les 16 pièces de l'inventaire 2601715 comprennent-elles le message de 17:57 sous une désignation non explicite ? Vérifier le contenu des annexes, pas uniquement les intitulés.
- Les 18 messages candidats relèvent-ils tous effectivement de la question A/B/C ? Réserver les messages purement contextuels dans une catégorie distincte, mais ne pas les faire disparaître sans critère annoncé.
- Les réponses institutionnelles ne répondent-elles jamais à A/B/C ? Vérifier l'affirmation par une matrice binaire et un extrait exact, avec un statut `PARTIAL` lorsque nécessaire.
- Les notices emploient-elles `original`, `copie`, `reconstitution`, `inventaire` et `transcription` de manière stable et vérifiable ?

**Sortie attendue :** commentaires de revue et correction des écarts établis sur #131 ; consolidation par #133 ; examen du résultat binaire par #134. Aucune transmission non autorisée au greffe.
