---
title: "Sénatoriales Haute-Corse 2026 — matrice de redondance des canaux matériels de dépôt"
author: "Jean Hugues Noël Robert"
date: "2026-10-07"
version: "1.0"
status: "active — pre-filing"
language: "fr"
document_role: "operational"
document_kind: "filing-channel-matrix"
visibility: "public"
lifecycle_state: "active"
related:
  - "requete-conseil-constitutionnel-projet-v0.18.md"
  - "bordereau-pieces-requete-conseil-constitutionnel-v0.10.md"
  - "checklist-depot-requete-cc-2026-10-07.md"
  - "pre-filing-operational-plan-2026-10-07.md"
  - "filing-package-manifest-2026-10-07.md"
---

# Matrice de redondance des canaux matériels de dépôt

## 1. Règle juridique

L'article 33 de l'ordonnance n° 58-1067 fixe l'échéance au **7 octobre 2026 à 18 h** dans le présent dossier.

L'article 34 ne prévoit que deux destinataires juridiques :

1. le **secrétariat général du Conseil constitutionnel** ;
2. le **représentant de l'État**.

Le représentant de l'État avise ensuite électroniquement le secrétaire général et assure la transmission de la requête.

L'article 35 impose que la requête contienne les moyens d'annulation et que les pièces produites à leur soutien soient annexées.

Sources primaires :
- https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000023882786
- https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000006529992
- https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000006529993

## 2. Principe de redondance

La redondance doit porter sur les **voies de remise**, jamais sur le contenu :

~~~text
un paquet canonique gelé
→ plusieurs exemplaires strictement identiques
→ plusieurs voies matérielles indépendantes
→ plusieurs preuves de réception
~~~

Interdiction opérationnelle :

~~~text
voie A = version X
voie B = version X+1
~~~

Toutes les voies mobilisées doivent porter la même requête, le même bordereau et, autant que matériellement possible, le même jeu de pièces.

Chaque exemplaire peut porter une mention de traçabilité du type :

> « Exemplaire redondant du même paquet de dépôt — ne constitue pas un recours distinct. »

## 3. Matrice des voies

| Voie | Destinataire juridique | Modalité matérielle | Confiance juridique | Risque pratique | Preuve recherchée | Statut |
|---|---|---|---|---|---|---|
| **A** | Représentant de l'État | Remise physique à la préfecture de la Haute-Corse à Bastia | **Haute** : destinataire expressément prévu par l'art. 34 | Accueil sur rendez-vous / fermeture ordinaire 15 h 30 | récépissé daté + heure + cachet/signature + copie du bordereau | **PRIMAIRE** |
| **B** | Secrétariat général du Conseil constitutionnel | Remise physique directe à Paris, par le requérant ou un porteur/coursier | **Haute sur le destinataire** ; modalités pratiques à confirmer | distance Corse→Paris ; horaires de réception non établis par les sources examinées | preuve de remise au Conseil avec date/heure | **REDONDANCE FORTE si logistiquement possible** |
| **C** | Secrétariat général du Conseil constitutionnel | Coursier / express avec remise physique garantie avant l'échéance | **Haute si réception effective avant 18 h** | aléa transport ; nécessité d'une preuve de livraison incontestable | preuve électronique + nom/service receveur + heure | **REDONDANCE CONDITIONNELLE** |
| **D** | Secrétariat général du Conseil constitutionnel | Lettre recommandée / courrier postal | **Possible en principe comme requête écrite adressée au SG**, mais la jurisprudence regarde la réception | très élevé à J0 ; cachet d'expédition insuffisant comme sécurité | avis de réception antérieur à 18 h | **NE PAS UTILISER COMME FILET PRINCIPAL LE 7/10** |
| **E** | Représentant de l'État | Lettre recommandée / express à la préfecture | Même limite : seule la réception utile avant l'échéance sécurise | aléa postal | avis de réception / remise avant 18 h | **SECONDAIRE seulement si réception garantie** |
| **F** | Représentant de l'État | Remise par commissaire de justice / porteur mandaté à la préfecture | **Adjoint probatoire**, pas troisième canal juridique | disponibilité du professionnel / acceptation matérielle | acte/constat de remise ou de tentative + récépissé administratif | **REDONDANCE PROBATOIRE** |
| **G** | Représentant de l'État ? | Remise à la sous-préfecture de Corte | **NON ÉTABLI** : l'art. 34 vise le représentant de l'État ; aucune source examinée ne confirme que la sous-préfecture reçoit ce contentieux pour son compte | risque d'incompétence matérielle / routage tardif | confirmation écrite préalable de la préfecture + récépissé | **NE PAS COMPTER COMME CANAL SÛR SANS CONFIRMATION** |
| **H** | Préfecture / Conseil | Courriel avec PDF du paquet | **NON ACQUIS comme mode de saisine du requérant** ; l'art. 34 mentionne l'électronique pour la transmission préfet→Conseil | risque d'irrecevabilité si utilisé seul | accusé institutionnel explicite | **COPIE D'INFORMATION / TRACE, JAMAIS SEUL** |
| **I** | Préfecture / Conseil | Télécopie, si numéro institutionnel utilisable | **NON ÉTABLI** par les sources examinées | preuve de contenu/réception imparfaite, procédure non publiée | rapport de transmission + confirmation téléphonique/écrite | **TRACE REDONDANTE seulement** |

## 4. Date de réception, non simple date d'envoi

Le Conseil constitutionnel a déjà rejeté comme tardives des requêtes en constatant la **date à laquelle elles ont été reçues au secrétariat général** après l'expiration du délai.

Conséquence opérationnelle :

> une preuve d'expédition avant 18 h ne doit pas être traitée comme équivalente à une preuve de réception avant 18 h.

Références :
- décision n° 2017-5267 QPC/SEN du 1er décembre 2017 ;
- décision n° 2017-5256 QPC/AN du 16 novembre 2017.

## 5. Préfecture de Haute-Corse — contrainte horaire

La préfecture publie des horaires ordinaires d'accueil au public :

- 8 h 30–11 h 30 ;
- 13 h 30–15 h 30 ;
- accueil indiqué comme étant sur rendez-vous.

Source :
https://www.haute-corse.gouv.fr/Services-de-l-Etat/Prefecture-et-sous-prefectures/Prefecture-de-la-Haute-Corse/Organisation-horaire-et-coordonnees-de-la-Prefecture

Adresse postale publique :
Préfecture de la Haute-Corse
Rond-point Maréchal Leclerc de Hautecloque
20401 Bastia Cedex 9

Conséquence :

> le seuil opérationnel sûr n'est pas 18 h mais l'heure réelle à laquelle une remise horodatée peut encore être obtenue.

## 6. Conseil constitutionnel

Adresse institutionnelle publique :
Conseil constitutionnel
2 rue de Montpensier
75001 Paris

Le site du Conseil confirme l'existence d'un accueil à cette adresse, mais les sources examinées ne donnent pas ici un horaire publié spécifique pour la réception des requêtes électorales.

Donc :

> toute remise physique directe à Paris doit faire l'objet d'une confirmation pratique préalable de l'accès et de la réception.

## 7. Ordre de mobilisation recommandé

### Niveau 1 — créer au moins une saisine incontestable

1. **Remise physique à la préfecture de Bastia**, le plus tôt possible, avec deux exemplaires de la fiche de remise.
2. Obtenir une trace comportant au minimum date, heure, service receveur et identification suffisante du paquet.

### Niveau 2 — redondance indépendante du même canal juridique ou de l'autre destinataire

3. Si logistiquement disponible, faire déposer **un exemplaire identique au Conseil constitutionnel à Paris** par un porteur/coursier.
4. Si un commissaire de justice peut intervenir utilement, lui confier un exemplaire identique pour remise à la préfecture ou, à défaut, constat de la remise/tentative.

### Niveau 3 — traces complémentaires

5. Après ou parallèlement aux remises matérielles, transmettre une **copie numérique strictement identique** aux contacts institutionnels déjà utilisés, avec objet indiquant explicitement :
   « COPIE DE TRAÇABILITÉ — requête remise matériellement le [date/heure] — ne se substitue pas au dépôt article 34 ».
6. Conserver les accusés automatiques et humains sans leur attribuer seuls la qualité de saisine.

## 8. Contrôle anti-divergence

Avant départ :

- calculer SHA-256 de la requête PDF ;
- calculer SHA-256 du bordereau PDF ;
- calculer SHA-256 du recueil/pièces ou du manifeste correspondant ;
- imprimer ou conserver une fiche portant ces empreintes ;
- numéroter les exemplaires physiques : A, B, C… ;
- vérifier que tous les exemplaires sont binaires ou matériellement identiques.

Après chaque remise :

- photographier / numériser la preuve de réception ;
- noter immédiatement date, heure, lieu, personne/service, incident éventuel ;
- ne modifier aucun exemplaire déjà remis ;
- si une correction devient indispensable, la qualifier comme dépôt ou mémoire ultérieur distinct, sans réécrire l'histoire du premier dépôt.

## 9. Point à confirmer le matin du 7 octobre

Appeler dès l'ouverture :

1. la préfecture de Haute-Corse pour confirmer le service concret receveur et l'accès sans ambiguïté ;
2. le Conseil constitutionnel pour confirmer les modalités pratiques d'une remise directe à son secrétariat général ;
3. si envisagée, la sous-préfecture de Corte, mais uniquement pour obtenir une confirmation explicite qu'elle est habilitée à recevoir la requête **pour le représentant de l'État**.

Les réponses orales doivent être notées comme telles ; demander si possible une confirmation écrite.
