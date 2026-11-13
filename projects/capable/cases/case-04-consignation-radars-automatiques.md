---
title: "Cas 04 — La consignation préalable des radars automatiques : le péage censitaire d'accès au juge"
description: "Comment l'obligation de payer avant de pouvoir contester une amende automatisée renverse la présomption d'innocence et discrimine par l'argent."
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-05"
version: "0.1"
status: "working-paper"
license: "CC BY-SA 4.0"
language: "fr"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/capable/cases/case-04-consignation-radars-automatiques.md"
document_role: "source"
document_kind: "reality-case"
visibility: "public"
lifecycle_state: "working"
update_policy: "UP-DEFAULT-REVIEWED"
provenance:
  origin_type: "repository"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "main"
  origin_date: "2026-10-05"
  derived_from:
    - "projects/capable/capable-test.md"
    - "projects/privai/cases/case-06-horizon-presomption-fiabilite-machine.md"
review:
  status: "unreviewed"
  reviewed_by: []
---

> **Brouillon non relu — source de travail (Capable #152).** Contenu conservé pour examen contradictoire et vérification des faits et des références ; aucune validation éditoriale, juridique ou scientifique ni inclusion dans une édition publiée n'est impliquée par sa présence sur GitHub.

# Cas 04 — La consignation préalable des radars automatiques : le péage censitaire d'accès au juge

## Fiche synthétique

- **case_id** : CAPABLE-RC-04
- **domaine** : Justice de proximité, verbalisation automatisée et égalité des armes
- **source** : Code de procédure pénale (art. 529-10) ; Décision n° 2010-38 QPC du Conseil constitutionnel ; Rapports de la Défenseure des droits sur le Centre National de Traitement (CNT) de Rennes (2018–2023).
- **notions Capable associées** : Filtre censitaire, Automate de recouvrement, Règle du péage probatoire.

---

## 1. Ouverture formelle du possible

La chaîne de contrôle automatisé de la vitesse (radars automatiques gérés par l'ANTAI et le CNT de Rennes) émet chaque année plusieurs millions d'avis de contravention (volume exact à sourcer aux bilans ANTAI).

En théorie, l'article 6 de la Convention européenne des droits de l'homme garantit à toute personne le **droit à un recours juridictionnel effectif et impartial** pour contester le bien-fondé d'une accusation pénale.

Le Code de procédure pénale prévoit formellement que le titulaire du certificat d'immatriculation peut contester l'infraction (véhicule volé, plaque usurpée, cession du véhicule, ou contestation du conducteur réel).

---

## 2. L'épreuve du Réel : payer pour avoir le droit de parler

En pratique, l'article 529-10 du Code de procédure pénale pose une condition suspensive redoutable : à moins de dénoncer un tiers ou d'avoir déposé plainte pour vol, toute contestation sur le fond est **irrecevable si le citoyen n'a pas préalablement « consigné » le montant de l'amende forfaitaire** (généralement 135 €).

Cette obligation produit une mécanique d'asymétrie brutale :
1. **Le filtre censitaire d'accès au juge** : Pour un ménage précaire, un étudiant ou un travailleur au SMIC, immobiliser 135 € pendant un an ou dix-huit mois (délai moyen de transmission à l'Officier du Ministère Public et d'audiencement) représente une ponction intolérable sur le budget alimentaire ou énergétique. Les plus démunis renoncent massivement à contester des erreurs manifestes de l'automate pour éviter la saisie bancaire.
2. **Le piège de la dématérialisation forcée** : Le site de l'ANTAI rejette automatiquement les contestations sans motif clair en cas d'inadéquation de format d'image ou de formulaire. En cas d'échec informatique, l'amende est automatiquement majorée (375 €), ouvrant immédiatement la voie à une opposition administrative sur compte bancaire (OAT) sans intervention humaine.
3. **Le silence de l'OMP comme confirmation automatique** : Dans des milliers de cas, l'Officier du Ministère Public ne répond pas, encaisse la consignation et laisse le dossier s'éteindre par prescription ou rejet sans motivation.

---

## 3. Analyse au crible du Capable Test

| Palier d'instruction | Constat d'effectivité | Statut |
|---|---|---|
| **A. Ouverture du possible** | Recours juridictionnel prévu à l'article 529-10 du CPP. | `OPEN` |
| **B. Accessibilité** | Portail ANTAI opaque, téléprocédure exclusive, formats rigides. | `DIFFICULT` |
| **C. Exerçabilité sous contrainte** | Consignation financière préalable obligatoire sous peine d'irrecevabilité. | `CENSITAIRE` |
| **D. Liberté effective** | Le citoyen modeste est contraint de plaider coupable et payer par nécessité vitale. | `CRUSHED` |
| **E. Égalité effective** | 135 € est négligeable pour les hauts revenus, rédhibitoire pour les précaires. | `UNFAIR` |
| **G. Corrigibilité** | Recouvrement par saisie bancaire automatique sans audition contradictoire préalable. | `BLOCKED` |

---

## 4. Déblocage par l'Autonomie de Capacité

Capable défend la suppression intégrale de la consignation préalable pour les justiciables isolés et l'introduction d'un bouclier de protection :
- **Levée immédiate du péage de contestation** : La contestation motivée doit suspendre tout recouvrement sans cautionnement pécuniaire ;
- **Traçabilité EIM de la contestation** : Enregistrement de la preuve de contestation avec horodatage certifié opposable aux huissiers et au Trésor public ;
- **Contrôle humain obligatoire sous délai butoir** : Tout avis de majoration émis sans que l'Officier du Ministère Public n'ait expressément rejeté la réclamation par écrit motivé doit être frappé de nullité absolue.
