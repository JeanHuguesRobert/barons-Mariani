---
title: "Sénatoriales 2026 — trigger packet post-scrutin"
date: "2026-09-25"
target_event: "scrutin et proclamation du 27 septembre 2026"
status: "prepared_waiting_trigger"
language: "fr"
license: "CC BY-SA 4.0"
document_role: "operational-readiness"
document_kind: "reality-probe-trigger-packet"
visibility: "public"
lifecycle_state: "active"
update_policy: "UP-DEFAULT-REVIEWED"
related_probes:
  - RP-SEN-07
  - RP-SEN-08
  - RP-SEN-09
  - RP-SEN-10
review:
  status: unreviewed
  reviewed_by: []
---

# Sénatoriales 2026 — trigger packet post-scrutin

## Objet

Préparer l'ouverture des nouvelles surfaces d'observation créées par le scrutin et la proclamation, sans présumer qu'une branche contentieuse sera utilisée.

Le packet doit être activé à partir du moment où une source officielle publie ou constate les résultats / la proclamation.

## 1. Source officielle de départ

Résultats du ministère de l'Intérieur — Haute-Corse (2B) :

https://www.resultats-elections.interieur.gouv.fr/Senatoriales2026/ensemble_geographique/94/2B/index.html

État observé au 25 septembre :

- scrutin annoncé le 27 septembre 2026 ;
- un siège à pourvoir ;
- page actuellement en phase de publication des candidatures.

Cette observation n'anticipe aucun résultat.

## 2. RP-SEN-07 — fixer l'horloge officielle

Au premier constat post-scrutin :

```yaml
capture:
  source_url: ...
  observed_at: ...
  page_state: candidatures|resultats_provisoires|resultats_publies|autre
  proclaimed_at:
    value: ...
    source: ...
    confidence: ...
  elected_person:
    value: ...
    source: ...
```

Règle :

> ne pas déduire une heure de proclamation d'une simple heure de consultation du site.

Si seule la date est disponible, conserver l'heure comme `UNKNOWN`.

## 3. RP-SEN-08 — fenêtre des PV et annexes

L'article 32 de l'ordonnance n° 58-1067 prévoit que les procès-verbaux des commissions de recensement et leurs annexes sont tenus pendant dix jours à la disposition notamment des personnes ayant fait une déclaration de candidature.

Source officielle :
https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000023882783

### Probe

Dès que la proclamation est suffisamment fixée :

1. identifier le lieu / service matériel de consultation ;
2. demander ou effectuer la consultation dans la fenêtre ouverte ;
3. inventorier avant d'interpréter ;
4. rechercher d'abord les **sources de sources** : annexes, bordereaux, références, mentions de transmission ;
5. ne copier que ce qui est utile à la carte des inconnues.

### Sorties

```text
accès complet
→ inventorier les objets nouveaux
→ créer seulement les probes justifiés

accès partiel
→ identifier précisément le périmètre manquant

refus / obstacle
→ documenter demande, heure, interlocuteur et fondement invoqué
→ ne pas transformer le refus en preuve sur le contenu

aucune nouveauté
→ résultat valide
→ fermer les branches concernées si le périmètre est suffisamment certain
```

## 4. RP-SEN-09 — branche Conseil constitutionnel

L'article 33 de l'ordonnance n° 58-1067 prévoit que l'élection peut être contestée jusqu'au dixième jour suivant la proclamation, au plus tard à 18 h, notamment par les personnes ayant fait acte de candidature.

Source officielle :
https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000023882786

Cette branche doit être séparée en deux décisions :

```text
A — conserver l'option
B — exécuter ou non l'option
```

Le trigger packet ne décide que **A**.

### Préservation de l'option

À l'ouverture de l'horloge :

- fixer la date source de proclamation ;
- calculer le terme théorique, puis le vérifier ;
- conserver le jugement, les échanges TA/préfecture et la knowledge matrix courante ;
- figer la liste des inconnues encore ouvertes ;
- distinguer les moyens déjà documentés des moyens dépendant de pièces manquantes.

Aucune requête n'est envoyée automatiquement.

## 5. RP-SEN-10 — capacité d'instruction

Si RP-SEN-09 est ultérieurement exécuté, l'article 42 permet au Conseil constitutionnel et à ses sections d'ordonner une enquête et de se faire communiquer les documents et rapports ayant trait à l'élection.

Source officielle :
https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000006530002/2026-03-15

### Liste de pièces potentiellement utiles si elles restent manquantes

- logs d'acceptation / remise du message de 17:57:55 ;
- bordereaux de transmission au TA ;
- productions préfectorales postérieures à la saisine initiale ;
- traces des demandes d'originaux ;
- identité / heure de la « Réception d'une lettre » Sagace ;
- trace d'audience / minute si leur accès direct reste non résolu.

La décision de demander une mesure d'instruction reste distincte de son éventuelle ordonnance par le Conseil.

## 6. Arbre post-trigger

```text
proclamation
    ↓
RP-SEN-07 fixe l'horloge
    ├── RP-SEN-08 consultation PV / annexes
    │       ↓
    │   nouvelles sources ?
    │       ├── oui → nouveaux probes
    │       └── non → fermeture documentée
    │
    └── RP-SEN-09 option contentieuse disponible
            ├── non exécutée → consigner expiration
            └── exécutée
                  ↓
              RP-SEN-10
              mesure d'instruction éventuellement sollicitée
```

## 7. Condition de reprise du batch

Rejouer le batch incrémental dès l'un des événements suivants :

- résultat / proclamation officiellement publié ;
- PV ou annexe consulté ;
- réponse de la préfecture ;
- réponse du TA ;
- nouveau détenteur technique identifié ;
- décision humaine sur RP-SEN-09.

## 8. Discipline

Ce packet sert à **maximiser l'explorabilité**.

Il ne doit pas :

- transformer une voie juridique en recommandation politique ou contentieuse ;
- confondre résultat électoral et mérite du litige ;
- attendre les réponses CADA/CNIL pour préserver une éventuelle option électorale plus courte ;
- conclure qu'une pièce manquante n'existe pas sans examiner le périmètre du système observé.
