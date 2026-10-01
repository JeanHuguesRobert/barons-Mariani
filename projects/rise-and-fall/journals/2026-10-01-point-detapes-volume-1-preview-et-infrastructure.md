---
title: "Journal d'enquête — Étape majeure : Volume 1 Preview, Infrastructure et Cadre de Contribution"
author: "Jean Hugues Noël Robert"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-01"
status: "permanent-record"
language: "fr"
license: "CC BY-SA 4.0"
document_role: "investigation-journal"
document_kind: "synthesis-checkpoint"
visibility: "public"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/rise-and-fall/journals/2026-10-01-point-detapes-volume-1-preview-et-infrastructure.md"
---

# Journal d'enquête — Point d'étape : Volume 1 Preview, Infrastructure et Contribution

Ce document consigne de manière exhaustive et souveraine l'ensemble des résultats, décisions éditoriales, rectifications historiques et déploiements techniques réalisés pour le projet *Rise & Fall of the Mariani Family* à la date du **1er octobre 2026**.

Il constitue le pont mémoriel inaltérable destiné à garantir qu'aucune information, analyse ou démarche ne puisse être perdue lors des rotations de session d'agents ou de maintenance du Corpus.

---

## 1. Déploiement de l'infrastructure web publique

Le site de référence du projet est intégralement opérationnel en production sous protocole sécurisé HTTPS :
- **Domaine canonique :** `https://riseandfall.baronsmariani.org`
- **Routage DNS :** Enregistrement CNAME Cloudflare vers `fracta.fractavolta.com` (82.70.234.207).
- **Passerelle Edge :** Caddy reverse proxy sur `fracta` redirigeant le trafic vers `fracta2` (`100.84.109.87:80` via le réseau maillé Tailscale, avec repli public sur `130.110.241.116`).
- **Serveur applicatif et racine web :** Hébergement sur instance Oracle Cloud Infrastructure (OCI) dans `/srv/www/riseandfall/current/` (propriété `www-data:www-data`).
- **Synchronisation automatique :** Les fichiers sources résident dans `projects/rise-and-fall/site/` du dépôt GitHub `JeanHuguesRobert/barons-Mariani` (branche `main`).

---

## 2. Rectifications historiques et généalogiques canoniques

L'enquête a permis de purger plusieurs approximations secondaires et de fixer les vérités documentaires suivantes :

### 2.1. Le domaine familial de Minesteggio
- Le domaine historique, son château et ses terres agricoles se nomment **Minesteggio** (formes graphiques attestées selon les époques : *Minesteggio*, *Minesteghju*, *Ménesteggio*).
- Il ne doit pas être confondu avec le toponyme *Panate*, qui désigne une fontaine urbaine et une parcelle associée situées cours Paoli à Corte.

### 2.2. Le titre de baron westphalien (1813)
- Le titre de baron conféré à Antoine Dominique Mariani est un **titre westphalien octroyé en 1813 par le Roi Jérôme Bonaparte** (frère cadet de Napoléon Ier).
- L'attribution s'est déroulée dans le contexte dramatique de la fin du Royaume de Westphalie et de la débâcle de Cassel, **au moment précis où le Journal Officiel du royaume a cessé de paraître**.
- Cette circonstance matérielle explique l'absence d'enregistrement ultérieur au *Moniteur Universel* de Paris, tout en fondant une possession d'usage ininterrompue et reconnue dans tous les actes civils, notariés, consulaires et funéraires sur plus d'un siècle et demi.

### 2.3. Lignée et dates canoniques du Corpus Mariani
L'état civil critique est définitivement stabilisé comme suit :
1. **Antoine Dominique Mariani (1776–1845) :** Né le 15 septembre 1776 à Muracciole / Corte. Sous-préfet de Corte (1811), baron westphalien (1813), bâtisseur de Minesteggio. Mort le 8 décembre 1845.
2. **Louis-Thomas Joseph Maurice Jérôme Mariani (1815–1890) :** 2e baron, magistrat, député de la Corse au Corps législatif sous le Second Empire (majorité dynastique). Débouté en 1863 face à Gavini.
3. **Louis-Hugues Ferdinand Marie Mariani (1815/1818–1886/1890) :** Magistrat, frère de Louis-Thomas. Époux (1853) de Marie Joséphine d'Angelis. Co-fondateur de la chapelle funéraire de Bastia (parcelle AR 186).
4. **Pierre Mariani (baron Pierre Mariani) († 17 février 1938) :** Fils de Louis-Hugues. Époux (1893) de Marguerite de Casabianca (1861–1919). Donateur du terrain du monument aux morts de Corte en 1924.
5. **Marie-Louise Mariani, épouse Robert (3 août 1901 – 26 février 1983) :** Fille unique du baron Pierre Mariani et de Marguerite de Casabianca. Épouse (1939) de Jean Robert (1900/1903–1969). Gardienne de Minesteggio.
6. **Marguerite Robert (12 décembre 1940 – 9 septembre 1993) :** Fille unique de Marie-Louise Mariani et Jean Robert. Mère de Jean-Hugues.
7. **Jean Hugues Noël Robert, baron Mariani (né le 25 décembre 1965) :** Fils de Marguerite Robert. Auteur de l'enquête, fondateur de l'association C.O.R.S.I.C.A., initiateur du Fonds Minesteggio.
8. **Marie-Louise Isabelle Garance Robert († 17 septembre 2024) :** Fille de Jean Hugues Noël Robert. Disparition tragique ayant fondé l'enquête capacitaire de *Suicide Corse*.

### 2.4. Héraldique et devise
- **Armoiries :** Écu d'azur à la tour crénelée d'argent, sommée de trois coquilles d'or en chef, accostée de branches de laurier et de chêne.
- **Timbre :** Tortil de baron (le dessin de travail initial figurant une couronne a été corrigé et documenté dans `projects/rise-and-fall/assets/cover/blason.md`).
- **Devise :** *« FIDELITAS · PARVORVM · FORTITVDO »* (« La fidélité est la force des humbles »).

---

## 3. Retrouvaille mémorielle : Antoine « Tony » Toma et l'étymologie de Minesteggio

Le 30 septembre 2026, l'enquête a identifié formellement **Antoine « Tony » Toma** (décédé le 2 mai 2026, maître de conférences à l'Université Toulouse III et mandoliniste cortenais honoré publiquement à Corte en août 2026) comme la source orale ayant transmis l'hypothèse toponymique d'une dérivation de *Minesteggio* à partir de racines latines associant *mini-/minus* (petit) et *stadium/staggio* (champ délimité, enclos).
- **Statut critique :** L'identité et la provenance du témoin sont prouvées ([E]). L'hypothèse linguistique elle-même reste consignée comme une hypothèse de travail ouverte ([O]).
- **Dossier source :** `projects/rise-and-fall/investigation/notes/2026-09-30-tony-toma-minesteggio.md`.

---

## 4. Les deux Reality Cases pilotes

### RC-01 : L'élection législative de 1863 (Louis-Thomas Mariani contre Sampiero Gavini)
- **Document primaire :** Mémoire imprimé de 72 pages de Louis Mariani (*Protestation contre les opérations électorales de la 2e circonscription de la Corse*).
- **Résultat contrefactuel :** Malgré des irrégularités avérées en milieu rural, l'avance de Gavini reste supérieure à 800 voix en neutralisant les bureaux contestés.
- **Portée épistémique :** Réfutation de la fable d'une persécution par l'État impérial. L'administration centrale soutenait Mariani comme candidat officiel ; c'est le tissu clientélaire local et la défection des maires ruraux qui ont provoqué sa défaite.
- **Fichier :** `projects/rise-and-fall/investigation/reality_cases/RC-01-1863-gavini.md`.

### RC-02 : La donation du monument aux morts de Corte (1924)
- **Source municipale :** *Corti — Storia è Patrimoniu*, p. 31 (Ville de Corte).
- **Fait établi :** Le monument aux morts de 1914-1918 a été érigé sur une parcelle donnée gratuitement à la commune par le baron Pierre Mariani.
- **Portée épistémique :** Démontre que toute réduction de l'assiette foncière ne relève pas de la ruine, de la spoliation ou de la prédation fiscale, mais peut découler d'un acte de libéralité patriotique et civique.
- **Fichier :** `projects/rise-and-fall/investigation/reality_cases/RC-02-1924-donation-corte.md`.

---

## 5. Le Livre Vivant : Volume I (1776–1870) — Projection intermédiaire instable

Conformément aux instructions reçues, le Volume I en préparation est matérialisé sous la forme d'une préversion complète :
- **Statut doctrinal :** *Projection intermédiaire instable* (non gelée). Elle préfigure fidèlement ce que sera l'édition bouclée tout en restant ouverte aux corrections et aux apports archivistiques.
- **URL :** `https://riseandfall.baronsmariani.org/editions/volume-1-preview/`
- **Fichiers sources du manuscrit (`projects/rise-and-fall/manuscript/book/`) :**
  - `00-ouverture.md`
  - `01-methode-deux-passes.md`
  - `02-antoine-dominique-et-titre-1813.md`
  - `03-reality-case-rc01-1863.md`
  - `04-reality-case-rc02-1924.md`
  - `05-minesteggio-la-memoire-retrouve-un-nom.md`
  - `06-deux-epoques-se-repondent.md` (Pivot 1863 ↔ 2026 avec *Suicide Corse*)
  - `07-chronologie-et-bifurcations.md`
  - `08-questions-ouvertes.md`
- **Contrat de projection :** `projects/rise-and-fall/projections/book-bootstrap.yml`.
- **Manifeste technique JSON :** `projects/rise-and-fall/site/editions/volume-1-preview/preview-status.json`.

---

## 6. Dispositif de participation et Guide public

Pour ouvrir la recherche aux savoirs extérieurs sans compromettre la rigueur méthodologique, un dispositif complet à deux voies a été mis en place :
- **Mentions légales :** `https://riseandfall.baronsmariani.org/mentions-legales.html` (statut non commercial, CC BY-SA 4.0, directeur de la publication : Jean Hugues Noël Robert, zéro traceur tiers, RGPD).
- **Page de contribution :** `https://riseandfall.baronsmariani.org/contribuer.html` détaillant :
  1. *4 domaines de compétences :* Archives notariales, Toponymie & philologie, Droit public & contentieux électoral, Informatique & Merkle DAG.
  2. *2 canaux :* Canal 1 public sur GitHub (Issues / PR) et Canal 2 privé et confidentiel par courriel (`jhr@baronsmariani.org`, `institutmariani@gmail.com`).
- **Guide public interactif :** `https://riseandfall.baronsmariani.org/guide.html` branché sur le pont Cogentia (`https://cogentia.fractavolta.com`), doté de ses scripts autonomes (`assets/guide.js`, `assets/guide.css`), permettant d'explorer le corpus et de générer localement un brouillon de courriel ou de ticket GitHub avant tout envoi volontaire.

---

## 7. État de synchronisation Git

Tous les éléments décrits ci-dessus sont commités et synchronisés sur le dépôt officiel :
- **Dépôt :** `https://github.com/JeanHuguesRobert/barons-Mariani`
- **Branche :** `main`
- **Statut de l'arbre de travail :** Rigoureusement propre (`working tree clean`), aligné avec `origin/main`.
