---
title: "Capable — inventaire raisonné des Notes de Campagne antérieures"
date: "2026-10-28"
status: "working-inventory — non exhaustif"
document_role: derived
document_kind: editorial-source-inventory
visibility: public
lifecycle_state: working
language: fr
source_documents:
  - "research/index.md"
  - "research/gr20_autonomie_de_capacite.md"
  - "research/traceabilite_civique_antimafia.md"
  - "research/cas_edf_blogpost.md"
  - "research/cas_edf.md"
  - "research/autonomia/note_campagne_statut_resident_effectivite.md"
  - "research/corse_selon_macron_autopsie_manoeuvre_avortee.md"
  - "projects/capable/campaigns/corse-capable-energie.md"
---
# Notes de Campagne : inventaire et potentiel de sédimentation

**Périmètre :** documents repérés par l'index du Corpus, les intitulés et les métadonnées, puis lus pour leur architecture et leurs passages substantiels. L'inventaire n'est **pas exhaustif** : la recherche globale de code GitHub a renvoyé HTTP 429 (limite temporaire), mais les lectures directes des sources listées ont abouti. Ne pas inférer des numéros absents qu'aucune autre note n'a existé.

## Corpus identifié

| Document | Date/statut de la source | Concept et cas traités | Livre : sédimentation candidate | Magazine / Annexes |
| --- | --- | --- | --- | --- |
| [GR20 : du quota à l'autonomie de capacité](../../../research/gr20_autonomie_de_capacite.md) | 16 mai 2026 ; brouillon de campagne | Un quota peut protéger un lieu saturé mais ne crée pas, à lui seul, une autre capacité ; réorienter la demande, développer des alternatives et localiser la valeur | **05 Trois Machines**, **02 Subsidiarité**, **06 Échelles**, **09 Communs** : distinguer fermeture locale nécessaire et création de possibles hors du goulet | Magazine : proposition de politique de la montagne, datée ; Annexe : données de fréquentation, réglementation, carte d'alternatives, coûts et sources |
| [Traçabilité civique anti-mafieuse](../../../research/traceabilite_civique_antimafia.md) | 16 mai 2026 ; brouillon | Tracer faits et actes d'emprise plutôt que constituer des fichiers de personnes ; distinguer vigilance civique et surveillance généralisée | **04 Liberté/Égalité/Fraternité**, **05 Révélateur/Stabilisateur**, **10 Capable Test** : une protection peut devenir elle-même une dépossession | Magazine : cas de démocratie, sécurité et imputabilité ; Annexe : protocole de signalement, exigences de preuve, minimisation, protection des personnes |
| [Note de Campagne n°3 : le cas EDF expliqué](../../../research/cas_edf_blogpost.md), associée au [dossier technique EDF](../../../research/cas_edf.md) | Note d'origine juin 2026, métadonnées hétérogènes (en-tête de classification 15/09, second en-tête interne 20/06), `release_candidate` et validation humaine requise | Production solaire qualifiée de « fatale » en contexte de pilotage, stockage hydraulique potentiel, comparaison des architectures et question de la capture de la valeur ; hypothèses Calacuccia | **03 Effectivité**, **05 Machines**, **09 Communs** : capacité physique disponible ≠ capacité accessible ; distinguer coûts totaux, coûts évités et gouvernance de la valeur | Magazine : lecture datée des choix d'infrastructure ; Annexe : calculs, hypothèses de 1 GWh, CRE, EDF, alternatives, conflits d'intérêts et précautions juridiques |
| [Statut de résident : cas pratique pour l'amendement d'effectivité](../../../research/autonomia/note_campagne_statut_resident_effectivite.md) | septembre 2026 ; document dérivé de campagne | Double test : possibilité juridique d'édicter une norme et effectivité de ses résultats ; question des conséquences sur la liberté, l'égalité et la fraternité dans les deux sens | **02 Subsidiarité**, **03 Effectivité**, **04 principes**, **10 Capable Test** : exemple central d'évaluation contradictoire d'une règle sensible | Magazine : débat contextualisé ; Annexe : avis du Conseil d'État 17/07/2025, versions de l'article 72-5, mesures, données et objections |
| [La Corse selon E. Macron : autopsie d'une manœuvre avortée](../../../research/corse_selon_macron_autopsie_manoeuvre_avortee.md) | 27 octobre 2026 ; source v0.2, version publiée sur Substack | Pouvoir institutionnel attribué ≠ capacité politique effective des habitants ; écart promesse/résultat et corrections | **02, 03, 04, 05, 10** ; sédimentation de la distinction, non transfert littéral de la chronique parlementaire | Magazine : séquence sénatoriale du 26 octobre, Note publiée le 27, réactions et suite annoncée ; Annexe : scrutins, procédures, propositions, sources |

## Complément de l'inventaire après recherche exhaustive des dépôts locaux (28 octobre)

Le relevé `git grep` effectué sur Fracta2 confirme les mentions déjà connues et fait apparaître une **sixième source**, absente du premier inventaire :

| Document | Date/statut | Apport de fond | Destination |
| --- | --- | --- | --- |
| [La Corse Capable — énergie, mobilité, logistique et valeur locale](../campaigns/corse-capable-energie.md) | 9 octobre 2026 ; `working-paper — public campaign note` ; revue non réalisée | Une ressource physique (soleil, véhicule, épargne, réseau) n'est pas encore une capacité ; combiner énergie, stockage, trajets, livraison, besoins humains et contrôle de la valeur. Hypothèses d'expérimentation à Corte ; FractaVolta présenté comme démonstrateur possible, non comme résultat acquis. | **Livre 03/05/06/09/10** : exemple transversal du passage ressources → capacités et du contrôle anti-capture ; **Magazine** : chronique datée des hypothèses et tests ; **Annexes** : protocole, données, calculs, risques juridiques et résultats effectivement observés |

**Interprétation du relevé shell :** la recherche couvre les fichiers textuels versionnés `.md/.yml/.yaml` des dépôts locaux parcourus et plusieurs variantes littérales de « note de campagne ». Elle ne démontre pas l'absence d'autres notes portant des désignations différentes, de fichiers hors Git ou de documents non textuels. Les mentions « note n°1 » et « note n°2 » ne sont pas identifiées dans ce relevé. Les références `note en délibéré` des dossiers judiciaires sont hors périmètre des Notes de Campagne.

**Correction méthodologique :** le dossier énergie du 9 octobre complète la note EDF de juin : ce sont **deux documents distincts**, l'un consacré à une architecture territoriale (énergie, mobilité et logistique), l'autre au cas d'un opérateur et du stockage potentiel. Il ne faut pas les fusionner ni présenter l'une comme une version de l'autre sans preuve.

## Trois acquis transversaux à ne pas perdre

**1. Éviter les fausses oppositions.** Le GR20 montre qu'une restriction peut être légitime à un point de saturation tout en restant insuffisante pour une politique de capacité ; la note anti-mafieuse refuse que le besoin de protection justifie une surveillance générale ; le statut de résident exige d'éprouver les effets d'une différenciation plutôt que d'en présumer le bien-fondé. Ces exemples illustrent les tensions et leur examen, sans produire un verdict automatique.

**2. Rendre le concept d'effectivité visible sur des terrains hétérogènes.** Une même question — quels possibles s'ouvrent, pour qui, à quel coût, avec quels recours ? — s'applique à la montagne, à l'énergie, à l'accès au logement et à la gouvernance publique. Cela soutient la grammaire d'échelles du Livre, sans supposer une causalité identique partout.

**3. Ne pas confondre la Note, ses preuves et les résultats.** La note EDF comprend des hypothèses techniques et des demandes de vérification ; le GR20 propose des dispositifs ; la note de résident propose des critères d'évaluation. Leur présence dans le Corpus n'atteste pas l'implémentation ou la validité empirique de chaque mécanisme. La Note n°3 doit conserver son statut de validation et ses métadonnées hétérogènes tant que la provenance exacte n'est pas réconciliée.

## Décisions éditoriales proposées

- **Livre :** faire de ces quatre notes antérieures un jeu de cas contrastés et récurrents, principalement dans les chapitres 02–06, 09 et 10 ; ajouter des paragraphes illustratifs brefs avec renvois vers les dossiers complets. Ne pas déplacer les Notes originales.
- **Magazine n°1 :** ouvrir une rubrique de **rétrospective des Notes de Campagne 2026** en précisant les dates et statuts des textes, distincte de l'actualité du 26–28 octobre. Aucun « n°2 » fictif.
- **Annexes :** construire une table de provenance source → publication dérivée → pièces justificatives → statut de validation ; traiter en priorité le dossier EDF (dates, hypothèses et validation), le statut de résident (droit et effets), le GR20 (contraintes environnementales) et la traçabilité (protection des personnes).
- **Sources en amont :** `research/index.md` pointe vers un fichier racine `cas_edf.md` qui n'est désormais qu'un avis de déplacement : utiliser `research/cas_edf.md` comme dossier technique et `research/cas_edf_blogpost.md` comme Note dérivée. Corriger l'index à sa prochaine régénération plutôt que réinventer un document manquant.

## Suite et limites

Recherche d'autres notes numérotées ou simplement étiquetées `campaign_note` dès retour de la recherche globale GitHub ; contrôle des historiques et des produits effectivement publiés ; confrontation source-first des calculs, références et dates avant de reprendre des chiffres dans le Livre. Les titres « n°1 », « n°2 », « n°3 » appliqués aux **Notes de Campagne** ne sont pas des numéros gelés du **Magazine**.

Aucun gel éditorial ni déploiement public n'est autorisé par cet inventaire.

## Recherche de filiation — compléments du 28 octobre (Git et Cogentia)

- Le `git grep` multi-dépôts fourni depuis Fracta2 a identifié six Notes ou textes désignés comme tels ; il confirme également que le numéro **3** de la Note EDF est explicite, mais ne trouve pas les chaînes littérales « Note de Campagne n°1 » et « n°2 ». **Le rang des Notes 1 et 2 demeure UNKNOWN**.
- La recherche de **messages de commits** GitHub a produit un commit pertinent pour « note de campagne » ([2ae38f0](https://github.com/JeanHuguesRobert/barons-Mariani/commit/2ae38f0a688c3c6e81ca9c513dea9b3673901bce)), sans établir l'identité des notes 1 et 2. Une recherche de messages de commits n'équivaut ni à `git log -S` ni à l'historique exhaustif des chemins.
- Le MCP Cogentia `grep` fournit 26 occurrences de « note de campagne » dans ses documents actifs et une occurrence de `campaign_note` (traçabilité anti-mafieuse). Sa recherche sémantique sur la filiation a retourné une **continuation requise** (`ctn_f9f4f243` ; embeddings absents) et aucun résultat documentaire utilisable à ce stade.
- L'appel `cogentia_john_run` est techniquement **réussi**, mais le gestionnaire par défaut exécuté est `mock.echo` : 0 appel de capacité et aucune exploration du Corpus. **Ce n'est pas une enquête réalisée par l'Agent JHN**.

### Seconde passe reproductible recommandée sur Fracta2

Pour vérifier des fichiers **supprimés ou renommés** avant de conclure sur les numéros 1 et 2 :

```bash
cd /srv/cogentia/repos/barons-Mariani
# Tous les chemins historiques pertinents, sans réécrire le dépôt.
git log --all --name-status --pretty=format:'COMMIT %h %ad %s' --date=short -- \
  'research/*campagne*' 'research/*campaign*' 'projects/capable/*' \
  | grep -Ei '^(COMMIT|[ACDRM][0-9]*[[:space:]])|campagne|campaign' | head -250
# Commits dont le diff a ajouté/supprimé une mention exacte.
git log --all --oneline -i -G 'note.{0,20}de campagne|campaign.note' -- '*.md' | head -100
# Statut du dépôt (permet de dater l'état local examiné).
git rev-parse HEAD; git status --short
```

**Ne pas confondre** résultats de recherche dans les messages, occurrences dans l'état actuel et historique de contenu. Le statut exhaustif reste ouvert jusqu'à inspection de ce journal. Aucun texte n'est à renuméroter rétrospectivement.

## Sédimentation effectuée — 28 octobre 2026

Une première série de raccords narratifs, **réversibles et non doctrinaux**, a été intégrée aux chapitres du Livre :

- `manuscript/04-liberte-egalite-fraternite-effectives.md` — traçabilité anti-mafieuse et tension entre protection et surveillance (commit `1029549`).
- `manuscript/05-machines-et-correction.md` — GR20, quotas, exploration d'autres possibilités (commit `3ec9c70`).
- `manuscript/06-fractalite-et-echelles.md` — comparaison montagne, statut de résident et énergie/logistique (commit `db5d81b`).
- `manuscript/09-communs-et-moyens.md` — combinaison énergie, stockage, trajets et valeur locale ; renvoi au dossier technique EDF (commit `81c89c2`).

**Limites :** ces ajouts ne valident pas les hypothèses empiriques des Notes et ne remplacent pas leurs dossiers probatoires. Les chapitres 02, 03 et 10 restent à confronter notamment à la Note du 27 octobre et au cas du statut de résident. **Aucun numéro gelé** et aucune publication HTML déclenchée.

## Seconde passe de sédimentation — chapitres 02, 03 et 10

- **02** — compétence attribuée, capacité réelle d'exercice et possibilité de contrôle ; sources : Note sur le statut de résident et Note du 27 octobre ; commit `a6a2005`.
- **03** — symétrie de l'évaluation des normes uniformes et différenciées, sans attribuer de résultat à une règle non appliquée ; source : Note sur le statut de résident ; commit `f3b5d9f`.
- **10** — exemple d'instruction du statut de résident ; qualification des quatre obligations de responsabilité d'effectivité comme **exigences doctrinales proposées**, sans prétention à une consécration identique en droit positif ; commit `51f9e32`.

Contrôle direct GitHub après modifications : les six sources de campagne et le dossier technique EDF consultés, ainsi que l'amendement d'effectivité 72-5, sont accessibles sur `main`. Ce contrôle est un **contrôle d'existence documentaire**, non une validation scientifique des contenus ni un contrôle automatique de tous les liens du manuscrit.

Ces sept enrichissements (chapitres 02, 03, 04, 05, 06, 09, 10) sont une première sédimentation éditoriale. Les choix d'intégration de l'essai philosophique, l'éventuel changement d'architecture du Livre et le gel du premier numéro demeurent distincts.
