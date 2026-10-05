---
title: "C.O.R.S.I.C.A. — quorum préparatoire 2026"
subtitle: "Établir le corps votant avant toute assemblée modificative"
description: "Registre public minimal des conditions de calcul du quorum, sans publication des coordonnées ni de la liste nominative privée des membres."
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-04"
last_modified_at: "2026-10-05"
version: "1.2"
status: "working-paper — preparatory"
license: "CC BY-SA 4.0"
language: "fr"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/institut/preparation/membership-quorum-2026.md"
document_role: "operational"
document_kind: "governance-register"
document_function: "quorum reconstruction"
visibility: "public"
lifecycle_state: "working"
update_policy: "UP-DEFAULT-REVIEWED"
related_documents:
  - "projects/institut/sources/statuts-corsica-1995-transcription.md"
  - "projects/institut/preparation/statutes-lineage.md"
  - "projects/institut/preparation/ag-age-2025-2026.md"
provenance:
  origin_type: "privacy-minimized-reconstruction"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "unknown"
  origin_date: "2026-10-04"
  derived_from:
    - "private membership register — aggregate only"
    - "governance records 2020 and 2025"
review:
  status: "unreviewed"
  reviewed_by: []
---

# C.O.R.S.I.C.A. — quorum préparatoire 2026

## 1. Règle

Si les statuts 1995 restent applicables, l’article 17 exige pour la première assemblée modificative la présence ou représentation d’au moins **un quart des membres en exercice**.

L’article 8 inclut dans l’assemblée générale les membres fondateurs, d’honneur, bienfaiteurs et actifs ; les membres adhérents n’en font pas partie.

## 2. Ancien registre retrouvé

Un registre privé d’adhérents créé en 2018 et modifié pour la dernière fois en 2019 contient **33 entrées**.

Ses catégories opérationnelles — par exemple usager, bénévole ou fonctions de projet — ne correspondent pas directement aux catégories juridiques des statuts 1995.

~~~text
présence dans le registre 2018–2019
≠
qualité de membre votant en 2026
~~~

Les coordonnées et la liste nominative ne sont pas publiées dans le Corpus.

## 3. État du calcul

~~~yaml
voting_members_2026:
  count: UNKNOWN
  quorum_25_percent: NOT_COMPUTABLE_YET
  reason: "absence de registre 2026 qualifié selon les catégories statutaires applicables"
~~~

Le nombre historique de 33 entrées ne doit pas être utilisé automatiquement comme dénominateur. Le nombre de personnes présentes dans un PV récent ne doit pas davantage être assimilé à l’effectif total.

## 3 bis. Traces postérieures retrouvées

### Adhésion 2020

Un email intitulé `Adhésion 2020` a été retrouvé. Il ne s'agit **pas** de l'adhésion d'une personne à C.O.R.S.I.C.A. : il s'agit de **C.O.R.S.I.C.A. adhérant elle-même à Énergie Partagée Association**.

Cette trace confirme une activité institutionnelle en 2020 mais n'ajoute aucun membre au corps votant interne.

### Usage d'AssoConnect

Des traces 2021–2022 montrent que C.O.R.S.I.C.A. disposait d'un compte AssoConnect. Le présent passage n'a cependant retrouvé ni export d'adhérents ni liste de membres issue de cet outil.

~~~text
outil de gestion utilisé
≠
registre de membres retrouvé
~~~

### Déclaration de mars 2026 : « 40 membres actifs »

Le 12 mars 2026, dans le cadre d'une demande extérieure relative à des vélos cargos, le Président écrit qu'« une population de 40 membres actifs de l'association C.O.R.S.I.C.A. va raisonnablement participer » à l'initiative.

Cette phrase constitue une **déclaration contemporaine d'ordre de grandeur**, mais elle ne suffit pas à établir que 40 personnes possèdent juridiquement la qualité de `membre actif` au sens précis de l'article 8 des statuts 1995.

Qualification :

~~~yaml
declared_active_population_2026:
  value: 40
  epistemic_status: REPORTED_BY_ASSOCIATION_PRESIDENT
  context: external_project_participation_estimate
  statutory_membership_equivalence: NOT_ESTABLISHED
  use_as_quorum_denominator: PROHIBITED_WITHOUT_RECONCILIATION
~~~

Elle devient néanmoins une piste importante : un écart éventuel entre un registre statutaire reconstitué et cet ordre de grandeur devra être expliqué.

## 3 ter. Structure agrégée du registre privé 2018–2019

Le tableur privé contient 33 entrées. Sans publier aucune identité ni coordonnée, les libellés opérationnels observés se répartissent ainsi :

| Libellé opérationnel dominant | Nombre |
|---|---:|
| « usager » | 10 |
| « bénévole » (avec ou sans spécialité) | 16 |
| fonction / responsabilité opérationnelle | 6 |
| statut vide | 1 |

Seules 9 entrées comportent une date d’entrée renseignée dans la colonne correspondante.

Ces libellés ne sont **pas** les catégories juridiques de l’article 3 des statuts 1995. En particulier :

~~~text
bénévole
≠ automatiquement membre actif statutaire

usager
≠ automatiquement membre adhérent statutaire

fonction de projet
≠ admission par le conseil d’administration
~~~

L’article 3 exige en effet, pour devenir membre, un agrément du conseil d’administration après présentation par plusieurs membres. Le présent passage n’a pas retrouvé de registre d’agréments correspondant aux 33 lignes.

## 3 quater. Pratique 2019–2020 : indice de divergence entre texte et usage

Un courrier d’octobre 2019 décrit C.O.R.S.I.C.A. comme ayant des « membres actifs qui votent » et des « membres inactifs qui ne votent pas ». Cette grammaire correspond davantage au projet de refonte 2018–2019 qu’au vocabulaire exact des statuts 1995.

Un PV du 15 octobre 2020 retrouvé dans un dossier bancaire décrit ensuite un bureau composé de trois fonctions : président, trésorier, secrétaire. La copie retrouvée est non signée et Société Générale en demandera une version signée en 2023.

Or l’article 5 des statuts 1995 prévoit un bureau comprenant aussi un ou deux vice-présidents.

La meilleure lecture provisoire est donc :

~~~text
pratique associative ayant évolué
→ ESTABLISHED / RECONSTRUCTED

adoption formelle du modèle 2018
→ NOT FOUND

correspondance parfaite entre pratique et statuts 1995
→ FALSE / NON OBSERVED
~~~

Cette divergence interdit d’utiliser sans contrôle les catégories historiques du tableur pour calculer le corps électoral 2026.

## 3 quinquies. Conséquence opérationnelle pour la convocation

Avant d’envoyer une convocation modificative, il faut produire en privé une matrice minimale :

~~~text
personne
→ preuve d’admission
→ catégorie statutaire 1995
→ preuve éventuelle de démission / radiation
→ membre en exercice ?
→ droit de participer à l’AG ?
→ droit de vote ?
~~~

Le Corpus public ne conservera ensuite que les agrégats et la méthode.


## 3 sexies. Audit quantitatif du registre privé

Un nouveau passage direct sur le tableur privé confirme, sans publier aucune identité ni coordonnée :

~~~yaml
historical_register_2018_2019:
  person_rows: 33
  operational_status_filled: 32
  explicit_adhesion_or_payment_field_filled: 2
  entry_date_filled: 9
  operational_labels:
    benevole: 16
    usager: 10
    function_or_responsibility: 6
    blank: 1
~~~

Cette structure renforce le diagnostic précédent.

Le tableur est principalement un **registre opérationnel de personnes gravitant autour des activités**, pas un registre statutaire suffisamment probant pour calculer le corps électoral.

En particulier :

~~~text
33 lignes historiques
≠ 33 membres statutaires

32 statuts opérationnels renseignés
≠ 32 membres votants

2 mentions d’adhésion / paiement
≠ 2 seuls membres

9 dates d’entrée
≠ 9 admissions statutaires prouvées
~~~

Aucune colonne ne fournit à elle seule :

- la décision d’agrément du conseil d’administration exigée par l’article 3 ;
- la catégorie juridique 1995 attribuée ;
- une éventuelle démission ;
- une éventuelle radiation ;
- la continuité de la qualité de membre jusqu’en 2026.

### Conséquence quantitative

Le dénominateur juridique reste donc **UNKNOWN**.

Il serait méthodologiquement incorrect de calculer un « quorum conservatoire » à partir de 33 ou de 40 sans reconstruire les admissions statutaires.

Le prochain gain probatoire ne viendra probablement pas d’un calcul supplémentaire, mais de traces d’agrément, de PV, de cotisations qualifiées ou d’une validation collective préalable de la liste des membres en exercice.




## 3 septies. Recherche ciblée des agréments — résultat au 5 octobre 2026

Une recherche Gmail ciblée sur 2018–2026 a été effectuée avec les termes relatifs à l'adhésion, aux membres actifs, aux bénévoles, aux cotisations et à C.O.R.S.I.C.A.

Résultat utile :

- un courrier du 14 octobre 2019 décrit explicitement l'association comme ayant des « membres actifs qui votent » et des « membres inactifs qui ne votent pas » ;
- cette formulation confirme une pratique de qualification interne, mais correspond davantage à la grammaire du projet statutaire 2018 qu'au texte déposé de 1995 ;
- aucun procès-verbal ou acte individualisé d'agrément du conseil d'administration correspondant aux personnes du registre 2018–2019 n'a été retrouvé lors de cette recherche ;
- aucune campagne d'adhésion interne 2021–2026 suffisamment qualifiée pour reconstruire à elle seule le corps électoral n'a été retrouvée ;
- la déclaration de mars 2026 de « 40 membres actifs » reste donc un ordre de grandeur opérationnel, pas un dénominateur statutaire.

Qualification :

~~~text
existence d'une pratique membres actifs / inactifs
→ ESTABLISHED

équivalence avec catégories des statuts 1995
→ NOT ESTABLISHED

agréments nominatifs du CA
→ NOT FOUND

corps électoral 2026
→ BLOCKED / PRIVATE RECONSTRUCTION REQUIRED
~~~

Cette recherche confirme que la prochaine étape n'est plus une recherche plein texte générale, mais une **qualification nominative privée et contradictoire** des cas plausibles.

## 3 octies. Protocole minimal de qualification privée

Pour chaque personne plausible, la matrice privée doit conserver :

| Champ | Valeur candidate |
|---|---|
| trace d'entrée / relation | source datée |
| agrément du CA | ESTABLISHED / RECONSTRUCTED / NOT FOUND |
| catégorie statutaire 1995 | fondateur / honneur / bienfaiteur / actif / adhérent / UNKNOWN |
| pratique 2018–2020 | actif-votant / inactif / bénévole / usager / fonction / UNKNOWN |
| démission | ESTABLISHED / NOT FOUND |
| radiation | ESTABLISHED / NOT FOUND |
| membre en exercice au cut-off | YES / PROBABLE / DISPUTED / NO / UNKNOWN |
| appartient à l'AG | YES / PROBABLE / DISPUTED / NO / UNKNOWN |
| source de qualification | référence privée |

Le Corpus public ne doit recevoir que les agrégats et la méthode.

Principe conservatoire pour la convocation :

> toute personne dont la qualité votante reste raisonnablement plausible doit être traitée de manière à ne pas être silencieusement privée de la possibilité de faire valoir sa qualité ; la qualification définitive doit être traçable avant le calcul du quorum.

Cette formulation est une règle de robustesse documentaire, non une conclusion juridique sur un cas individuel.

## 3 novies. Triangulation avec les trois participants décrits à l'AG 2025

Un rapprochement privé a été effectué entre le PV rétrospectif de l'AG 2025 et le registre opérationnel 2018–2019.

Résultat agrégé :

~~~yaml
ag_2025_reported_participants: 3
found_in_2018_2019_operational_register: 3
operational_labels:
  president: 1
  volunteer: 1
  volunteer_incubated: 1
explicit_adhesion_field_filled_for_these_rows: 0
entry_date_filled_for_these_rows: 0
~~~

Cette convergence confirme que les personnes décrites dans le PV 2025 appartenaient bien à l'écosystème opérationnel historique de l'association.

Elle **ne résout pas** le problème statutaire :

~~~text
présence dans un ancien registre opérationnel
+
présence rapportée à une AG
≠
preuve d'agrément au sens de l'article 3
≠
catégorie statutaire 1995 établie
~~~

Le cas est particulièrement instructif : même les participants les mieux documentés de l'AG récente ne permettent pas de déduire mécaniquement le dénominateur juridique du quorum.


## 3 decies. Recherche nominative ciblée — saturation des archives passives

Un passage nominatif privé a ensuite été effectué sur les personnes les mieux documentées dans les rôles de gouvernance et sur les deux fondateurs historiques autres que le Président.

### Résultat général

Aucun acte nominatif d'agrément du conseil d'administration conforme à l'article 3 n'a été retrouvé.

Aucune démission ou radiation statutaire explicite des fondateurs recherchés n'a été retrouvée non plus.

Cette seconde absence ne vaut pas preuve de maintien de la qualité : elle signifie seulement `NOT FOUND`.

### Indices de pratique retrouvés

Les archives montrent cependant plusieurs indices forts de fonctions exercées :

- dès mai 2018, une carte de travail de l'Institut porte sur un rendez-vous bancaire pour « déclarer statut trésorier et compte en ligne » et est manipulée par la personne concernée ;
- de 2020 à 2022, une carte récurrente porte le libellé « Frais de l'adhérant LR » ;
- la même personne intervient ensuite de manière répétée sur la banque C.O.R.S.I.C.A. et la conformité documentaire jusqu'en 2023 ;
- le registre 2018–2019 la qualifie d'« ancien secrétaire » ;
- les participants rapportés à l'AG 2025 apparaissent tous dans le registre opérationnel historique.

Ces éléments renforcent l'existence d'une pratique institutionnelle réelle, mais ils ne résolvent pas le point de droit documentaire :

~~~text
fonction effectivement exercée
≠ preuve de l'agrément initial comme membre

libellé « adhérant »
≠ qualification certaine « membre adhérent » au sens technique de l'article 3

présence durable dans la gouvernance
≠ acte d'admission retrouvé
~~~

Le terme « adhérant » utilisé dans une carte de frais est trop ambigu pour classer rétroactivement la personne dans la catégorie statutaire non-votante des « membres adhérents ».

### Changement de phase

La recherche plein texte générale et nominative atteint désormais un rendement décroissant.

~~~text
ARCHIVE SEARCH
→ substantially exhausted for admission acts

NEXT
→ ACTIVE QUALIFICATION
~~~

La suite doit donc privilégier :

1. sollicitation privée des personnes plausibles pour retrouver leurs propres pièces ou souvenirs documentables ;
2. recherche ciblée des anciens PV / registres papier éventuellement hors Drive ;
3. confrontation contradictoire d'une liste candidate avant son gel ;
4. si nécessaire, accompagnement Guid'Asso / greffe sur la régularisation d'une association ancienne dont le registre d'admission est incomplet.

Une attestation ou un souvenir n'est pas traité comme équivalent automatique à l'agrément : il constitue une trace supplémentaire à trianguler avec les pratiques, PV et règles statutaires.


## 3 undecies. Formulaire d'inscription Institut Mariani 2018

Le dossier privé `Adhérents/INSTITUT` contient un Google Form et sa feuille de réponses, créés en juillet 2018.

Audit agrégé, sans identité ni coordonnée :

~~~yaml
registration_form_2018:
  response_rows: 6
  fields_include:
    - identity
    - operational_status
    - email
    - phone
    - identity_document_upload
    - "Cotisation association payée"
  payment_field_filled_in_visible_responses: 0
  statutory_ca_approval_field: absent
  statutory_1995_category_field: absent
~~~

Le formulaire confirme qu'une procédure pratique d'inscription à l'écosystème Institut existait en 2018.

Il ne constitue pas une preuve suffisante d'admission comme membre C.O.R.S.I.C.A. au sens de l'article 3 :

~~~text
formulaire d'inscription Institut
≠ demande statutaire C.O.R.S.I.C.A. démontrée

réponse au formulaire
≠ agrément du conseil d'administration

statut opérationnel saisi
≠ catégorie juridique 1995
~~~

Un dossier de réponses avec pièces d'identité existe également. Il n'a pas été inspecté : ces pièces privées ne sont pas nécessaires à la qualification juridique recherchée et leur consultation ajouterait une exposition de données sans gain probatoire proportionné.

Cette découverte renforce la distinction entre **onboarding opérationnel** et **admission institutionnelle**.

## 3 undecies. Déclaration contemporaine sur la pratique active

Au 5 octobre 2026, le Président précise que la pratique ancienne de C.O.R.S.I.C.A. distingue les membres actifs des autres membres principalement usagers, l’adhésion étant libre.

Selon cette déclaration, seuls deux membres sont aujourd’hui actifs de manière continue : le Président et Maguy Ghionga, actuellement décrite comme Trésorière. Quelques usagers sont actifs épisodiquement.

Cette information modifie fortement la lecture de l’ordre de grandeur « 40 membres actifs » employé en mars 2026 : ce dernier doit être compris comme une estimation de population participante à un projet, et non comme un état nominatif du corps actif continu.

~~~text
40 participants / actifs potentiels dans un projet
≠
40 membres actifs continus
≠
40 membres votants statutaires
~~~

Pour le quorum, la déclaration actuelle est un indice important mais ne suffit toujours pas à résoudre seule les catégories juridiques de 1995. Elle oriente cependant la reconstruction privée vers un petit noyau actif continu + une périphérie d’usagers / participants épisodiques, plutôt que vers l’hypothèse d’un grand corps actif permanent.

## 4. Reconstruction requise

Le registre nominatif de travail doit rester privé et, pour chaque personne, déterminer uniquement ce qui est nécessaire : catégorie statutaire, trace d’entrée, éventuelle sortie, droit de vote et source de cette qualification.

Le Corpus public pourra publier l’agrégat :

~~~text
membres votants établis : N
cas probables : M
cas à vérifier : K
quorum conservatoire : Q
~~~

## 4 bis. Perte de qualité de membre : conséquence pour la reconstruction

L'article 4 des statuts 1995 prévoit que la qualité de membre se perd :

- par démission ;
- ou par **radiation prononcée** par le conseil d'administration, notamment pour non-paiement de cotisation ou motif grave, avec possibilité de recours à l'assemblée générale.

Cela interdit une simplification fréquente mais ici dangereuse :

~~~text
pas de cotisation retrouvée
≠
perte automatique de la qualité de membre
~~~

Pour les personnes qui auraient réellement acquis une catégorie statutaire votante, il faut donc rechercher une démission, une radiation ou une autre cause certaine de sortie avant de les retirer du dénominateur.

Inversement, l'ancien tableur 2018–2019 ne prouve pas à lui seul que ses 33 entrées avaient acquis une catégorie statutaire votante : plusieurs y apparaissent seulement comme « usager » ou « bénévole ».

La reconstruction correcte est donc bilatérale :

~~~text
admission / catégorie votante à établir
+
sortie éventuelle à établir
=
qualité de membre en exercice
~~~

## 4 ter. Risque juridique : l'agrément statutaire n'est pas une formalité décorative

Une jurisprudence de la Cour de cassation directement pertinente pour la méthode de reconstruction a été identifiée :

- Cour de cassation, 2e chambre civile, 6 septembre 2018, n° 17-19.657 ;
- source officielle : https://www.legifrance.gouv.fr/juri/id/JURITEXT000037450583

Dans l'affaire jugée, les statuts prévoyaient une demande d'adhésion suivie d'une décision du conseil d'administration. La juridiction a notamment retenu que le seul paiement de la cotisation ne suffisait pas à établir la qualité de membre lorsque l'agrément du conseil était statutairement requis ; la présence de personnes dont la qualité de membre n'était pas démontrée avait contribué à l'irrégularité de la composition des organes et à l'annulation des décisions.

Cette décision ne préjuge pas automatiquement du cas C.O.R.S.I.C.A., dont les faits et le texte sont propres. Elle confirme toutefois le risque méthodologique :

~~~text
participation aux activités
≠ qualité de membre

paiement / adhésion pratique
≠ nécessairement agrément statutaire

présence à une AG antérieure
≠ preuve suffisante si la qualité de membre est contestable
~~~

Pour C.O.R.S.I.C.A., l'article 3 des statuts 1995 exige précisément un agrément par le conseil d'administration après présentation par plusieurs membres.

Conséquence de prudence :

> **Le corps électoral ne doit pas être construit par simple présomption à partir du tableur, des cotisations, du bénévolat ou de la participation à des réunions. Il faut rechercher l'acte d'admission ou un faisceau suffisamment robuste permettant d'établir qu'une admission statutaire a réellement eu lieu.**

## 5. Principe conservatoire

En cas d’incertitude sur une qualité de membre encore plausible, le cas doit rester explicitement à vérifier. Aucune exclusion du corps votant ne doit être déduite d’un simple silence documentaire.