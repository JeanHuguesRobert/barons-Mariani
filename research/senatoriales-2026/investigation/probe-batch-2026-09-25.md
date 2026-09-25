---
title: "Sénatoriales 2026 — batch d'expansion et réduction des Reality Probes"
date: "2026-09-25"
batch_id: "RPB-SEN-2026-09-25-01"
status: "working"
language: "fr"
license: "CC BY-SA 4.0"
document_role: "analysis"
document_kind: "reality-probe-batch"
visibility: "public"
lifecycle_state: "active"
update_policy: "UP-DEFAULT-REVIEWED"
source_map: "research/senatoriales-2026/investigation/probe-map.md"
method:
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/reality_probe_mapping.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/reality_probe_selection.md"
execution_semantics: "analysis only; this batch does not authorize or execute external Acts"
review:
  status: unreviewed
  reviewed_by: []
---

# Sénatoriales 2026 — batch d'expansion et réduction des Reality Probes

## 0. Contrat du batch

Ce batch applique en une fois la méthode :

```text
PASS A — EXPAND
→ développer les sorties qui changent réellement la carte

PASS B — REDUCE
→ fusionner les équivalences
→ détecter les dépendances, redondances et gaps
→ rendre visibles les deadlines / risques d'expiration
→ conserver les branches non exécutées

EXECUTE
→ phase séparée, jamais implicite
```

Il ne décide pas d'engager un recours, une autorité ou une interaction supplémentaire.

---

# PASS A — EXPANSION

## RP-SEN-01 — Préfecture : traces mail / documents / transmissions

**Prior.** Le message de 17:57:55 est établi côté expéditeur ; l'heure d'acceptation côté destinataire et son éventuelle transmission au TA restent ouvertes.

### O1-A — logs : acceptation avant 18 h

**Établit :**
- un événement technique d'acceptation avant 18 h, selon la sémantique exacte du timestamp fourni.

**N'établit pas :**
- lecture humaine avant 18 h ;
- traitement avant 18 h ;
- transmission au TA ;
- effet juridique du message.

**Ferme / affaiblit :**
- « aucune acceptation serveur avant 18 h ».

**Ouvre :**
- heure de remise ;
- heure de lecture / traitement si traçable ;
- transmission au TA.

**Next :**
- RP-SEN-06 ;
- RP-SEN-14 ;
- éventuellement RP-SEN-13 si le journal révèle un autre système.

### O1-B — logs : acceptation à partir de 18 h

**Établit :**
- absence d'acceptation avant 18 h dans le journal considéré.

**N'établit pas :**
- la cause du retard ;
- la complétude de la chaîne technique ;
- la portée juridique de ce timestamp.

**Ouvre :**
- topologie transport ;
- timestamps intermédiaires ;
- éventuel filtrage / relais.

**Next :**
- RP-SEN-05 ;
- RP-SEN-13 ;
- RP-SEN-14.

### O1-C — transfert au TA documenté

**Établit :**
- une transmission institutionnelle ou technique, selon la trace fournie.

**N'établit pas :**
- nécessairement sa prise de connaissance par la formation de jugement.

**Next :**
- trianguler avec RP-SEN-02 / RP-SEN-06 / RP-SEN-14.

### O1-D — aucune transmission retrouvée

**Établit seulement :**
- absence dans le périmètre effectivement interrogé.

**Question suivante :**
- ce périmètre couvre-t-il toutes les voies possibles ?

**Next :**
- RP-SEN-05 / RP-SEN-06 / RP-SEN-13.

### O1-E — autre détenteur / autre système identifié

**Rendement génératif élevé.**

**Next :**
- RP-SEN-13 immédiatement cartographiable.

### O1-F — données expirées / détruites

**Établit :**
- indisponibilité actuelle si l'information est précise.

**Ouvre :**
- politique de rétention ;
- date de purge ;
- copies secondaires ;
- traces dérivées ;
- éventuelle limitation future pour ce qui existe encore.

**Next :**
- RP-SEN-05 ;
- RP-SEN-13 ;
- RP-SEN-04 si d'autres données personnelles pertinentes subsistent.

### O1-G — refus ou communication partielle

**Next :**
- qualifier document par document / donnée par donnée ;
- RP-SEN-11 ou RP-SEN-12 seulement lorsque leur déclencheur propre est atteint.

### O1-H — silence

**Établit :**
- état du canal et de la demande à une date donnée.

**N'établit pas :**
- U1, U2 ou U3.

---

## RP-SEN-02 — TA Bastia : dossier matériel / audience / minute

### O2-A — six réponses complètes

Ferme ou réduit directement U4/U5 ; chaque réponse reste atomique dans la matrice.

### O2-B — « Réception d'une lettre » identifiée

**Next :**
- comparer auteur, objet, heure, pièce et relation au dossier ;
- si pièce nouvelle : inspection dédiée + RP-SEN-14.

### O2-C — inventaire de pièces fourni

**Rendement génératif :**
- potentiellement plusieurs pièces ou productions nouvelles.

**Next :**
- comparer l'inventaire avec les traces préfectorales et les pièces déjà détenues.

### O2-D — document d'audience confirmé et communiqué

**Établit :**
- existence + contenu directement accessible.

**Next :**
- qualifier ce qu'il établit réellement ; ne pas assimiler trace d'audience à transcription exhaustive.

### O2-E — document confirmé mais non communicable

**Établit :**
- existence.

**N'établit pas :**
- contenu.

**Next :**
- demander / noter le fondement et rechercher une autre voie si pertinente.

### O2-F — absence déclarée de trace séparée d'audience

Ferme la branche « document séparé détenu par le greffe », sous réserve de la précision de la réponse.

### O2-G — minute accessible

**Next :**
- inspection / comparaison avec l'expédition reçue.

### O2-H — réponse partielle ou silence

Conserver chaque sous-question indépendamment ; ne pas fermer U4/U5 en bloc.

---

## RP-SEN-03 — trace expéditeur originale

### O3-A — message original + Message-ID + headers conservés

**Établit / préserve :**
- émission ;
- identifiants côté expéditeur ;
- route et métadonnées effectivement présentes.

**N'établit pas :**
- acceptation serveur destinataire.

**Next :**
- RP-SEN-14 ;
- comparaison avec O1-A/O1-B.

### O3-B — informations de livraison supplémentaires disponibles

**Rendement génératif :**
- nouveaux timestamps ou serveurs intermédiaires.

**Next :**
- RP-SEN-05 / RP-SEN-13 si une infrastructure tierce apparaît.

### O3-C — aucune métadonnée supplémentaire

**Résultat valide :**
- la branche expéditeur est conservée mais ne réduit pas U1 au-delà de l'émission.

**Stop :**
- ne pas multiplier les extractions identiques.

---

## RP-SEN-04 — limitation RGPD

### O4-A — limitation acceptée

**Préserve :**
- les données visées sous le régime applicable.

**N'établit pas :**
- leur contenu ;
- leur communication.

### O4-B — limitation refusée / inapplicable

**Next :**
- qualifier le motif ;
- ne pas convertir le refus en preuve d'existence ou d'inexistence.

### O4-C — responsable indique ne plus avoir besoin des données mais les conserve

**Rendement génératif :**
- précise l'état de conservation et peut justifier une analyse plus ciblée de l'article 18.

### O4-D — aucune donnée correspondante n'est détenue

Retour vers topologie : RP-SEN-05 / RP-SEN-13.

---

## RP-SEN-05 — topologie de la messagerie

### O5-A — système et détenteur identifiés

**Établit :**
- nouvelle topologie.

**Next :**
- RP-SEN-13.

### O5-B — politique de conservation identifiée

**Établit :**
- une durée ou un critère de rétention.

**Effet :**
- crée une deadline épistémique réelle ou permet d'écarter une urgence supposée.

### O5-C — plusieurs couches identifiées

Exemple abstrait :

```text
passerelle
→ antispam
→ serveur
→ boîte
→ archivage
```

**Next :**
- ne pas demander « le log » comme objet unique ;
- sélectionner les couches capables de discriminer U1.

### O5-D — aucune information topologique obtenue

Ne ferme pas U1 ; peut déplacer la recherche vers un autre observateur.

---

## RP-SEN-06 — reçus / bordereaux de transmission TA

### O6-A — reçu initial complet avec liste de fichiers et heure

**Établit :**
- état de la transmission initiale.

**Next :**
- comparer à l'inventaire TA et au corpus candidat.

### O6-B — reçu d'une production ultérieure

**Établit :**
- existence et timing d'une transmission postérieure.

**Next :**
- identifier son contenu précis ;
- RP-SEN-14.

### O6-C — seulement un identifiant de transaction

**Rendement génératif :**
- identifiant exploitable pour demander ou retrouver le détail.

### O6-D — aucun bordereau distinct

**Next :**
- vérifier si l'inventaire est incorporé à une autre trace ou vue.

---

## RP-SEN-07 — proclamation officielle / ouverture des horloges

Le scrutin du 27 septembre 2026 est fixé par le décret n° 2026-301 du 21 avril 2026.

### O7-A — proclamation officielle identifiée avec date / heure

**Établit :**
- ancre temporelle pour les fenêtres post-scrutin.

**Next :**
- activer RP-SEN-08 ;
- rendre RP-SEN-09 temporellement évaluable.

### O7-B — résultats publiés mais heure de proclamation non visible

**Next :**
- chercher l'acte / PV / annonce permettant de fixer la proclamation, sans inventer l'heure.

### O7-C — correction ultérieure des résultats

**Next :**
- conserver versions et timestamps ;
- ne pas écraser l'état antérieur.

---

## RP-SEN-08 — PV de recensement et annexes

L'article 32 de l'ordonnance n° 58-1067 prévoit une mise à disposition pendant dix jours pour les personnes ayant fait une déclaration de candidature.

### O8-A — consultation complète

**Rendement ciblé :**
- contenu du dossier final.

**Rendement sérendipitaire / génératif :**
- annexes, références ou objets non anticipés.

**Next :**
- créer de nouveaux probes seulement pour les objets matériels nouvellement révélés.

### O8-B — consultation partielle

**Next :**
- identifier précisément ce qui manque et pourquoi.

### O8-C — accès refusé ou contesté

**Établit :**
- état du canal d'accès.

**Next :**
- documenter immédiatement date, demande, réponse et fondement invoqué ;
- ne pas présumer la solution juridique.

### O8-D — aucune nouveauté

**Résultat utile :**
- le dossier final n'ajoute aucun discriminant identifié.

**Stop possible :**
- ne pas forcer une signification à l'absence de nouveauté.

---

## RP-SEN-09 — saisine éventuelle du Conseil constitutionnel

### O9-A — branche non exécutée

**Important :**
- la Probe Map conserve néanmoins la voie comme possibilité historique jusqu'à expiration.

### O9-B — requête déposée et enregistrée

**Établit :**
- nouveau contentieux / nouvel observateur institutionnel.

**Next :**
- suivre instruction ;
- RP-SEN-10 devient disponible comme demande ou signalement d'utilité.

### O9-C — irrecevabilité procédurale

**Établit :**
- fermeture de cette voie pour le motif retenu.

**N'établit pas :**
- vérité ou fausseté des faits documentaires sous-jacents.

### O9-D — examen au fond

**Next :**
- conserver les échanges, observations, pièces demandées et mesures d'instruction comme nouvelles traces.

---

## RP-SEN-10 — mesure d'instruction devant le Conseil constitutionnel

L'article 42 permet au Conseil et à ses sections d'ordonner une enquête et de se faire communiquer des documents et rapports ayant trait à l'élection.

### O10-A — mesure ordonnée et documents produits

**Rendement élevé :**
- changement d'observateur réussi ;
- nouvelles traces potentiellement inaccessibles auparavant.

### O10-B — mesure non ordonnée

**N'établit pas :**
- inexistence des documents ;
- inutilité intrinsèque des questions.

### O10-C — mesure partielle

**Next :**
- traiter chaque document obtenu comme trace distincte ;
- ne pas considérer la non-production du reste comme preuve de non-existence.

---

## RP-SEN-11 — CADA

La CADA indique qu'une administration dispose d'un mois pour répondre à une demande de communication ; le silence vaut refus implicite, et la saisine intervient après un refus exprès ou tacite.

### O11-A — avis favorable à la communication

**Établit :**
- position de la CADA sur la communicabilité.

**N'établit pas :**
- contenu des documents avant leur communication.

### O11-B — avis défavorable / incompétence / document juridictionnel

**Établit :**
- fermeture ou déplacement de la voie CRPA pour le motif retenu.

**Next :**
- re-router seulement si un autre régime est réellement pertinent.

### O11-C — administration communique pendant la procédure

**Effet :**
- le probe produit directement des traces sans attendre une issue plus formelle.

---

## RP-SEN-12 — CNIL

### O12-A — réponse du responsable obtenue avant toute réclamation

**Effet :**
- peut rendre la branche CNIL inutile ou la restreindre aux résidus.

### O12-B — réclamation et intervention CNIL

**Rendement :**
- nouvel observateur sur le traitement des données personnelles.

### O12-C — données hors périmètre du droit d'accès ou inexistantes

**Next :**
- ne pas transformer un échec RGPD en conclusion CRPA ou contentieuse.

---

## RP-SEN-13 — nouveau détenteur technique

### O13-A — détention confirmée

**Next :**
- probe ciblé sur les traces exactes et leur conservation.

### O13-B — détention niée mais nouveau détenteur indiqué

**Rendement génératif :**
- continuation récursive RP-SEN-13 vers le détenteur suivant.

### O13-C — chaîne circulaire de redirections

**Observation :**
- topologie institutionnelle problématique ou incomplète.

**Discipline :**
- cartographier la boucle ;
- ne pas en inférer une intention.

### O13-D — détenteur final identifié mais traces expirées

**Ferme :**
- cette branche documentaire, si la réponse est suffisamment précise.

**Next :**
- rechercher seulement les copies / traces dérivées encore plausibles.

---

## RP-SEN-14 — reconstruction multitraces

### O14-A — convergence des timestamps et inventaires

**Établit :**
- chaîne cohérente pour les événements effectivement couverts.

### O14-B — divergence explicable

Exemple :

```text
send time
≠ gateway acceptance
≠ mailbox delivery
≠ human opening
≠ TA filing
```

**Résultat :**
- la divergence cesse d'être une contradiction une fois la sémantique des événements établie.

### O14-C — divergence non expliquée

**Next :**
- créer un probe ciblé sur le maillon discriminant, pas une nouvelle demande générale.

### O14-D — nouvel objet absent de la carte

**Rendement génératif :**
- créer un nouvel Ux et, si nécessaire, un nouveau RP-SEN-nn.

---

# PASS B — RÉDUCTION

## 1. États après expansion

### Actifs / en attente d'une réponse déjà demandée

```text
RP-SEN-01
RP-SEN-02
```

Aucun nouveau courrier identique n'est justifié sans événement nouveau.

### Disponible sans dépendre d'une réponse institutionnelle

```text
RP-SEN-03
RP-SEN-14
```

Ce sont des probes internes / de préservation et convergence.

### Conditionnels sur information nouvelle

```text
RP-SEN-04
RP-SEN-05
RP-SEN-06
RP-SEN-13
```

Ils deviennent plus précis si RP-SEN-01/02 révèle une topologie ou une lacune.

### Déclenchés par changement de phase

```text
RP-SEN-07 → scrutin / proclamation
RP-SEN-08 → proclamation
RP-SEN-09 → proclamation + décision humaine d'utiliser ou non la voie
RP-SEN-10 → seulement si RP-SEN-09 est exécuté
```

### Déclenchés par refus / silence selon leur régime propre

```text
RP-SEN-11 → CRPA / CADA
RP-SEN-12 → RGPD / CNIL
```

## 2. Dominances / redondances

Aucun des deux probes actifs RP-SEN-01 et RP-SEN-02 ne domine l'autre : ils observent des systèmes distincts et leur valeur vient précisément de la triangulation.

RP-SEN-05 ne doit pas être exécuté comme demande autonome tant que RP-SEN-01 peut encore révéler directement le détenteur ou le système : sa valeur augmente en cas de réponse « non détenu ici », « expiré » ou « géré par X ».

RP-SEN-06 est partiellement contenu dans RP-SEN-01 et RP-SEN-02. Il devient utile seulement si leurs réponses restent trop globales pour identifier les transactions de dépôt.

RP-SEN-11 et RP-SEN-12 ne sont pas interchangeables : le premier concerne le régime de communication des documents administratifs lorsqu'il est applicable ; le second les droits relatifs aux données personnelles. Une même trace peut nécessiter de distinguer les deux régimes.

RP-SEN-10 n'existe opérationnellement qu'à l'intérieur de RP-SEN-09 ; il reste néanmoins séparé dans la carte parce qu'il représente une capacité d'observation distincte.

## 3. Deadlines et durée de vie

### Risque de rétention technique

**Classe : inconnue mais potentiellement courte.**

Objet :
- journaux de messagerie ;
- journaux de filtrage / transfert ;
- métadonnées de systèmes.

Conséquence :
- la demande de conservation déjà envoyée fait partie de RP-SEN-01 ;
- RP-SEN-04 ne doit être activé que si ses conditions propres deviennent pertinentes.

### Scrutin

Le décret n° 2026-301 convoque les collèges électoraux le **27 septembre 2026**.

Source :
https://www.legifrance.gouv.fr/loda/id/JORFTEXT000053925339

### Fenêtre article 32

Après l'élection, les PV de recensement sont mis à disposition pendant **dix jours** des personnes visées par l'article 32.

Source :
https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000023882783

### Contentieux / instruction

Les articles 33 et suivants de l'ordonnance organique régissent la contestation de l'élection ; l'article 42 fournit un pouvoir d'instruction au Conseil constitutionnel.

Source :
https://www.legifrance.gouv.fr/codes/section_lc/JORFTEXT000000705065/LEGISCTA000006096045/

### CADA

La CADA rappelle qu'une demande de communication reçoit en principe une réponse dans le mois ; le silence constitue un refus implicite permettant ensuite sa saisine.

Source :
https://www.cada.fr/administration/la-communication-des-documents-administratifs

## 4. Gaps détectés par le batch

L'expansion révèle trois catégories de probes insuffisamment explicites dans la carte initiale.

### NEW-RP-A — corpus juridique et administratif officiel

**Fonction :** `PASSIVE / DISCRIMINATE`

Objet :
- consolider les textes applicables ;
- identifier les instructions, formulaires, notices ou documents officiels relatifs au dépôt et à la régularisation des candidatures sénatoriales ;
- distinguer ce que dit la loi, ce que dit une instruction et ce qui relève d'une pratique locale.

Ce probe ne dépend d'aucune réponse de la préfecture.

### NEW-RP-B — reconstruction intégrale côté candidat

**Fonctions :**
- `PRESERVE`
- `TRIANGULATE`

Objet :
- reconstituer le bundle exact envoyé / déposé ;
- conserver chaque version des CERFA et documents ;
- associer chaque message à son Message-ID, timestamp et pièce ;
- reconstituer la séquence des échanges du 11 septembre sans s'appuyer sur des résumés postérieurs.

### NEW-RP-C — jurisprudence comparable

**Fonction :** `PASSIVE / REVEAL`

Objet :
- rechercher les décisions du Conseil constitutionnel et, lorsque pertinent, du TA sur des refus d'enregistrement de candidatures sénatoriales ;
- identifier les faits discriminants retenus dans les précédents ;
- ne pas transposer mécaniquement une solution dont les faits diffèrent.

Ces trois probes sont **candidats générés par le batch** ; ils ne sont pas encore numérotés dans la carte canonique afin de conserver une étape de revue avant promotion.

## 5. Inconnues sans probe détectées

Aucune U1–U6 n'est totalement dépourvue de probe.

En revanche, deux dimensions transversales méritent d'être ajoutées lors de la prochaine révision :

```text
U7 — quelle règle / instruction exacte gouvernait chaque défaut allégué et chaque possibilité de régularisation ?

U8 — quel était exactement le bundle candidat à chaque instant critique du 11 septembre ?
```

NEW-RP-A et NEW-RP-B couvrent respectivement U7 et U8.

## 6. Probes sans rendement suffisant détectés

Aucun probe canonique n'est supprimé à ce stade.

Deux garde-fous ressortent néanmoins :

- ne pas répéter RP-SEN-01 ou RP-SEN-02 sans nouvelle information ;
- ne pas exécuter RP-SEN-05 / 06 de manière générique tant qu'un déclencheur ne permet pas de les rendre plus ciblés.

## 7. Vue réduite

```text
MAINTENANT
├── RP-SEN-01  WAIT response
├── RP-SEN-02  WAIT response
├── RP-SEN-03  internal preservation available
├── RP-SEN-14  continuous convergence
├── NEW-RP-A   passive legal/official-source research candidate
└── NEW-RP-B   candidate-side reconstruction candidate

SI RÉPONSE TECHNIQUE / REDIRECTION
├── RP-SEN-04  preservation if legally applicable
├── RP-SEN-05  infrastructure topology
├── RP-SEN-06  transaction receipts
└── RP-SEN-13  newly identified holder

APRÈS SCRUTIN / PROCLAMATION
├── RP-SEN-07  fix official clock
├── RP-SEN-08  inspect PV + annexes
├── RP-SEN-09  available constitutional litigation branch
└── RP-SEN-10  possible instruction only inside RP-SEN-09

APRÈS TRIGGER D'ACCÈS
├── RP-SEN-11  CADA
└── RP-SEN-12  CNIL

RECHERCHE PASSIVE COMPARATIVE
└── NEW-RP-C   comparable case law
```

## 8. Diff de carte produit par le batch

### Nouveaux probes candidats

- NEW-RP-A — corpus juridique / administratif officiel ;
- NEW-RP-B — reconstruction intégrale côté candidat ;
- NEW-RP-C — jurisprudence comparable.

### Probes supprimés

Aucun.

### Probes rendus plus étroits

- RP-SEN-05 : à déclencher sur topologie manquante ;
- RP-SEN-06 : à déclencher sur manque d'inventaire transactionnel ;
- RP-SEN-04 : seulement si les conditions de limitation deviennent matériellement pertinentes.

### Nouvelles inconnues candidates

- U7 — règle / instruction exacte et régularisation ;
- U8 — bundle candidat exact à chaque instant critique.

### Deadlines nouvellement mises en évidence

- risque de purge technique : date inconnue ;
- scrutin : 27 septembre 2026 ;
- fenêtre de dix jours de l'article 32 après l'élection ;
- horloge contentieuse à fixer à partir de la proclamation ;
- horloges CRPA/RGPD distinctes.

## 9. Condition de reprise

Le batch doit être rejoué, de manière incrémentale plutôt que depuis zéro, lorsqu'un des événements suivants survient :

- réponse du TA ;
- réponse de la préfecture ;
- découverte d'un détenteur ou système nouveau ;
- proclamation des résultats ;
- consultation des PV / annexes ;
- nouvelle pièce candidate ;
- décision humaine d'exécuter ou non une branche contentieuse ;
- expiration ou identification d'une deadline de conservation.
