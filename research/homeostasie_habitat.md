---
title: "Homéostasie de l’habitat"
subtitle: "Diagnostic, modes dégradés et agents IA pour l’autonomie domestique"
author: "Jean Hugues Noël Robert"
status: "draft"
version: "0.1"
date: "2026-06-20"
repository: "barons-Mariani"
path: "research/homeostasie_habitat.md"
type: "source_note"
language: "fr"
tags:
  - École Mariani de l’Autonomie
  - homéostasie
  - habitat
  - IA
  - diagnostic
  - capteurs
  - actionneurs
  - eau chaude
  - mode dégradé
  - autonomie de capacité
  - FractaVolta
corpus_hierarchy:
  level: "source_note"
  role: "note conceptuelle sur l’habitat comme système homéostatique"
  derived_from:
    - "research/ecole_mariani_autonomie.md"
    - "research/ecole_mariani_autonomie_terrains_pilotes.md"
    - "conversation ChatGPT du 2026-06-20 sur le cumulus comme inertie thermique pilotée"
  may_generate:
    - "fiche technique habitat homéostatique"
    - "module pédagogique diagnostic assisté par IA"
    - "fiche eau chaude en mode dégradé"
    - "article Substack sur l’homéostasie de l’habitat"
related_documents:
  - "research/ecole_mariani_autonomie.md"
  - "research/ecole_mariani_autonomie_terrains_pilotes.md"
  - "research/noyau_doctrinal_rendre_capable.md"
related_projects:
  - "École Mariani de l’Autonomie"
  - "FractaVolta"
  - "Cogentia"
  - "Paese Capace"
---

# Homéostasie de l’habitat

## Résumé

L’habitat peut être pensé comme un système homéostatique : il ne vise pas un confort parfait permanent, mais la conservation de fonctions vitales ou importantes dans des conditions changeantes.

Dans le cas de l’eau chaude, le mode dégradé ne doit pas être compris comme l’obligation de conserver à tout prix la température idéale. Le besoin primaire est d’avoir de l’eau. Si l’eau n’est pas à la bonne température pendant une panne brève, c’est gênant, mais ce n’est généralement pas critique.

Cette distinction est essentielle pour l’École Mariani de l’Autonomie : elle permet de hiérarchiser les fonctions, de distinguer panne critique et perte de confort, et de concevoir des systèmes plus simples, plus robustes et plus explicables.

Formule :

> L’homéostasie de l’habitat ne garantit pas le confort parfait. Elle garantit la continuité suffisante des fonctions importantes.

---

## 1. Principe

Un habitat autonome ou semi-autonome ne doit pas être évalué seulement par sa capacité à fonctionner comme un logement raccordé à des réseaux centralisés.

Il doit être évalué par sa capacité à maintenir des fonctions essentielles en conditions variables :

- eau disponible ;
- température acceptable ;
- éclairage minimal ;
- communication ;
- sécurité ;
- conservation minimale ;
- capacité de diagnostic ;
- capacité de réparation ou de contournement ;
- possibilité de revenir à un fonctionnement manuel simple.

Le confort optimal est désirable, mais il n’est pas toujours prioritaire.

En mode dégradé, la question n’est pas :

> Le système fournit-il exactement le même confort qu’en mode normal ?

La bonne question est :

> Quelle fonction reste disponible, à quel niveau, pendant combien de temps, avec quelle capacité de diagnostic et de retour à la normale ?

---

## 2. Application à l’eau chaude

Dans le cas du circuit d’eau chaude hybride, trois niveaux doivent être distingués :

### 2.1 Fonction vitale ou primaire

Avoir de l’eau au robinet.

Si le système d’optimisation thermique tombe en panne, l’eau doit continuer à circuler, même froide ou tiède.

### 2.2 Fonction de confort

Avoir de l’eau à la bonne température.

C’est important, mais ce n’est pas toujours critique, surtout si la panne est brève.

### 2.3 Fonction d’optimisation

Choisir automatiquement entre :

- eau du réseau ;
- eau issue du cumulus utilisé comme réserve thermique ;
- préchauffage solaire ;
- appoint gaz ou autre ;
- stockage thermique ;
- by-pass.

Cette fonction améliore l’efficacité, mais elle ne doit pas rendre indisponible la fonction primaire.

---

## 3. Modes de fonctionnement

### 3.1 Mode normal

Le système mesure, arbitre et optimise.

```text
capteurs
→ diagnostic local
→ décision de routage
→ électrovannes
→ température utile
→ documentation de l’état
```

### 3.2 Mode dégradé acceptable

Le système ne chauffe plus correctement, mais l’eau reste disponible.

```text
eau réseau
→ by-pass ou circuit ouvert
→ usage possible, même sans température idéale
```

Ce mode est acceptable si :

- la panne est brève ;
- l’eau reste disponible ;
- le risque de brûlure est absent ;
- le risque sanitaire est maîtrisé ;
- l’habitant comprend ce qui se passe ;
- le diagnostic est possible.

### 3.3 Mode critique

Le système empêche l’accès à l’eau, présente un risque de fuite, de brûlure, de gaz, de fumées, d’électricité ou de contamination.

Ce mode doit être évité par conception.

---

## 4. Rôle des capteurs

Les capteurs transforment une panne opaque en situation analysable.

Pour l’eau chaude, les capteurs utiles sont notamment :

- température eau réseau ;
- température haut du cumulus ;
- température bas du cumulus ;
- température sortie usage ;
- débit ;
- pression ;
- état des électrovannes ;
- présence ou absence de demande ;
- énergie consommée par l’appoint ;
- alerte CO ou gaz si un appoint gaz est présent ;
- humidité ou détection de fuite.

Le capteur ne sert pas seulement à automatiser. Il sert aussi à apprendre.

Formule :

> Ce qui est mesuré devient explicable. Ce qui est explicable devient transmissible.

---

## 5. Rôle des actionneurs

Les actionneurs permettent de tester, contourner et restaurer.

Exemples :

- électrovanne d’entrée réseau directe ;
- électrovanne vers cumulus ;
- électrovanne sortie cumulus ;
- électrovanne vers appoint ;
- by-pass motorisé ou manuel ;
- relais de commande d’un appoint ;
- vanne de purge ;
- fermeture automatique en cas de fuite.

Ils ne doivent pas créer une boîte noire supplémentaire.

Chaque actionneur doit avoir :

- un état lisible ;
- une commande manuelle ou procédure de secours ;
- une documentation ;
- une logique de défaut sûre.

---

## 6. Agents IA et diagnostic actif

Les agents IA peuvent jouer un rôle important si le système leur fournit les bons signaux.

Ils peuvent aider à :

- interpréter les mesures ;
- détecter les incohérences ;
- proposer des tests ;
- guider l’habitant pas à pas ;
- distinguer panne de capteur, panne d’actionneur, panne hydraulique ou panne thermique ;
- produire un journal de diagnostic ;
- préparer une intervention professionnelle si nécessaire.

Exemple de recherche de panne :

```text
symptôme : eau froide à la sortie usage

agent IA :
1. vérifier température eau réseau
2. vérifier température haut cumulus
3. vérifier ouverture électrovanne C
4. vérifier débit détecté
5. vérifier pression
6. tester ouverture by-pass
7. comparer état commandé / état mesuré
8. conclure : pas de réserve chaude, électrovanne bloquée, capteur incohérent, ou appoint indisponible
```

L’IA ne remplace pas la compétence humaine. Elle organise l’observation et réduit l’opacité.

---

## 7. Homéostasie et Autonomie de Capacité

L’homéostasie de l’habitat rejoint directement l’Autonomie de Capacité.

Un système vraiment autonome n’est pas celui qui ne tombe jamais en panne.

C’est celui qui :

- détecte ses écarts ;
- maintient une fonction minimale ;
- explique son état ;
- permet des tests ;
- permet une réparation ;
- évite l’effondrement en cascade ;
- apprend de ses incidents ;
- transmet ses procédures.

Cela distingue deux modèles.

### 7.1 Modèle classique opaque

```text
panne
→ incompréhension
→ urgence
→ prestataire
→ facture
→ dépendance maintenue
```

### 7.2 Modèle capacitaire

```text
panne
→ mesure
→ diagnostic assisté
→ mode dégradé acceptable
→ action corrective
→ documentation
→ apprentissage
```

Formule :

> L’autonomie n’est pas l’absence de panne. C’est la capacité à ne pas devenir impuissant quand une panne survient.

---

## 8. Lien avec FractaVolta

L’homéostasie de l’habitat prépare naturellement FractaVolta.

Dès que les usages sont mesurés, priorisés et routés, l’énergie cesse d’être un flux indifférencié.

Elle devient une ressource gouvernable :

- quantité ;
- source ;
- destination ;
- priorité ;
- urgence ;
- capacité de report ;
- mode dégradé ;
- coût ;
- trace.

C’est la logique des packets d’énergie.

Un habitat homéostatique peut donc être vu comme un premier nœud FractaVolta : il mesure ses besoins, arbitre ses ressources, maintient ses fonctions importantes et documente ses décisions.

---

## 9. Continuations

### 9.1 Fiche eau chaude homéostatique

Produire une fiche spécifique sur le circuit eau chaude : capteurs, actionneurs, by-pass, diagnostic IA, modes dégradés.

### 9.2 Référentiel des fonctions essentielles

Définir, pour un logement, les fonctions à maintenir : eau, lumière, communication, sécurité, froid alimentaire, chauffage minimal, mobilité, données.

### 9.3 Grille des modes dégradés

Créer une grille distinguant :

- panne sans impact ;
- perte de confort ;
- perte de fonction importante ;
- risque matériel ;
- risque sanitaire ;
- risque vital.

### 9.4 Agents de diagnostic

Définir les premiers agents IA spécialisés : agent eau chaude, agent énergie, agent humidité, agent batterie, agent facture, agent maintenance.

---

## 10. Conclusion

L’habitat autonome ne doit pas être conçu comme une machine parfaite.

Il doit être conçu comme un organisme technique capable de maintenir ses fonctions importantes, de diagnostiquer ses écarts, de fonctionner en mode dégradé, de guider l’habitant et de produire de l’apprentissage.

Cette perspective permet de dépasser l’opposition entre confort moderne et retour archaïque à la débrouille.

Il ne s’agit pas de revenir à la fontaine.

Il s’agit de faire en sorte que, même quand l’optimisation échoue, l’eau reste disponible, le système reste compréhensible, et l’habitant reste capable.

Formule finale :

> L’homéostasie de l’habitat est la capacité d’un logement à préserver ses fonctions importantes tout en rendant ses écarts visibles, diagnostiquables et réparables.
