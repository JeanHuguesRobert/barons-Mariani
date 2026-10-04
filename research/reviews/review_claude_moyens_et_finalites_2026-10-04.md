---
title: "Revue adverse externe — Moyens et finalités (v0.2-draft)"
language: "fr"
status: "review — non décisionnelle ; arbitrage humain requis"
review_target:
  repository: "JeanHuguesRobert/barons-Mariani"
  files:
    - "research/moyens_et_finalites.md"
  received_as: "copie par fichier : moyens_et_finalites_v0.2-draft_frontmatter-canonique.md"
  reviewed_version: "v0.2-draft"
  reviewed_commit: "non disponible — le chemin research/moyens_et_finalites.md renvoie 404 sur la branche main publique (vérifié le 2026-10-04) ; copie non hachée par moi (le fichier n'était pas accessible sur disque dans cette passe)"
  review_scope: "conceptual / constitutional / electoral / empirical / methodological"
  requested_by: "Jean Hugues Noël Robert"
  reviewer: "Claude Sonnet 5.5 (Anthropic), claude.ai, avec recherche et lecture web"
  review_date: "2026-10-04"
  human_validation_required: true
---

# Revue adverse externe — *Moyens et finalités* (v0.2-draft)

**Avertissement.** Je ne suis pas juriste. Cette revue est conceptuelle et méthodologique, pas un avis juridique. Le nom de fichier `review.md` suit le contrat `reviewer.md` (pas de version dans le nom) ; l'identification de la cible est dans le frontmatter.

## 0. Déclaration de décorrélation et test de Packet Closure

**Exécutant et accès.** Claude Sonnet 5.5, avec recherche web et lecture de pages publiques. Pas de dépôt Git cloné, pas d'accès aux sources privées.

**Exposition préalable (matérielle).**
1. J'ai revu, dans la même session et pour le même auteur, la **v0.1** de ce document (30 septembre). Cette revue figure dans une session de chat, non dans le dépôt. Je ne suis donc **pas** un lecteur vierge de la v0.1.
2. J'ai aussi revu dans la session un autre paquet du même auteur (« Packetization + Delimited Continuations »).
3. Le Corpus a déjà intégré des revues Claude d'autres documents (journal de version de l'amendement d'effectivité : « revue externe Claude », « seconde passe Claude », « revue adverse Claude »). Mon indépendance **par rapport au Corpus** est donc plus faible que mon indépendance par rapport à l'assistant de rédaction.

**Décorrélation par rapport à la rédaction.** Le frontmatter indique `ai_assisted_by: GPT-5.6 Sol`. Si cela couvre toute la rédaction, nous sommes de familles de modèles différentes, ce qui est un point favorable. Je ne peux pas le vérifier. Degré global : **moyen**.

**Sources résolues pour cette revue.** Contrat `cogentia/prompts/reviewer.md` ; protocole `barons-Mariani/research/review_protocol.md` ; `cogentia/research/documents_as_cognitive_packets.md` (v0.6) ; `cogentia/research/trace_treatment_packet.md` (v0.1) ; `barons-Mariani/research/autonomia/amendement_effectivite_article_72-5.md` (v0.5-rc1) ; communiqués et presse sur la décision du TA de Bastia ; textes sur le délai de protestation devant le Conseil constitutionnel.
**Non résolues ou non tentées :** `projects/capable/doctrine.md`, `principe_effectivite.md`, `triangulation_du_reel.md`, `grammaire_autonomie_de_capacite.md`, `tensions_liberte_egalite_fraternite_effectives.md`, `convergence_scrutin_requete_amendement_qpc_2026-09-29.md` ; le texte de la décision du TA ; l'issue `#88` (extrait seulement).

### Packet Closure `Closed(p, h, E)` — résultat

`p` = la Capsule reçue ; `h` = moi, Reviewer externe ; `E` = la copie Markdown + les références publiques résolubles.

| Critère (qualification d'une Capsule, `documents_as_cognitive_packets` §4) | Constat sur la v0.2 |
|---|---|
| Identité | Pas de `packet_id`. Le Corpus déclare lui-même l'identité stockage-indépendante « provisoire, pas encore d'ID » |
| Frontière causale | `causal_frontier: "v0.2-draft-after-corpus-reassessment"` est une étiquette, non une référence vérifiable (pas de commit, pas de hachage) |
| Contrat de handler | Dans la prose (§18), pas dans le frontmatter ; pas de bloc `closure` (mode, handler admissible, environnement, références) |
| Clôture | Mode non déclaré. Le chemin `Ithaca` / `review_target.files` est **404** sur `main` : la clôture référentielle échoue aujourd'hui, la clôture par copie fonctionne |
| Continuation | `current_phase: external-review` et §21 : présent, mais la v0.2 a **supprimé** les champs de la v0.1 `packet.state`, `packet.next_handler_role`, `packet.resumable` |
| Retour | `ithaca` présent (mais non résoluble publiquement) |
| Contraintes / autorité | Conflit d'intérêt épistémique déclaré en §18.2 ; pas d'autorité de mandat dans le frontmatter |

**Verdict.** Par copie, j'ai pu reconstruire la thèse, la cible et la tâche **sans contexte conversationnel privé de la rédaction**. Mais (a) ma propre mémoire de la v0.1 contamine le test ; (b) il m'a fallu **deviner les URL** des contrats (`JeanHuguesRobert/cogentia/prompts/reviewer.md` n'est pas une URL ; la règle de résolution n'est pas déclarée) ; (c) la clôture référentielle est impossible tant que le fichier n'est pas publié. **Résultat : clôture par copie suffisante, clôture référentielle absente, test non propre.**

**Coût de clôture observé.** 0 message d'explication de l'auteur ; 5 matérialisations de références publiques pour appliquer le contrat et le protocole ; 1 recherche externe pour l'état du contentieux. Les deux revues précédentes (mon `v0.1` et celle d'un autre Reviewer pour d'autres documents) n'étaient pas dans l'environnement `E`.

## 1. Résumé de la thèse

Inchangée sur le fond par rapport à la v0.1 : un moyen institutionnel `M` légitimé par une finalité `F` peut, par ses effets, réduire les capacités nécessaires à `F`. Les sections 2 à 15 (capacité = voie praticable, personnelle/systémique, autonome/dépendante, H1–H6) sont **textuellement identiques** à la v0.1. Ce qui change en v0.2 :
- le statut du document (Capsule candidate d'un Logical Cognitive Packet, §0) ;
- une analogie finalité / incarnation (§1 bis) ;
- une chaîne de traitement des traces (§14 bis) ;
- IA11 et IA12 dans la revue interne ;
- une politique de cycle de vie (§19 bis) ;
- l'exigence qu'un Reviewer évalue la Packet Closure (§18.1).

## 2. Symmetry test

Peut-on reconstruire la thèse, les distinctions principales et la structure d'argument à partir du seul texte ? **Oui** pour la thèse et les distinctions de fond. **Non** pour l'architecture ajoutée en v0.2 : Logical Packet, Packet Capsule, causal frontier, Review / Objection Packet, Hypothesis Packet, Trace Treatment Packet et la politique `DISCARD / COOL / SUPERSEDE / ERASE` ne sont définis que par renvoi à `cogentia:research/documents_as_cognitive_packets.md` et `trace_treatment_packet.md`. Ce ne sont pas des produits d'un document source symétrique.

## 3. Stabilized concepts

- Séparation capacité personnelle / systémique (§4.1).
- Séparation liberté / secret / imputabilité (§4.3) — sous réserve de mon E1 de la v0.1, non corrigé.
- Gradation friction, désajustement, inversion (§12).
- Table IA : l'intention de la règle N est claire.
- Dans la v0.2 : la distinction entre une **représentation documentaire** et le **travail** qu'elle porte est une bonne hygiène (voir tout de même D2).

## 4. Fragile or ambiguous concepts

Tout ce qui était fragile en v0.1 le reste (capacité, dépendance, effectivité en trois sens, F non déterminée : voir mon `review` v0.1). En v0.2 s'ajoutent :
- **« Identité du travail cognitif »** et **« continuité logique »** (§0) : critère circulaire (voir D2).
- **« Incarnation institutionnelle »** (§1 bis) : métaphore qui introduit une ontologie de l'identité alors que l'objet est un moyen institutionnel.
- **« Causal frontier »** : défini comme étiquette, non comme point vérifiable.

## 5. Conceptual drift risks

| Dérive | Risque |
|---|---|
| Packet logique ↔ document ↔ institution | analogie utilisée comme argument (§1 bis) |
| Trace ↔ preuve | le §14 bis dit « pas une preuve », mais ne traite que le sens confirmant |
| Revue ↔ rendement assimilé | une revue « assimilée » par la partie revue n'est plus auditable une fois détruite |
| Capsule ↔ document public de recherche | le document est `visibility: public`, `document_kind: research-paper` et s'adresse à des publicistes ; son enveloppe suppose un lecteur du Corpus |

## 6. Errors

```text
ID: E-A
Localisation: §19 (« arbitrage humain → v0.2 ») et §21 (« THEN … → v0.2 »)
Type: factuel (incohérence interne)
Constat: le document est lui-même la v0.2. Les deux sections décrivent la version
  suivante comme « v0.2 ».
Gravité: basse
Action: remplacer par « v0.3 » (ou « version suivante »).
```

```text
ID: E-B
Localisation: §0 (« sont des incarnations ou Capsules successives d'un même travail tant que
  sa continuité logique est préservée »)
Type: inférentiel
Constat: l'énoncé présente comme acquise une identité à travers les Capsules. Le Corpus
  source la déclare « provisoire — pas encore d'identifiant indépendant du stockage »
  (documents_as_cognitive_packets v0.6, frontmatter) et laisse RT-006 (test d'identité du
  fichier) ouvert. Le critère « continuité logique » n'est pas défini : il suppose ce qu'il
  doit établir.
Gravité: moyenne
Action: reformuler : « l'hypothèse de travail est que… ; identité provisoire, non testée »,
  et ne pas l'utiliser comme prémisse en §1 bis.
```

Mon **E1 de la v0.1** (transfert de l'interdiction du mandat impératif au grand électeur, §4.3) reste applicable tel quel : la section est inchangée. Je ne le recompte pas (Rule N).

## 7. Novel objections (delta v0.2)

Chaque finding : localisation → objection → preuve → gravité → action.

### D1 — L'ontologie importée est hors domaine et aggrave l'inflation terminologique
- **Localisation :** §0, §1 bis, §14 bis, §19 bis, IA11, IA12, §18.1, frontmatter `x-cognitive-packet`.
- **Objection :** environ un quart du texte nouveau décrit l'infrastructure du Corpus (Packet, Capsule, frontière causale, Ithaca, TTP, cycle de vie), et **aucune** de ces notions n'est utilisée dans l'analyse de H1–H6. La concession IA7 (inflation) est `load-bearing` et ouverte ; la v0.2 ajoute une dizaine de termes sans les soumettre au test d'utilité qu'IA7 prescrit.
- **Preuve :** les sections 2–15 sont identiques à la v0.1 et ne mentionnent ni Packet ni Capsule. Le document est classé `research-paper`, `visibility: public`.
- **Gravité :** moyenne à haute.
- **Action :** déplacer l'enveloppe et la politique de cycle de vie dans une annexe ou une note de méthode séparée (ce que la règle « source / produit dérivé » du protocole recommande déjà), et garder l'article lisible sans l'ontologie.

### D2 — Le critère d'identité est circulaire et déjà connu sous un autre nom
- **Localisation :** §0.
- **Objection :** « même travail tant que la continuité logique est préservée » ne dit pas ce qui compte comme continuité. Le problème est ancien : FRBR / IFLA-LRM (œuvre, expression, manifestation, exemplaire), les identifiants persistants (DOI, Handle), W3C PROV (spécialisation, `alternateOf`), la théorie archivistique de l'identité du document [mémoire, non revérifié]. Ces cadres ont les mêmes critères flous d'identité de l'« œuvre ». L'analogie Packet / Capsule / document / placement est leur transposition.
- **Gravité :** moyenne.
- **Action :** soit citer ces cadres et dire ce que l'ontologie du Corpus ajoute, soit supprimer le paragraphe d'identité de ce document.

### D3 — « Stabilité de la finalité, révisabilité de l'incarnation » est un principe normatif tiré d'une analogie, en tension avec la F sous-déterminée
- **Localisation :** §1 bis.
- **Objection :** le principe suppose une finalité `F` stable et déterminée. Or ma revue v0.1 (N11) a montré que `F` est souvent plurielle et construite par l'analyste. Le droit constitutionnel fait évoluer les finalités par interprétation (création d'objectifs à valeur constitutionnelle, réinterprétations). La tradition pragmatiste va plus loin : fins et moyens forment un continuum et les fins se révisent à travers les moyens (Dewey ; Lindblom, « muddling through ») [mémoire, non revérifié]. La « symétrie des deux erreurs » du §1 bis (garder un moyen / abandonner une finalité) est en outre un homme de paille : l'abandon d'une finalité à cause de l'échec d'un moyen n'est défendu par personne dans le document.
- **Gravité :** moyenne.
- **Action :** reformuler en « stabilité **relative** de la finalité, révisable par ses procédures propres », et la subordonner à la règle N11 (F tirée de sources primaires).

### D4 — §14 bis valide une hypothèse avec une méthode elle-même non validée, et ne traite que la trace qui confirme
- **Localisation :** §14 bis.
- **Objection :** (i) le Trace Treatment Packet est `unreviewed`, version 0.1, daté du **30 septembre 2026**, avec ses trois Reality Tests encore à faire (`RT-TTP-001/002/003`) ; le document l'emploie comme procédure épistémique. (ii) L'exemple choisi est la déclaration de refus de présentation (« je refuse parce que mon nom serait publié »). C'est un **autodiagnostic de motif**, dont la validité est connue pour être limitée (Nisbett et Wilson, 1977 ; biais de désirabilité sociale) [mémoire, non revérifié]. (iii) La chaîne ne montre pas comment traiter une trace **défavorable** à H3 (par exemple le nombre de candidats qualifiés avant et après 2016, voir mon N8 de la v0.1). L'asymétrie viole l'esprit d'IA1.
- **Gravité :** moyenne.
- **Action :** (a) dire que la méthode est expérimentale et non validée ; (b) fournir un exemple symétrique, avec une trace défavorable à H3 ; (c) mentionner des outils éprouvés pour l'étape `TEST` : matrice des hypothèses concurrentes (Heuer, ACH), expériences de liste pour les attitudes sensibles, grilles de fiabilité de source (Admiralty/STANAG 2511) [mémoire, non revérifié].

### D5 — La politique « revue brute éliminable » s'applique mal à ce document, et viole le test §13 du document lui-même
- **Localisation :** IA12, §19 bis.
- **Objection :** la règle permet de `DISCARD` une revue brute une fois ses findings « assimilés ». Mais (i) l'assimilation est faite par la **partie revue** (Redactor et auteur, avec conflit d'intérêt déclaré) : rien ne permet ensuite de vérifier que les dispositions reflètent fidèlement des objections défavorables. (ii) Le §13 (question 7) du document demande : existe-t-il un moyen moins destructeur ? Ici oui : `COOL / ARCHIVE` (§19 bis). La première question du §1 (« M détruit quelle information ? ») s'applique directement : détruire la revue brute détruit l'information qui permet d'auditer l'assimilation. (iii) **Démonstration par l'exemple :** ma revue de la v0.1 n'apparaît ni dans `review.reviewed_by` (`[]`), ni dans `version_history`, ni dans une table de dispositions de la v0.2 ; le champ `review_lineage` de la v0.1 a disparu du frontmatter. La perte de traçabilité décrite se produit déjà.
- **Gravité :** moyenne à haute (touche la crédibilité de toute la chaîne de revue).
- **Action :** conserver les revues brutes ayant un conflit d'intérêt déclaré en archive hachée (SHA-256 consigné dans `review.reviewed_by`) ; retenir au minimum la liste verbatim des findings avec gravité **avant** disposition ; réintroduire `review_lineage`.

### D6 — Le frontmatter « canonique » est en recul par rapport au contrat de Capsule du Corpus
- **Localisation :** frontmatter, `x-cognitive-packet`.
- **Objection :** voir le tableau du §0. Les champs `packet.state`, `packet.next_handler_role`, `packet.resumable` de la v0.1 ont été retirés ; `packet_id`, `capsule_id`, `closure.*`, `routing.next_handler_capability` n'existent pas ; `causal_frontier` n'est pas vérifiable ; `Ithaca` et `review_target.files` pointent vers un fichier non publié.
- **Gravité :** moyenne.
- **Action (frontmatter minimal réparé, d'après l'exemple du Corpus lui-même) :**

```yaml
x-cognitive-packet:
  candidate: true
  packet_id: "provisional-no-storage-independent-id"
  capsule_id: "moyens_et_finalites@v0.2-draft+sha256:<hash>"
  causal_frontier: "sha256:<hash de cette copie>"   # ou commit exact
  closure:
    mode: inline            # référentiel après publication
    admissible_handler: "decorrelated-reviewer / reviewer.md v0.1 / review_protocol.md v0.1"
    environment: "public GitHub JeanHuguesRobert/{cogentia,barons-Mariani} + web"
    refs:
      - "https://github.com/JeanHuguesRobert/cogentia/blob/main/prompts/reviewer.md"
      - "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/review_protocol.md"
  routing:
    next_handler_capability: "decorrelated-adversarial-review"
  return:
    ithaca: "<chemin ou URL publiée, ou issue>"
  state: "drafted_internal_review_pending_external"
  resumable: true
```

### D7 — L'amendement et le contentieux ont des échéances datées que la v0.2 n'utilise pas
- **Localisation :** §8, §9, §10, §15-H4.
- **Constat :**
  - **Contentieux :** la requête devant le Conseil constitutionnel doit être enregistrée au plus tard le **mercredi 7 octobre 2026 à 18 h** (source d'avocat ; les pièces de l'auteur citent la même échéance). La v0.2 est datée du 4 octobre : trois jours.
  - **Amendement (H4) :** d'après la note d'amendement de l'auteur, commission des lois du Sénat le 21 octobre, **dépôt des amendements de séance au plus tard le 23 octobre à 12 h**, séance le 26 octobre (non revérifié par moi).
- **Objection :** ces dates font de H4 un **Reality Test avec prédiction datée** (« un sénateur ou le Gouvernement dépose-t-il un amendement d'effectivité avant la clôture ? »), mais le document le qualifie toujours de « Reality Test en cours » sans prédiction consignée.
- **Gravité :** moyenne.
- **Action :** consigner **avant** le 23 octobre la prédiction et le critère d'interprétation de H4 (voir §12). Rappel : le dossier contentieux ne doit pas s'appuyer sur H1 ni sur ce document (le §0 le dit lui-même).

### D8 — Une incohérence dans le document de l'amendement se répercute sur la référence faite en §9
- **Localisation :** `amendement_effectivite_article_72-5.md` (en-tête : « Alinéa 6, première phrase » ; §5 : « cinquième alinéa »).
- **Objection :** le même texte est localisé à l'alinéa 6 dans le dispositif parlementaire et au cinquième alinéa dans la note de justification. Le §9 du présent document s'appuie sur ce texte comme test récursif.
- **Gravité :** basse à moyenne (précision légistique, fragile devant un dépôt réel).
- **Action :** vérifier la numérotation sur le texte transmis au Sénat (n° 782) avant dépôt. Cette observation concerne le document source de l'amendement et non ce papier ; je ne l'ai pas tranchée.
- **Complément :** la note d'amendement a déjà intégré deux points que mon examen de la v0.1 mentionnait (collision du mot « capacité » avec la capacité juridique des personnes ; décision du Conseil constitutionnel de 2018 sur la fraternité). La v0.2 de *Moyens et finalités* ne les reprend pas : ils devraient y être propagés.

## 8. Concessions assessed

| Concession | Classification | Évaluation | Obligation restante |
|---|---|---|---|
| IA11 (document ≠ Packet logique) | `corrected` | La distinction est écrite, mais l'identité entre Capsules est posée sans critère (E-B, D2) | Reformuler en hypothèse |
| IA12 (rétention des revues) | `integrated` → **load-bearing** (reclassé) | La crédibilité de « revue externe » dépend de l'auditabilité de l'assimilation ; la politique la compromet (D5) | Archive hachée ; liste verbatim ; `review_lineage` |
| IA2, IA4, IA7 | `load-bearing` | Inchangées ; IA7 aggravée par D1 | Voir ma revue v0.1 |
| IA3, IA6, IA9 | `reformulate` / `integrated` | Toujours non visibles dans le corps du texte | Voir ma revue v0.1 |
| IA1, IA5, IA8, IA10 | `bounding` / `integrated` | Inchangées | — |

## 9. Prior art / état de l'art (delta)

| Notion v0.2 | Antériorités | Verdict |
|---|---|---|
| Identité du travail à travers ses représentations | FRBR / IFLA-LRM ; DOI / Handle ; W3C PROV ; identité archivistique | recoupement fort, non cité |
| `DISCARD / COOL / SUPERSEDE / ERASE` | gestion des enregistrements (ISO 15489, tableaux de conservation, sort final) ; droit à l'effacement (RGPD, art. 17) | recoupement fort, non cité |
| Revue → dispositions → intégration | lettres de réponse point par point en évaluation par les pairs ; triage d'issues | recoupement fort |
| Chaîne de traitement des traces | analyse du renseignement (ACH, grilles de fiabilité) ; chaîne de conservation de la preuve | recoupement fort |
| Finalité stable / incarnation révisable | Dewey (continuum fins–moyens) ; Lindblom | tension, non cité |

Sources effectivement consultées dans cette passe : contrat reviewer, protocole de revue, `documents_as_cognitive_packets` v0.6, `trace_treatment_packet` v0.1, note d'amendement v0.5-rc1, communiqués et presse sur le TA de Bastia. Le reste est de ma mémoire.

## 10. Blind spots

- **Auto-application du §13** à la politique de cycle de vie (D5) : le document n'applique pas à son propre dispositif la question « un moyen moins destructeur existe-t-il ? ».
- **Public visé :** un article destiné à des publicistes porte une enveloppe écrite pour un lecteur du Corpus.
- **Asymétrie des traces :** seule une trace qui confirme est décrite (D4).
- **Les échéances réelles** (D7).

## 11. Correlation risks

1. **Mémoire de la v0.1** (la mienne) : je risque de confirmer mes propres findings plutôt que de relire à neuf.
2. **Corpus partiellement façonné par des revues Claude** (voir §0).
3. **Cadre du contrat** : les douze questions et la structure de livrable orientent la lecture vers le cadre de l'auteur.
4. **Cadrage des antériorités** de mémoire, biaisé vers le canon anglophone et français.
5. **Test de clôture non propre** (mémoire ; URL devinées).

## 12. Booster opportunities

1. **Pré-enregistrer H4** avant le 23 octobre 12 h : prédiction (dépôt d'un amendement d'effectivité par un sénateur ou le Gouvernement : oui / non), critère d'interprétation (si non : explication par le manque de canal ou par le désintérêt ?), et ce qui compterait comme réfutation.
2. **Test de clôture honnête** : refaire le Reality Test avec un Reviewer qui n'a rien vu de la v0.1, une fois le fichier **publié** (clôture référentielle) et le frontmatter réparé (D6).
3. **Archive hachée des revues** : transforme IA12 en démonstration plutôt qu'en vulnérabilité.
4. **Séparer** le papier de recherche et l'annexe de méthode (D1).
5. **Exemple symétrique pour §14 bis** : une trace défavorable à H3 traitée par la même chaîne.

## 13. Falsification opportunities

- **Pour le dispositif d'enveloppe :** si une revue fondée sur le seul texte de fond (sections 2–15), sans §0 ni frontmatter, produit les mêmes findings, l'enveloppe n'ajoute pas de bénéfice mesurable.
- **Pour IA12 :** si un relecteur tiers, ayant seulement la table de dispositions, ne peut pas retrouver les findings défavorables d'une revue détruite, la politique est auditablement insuffisante.
- **Pour H4 :** non-dépôt d'un amendement par un sénateur avant la clôture (voir §12) : la redondance existe sur le papier mais n'est pas exercée.

## 14. Signal / noise report

- **Intégrer maintenant :** E-A, E-B, D6 (frontmatter), D5 (archive hachée et `review_lineage`).
- **Reformuler avant intégration :** D3, D4.
- **Garder comme piste :** D2 (cadres d'identité), D1 (séparation en deux documents).
- **Arbitrage humain requis :** D1, D5, D7.
- **À ignorer comme bruit :** les points stylistiques de la v0.1 déjà dispositionnés.
- **Rule N :** mes findings de la v0.1 (E1, N1–N12) **ne sont pas recomptés** ; ils restent ouverts car le texte concerné est inchangé et aucune disposition n'est enregistrée dans la v0.2.

## 15. Structural improvements

1. Ajouter à la v0.3 une **table de dispositions** de ma revue v0.1 (au sens du §6 du protocole : objection, source, gravité, décision, effet) ; sinon la revue est « non intégrée » au sens du protocole.
2. Déplacer l'architecture Packet (§0, §1 bis, §14 bis, §19 bis) vers une annexe ou un document de méthode.
3. Remplacer l'étiquette `causal_frontier` par un hachage ou un commit.
4. Publier le fichier à son chemin avant de redemander un test de clôture référentielle.
5. Corriger les « → v0.2 » obsolètes.
6. Réconcilier le titre de §16 (« passe corrélée v0.1 ») avec l'ajout d'IA11–IA12 (items de la v0.2).

## 16. Internal corpus references to strengthen

- `review_protocol.md` §6 : table d'intégration obligatoire (pas encore produite pour mes findings).
- `review_protocol.md` §3 : statut `non_integrable_until_routed` — à vérifier pour cette revue : le ciblage est explicite mais `reviewed_commit` n'existe pas.
- `documents_as_cognitive_packets.md` §4 (test de qualification) et §22 (dispositions de RT-001) : modèle à suivre pour la v0.3.
- Note d'amendement §25 : bon exemple de table d'arbitrage à répliquer ici.

## 17. Possible derived products

Prématuré tant que D1 n'est pas tranché. Seuls deux produits sont à faible risque : une **note de méthode** isolant l'enveloppe Packet, et une **fiche de dispositions** de la v0.2.

## 18. Continuation report

- **Points to preserve :** les sections 2–15 (nettes) ; la déclaration d'intérêt (§18.2) ; l'esprit de la règle N ; l'exigence d'un test de clôture.
- **Points to correct :** E-A, E-B, D6, et E1 de la v0.1.
- **Points to deepen :** D3, D4, D5.
- **Conceptual risks :** inflation (D1) ; circularité d'identité (D2).
- **Stylistic risks :** densité du frontmatter pour un lecteur non Corpus.
- **To integrate now :** E-A, E-B, D6, archive hachée.
- **To defer :** D1 (décision de séparation), D2 (cadres d'identité).
- **Next recommended action :** publier le fichier, réparer le frontmatter, produire la table de dispositions de mes deux revues, puis relancer un Reviewer vierge.

## 19. Recommandation

**Ne pas stabiliser ; passer en v0.3.** La v0.2 est un changement d'**enveloppe**, pas une réponse aux findings de fond : les sections qui portaient mes objections (H1 règle/standard, H2 sans mécanisme, H3 déjà instrumentée, E1) n'ont pas bougé. L'enveloppe ajoutée est utile à l'infrastructure du Corpus mais coûte à la lisibilité du papier et contient trois fragilités propres (D2, D4, D5). Cette recommandation ne décide pas de l'intégration.

## 20. Yield report

```text
Errors identified (v0.2 delta): 2
  factual: 1 (E-A)
  inferential: 1 (E-B)
  attributive: 0
  (E1 de ma revue v0.1 reste ouvert ; non recompté)
Claims marked unverified: 5
Novel objections (delta): 8 (D1–D8)
Concessions assessed: 9
Concessions reclassified to load-bearing: 1 (IA12)
Blind spots: 4
Correlation risks: 5
Falsification opportunities: 3
Booster opportunities: 5
Structural improvements: 6
```

## 21. Final compliance check

- [x] Nom de fichier conforme (`review.md`, sans version dans le nom).
- [x] Analyse complète dans le fichier ; la réponse de conversation ne contient pas d'analyse absente d'ici.
- [x] Pas de recommandation d'archiver tous les tâtonnements conversationnels (le contraire : une archive hachée des revues avec conflit d'intérêt seulement).
- [x] Logique source / produit dérivé préservée (D1).
- [x] Ancrage humain de la décision préservé ; le Reviewer ne décide pas de l'intégration.
- [x] Distinction clôture / révisabilité préservée.
- [x] Discipline signal / bruit (§14).
- [x] Lien de téléchargement fourni dans la réponse (carte de fichier).
- [ ] **Réserve :** `reviewed_commit` indisponible (fichier non publié) ; ciblage par version et nom de copie ; hachage non produit.

## 22. Return packet

```yaml
result: completed
reviewer_decision: "revise (v0.3) — ne pas stabiliser"
packet_closure:
  by_copy: "sufficient to produce the review"
  by_reference: "absent — target path 404 on public main; contract URLs inferred"
  test_clean: false
  reason: "reviewer retains prior-session memory of v0.1; resolver rules undeclared"
strongest_finding: >
  La politique de destruction des revues brutes (IA12/§19 bis) viole le test du document
  (§13 q.7, moyen moins destructeur : COOL/ARCHIVE) et la lignée de ma revue v0.1 est déjà
  absente de la v0.2 : la perte de traçabilité décrite se produit.
sources_or_regions_still_unchecked:
  - "projects/capable/doctrine.md, principe_effectivite.md, triangulation_du_reel.md"
  - "texte de la décision du TA de Bastia ; issue #88 (extrait seul)"
  - "numérotation de l'alinéa dans le texte n° 782 du Sénat"
next_recommended_action: >
  Publier le fichier ; réparer le frontmatter (D6) ; produire la table de dispositions de mes
  deux revues ; pré-enregistrer H4 avant le 23 octobre 12 h ; relancer un Reviewer vierge.
human_arbitration_required: true
```