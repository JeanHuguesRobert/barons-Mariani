---
title: "PrivAI n°1 — Chapitre 10 : L'infrastructure est l'AI Safety"
subtitle: "Compute, données, énergie, modèles et dépendances"
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-04"
version: "0.1"
status: "working-paper"
license: "CC BY-SA 4.0"
language: "fr"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/privai/manuscript/n1/10-infrastructure-est-ai-safety.md"
document_role: "source"
document_kind: "manuscript-chapter"
visibility: "public"
lifecycle_state: "working"
ai_assisted_by:
- "Antigravity (Gemini 3.8 Flash High) — drafting assistance, 2026-10-04, 2026-10-05"
provenance:
  origin_type: "corpus-derivation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "research/democratic_ai_safety.md"
  origin_date: "2026-05-11"
  derived_from:
    - "barons-Mariani/research/potentics_of_compute.md"
    - "barons-Mariani/projects/privai/annexes/matrice-asymetries-personnes-morales.md"
    - "barons-Mariani/research/the_network_is_the_learning_computer.md"
---

# Chapitre 10 : L'infrastructure est l'AI Safety

## 1. La matérialité d'acier et de watts

L'idéologie numérique a longtemps propagé l'illusion d'une informatique désincarnée. Les métaphores évanescentes du « cloud », du « cyberespace » ou des « algorithmes virtuels » occultent la réalité physique la plus brutale : l'intelligence artificielle est **l'une des industries les plus lourdes, les plus centralisées et les plus énergivores de l'histoire humaine**.

L'intelligence artificielle contemporaine, c'est :
- des centaines de milliers d'accélérateurs graphiques (GPU, TPU) gravés par une unique fonderie mondiale (TSMC à Taïwan) selon des procédés nanométriques extrêmes ;
- des centres de données monumentaux consommant autant d'électricité qu'une agglomération de plusieurs millions d'habitants ;
- des millions de mètres cubes d'eau douce évaporés pour refroidir les baies de serveurs ;
- des câbles sous-marins transocéaniques contrôlés par les oligopoles de la connectivité mondiale.

Prétendre concevoir une « AI Safety » qui se limiterait à des filtres de conversation éthiques, à des comités de déontologie ou à des déclarations de bonnes pratiques, tout en abandonnant la possession du matériel et de l'énergie à trois ou quatre conglomérats transnationaux, est une hypocrisie politique insoutenable.

La règle d'acier posée par PrivAI est limpide : **l'infrastructure est l'AI Safety.** Qui ne possède pas son calcul ne possède pas sa liberté.

---

## 2. Dépasser le modèle du pod : PrivAI et le protocole Solid

Dans l'histoire de la résistance au Web centralisé, le projet **Solid** initié par Tim Berners-Lee a représenté une avancée conceptuelle majeure : rendre à l'utilisateur le contrôle de ses données personnelles en les hébergeant dans des espaces décentralisés (*Personal Online Data Stores* ou *Pods*), la plateforme devant demander l'accès à ces données pour chaque service.

PrivAI salue cet effort pionnier mais constate ses limites face à l'âge des modèles génératifs et agentiques.

| Dimension | Approche Solid (Web décentralisé) | Approche PrivAI (Souveraineté cognitive) |
|---|---|---|
| **Objet central** | Les données statiques (fichiers, contacts, profils). | L'agence, les représentations, le calcul et les actes opposables. |
| **Lieu d'action** | Où sont stockées les données (Pod personnel). | Qui exécute l'inférence et sous quelle chaîne de mandat. |
| **Modèle d'accès** | Autorisation de lecture/écriture via API. | Projection cognitive bornée KYS et non-substitution politique. |
| **Imputabilité** | Gestionnaire de clés cryptographiques. | Reçus probatoires, traçabilité des actes et chaîne de responsabilité. |

PrivAI ne se contente pas de sanctuariser le lieu du stockage : il sanctuarise **le moteur d'inférence et la chaîne de décision**. Avoir ses données dans un coffre personnel ne protège de rien si, pour les analyser ou répondre à une convocation administrative, on est obligé de les envoyer dans le modèle propriétaire d'un tiers qui les exploitera pour affiner sa domination institutionnelle.

---

## 3. Le salut par les modèles ouverts et le calcul local

La ligne de défense de la souveraineté humaine repose sur le développement vigoureux et non négociable de **l'écosystème open-weights et local-first** :

1. **L'émancipation du modèle local :** L'optimisation algorithmique, la quantification (4-bit, 2-bit) et les progrès des puces grand public permettent désormais d'exécuter des modèles de plusieurs dizaines de milliards de paramètres sur des ordinateurs individuels ou des serveurs locaux associatifs.
2. **L'immunité contre la censure et la coupure :** Un modèle tournant en local sur une station de travail hors-ligne ne peut être ni désactivé à distance, ni censuré par une mise à jour silencieuse de conditions d'utilisation, ni soumis à une coupure de réseau ordonnée par une puissance étrangère.
3. **La transparence intégrale des poids :** Seuls les modèles dont les poids sont publics et inspectables permettent de certifier l'absence de portes dérobées, de filtres d'influence idéologique clandestins ou de télémétrie extractive.

La souveraineté cognitive n'est pas un slogan : c'est un poste de calcul personnel, relié à une énergie maîtrisée, exécutant un modèle inspectable, au service d'un esprit libre.

---

## 4. La géopolitique du silicium et la fable des modèles frontières

La rhétorique promotionnelle des laboratoires de pointe impose l'idée que seule une course effrénée vers des architectures géantes (modèles de plus de 500 milliards de paramètres entraînés sur des mégagrid d'énergie de plusieurs centaines de mégawatts) permettrait d'atteindre l'intelligence utile.

Cette fable sert un objectif politique précis : **ériger une barrière capitalistique insurmontable**.
- En maintenant la frontière de l'état de l'art à un seuil financier inaccessible aux citoyens, aux universités et aux petites nations, les conglomérats s'assurent que toute la cognition avancée de l'humanité transite obligatoirement par leurs serveurs.
- Ce modèle repose sur une vulnérabilité géopolitique colossale : la dépendance absolue envers les machines de photolithographie extrême UV néerlandaises (ASML) et les usines de fabrication taïwanaises (TSMC), créant un goulet d'étranglement mondial sous la tutelle militaire et réglementaire des superpuissances.

PrivAI dénonce cette fuite en avant : la sécurité démocratique ne consiste pas à courir derrière l'hypertrophie computationnelle des monopoles, mais à concevoir une informatique cognitive résiliente, décentralisée et proportionnée aux besoins réels de la délibération et de l'émancipation.

---

## 5. Le seuil capacitaire des modèles 3B-8B et le triomphe de la frugalité

L'avancée technologique la plus émancipatrice de ces dernières années n'est pas l'inflation des clusters géants, mais l'élévation spectaculaire de l'efficacité des **petits modèles ouverts (de 3 à 8 milliards de paramètres)** :

- Grâce aux techniques de distillation, de quantification agressive (Q4_K_M, AWQ) et d'entraînement sur des corpus synthétiques hautement filtrés, un modèle de 3B ou 7B paramètres en 2026 rivalise, sur les tâches de raisonnement logique, d'analyse documentaire et d'extraction de faits, avec les monstres propriétaires d'il y a trois ans.
- Ce seuil capacitaire change la donne politique : un modèle 8B quantifié tient sur 5 Go de mémoire vive. Il s'exécute à plus de 30 jetons par seconde sur le processeur neuronal (*NPU*) d'un ordinateur portable grand public ou sur une puce ARM basse consommation, pour une enveloppe énergétique inférieure à 25 watts.
- La frugalité computationnelle brise l'asymétrie : le citoyen n'a plus besoin de louer les faveurs d'un supercalculateur étranger pour auditer ses contrats ou rédiger ses recours. Son matériel personnel suffit à lui conférer une défense cognitive de premier rang.

---

## 6. Fédérations de calcul citoyen et inférence vérifiable (RAIX)

Pour les opérations complexes exigeant une puissance supérieure (simulations de politiques publiques, audits croisés de grands jeux de données administratifs), la solution PrivAI ne passe pas par la soumission au cloud marchand, mais par la mutualisation coopérative formalisée dans les travaux sur la *Potentique du calcul* (*Potentics of Compute*) et le protocole **RAIX** (*Resource Allocation for Inferred eXecution*) :

1. **La mise en réseau de capacités dormantes :** Des millions de processeurs graphiques et de stations de travail citoyennes restent inactifs la nuit. Des fédérations décentralisées permettent d'agréger ce calcul bénévole ou rétribué en biens communs, sous le contrôle exclusif de collectifs indépendants.
2. **L'inférence vérifiable sans confiance aveugle :** Le protocole RAIX résout l'inconvénient historique des réseaux distribués par l'introduction de preuves d'inférence cryptographiques et d'audits statistiques croisés. L'administré qui soumet un calcul confidentiel reçoit un reçu d'exécution mathématique certifiant que le code exact a été exécuté sur les données exactes, sans fuite d'information ni falsification du résultat.
3. **Le découplage infrastructurel :** L'intelligence collective s'affranchit des dépendances captives. Le réseau citoyen devient lui-même un ordinateur apprenant souverain, immunisé contre les censures d'État et les chantages tarifaires des plateformes.
