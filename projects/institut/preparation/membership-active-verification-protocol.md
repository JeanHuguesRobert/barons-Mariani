---
title: "C.O.R.S.I.C.A. — protocole actif de qualification des membres"
subtitle: "Passer des archives incomplètes à une liste de convocation traçable"
description: "Protocole public et privacy-minimized pour qualifier en privé les personnes susceptibles d’appartenir à l’assemblée générale avant l’AGE 2026."
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-05"
last_modified_at: "2026-10-05"
version: "0.1"
status: "working-paper — preparatory"
license: "CC BY-SA 4.0"
language: "fr"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/institut/preparation/membership-active-verification-protocol.md"
document_role: "operational"
document_kind: "verification-protocol"
document_function: "private membership qualification method"
visibility: "public"
lifecycle_state: "working"
update_policy: "UP-DEFAULT-REVIEWED"
related_documents:
  - "projects/institut/preparation/membership-quorum-2026.md"
  - "projects/institut/preparation/governance-membership-baseline.md"
  - "projects/institut/preparation/ag-age-2026-readiness.md"
  - "projects/institut/sources/statuts-corsica-1995-transcription.md"
provenance:
  origin_type: "procedural-consolidation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "unknown"
  origin_date: "2026-10-05"
review:
  status: "unreviewed"
  reviewed_by: []
---

# C.O.R.S.I.C.A. — protocole actif de qualification des membres

## 1. Objet

Les recherches passives n’ont pas permis de reconstituer un registre statutaire complet des admissions.

La suite doit donc être active, contradictoire et minimale :

~~~text
archives disponibles
→ personne plausible
→ vérification privée
→ qualification
→ possibilité de contestation / correction
→ gel de la liste
→ calcul du quorum
→ convocation
~~~

Le but n’est pas de recréer artificiellement le passé, mais d’obtenir une base suffisamment robuste pour ne priver silencieusement personne d’un droit éventuel et ne pas admettre comme votant une personne dont la qualité n’est pas défendable.

## 2. Questions minimales par personne

La fiche privée doit contenir uniquement ce qui est nécessaire :

| Question | Valeurs de travail |
|---|---|
| Existe-t-il une trace de relation avec C.O.R.S.I.C.A. ? | oui / non |
| Une admission par le CA est-elle documentée ? | ESTABLISHED / RECONSTRUCTED / NOT FOUND |
| Une catégorie 1995 peut-elle être attribuée ? | fondateur / honneur / bienfaiteur / actif / adhérent / UNKNOWN |
| Une démission est-elle documentée ? | ESTABLISHED / NOT FOUND |
| Une radiation est-elle documentée ? | ESTABLISHED / NOT FOUND |
| La personne se considère-t-elle encore membre ? | oui / non / incertain / sans réponse |
| Dispose-t-elle d’une pièce ou d’un souvenir précis d’admission ? | oui / non |
| Qualité de membre en exercice | YES / PROBABLE / DISPUTED / NO / UNKNOWN |
| Droit de participer à l’AG | YES / PROBABLE / DISPUTED / NO / UNKNOWN |

Les coordonnées et réponses nominatives restent privées.

## 3. Message de vérification candidat

Le contact doit être neutre et ne pas suggérer la réponse :

> C.O.R.S.I.C.A. prépare une mise à jour de sa gouvernance et reconstitue son registre de membres à partir d’archives anciennes incomplètes. Vous apparaissez dans une ancienne trace liée à l’association ou à ses activités. Afin de ne ni vous exclure à tort ni vous attribuer une qualité que vous n’avez pas, pouvez-vous indiquer : si vous avez été membre de C.O.R.S.I.C.A. ; si vous vous souvenez de la forme de votre admission ou de votre catégorie ; si vous avez ensuite démissionné ou reçu notification d’une radiation ; et si vous disposez d’un document utile ? Cette demande ne préjuge pas de votre qualification finale au regard des statuts.

Toute réponse est une trace déclarative, pas une décision juridique automatique.

## 4. Règles de qualification

~~~text
souvenir seul
→ REPORTED

souvenir + trace contemporaine convergente
→ possible RECONSTRUCTED

PV / décision CA authentifiée
→ ESTABLISHED sous réserve du contenu

absence de réponse
→ UNKNOWN, jamais NO par défaut

absence de cotisation retrouvée
→ ne prouve pas la perte de qualité

activité bénévole / usage / fonction
→ ne prouve pas à elle seule l’admission
~~~

## 5. Contradiction avant gel

Avant calcul du quorum, toute personne classée DISPUTED ou dont l’exclusion pourrait modifier matériellement le dénominateur doit pouvoir faire valoir une correction.

Le gel doit produire :

~~~yaml
cutoff_date: ...
established_voting_members: N
probable_voting_members: M
disputed_cases: K
unknown_cases: U
quorum_method: ...
qualification_method_version: ...
~~~

La liste nominative reste privée ; le Corpus public reçoit la méthode et les agrégats.

## 6. Escalade

Si les cas incertains restent suffisamment nombreux pour rendre le quorum ou l’initiative de modification contestables :

~~~text
qualification interne
→ insuffisante
→ Guid’Asso / greffe / conseil juridique
→ question précise et documentée
~~~

La question externe doit porter sur le mécanisme de régularisation, pas demander à l’administration d’inventer l’histoire factuelle de l’association.

## 7. Reality Test

Le succès du protocole se mesure par la diminution des cas UNKNOWN, la traçabilité de chaque qualification, l’absence de données personnelles inutiles dans le Corpus, la capacité à calculer un quorum défendable et la capacité à expliquer après coup pourquoi une personne a été convoquée ou non.

La méthode reste révisable si le Réel révèle une meilleure source ou une erreur de classification.