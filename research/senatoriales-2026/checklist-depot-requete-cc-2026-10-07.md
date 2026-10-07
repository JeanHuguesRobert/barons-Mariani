---
title: "Checklist agile — dépôt de la requête au Conseil constitutionnel"
subtitle: "Sénatoriales Haute-Corse 2026 — contrôle pré-dépôt et points découverts en chemin"
author: "Jean Hugues Noël Robert"
date: "2026-10-07"
version: "0.51"
status: "active — living checklist"
language: "fr"
document_role: "operational"
document_kind: "legal-filing-checklist"
document_function: "pre-filing-control"
visibility: "public"
lifecycle_state: "active"
update_policy: "UP-DEFAULT-REVIEWED"
related:
  - "requete-conseil-constitutionnel.md"
  - "bordereau-pieces-requete-conseil-constitutionnel-v0.10.md"
  - "investigation/architecture-recours-cc-cedh-remedes-2026-10-05.md"
  - "qpc/qpc-a-candidature-senatoriale-2026.md"
  - "investigation/precedents_contentieux_et_couverture_medias_2017_2020_2024_2026.md"
  - "pre-filing-operational-plan-2026-10-07.md"
  - "protocole-constitution-requete-cc-2026-10-07.md"
  - "investigation/annexe-chronologie-detaillee-requete-cc-2026-10-07.md"
  - "investigation/gmail-audit-requete-2026-09-10-2026-10-07.md"
  - "matrice-canaux-materiels-depot-2026-10-07.md"
  - "note-depot-dematerialise-requete-cc-2026-10-07.md"
  - "investigation/annexe-documentation-double-lecture-2026-10-07.md"
  - "../reviews/audit-double-lecture-requete-v0.23-2026-10-07.md"
  - "../reviews/audit-intelligibilite-requete-v0.22-2026-10-07.md"
  - "filing-package-manifest-2026-10-07.md"
  - "fiche-remise-requete-cc-2026-10-07.md"
  - "../reviews/review_internal_requete_cc_motifs_rejet_2026-10-06.md"
  - "../autonomia/corse_laboratoire.md"
  - "../autonomia/amendement_effectivite_article_72-5.md"
---

# Checklist agile — dépôt de la requête au Conseil constitutionnel

## Règle d'usage

Cette checklist est **vivante** jusqu'au dépôt.

Tout point nouveau rencontré en cours de préparation qui peut matériellement changer la recevabilité, un moyen, une pièce, une conclusion, une voie parallèle, un délai, un remède ou la capacité de vérification doit être ajouté immédiatement ici, puis relié au document concerné.

Principe :

```text
NEW TRACE / NEW OBJECTION / NEW REMEDY / NEW DEADLINE
→ est-ce matériel pour le dépôt ?
→ oui : ajouter à la checklist
→ qualifier : MUST BEFORE FILING | SHOULD BEFORE FILING | POST-FILING
→ relier au document / pièce / source
→ fermer seulement après vérification
```

Ne pas attendre une "version finale" pour enregistrer un point utile.

### Standard probatoire — niveau maximal raisonnablement atteignable

Le dossier vise, pour chaque fait matériel important, le **plus haut niveau de preuve raisonnablement accessible**, avec une méthode proche de celle d'un enquêteur judiciaire particulièrement scrupuleux et conscient des risques de falsification, d'altération, d'usurpation et d'attaque informatique.

Conséquences pratiques :

- privilégier les **traces primaires et vérifiables** plutôt que les souvenirs, reconstructions ou affirmations non corroborées ;
- conserver l'**original natif** chaque fois qu'il existe, sans le remplacer par une capture ou une transcription ;
- calculer et conserver une **empreinte cryptographique forte (SHA-256 au minimum)** de tout fichier produit ou référencé ;
- documenter autant que possible la **provenance**, la date, le canal d'acquisition, la chaîne de conservation et toute transformation effectuée ;
- distinguer strictement **original / copie / photographie / capture / export / transcription / reconstruction** ;
- rechercher des **corroborations indépendantes** : métadonnées, journaux, accusés, traces serveur, historiques, pièces postales, chronologies, témoins ou systèmes tiers ;
- ne jamais présenter comme certain ce qui n'est qu'inféré ; qualifier explicitement les niveaux : **établi / fortement corroboré / plausible / non établi** ;
- pour les éléments numériques sensibles, raisonner comme si une contestation d'authenticité ou une cyberattaque devait être examinée : intégrité, horodatage, identité de la source, continuité de la conservation, cohérence inter-traces et possibilité d'une vérification indépendante ;
- lorsqu'une preuve plus forte est raisonnablement accessible, ne pas se satisfaire d'une preuve plus faible par commodité.

Ce standard n'impose pas une preuve impossible : il impose de pouvoir expliquer **pourquoi le niveau produit est le meilleur niveau raisonnablement atteignable** au moment du dépôt.

### Invariant d'autonomie du dossier et des pièces

Le dossier remis au Conseil doit être **autoportant**. Un juriste ne doit jamais avoir à connaître le Corpus, une conversation passée, un dépôt GitHub, un courriel non produit ou une convention interne pour comprendre une affirmation, une pièce ou un raisonnement.

Règle impérative :

```text
TOUTE CHOSE INVOQUÉE
→ doit être définie avant usage ;
→ son rôle dans le raisonnement doit être explicite ;
→ si elle est matériellement utile, elle doit être produite dans le dossier final ;
→ si l'incorporation est impraticable, fournir un accès Internet stable et vérifié,
   accompagné d'une empreinte forte (SHA-256 au minimum), d'une date de gel,
   d'une description suffisante et, si nécessaire, d'une transcription ou extraction lisible ;
→ aucune référence orpheline à "le Corpus", "la vidéo", "le mail", "le document",
   "l'annexe" ou à toute notion interne non définie n'est admise.
```

Pour **chaque pièce**, le contrôle pré-dépôt doit permettre de retrouver au minimum : **numéro**, **intitulé bref**, **date**, **origine/provenance**, **description matérielle**, **fait(s) qu'elle établit ou éclaire**, **place dans le raisonnement**, **fichier(s) exact(s)**, **mode de production** (embarqué / annexe / lien externe), **URL vérifiée le cas échéant**, **SHA-256**, **statut de vérification**, **lisibilité**, **éventuelle transcription**, **éventuelle occultation/minimisation**, et **présence effective dans le paquet remis**.

## Data plane / Control plane — application au dossier

Cette requête applique explicitement une séparation ancienne et canonique du Corpus.

### Data plane

Le **data plane** contient ce qui est effectivement porté, transformé ou remis :
- requête ;
- annexes ;
- chronologie ;
- bordereau ;
- pièces ;
- fichiers natifs ;
- preuves de réception ;
- versions gelées.

### Control plane

Le **control plane** gouverne la construction, la sélection, la vérification et le gel :
- présente checklist ;
- protocole de constitution ;
- audit Gmail ;
- revue adverse ;
- audit double lecture ;
- règles de provenance / SHA ;
- matrice des canaux de dépôt ;
- règles de redondance ;
- kill-switches.

### Invariant FractaCognition

Le control plane n'est pas une preuve du fond. Il réduit le risque de perdre, déformer, oublier ou surinterpréter les éléments du data plane.

~~~text
CONTROL PLANE
→ sélectionne / contraint / vérifie / route / gèle

DATA PLANE
→ contient / transporte / matérialise / prouve
~~~

Une règle de contrôle qui ne produit aucun effet observable sur le data plane est suspecte de bureaucratie. Une donnée importante du data plane qui échappe au control plane est un risque de dossier.


### Couplage obligatoire entre control plane et data plane

Le dossier applique la correspondance fonctionnelle suivante :

~~~text
DATA PLANE    ↔ cognition
CONTROL PLANE ↔ métacognition
~~~

Le parallèle n'est pas une identité de substance : une checklist, un diagnostic ou une mesure peuvent eux-mêmes devenir des données lorsqu'ils sont étudiés. Il porte sur la **fonction dans la boucle** : le data plane produit, transforme ou transporte ; le control plane oriente, contraint, vérifie et corrige.

Invariant opérationnel :

> **Toute action dans le data plane doit être guidée par les règles du control plane pertinent.**

Pour toute rédaction, révision, qualification, sélection de pièce, gel, transmission ou autre action portant sur la requête et ses annexes :

~~~text
ACTE SUR LE DATA PLANE
→ identifier la localité de l'acte
→ charger le control plane local applicable
→ identifier les règles pertinentes
→ agir
→ contrôler le résultat contre ces règles
→ élargir vers des règles plus générales seulement si nécessaire
~~~

Cette priorité est une règle d'**activation**, non une règle de supériorité normative : les contraintes héritées du Corpus continuent de s'appliquer. Le control plane local spécialise et rend saillantes les règles propres à l'acte concret ; il ne peut ni annuler une règle supérieure ni fabriquer une autorité absente.

**Test de défaillance :** si une règle locale existante aurait empêché une erreur effectivement produite mais n'a pas été consultée ou appliquée, traiter l'incident comme une **défaillance d'activation du control plane**, et non seulement comme une erreur ponctuelle du data plane. La correction doit alors porter à la fois sur l'objet erroné et sur la boucle de contrôle qui devait l'intercepter.

Références conceptuelles canoniques du Corpus : séparation control/data plane dans Inox/Cogentia et principe de localité / FractaCognition.



### Gate terminal de contrôle des sorties — validation avant émission

Le control plane s'applique aussi à la **sortie candidate** produite après l'analyse.

Il ne suffit pas de charger les règles avant d'agir : toute restitution humaine, toute écriture destinée au data plane et toute publication doivent être relues contre les invariants locaux immédiatement avant émission.

Boucle obligatoire :

~~~text
SORTIE CANDIDATE
→ identifier les règles locales applicables au rendu
→ vérifier les références documentaires
→ vérifier les libellés canoniques
→ vérifier les qualifications probatoires et juridiques
→ vérifier les bornes / incertitudes requises
→ vérifier l'absence de marqueurs internes interdits
→ corriger
→ seulement ensuite émettre / écrire / publier
~~~

### Contrôle terminal des références de pièces

Toute occurrence d'un identifiant documentaire stable doit être contrôlée avant émission :

~~~text
P-xx / P-xx.a / PREF-xx
→ le numéro est-il présent ?
→ le libellé intelligible est-il présent ?
→ le libellé correspond-il au meilleur libellé canonique courant ?
→ la référence reste-t-elle compréhensible hors contexte immédiat ?
~~~

Règle impérative :

> **Aucune référence de pièce ne doit sortir du système sous la forme d'un identifiant nu lorsqu'un libellé canonique est disponible.**

Exemples :

~~~text
À ÉVITER :
P-46

À ÉCRIRE :
P-46 — Registre exhaustif des courriels Préfecture / Tribunal administratif
~~~

Cette exigence vaut pour :
- la requête ;
- les annexes ;
- le bordereau ;
- les revues ;
- les comptes rendus de contrôle ;
- les réponses conversationnelles destinées à Jean Hugues Robert ;
- toute autre explication humaine produite à partir du dossier.

### Défaillance d'activation au stade de sortie

Si une règle locale correctement chargée aurait empêché une erreur mais que l'erreur apparaît malgré tout dans une restitution, classer l'incident comme :

> **défaillance d'activation du control plane au stade de sortie**

La correction doit alors porter sur deux niveaux :

1. **objet erroné** — corriger immédiatement la formulation ou la référence ;
2. **boucle de contrôle** — renforcer le gate terminal afin que le même type d'erreur soit détecté avant émission.

Cas canonique du 7 octobre 2026 :
- la règle « numéro + libellé intelligible » était déjà présente ;
- une analyse mécanique a produit l'identifiant `P-46` ;
- cet identifiant a été restitué sans résolution vers son libellé canonique ;
- l'incident est donc un défaut d'activation terminale, non une absence de règle.

Test final avant émission :

> **Si cette sortie était l'unique page lue par un tiers, comprendrait-il chaque référence documentaire sans devoir connaître le code interne du dossier ?**

Si la réponse est non, la sortie ne doit pas être émise en l'état.


### Gel du paquet PDF — builds éphémères, artefact unique, Release immuable

Le PDF d'assemblage final suit un protocole distinct de la rédaction des sources.

~~~text
SOURCES / CONTRAT
→ versionnés dans Git

BUILDS PDF INTERMÉDIAIRES
→ locaux / temporaires
→ jamais commités

CANDIDAT VALIDÉ
→ SHA-256 local
→ GitHub Release en brouillon
→ upload
→ retéléchargement
→ comparaison SHA-256

PUBLICATION
→ acte distinct
→ Release immuable
→ URL définitive
~~~

Règles impératives :

- aucun build intermédiaire ne doit polluer l'historique Git ;
- le contrat d'assemblage doit nommer chaque composant et son ordre ;
- toute pièce requise sans fichier matérialisé bloque le build final ;
- `freeze` et `publish` sont des opérations distinctes ;
- la création de la Release en brouillon ne vaut pas dépôt ;
- la publication de la Release est un acte externe terminal et doit rester explicitement autorisée ;
- l'empreinte SHA-256 du fichier local, du fichier retéléchargé depuis la Release en brouillon et du fichier public après publication doit être identique ;
- le lien communiqué doit désigner l'asset de la Release gelée, non une branche mutable telle que `main`.

Contrat courant : `research/senatoriales-2026/filing-package-2026-10-07.yml`.

### Règle de style à deux vitesses

**Grand public :**
~~~text
lecteur intelligent
+ attention rare
+ temps rare
→ phrases courtes
→ une idée par phrase
→ mots concrets
→ métaphores parlantes
→ conclusion explicite
~~~

**Expert :**
~~~text
juriste junior
+ aucune connaissance préalable du dossier
→ règle
→ source
→ application
→ objection
→ réponse
→ conséquence
~~~

**Talleyrand :**
~~~text
implicite utile
→ expliciter
ambiguïté plausible
→ fermer
enchaînement logique
→ écrire
~~~

Une section qui ne peut être comprise qu'en « lisant entre les lignes » échoue au contrôle.

### Autoportance historique — troisième horizon de lecture

La double lecture **grand public / expert** n'est pas seulement une technique de vulgarisation et de contrôle juridique. Le document doit aussi rester intelligible comme **trace historique autonome de la Corse de 2026**.

Le lecteur futur ne doit pas avoir besoin de connaître le Corpus, les conversations de travail, les acteurs de 2026, les débats alors contemporains sur l'autonomie, ni les usages administratifs implicites pour comprendre :
- ce qui s'est passé ;
- pourquoi cela comptait à ce moment de l'histoire de la Corse ;
- quelles capacités, contraintes et voies de recours existaient ;
- quelles démarches ont été entreprises ;
- quelles réponses institutionnelles sont documentées ;
- quelles questions demeuraient sans réponse suffisante ou restaient à établir au moment du dépôt.

Règle :

~~~text
PORTÉE CONTENTIEUSE
≠ VALEUR D'INTELLIGIBILITÉ
≠ VALEUR HISTORIQUE
≠ DÉCISION MATÉRIELLE DE PRODUCTION
~~~

Une pièce peut être non déterminante juridiquement à elle seule et néanmoins structurante pour comprendre la séquence. Inversement, une pièce juridiquement importante n'a pas besoin d'être chargée artificiellement d'une signification historique qu'elle ne porte pas.

Pour chaque développement et chaque pièce, tester trois lecteurs :

1. **lecteur contemporain grand public** — comprend-il sans jargon ni contexte implicite ?
2. **lecteur expert / juridiction** — peut-il contrôler la règle, le fait, la preuve, l'objection et la conséquence ?
3. **lecteur historique futur** — pourrait-il reconstruire le sens de la séquence sans accès au Corpus ni connaissance préalable de la Corse politique de 2026 ?

Cette troisième exigence n'autorise ni digression gratuite, ni emphase historique, ni surqualification. Elle impose au contraire de conserver le **contexte matériel nécessaire**, de dater les faits, d'identifier les acteurs et institutions, d'expliciter les enjeux contemporains et de séparer strictement faits établis, interprétations, hypothèses et mémoire du requérant.

Le but n'est pas de déclarer dans la requête qu'elle « fera l'Histoire ». Le but est de l'écrire de telle sorte qu'elle puisse, si elle devient une source historique, être comprise et vérifiée sans reconstruction extérieure inutile.


### Double horizon contentieux — Conseil constitutionnel + préparation CEDH

Le travail ne poursuit pas un seul objectif juridictionnel.

Il doit simultanément :

1. **contester l'élection sénatoriale du 27 septembre 2026 devant le Conseil constitutionnel**, dans le cadre, les délais, l'office et les remèdes propres au contentieux électoral parlementaire ;
2. **préserver et préparer dès maintenant un éventuel recours ultérieur devant la Cour européenne des droits de l'homme (CEDH)**, sans attendre l'issue nationale pour commencer à documenter les griefs, les répétitions alléguées, les diligences, les réponses institutionnelles, les préjudices et l'épuisement des voies de recours pertinentes.

Invariant :

~~~text
DOSSIER CONSEIL CONSTITUTIONNEL
≠ DOSSIER CEDH

mais

PREUVE / CHRONOLOGIE / TRAÇABILITÉ / GRIEFS PRÉSERVÉS
→ peuvent alimenter les deux
~~~

Le control plane doit donc empêcher deux erreurs symétriques :

- **polluer la requête électorale nationale** avec des développements CEDH qui n'y servent aucun moyen recevable ;
- **perdre aujourd'hui une trace utile à Strasbourg** au motif qu'elle n'est pas décisive pour le Conseil constitutionnel.

Pour chaque élément matériel, poser aussi la question suivante :

> **Cet élément est-il utile seulement au contentieux électoral immédiat, seulement à la préservation d'un futur grief CEDH, aux deux, ou à aucun des deux ?**

Le futur dossier CEDH devra être construit séparément, avec ses propres contrôles de recevabilité, qualité de victime, épuisement des recours internes, délai, griefs conventionnels, causalité et réparation.

La continuité alléguée d'un traitement médiatique défavorable depuis **2017**, y compris lorsqu'elle concerne des médias de service public, doit être documentée comme une **hypothèse longitudinale à tester** et non comme une conclusion acquise. Le dossier devra distinguer, année par année et média par média : information disponible, traitement observé, comparateurs, démarches entreprises, réponses reçues, effet allégué sur le scrutin, effet réputationnel, préjudice moral allégué et preuve disponible.

Les demandes éventuelles de réparation constituent un sous-dossier distinct : leur fondement, leur recevabilité, leur causalité et leur quantification devront être instruits séparément. Toute intention déclarée d'affecter une éventuelle somme à un fonds ou à une structure d'intérêt général ne modifie ni l'existence juridique du préjudice personnel allégué ni les conditions d'octroi d'une satisfaction équitable ; elle doit donc rester séparée de la démonstration du dommage.

### Règle de présentation des résultats — collège électoral d'abord

Dans un scrutin sénatorial où la participation des membres du collège électoral est juridiquement contrainte par l'article **L.318 du code électoral**, la mesure la plus immédiatement intelligible d'un résultat ou d'un volume électoral est sa part du **collège électoral total**, et non d'abord son nombre brut de voix.

Règle générale de rédaction :

~~~text
POURCENTAGE DU COLLÈGE ÉLECTORAL
→ d'abord

VALEUR ABSOLUE
→ ensuite, entre parenthèses ou dans la même proposition

AUTRE DÉNOMINATEUR UTILE
→ seulement ensuite, en l'identifiant explicitement
~~~

Exemples attendus pour la Haute-Corse 2026 :

- **71,8 % du collège (442 voix sur 616)** pour M. Parigi ;
- **14,3 % du collège (88 voix sur 616)** pour M. Battini ;
- **5,8 % du collège (36 bulletins sur 616)** pour les blancs ;
- **6,5 % du collège (40 bulletins sur 616)** pour les nuls ;
- **12,3 % du collège (76 bulletins sur 616)** pour blancs + nuls ;
- **86,0 % du collège (530 suffrages sur 616)** pour les exprimés ;
- **98,4 % du collège (606 votants sur 616)** pour la participation.

Cette règle vaut dans la requête, les annexes explicatives, le bordereau lorsqu'il résume un résultat, l'inventaire probatoire, les comparaisons longitudinales et les formulations grand public.

**Exception de précision juridique :** lorsqu'un texte de droit définit lui-même un seuil sur un autre dénominateur — par exemple la majorité absolue des **suffrages exprimés** — ce dénominateur légal doit rester explicite et ne doit jamais être remplacé par le pourcentage du collège. La présentation doit alors distinguer les deux mesures : **règle légale sur les exprimés**, puis traduction éventuelle en part du collège pour l'intelligibilité comparative.

Motif : dans ce scrutin, l'article L.318 sanctionne le membre du collège électoral qui, sans cause légitime, ne prend pas part au scrutin. La participation observée doit donc être lue avec cette contrainte institutionnelle en tête. Cette règle de présentation ne permet aucune inférence sur le choix individuel d'un grand électeur.


### Règle de précédence sémantique — aucun référent ne doit « tomber du ciel »

La requête doit être lisible **strictement dans l'ordre où elle est écrite**.

Un lecteur ne doit jamais avoir besoin :
- de connaître un élément qui n'a pas encore été introduit ;
- d'aller chercher plus loin dans le document pour comprendre une phrase présente ;
- de connaître le Corpus, une conversation, un article de presse ou une analyse externe non encore exposée ;
- d'inférer à quoi renvoient des expressions comme « ce soutien », « cette base », « cette offre », « ces éléments », « ce contexte », « cette séquence », « cette pièce » ou « ce contraste ».

Invariant :

~~~text
RÉFÉRENT
→ introduit avant usage

FAIT
→ exposé avant conséquence

COMPARATEUR
→ identifié avant comparaison

CONCEPT
→ défini avant raccourci

PRONOM / DÉMONSTRATIF
→ antécédent explicite, proche et non ambigu
~~~

Une phrase qui dépend d'un élément correctement expliqué seulement plus loin est considérée comme un **défaut de structure**, même si l'information existe ailleurs dans le document.

Test obligatoire pour chaque paragraphe :

> **Un lecteur qui s'arrête exactement ici possède-t-il déjà toutes les informations nécessaires pour comprendre cette phrase comme nous voulons qu'elle soit comprise ?**

Si la réponse est non, il faut soit introduire l'élément plus tôt, soit reformuler, soit déplacer le passage.

Cette règle vaut particulièrement pour :
- les soutiens politiques ou institutionnels ;
- les comparateurs électoraux ou médiatiques ;
- les pièces citées par numéro ;
- les expressions abrégées (« offre absente », « base institutionnelle », « chaîne de transmission », etc.) ;
- les références à un événement antérieur dont la chronologie n'a pas encore été racontée ;
- les raisonnements causaux dont une prémisse est exposée seulement dans une section ultérieure.


### Règle de langue — français d'abord, anglais technique traduit immédiatement

La langue de la République étant le français, la requête, ses annexes et ses documents de contrôle doivent être rédigés en français.

Lorsqu'un terme anglais est conservé parce qu'il constitue un marqueur technique utile, une convention du Corpus, un statut machine ou un terme difficilement substituable sans perte de précision, sa traduction française doit apparaître **immédiatement** à sa première occurrence utile et, si le contexte l'exige, être répétée lorsque le lecteur pourrait ne plus se souvenir de la convention.

Forme attendue :

~~~text
UNKNOWN (inconnu)
working draft (brouillon de travail)
control plane (plan de contrôle)
data plane (plan de données)
hash (empreinte cryptographique)
bundle (ensemble de fichiers / paquet documentaire)
~~~

Règles :
- ne pas supprimer automatiquement le terme anglais lorsqu'il porte une valeur technique ou une convention stable ;
- ne jamais laisser un terme anglais technique essentiel sans traduction française immédiate ;
- préférer ensuite le français dans le corps du raisonnement, sauf lorsqu'il faut citer exactement un statut, un nom de champ, un terme informatique, un intitulé de fichier ou une convention machine ;
- pour les citations exactes en anglais, fournir une traduction française adjacente si leur compréhension est nécessaire au raisonnement ;
- ne pas transformer cette règle en surcharge : la traduction doit être courte, exacte et située au point d'usage.

Test de lecture :

> **Un lecteur francophone qui ne connaît pas le jargon technique peut-il comprendre la phrase sans devoir deviner le sens du terme anglais ?**


### Règle de séparation méthode / résultat — la requête ne décrit pas son moteur interne

Le **control plane (plan de contrôle)** contient les méthodes, principes, audits, checklists, heuristiques, noms internes et règles de fabrication du dossier.

La **requête** ne doit pas expliquer au Conseil comment elle a été produite lorsque cette explication n'est pas juridiquement ou factuellement nécessaire.

Invariant :

~~~text
MÉTHODE INTERNE
→ control plane

RÉSULTAT VÉRIFIABLE
→ requête
~~~

Exemples d'éléments à maintenir hors du corps de la requête sauf nécessité démontrée :
- « Talleyrand appliqué » ;
- références à FractaCognition ;
- descriptions de nos protocoles de revue ou de nos audits internes ;
- explications sur la manière dont le texte évite une erreur ;
- commentaires tels que « le document ne demande jamais au lecteur de… » ;
- noms internes de passes, heuristiques ou mécanismes de production.

La requête doit **incarner** ces règles sans les commenter.

Exemple :

~~~text
À ÉVITER :
« Talleyrand appliqué : lorsqu'une heure n'est pas établie, le document le dit. »

À ÉCRIRE :
« L'heure de réception par le serveur de l'État n'est pas établie. »
~~~

Exception : une méthode peut être exposée si elle constitue elle-même un fait matériel, une méthode d'analyse nécessaire à la vérification d'une pièce, ou si son explicitation est indispensable au contradictoire. Dans ce cas, elle doit être présentée comme méthode probatoire concrète, non comme commentaire sur notre processus de rédaction.

Test obligatoire :

> **Cette phrase apprend-elle quelque chose sur l'affaire, la preuve ou le droit, ou seulement sur la façon dont nous avons construit le document ?**

Si elle ne décrit que la fabrication du document, elle appartient au control plane et doit être retirée de la requête.


### Règle d'atemporalité rédactionnelle — ne pas raconter l'évolution de notre connaissance

La requête doit exposer **l'état utile du dossier**, non l'histoire de sa préparation.

Les marqueurs tels que **« désormais »**, **« maintenant »**, **« à ce stade »**, **« dorénavant »**, **« jusqu'ici »**, **« actuellement »** ou **« à présent »** sont à supprimer lorsqu'ils décrivent seulement l'évolution de notre travail, la découverte progressive d'une pièce ou la maturation d'une analyse.

Invariant :

~~~text
ÉVOLUTION DE NOTRE TRAVAIL
→ control plane

ÉTAT DU DOSSIER AU MOMENT DU DÉPÔT
→ requête
~~~

Exemple :

~~~text
À ÉVITER :
« Inventaire initial désormais établi par P-14 »

À ÉCRIRE :
« P-14 établit l'inventaire initial des seize pièces. »
~~~

Ces marqueurs temporels restent admissibles uniquement lorsqu'ils décrivent **un fait matériel de l'affaire** ou une situation juridiquement pertinente au moment considéré.

Test :

> **Le mot temporel décrit-il un événement du dossier, ou seulement le fait que nous savons aujourd'hui quelque chose que nous ne savions pas hier ?**

Dans le second cas, il doit être retiré de la requête.


### Règle de force argumentative — ne pas plaider contre soi-même

La requête doit exposer avec netteté les faits, les règles, les analogies et les moyens soutenus par le requérant. Elle ne doit pas multiplier les formules qui en diminuent spontanément la portée avant même que le juge ne les apprécie.

Il faut distinguer deux choses :
- les limites factuelles ou juridiques réellement nécessaires à l'exactitude du dossier, qui doivent être conservées ;
- les précautions rhétoriques redondantes, qui reviennent à faire nous-mêmes le travail d'objection, de minoration ou de rejet.

La seconde catégorie doit disparaître du corps de la requête.

Règle pratique : dire ce que la pièce établit, ce que le texte permet de soutenir et quelle conséquence est demandée. L'appréciation finale de la force du moyen appartient au juge.

Les formulations telles que « au mieux », « seulement », « au minimum », « n'est pas automatiquement transposable », « volontairement borné », « infiniment subsidiaire » ou toute autre précaution analogue doivent être conservées uniquement lorsqu'elles correspondent à une véritable limite juridique, probatoire ou procédurale indispensable.

Le contrôle critique ne disparaît pas. Il est déplacé vers le plan de contrôle : lorsqu'une affirmation paraît fragile, excessive ou insuffisamment établie, elle doit être signalée au requérant pour décision, et non affaiblie automatiquement dans le texte au nom d'une protection paternaliste.

Le style recherché est ferme, exact et audacieux. Il ne doit être ni téméraire ni timoré.


### Règle de français idiomatique — pas de calques mécaniques

Le français de la requête doit être naturel, idiomatique et immédiatement compréhensible.

Il est interdit de traduire littéralement une expression anglaise, informatique, administrative ou conceptuelle si le résultat produit en français une formule étrange, artificielle ou obscure.

Règle pratique :
- partir du sens à transmettre ;
- reformuler dans un français courant ou juridique naturel ;
- accepter une phrase plus longue si elle est plus claire ;
- préférer une image française évidente à un calque technique ;
- supprimer toute métaphore qui demande au lecteur de deviner ce qu'elle signifie.

Exemple :

À éviter :
« L'enjeu est comparable à une chaîne de colis. »

À écrire :
« Il faut pouvoir suivre le trajet des documents : ce qui a été reçu, transmis et finalement versé au dossier. »

Cette règle complète la traduction immédiate des termes anglais : traduire n'est pas suffisant si la traduction reste artificielle.

Test obligatoire :

> Une personne cultivée qui ne connaît ni l'informatique ni notre vocabulaire interne comprend-elle immédiatement la phrase, sans devoir reconstruire l'expression d'origine ?

Si la réponse est non, il faut réécrire.



Exemple supplémentaire de calque à proscrire :

À éviter :
« D'autres questions sont restées ouvertes. »

Préférer selon le sens exact :
- « D'autres questions sont restées sans réponse suffisante. »
- « D'autres questions n'ont reçu qu'une réponse partielle. »
- « Certaines questions demeurent non résolues. »

Le choix dépend du statut probatoire réel de la réponse.

### Règle de textualité souveraine et de qualité littéraire

La requête est un texte juridique narratif. Sa compréhension ne doit dépendre d'aucun bloc de code, symbole logique, flèche, tableau, couleur, police ou autre artifice graphique.

La mise en forme peut aider à lire ; elle ne doit jamais porter le sens. Le document doit rester sémantiquement complet s'il est dactylographié avec seulement du texte, des titres, des sous-titres, des paragraphes, une numérotation simple et un sommaire.

En conséquence :
- supprimer les blocs de code du corps de la requête ;
- remplacer les symboles comme « ≠ » et « → » par des phrases françaises ;
- éviter les tableaux lorsque du texte continu raconte mieux l'affaire ;
- ne jamais faire dépendre une distinction juridique du seul gras ou de la disposition visuelle ;
- conserver une hiérarchie claire de titres et sous-titres ;
- ajouter un sommaire au document long.

Le test de contrôle est celui de la machine à écrire : si toute la mise en forme disparaît, le lecteur doit comprendre exactement la même chose.

La requête doit en outre être fluide, narrative et agréable à lire. Elle ne doit pas ressembler à un cahier des charges, une spécification technique ou une checklist. Le lecteur doit pouvoir suivre naturellement les faits, le temps, les décisions et leurs conséquences ; le juriste doit pouvoir vérifier les règles, les sources, les pièces, les objections et les conclusions.

Les successions mécaniques de labels comme « FAIT / PREUVE / RÈGLE / ÉCART / INCIDENCE » sont à transformer en prose lorsqu'elles cassent la lecture. La double lecture grand public / expert est une qualité de l'écriture, non l'obligation de juxtaposer partout deux blocs rigides.

Toute réécriture de style conserve strictement les faits, les qualifications, les réserves probatoires réellement nécessaires, les incertitudes, les pièces et les conclusions.

### Règle de qualification des réponses institutionnelles

Toute analyse d'une demande adressée à une institution distingue au minimum cinq états :

1. réponse absente ;
2. réponse non retrouvée ;
3. réponse partielle ;
4. réponse hors sujet ;
5. information explicitement déclarée indisponible.

Ces états ne sont pas interchangeables.

La formulation retenue doit correspondre exactement à la trace disponible. Une recherche infructueuse permet d'écrire « réponse non retrouvée », pas « aucune réponse n'existe ». Une réponse qui traite un autre objet est une réponse hors sujet, pas une absence de réponse.

Cette taxonomie vaut pour P1–P18, D1–D10, P-45 et toute autre séquence de demandes institutionnelles.

### Traçabilité des Actes — règle transversale

La Traçabilité des Actes constitue une grille documentaire utile au présent contentieux.

Elle repose sur une idée simple : lorsqu'un acte public produit ou prépare un effet, il doit être possible, dans la mesure où des traces existent ou devraient normalement exister, de reconstituer ce qui a été fait, par qui, quand, sur quelle base et avec quelle transmission.

Dans la requête, cette notion ne doit pas devenir une théorie abstraite. Elle sert à éclairer des questions concrètes : réception d'un courriel, classement ou routage, transmission au Tribunal administratif, production complémentaire éventuelle, accès effectif de la formation de jugement à une pièce, création et validation d'un acte, conservation des traces et modalités de remise du recours lui-même.

La traçabilité protège les deux côtés du contradictoire. Elle peut établir une faute ou une lacune, mais elle peut tout autant établir qu'une administration a correctement reçu, routé, transmis ou traité un élément et fermer une contestation.

Une absence de trace ou de réponse ne doit jamais être transformée automatiquement en intention. Elle peut toutefois réduire objectivement la capacité à vérifier contradictoirement ce qui a été fait et, lorsqu'un recours est enfermé dans un délai bref, affecter son effectivité.

La note factuelle relative à l'évolution des réponses institutionnelles doit être reliée aux demandes P1–P18, D1–D10, à P-45 et aux pièces primaires correspondantes.


### Règle de redondance sémantique — tableaux et schémas hors du corps

Le corps de la requête doit rester intégralement compréhensible en texte continu.

Les tableaux, schémas, chronologies graphiques et autres présentations visuelles ne doivent jamais contenir une information, une nuance, une qualification ou une relation logique qui n'existe pas déjà dans le texte.

Leur fonction est exclusivement de rendre une information déjà exposée plus rapide à parcourir, comparer ou vérifier.

Règle générale :

1. le corps de la requête expose d'abord l'information en français continu ;
2. lorsqu'une présentation tabulaire ou graphique améliore la lecture, le texte renvoie vers une annexe ;
3. l'annexe peut reprendre la même matière sous forme de tableau, schéma ou autre représentation synthétique ;
4. supprimer le tableau ou le schéma ne doit provoquer aucune perte sémantique.

La règle vaut pour :
- tableaux de faits ;
- tableaux de pièces ;
- comparaisons ;
- chronologies ;
- matrices de demandes et réponses ;
- schémas de circulation documentaire ;
- représentations causales ou procédurales ;
- toute autre visualisation.

Un tableau n'est donc jamais une seconde source de contenu. C'est une autre vue du même contenu.

Test obligatoire :

> Si l'annexe tabulaire ou le schéma disparaît, le lecteur du seul corps de la requête dispose-t-il encore de toutes les informations nécessaires, avec la même portée et les mêmes réserves ?

Si la réponse est non, le texte principal doit être complété avant de renvoyer à l'annexe.

Réciproquement, l'annexe ne doit pas ajouter subrepticement une affirmation nouvelle sous prétexte de synthèse. Toute information nouvelle doit d'abord être introduite et qualifiée dans le texte de référence.


### Règle de référence canonique des pièces — numéro et libellé indissociables

Toute pièce citée dans la requête doit être identifiable immédiatement sans obliger le lecteur à consulter le bordereau.

La référence canonique associe systématiquement :
- le numéro de la pièce ;
- son libellé intelligible.

Cette règle vaut dans les deux sens.

À éviter :
- « P-28 » seul ;
- « la proposition de consultation des pièces électorales » sans numéro, lorsqu'il s'agit de la pièce identifiée au bordereau.

À écrire :
- « P-28 — proposition de consultation des pièces électorales » ;
- ou, dans une phrase, « la proposition de consultation des pièces électorales (P-28) ».

Le même principe s'applique aux sous-pièces PREF-xx et à toute autre numérotation documentaire stable.

Le libellé doit être suffisamment descriptif pour qu'un lecteur comprenne immédiatement de quel document il s'agit. Il ne doit pas se réduire à une catégorie vague comme « courriel », « document » ou « annexe » si un intitulé plus précis existe.

Une première occurrence peut employer le libellé complet. Les occurrences suivantes peuvent être légèrement raccourcies, mais doivent conserver à la fois le numéro et un libellé reconnaissable.

Test obligatoire :

> Si le numéro disparaissait, le lecteur saurait-il encore de quelle pièce il s'agit ? Si le libellé disparaissait, le lecteur saurait-il encore ce que contient la pièce ?

Si l'une des réponses est non, la référence est insuffisante.


### Règle d'amélioration continue des libellés de pièces

Le numéro d'une pièce est un identifiant stable. Son libellé, en revanche, peut être amélioré lorsqu'une formulation plus claire facilite la compréhension du dossier.

Il ne faut donc pas conserver un intitulé médiocre par inertie.

Lorsqu'un libellé paraît :
- trop vague ;
- trop technique ;
- trop long sans nécessité ;
- ambigu ;
- difficile à mémoriser ;
- insuffisamment descriptif de la fonction réelle de la pièce ;

il doit être reformulé dans un français naturel, précis et immédiatement intelligible.

L'amélioration du libellé ne doit modifier ni l'identité matérielle de la pièce, ni son numéro, ni sa portée probatoire.

Toute modification d'un libellé doit être propagée de manière cohérente dans l'ensemble du dossier :
- requête ;
- bordereau de pièces ;
- inventaire probatoire ;
- annexes ;
- chronologies ;
- notes d'enquête ;
- sous-inventaires ;
- renvois internes.

Le couple canonique est donc :

**numéro stable + meilleur libellé disponible à l'état courant du dossier.**

Avant toute propagation, vérifier qu'aucun changement de libellé ne crée une ambiguïté avec une autre pièce ou ne donne à la pièce une portée qu'elle n'a pas.

L'objectif n'est pas la stabilité lexicale pour elle-même, mais l'intelligibilité du dossier.


### Principe général d'agilité — ne pas rester prisonnier du passé

Le dossier, le Corpus et leurs conventions sont des objets vivants.

Une décision antérieure, un libellé, une structure, une qualification, un classement, une méthode ou une convention n'acquiert pas de valeur du seul fait qu'elle existe déjà.

Lorsqu'un changement améliore de manière justifiée :
- l'exactitude ;
- l'intelligibilité ;
- la cohérence ;
- la force probatoire ;
- la qualité juridique ;
- la simplicité ;
- la maintenabilité ;
- ou l'effectivité du dossier ;

ce changement doit pouvoir être effectué.

Le coût de propagation n'est pas, à lui seul, une raison suffisante pour conserver une solution devenue moins bonne.

Règle pratique :

**conserver ce qui reste juste ; corriger ce qui ne l'est plus ; améliorer ce qui peut l'être ; propager le changement partout où il produit des conséquences.**

L'agilité ne signifie pas réécrire silencieusement le passé.

Tout changement substantiel doit :
- préserver, lorsqu'il est utile, l'historique permettant de comprendre l'évolution ;
- éviter de modifier rétroactivement le sens d'une pièce ou d'un fait ancien ;
- conserver les numéros et identifiants stables lorsqu'ils jouent un rôle de référence ;
- propager les conséquences dans les documents dépendants ;
- faire apparaître clairement, lorsque c'est matériel, ce qui a changé et pourquoi.

Le test n'est donc jamais : « est-ce ainsi que nous faisions auparavant ? »

Le test est :

> **À l'état actuel des faits, du droit et du dossier, cette solution reste-t-elle la meilleure ?**

Si la réponse est non, le passé ne doit pas empêcher l'amélioration présente.


### Règle d'étanchéité entre fabrication et texte juridictionnel

La requête ne doit pas exposer son histoire de fabrication.

Les numéros de version internes, noms de passes, mentions de brouillons antérieurs, indications de migration, commentaires de consolidation et autres traces du processus éditorial appartiennent au plan de contrôle et à l'historique Git, pas au texte soumis au juge.

À proscrire dans le corps de la requête :
- « v0.5 », « v0.26 » ou toute autre référence à une version interne ;
- « dans la version précédente » ;
- « ce passage a été corrigé » ;
- « la présente version hiérarchise » ;
- toute phrase qui oblige le lecteur à connaître l'histoire de rédaction pour comprendre le texte.

La requête doit toujours présenter directement l'état actuel du raisonnement.

Exception : une version d'une pièce externe ou d'un document source peut être mentionnée lorsqu'elle constitue elle-même un fait utile, à condition d'expliquer clairement ce dont il s'agit.

Test obligatoire :

> Un lecteur qui ne connaît ni GitHub ni l'historique de rédaction comprend-il la phrase sans information extérieure ?

Si la réponse est non, la trace de fabrication doit être retirée du corps.


### Règle d'ergonomie — toujours fournir un lien directement cliquable

Lorsqu'un document, une annexe, une requête, un bordereau, une note ou toute autre ressource GitHub est proposée à la lecture de Jean Hugues Noël Robert, la réponse doit fournir directement son **URL complète et cliquable**.

Un chemin de dépôt, un nom de fichier, un numéro de version, un SHA de commit ou une référence interne ne suffit pas lorsqu'il s'agit d'inviter à ouvrir le document.

À éviter :

`research/senatoriales-2026/requete-conseil-constitutionnel.md`

À fournir :

`https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/senatoriales-2026/requete-conseil-constitutionnel.md`

Le chemin interne peut être ajouté pour la traçabilité, mais jamais à la place du lien utilisable.

Cette règle vaut aussi dans les échanges conversationnels avec l'auteur : ne pas lui imposer de reconstruire une URL à partir d'informations techniques déjà connues du système.


### Référence stable de la requête

La requête possède désormais un nom de fichier canonique sans numéro de version :

`research/senatoriales-2026/requete-conseil-constitutionnel.md`

Ce chemin est la référence stable à utiliser dans les échanges, les annexes, les notes de stratégie et les documents dépendants.

Les numéros de version peuvent continuer à exister dans le frontmatter, l'historique Git ou des instantanés d'archive, mais ils ne doivent plus obliger le lecteur ou les documents liés à changer de lien à chaque révision.

Règle générale : **l'objet vivant conserve une adresse stable ; son histoire est portée par le versionnage et Git, non par le nom de fichier courant.**

### Nommage intelligible des QPC

Les désignations « QPC A » et « QPC B » sont abandonnées.

Les deux pistes constitutionnelles sont désormais nommées par leur objet :

- **QPC — article L.303 : garanties juridictionnelles, office du juge électoral et séparation des pouvoirs** ;
- **QPC — article L.299 : formalisme de candidature et empêchement fonctionnel du remplaçant**.

Une QPC doit toujours être désignée par un intitulé permettant de comprendre immédiatement le texte visé et la question constitutionnelle étudiée. Les lettres, sigles internes ou numéros de travail ne peuvent servir seuls de nom public.


### QPC dans le paquet final adressé au Conseil constitutionnel

Les deux QPC ne doivent pas rester des pistes de recherche extérieures à la requête.

Le paquet effectivement adressé au Conseil constitutionnel doit comprendre :

- la requête électorale stable `requete-conseil-constitutionnel.md`, qui **soulève expressément** les deux QPC et en expose l'objet ;
- un mémoire distinct et motivé **« QPC — article L.303 : garanties juridictionnelles, office du juge électoral et séparation des pouvoirs »** ;
- un mémoire distinct et motivé **« QPC — article L.299 : formalisme de candidature et empêchement fonctionnel du remplaçant »**.

Les deux mémoires QPC sont des éléments constitutifs du dépôt final, non de simples annexes facultatives ou notes de recherche.

Avant figement du paquet, vérifier pour chacune :
1. disposition législative exacte ;
2. applicabilité au litige ;
3. droit ou liberté constitutionnellement garanti invoqué ;
4. état de la jurisprudence constitutionnelle antérieure ;
5. caractère nouveau ou sérieux ;
6. rédaction autonome, intelligible et motivée ;
7. présence effective dans le paquet remis au Conseil.


### Préservation CEDH — épuisement dès la requête nationale

La requête au Conseil constitutionnel poursuit également un objectif de **préservation conventionnelle**.

Règle impérative : tout grief que le requérant pourrait vouloir porter ultérieurement devant la Cour européenne des droits de l'homme doit être soumis au niveau national **au moins en substance**, dans les formes et délais internes, afin de laisser à l'État français la possibilité de le prévenir ou de le redresser.

Les griefs conventionnels à préserver dans la requête sont au minimum :

- **article 3 du Protocole n° 1** : droit concret et effectif de se porter candidat aux élections du corps législatif ; légalité, prévisibilité, proportionnalité et garanties contre l'arbitraire ;
- **article 13 combiné avec l'article 3 du Protocole n° 1** : recours effectivement capable d'examiner et de redresser l'atteinte électorale ;
- **article 14 combiné avec l'article 3 du Protocole n° 1** : volet handicap et désavantage particulier, sous réserve de la qualité personnelle de victime.

Ne pas utiliser **l'article 6 CEDH** comme fondement principal du contentieux électoral : le droit de se porter candidat est un droit politique, non un droit civil au sens de l'article 6 § 1.

Après toute réécriture de la requête, vérifier que la substance de ces trois griefs n'a pas disparu.

La matrice de contrôle dédiée est :
`research/senatoriales-2026/investigation/preservation-cedh-2026-10-07.md`.

### Délai et forme d'une future saisine CEDH

Après chaque décision nationale définitive pertinente :

1. conserver le texte intégral, sa date, son mode de notification et la preuve correspondante ;
2. ouvrir immédiatement un compteur conservatoire de **quatre mois** ;
3. identifier grief par grief la décision nationale finale pertinente ;
4. préparer le formulaire officiel complet prévu par l'article 47 du règlement de la Cour ;
5. ne jamais compter sur un courrier sommaire, un courriel ou un fax pour interrompre le délai ;
6. envoyer le formulaire complet par voie postale et conserver la preuve du cachet postal ;
7. préserver toutes les écritures nationales, pièces produites, QPC, preuves de dépôt et décisions.

La stratégie CEDH doit être construite comme une continuation documentée du contentieux national, non comme une reconstruction rétrospective après la décision du Conseil constitutionnel.


### Préservation individualisée du grief de Mme Vernerey

La requête et le mémoire QPC L.299 doivent distinguer :
- l'atteinte directement subie par M. Robert du fait de l'exclusion de sa candidature ;
- l'effet propre du formalisme sur Mme Laurence Vernerey comme remplaçante ayant consenti à la candidature et demandé une assistance matérielle.

Ne pas affirmer sans vérification qu'elle a qualité autonome pour agir devant le Conseil constitutionnel. En revanche, exposer dès maintenant la substance de son grief : engagement dans la candidature, consentement, handicap, empêchement fonctionnel, demande faite au tiers, absence alléguée d'aménagement et effet d'exclusion.

Objectif de subsidiarité : permettre aux juridictions nationales d'examiner cette difficulté avant toute éventuelle saisine personnelle de la CEDH par Mme Vernerey.


### Généralité des QPC et expérience de pensée sur les remèdes

Une QPC est déclenchée par un litige concret mais porte sur une disposition législative générale. Ne jamais réduire :
- la QPC L.299 à Mme Laurence Vernerey ;
- la QPC L.303 à M. Jean Hugues Noël Robert, à Mme Vernerey ou à M. Parigi.

Les faits individuels établissent l'applicabilité et le caractère concret de la question ; la formulation constitutionnelle doit être capable de gouverner toute situation juridiquement comparable.

Séparément, conserver dans la requête l'hypothèse de proclamation directe au titre de l'article 41 comme **expérience de pensée à des fins de raisonnement** sur l'étendue des pouvoirs réparateurs.

Règle de qualification :
- l'article 41 établit réellement que le Conseil peut, dans les cas où ses conditions sont réunies, réformer une proclamation et proclamer le candidat régulièrement élu ;
- ne pas en déduire que Jean Hugues Noël Robert remplit cette condition dans le présent scrutin ;
- expliciter que l'intérêt de la demande subsidiaire est de distinguer existence abstraite du pouvoir, applicabilité au cas d'espèce et autres remèdes disponibles ;
- intégrer symétriquement les conséquences qu'un remède pourrait produire pour le sénateur actuellement proclamé élu.

Ne pas supprimer cette fonction sous prétexte qu'elle est atypique : elle fait partie du raisonnement sur l'effectivité et sur les limites du remède.


### Règle de conservation sémantique des passes d'intelligibilité

Une demande de rendre la requête plus intelligible n'autorise **aucune réduction de sa sémantique**.

Toute passe de réécriture doit être sémantiquement conservative sauf instruction explicite contraire de l'auteur.

Avant de substituer une nouvelle version de lecture à la précédente :
1. inventorier les propositions, distinctions, réserves, conséquences, demandes et fonctions argumentatives de la version source ;
2. vérifier leur présence sous forme équivalente dans la version cible ;
3. distinguer le métatexte de fabrication, qui peut sortir du corps, du contenu juridiquement ou argumentativement utile ;
4. effectuer un diff sémantique après réécriture ;
5. toute suppression volontaire d'une idée de fond requiert un arbitrage humain explicite.

Règle canonique : **plus clair ne signifie jamais moins complet**.

Audit associé :
`research/senatoriales-2026/investigation/audit-pertes-semantiques-versions-requete-2026-10-07.md`


### Revue adverse QPC — points à préserver

**L.299 — grief contre la loi, non simple erreur d'application**
- Le droit d'éligibilité directement atteint est d'abord celui du candidat principal dont toute la candidature est exclue à raison d'une formalité imposée au remplaçant.
- Meilleure objection : L.299 pourrait déjà recevoir l'interprétation adaptée reconnue par le Conseil d'État pour L.265 ; dans ce cas le problème serait seulement l'application du texte.
- Réponse recherchée : formuler la QPC sur la constitutionnalité d'une interprétation qui interdirait toute adaptation et privilégier une conformité sous réserve.

**L.303 — fenêtre préélectorale sans voie de contrôle utile**
- Ne pas réduire le grief à l'absence de double degré de juridiction.
- Ne pas affirmer que le Conseil constitutionnel devait nécessairement pouvoir être saisi lui-même avant le scrutin.
- Cibler spécialement la seconde phrase : « Son jugement ne peut être contesté que devant le Conseil constitutionnel saisi de l'élection. »
- Dans le cas 2026, jugement le 14 septembre, scrutin le 27 septembre : **treize jours calendaires** pendant lesquels l'exclusion n'était pas encore irréversible, alors que le TA avait dû statuer en trois jours.
- Question générale : le législateur peut-il fermer toute voie de contrôle utile pendant cette fenêtre jusqu'à ce que le scrutin consomme l'atteinte ?
- Objection à anticiper : article 59 de la Constitution + article 33 de l'ordonnance organique structurent le contentieux post-électoral ; l'article 33 a été contrôlé a priori en 2011.
- Réponse : la QPC ne réclame pas nécessairement un recours préélectoral devant le Conseil constitutionnel ; elle attaque la fermeture de toute autre voie utile créée par L.303.

Règle : **la célérité explique un recours rapide ; elle ne suffit pas, à elle seule, à expliquer une période d'attente sans recours alors que le dommage reste encore évitable.**

## Mode d'emploi opératoire — comment construire et promouvoir une version

Avant toute nouvelle version de la requête :

~~~text
1. intégrer toute nouvelle trace / objection / réponse institutionnelle
2. qualifier son statut probatoire
3. l'insérer dans la chronologie
4. la rattacher à une pièce, ou motiver sa réserve/exclusion
5. mettre à jour l'inventaire probatoire
6. mettre à jour le bordereau si elle doit être produite
7. exécuter l'audit Gmail différentiel
8. revérifier les propositions de droit load-bearing sur sources officielles
9. rechercher les traces adverses ou contradictoires
10. refaire une passe "motifs de rejet"
11. contrôler requête ↔ chronologie ↔ bordereau ↔ inventaire
12. promouvoir seulement si les divergences sont fermées ou explicitement UNKNOWN
~~~

Bugs bloquants de préparation :
- fait matériel important absent de la chronologie ;
- pièce importante sans fait clairement identifié ;
- courriel INCLUDE sans mapping ;
- heure reconstruite sans preuve ;
- contradiction non qualifiée ;
- proposition de droit load-bearing sans source officielle vérifiée ;
- modification d'un seul objet qui rend les autres faux.

Le protocole complet est `protocole-constitution-requete-cc-2026-10-07.md`.

## A. MUST BEFORE FILING

- [ ] **Intelligibilité grand public — budget attentionnel minimal** — écrire comme pour un lecteur intelligent mais disposant de très peu de temps et d’attention. **Le but n'est pas de faire court ; le but est de faire facile à comprendre.** Une section peut être longue si cette longueur réduit l'effort cognitif, explicite les étapes et évite au lecteur de reconstruire le raisonnement. Une phrase doit porter une idée principale, mais plusieurs phrases courtes peuvent être préférables à une phrase condensée. Préférer sujet + verbe + conséquence. Définir tout terme technique avant usage. Employer des métaphores concrètes seulement si elles éclairent réellement (« une porte », « une chaîne », « une horloge », « un filet de sécurité »). Éviter les phrases à tiroirs, les doubles négations, les renvois implicites et les acronymes non expliqués. Le but n’est pas de simplifier la pensée, mais de **réduire la charge mentale** nécessaire pour la comprendre.
- [ ] **Longueur ≠ complexité cognitive** — ne jamais raccourcir pour le seul plaisir de raccourcir. Une explication plus longue est préférable si elle rend les prémisses visibles, découpe les étapes, définit les termes, montre les exemples et ferme les malentendus. Le critère d'échec n'est pas « trop de mots » ; c'est « trop d'effort pour comprendre ». La compression est utile seulement si elle ne transfère pas le travail cognitif au lecteur.
- [ ] **Intelligibilité expert — niveau juriste junior** — écrire pour un juriste compétent qui ne connaît ni le dossier ni toutes les spécialités mobilisées. Être didactique : rappeler la règle, son rang, sa fonction, la jurisprudence utile, le fait auquel elle s’applique, le meilleur contre-argument et la conséquence. Un lecteur expert doit pouvoir apprendre quelque chose sans avoir à reconstruire les prémisses.
- [ ] **Principe de Talleyrand — expliciter ce qui “va sans dire”** — toute prémisse utile, tout lien causal, toute distinction de régime, toute limitation et toute conséquence doivent être écrits. Interdire les sous-entendus décisifs, les pronoms ambigus, les « donc » non démontrés, les références floues (« cela », « cette pièce », « ce point ») et les transitions qui obligent le lecteur à deviner le raisonnement. **Ce qui va sans dire va encore mieux en le disant.**
- [ ] **Test anti-malentendu** — pour chaque grande section, demander : « quelles sont les trois mauvaises interprétations les plus faciles ? ». Ajouter une phrase explicite qui les empêche si elles sont plausibles.
- [ ] **Double accessibilité de lecture — MUST ABSOLU** — chaque grande section doit être intelligible à la fois par un lecteur non juriste et exploitable immédiatement par un juriste. Cela ne requiert plus deux rubriques mécaniques « Grand public / Expert ». La prose peut être unique, à condition qu'elle contienne à la fois le contexte et la finalité en langage courant, puis la règle, la source, la pièce, la qualification, le meilleur contre-argument et la conséquence. Les deux niveaux de compréhension doivent porter exactement le même sens et les mêmes réserves.
- [ ] **Documentation annexée** — joindre `investigation/annexe-documentation-double-lecture-2026-10-07.md` comme couche pédagogique : glossaire, acteurs, carte de procédure, chronologie, explication L.298/L.299/L.303, article 34, preuve électronique, statuts probatoires, guide du bordereau, tableaux question→trace→réponse→UNKNOWN et solutions praticables.
- [ ] **Complétude initiale maximale raisonnable** — privilégier un dossier initial aussi complet que possible, même long, dès lors que la longueur sert la compréhension, la preuve ou la préservation d’un grief. Raison juridique : les griefs nouveaux après le délai de l’article 33 peuvent être irrecevables ; l’article 35 ne prévoit qu’une faculté exceptionnelle de compléter certaines pièces. La longueur doit être structurée pour ne pas masquer le noyau contentieux.
- [ ] **Narration juridiquement contrôlée** — la requête doit expliquer non seulement « quoi », mais aussi le contexte, la finalité recherchée, les moyens employés, les contraintes et les réponses institutionnelles. Toute intention attribuée à un tiers doit être sourcée ou reformulée en fait observable / hypothèse.
- [~] **Intelligibilité ≠ brièveté — audit v0.22** — passe substantielle accomplie : plusieurs paragraphes ont été **dépliés** en davantage de phrases afin de réduire la charge cognitive. Le nombre de mots n'est pas un critère de réussite. Audit : `../reviews/audit-intelligibilite-requete-v0.22-2026-10-07.md`.
- [ ] **Passe micro-style phrase par phrase** — sur le texte hérité des versions antérieures, couper les phrases trop longues, supprimer les enchâssements inutiles, vérifier les antécédents de « cela / ceci / ce point / cette pièce », expliquer les acronymes à la première occurrence et fermer les « donc » dont la prémisse n'est pas écrite. Ne modifier aucun fait ni niveau de certitude.
- [x] **Placement final du control plane** — arbitrage appliqué en v0.23 : la check-list Cognitive Packet, le protocole de revue et les changelogs restent dans le control plane du Corpus et sont retirés du corps de la candidate de dépôt. Le texte juridictionnel conserve seulement les éléments utiles au Conseil.
- [x] **Audit double lecture section par section** — fermé sur la v0.23 : Premier écran, recevabilité, résumé, chronologie, formalités, solutions praticables, griefs 1–5, temporalité, conclusions et bordereau/matérialisation disposent d’une lecture grand public et d’une lecture expert cohérentes.
- [ ] **Mode d'emploi de constitution de la requête** — appliquer avant toute promotion de version le protocole `protocole-constitution-requete-cc-2026-10-07.md` : synchroniser requête, chronologie, bordereau, inventaire, Gmail, sources juridiques, contradictions et revue « motifs de rejet ». Aucun de ces objets ne doit diverger silencieusement.
- [ ] **Annexe chronologique détaillée** — joindre au paquet la chronologie `investigation/annexe-chronologie-detaillee-requete-cc-2026-10-07.md`, ordonnée jour par jour puis heure croissante, du premier courriel à la préfecture du **10 septembre à 17:01:56** jusqu'au dépôt effectif ; chaque acte matériel doit pointer vers sa pièce ou sa source et chaque UNKNOWN doit rester explicite.
- [ ] **Audit Gmail exhaustif avant gel** — exécuter puis fermer le registre `investigation/gmail-audit-requete-2026-09-10-2026-10-07.md`. Toute trace potentiellement pertinente doit recevoir une disposition **INCLUDE / RÉSERVE / EXCLURE + motif / REVIEW** ; tout INCLUDE doit être mappé à une pièce ou à une annexe. Rechercher envoyés et reçus, par domaines/adresses, dates, fils et mots-clefs ; ne pas se limiter aux objets déjà connus.
- [ ] **Audit Gmail — messages révélés hors cartographie initiale** — arbitrer explicitement au minimum : premier envoi du 10/09 à 17:01:56 et son bounce/DSN ; rectification du 12/09 ; commission de propagande du 16/09 ; proposition Télérecours du 18/09 ; relance préfecture du 21/09 ; demande lieu/proclamation du 26/09 ; première demande PV du 27/09 ; acceptation consultation du 30/09.
- [x] **P-04 — premier envoi et DSN** — le premier envoi du 10/09 à 17:01:56 est désormais corroboré par trois DSN natifs d'échec pour taille (~17:02:59, ~17:03:34, ~17:04:35) puis par la retransmission allégée de 17:54:50. P-04 devient la chaîne technique complète ; conserver les messages natifs et calculer les SHA des fichiers effectivement produits.
- [ ] **Chronologie ↔ bordereau ↔ requête** — avant gel, contrôler automatiquement/manuellement qu'aucun fait important cité dans la requête n'est absent de la chronologie, qu'aucune pièce importante n'est orpheline de fait, et qu'aucun événement chronologique important n'est dépourvu de source identifiable.

- [x] **Délai** — échéance légale vérifiée : **7 octobre 2026 à 18 h** (art. 33 de l’ordonnance du 7 novembre 1958).
- [~] **Version canonique de dépôt** — la candidate courante est la requête stable `research/senatoriales-2026/requete-conseil-constitutionnel.md`. L'objet vivant garde cette adresse stable ; la version réellement déposée devra être figée, horodatée, hachée et tracée au moment du dépôt.
- [x] **Premier écran contentieux** — juridiction, requérant, qualité pour agir, élection contestée, décision initiale, délai, griefs et conclusions sont explicités dans la requête stable.
- [x] **Forclusion des griefs nouveaux** — point load-bearing : tous les moyens matériels doivent être contenus en substance dans la requête initiale. Décision n° 2024-6345/6354/6370 AN/QPC : un grief présenté pour la première fois après le délai de l’article 33 est irrecevable.
- [x] **Article 35 : pièces, pas réserve générale de moyens** — le Conseil peut exceptionnellement accorder un délai pour une partie des pièces ; ne pas compter sur cette faculté pour créer un grief nouveau après 18 h.
- [~] **Canal de dépôt — article 34** — règle juridique vérifiée : requête écrite au secrétariat général du Conseil constitutionnel ou au représentant de l’État. La matrice `matrice-canaux-materiels-depot-2026-10-07.md` distingue désormais destinataire juridique, modalité matérielle, preuve et risque. L’acte matériel de remise reste à accomplir. Ne pas compter sur un simple courriel du requérant comme canal acquis.
- [ ] **Redondance matérielle du dépôt — même paquet, plusieurs voies** — mobiliser autant que raisonnablement possible plusieurs voies indépendantes **du même paquet gelé** : au minimum remise physique au représentant de l’État à Bastia ; si possible remise directe d’un exemplaire strictement identique au secrétariat général du Conseil constitutionnel à Paris par porteur/coursier ; envisager un commissaire de justice comme renfort probatoire de remise. Chaque voie doit produire sa propre preuve datée et horodatée.
- [ ] **Anti-divergence entre dépôts redondants** — avant toute remise multiple, figer une seule requête canonique, un seul bordereau et un seul jeu de pièces ; calculer les SHA-256 et identifier les exemplaires physiques. Interdiction de déposer silencieusement des versions différentes par des canaux parallèles. Une correction postérieure devient un objet distinct et explicitement daté.
- [ ] **Réception avant délai ≠ expédition avant délai** — pour tout canal postal, express ou coursier, exiger une preuve de **réception** avant l’échéance ; ne pas considérer le cachet d’expédition comme filet suffisant. Jurisprudence de contrôle : décisions 2017-5267 QPC/SEN et 2017-5256 QPC/AN.
- [ ] **Préfecture Bastia — sécuriser l’accès pratique** — l’accueil public ordinaire publié est 8 h 30–11 h 30 et 13 h 30–15 h 30, sur rendez-vous. Confirmer dès l’ouverture le service concret receveur, l’accès et la possibilité d’obtenir récépissé/cachet avec heure ; viser une remise très antérieure à 15 h 30, sans organiser le dépôt autour de 18 h.
- [ ] **Conseil constitutionnel — remise directe à Paris** — confirmer dès l’ouverture les modalités pratiques de réception d’une requête électorale au secrétariat général, 2 rue de Montpensier, et, si une personne/coursier est mobilisable à Paris, lui transmettre un exemplaire strictement identique avec instruction d’obtenir une preuve de remise datée et horodatée.
- [ ] **Sous-préfecture de Corte — ne pas présumer l’habilitation** — aucune source examinée ne suffit à établir qu’une remise à la sous-préfecture vaut à elle seule saisine du « représentant de l’État » au sens de l’article 34. Ne compter cette voie qu’après confirmation explicite qu’elle reçoit la requête pour le compte du représentant de l’État ; sinon la traiter comme tentative/trace complémentaire.
- [ ] **Dépôt dématérialisé — article 34 + CRPA** — mobiliser une voie électronique vers le représentant de l’État comme **redondance juridiquement argumentée** : l’article 34 exige une « requête écrite adressée » sans imposer le papier ; les articles L.112-8, L.112-9 et R.112-9-2 CRPA organisent en principe la saisine électronique d’une administration, et L.112-11 / R.112-11-1 l’accusé électronique. Vérifier l’absence d’exclusion spécifique et les modalités du téléservice applicable. Tant qu’aucune confirmation explicite ne ferme ce point, **ne pas en faire l’unique canal**.
- [ ] **SVE / canal électronique officiel de la préfecture** — identifier et utiliser, si matériellement possible avant l’échéance, le téléservice officiel « Saisir l’administration par voie électronique » ou tout canal institutionnel prévu pour les services de l’État ; fournir identité complète, objet explicite « REQUÊTE ARTICLE 34 », paquet canonique figé, manifeste SHA, et demander un accusé indiquant date de réception et service.
- [ ] **Courriels institutionnels redondants** — envoyer le même paquet figé aux boîtes institutionnelles déjà actives dans le dossier si les limites de taille le permettent ; conserver EML/MIME, DSN, accusés automatiques et humains. Si le paquet est trop volumineux, documenter le mécanisme de transfert et son empreinte. Ne jamais confondre preuve d’envoi et preuve de réception.
- [ ] **Conseil constitutionnel — voie électronique directe à confirmer** — rechercher/obtenir confirmation du secrétariat général sur l’existence d’une adresse ou téléprocédure acceptant une requête électorale dématérialisée. En l’absence de confirmation, qualifier tout envoi électronique direct comme tentative/copie de traçabilité et maintenir les autres voies.
- [ ] **Doctrine de support** — documenter explicitement que le choix du dématérialisé vise l’intégrité et la traçabilité : fichiers gelés, SHA-256, horodatage, manifeste, conservation des natifs et preuves de réception. Ne jamais soutenir que « numérique = valide » par nature ; soutenir seulement que le numérique permet une chaîne de preuve plus fine lorsqu’il est admis par le canal juridique.
- [ ] **P-45 — silence administratif sur les modalités de dépôt** — produire **intégralement** dans le dossier les quatre courriels P-45.a à P-45.d : 26/09 demande au Bureau des élections ; 28/09 demande directe à la Sous-préfecture de Corte ; 01/10 consolidation avec Sous-préfecture en copie ; 02/10 relance numérotée P1–P18 avec P11/P12. L'index public `investigation/sources/chaine-silence-etat-modalites-depot-2026-09-26-10-02.md` ne remplace pas les messages natifs.
- [ ] **P-45 — intégralité et authenticité des courriels** — pour chaque sous-pièce, joindre une représentation lisible du message **complet**, avec date/heure, objet, destinataires/copies et en-têtes utiles ; conserver si possible l'export natif EML/RFC822 ; calculer le SHA-256 du fichier effectivement produit ; vérifier que le sous-identifiant P-45.x du bordereau correspond exactement au fichier annexé.
- [x] **P-45 — borne probatoire du silence** — recherche Gmail ciblée vérifiée : le fil du 26/09 et celui du 28/09 ne contiennent chacun qu'un message sortant ; aucune réponse provenant de l'adresse institutionnelle de la Sous-préfecture de Corte n'a été retrouvée entre le 28/09 et le 07/10. Ne pas écrire « l'État n'a jamais répondu » : P-28 établit une réponse sur la consultation des pièces. La proposition documentée est plus étroite : **aucune réponse substantielle retrouvée sur la modalité de dépôt article 34 malgré les demandes et relances identifiées**.
- [ ] **P-45 — présence dans la requête et le bordereau** — contrôler avant gel que la requête stable cite **P-45.a — demande du 26 septembre**, **P-45.b — demande du 28 septembre**, **P-45.c — consolidation du 1er octobre** et **P-45.d — relance du 2 octobre** dans la chronologie et dans le grief d'effectivité, et que le bordereau les identifie comme sous-pièces A à produire intégralement.
- [ ] **Marge opérationnelle de dépôt** — fixer une heure-cible interne antérieure à 18 h, un seuil explicite d'arrêt des améliorations non essentielles et une priorité absolue à la remise + preuve de remise. Ne jamais sacrifier le dépôt au perfectionnement tardif du dossier.
- [ ] **Gel pré-dépôt** — une fois la dernière revue terminée : figer SHA/version, PDF ou exemplaire réellement remis, bordereau et pièces ; toute correction ultérieure doit devenir explicitement postérieure au dépôt.
- [x] **Fondement du recours** — articulation stabilisée : Constitution art. 59 / ordonnance de 1958 / code électoral, notamment L.303.
- [ ] **FBF des pointeurs de version courante** — avant gel, rechercher mécaniquement dans la requête, le bordereau, l'inventaire et la checklist toute mention d'une ancienne version qui prétend encore décrire l'état courant ; conserver les références historiques uniquement lorsqu'elles sont explicitement historiques.
- [ ] **Bordereau autonome** — vérifier que le bordereau de pièces correspond exactement aux pièces effectivement jointes et à leur numérotation.
- [ ] **Registre probatoire autoportant pièce par pièce** — pour chaque P-xx (et chaque sous-pièce d'un ensemble composite), contrôler numéro, titre, date, provenance, description, rôle probatoire/argumentatif, fichier source, URL éventuelle, empreinte SHA-256, transcription si utile, confidentialité/occultation, et présence effective dans le paquet final. Une référence externe ne remplace jamais une définition suffisante dans la requête ou le bordereau.
- [ ] **Règle de lisibilité humaine des pièces — “ce que c’est / place dans le raisonnement”** — chaque pièce P-xx doit pouvoir être comprise sans mémoriser la numérotation. Pour chaque pièce (et sous-pièce si nécessaire), maintenir une mini-fiche en deux étages : **(1) Ce que c’est** : description courte, concrète et factuelle de l’objet, de sa date et de son origine ; **(2) Place dans le raisonnement** : proposition exacte qu’elle soutient, étape du raisonnement à laquelle elle se rattache, limite de ce qu’elle n’établit pas, et fonction dans le dossier (**noyau / soutien / contexte-réserve / sensible**). Ajouter, lorsque matériel, sa **valeur historique/documentaire** : ce qu’un lecteur futur perdrait de la compréhension de la séquence si cette pièce ou son contenu n’était pas conservé ou expliqué. Éviter dans les revues, checklists, bordereaux et explications humaines les références nues du type « P-14 » lorsqu’un lecteur devrait connaître la pièce par cœur ; écrire par exemple **« P-14 — requêtes préfectorales n° 2601714 et 2601715 + bundles TA »**. Une table compacte peut abréger seulement si l’intitulé reste visible sur la même ligne.
- [ ] **Pièces composites — sous-numérotation stable** — lorsqu'une même séquence probatoire comporte plusieurs objets matériels distincts (avis postal, enveloppe, page de notification, jugement, photographie contextuelle, recto/verso, transcription), conserver le numéro principal mais attribuer des sous-identifiants stables (ex. P-20.a, P-20.b…) afin qu'une citation pointe vers un objet précis sans renumérotation globale du dossier.
- [ ] **Manifeste forensique du paquet** — établir une relation vérifiable `numéro de pièce → fichier exact → nombre de pages → taille → SHA-256 → provenance → transformation/occultation éventuelle → support effectivement remis`. Toute copie transformée ou expurgée reçoit son propre hash ; le hash de l'original natif est conservé séparément.
- [ ] **Originaux et copies expurgées** — pour toute pièce produite sous forme expurgée (notamment P-44), conserver l'original natif intact, documenter l'opération de dérivation et ne jamais remplacer l'original par la version nettoyée.
- [ ] **Pièces critiques** — vérifier présence, lisibilité, date, origine et concordance des pièces relatives au dépôt de candidature, aux formalités de la remplaçante, au TA, aux échanges préfectoraux et au scrutin.
- [ ] **P-09 — borne probatoire explicite** — vérifier que partout où P-09 est invoquée, elle n'établit que la prise en charge / le dépôt à 12 h 20 et **ne vaut pas preuve de conformité juridique** de la candidature.
- [ ] **P-09 — récépissé provisoire : scan + transcription textuelle** — joindre au paquet remis le scan/reproduction lisible du récépissé provisoire délivré le **11 septembre 2026 à 12 h 20** et une transcription textuelle fidèle de tous les champs lisibles. La transcription déjà conservée dans le Corpus peut servir de base, mais la version de dépôt doit être contrôlée ligne à ligne contre l'image primaire ; signaler explicitement toute mention illisible, anomalie ou lacune au lieu de la compléter par inférence.

- [x] **P-08 — verrou anti-régression sur le trajet du 11 septembre** — conserver comme état canonique : **train n°2 Ajaccio–Bastia** ; plan initial Corte **09 h 45** → Bastia **11 h 39** ; départ réel de Corte plus tardif ; stop puis montée **très probable** à **Lucciana L’Alivella** vers l'horaire théorique de **11 h 04** ; billet CFC émis à **11 h 25** **vendu à bord**, donc cette heure n'est pas l'heure de montée ; Lupinu observé vers **11 h 51**, Bastia vers **11 h 55**. **Ne jamais réintroduire l'hypothèse erronée du train n°214**, née d'une coïncidence d'horaire à Lupinu. Ne jamais promouvoir Lucciana de « très probable » à « certaine » sans nouvelle trace indépendante.
- [x] **P-13 — verrou temporel préparation / création / envoi** — conserver trois temps distincts : **~17 h 30** = préparation de la déclaration commune (**rapportée / trace conversationnelle**) ; **17 h 45 min 55 s CEST** = création de `VID_20260911_174455.mp4` selon la métadonnée native actuellement retenue ; **17 h 57 min 55 s** = envoi Gmail du lien au BEDL. Interdiction de résumer ces trois événements par une formule unique du type « vidéo enregistrée à 17 h 30 ». Lors du gel, recalculer SHA-256, taille et métadonnées sur le fichier natif effectivement produit et conserver la source exacte de chaque horodatage.
- [ ] **P-13 — contrôle forensique de l'original vidéo** — recalculer sur le fichier natif effectivement conservé le SHA-256 annoncé `aaac3d97801f57185e38cb3c26f9ec4597aee52188a494f63a81874e1fb1a7d8`, vérifier la taille annoncée (**79 663 474 octets**) et distinguer strictement l'heure inscrite dans le nom `VID_20260911_174455.mp4`, les métadonnées natives éventuelles, l'heure de versement Drive et toute autre trace indépendante. Ne pas appeler « heure de création » une valeur dont la source exacte n'est pas explicitée.
- [ ] **P-17 — note manuscrite recto-verso remise à l'audience : scan + transcription textuelle** — joindre la reproduction recto-verso de la feuille manuscrite remise en main propre au début de l'audience du **14 septembre 2026**, ainsi qu'une transcription textuelle fidèle. Le texte avait été dicté dans une conversation contemporaine, mais le libellé exact doit être récupéré ou vérifié contre le scan : **ne pas reconstruire silencieusement de mémoire**. Cette pièce doit être traitée comme une production autonome de l'audience et reliée à la chronologie et au bordereau.
- [ ] **P-17 — rattachement procédural** — distinguer : existence et contenu photographiés ; remise en main propre rapportée par le requérant ; mention générale d'« observations écrites et orales » dans le jugement ; rattachement exact à l'entrée Sagace « Réception d'une lettre » encore à établir. Ne pas transformer ces indices convergents en preuve institutionnelle plus forte qu'ils ne le sont.
- [ ] **P-17 — granularité matérielle** — distinguer au minimum le recto, le verso et la transcription vérifiée comme trois objets identifiables sous un même numéro principal ; préciser pour chacun le fichier exact et son SHA-256. La transcription est un dérivé de lecture ; les images du manuscrit restent les pièces primaires.
- [x] **P-14 — deux requêtes préfectorales retrouvées et comparées** — les bundles `2601714` et `2601715` contiennent une saisine signée de trois pages au même contenu substantiel ; leur position dans les bundles diffère. Ne pas parler d'identité binaire des PDF complets sans comparaison de fichiers.
- [x] **P-14 — distinction L.298 / L.299 dans la saisine** — l'exposé des faits rappelle **L.298 et L.299** ; la partie « Discussion » reproduit et développe expressément **L.299** pour l'exigence d'« original », sans développement autonome de L.298.
- [x] **e-Sagace — sens des conclusions** — les deux dossiers affichent un refus pour méconnaissance alléguée de **L.298, L.299 et L.301**. Qualifier correctement : il s'agit du sens des conclusions, pas du jugement.
- [ ] **Jugement primaire — contrôle L.298 / L.299 / L.301** — relire ligne à ligne l'expédition primaire P-20 et enregistrer exactement les dispositions visées et développées. Si L.298 est absent de la motivation alors qu'il figure dans le sens des conclusions e-Sagace, décrire cette différence sans en déduire automatiquement qu'un moyen aurait été ignoré.
- [ ] **P-20 — heure de mise à disposition** — conserver comme **UNKNOWN** l'heure exacte de mise à disposition du jugement au greffe tant qu'une trace primaire ne la fixe pas.
- [ ] **P-20 — chaîne matérielle de notification du jugement du 14 septembre** — traiter séparément, sous P-20 avec sous-identifiants stables, (a) l'avis de passage / notification trouvé dans la boîte aux lettres, (b) l'enveloppe ou pli recommandé retiré à La Poste et les éléments permettant d'en rattacher le retrait au lieu et à la date, y compris la photographie de la plaque « Avenue du Baron Mariani » prise, selon le requérant, en sortant du bureau après le retrait du pli ; l'adresse du bureau **La Poste CORTE — Avenue du Baron Mariani, 20250 Corte** est vérifiée sur le localisateur officiel de La Poste (https://localiser.laposte.fr/haute-corse/corte/corte-200960), (c) la page de notification du greffe, (d) les trois pages du jugement. Pour chaque élément : fichier exact, date/provenance, SHA-256, lisibilité et fonction probatoire. Ne pas présenter une photographie comme horodatée si ses métadonnées ou une autre trace indépendante ne l'établissent pas.
- [x] **P-20 — fonction probatoire de la photo « Avenue du Baron Mariani »** — l'utiliser d'abord comme **repère matériel et intelligible** montrant que « Baron Mariani » n'est pas une désignation inventée ex nihilo pour la campagne : l'expression appartient à la toponymie publique de Corte. Borne impérative : cette photo **ne prouve pas à elle seule** un droit nobiliaire personnel du requérant ni sa filiation/généalogie ; si ces points deviennent matériels, ils exigent leurs propres pièces.
- [x] **P-20 — borne ante quem de la photographie** — une trace conversationnelle antérieure établit que la photographie de la plaque « Avenue du Baron Mariani » avait déjà été transmise à ChatGPT **au plus tard le 25 septembre 2026 à 15 h 17 CEST**. Employer cette donnée uniquement comme **borne supérieure de possession/transmission de l'image**, jamais comme heure de prise de vue.
- [ ] **P-20 — contrôle postal croisé** — relever et comparer sur l'avis de passage, le pli, l'AR et toute preuve de distribution : numéro de recommandé / identifiant de suivi, dates de présentation et de retrait/distribution, cachets, bureau, expéditeur/destinataire. Utiliser les identifiants identiques comme jonctions probatoires, sans présumer l'identité si un champ est illisible.
- [x] **P-44 — chaîne France Transfert retrouvée** — deux courriels reçus le 11 septembre à **18 h 45 min 53 s** : avis de pli provenant du greffe et mot de passe transmis séparément. Le premier annonce les quatre fichiers (deux CRAASE + deux PDF préfectoraux). Mot de passe et liens non publiés.
- [ ] **P-44 — pièce à matérialiser pour le dépôt** — joindre au paquet Conseil une copie des deux courriels France Transfert établissant la provenance de P-14, en masquant mot de passe, lien et jetons inutiles ; conserver les originaux natifs disponibles pour vérification.
- [x] **Influence sur le scrutin** — la requête distingue clairement :
  - l'écart entre candidats présents ;
  - la distance à la majorité absolue ;
  - la borne contrefactuelle ;
  - les comparaisons 2A/2B comme ordres de grandeur, non comme transferts de voix.
- [x] **22–29 % / 33 %** — pourcentages entiers dans le framing public et la démonstration principale ; valeurs exactes et dénominateurs conservés dans la couche de vérification.
- [x] **A Voce** — nature politique de l’offre 2026 intégrée et sourcée ; ne pas réduire 2026 à une répétition mécanique de la candidature de 2020.
- [x] **"Acqua in bocca" / soutien public ≠ vote réel** — intégré comme problème d’inférence électorale, non comme essence culturelle : base institutionnelle minimale identifiable d’environ **1 % (5 grands électeurs)** contre **14 % (88 voix)** au résultat, sans attribution individuelle des bulletins.
- [x] **Déclarations publiques / commentaires de presse — P-41** — principales sources et bornes revérifiées ; conserver comme **B — soutien / réserve**, non comme pièce du noyau à joindre par défaut. Les formulations adverses restent conservées ; aucune intention rapportée ni appartenance institutionnelle n’est transformée en bulletin secret.
- [x] **Bulletin nul "BARON MARIANI"** — statut borné dans la v0.14 et le bordereau : trace matérielle d'une offre absente ; ni suffrage valide, ni identification certaine d'un électeur, ni preuve autonome d'influence déterminante.
- [x] **Conclusions** — la v0.14 distingue annulation comme conclusion principale, mesures d’instruction subsidiaires et proclamation directe comme conclusion infiniment subsidiaire / probe exploratoire.
- [x] **Effet de l’annulation — LO 322** — v0.14 corrigée : demander l’annulation comme remède principal et demander au Conseil d’en tirer les conséquences légales ; LO 322 prévoit l’élection partielle dans les trois mois.
- [x] **Remède extrême** — décision explicite : la proclamation directe est conservée comme conclusion infiniment subsidiaire et probe exploratoire ; elle n’est pas présentée comme le remède normalement disponible.
- [~] **QPC — deux mémoires distincts créés, revue finale à fermer** — les deux mémoires juridictionnels existent désormais : `qpc/memoire-qpc-l303-garanties-juridictionnelles.md` et `qpc/memoire-qpc-l299-formalisme-candidature-empechement-remplacant.md`. Avant gel : vérifier une dernière fois la déclaration antérieure de conformité, la formulation exacte du droit/liberté garanti, le caractère sérieux, les références jurisprudentielles et la cohérence exacte avec la requête.
- [~] **Contrôle de solidité QPC** — les deux QPC ont vocation à être incluses dans le dépôt final, mais chacune doit rester juridiquement autonome et réellement dirigée contre la disposition législative elle-même. Si une formulation ne satisfait pas les conditions propres à la QPC, la corriger avant dépôt plutôt que la conserver sous une qualification inexacte.
- [x] **Défenseur des droits** — saisine maintenue distincte du recours CC ; aucun effet suspensif sur les délais ne lui est attribué.
- [x] **Trace Défenseur des droits — P-42** — saisine du 26 septembre vérifiée dans Gmail ; déléguée mise en copie les 1er et 2 octobre ; aucune réponse provenant de son adresse retrouvée dans la recherche ciblée au 6 octobre. Ne pas écrire « aucune réponse n'existe », mais « aucune réponse retrouvée ».
- [ ] **Corpus complet des courriels** — conserver et indexer tous les courriels matériellement pertinents avec préfecture, TA, Défenseur des droits, remplaçante et autres acteurs ; distinguer **complétude de conservation** et **sélectivité de production au Conseil**.
- [~] **Minute du jugement / demandes réitérées au TA — P-21, P-29 à P-33** — chaîne documentaire matérialisée dans `investigation/chaine-ta-p29-p33-2026-10-06.md`, avec séparation demande/réponse/inconnu. Reste à vérifier que les courriels natifs P-29 à P-33 sont effectivement présents et lisibles dans le paquet matériel remis ; l’index ne les remplace pas.
- [x] **P-43 — correspondance contemporaine avec Laurence Vernerey du 7 au 14 septembre** — index vérifié créé à partir de Gmail. **P-43.a — courriel « Autorisation » du 10 septembre 2026** et **P-43.b — courriel « Porte-parole » du 11 septembre 2026** sont désormais des sous-pièces à **production obligatoire** dans le paquet final. Produire les messages natifs et une représentation lisible ; occulter seulement les données privées étrangères au litige.
- [ ] **Diligence Bastia → Ajaccio du 11 septembre** — documenter explicitement la séquence matérielle après le dépôt physique à Bastia : déplacement du candidat jusqu’à Ajaccio pour rejoindre Mme Vernerey et enregistrer avec elle, avant 18 h, une déclaration vidéo commune. Vérifier et relier les traces disponibles du déplacement et de l’horaire ; ne pas réduire cette diligence à la simple existence abstraite d’une « vidéo ».
- [ ] **Vidéo P-13 — texte exact lu en commun** — retrouver ou établir une transcription fidèle du texte effectivement lu par M. Robert et Mme Vernerey dans la prise continue du 11 septembre ; permettre au Conseil de lire immédiatement les affirmations d’identité, de volonté et de consentement sans dépendre du seul visionnage. Conserver la distinction : force probatoire du consentement ≠ substitution automatique aux formalités de L.299.
- [x] **P-12/P-13 — émission avant l’échéance** — courriel de transmission envoyé au Bureau des élections le 11 septembre à **17 h 57 min 55 s**, avec lien vers la déclaration vidéo commune ; l’inventaire initial P-14 ne mentionne ni P-11 ni P-12. Ne pas confondre émission établie avec réception par l’infrastructure de l’État ou versement au TA, qui restent des questions distinctes.
- [ ] **Chaîne de relances vidéo — 14–18 septembre** — faire apparaître dans la requête, pièces à l’appui, la continuité des démarches : **14/09 avant audience**, demande à la préfecture avec greffe en copie de faire verser le courriel/vidéo manquant ; **15/09**, trois questions factuelles (reçu avant 18 h ? transmis avec la saisine ? transmis ultérieurement ?) ; **16/09**, relance ; réponse Vidal ne répondant pas matériellement aux trois questions ; **17/09**, reformulation « oui / non / information non disponible » ; **18/09**, nouvelle relance constatant l’absence de réponse. Relier ensuite les demandes des 25/09, 01/10 et 02/10.
- [ ] **Vidéo — triptyque probatoire** — distinguer et documenter séparément : **(a) produite/envoyée**, **(b) reçue/versée au dossier**, **(c) effectivement examinée/visionnée**. À ce stade : (a) établi côté expéditeur ; (b) non établi pour P-12/P-13 ; (c) aucune trace institutionnelle identifiée. Ne jamais convertir l’absence de preuve de (b) ou (c) en preuve positive de non-transmission ou de non-examen.
- [ ] **Diligences maximales sur le consentement** — vérifier que la requête expose cumulativement, et non en fragments dispersés : autorisation écrite de Laurence, pièces d’identité et électorales, présence physique du candidat, déplacement pour rencontre physique commune, déclaration vidéo en prise continue, transmission avant 18 h, offre de visionnage au TA rapportée, puis production AAH. L’objet est de permettre au Conseil d’apprécier la réalité et l’intensité des garanties apportées sur l’authenticité du consentement.
- [ ] **Biais de cadrage / propagation de prémisse** — vérifier que la requête explique, sans psychologie attribuée aux personnes, le risque qu’une prémisse administrative globale (« originaux papier ») ait structuré l’examen juridictionnel au point de rendre périphériques les éléments dissonants : consentement documenté, handicap, présence physique du candidat, solutions praticables, vidéo et distinction L.298/L.299. Employer un vocabulaire de cadrage institutionnel / propagation de prémisse, pas un diagnostic cognitif individuel.
- [~] **Test de cohérence candidat / remplaçante** — isoler la question suivante : si la dématérialisation était en elle-même rédhibitoire, pourquoi distinguer le traitement du candidat physiquement présent et celui de la remplaçante absente, alors que la saisine mobilise spécialement L.299 ? Si le vrai nœud est l’acte personnel de la remplaçante, vérifier que handicap, consentement éclairé et CE 14 mai 2021, n° 445497 sont examinés explicitement.
- [x] **CEDH** — la v0.14 ne présente pas Strasbourg comme un appel du Conseil constitutionnel et conserve la logique recours internes pertinents → décision interne définitive → délai de quatre mois.
- [x] **Symétrie seulement conditionnelle** — la v0.14 explicite que Robert comme Parigi ne peuvent envisager Strasbourg qu’en qualité personnelle de victime d’un grief conventionnel défendable ; la fermeture de la voie interne ne crée pas à elle seule un droit à un examen au fond.
- [x] **2017 / 2024 / 2026** — répétition conservée comme contexte, connaissance institutionnelle et hypothèse de mécanisme récurrent ; **répétition ≠ situation continue** et ne rouvre pas, à elle seule, les délais expirés.
- [ ] **Qualité de victime CEDH — matrice Robert / Vernerey** — séparer les griefs directement subis par le candidat de ceux directement liés à la remplaçante et au handicap ; ne pas présumer qu’un requérant peut porter automatiquement le grief personnel de l’autre.
- [ ] **Comparatif média service public — 2017 / 2020 / 2024 / 2026** — inventorier, pour chacune des quatre candidatures, France 3 Corse ViaStella / France Télévisions et Radio France-ICI/RCFM : invitation ou non aux débats, entretiens, durée/format, date dans la campagne, présentation éditoriale, comparateurs parmi les autres petites candidatures ; distinguer trace d'absence de couverture, absence réellement vérifiée et refus explicite.
- [ ] **Comparatif média général — 2017 / 2020 / 2024 / 2026** — même grille pour Corse-Matin, Corse Net Infos, Alta Frequenza et autres médias significatifs ; comparer les petites candidatures entre elles, pas seulement aux favoris.
- [ ] **Forme et fond des quatre candidatures** — documenter séparément : titulaire/remplaçant, étiquette ou alliance, offre politique effectivement formulée, thèmes de fond, dispositif de campagne, originalités de forme, et manière dont les médias résument ou caricaturent éventuellement cette offre ; ne pas confondre ton éditorial et description du programme.
- [ ] **CSA / Arcom / juridictions — effectivité des recours** — tracer pour 2017 et 2024 les saisines, accusés, numéros, réponses de fond éventuelles et absence de suite retrouvée. État vérifié au 6 octobre : ticket CSA **227435** accusé le 7 juin 2017 ; alerte Arcom **807989** validée le 21 juin 2024 ; recherche ciblée actuelle sans réponse de fond retrouvée sous ces identifiants. Une absence de réponse retrouvée n'est pas encore une preuve d'absence absolue.
- [ ] **Hypothèse “décoratif vs effectif”** — ne pas l'énoncer comme fait global avant matrice comparative. Tester : droit formel d'être candidat / accès réel au débat / recours accessible / réponse obtenue / remède capable de réparer. Relier cette grille à l'amendement d'effectivité sans prétendre que le droit positif consacre déjà un principe général d'effectivité.
- [ ] **Corse laboratoire / expérimentation mesurée** — conserver l'ancrage historique vérifié : un rapport de l'Assemblée nationale qualifie explicitement 1982-1992 de « laboratoire institutionnel » et le statut de 1982 d'anticipation de la décentralisation ensuite étendue aux régions. Pour toute affirmation plus large (« nombreuses innovations généralisées »), exiger une série de cas documentés avant publication.
- [ ] **Droit positif de l'expérimentation** — rappeler que l'article 72 de la Constitution et les articles LO1113-1 s. CGCT organisent déjà des expérimentations territoriales bornées dans le temps et évaluées ; utiliser ce voisin juridique comme précédent de méthode, non comme validation automatique de l'amendement 72-5.
- [~] **Revue adverse finale** — passe interne corrélée « motifs de rejet » effectuée et archivée ; trois risques dominants : dépôt/preuve, L.299 + exception handicap, incidence sur le scrutin. Une revue externe décorrélée reste souhaitable si disponible mais ne doit pas retarder le dépôt.
- [x] **Précédent refus d’enregistrement — 2014-4909 SEN** — conserver le précédent direct : le Conseil, saisi de l’élection, a examiné un refus préfectoral d’enregistrement d’une candidature sénatoriale ; ne pas lui faire dire davantage sur le fond de 2026.
- [x] **Calendrier Sénat objectivé** — 7 octobre 15 h : audition de la ministre ; 21 octobre matin : réunion de la commission pour le rapport ; 26 octobre : discussion en séance publique. Utiliser ces dates pour la perte temporelle et une demande d’examen dans les meilleurs délais, sans inventer de procédure d’urgence.
- [ ] **Faits / hypothèses / arguments** — dernière passe de qualification : aucun élément rapporté ou inféré ne doit être promu silencieusement en fait acquis.
- [ ] **Intelligible par le grand public** — vérifier qu'un lecteur non juriste peut comprendre en une lecture : ce qui s'est passé, pourquoi cela compte, quel est le seuil ou l'ordre de grandeur pertinent, et ce qui est demandé au Conseil, sans devoir reconstruire l'argument à partir des annexes.
- [ ] **Intelligible par un juriste junior du Conseil constitutionnel** — vérifier qu'un juriste découvrant le dossier peut identifier immédiatement : compétence, recevabilité, faits matériels, griefs, normes invoquées, pièces utiles, démonstration d'influence, conclusions principales/subsidiaires et points restant incertains, sans connaissance préalable du Corpus.

## B. SHOULD BEFORE FILING

- [ ] **Architecture recours** — vérifier la cohérence entre requête, QPC, Défenseur des droits, éventuelle CEDH et probes de remèdes.
- [ ] **Synchronisation Suicide Corse n°4** — refléter les changements substantiels de la requête sans prétendre qu'un brouillon est déjà déposé.
- [ ] **Communication publique** — vérifier que les publications publiques restent compatibles avec la requête sans lui substituer une rhétorique différente sur les faits.
- [ ] **Ouverture assumée — texte à préserver sans altération** — si l'ouverture est retenue dans la requête ou dans une version publique associée, conserver exactement : **« Obtenir le respect, en Corse comme ailleurs, réclame d'en manifester ; le mépris appelle le mépris ».** Ne pas lisser cette phrase au nom d'une prudence stylistique ; contrôler seulement sa place, sa fonction et la transition immédiate vers les faits et le droit.
- [ ] **Style / panache sans perte probatoire** — le texte peut mobiliser avec parcimonie des références historiques, maximes et proverbes corses lorsqu'ils servent la compréhension ou la mémorisation. Chaque citation doit être soit vérifiée, soit explicitement présentée comme attribution traditionnelle. Éviter l'empilement décoratif : une référence doit porter une idée ou une transition, pas remplacer une démonstration.
- [ ] **Danton / audace** — si mobilisé, préférer la formulation historiquement attestée du discours du 2 septembre 1792 : « de l'audace, encore de l'audace, toujours de l'audace » ; l'utiliser comme signal de méthode ou de ton, non comme argument juridique.
- [ ] **Talleyrand / explicitation** — rappeler si utile la maxime traditionnellement attribuée à Talleyrand, « Ce qui va sans dire va encore mieux en le disant », comme principe de lisibilité : expliciter ce qui est décisif même si cela paraît évident.
- [ ] **Proverbes corses** — avant insertion, vérifier graphie, sens, source et adéquation au passage ; éviter toute formule dont le sens serait ambigu pour un lecteur non corsophone.
- [ ] **Framing** — appliquer la règle : fait fort → conséquence → borne ; éviter le defensive-first.
- [ ] **Estimations** — éviter les décimales dans le framing lorsqu'elles créent une fausse précision ; conserver l'exact dans les annexes.
- [ ] **Traçabilité** — conserver pour chaque nouvelle source le lien, la date, l'auteur, le statut de vérification et l'usage exact envisagé.
- [ ] **Sources Web mutables** — lorsqu'une URL sert matériellement de preuve, conserver si possible une copie figée du contenu pertinent, avec date de capture et SHA-256 ; l'URL seule ne constitue pas une archive stable.

## C. CEDH — CHECKLIST DE PRÉSERVATION DU GRIEF

Ces points ne remplacent pas le dépôt au Conseil constitutionnel. Ils servent à éviter qu'une future voie européenne soit affaiblie aujourd'hui par omission.

### MUST BEFORE FILING AU CONSEIL CONSTITUTIONNEL

- [ ] **Soulever en substance le grief conventionnel pertinent** — faire apparaître dans la requête nationale, sans transformer celle-ci en requête CEDH, la substance du droit invoqué : droit de se porter candidat et effectivité du recours électoral au titre de l'article 3 du Protocole n° 1.
- [ ] **Ne pas surcharger l'article 13** — le traiter, s'il est maintenu, comme grief conventionnel distinct à vérifier ; ne pas supposer qu'il ajoute automatiquement une garantie autonome à celle que la jurisprudence déduit déjà de l'article 3 du Protocole n° 1.
- [ ] **Article 14 / handicap** — ne l'ouvrir que si le dossier permet d'identifier un traitement défavorable suffisamment rattachable à un critère protégé et au champ d'un droit conventionnel ; conserver séparément les faits d'accessibilité et la qualification de discrimination.
- [ ] **Applicabilité au Sénat** — documenter que l'article 3 du Protocole n° 1 couvre le choix de la législature et peut s'appliquer à une chambre haute disposant de pouvoirs législatifs ; ne pas traiter ce point comme acquis par simple analogie.
- [ ] **Épuisement utile** — identifier les recours internes **normaux et effectifs** pour chaque grief. Ne pas croire qu'une démarche extraordinaire, discrétionnaire ou dépourvue de pouvoir de redressement prolonge le délai de Strasbourg.
- [ ] **Défenseur des droits ≠ suspension du délai CEDH** — le mobiliser pour documenter, recommander, intervenir ou qualifier une difficulté ; ne jamais lui attribuer un effet interruptif ou suspensif sur le délai européen.
- [ ] **2017 / 2024** — les conserver comme contexte de répétition et éléments de connaissance institutionnelle ; ne pas les présenter comme rouvrant le délai de quatre mois d'une décision ancienne.
- [ ] **2024 hors délai autonome** — à défaut d'un fondement exceptionnel précis et vérifié, traiter la contestation autonome de la décision 2024 comme hors délai CEDH.
- [ ] **2026 : point de départ à calculer après la décision finale pertinente** — ne pas pré-calculer aujourd'hui une date de Strasbourg ; enregistrer exactement la date de la décision définitive et, le cas échéant, sa date de notification.
- [ ] **Formulaire complet** — rappeler que seul l'envoi d'une requête complète conforme aux exigences de la Cour interrompt le délai de quatre mois ; une lettre d'intention ou une démarche incomplète ne doit pas être utilisée comme filet de sécurité.
- [ ] **Même grief, même substance** — conserver la trace de l'endroit où chaque grief conventionnel a été soulevé devant le juge national afin de pouvoir démontrer l'épuisement.
- [ ] **Qualité de victime** — après décision nationale, vérifier séparément que le requérant demeure directement affecté par chaque violation alléguée et qu'aucun remède national n'a effacé cette qualité.
- [ ] **Remède demandé à Strasbourg** — ne pas présenter la CEDH comme pouvant "proclamer un sénateur". Distinguer constat de violation, satisfaction équitable éventuelle et mesures générales/individuelles relevant ensuite de l'exécution.
- [ ] **Réponse du Réel** — si Strasbourg rejette pour irrecevabilité, classer la cause exacte : délai, non-épuisement, incompatibilité ratione materiae/personae, défaut manifeste de fondement, absence de désavantage significatif, autre. Ne jamais convertir une irrecevabilité en validation du fond.

### POST-DÉCISION DU CONSEIL CONSTITUTIONNEL

- [ ] Geler immédiatement la décision, sa date de publication, sa date de notification éventuelle et le dossier national réellement examiné.
- [ ] Dresser une matrice **grief CEDH → fait → norme → endroit où le grief a été soulevé en France → réponse nationale → résidu**.
- [ ] Calculer le délai de quatre mois **par grief**, à partir de la décision finale pertinente dans le processus d'épuisement.
- [ ] Vérifier si un recours supplémentaire invoqué est réellement normal et effectif avant de considérer qu'il retarde le point de départ.
- [ ] Préparer le formulaire Rule 47 et les annexes suffisamment tôt pour qu'une requête complète parte avant l'échéance, sans compter sur un week-end ou un jour férié pour prolonger le délai.
- [ ] Séparer clairement : **2026 = objet potentiel de la requête** ; **2017/2024 = contexte, répétition, connaissance, éventuellement preuve de pattern**, sauf grief autonome encore recevable démontré.


## D. POST-FILING / NEXT REALITY TESTS

- [ ] Enregistrer la preuve du dépôt : date, heure, canal, récépissé / accusé, version exacte, liste exacte des pièces.
- [ ] Geler une copie forensique de la requête déposée et du bordereau.
- [ ] Distinguer toute version ultérieure de la version déposée.
- [ ] Suivre les mesures d'instruction, observations adverses et demandes du Conseil.
- [ ] Mettre à jour la matrice : `NEW TRACE → confirme → infirme → OPEN → documents modifiés`.
- [ ] Après décision nationale définitive, réévaluer séparément toute voie CEDH et calculer son délai propre.
- [ ] En cas de rejet, classer précisément : recevabilité, absence d'influence, fond, office, preuve, autre.
- [ ] En cas d'accueil partiel ou total, cartographier immédiatement les conséquences et voies possibles pour chaque partie.

## E. Règle agile

Un point découvert en chemin n'a pas besoin d'attendre la prochaine "grande version".

S'il est matériel et vérifiable :

> **on l'ajoute, on le relie, on le qualifie, puis on le ferme quand la Réalité a répondu.**


## UPDATE — 6 octobre 2026 — v0.9

- brouillon courant promu : `requete-conseil-constitutionnel-projet-v0.9.md` ;
- correction matérielle : la QPC est directement possible à l'occasion du contentieux électoral parlementaire devant le Conseil constitutionnel ; le verrou n'est donc plus l'instance mais la **qualité juridique de chaque question** ;
- QPC A : `L.299` devient le premier candidat à tester dans un mémoire distinct ;
- QPC B : non cristallisée à ce stade ;
- proclamation directe : désormais conclusion **infiniment subsidiaire**, explicitement exploratoire, à revoir avant dépôt.

## UPDATE — 6 octobre 2026 — lisibilité double public / juriste junior

- ajout d'un contrôle d'intelligibilité grand public ;
- ajout d'un contrôle d'intelligibilité pour un juriste junior du Conseil constitutionnel ;
- ces deux contrôles sont classés **MUST BEFORE FILING** : la requête doit être simultanément compréhensible sans jargon inutile et navigable juridiquement sans connaissance préalable du Corpus.


## UPDATE — 6 octobre 2026 — v0.10 / annexe P-41

- brouillon courant promu : `requete-conseil-constitutionnel-projet-v0.10.md` ;
- bordereau courant : `bordereau-pieces-requete-conseil-constitutionnel-v0.8.md` ;
- création de P-41 : annexe ciblée de déclarations publiques et commentaires de presse contemporains ;
- règle de crible : conserver les sources favorables **et** le framing adverse ; distinguer acteur / journaliste / résultat primaire / inférence ;
- point de vigilance renforcé : « cinq grands électeurs » désigne une **base institutionnelle minimale directement identifiable**, jamais l'ensemble des soutiens publics ni cinq bulletins attribuables ;
- avant dépôt, décider si P-41 est effectivement jointe ou reste une pièce de soutien/réserve.


## UPDATE — 6 octobre 2026 — répétition, médias, effectivité, Corse laboratoire

- ouverture d'un comparatif longitudinal **2017 / 2020 / 2024 / 2026** de la couverture du service public et de la couverture médiatique générale, avec comparateurs parmi les petites candidatures ;
- ajout d'une analyse séparée de la **forme** et du **fond** des quatre candidatures afin de mesurer les écarts entre offre réellement formulée et présentation médiatique ;
- traces institutionnelles confirmées : CSA ticket **227435** (2017) et Arcom alerte **807989** (2024) ; aucune réponse de fond retrouvée sous ces identifiants dans la recherche Gmail ciblée au 6 octobre ;
- l'hypothèse « droit décoratif / droit effectif » devient une **hypothèse à tester par chaîne d'effectivité**, pas une conclusion présupposée ;
- ancrage historique confirmé par une source parlementaire : la Corse est explicitement décrite comme **« laboratoire de la décentralisation »** pour la séquence ouverte en 1982 ;
- la généralisation « de nombreuses innovations corses ont ensuite été reprises ailleurs » reste à démontrer cas par cas ; ne pas sur-vendre ce point avant inventaire.


## UPDATE — 6 octobre 2026 — v0.8 / plateau pré-dépôt

- brouillon courant : `requete-conseil-constitutionnel-projet-v0.17.md` ;
- découverte load-bearing : **les griefs nouveaux sont forclos après le délai de l’article 33** ; toutes les branches matérielles doivent donc être présentes en substance dans la requête initiale ;
- distinction durcie : article 35 = délai exceptionnel pour certaines **pièces**, pas réserve générale de moyens ;
- canal de dépôt de l’article 34 ajouté comme contrôle opérationnel prioritaire ;
- grief L.299 recentré sur le texte réel + exception handicap, et non sur une équivalence simpliste papier/numérique ;
- calendrier sénatorial exact intégré : 7 / 21 / 26 octobre ;
- QPC soumises à un **kill-switch de qualité** : aucune QPC de remplissage ;
- CEDH : répétition ≠ situation continue ; qualité de victime Robert/Vernerey à cartographier ;
- à ce stade, les gains restants sont surtout matériels : dépôt, bordereau, pièces, QPC A éventuelle et revue adverse finale.


## UPDATE — 6 octobre 2026 — CEDH / boucle vers le plateau

- le volet CEDH est désormais traité comme une **préservation de griefs dès le dépôt national**, non comme un travail à commencer après coup ;
- la règle des quatre mois est couplée à l'épuisement des seuls recours **normaux et effectifs** : une démarche extraordinaire ou sans pouvoir de redressement ne sert pas à étirer le délai ;
- la saisine du Défenseur des droits est utile comme probe et source institutionnelle, mais n'interrompt pas le délai CEDH ;
- 2017 et 2024 servent d'abord à tester la **répétition** et la connaissance du problème ; ils ne ressuscitent pas une requête autonome hors délai ;
- le plateau pré-dépôt sera atteint lorsque les nouvelles objections deviennent répétitives et qu'aucun point nouveau ne change matériellement recevabilité, grief, pièce, conclusion, QPC ou préservation CEDH.



## UPDATE — 6 octobre 2026 — style, audace et lisibilité publique

- conservation verbatim demandée pour l'ouverture possible : **« Obtenir le respect, en Corse comme ailleurs, réclame d'en manifester ; le mépris appelle le mépris ».** ;
- ajout d'un contrôle **style / panache sans perte probatoire** : références historiques et proverbes peuvent rythmer le texte s'ils servent une idée et restent séparés de la démonstration juridique ;
- Danton : formulation de référence « de l'audace, encore de l'audace, toujours de l'audace » ;
- Talleyrand : l'explicitation reste un principe de lisibilité et de FractaCognition ;
- toute formule corse doit être vérifiée avant insertion afin d'éviter un effet de style au prix d'une ambiguïté de sens.

## UPDATE — 6 octobre 2026 — v0.11 / corpus courriels

- brouillon courant : `requete-conseil-constitutionnel-projet-v0.11.md` ;
- bordereau courant : `bordereau-pieces-requete-conseil-constitutionnel-v0.8.md` ;
- ajout **P-42** : saisine Défenseur des droits et suivi vérifié ;
- ajout **P-43** : index probatoire de la correspondance avec Laurence Vernerey ;
- règle nouvelle : **tout courriel matériellement pertinent doit être conservé et indexé ; tout courriel conservé n'a pas vocation à être annexé** ;
- priorité pré-dépôt : matérialiser les messages natifs effectivement cités dans la requête et vérifier qu'aucune pièce privée redondante n'alourdit le dossier.


## UPDATE — 6 octobre 2026 — FBF v0.9

Passe **Fix Bugs First** sur le paquet pré-dépôt :

- requête courante : `v0.17` ;
- bordereau courant : `v0.8` ;
- inventaire probatoire : aligné sur `v0.17` ;
- corrections des références résiduelles `v0.13` / `v0.11` / bordereau `v0.7` lorsqu’elles prétendaient décrire l’état courant ;
- contrôle mécanique du bordereau : séquence continue `P-01` à `P-43`, aucune pièce citée par la requête n’est absente du bordereau ;
- fermetures de checklist sur les points déjà effectivement résolus par la v0.14 : premier écran contentieux, statut du bulletin nul, architecture des conclusions, remedial probe, séparation Défenseur des droits, cadrage CEDH et symétrie conditionnelle.

Restent volontairement ouverts les points qui exigent un acte matériel ou une vérification du paquet réellement déposé : canal et preuve de dépôt, gel pré-dépôt, concordance exacte bordereau ↔ fichiers joints, lisibilité des pièces critiques, P-41, matérialisation P-21/P-29 à P-33, et revue adverse finale centrée sur les motifs de rejet.


## UPDATE — 6 octobre 2026 — plan de dépôt et revue de rejet

Objets ajoutés :

- `pre-filing-operational-plan-2026-10-07.md` — articles 33–35, canal légal, preuve de remise et marge opérationnelle ;
- `filing-package-manifest-2026-10-07.md` — distinction Corpus / bordereau / paquet matériel / paquet remis ;
- `../reviews/review_internal_requete_cc_motifs_rejet_2026-10-06.md` — revue interne corrélée centrée sur les voies de rejet.

Arbitrage P-41 : **soutien/réserve**, ne pas joindre par défaut au noyau initial.

La fermeture complète du dépôt reste impossible avant vérification matérielle des pièces et obtention de la preuve réelle de remise.


## UPDATE — 6 octobre 2026 — v0.10 / vidéo, consentement et traçabilité

- ajout du contrôle de la **diligence Bastia → Ajaccio** du 11 septembre, à documenter par traces disponibles ;
- ajout d’un contrôle de **transcription exacte de P-13**, afin que le contenu probatoire de la déclaration commune soit immédiatement lisible ;
- ajout de la chaîne de demandes **14–18 septembre** portant spécifiquement sur la réception, le versement et le traitement du courriel de 17 h 57 / vidéo, avant les relances des 25 septembre, 1er et 2 octobre ;
- ajout du triptyque **produite/envoyée → reçue/versée → effectivement examinée**, avec interdiction de transformer une inconnue en fait négatif acquis ;
- ajout d’un contrôle des **diligences cumulatives** destinées à garantir l’authenticité du consentement de la remplaçante ;
- ajout du **biais de cadrage / propagation de prémisse** comme test institutionnel et non psychologique ;
- ajout du **test de cohérence candidat/remplaçante**, articulé à L.298, L.299, au handicap et à CE, 14 mai 2021, n° 445497.


## UPDATE — 6 octobre 2026 — v0.11 / requêtes préfectorales et France Transfert

- synchronise la checklist avec la **requête v0.17** et le **bordereau v0.9** ;
- ferme la récupération et la comparaison des deux saisines préfectorales ;
- distingue explicitement **L.298/L.299 dans la saisine**, **L.298/L.299/L.301 dans le sens des conclusions e-Sagace**, et le contrôle encore à effectuer sur les motifs exacts du jugement primaire ;
- ajoute **P-44** comme chaîne de provenance France Transfert en deux courriels, avec règle de non-publication des secrets techniques ;
- maintient ouvert uniquement le travail matériel restant sur ce sous-front : contrôle primaire du jugement et matérialisation expurgée de P-44 dans le paquet de dépôt.

## UPDATE — 6 octobre 2026 — P-09 / P-17 : image primaire + transcription

- **P-09** : le récépissé provisoire ne doit pas être seulement cité ; le paquet de dépôt doit contenir son **scan lisible** et une **transcription textuelle vérifiée** ;
- **P-17** : la note manuscrite recto-verso remise à l'audience doit être produite sous les deux formes, **reproduction recto-verso + transcription textuelle** ;
- règle commune : l'image primaire fait foi ; toute transcription est dérivée et doit signaler ses incertitudes ; aucune lacune ne doit être comblée par inférence ;
- le texte exact de P-17 est à récupérer de la conversation contemporaine et/ou à vérifier sur le scan dès qu'il est retrouvé ;
- les scans du jugement du TA recherchés parallèlement feront l'objet du contrôle primaire déjà ouvert sur P-20.


## UPDATE — 7 octobre 2026 — redondance des canaux de dépôt

La stratégie de dépôt devient explicitement **redondante**, sous une contrainte d'identité stricte du paquet.

Source de travail : `matrice-canaux-materiels-depot-2026-10-07.md`.

Invariants ajoutés :

~~~text
plusieurs voies de remise
≠ plusieurs versions du recours

preuve d'expédition
≠ preuve de réception

courriel de copie
≠ saisine acquise

sous-préfecture
≠ représentant de l'État sans confirmation
~~~

Priorité opérationnelle :
1. remise physique anticipée à la préfecture de Bastia avec récépissé horodaté ;
2. si matériellement possible, remise directe redondante du même paquet au Conseil constitutionnel à Paris ;
3. commissaire de justice / porteur comme renfort probatoire ;
4. copies numériques ou fax uniquement comme traces supplémentaires, jamais comme unique fondement de la saisine.

La jurisprudence retrouvée impose une prudence maximale sur le temps : le Conseil a déjà rejeté des requêtes en se fondant sur leur **date de réception** au secrétariat général, postérieure au délai.


## UPDATE — 7 octobre 2026 — P-45 / silence sur le canal de dépôt

Le brouillon courant devient **v0.18** et le bordereau courant **v0.10**.

Une nouvelle pièce composite **P-45** documente les demandes et relances sur la modalité pratique de dépôt :
- P-45.a — 26 septembre, Bureau des élections ;
- P-45.b — 28 septembre, Sous-préfecture de Corte ;
- P-45.c — 1er octobre, consolidation avec Sous-préfecture en copie ;
- P-45.d — 2 octobre, relance P1–P18 avec P11/P12.

Règle : les quatre courriels doivent être **produits intégralement** dans le paquet juridictionnel, pas seulement résumés. Le Corpus public conserve un index minimisé ; les messages natifs restent la preuve primaire.

Qualification : documenter un **silence procédural ciblé** sur le canal de dépôt malgré des relances multiples, sans transformer ce silence en preuve d'intention ni en affirmation d'absence générale de réponse de l'État.


## UPDATE — 7 octobre 2026 — v0.15 / handoff et chaîne postale

- croisement du handoff `reprise-senatoriales-cc-2026-10-07.md` avec l'état courant du Corpus ;
- ajout des contrôles P-09, P-13, P-17 et P-20 issus de ce croisement ;
- adresse officielle du bureau La Poste CORTE vérifiée : **Avenue du Baron Mariani, 20250 Corte** ;
- ajout du témoignage précis du requérant : photographie de la plaque prise en sortant du bureau après retrait du courrier recommandé de notification du jugement ;
- ajout du manifeste forensique, de la conservation des originaux/expurgés, du gel des sources Web mutables, de la marge opérationnelle et du FBF des pointeurs de versions courantes.


## UPDATE — 7 octobre 2026 — protocole de constitution et annexe chronologique

Deux contrôles deviennent MUST BEFORE FILING :

1. **protocole de constitution** : aucune version ne peut être promue sans synchronisation de la requête, de la chronologie, du bordereau, de l'inventaire, de Gmail et des sources juridiques ;
2. **chronologie détaillée annexée** : jour par jour, heure croissante, depuis le premier courriel à la préfecture du 10 septembre à 17:01:56 jusqu'au dépôt effectif.

Un registre d'audit Gmail différentiel est créé pour éviter qu'un message matériel reste hors du dossier. Les messages pertinents ne sont pas automatiquement tous produits : chacun doit être classé INCLUDE / RÉSERVE / EXCLURE avec motif / REVIEW.


## UPDATE — 7 octobre 2026 — control/data plane, dématérialisation et double lecture

Le dossier est désormais explicitement structuré en deux plans :

~~~text
CONTROL PLANE = checklist / protocoles / audits / règles de gel / routage
DATA PLANE    = requête / annexes / pièces / fichiers / preuves / remises
~~~

Cette séparation est une application directe de la tradition control/data plane du Corpus et de FractaCognition.

Trois nouveaux MUST :
1. **dépôt dématérialisé redondant**, fondé sur l’art. 34 et étudié à la lumière du CRPA L.112-8 et suivants, sans en faire l’unique voie tant que l’applicabilité spéciale n’est pas confirmée ;
2. **double lecture grand public / expert dans chaque grande section** ;
3. **complétude initiale maximale raisonnable**, car les griefs nouveaux tardifs sont exposés à l’irrecevabilité et l’art. 35 ne garantit aucun complément général après délai.

L’audit de la v0.19 conclut que la double lecture n’est **pas encore satisfaite partout** : point bloquant avant gel.


## UPDATE — 7 octobre 2026 — P-20 / borne ante quem conversationnelle

- ajout d'une trace indépendante de disponibilité de l'image : photographie déjà transmise à ChatGPT au plus tard le **25 septembre 2026 à 15 h 17 CEST** ;
- qualification stricte : borne ante quem de possession/transmission, pas horodatage de prise de vue.


## UPDATE — 7 octobre 2026 — fonction de la photo « Avenue du Baron Mariani »

- recentre la fonction de la photographie : non pas dater prioritairement le retrait postal, mais donner un repère matériel simple montrant l'ancrage public/local de la désignation « Baron Mariani » ;
- borne explicite : la toponymie publique ne prouve ni titre nobiliaire personnel ni généalogie ; ces questions restent distinctes et réclameraient leurs propres preuves si elles devenaient matérielles.


## UPDATE — 7 octobre 2026 — v0.21 / boucle v0.23

- corrige les pointeurs courants vers la candidate de dépôt **v0.23** ;
- sépare plus strictement data plane et control plane : retrait de la check-list Cognitive Packet, du protocole de revue et des changelogs du corps de la requête ;
- réintroduit **L.318** de manière bornée dans le grief d'incidence, sans inférence sur le vote individuel ;
- propage le rôle exact de la photographie « Avenue du Baron Mariani » et sa borne ante quem ;
- effectue une micro-passe d'intelligibilité sur des pronoms ambigus ;
- conserve la matérialisation du paquet, le gel et la preuve de réception comme principaux points restant à achever.


## UPDATE — 7 octobre 2026 — v0.22 / contrôle pièce par pièce lisible

Le contrôle matériel des pièces adopte une règle de lecture obligatoire : **un numéro de pièce ne doit jamais devenir un code que le lecteur est supposé connaître par cœur**.

Pour chaque pièce P-xx, le control plane conserve désormais deux informations immédiatement lisibles :

1. **Ce que c’est** — description courte, concrète, datée et sourcée de l’objet ;
2. **Sa place dans le raisonnement** — ce que la pièce permet d’établir, où elle intervient dans la chaîne argumentative, ce qu’elle ne permet pas d’inférer, et son niveau de production (noyau / soutien / contexte-réserve / sensible).

Exemple de forme attendue :

~~~text
P-14 — requêtes préfectorales n° 2601714 et 2601715 + bundles TA
Ce que c’est : ...
Place dans le raisonnement : ...
~~~

Cette règle vaut pour le contrôle pièce par pièce, le bordereau, les revues et les explications destinées à un humain. Elle ne change ni la numérotation P-xx ni le statut matériel des pièces et **n’emporte aucun gel du paquet de dépôt**.


## UPDATE — 7 octobre 2026 — v0.23 / autoportance historique

La double lecture est désormais explicitement comprise comme une architecture à **trois horizons de lecture** : grand public contemporain, expert/juridiction, lecteur historique futur.

Nouvel invariant : la valeur d'une pièce ne se réduit pas à sa force probatoire immédiate ni à la décision de la joindre matériellement. Le contrôle doit distinguer **portée contentieuse**, **fonction dans le raisonnement**, **valeur historique/documentaire** et **décision de production**.

La requête v0.24 reçoit une note de lecture bornée : elle affirme son ambition d'être aussi autoporteuse que possible et de documenter intelligiblement la séquence corse de 2026, tout en précisant que cette ambition n'ajoute aucun grief et ne demande pas au Conseil de statuer sur une interprétation historique.


## UPDATE — 7 octobre 2026 — v0.24 / double horizon contentieux

Le control plane formalise désormais deux objectifs parallèles :

- **Conseil constitutionnel** : contester l'élection sénatoriale du 27 septembre 2026 et le refus d'enregistrement dans le cadre de L.303 ;
- **CEDH** : préserver et préparer dès maintenant un éventuel recours européen ultérieur.

Règle de séparation : aucun développement CEDH ne doit encombrer la requête nationale s'il n'y sert aucun moyen recevable ; inversement, aucune trace potentiellement utile à Strasbourg ne doit être perdue au seul motif qu'elle est périphérique pour le Conseil constitutionnel.

La série alléguée **2017 → 2020 → 2024 → 2026** sur le traitement médiatique devient un axe longitudinal à documenter, avec séparation stricte entre faits observés, comparaison, causalité alléguée, atteinte à la réputation, préjudice moral et éventuelle réparation.


## UPDATE — 7 octobre 2026 — v0.25 / résultats rapportés au collège électoral

Nouvel invariant de présentation : pour les votes, résultats, blancs, nuls, exprimés et ordres de grandeur électoraux, afficher **d'abord le pourcentage du collège électoral total**, puis la valeur absolue. Cette convention est motivée par le caractère juridiquement contraint de la participation sénatoriale (art. L.318).

Audit de la v0.24 : plusieurs passages restent à corriger lors de la prochaine promotion, notamment les formulations commençant par **442 voix**, **88 voix**, **36 blancs**, **40 nuls**, le résumé P-27 et certains développements sur l'incidence. La note `investigation/contre_cela_naurait_rien_change_2026-10-02.md` et plusieurs passages de la v0.24 respectent déjà la convention.

Exception : lorsqu'un seuil légal est défini sur les suffrages exprimés, conserver le dénominateur juridiquement pertinent et donner en complément, si utile, son équivalent rapporté au collège.


## UPDATE — 7 octobre 2026 — v0.26 / précédence sémantique

Ajout d'un invariant de lecture séquentielle : **aucun référent ne doit “tomber du ciel”**.

Audit initial de la requête v0.24 : le passage d'incidence situé avant la chronologie contient plusieurs cas à corriger lors de la prochaine promotion, notamment :
- « sa base institutionnelle directement identifiable » sans introduction préalable de cette base ;
- « soutien public visible » sans avoir encore exposé ce soutien ;
- « ces éléments » alors que les éléments pertinents ne sont pas tous définis au même niveau ;
- plus largement, plusieurs démonstratifs ou raccourcis (« cette offre », « cette pièce », « ce contexte », « cette séquence ») doivent être contrôlés phrase par phrase.

La correction ne consiste pas seulement à remplacer des pronoms : l'ordre des informations doit être restructuré lorsqu'une prémisse apparaît après la conclusion qu'elle est censée rendre intelligible.


## UPDATE — 7 octobre 2026 — v0.27 / français d'abord

Nouvel invariant linguistique : tout terme anglais conservé pour sa valeur technique doit être immédiatement traduit en français.

Exemple canonique : **UNKNOWN (inconnu)**.

Cette règle vaut pour la requête, les annexes, les tableaux, les statuts probatoires, les documents de contrôle et les explications destinées au lecteur. Les termes anglais peuvent rester lorsqu'ils constituent une convention technique utile, mais ils ne doivent jamais être supposés compris sans traduction.


## UPDATE — 7 octobre 2026 — v0.28 / méthode interne hors requête

Nouvel invariant : la requête doit montrer le **résultat** du travail de contrôle, pas expliquer son moteur interne.

Correction différée identifiée dans la v0.24 : supprimer notamment **« Talleyrand appliqué : lorsqu'une heure n'est pas établie, le document le dit. Il ne demande jamais au lecteur de l'inférer silencieusement. »** et reformuler uniquement le constat utile.

Audit à effectuer lors de la prochaine promotion : rechercher dans toute la requête les mentions de Talleyrand, FractaCognition, control/data plane, protocoles, audits, règles de rédaction, commentaires métatextuels et autres traces du processus de fabrication ; ne conserver que ce qui est matériellement nécessaire à la compréhension, à la preuve ou au contradictoire.


## UPDATE — 7 octobre 2026 — v0.29 / suppression des marqueurs de progression interne

Ajout d'un invariant : la requête expose l'état du dossier, pas l'histoire de sa fabrication.

Audit initial de la v0.24 : plusieurs occurrences doivent être corrigées lors de la prochaine promotion, notamment :
- « Inventaire initial désormais établi par P-14 » ;
- « la provenance ... est désormais documentée plus finement » ;
- « l'inventaire ... est désormais établi grâce à P-14 » ;
- « P-14 permet désormais d'établir ... » ;
- ainsi que d'autres « désormais / maintenant / actuellement » qui doivent être distingués selon qu'ils décrivent l'affaire ou seulement l'évolution de notre connaissance.

La correction attendue est généralement une formulation directe au présent : **« P-14 établit... »**, **« la provenance est documentée par... »**, etc.


## UPDATE — 7 octobre 2026 — requête v0.25 / premier paquet de corrections appliqué

Première passe appliquée à la requête sans gel :
- adresse de procédure remplacée par `jeanhuguesrobert@gmail.com` ;
- suppression de l'affirmation erronée selon laquelle le requérant serait grand électeur / membre du collège électoral ; qualité pour agir recentrée sur la personne ayant fait acte de candidature ;
- résultats électoraux reformulés avec pourcentage du collège d'abord, valeur absolue ensuite ;
- comparateur Battini introduit avant la conclusion « soutien public visible ≠ vote secret » ;
- `UNKNOWN` devient `UNKNOWN (inconnu)` ;
- suppression de « Talleyrand appliqué » et d'autres commentaires sur la fabrication du document ;
- suppression ou neutralisation des marqueurs `désormais / maintenant / à ce stade` lorsqu'ils ne décrivaient que l'évolution de notre connaissance ;
- remplacement de `bundle` par une formulation française dans le corps du texte ;
- retrait du mécanisme interne d'audit Gmail de la requête.

Cette promotion reste une version de travail ; d'autres paquets de corrections peuvent être intégrés avant tout gel.

## UPDATE — 7 octobre 2026 — v0.30 / force argumentative

Nouvel invariant : la requête ne doit pas affaiblir spontanément ses propres moyens par des précautions rhétoriques redondantes. Les limites réellement nécessaires sont conservées ; les atténuations qui relèvent de l'appréciation du juge sont retirées. La revue critique reste dans le plan de contrôle et fait l'objet d'un signalement au requérant lorsqu'une affirmation paraît excessive ou fragile.


## UPDATE — 7 octobre 2026 — v0.31 / français idiomatique

Ajout d'un invariant : la requête ne doit contenir aucun calque littéral produisant un français artificiel. L'expression « chaîne de colis » est supprimée et remplacée par une formulation naturelle décrivant le trajet des documents.

Audit à poursuivre sur les expressions techniques ou conceptuelles qui pourraient rester opaques au lecteur, notamment lorsqu'elles sont compréhensibles pour l'auteur mais pas pour un lecteur extérieur.


## UPDATE — 7 octobre 2026 — v0.32 / textualité, style et traçabilité

Le plan de contrôle formalise trois exigences supplémentaires : textualité complète sans artifice graphique nécessaire au sens ; style narratif et littéraire ; qualification précise des réponses institutionnelles.

La Traçabilité des Actes est désormais une grille transversale du dossier, y compris pour les modalités de remise du recours. Elle doit rester concrète, symétrique et vérifiable, et ne vaut jamais attribution automatique d'une intention.


## UPDATE — 7 octobre 2026 — v0.33 / tableaux et schémas comme vues annexes

Nouvel invariant : les tableaux et schémas quittent le corps de la requête lorsqu'ils servent seulement à présenter plus efficacement une matière déjà exposée.

Le corps contient toujours l'équivalent sémantique complet en texte continu. Les annexes peuvent fournir des vues tabulaires ou graphiques, sans ajouter de contenu nouveau.

Cette règle s'applique à tous les tableaux et schémas actuels et futurs de la requête.


## UPDATE — 7 octobre 2026 — v0.34 / questions sans réponse

Ajout d'un exemple explicite à la règle de français idiomatique : éviter le calque « question restée ouverte » lorsqu'il signifie en réalité qu'une question est restée sans réponse suffisante, n'a reçu qu'une réponse partielle ou demeure non résolue.


## UPDATE — 7 octobre 2026 — v0.35 / références de pièces autoporteuses

Nouvel invariant : chaque référence documentaire associe le numéro de pièce et son libellé intelligible. La règle vaut dans les deux sens : aucun numéro isolé lorsque son contenu n'est pas immédiatement connu, et aucun libellé d'une pièce identifiée sans son numéro. Une passe exhaustive doit harmoniser la requête, le bordereau et les annexes.


## UPDATE — 7 octobre 2026 — v0.36 / libellés de pièces vivants

Les numéros de pièces restent stables, mais leurs libellés peuvent et doivent être améliorés lorsqu'une formulation plus claire rend le dossier plus facile à comprendre. Toute amélioration doit ensuite être propagée dans tous les documents qui référencent la pièce.


## UPDATE — 7 octobre 2026 — v0.37 / principe général d'agilité

Le plan de contrôle explicite une règle plus générale : aucune convention passée n'est intangible par inertie. Lorsqu'un changement améliore réellement le dossier, il doit pouvoir être fait et propagé, même si cela représente du travail. L'historique utile et les identifiants stables sont préservés afin que l'agilité ne devienne jamais une réécriture silencieuse du passé.


## UPDATE — 7 octobre 2026 — v0.38 / suppression des traces de fabrication

Les références aux versions internes de la requête et aux étapes de rédaction sont interdites dans le corps juridictionnel. Le texte expose directement l'état courant du raisonnement ; l'historique de fabrication reste dans le plan de contrôle et dans Git.


## UPDATE — 7 octobre 2026 — v0.40 / liens directement utilisables

Ajout d'une règle d'ergonomie : lorsqu'un document GitHub est proposé à la lecture, fournir systématiquement son URL complète et cliquable. Un chemin de fichier ou une référence technique peut compléter le lien, mais ne doit jamais le remplacer.


## UPDATE — 7 octobre 2026 — v0.41 / référence stable et QPC nommées

La requête courante est désormais référencée par le chemin stable `requete-conseil-constitutionnel.md`. Les anciennes désignations QPC A / QPC B sont remplacées par des intitulés intelligibles fondés sur les articles L.303 et L.299 et leur objet constitutionnel.


## UPDATE — 7 octobre 2026 — v0.42 / QPC constitutives du dépôt final

Les deux QPC L.303 et L.299 doivent être effectivement soulevées dans la requête adressée au Conseil constitutionnel et déposées simultanément sous forme de mémoires distincts et motivés. Elles ne sont plus traitées comme de simples pistes extérieures au paquet final.


## UPDATE — 7 octobre 2026 — v0.43 / préservation CEDH structurée

Ajout d'une règle de préservation conventionnelle : la requête nationale doit contenir au moins en substance les griefs susceptibles d'être ultérieurement portés à Strasbourg. Les axes conservés sont l'article 3 du Protocole n° 1, l'article 13 combiné avec celui-ci, et l'article 14 combiné avec celui-ci pour le handicap. La matrice dédiée fixe également les exigences d'épuisement, de qualité de victime, de délai de quatre mois et de formulaire Rule 47.


## UPDATE — 7 octobre 2026 — v0.44 / couplage control plane ↔ data plane

Ajout d'un invariant métacognitif issu d'un incident concret : une formulation déjà interdite par la checklist locale (« question ouverte » employée au sens de question non résolue) a été réintroduite parce que le plan de contrôle local n'avait pas été rechargé avant rédaction.

La correction ne porte donc pas seulement sur le vocabulaire. Elle formalise la règle générale :

> **Toute action dans le data plane doit être guidée par les règles du control plane pertinent.**

Application locale obligatoire : **charger le control plane local avant d'agir, produire, relire contre ce control plane, puis élargir seulement si nécessaire**. Une règle locale qui aurait empêché une erreur mais n'a pas été activée signale une **défaillance d'activation du control plane**.

Cette règle est explicitement rapprochée du couple **cognition / métacognition** et du principe de localité de FractaCognition, sans transformer cette analogie fonctionnelle en identité rigide.


## UPDATE — 7 octobre 2026 — v0.47 / conservation sémantique

Ajout d'une règle explicite de non-régression : les passes d'intelligibilité doivent conserver intégralement le sens. Un audit rétrospectif des versions 0.20, 0.23, 0.26, 0.27 et de la requête stable identifie les pertes ou affaiblissements et documente leur restauration.


## UPDATE — 7 octobre 2026 — v0.45 / gel PDF et Release immuable

Ajout du protocole de matérialisation du dossier final : les sources et le contrat d'assemblage sont versionnés ; les rendus intermédiaires restent éphémères ; un seul PDF validé peut être promu dans une GitHub Release d'abord en brouillon puis, après contrôle terminal, publiée sous régime d'immutabilité. Le contrôle exige l'égalité SHA-256 avant upload, après retéléchargement du brouillon et après publication.


## UPDATE — 7 octobre 2026 — v0.48 / crible de conformité

Le crible de la requête stable a révélé plusieurs divergences du control plane lui-même : pointeurs v0.23 encore présentés comme courants, anciennes désignations QPC A/B et exigence devenue obsolète de rubriques mécaniques « Grand public / Expert ». Les règles actives sont réalignées sur la référence stable, les deux QPC nommées et le principe d'intelligibilité sans perte sémantique.


## UPDATE — 7 octobre 2026 — v0.49 / mémoires QPC distincts

Création de deux mémoires distincts et motivés candidats au dépôt :
- `qpc/memoire-qpc-l303-garanties-juridictionnelles.md` ;
- `qpc/memoire-qpc-l299-formalisme-candidature-empechement-remplacant.md`.

Les anciennes notes QPC restent des dossiers de recherche. Les mémoires deviennent les objets à contrôler pour le paquet final.


## UPDATE — 7 octobre 2026 — v0.51 / gate terminal de contrôle des sorties

Ajout d'un gate terminal obligatoire : toute sortie candidate est relue contre le control plane local avant émission. Les références documentaires doivent notamment être résolues sous la forme **numéro + libellé intelligible** ; un identifiant nu comme `P-46` est interdit lorsqu'un libellé canonique est disponible. L'incident ayant motivé cette correction est classé comme **défaillance d'activation du control plane au stade de sortie**.
