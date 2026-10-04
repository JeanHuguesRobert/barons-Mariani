---
title: "De la licence GPL aux clusters de GPU : comment le cloud et l'IA contournent le logiciel libre"
subtitle: "Chronique de la troisième enclosure : quand l'asymétrie matérielle confisque l'abondance algorithmique"
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-04"
version: "0.1"
status: "working-paper"
license: "CC BY-SA 4.0"
language: "fr"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/commons/magazine/2026-10-04-enclosure-du-cloud-et-ia.md"
document_role: "source"
document_kind: "magazine-article"
visibility: "public"
lifecycle_state: "working"
---

# De la licence GPL aux clusters de GPU : comment le cloud et l'IA contournent le logiciel libre

**Par Jean Hugues Noël Robert, baron Mariani**  
*Institut Mariani / C.O.R.S.I.C.A. — Corte, 4 octobre 2026*

---

## 1. La faille originelle : l'enclosure par le service (SaaS)

En 1985, lorsque Richard Stallman conçut la General Public License (GPL), le monde informatique était dominé par la distribution physique de logiciels sur disquettes et bandes magnétiques. L'enjeu était limpide : quiconque distribuait un binaire compilé devait en fournir le code source sous peine de contrefaçon.

Cette forteresse juridique du *copyleft* a remarquablement fonctionné pendant vingt ans. Mais à partir des années 2010, l'avènement du Cloud computing et des architectures en mode service (Software as a Service — SaaS) a révélé une faille structurelle d'une portée dévastatrice.

Pour contourner la GPL, les géants du cloud (Amazon Web Services, Microsoft Azure, Google Cloud) n'ont pas eu besoin de violer la licence : ils ont cessé de **distribuer** les logiciels. En exécutant Linux, PostgreSQL, Redis ou Kubernetes exclusivement sur leurs propres serveurs distants, ils fournissaient un accès réseau à des millions d'utilisateurs sans jamais transférer de binaire. L'obligation de réciprocité du copyleft classique était neutralisée d'un trait.

Le logiciel libre est ainsi devenu la matière première gratuite sur laquelle s'est édifié le plus formidable oligopole centralisé de l'histoire du capitalisme. Des milliers de développeurs bénévoles ont entretenu le moteur du monde, tandis que trois ou quatre corporations américaines en prélevaient la totalité de la rente de péage.

---

## 2. Le choc du calcul : l'intelligence artificielle comme barrière capitalistique

L'explosion de l'intelligence artificielle générative et des modèles de fondation (LLMs) entre 2023 et 2026 a porté cette dynamique d'enclosure à un niveau qualitatif supérieur.

Sur le plan mathématique, un réseau de neurones est un ensemble d'équations et de coefficients matriciels (les poids). Le code d'inférence est bref, élégant et parfaitement non rival : n'importe quel ordinateur portable peut en théorie calculer une passe avant d'attention (*self-attention*).

Pourtant, le coût de fabrication d'un modèle frontière relève d'une économie industrielle d'une brutalité inouïe :
- Des grappes de 50 000 à 100 000 processeurs graphiques ultra-spécialisés (GPU/TPU) fonctionnant en parallèle pendant des mois ;
- Des investissements d'infrastructure se chiffrant en centaines de millions, voire en milliards de dollars par modèle ;
- Des besoins électriques mesurés en dizaines de mégawatts, rivalisant avec la consommation de villes entières.

Ici s'opère le basculement : **si l'algorithme est non rival, le calcul matériel (*compute*) et l'énergie nécessaire à son apprentissage sont violemment rivaux et hyper-concentrés.**

En dressant une barrière financière infranchissable pour les universités, les laboratoires publics et les communautés de hackers, les barons du cloud privatisent de facto la production de l'intelligence artificielle générale. L'usager n'a plus accès qu'à une interface de programmation (API wall) soumise à des conditions générales arbitraires, à une surveillance algorithmique totale de ses requêtes et à un prix fixé discrétionnairement par le monopoleur.

---

## 3. Le leurre de l'Open Source sans souveraineté d'apprentissage

Face à cette clôture, certains conglomérats ont publié les fichiers de poids de leurs modèles sous des licences dites « ouvertes » (l'écosystème des *open weights*). 

Si cette démarche représente un progrès incontestable par rapport aux boîtes noires propriétaires pures — en permettant l'inférence locale et la recherche de sécurité —, elle ne reconstitue pas un véritable bien commun au sens d'Ostrom :
- Les poids d'un modèle sans le jeu de données d'entraînement complet, sans le code d'alignement et sans la capacité financière de ré-entraîner le modèle sont des **artefacts gelés**.
- La communauté peut adapter le modèle (*fine-tuning*), mais elle ne peut pas en contester les fondations ontologiques ni en corriger les biais matriciels profonds sans disposer du cluster de calcul d'origine.
- Pire encore, certaines licences d'accompagnement imposent des clauses d'usage commercial restreint ou des seuils d'utilisateurs bloquants, réintroduisant la logique d'enclosure sous le masque de l'ouverture.

---

## 4. Les chemins de la contre-offensive : vers les communs cognitifs territoriaux

Comment briser cet étau et préserver l'autonomie cognitive des communautés humaines ? La réponse ne viendra pas d'un retour nostalgique au passé, mais de l'invention d'instruments institutionnels et techniques adaptés à ce nouveau substrat :

1. **La frugalité et la quantification locale :**  
   L'essor des petits modèles spécialisés (Small Language Models), quantifiés en 4-bit ou 8-bit et capables de tourner efficacement sur du matériel grand public (puces Apple Silicon, stations de travail locales), constitue la première ligne de défense de la souveraineté personnelle. Le savoir doit pouvoir s'exécuter hors réseau et sans compte cloud.
2. **Les consortiums publics de compute :**  
   À l'image du CERN pour la physique fondamentale des particules, les démocraties doivent financer des supercalculateurs académiques ouverts, garantissant aux chercheurs la capacité d'entraîner des modèles publics sous contrôle citoyen.
3. **Les communs cognitifs persistants (Cogentia Commons) :**  
   La valeur ne réside pas dans la génération stochastique de texte par un modèle opaque, mais dans la rigueur de la traçabilité des raisonnements, l'imputabilité des thèses et la documentation publique des réfutations. En mutualisant les processus d'exploration possibiliste plutôt qu'en déléguant la pensée à des oracles privés, les communautés humaines restaurent leur capacité d'action souveraine.

La bataille pour les biens communs du XXIe siècle ne se joue plus seulement dans les forêts et les cours d'eau : elle se livre désormais sur les plaquettes de silicium et les architectures de calcul qui conditionnent notre capacité collective à penser l'avenir.
