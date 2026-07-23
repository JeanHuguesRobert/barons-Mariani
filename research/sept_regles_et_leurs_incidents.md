---
title: "Sept règles et leurs incidents"
subtitle: "Complément opératoire à la Seconde Méthode"
description: "Règles de travail dégagées lors de la session des 20-22 juillet 2026, chacune rattachée à l'échec documenté qui l'a produite. Conservation du retour négatif appliquée à la méthode elle-même."
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A."
email: "jhr@baronsmariani.org"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/sept_regles_et_leurs_incidents.md"
version: "0.1"
status: "note de travail"
date: "2026-07-22"
last_modified_at: "2026-07-22"
license: "CC BY-SA 4.0"
document_role: "source"
document_kind: "research-note"
visibility: "public"
lifecycle_state: "working"
tags: [seconde-methode, potentics, methode, retour-negatif]
related:
  - "research/second_method.md"
  - "research/potentics.md"
  - "https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/CPKT-2026-001_c11_substitution.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/corpus_navigation_audit.md"
---

# Sept règles et leurs incidents

## Complément opératoire à la Seconde Méthode

Potentics pose que l'échec documenté a la même valeur épistémique que le succès. La Seconde Méthode ajoute que la méthode académique néglige le retour négatif, et que cette négligence fait rejouer les mêmes impasses. Cette note applique le principe à la conduite du travail : sept règles, chacune attachée à l'incident qui l'a produite au cours d'une seule session de travail humain-IA, les 20-22 juillet 2026. Aucune n'est déduite ; toutes sont payées.

L'ordre est celui de leur découverte.

---

### 1. Choisir le protocole de verrouillage d'après le coût du rollback

**Incident.** La publication d'un article a été bloquée en attente d'une autorisation d'attribution, alors que l'information n'avait jamais été marquée confidentielle et portait sur une architecture publiée.

**Règle.** Le verrouillage pessimiste — obtenir l'accord, puis écrire — ne s'impose que là où l'annulation est impossible ou coûteuse : un texte figé, une soumission à revue, une décision irréversible. Sur un document vivant, où corriger coûte un commit, le verrouillage optimiste est la bonne stratégie : publier, signaler à la personne citée, ouvrir une voie de contestation, corriger sur demande. Le modèle des documents vivants ne fait pas que tolérer l'optimisme, il le rend rationnel.

**Contre-emploi.** Demander d'abord là où corriger ne coûte rien n'est pas de la prudence : c'est de la lenteur déguisée en scrupule.

---

### 2. Aucune pièce porteuse ne repose sur un témoignage privé invérifiable

**Incident.** Un fait historique inédit, obtenu par correspondance privée, se retrouvait au fondement d'un argument de l'article. L'argument devenait donc révocable par une seule personne.

**Règle.** Séparer systématiquement deux couches. Ce que l'on peut reconstruire soi-même — inférence, raisonnement, lecture des sources publiées — porte l'argument, en nom propre, sans attribution. Ce que seul un témoin peut fournir vient ensuite corroborer, attribué. Si le témoin se rétracte, la corroboration tombe et la charpente tient.

---

### 3. L'attribution rend l'énoncé falsifiable

**Corollaire de la précédente, et sa justification profonde.**

Citer n'est pas seulement une politesse : « personal communication, 21 July 2026 » donne à un lecteur sceptique le moyen d'aller vérifier. Le même fait sans source est invérifiable, donc — au sens strict de Potentics — sans valeur épistémique. Le choix réel n'est jamais « citer ou s'approprier » : c'est **citer, ou ne pas dire**.

---

### 4. Tirer au sort quand les options sont équivalentes

**Règle.** Si deux options sont réellement équivalentes, l'espérance de gain d'une délibération supplémentaire est nulle et son coût ne l'est pas. Délibérer devient strictement perdant. Le tirage au sort est alors l'opérateur d'exploration correct quand le gradient est plat — c'est exactement ce que fait la nature.

**Précaution, qui est aussi un test gratuit.** Le tirage révèle la préférence cachée : si le résultat soulage ou déçoit, les options n'étaient pas équivalentes et l'on vient de découvrir le critère manquant. Obéir alors au sentiment, pas à la pièce. Une hésitation qui dure signale plus souvent un critère non trouvé qu'une véritable égalité.

**Condition de validité.** Le tirage n'est rationnel que couplé à la conservation des retours négatifs : il produit une donnée là où la délibération n'aurait produit qu'une opinion, à condition que l'échec revienne avec sa trace.

---

### 5. Ne jamais écrire sans version, ne jamais reconstruire de mémoire

**Incident.** Une section entière d'un document a été détruite par une substitution non vérifiée. La perte n'a été découverte que par hasard, et la section a d'abord été « restaurée » depuis le souvenir de l'avoir écrite — c'est-à-dire non restaurée, mais recomposée, sans preuve d'identité.

**Règle.** Toute écriture suit le cycle complet : lire l'état réel, écrire, **vérifier le différentiel**, valider. Sans version, pas de verrouillage optimiste possible — la stratégie de la règle 1 suppose qu'un conflit soit détectable. Et une reconstruction de mémoire n'est jamais une restauration : elle se déclare comme reconstruction, ou elle ment.

**Généralisation.** Ce qui n'est pas vérifié après écriture n'est pas écrit.

---

### 6. Inventorier l'état du destinataire avant d'empaqueter

**Incident.** Sept chantiers ont été rédigés comme s'ils étaient neufs. L'inventaire, fait ensuite, a montré que cinq d'entre eux existaient déjà, ouverts et dormants, dans le suivi de projet.

**Règle.** Un paquet destiné à un dépôt, une institution ou une personne s'empaquette après lecture de l'état courant de sa destination, jamais avant. Empaqueter sans lire le home, c'est produire des doublons et perdre le travail antérieur.

**Trouvaille latérale, plus précieuse que la règle.** La doctrine vivait dans les articles, l'implémentation dans le suivi de projet, et aucun des deux ne connaissait l'autre. L'inventaire n'a pas seulement évité des doublons : il a produit la jointure.

---

### 7. Une recherche tronquée qui s'ignore produit des faux négatifs confiants

**Incident.** Un document fondateur du corpus a été déclaré introuvable après une recherche dont la liste de résultats avait été tronquée sans que la troncature soit déclarée. Le document était trouvable depuis le début.

**Règle.** Toute recherche déclare sa frontière — ce qui a été cherché, où, et jusqu'où. Une absence n'est un résultat qu'à l'intérieur d'une frontière déclarée ; sans elle, « je n'ai pas trouvé » se déguise en « cela n'existe pas ». C'est la version élémentaire de l'exigence A1 des paquets cognitifs : distinguer « cherché, rien trouvé dans la frontière B » de « pas cherché ».

---

## Ce que cette note ne prétend pas

Ces règles ne sont ni originales ni complètes. Plusieurs sont connues sous d'autres noms — contrôle de concurrence, discipline de versionnement, déclaration de frontière de recherche. Leur intérêt n'est pas la nouveauté : c'est qu'elles ont chacune été payées d'un incident daté, dans un travail réel, et que l'incident est conservé avec la règle. Une règle sans son incident se discute ; une règle avec son incident se retient.

## Continuation

- Les règles 1, 5 et 7 sont mécanisables : un outil peut vérifier le différentiel, exiger une déclaration de frontière, refuser une écriture sans version. Les règles 2, 3 et 6 relèvent du jugement. La règle 4 est une politique. Cartographier lesquelles peuvent entrer dans l'outillage et lesquelles doivent rester dans la relecture humaine.
- Chaque nouvel incident documenté est candidat à une huitième règle. La note est vivante par construction : elle est le journal de retours négatifs de la méthode elle-même.
