# VIGILIA
## Système distribué d’évitement des collisions et de perception territoriale

**Version : 1.0**  
**Auteur : Jean Hugues Noël Robert**, baron Mariani. 1 cours Paoli, F-20250 Corte  
**Contexte : Déploiement rural – Corse (phase pilote)**  
**Date : 2026-04-17**

---

# 1. Résumé exécutif (lecture double)

## Lecture politique (élus ruraux)

VIGILIA est un système léger, non intrusif et peu coûteux permettant de réduire significativement les accidents entre véhicules et animaux en zone rurale, sans recourir à des clôtures, infrastructures lourdes ou mesures de contrainte.

Il transforme la mobilité quotidienne des habitants en réseau de vigilance partagé.

---

## Lecture technique (ingénieurs)

VIGILIA est une architecture de capteurs distribués basée sur des balises LoRaWAN basse consommation et des récepteurs embarqués dans les véhicules, exploitant des mesures de puissance de signal (RSSI) et de mobilité GPS pour reconstruire des champs probabilistes de présence.

---

# 2. Problématique territoriale (Corse)

Les territoires ruraux présentent un problème structurel :

- divagation animale (bovins, ovins, caprins)
- visibilité limitée sur les routes secondaires
- coûts élevés des infrastructures de protection (clôtures, passages canadiens)
- tension entre usage agricole et circulation routière

Les solutions actuelles sont :
- coûteuses
- statiques
- localisées
- parfois socialement conflictuelles

---

# 3. Principe général de VIGILIA

VIGILIA repose sur une idée simple :

> Transformer des signaux radio faibles et opportunistes en information de sécurité exploitable.

Le système ne cherche pas à localiser précisément les animaux, mais à détecter leur présence probable dans une zone critique.

---

# 4. Architecture système

## 4.1 Couche animale (balises LoRaWAN)

Chaque animal équipé porte une balise :

- technologie : LoRa / LoRaWAN
- ultra basse consommation
- émission périodique d’un identifiant anonyme
- autonomie longue durée (multi-annuelle)
- coût cible : faible (~10–20 €)

Fonction :
- émission de signaux radio intermittents

---

## 4.2 Couche véhicule (récepteurs embarqués)

Chaque véhicule volontaire devient un capteur mobile :

- smartphone (GPS + calcul + réseau)
- ou module USB LoRa compatible
- réception passive des signaux animaux
- mesure RSSI (intensité du signal)

Aucun matériel lourd embarqué requis.

---

## 4.3 Couche réseau (agrégation distribuée)

Les véhicules transmettent :

- timestamp
- position GPS
- intensité du signal
- identifiant anonymisé de la balise détectée

Ces données sont agrégées dans un backend léger.

---

## 4.4 Couche d’inférence

Le système reconstruit :

- zones de probabilité de présence animale
- gradients de proximité
- évolution temporelle des risques

Il ne s’agit pas d’un GPS animal, mais d’un **champ de présence probabiliste**.

---

# 5. Modèle de fonctionnement (lecture ingénieur)

## 5.1 Signal

Chaque véhicule mesure :

- RSSI(t)
- variation de RSSI sur trajectoire
- corrélation avec mouvement GPS

---

## 5.2 Exploitation du mouvement

Le déplacement du véhicule transforme un signal faible en information exploitable :

- variation spatiale du signal
- effets d’ombre et de diffusion
- convergence multi-observateurs

---

## 5.3 Fusion multi-véhicules

Plusieurs véhicules équipés permettent :

- triangulation probabiliste
- réduction de variance
- amélioration non linéaire de la précision

---

## 5.4 Sortie système

Le système produit :

- cartes de risque dynamiques
- alertes locales embarquées
- zones de vigilance renforcée

---

# 6. Principe de performance

La performance dépend de :

- densité de véhicules équipés
- densité de balises animales
- régularité de circulation

Propriété clé :

> le système s’améliore avec l’usage.

---

# 7. Cas d’usage 1 — Évitement des collisions (Corse)

## Objectif

Réduire les collisions entre :

- véhicules
- animaux en divagation

---

## Fonctionnement

- détection d’une balise à proximité
- variation du signal avec mouvement du véhicule
- estimation d’une zone de présence probable
- alerte conducteur (visuelle / sonore)

---

## Effet attendu

- réduction des accidents
- adaptation préventive de la vitesse
- diminution des conflits d’usage du territoire

---

# 8. Cas d’usage 2 — Suivi distribué de ressources mobiles

## Objectif

Assurer la visibilité de ressources mobiles critiques :

- batteries de véhicules électriques
- conteneurs énergétiques mobiles
- équipements logistiques circulants

---

## Fonctionnement

- chaque ressource possède un identifiant radio
- les véhicules et infrastructures détectent ces signaux
- reconstruction de trajectoires probabilistes
- absence de dépendance à une infrastructure centralisée

---

## Effet attendu

- meilleure coordination logistique
- réduction des pertes et incertitudes
- robustesse en zones rurales ou déconnectées

---

# 9. Coûts et déploiement

## Ordres de grandeur

- balise animale : ~10 à 20 €
- module véhicule : ~50 à 100 € (optionnel)
- backend logiciel : faible à modéré (cloud léger ou local)

---

## Stratégie de déploiement

- phase 1 : zones pilotes rurales
- phase 2 : extension intercommunale
- phase 3 : généralisation territoriale

---

# 10. Architecture conceptuelle

VIGILIA s’intègre dans une architecture plus large de perception territoriale :

- signaux physiques → données
- données → inférences probabilistes
- inférences → décisions locales

---

# 11. Lecture politique (élus)

VIGILIA permet :

- réduction des coûts d’infrastructure (pas de clôtures systématiques)
- diminution des accidents routiers
- approche non conflictuelle avec les activités agricoles
- solution évolutive et progressive

Principe central :

> améliorer la sécurité sans transformer le territoire en zone contrainte.

---

# 12. Lecture technique (ingénieurs)

VIGILIA est :

- un réseau LoRa opportuniste mobile
- un système de fusion de signaux faibles (RSSI)
- une architecture de localisation probabiliste distribuée
- un système edge + backend léger
- un problème de reconstruction de champ de présence dynamique

---

# 13. Limites connues

- dépendance à la densité de participants
- incertitude inhérente (non déterminisme)
- précision inférieure à un GPS classique (par conception)
- nécessité d’adoption progressive

---

# 14. Position conceptuelle

VIGILIA est :

> un système de perception territoriale probabiliste basé sur signaux radio faibles et mobilité des observateurs.

---

# 15. Conclusion

VIGILIA propose une alternative aux infrastructures lourdes :

> transformer la mobilité quotidienne en réseau de vigilance partagé, capable de réduire les collisions sans contrainte physique sur le territoire.

---

# 16. Licence

Projet open source.

Attribution requise :

**Jean Hugues Noël Robert — VIGILIA (2026)**
