---
review_target:
  repository: "JeanHuguesRobert/barons-Mariani"
  files:
    - "research/moyens_et_finalites.md"
  reviewed_version: "v0.3-draft"
  reviewed_commit: "38500f09a3656963dbf9dbaa1a3c96283907a6cb"
  review_scope: "conceptual / constitutional / electoral / empirical / methodological"
  requested_by: "Jean Hugues Noël Robert"
  reviewer: "Grok 4.7"
  review_date: "2026-10-05"
  human_validation_required: true
review_contract: "JeanHuguesRobert/cogentia/prompts/reviewer.md @ main, version 0.5, date 2026-08-15"
protocol: "JeanHuguesRobert/barons-Mariani/research/review_protocol.md @ main, version 0.1, 2026-06-18"
status: "independent-pass-frozen-before-cross-review"
---

# Revue adverse — Moyens et finalités

## Déclaration de décorrélation

- **Exécutant.** Grok 4.7. Non rédacteur du document cible. Le frontmatter du commit attribue la rédaction et la passe adverse interne à GPT-5.6 Sol.
- **Exposition antérieure.** Cette session n'a pas lu une version antérieure du fichier, ni une revue de ce fichier, avant la première passe. La mémoire persistante de l'utilisateur contient l'Autonomie de Capacité, le contentieux sénatorial, l'amendement d'effectivité et le cadre Cogentia. Elle ne contient pas le texte de `38500f09` ni la revue Claude. Persona et mémoire peuvent avoir coloré le cadre. Ce n'est pas une revue vierge.
- **Frontière de lecture, première passe.** Lu : le blob exact du commit (31 483 octets, 1 000 lignes, fin réelle au milieu d'IA7) ; `cogentia/prompts/reviewer.md` v0.5 ; `barons-Mariani/AGENTS.md` ; `barons-Mariani/research/review_protocol.md` ; extraits opérationnels de `cogentia/AGENTS.md` et de `instructions/AGENTS.shared.md`. Non lus avant gel : `research/reviews/review_claude_moyens_et_finalites_2026-10-04.md` ; le dossier factuel du contentieux ; les autres documents du Corpus cités en `related_documents`, sauf ce que le document cible en reprend lui-même. Sources externes consultées : Constitution art. 3 et 27 (Légifrance), code électoral L. 298–L. 305 et L. 318 via sources secondaires concordantes, décision n° 2017-172 PDR du 20 juillet 2017, loi organique n° 2016-506 du 25 avril 2016 via exposés du Conseil constitutionnel, comptages de présentations 2012/2017/2022.
- **Conflit.** Le reviewer opère dans une session dont la mémoire et la consigne de style identifient l'auteur. Cela qualifie l'indépendance. Cela ne transfère pas l'arbitrage.
- **Degré.** Décorrélation haute sur le texte du commit et sur la revue Claude au moment de la première passe. Décorrélation moyenne-faible sur le cadre doctrinal de l'auteur. Revue externe, non confirmation indépendante au sens fort.

## Déclaration de risque de corrélation

Hypothèses de cadre possiblement partagées avec le rédacteur, donc capables de faire échouer la revue dans le même sens :

1. Traiter l'effectivité comme un écart observable entre ouverture juridique et exercice réel est déjà le bon grain d'analyse.
2. Un moyen institutionnel se justifie d'abord par une finalité reconstructible, puis se critique par ses coûts.
3. Le vocabulaire de falsification suffit à rendre une hypothèse testable.
4. Le cas personnel est un Reality Case utile plutôt qu'un biais de sélection de la théorie.

Ces quatre points sont attaqués ci-dessous. S'ils sont faux, plusieurs findings de « synthèse utile » tomberaient avec eux.

## Reality Test secondaire — Packet Closure

`Closed(p, h, E)` pour *p* = capsule au commit `38500f09`, *h* = reviewer sans contexte conversationnel privé du rédacteur, *E* = commit + contrats publics + sources primaires citées ici.

Résultat : **partiellement clos.**

- Clos pour la thèse électorale et capacitaire des §§ 1–15 : la question, les six hypothèses, les distinctions et les concessions internes se lisent sans atelier privé.
- Non clos pour l'identité de Packet : `causal_frontier: git:10970fa…` n'est pas le commit examiné ; la continuité logique est déclarée non stabilisée (§ 0) ; IA7 est coupé. Un lecteur ne peut pas clore le traitement des objections internes.
- La question d'infrastructure ne porte pas la revue de fond. Elle est notée et quittée.

# 1. Summary of the thesis

Un moyen institutionnel `M` adopté pour une finalité `F` peut rester conforme à ses règles tout en réduisant les capacités nécessaires à `F`. La capacité est proposée comme voie située : possibilité, accès, dépendance, fenêtre temporelle. La perte d'une voie personnelle n'est pas une perte systémique. Le secret du bulletin, la publicité des présentations et le formalisme de candidature sont examinés comme des moyens légitimes dont le coût informationnel ou éliminatoire doit être distingué de leur fonction protectrice. La gradation friction / désajustement / inversion réserve l'inversion aux cas où le moyen compromet `F` alors qu'une configuration moins destructive la préserverait. Six hypothèses ouvertes (H1–H6) portent sur le formalisme, l'imputabilité autour du bulletin secret, le coût réputationnel des présentations, la redondance des voies d'amendement, le temps, et les effets cumulatifs. Le principe associé est la stabilité relative d'une finalité explicitée et la révisabilité de son incarnation. Le contentieux sénatorial de l'auteur est déclaré Reality Case involontaire, non preuve. L'Autonomie de Capacité est le nom de corpus de cette grille, non une démonstration déjà stabilisée.

# 2. Errors

## E1 — Le « donc » institutionnel ne suit pas de l'analogie Packet

- **Localisation.** § 1 bis, phrases « Cette distinction fournit une analogie utile pour les institutions » puis « Le principe est donc : stabilité relative et explicitée de la finalité, révisabilité de son incarnation institutionnelle. »
- **Sous-type.** Inferential.
- **Pourquoi cela échoue.** Une analogie méthodologique ne produit pas un principe institutionnel. Le document le dit ensuite (« Elle ne constitue pas une prémisse de H1–H6 et ne démontre rien »). Le `donc` et le disclaimer se contredisent. Si le disclaimer gouverne, le principe n'est pas dérivé. S'il est dérivé, le disclaimer est faux.
- **Formulation corrigée.** « L'analogie Packet suggère, sans le démontrer, de séparer une finalité explicitée de l'incarnation qui la sert. Cette séparation est une hypothèse de méthode, non un principe établi. »
- **Gravité.** Forte sur la section 1 bis ; non bloquante pour H1–H6 si le disclaimer est tenu pour la phrase gouvernante.
- **Action proposée.** `reformulate`. Supprimer le `donc`.

## E2 — H1 n'est pas une hypothèse falsifiable au sens où le document le dit

- **Localisation.** § 5.3 et § 15, H1.
- **Sous-type.** Inferential.
- **Pourquoi cela échoue.** H1 a la forme : *si* irrégularité non substantielle, *si* régularisable dans le temps utile, *si* sans atteinte à l'égalité ni à la sécurité, *alors* défaut d'effectivité. Les « renforcements » listés sont les antécédents. Les « réfutations » listées sont leur négation. Observer que les antécédents sont réunis confirme une stipulation, pas une relation indépendante entre formalisme et effectivité. Une hypothèse falsifiable devrait pouvoir être fausse *alors même que* les antécédents sont vrais — par exemple si l'exclusion définitive, dans ces conditions, préservait encore mieux l'égalité ou la sécurité qu'une régularisation. Cette possibilité est exclue par la définition.
- **Formulation corrigée.** « H1 est un critère normatif d'effectivité procédurale, applicable seulement après qualification séparée du caractère substantiel, de la régularisabilité et de l'égalité. Ce n'est pas, en l'état, un test empirique. »
- **Gravité.** Forte. Le vocabulaire de falsification est load-bearing pour la prétention méthodologique du papier.
- **Action proposée.** `reformulate`.

## E3 — La capsule au commit n'est pas un document fermé

- **Localisation.** Fin du blob, ligne 1000, section IA7 : « Termes proposés : ». Taille vérifiée : 31 483 octets. Le commit message est « research: stamp Moyens et finalités review frontier ».
- **Sous-type.** Factual.
- **Pourquoi cela échoue.** Le fichier examiné s'interrompt au milieu de l'objection interne sur la multiplication ontologique. Il n'y a pas de clôture d'IA7, ni de bibliographie, ni de section de sortie. Une revue qui traiterait ce blob comme le texte intégral de v0.3 assimilerait une sérialisation coupée. Ce n'est pas une absence de vérification : la fin du blob a été lue.
- **Formulation corrigée.** « Au commit `38500f09`, la capsule est tronquée en IA7. Toute assimilation de v0.3 doit partir d'un blob qui ferme IA7, ou déclarer ce commit comme frontière incomplète. »
- **Gravité.** Bloquante pour la stabilisation de cette capsule. Non bloquante pour critiquer §§ 1–15, qui sont lisibles.
- **Action proposée.** `corrected` sur le statut du commit ; arbitrage humain sur la restauration du texte manquant. Ne pas inventer la fin.

Aucune autre phrase des §§ 1–15 n'a été établie comme fausse sur un point de droit positif vérifié. Plusieurs sont sous-déterminées : elles sont en section 7, pas ici.

# 3. Novel objections

Rule N : une objection déjà concédée n'est reprise ici que si la concession est load-bearing et que son traitement ne répond pas.

## N1 — Le secret du grand électeur est d'abord un attribut du suffrage, pas un réglage d'imputabilité

- **Localisation.** § 4.3 ; § 6.2–6.4.
- **Type.** Objection de qualification juridique.
- **Objection.** L'article 3 de la Constitution dispose que le suffrage, direct ou indirect, « est toujours universel, égal et secret ». L'article 27 (« Tout mandat impératif est nul ») vise les membres du Parlement, pas les grands électeurs. L'article L. 318 du code électoral oblige à prendre part au scrutin ; l'émargement constate la participation, non le contenu. La coexistence « liberté + publicité » des votes parlementaires ne transfère pas. Elle montre que *certains* actes politiques publics sont libres. Elle ne montre pas que le bulletin d'un suffrage puisse être partiellement désanonymisé sans toucher l'article 3.
- **Meilleure justification du mécanisme, avant le coût.** Le secret empêche la preuve d'exécution d'une consigne, d'une menace ou d'un achat. Dans un collège de notables, à proximité élevée, cette fonction est plus forte que dans un électorat de masse anonyme. Le document la voit (§ 6.2). Il sous-estime ensuite que cette fonction est constitutionnellement solidifiée, pas seulement instrumentale.
- **Raisonnement.** Accepter H2 comme question de *policy* (« quelle imputabilité autour du bulletin ») reclasse un attribut constitutionnel en variable d'ajustement. C'est le glissement que le papier doit bloquer explicitement, ou assumer comme proposition de révision constitutionnelle.
- **Gravité.** Bloquante si H2 est lu comme critique du droit positif. Forte s'il est lu comme hypothèse de réforme.
- **Action proposée.** `reformulate`. Séparer : (i) droit positif, article 3, non négociable par analogie avec l'article 27 ; (ii) proposition normative, qui exigerait une révision ou une construction compatible avec le secret intégral du bulletin.

## N2 — L'espace d'imputabilité « autour » du bulletin est déjà occupé

- **Localisation.** § 6.4, H2.
- **Type.** Objection empirique et conceptuelle.
- **Objection.** Le document demande une imputabilité supplémentaire compatible avec un bulletin non prouvable. Il ne teste pas les mécanismes déjà en place : émargement de la participation ; identité publique des grands électeurs, pour l'essentiel élus ; scrutin de liste dans les départements à la proportionnelle, où le choix est un choix de liste, agrégeable ; discipline partisane observable au niveau du collège, pas du bulletin. Ces mécanismes restaurent une imputabilité *de rôle* et *d'agrégat*. Ce qui reste inaccessible est précisément l'imputabilité individuelle du choix. H2 doit dire quelle imputabilité manque encore une fois ces voies épuisées. Sinon « autour du bulletin » nomme l'écart que le secret a pour fonction de maintenir.
- **En faveur de H2.** Des collèges petits rendent l'agrégat presque individuel. Une imputabilité de mandat ou de délégation publique, distincte du bulletin, pourrait exister sans preuve du vote.
- **Contre.** Toute restauration qui permet à un tiers de sanctionner un écart individuel recrée la contrôlabilité que § 6.2 juge substantielle. Le document le concède (IA4) sans exhiber un mécanisme qui échappe aux deux branches.
- **Observation qui renforcerait.** Un dispositif existant, dans un suffrage secret, qui a augmenté la sanction politique individuelle sans permettre la preuve du bulletin, documenté par une variation de comportement coercitif.
- **Observation qui affaiblirait fortement.** Constat que les voies déjà publiques (participation, étiquette, liste) n'ont pas réduit la coercition locale, et qu'aucun ajout non prouvant ne le fait non plus.
- **Réfutation réelle.** Démonstration qu'il n'existe pas de signal corrélé au choix individuel qui ne soit pas, dans un collège de cette taille, une preuve pratique du bulletin.
- **Gravité.** Forte.
- **Action proposée.** `piste` tant qu'aucun mécanisme n'est nommé ; `conceded:load-bearing` déjà posé en IA4, traitement inadéquat parce que non opérationnel.

## N3 — H3 est déjà confrontée à une trace adverse agrégée plus forte que le test Capable

- **Localisation.** § 7.3–7.4 ; § 14 bis ; § 15 H3.
- **Type.** Objection empirique.
- **Objection.** La décision n° 2017-172 PDR du 20 juillet 2017 constate que les règles de 2016 — envoi postal et publicité intégrale — n'ont pas eu de conséquences négatives significatives sur le nombre total de présentations : 14 586 formulaires reçus, dont 14 296 validés, contre environ 15 000 en 2012 ; onze candidats contre dix en 2012 et douze en 2007. Les comptages publics donnent 13 427 présentations et 12 candidats en 2022. Le mécanisme causal proposé (publicité → assimilation à un soutien → refus) peut survivre comme effet distributionnel ou comme effet sur des candidatures marginales. Il ne survit pas, en l'état, comme effet sur le volume ou sur le nombre de candidats qualifiés. Le document mentionne une trace adverse de ce type (§ 14 bis) mais ne la traite pas avec la source primaire déjà disponible. Un Reality Test Capable serait un cas situé, sélectionné par l'hypothèse, inutilisable seul — le document le dit. Il ne distingue pas l'hypothèse agrégée, déjà affaiblie, de l'hypothèse distributionnelle, non pré-enregistrée.
- **En faveur de H3.** Témoignages d'élus ; baisse tendancielle du stock de présentations ; violence contre les élus comme facteur confondant ; effet possible sur *qui* est présenté, invisible dans le total.
- **Contre.** Stabilité du nombre de candidats avant/après 2016 ; appréciation explicite du juge de l'élection présidentielle.
- **Renforcement.** Déclarations contemporaines, datées, d'élus habilités, liant un refus nommé à la publication, avec corroboration et exclusion des autres motifs.
- **Affaiblissement fort.** Déjà partiellement observé en 2017 et 2022 sur les totaux.
- **Réfutation réelle.** Contrefactuel montrant que la composition partisane des candidats qualifiés est inchangée à seuil de présentation constant, et qu'aucun refus documenté n'est causalement lié à la publicité plutôt qu'au refus politique de présenter.
- **Gravité.** Forte pour la version agrégée ; moyenne pour une version distributionnelle reformulée.
- **Action proposée.** `reformulate`. Citer 2017-172 PDR. Scinder H3-agrégée et H3-distributionnelle. Ne pas pré-enregistrer un cas unique comme test de la première.

## N4 — Le pré-enregistrement de H4 ne sépare pas les hypothèses concurrentes

- **Localisation.** § 15, H4, pré-enregistrement du 2026-10-04.
- **Type.** Objection méthodologique.
- **Objection.** La branche « oui » (un titulaire du droit d'amendement dépose ou transforme la proposition) est compatible avec : redondance compensatrice ; entrepreneuriat parlementaire ordinaire indépendant de la voie personnelle perdue ; reprise opportuniste ; coïncidence de calendrier. Elle ne restaure pas la voie personnelle, le document le dit. Elle ne prouve pas non plus que la voie personnelle était redondante. La branche « non » est déjà déclarée non concluante (canal, désaccord, priorité, calendrier, non-réponse, refus). Un test dont les deux issues principales sont compatibles avec l'hypothèse et avec sa négation ne distingue pas. Le critère de falsification de la « version forte » exige en outre « transmission traçable et suffisamment précoce » et « pas pratiquement accessibles ». Ces prédicats ne sont pas opérationnalisés avant l'observation : qui transmet, à qui, quel délai est précoce, quel silence compte comme inaccessibilité.
- **En faveur de H4.** L'existence juridique de plusieurs titulaires du droit d'amendement est exacte. Une voie utilisée est une capacité systémique non nulle.
- **Contre.** Des voies juridiques hétérogènes (citoyen, sénateur, rapporteur, Gouvernement) ne sont pas une redondance au sens de Landau 1969 : la redondance suppose des composants substituables vers le même effet. Ici les pouvoirs, les coûts et les dépendances diffèrent. Le document le note (§ 10) puis continue d'appeler l'ensemble redondance.
- **Renforcement.** Dépôt par un acteur qui n'aurait pas été saisi sans la transmission, avec trace du motif, dans la fenêtre, et comparaison à une proposition témoin non transmise.
- **Affaiblissement fort.** Dépôt qui aurait eu lieu de toute façon ; ou absence de dépôt avec motif substantiel de désaccord.
- **Réfutation réelle.** Fenêtre close, transmission précoce au sens pré-enregistré, absence de tout acte, et absence de désaccord substantiel enregistré. Encore faut-il avoir fixé ces termes avant l'observation.
- **Gravité.** Forte sur la prétention de pré-enregistrement ; moyenne sur l'idée banale que plusieurs portes existent.
- **Action proposée.** `reformulate`. Réserver « redondance » aux voies substituables. Appeler les autres « voies alternatives hétérogènes ».

## N5 — F n'est pas identifiée par le test qui la présuppose

- **Localisation.** §§ 1, 1 bis, 13.
- **Type.** Objection conceptuelle.
- **Objection.** Le test d'effectivité commence par « Quelle est sa finalité ? ». Pour le secret, les finalités recevables sont au moins : protection de la liberté du choix ; impossibilité de vérifier une pression ; égalité du suffrage ; attribut constitutionnel non instrumental ; confiance dans le décompte. Elles ne sont pas réductibles à une `F` dont l'analyste, le juge, le constituant de 1958 ou le collège serait le dépositaire unique. Le document dit que `F` n'est ni unique ni immuable. Le test opère ensuite comme si une `F` était suffisamment explicitée pour juger qu'un coût la compromet. Qui tranche le conflit de finalités n'est pas dit. Sans cette règle, « inversion moyen–fin » est le nom du désaccord de l'analyste avec l'institution.
- **Gravité.** Forte.
- **Action proposée.** `reformulate`. Pour chaque moyen, lister les finalités en concurrence, leur source (texte, jurisprudence, justification historique, reconstruction), et l'autorité qui les hiérarchise. Ne pas conclure à l'inversion tant que cette hiérarchie n'est pas attribuée.

## N6 — Le cas personnel reste le générateur des exemples, malgré la précaution déclarée

- **Localisation.** §§ 4.1, 5, 8, 9 ; IA1.
- **Type.** Objection de dépendance au cas.
- **Objection.** IA1 distingue fait, grief, qualification et hypothèse, et demande à la revue externe de vérifier si la précaution est réelle. Elle ne l'est que partiellement. Les trois cas sont réels ; deux (formalisme, secret) et le fil rouge corse sont ordonnés par la candidature alléguée de l'auteur et par l'amendement qu'il porte. Aucun cas n'applique la même grille à une formalité qui a *protégé* l'égalité contre un intérêt de l'auteur, ni à un secret qui a empêché une coercition observable. La symétrie des critères de réfutation est déclarée. La symétrie des cas ne l'est pas. Une théorie générale produite à partir d'un contentieux personnel peut être vraie. Elle n'est pas encore distinguée de sa fonction justificative.
- **Gravité.** Forte pour toute montée en généralité. Moyenne si le papier reste un cadre appliqué à un dossier déclaré.
- **Action proposée.** `arbitration`. Soit restreindre le statut à « cadre essayé sur un dossier situé ». Soit ajouter un cas adverse où le formalisme éliminatoire est tenu pour justifié.

## N7 — H5 et H6 n'ajoutent pas une distinction aux doctrines qu'elles recouvrent

- **Localisation.** §§ 11, 15 H5 et H6.
- **Type.** Objection de prior art. Concession IA2 load-bearing, traitement non répondant : relevée ici.
- **Objection.** « Le temps est une composante de la capacité » reformule la forclusion, la perte de chance, l'irréversibilité, le recours effectif (article 13 CEDH, exigence d'effectivité) et la *path dependence* (Pierson). « La conformité séparée n'entraîne pas l'effectivité de la chaîne » reformule le sophisme de composition, les coûts de transaction cumulés et l'effet de procédures successives. Le gain analytique n'apparaît que si la grille prédit un cas que ces doctrines qualifient autrement. Aucun cas de ce type n'est donné.
- **Gravité.** Moyenne. Non bloquante si les termes sont présentés comme checklist, pas comme théorie propre.
- **Action proposée.** `reformulate` ou abandon des termes qui ne discriminent pas — option déjà ouverte par IA2.

# 4. Concessions assessed

| ID | Concession | Typage source | Test : l'argument en dépend-il encore ? | Évaluation |
|---|---|---|---|---|
| C1 | IA1, auto-confirmation du cas personnel, `integrated` | intégré | Oui pour la montée en généralité | Typage trop favorable. La distinction des catégories est réelle ; elle ne neutralise le choix des cas. Reclasser le résidu en `conceded:load-bearing`. Traitement inadéquat. Voir N6. |
| C2 | IA2, renommage possible de la proportionnalité, de l'effectivité, des capabilities, des coûts de transaction, de la résilience et des veto points, `conceded:load-bearing` | load-bearing | Oui | Typage correct. Le report à une revue de prior art ne répond pas. Reste ouvert. Voir section 8C et N7. |
| C3 | IA3, extension excessive de « capacité », `reformulate` | à stabiliser | Oui | Typage correct. Non stabilisé. Section 7. |
| C4 | IA4, le secret peut être bien calibré, `conceded:load-bearing` | load-bearing | Oui, H2 en dépend | Typage correct. Le critère de falsification est juste et non opérationnel. Reste ouvert. Voir N1, N2. |
| C5 | IA5, présentation ≠ suffrage, `conceded:bounding` | bounding | Non, si la comparaison ne prescrit pas l'identité des régimes | Typage correct à cette condition. Adéquat pour interdire la déduction d'identité. Inadéquat s'il laisse croire que la publicité parlementaire informe le secret du suffrage. |
| C6 | IA6, probabilité de succès faible, `integrated` | intégré | Non pour l'existence de la voie ; oui si le papier fait encore porter un enjeu systémique sur la voie personnelle | Adéquat comme distinction existence / probabilité. À tenir dans § 8, où la chaîne candidature → capacités futures de la Corse reste rhétoriquement chargée. |
| C7 | § 5.1, faits du contentieux non établis ici | bounding | Non pour H1 comme critère ; oui si un lecteur lit H1 comme qualifiant le dossier | Adéquat, à condition de ne pas faire du dossier l'illustration implicite. |
| C8 | § 7.4, un cas Capable ne généralise pas | bounding | Non | Adéquat. Ne dispense pas de traiter la trace agrégée déjà publique. |
| C9 | § 1 bis, l'analogie ne démontre rien | bounding en intention | Le `donc` la rend load-bearing localement | Contradiction avec E1. Le disclaimer est la bonne phrase ; il ne gouverne pas encore le paragraphe. |
| C10 | H4, l'absence de dépôt ne ferme pas le système | bounding | La version forte en dépend encore | Le « si non » est correctement affaibli. Le « si oui » ne l'est pas. Concession incomplète. Voir N4. |

# 5. Symmetry test

Le lecteur qui ignore Cogentia peut reconstruire la thèse des §§ 1–15, les six hypothèses et la gradation friction / désajustement / inversion. Il ne peut pas reconstruire l'identité de Packet, la `causal_frontier`, ni la fin d'IA7. La symétrie de fond est donc bonne pour le papier électoral, mauvaise pour l'enveloppe. La phrase d'ouverture (« représentation documentaire courante d'un travail cognitif vivant », « Packet Capsule candidate ») impose un cadre que le disclaimer de § 1 bis dit ne pas être une prémisse. Un lecteur extérieur lit d'abord le cadre.

Verdict : source presque symétrique sur le fond électoral ; enveloppe non symétrique. Ne pas certifier la capsule entière comme autoporteuse.

# 6. Stabilized concepts

Assez stables pour être réutilisés, sous les bornes indiquées :

- **Conformité ≠ service effectif de la finalité.** Standard, correctement rappelé. Réutilisable comme question, pas comme résultat.
- **Perte personnelle ≠ perte systémique.** Distinction nette (§ 4.1). C'est le meilleur apport local du papier, à condition de ne pas réimporter la perte personnelle par la chaîne du § 8.
- **Capacité autonome / capacité dépendante.** Utile, proche de l'agence et du veto, mais formulée sans prétendre que la dépendance annule l'effet. Réutilisable comme distinction, pas comme mesure.
- **Friction ≠ désajustement ≠ inversion.** La réserve du terme « inversion » est la bonne discipline. Réutilisable seulement avec le critère d'alternative moins destructive effectivement exhibée.
- **Présenter ≠ soutenir ≠ annoncer un vote.** Distinction juridique correcte. Stable.
- **Réparation juridique ≠ restauration fonctionnelle ≠ restitution historique.** Distinction claire (§ 11). Stable comme vocabulaire ; non originale.

# 7. Fragile or ambiguous concepts

- **Capacité.** « Notamment l'existence d'une voie effectivement praticable » mélange droit, accès, dépendance, délai et effet. Stabiliser : une capacité située est le quadruplet (effet visé, voie, dépendance, fenêtre), pas une grandeur. Hors de ce quadruplet, ne pas employer le mot.
- **Voie.** Tantôt maillon d'une chaîne, tantôt acteur titulaire d'un pouvoir. Stabiliser par un schéma unique : acteur, acte, effet, substituabilité.
- **Cascade.** Fermeture amont supprimant des effets aval. Vrai par construction si la chaîne est nécessaire. Stabiliser en exigeant que chaque maillon soit nécessaire, pas seulement narratif. La chaîne candidature → amendement → capacités de la Corse n'est pas nécessaire : d'autres déposent des amendements.
- **Redondance capacitaire.** Voir N4. Stabiliser par substituabilité, coût comparable, fenêtre commune. Sinon parler de pluralité de voies.
- **Fenêtre capacitaire.** Recouvre forclusion et irréversibilité. Stabiliser en datant l'ouverture, la clôture utile et l'acte qui la ferme, sur un calendrier de texte positif.
- **Inversion moyen–fin.** Réservée, mais le critère « compromet substantiellement » n'a pas de seuil. Stabiliser par une alternative nommée qui préserve la protection identifiée, pas par l'intensité du coût.
- **Finalité.** Voir N5.
- **Autonomie de Capacité.** Nom de corpus. Non stabilisé comme contribution distincte tant que IA2 n'est pas répondue.
- **Imputabilité autour du bulletin.** Non instanciée.

# 8. Conceptual drift risks

- Vérité du grief / qualification juridique / hypothèse capacitaire : la séparation est écrite ; le fil rouge du § 8 les réenchaîne.
- Article 27 / article 3 : liberté du représentant et secret du suffrage.
- Publicité d'un acte de filtrage / publicité d'un suffrage.
- Redondance technique / pluralité de compétences.
- Effectivité comme concept juridique / effectivité comme devise opérationnalisée.
- Analogie Packet / principe institutionnel.
- « Falsifiable » / « critère normatif conditionnel ».
- Perte d'une possibilité / perte d'un résultat.

## 8A. Possibility-space closure / Booster test

Applicable : le papier porte sur ce que les institutions rendent possible.

- **Invariant de présent.** Le collège sénatorial indirect, le seuil de présentations et la publicité intégrale sont traités comme le régime dans lequel tester les coûts. Ils ne sont pas déduits comme seuls régimes possibles. Pas une erreur d'impossibilité. Le risque inverse est de traiter leur révision comme une variable ordinaire (N1).
- **Statut d'impossibilité.** Pas d'usage abusif de « impossible » sur H1–H6. H2 dit « il est possible que », ce qui est trop faible plutôt que trop fermé.
- **Résidu non assimilé.** Le secret comme attribut constitutionnel, non comme coût. Le papier le range parmi les fonctions du moyen. Il résiste à ce rangement. À conserver comme résidu, pas à renommer « dépendance capacitaire ».
- **Booster.** Aucun ajout de force institutionnelle n'est proposé qui serait remplaçable par un test plus petit. Le plus petit test déjà disponible pour H3 est la décision 2017-172 PDR, non un nouveau dispositif. `No Booster candidate identified` au sens d'une intervention plus légère que le papier proposerait d'alourdir. Le papier lui-même est déjà au-dessus du plus petit test.

## 8B. Unexplored-space / blind-spot review

- **B1. Contentieux électoral comparé du formalisme de recevabilité.** La jurisprudence électorale française distingue souvent l'irrégularité qui altère la sincérité ou le résultat de celle qui ne l'altère pas. Les mémentos préfectoraux qualifient par ailleurs la déclaration de candidature de formalité substantielle. Le papier ne confronte pas H1 à cette paire. Plus petit ajout : pour la formalité litigieuse du dossier, citer la disposition du code électoral et la décision de refus ou d'enregistrement, puis dire si le juge électoral traite ce type de manquement comme substantiel ou régularisable. `[provisional: dossier factuel non lu]`
- **B2. Taille du collège et théorie du vote obligatoire.** La littérature sur le *compulsory voting* sépare obligation de participation et liberté du choix. Le papier la mentionne (§ 6.1) sans l'utiliser pour borner H2. Plus petit ajout : une page sur la doctrine de la Commission de Venise (Code de bonne conduite en matière électorale, secret et vote obligatoire) et sur ce qu'elle interdit explicitement.
- **B3. Gatekeeping des nominations, hors présidentielle française.** Les travaux sur endorsements et sélecteurs de candidatures prédisent un coût réputationnel du parrainage public *et* un gain de signal. Le papier ne considère que le coût. Plus petit ajout : traiter le gain d'information pour l'électeur et pour les autres présentateurs comme finalité concurrente, pas comme externalité négligeable.
- **B4. Contrôle de proportionnalité déjà disponible.** Conseil constitutionnel et CEDH disposent d'un test d'adéquation, de nécessité et de balance. Le papier ne dit pas quel cas ce test ne peut pas voir et que la grille capacitaire verrait. C'est le point qui départage contribution et renommage.

Aucun de ces angles n'est une citation manquante décorative. Chacun peut changer la prétention de nouveauté ou la qualification de H1–H3.

## 8C. Correlation-risk and living state-of-the-art review

**Risques de corrélation.** Voir la déclaration initiale. Le plus matériel : accepter que nommer une voie, une dépendance et une fenêtre constitue un apport une fois les doctrines classiques concédées.

**État de l'art consulté.** Frontière de recherche : 2026-10-05. Domaine juridique lent ; scan proportionné, pas une revue systématique.

| Prétention du papier | État vivant | Ce que cela établit |
|---|---|---|
| Moyen / fin, incarnation révisable | Dewey, *Human Nature and Conduct* (1922) et *Theory of Valuation* (1939) : moyens et fins se déterminent réciproquement ; Weber, rationalité en finalité ; Alexy, proportionnalité | La séparabilité « F stable, M révisable » est une simplification. Les fins sont souvent révisées par l'échec des moyens. |
| Capacité comme possibilité réelle | Sen, *Equality of What?* (1979), *Development as Freedom* (1999) ; Nussbaum, capabilities | Proche. Sen distingue déjà fonctionnement et capacité, et refuse la réduction au droit formel. L'apport local serait la fenêtre et la dépendance institutionnelle électorale, non le concept. |
| Effectivité | Droit administratif ; article 13 CEDH ; principe d'effectivité UE | Doctrine établie. Le papier le reconnaît (§ 2) sans montrer l'écart. |
| Redondance | Landau, « Redundancy, Rationality, and the Problem of Duplication and Overlap », *Public Administration Review*, 1969 ; Ting, redondance stratégique | La redondance exige une substituabilité. Les voies hétérogènes du § 10 n'y satisfont pas automatiquement. |
| Veto et dépendance | Tsebelis, *Veto Players*, 2002 ; Immergut, veto points | « Je peux demander à Y » est un veto point. Nommer une dépendance capacitaire ne déplace pas le résultat. |
| Temps | Pierson, « Increasing Returns, Path Dependence, and the Study of Politics », *APSR*, 2000 ; forclusion, perte de chance | H5 est dans cette famille. |
| Secret et imputabilité | Article 3 Constitution ; Commission de Venise, Code de bonne conduite en matière électorale ; littérature principal-agent sur le vote de mandat | Le secret est la solution standard au problème d'agence électeur/mandant local lorsque la preuve du vote permet la sanction privée. |
| Présentations | Loi organique n° 2016-506 ; décision n° 2017-172 PDR | La version agrégée de H3 est déjà affaiblie par le juge compétent. |

**Écart vivant.** Pas de gap d'implémentation ou de marché : le domaine n'est pas un marché technique. Le gap est doctrinal : le papier ne cite pas les tests qu'il devrait battre. IA2 l'admet. L'admission n'est pas le travail.

# 9. Signal/noise report

- **Intégrer maintenant, si l'arbitrage retient la correction.** E1 (`donc` analogique). E2 (statut de H1). N1 (article 3 / article 27). N3 (citer 2017-172 PDR et scinder H3).
- **Reformuler avant toute intégration.** N2, N4, N5, N7. Définitions de la section 7.
- **Piste.** Mécanisme d'imputabilité non prouvante, seulement s'il est nommé. Cas adverse de formalisme justifié.
- **Bruit.** Développement supplémentaire de l'enveloppe Packet dans ce papier. Il n'aide pas H1–H6 et rompt l'autoporte.
- **Arbitrage humain.** N6 (statut du cas personnel). E3 (restauration de la fin tronquée). Maintien ou abandon du nom « Autonomie de Capacité » après prior art.
- **Frontmatter.** `review.status: unreviewed` est cohérent avec le lignage, qui ne prétend pas purger la revue Claude. `canonical_url` pointe vers `main`, pas vers le commit : risque de trace fausse si `main` a divergé. `[unverified: git rev-parse main:research/moyens_et_finalites.md au moment de l'assimilation]`. `provenance.origin_* : unknown` est un état enregistré, pas une erreur. Pas de `last_stamped_at` dans le frontmatter lu : absence, donc amélioration structurelle, pas mensonge. Le champ `version_history` couvre le rôle du changelog.

# 10. Structural improvements

Chaque item a un test de complétion.

1. **Fermer le blob.** Test : le fichier au commit de travail se termine après la dernière section annoncée, et IA7 contient une liste close de termes et une disposition.
2. **Déplacer l'enveloppe Packet après le papier, ou en annexe.** Test : un lecteur qui s'arrête avant toute occurrence de « Packet » a déjà lu la question, les distinctions, H1–H6 et le test du § 13.
3. **Tableau unique des moyens.** Colonnes : texte positif, finalités concurrentes, capacité protégée, capacité réduite, dépendance, fenêtre datée, alternative nommée, observation falsifiante, statut (friction / désajustement / inversion / non qualifié). Test : chaque moyen des cas I–III a une ligne, et aucune ligne « inversion » n'est remplie sans alternative nommée.
4. **Séparer critère normatif et hypothèse empirique.** Test : H1 n'emploie plus « falsifiable » ; H3 et H4 ont une observation dont l'échec n'est pas la négation de leur définition.
5. **Sources primaires en note.** Test : article 3, article 27, L. 318, loi organique 2016-506 et décision 2017-172 PDR sont cités aux paragraphes qui les mobilisent ou les contredisent.

# 11. Internal corpus references

Un lecteur sans les documents liés perd la définition stabilisée d'Autonomie de Capacité et le détail du contentieux. Le papier le dit (§ 5.1) pour le contentieux. Il ne donne pas, pour l'Autonomie de Capacité, la définition minimale qui rendrait le nom inutile à résoudre. Recommandation : annotation optionnelle vers `projects/capable/doctrine.md` et vers le dossier factuel. Ne pas faire de ces fichiers une prémisse. Aucune intégration de liaison supplémentaire : la tentation de corpus est ici un coût, pas un gain. Les §§ 0, 1 bis et 14 bis dépendent déjà trop de Cogentia pour un papier qui annonce s'en séparer.

# 12. Possible derived products

Pas de produit public dérivé tant que E2, N1 et N3 ne sont pas arbitrés. Un fil « formalisme / secret / présentations » dérivé maintenant transporterait un critère stipulé, une analogie constitutionnelle fragile et une hypothèse agrégée déjà affaiblie. Raison suffisante pour omettre les dérivés.

# 13. Continuation report

- **Préserver.** La question initiale. La distinction perte personnelle / perte systémique. La réserve sur « inversion ». La distinction présenter / soutenir. Le refus de traiter la devise comme un score (§ 14). Les concessions IA2 et IA4, à condition de les traiter.
- **Corriger.** E1, E2, E3. Article 3 contre article 27. Trace 2017-172 PDR.
- **Approfondir.** Substituabilité réelle des voies. Conflit de finalités du secret. Cas adverse de formalisme.
- **Risque conceptuel.** L'Autonomie de Capacité devient le nom de toute critique d'un coût institutionnel.
- **Risque stylistique.** Chaînes textuelles qui mimiquent une nécessité.
- **Intégrer maintenant.** Rien sans arbitrage. Les corrections E1 et N1 sont les plus proches d'un défaut réparable.
- **Différer.** Mécanisme H2. Montée en théorie générale.
- **Prochaine action recommandée.** Arbitrage humain sur le statut du commit tronqué, puis reformulation de H1 et H3 avant toute nouvelle revue de fond. Ne pas stabiliser v0.3 en l'état.

# Falsification opportunities

| Hypothèse | Meilleur argument pour | Meilleur argument contre | Renforcerait | Affaiblirait fortement | Réfuterait |
|---|---|---|---|---|---|
| H1 | Une formalité sans fonction résiduelle, encore corrigeable, ne devrait pas éliminer | La déclaration *est* l'acte ; le délai ferme l'égalité ; le juge électoral ne transpose pas Danthony automatiquement | Formalité dont la fonction était déjà satisfaite par une pièce au dossier, temps utile non clos, aucun concurrent lésé, texte n'exigeant pas la forme précise | Texte ou jurisprudence qualifiant cette formalité de substantielle et non régularisable à ce stade | Antécédents réunis et régularisation produisant néanmoins une inégalité ou une insécurité que l'exclusion évitait — observation que la forme actuelle de H1 exclut |
| H2 | Le secret détruit aussi l'imputabilité démocratique | Article 3 ; l'écart restant est la fonction du secret ; mécanismes autour du bulletin déjà là | Dispositif existant augmentant la sanction de rôle sans preuve du bulletin, avec baisse mesurée de la coercition | Ces dispositifs existent et la coercition locale demeure ; tout ajout utile recrée une preuve pratique | Preuve que, dans un collège de cette taille, tout signal du choix individuel est une preuve pratique |
| H3 | Coût réputationnel déclaré par des présentateurs | 2017-172 PDR ; volumes 2012/2017/2022 ; nombre de candidats stable | Refus datés, motivés par la publication, corroborés, autres motifs exclus | Totaux et nombre de qualifiés stables — déjà largement le cas | Composition des qualifiés inchangée et refus documentés expliqués par le désaccord politique, pas par la publication |
| H4 | Plusieurs titulaires du droit d'amendement | Voies non substituables ; pré-enregistrement non discriminant | Dépôt causalement lié à la transmission, fenêtre tenue, proposition témoin non reprise | Dépôt indépendant de la transmission, ou refus motivé sur le fond | Inaccessibilité pratique pré-enregistrée (délai, destinataires, seuil de silence) malgré transmission précoce, sans désaccord substantiel |
| H5 | Une élection ultérieure ne recrée pas l'événement manqué | Forclusion, perte de chance, path dependence disent déjà cela | Cas où ces doctrines qualifient « réparé » et où la grille capacitaire qualifie autrement, avec conséquence opérationnelle | Aucun cas discriminant | Abandon si aucun cas discriminant après recherche dédiée |
| H6 | La chaîne peut échouer quand chaque maillon est régulier | Sophisme de composition déjà connu ; à tester cas par cas, le document le dit | Chaîne électorale précise où chaque contrôle séparé valide et l'effet conjoint détruit `F` identifiée | Réduction du cas à une somme de désajustements déjà qualifiables un par un | Abandon de la prétention de théorie propre si le cas se réduit |

# Recommendation

Ne pas stabiliser ce document. Ne pas le publier comme papier de fond. §§ 4.1, 4.2, 12 et 14 résistent comme distinctions locales. H1, H2, H4 et le principe de § 1 bis ne résistent pas sous leur prétention actuelle. H3 agrégée est déjà en difficulté empirique. H5 et H6 ne justifient pas un vocabulaire propre tant qu'un cas discriminant manque. L'arbitrage reste à Jean Hugues Noël Robert.

# 14. Yield report

- Errors identified: 3 (factual 1 / inferential 2 / attributive 0)
- Claims marked unverified: 2 (identité de `main` et du commit ; qualification jurisprudentielle de la formalité litigieuse, dossier non lu)
- Novel objections, not conceded by the source: 5 (N1, N3, N4, N5, N6). N2 et N7 prolongent des concessions load-bearing dont le traitement ne répond pas ; comptées avec les objections ouvertes, pas comme nouveautés pures.
- Concessions assessed: 10
- Concessions reclassified from `bounding` to `load-bearing`: 1 (C1 / IA1, résidu)
- Possibility-space closure findings: 1 (résidu constitutionnel du secret)
- Impossibility-status errors: 0
- Unassimilated residues worth preserving: 1
- Booster opportunities: 0
- Material blind spots / unexplored regions: 4
- Correlated-assumption risks: 4
- Living state-of-the-art gaps: 1 (prior art admis, non traité)
- Recommendations carrying a completion test: 5 of 5
- Findings marked provisional: 1 (B1)
- Frontmatter breaches: 0 false / 1 absent (`last_stamped_at`) + 1 risque de trace (`canonical_url` vers `main`) unverified

# 15. Delivery compliance check

- Fichier demandé : `review.md`, sans numéro de version dans le nom.
- L'analyse substantielle de la première passe est dans ce fichier.
- La réponse conversationnelle ne doit pas ajouter d'analyse absente de ce fichier.
- Lien de téléchargement : à émettre avec la réponse.
- La section de revue croisée, si elle suit, est ajoutée après gel et ne réécrit pas les sections 1 à 15.

# Return packet

```text
target: research/moyens_et_finalites.md@38500f09
reviewer: Grok 4.7
date: 2026-10-05
stabilization: not recommended
established:
  - conformité ≠ effet
  - perte personnelle ≠ perte systémique
  - présenter ≠ soutenir
  - inversion réservée aux alternatives exhibées
false_or_broken:
  - donc analogique du § 1 bis
  - H1 comme hypothèse falsifiable
  - capsule close à ce commit
load-bearing_still_open:
  - IA2 prior art
  - IA4 calibration du secret
  - article 3 contre transfert de l'article 27
  - générateur personnel des cas
reformulate:
  - H3 scindée agrégée / distributionnelle
  - H4 substituabilité et pré-enregistrement discriminant
  - F plurielle et autorité de hiérarchisation
prior_art:
  - effectivité, proportionnalité, capabilities, veto points, redondance Landau, path dependence
test_in_the_real:
  - H3 distributionnelle seulement, après avoir enregistré la trace 2017
  - H4 seulement avec prédicats opérationnels pré-enregistrés
abandon_unless_discriminant_case:
  - H5 et H6 comme théorie propre
  - Autonomie de Capacité comme nom d'une contribution distincte
arbitrate:
  - restauration du blob
  - statut situé ou théorie générale
```

---

Fin de la première passe, gelée avant lecture de la revue Claude.

## Cross-review après gel

La première passe ci-dessus est inchangée. Cette section a été écrite après lecture de `research/reviews/review_claude_moyens_et_finalites_2026-10-04.md` (Claude Sonnet 5.5, 2026-10-04, cible déclarée v0.2-draft, commit non disponible pour ce reviewer). Les deux revues ne portent pas sur le même blob : Claude sur une v0.2 transmise par copie ; Grok sur `38500f09`, v0.3-draft, tronqué en IA7. La v0.3 déclare avoir assimilé préparatoirement la revue Claude. Une convergence peut donc être une assimilation, pas une découverte indépendante.

### Findings indépendamment convergents

- L'analogie Packet ne fonde pas un principe institutionnel. Claude D3 ; Grok E1. La v0.3 a déjà la formule « stabilité relative » demandée par Claude, et conserve le `donc`. La convergence porte sur le vice inférentiel, pas sur la formulation déjà corrigée.
- `F` est sous-déterminée, souvent reconstruite par l'analyste, en tension avec un principe qui la suppose assez stable. Claude D3 / N11 de sa v0.1 ; Grok N5.
- Le transfert de l'interdiction du mandat impératif vers le grand électeur est abusif. Claude le tenait pour une erreur dès sa revue de la v0.1 et ne l'a pas recompté (Rule N). Grok N1 le reprend sur l'article 3, indépendamment de cette revue.
- La trace agrégée sur les présentations avant/après 2016 affaiblit H3 et doit être traitée, pas seulement la déclaration confirmatoire. Claude D4 / N8 de sa v0.1 ; Grok N3, avec la décision n° 2017-172 PDR.
- L'enveloppe Cognitive Packet n'est pas une prémisse de H1–H6 et dégrade l'autoporte. Claude D1 ; Grok sections 5 et 10.
- IA2 reste ouverte : capabilities, effectivité, proportionnalité, veto points, redondance, path dependence. Claude section 9 ; Grok N7 et 8C.
- Le cas personnel et l'assimilation par l'intéressé restent un risque de cadre. Claude D5 et IA1 ; Grok N6 et C1.

### Findings propres à Grok

- E2 : H1 est un critère stipulé, pas une hypothèse falsifiable. Non traité comme tel par Claude dans la revue v0.2 lue.
- E3 : le blob `38500f09` s'arrête au milieu d'IA7. Invisible pour une revue de la v0.2.
- N2 : l'imputabilité « autour » du bulletin est déjà occupée par l'émargement, l'identité publique des grands électeurs et le scrutin de liste.
- N4 : le pré-enregistrement de H4 ajouté en v0.3 ne distingue pas les hypothèses concurrentes. Claude, sur la v0.2, recommandait au contraire de le consigner (son booster §12 / D7). La critique porte sur la forme retenue après sa revue.
- N1 précise l'article 3 comme attribut du suffrage, au-delà du seul article 27.
- Scission H3 agrégée / H3 distributionnelle, avec les comptages 2017 et 2022.

### Findings propres à Claude qui paraissent matériellement valides

- D2 : l'identité à travers les représentations a un prior art (FRBR, PROV, identifiants persistants). Valide pour l'enveloppe, secondaire pour le papier de fond. Non vérifié indépendamment dans la première passe.
- D4 (i) et (ii) : employer un Trace Treatment Packet non stabilisé comme procédure, et prendre un autodiagnostic de motif comme trace privilégiée, reste un défaut même après l'ajout v0.3 d'une trace adverse. Le point Nisbett et Wilson n'a pas été revérifié ici ; l'objection de validité du motif déclaré tient sans lui.
- D5 : l'assimilation par la partie revue ne se vérifie pas sans conservation de la revue brute. Partiellement répondu par le `review_lineage` de la v0.3, pas clos.
- D7 : une fenêtre H4 sans dates opérationnelles ne teste rien. Valide comme exigence. Les heures précises (7 octobre 2026, 18 h ; 23 octobre, 12 h) restent `[unverified]` de ce côté ; elles ne sont pas reprises comme faits.
- D8 : incohérence d'alinéa dans la note d'amendement. Hors cible directe. `[provisional: amendement_effectivite_article_72-5.md non lu pour cette revue]`. Si elle est exacte, elle fragilise le test récursif du §9, pas H1–H6.

### Contradictions entre les deux Reviewers

- Pas de contradiction sur un fait juridique vérifié des deux côtés. La divergence principale est séquentielle : Claude demandait un pré-enregistrement de H4 ; la v0.3 l'a ajouté ; Grok juge ce pré-enregistrement non discriminant. Ce n'est pas un désaccord sur la v0.2.
- Claude D4 disait que §14 bis ne traitait que la trace confirmatoire. La v0.3 ajoute une trace adverse. Grok tient que l'ajout ne suffit pas tant que la décision 2017-172 PDR n'est pas citée. Désaccord de degré, pas d'existence.
- Claude E-A (le document v0.2 se décrivait comme produisant une v0.2) n'a pas d'équivalent dans le blob v0.3 lu. Soit assimilé, soit hors du texte tronqué. Non contredit.
- Poids relatif : Claude consacre l'essentiel du delta v0.2 à l'infrastructure Packet ; Grok la traite comme bruit dès qu'elle ne porte pas H1–H6. Divergence de cadre, déclarée. Elle peut faire manquer à chacun ce que l'autre voit : l'identité documentaire d'un côté, la qualification constitutionnelle du secret de l'autre.

### Risque de cadre commun

Réel, limité. Les deux revues partagent le contrat Reviewer, le soupçon d'auto-confirmation, et l'idée qu'un moyen se juge d'abord par la capacité qu'il protège. Ce dernier point est aussi une prémisse du document. Ni l'une ni l'autre n'a produit le cas adverse où le formalisme éliminatoire est tenu pour justifié contre l'intérêt de l'auteur. Cette absence commune est le trou le plus susceptible d'être un angle mort partagé, pas une convergence de preuve.