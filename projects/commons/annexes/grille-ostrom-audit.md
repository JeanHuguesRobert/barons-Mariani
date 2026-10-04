---
title: "Grille d'audit institutionnel d'Ostrom : méthode d'évaluation et de résistance à la capture"
subtitle: "Opérationnalisation des 8 principes de conception d'Elinor Ostrom et diagnostic des 7 modes de capture"
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-04"
version: "0.1"
status: "working-paper"
license: "CC BY-SA 4.0"
language: "fr"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/commons/annexes/grille-ostrom-audit.md"
document_role: "source"
document_kind: "method-audit-tool"
visibility: "public"
lifecycle_state: "working"
---

# Grille d'audit institutionnel d'Ostrom

## 1. Objet et méthode

Cette grille opérationnalise les travaux d'Elinor Ostrom (*Governing the Commons*, 1990 ; *Understanding Knowledge as a Commons*, 2007) pour évaluer la viabilité et la robustesse de n'importe quelle institution de biens communs — qu'elle porte sur un pâturage, un réseau d'irrigation, une forge logicielle, une boucle solaire d'autoconsommation ou un commun cognitif.

L'audit repose sur une double évaluation :
1. **Le test de complétude des 8 principes de conception.**
2. **Le diagnostic de vulnérabilité aux 7 modes de capture.**

---

## 2. Les 8 Principes de conception opérationnalisés

| N° | Principe Ostrom | Question diagnostique clé | Signaux d'alerte (Score faible) | Indicateurs de robustesse |
|---|---|---|---|---|
| **P1** | **Limites clairement définies** | *Sait-on exactement qui a le droit d'utiliser la ressource et quel est son périmètre ?* | Frontières floues, passagers clandestins indétectables, confusion entre accès libre et droit d'usage. | Registre transparent des membres, périmètre physique ou protocolaire rigoureusement délimité. |
| **P2** | **Concordance règles / conditions locales** | *Les règles de prélèvement, de copie ou de contribution sont-elles adaptées à la réalité du milieu ?* | Règles abstraites parachutées d'en haut, quotas déconnectés des variations saisonnières ou techniques. | Flexibilité saisonnière, différenciation contextuelle validée par les usagers directs. |
| **P3** | **Dispositifs de choix collectifs** | *Ceux qui subissent les règles peuvent-ils participer à leur modification ?* | Droit de veto exclusif d'un bailleur ou d'un conseil d'administration extérieur, apathie démocratique. | Assemblées régulières délibératives, processus d'amendement ouvert aux contributeurs actifs. |
| **P4** | **Surveillance mutuelle effective** | *Les surveillants sont-ils les usagers eux-mêmes ou des personnes leur rendant compte ?* | Police extérieure corrompue ou absente, invisibilité des prélèvements et abus. | Visibilité réciproque (ex. tour d'eau de Valence, git blame/log public, compteurs partagés). |
| **P5** | **Sanctions graduées** | *Les peines commencent-elles par un avertissement bienveillant avant de sévir ?* | Tolérance aveugle suivie d'un bannissement immédiat et brutal, punitions arbitraires. | Échelle claire : rappel amical → blâme public → suspension temporaire → exclusion définitive. |
| **P6** | **Résolution rapide des conflits** | *Existe-t-il des espaces locaux, peu coûteux et impartiaux pour régler les litiges ?* | Procédures judiciaires ruineuses, conflits gelés pourrissant la vie communautaire. | Médiation par les pairs, tribunaux oraux sans frais, comités d'arbitrage élus. |
| **P7** | **Reconnaissance minimale des droits** | *L'État central ou les autorités légales reconnaissent-ils la légitimité des règles locales ?* | Criminalisation étatique des usages (ex. Code forestier de 1827), interdiction des licences alternatives. | Statuts municipaux reconnus, licences opposables devant les tribunaux (ex. validité de la GPL). |
| **P8** | **Entreprises imbriquées (systèmes complexes)** | *La gouvernance s'articule-t-elle en couches gigognes polycentriques ?* | Monopole décisionnel monolithique incapable de gérer l'hétérogénéité territoriale. | Fédérations décentralisées, comités de bassins de vie, subsidiarité ascendante. |

---

## 3. Diagnostic des 7 modes de défaillance et de capture

Chaque projet de commun doit être éprouvé face aux sept vulnérabilités structurelles identifiées par le Corpus :

```text
1. L'ENCLOSURE PRIVATIVE
   Tentative par un acteur économique de transformer un droit d'usage partagé en titre de propriété exclusive (achat hostile, brevets, accaparement des terres).

2. LA CONFISCATION ÉTATIQUE
   Nationalisation bureaucratique dépossédant la communauté locale de sa capacité de décision et confiant la ressource à des fonctionnaires distants.

3. LE SOUS-ENTRETIEN ET L'ABANDON
   Défection des contributeurs par manque d'incitation ou d'énergie, laissant dépérir l'infrastructure matérielle ou le code (épuisement des mainteneurs).

4. LE PARASITISME (PASSAGER CLANDESTIN MASSIF)
   Extraction unilatérale de valeur sans réciprocité ni contribution aux coûts de maintenance (ex. hyperscalers exploitant le logiciel libre sans retour).

5. LA CAPTURE D'INFRASTRUCTURE (ENCLOSURE DE SERVICE)
   Fourniture gratuite du logiciel ou de la ressource, mais verrouillage propriétaire du canal d'accès, du serveur, du réseau ou de l'énergie.

6. L'ASYMÉTRIE INFORMATIONNELLE
   Complexification délibérée des règles et protocoles par une coterie d'experts privant la majorité de la compréhension et du contrôle du système.

7. LA BUREAUCRATISATION ET L'OLIGARCHIE INTERNE
   Dégénérescence des instances délibératives en baronnies locales fermées rejetant les nouveaux arrivants et étouffant la contestation interne.
```

---

## 4. Protocole d'évaluation chiffrée

Pour chaque principe $P_1$ à $P_8$, attribuer une note de 0 à 3 :
- **0** : Absence totale (danger immédiat d'effondrement ou de capture).
- **1** : Ébauche informelle sans garantie institutionnelle.
- **2** : Dispositif opérationnel fonctionnel mais fragile face aux crises.
- **3** : Règle constitutionnelle robuste, documentée et éprouvée dans le temps.

**Interprétation du score global (sur 24) :**
- **< 12 / 24** : *Commun fictif ou en voie d'enclosure imminente.*
- **12 à 18 / 24** : *Commun vulnérable nécessitant un renforcement institutionnel ciblé.*
- **> 18 / 24** : *Institution résiliente à haute maturité polycentrique.*
