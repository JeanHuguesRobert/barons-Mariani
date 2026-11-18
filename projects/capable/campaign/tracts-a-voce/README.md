---
title: "A Voce × Capable — 40 000 tracts comme Bouteilles à la Mer"
author: "Jean Hugues Noël Robert — proposition assistée par GPT-6"
date: 2026-11-18
last_modified_at: 2026-11-18
language: fr
license: CC BY-SA 4.0
status: "prototype opérationnel — non autorisé pour diffusion électorale"
document_role: "source"
document_kind: "campaign-research-protocol"
visibility: public
lifecycle_state: working
update_policy: UP-DEFAULT-REVIEWED
provenance:
  origin_type: conversation
  origin_repository: JeanHuguesRobert/barons-Mariani
  origin_date: 2026-11-18
  derived_from:
    - projects/capable/campaign/marche-du-soleil.md
    - musee-mariani/methodes/bouteille_a_la_mer.md
    - research/cognitive_packet_incarnations_and_missions.md
review:
  status: unreviewed
  reviewed_by: []
---

# A Voce × Capable — tracts incarnant des missions

> **Proposition du 18 novembre 2026.** Jean-François Baccarelli envisage l'impression de **40 000 tracts A Voce, une page, noir et blanc**, dans un contexte de soutien au mouvement Capable. Il ne s'agit **ni d'une commande passée, ni d'un contrat avec l'imprimeur, ni d'une diffusion accomplie**, ni d'un texte validé par A Voce ou par le mandataire de la campagne.

## 1. Décision d'architecture : ne pas confondre papier, mission et parrainage

Une **Bouteille à la mer** est une incarnation matérielle d'une mission facultative : elle peut être transmise, annotée ou faire revenir une contribution ; son porteur n'a pas à être identifié. **Un tract ne devient pas un parrainage parce qu'il a été imprimé, scanné ou transmis.**

Le vrai objectif réglementaire est d'obtenir au moins **500 présentations valides d'élus habilités**, sous conditions de diversité territoriale : au moins 30 départements/collectivités pris en compte, et pas plus de 50 comptabilisées par territoire. Les citoyens ordinaires ne peuvent pas signer ces présentations. Leur action possible est la discussion, la circulation du tract, le signalement public et la mise en relation volontaire ; la décision de présentation reste individuelle et libre à l'élu.

Ontologie réutilisée :

| Niveau | Identité | Ce que cela prouve — et ne prouve pas |
| --- | --- | --- |
| Édition | `edition_id` | Texte versionné, différent de chaque feuille |
| Incarnation papier | `copy_id` (`AV27-00001`…) | Référence interne unique dans le lot ; pas preuve de détention ni d'authenticité |
| 3Code | `3XX-XXX-XXX` | Référence humaine potentiellement homonyme ; ni numéro de série, ni code secret |
| QR | URL d'accès | Moyen d'accès seulement, pas preuve de visite consentie ni de résolution 3Code |
| Mission | `CAPABLE-PRESENTATIONS-2027` | Invitation volontaire à participer, pas mandat d'agir au nom du candidat |
| Événement | témoin/observation datée | Trace qualifiée, pas soutien établi |
| Élu habilité | identité vérifiée dans registre **séparé et protégé** | Contact ≠ intérêt ≠ promesse ≠ présentation transmise ≠ validation officielle |

**Ne jamais recopier des listes nominatives de porteurs, de signataires ou d'élus approchés dans un registre public de tracts.** Le suivi électoral doit réutiliser l'[Observatoire des Présentations](../observatoire-presentations-2027.md), avec ses états et sa provenance propre.

## 2. Arbitrage économique : deux couches d'impression

**Couche A — 40 000 tracts identiques** (impression économique, A4 ou autre format à décider, recto seul, N&B). Le tract présente Capable, une mission publique facultative et **un seul point d'entrée commun**, sous réserve de test HTTP et de conformité électorale. Cela permet l'impression traditionnelle sans données variables.

**Couche B — individualisation facultative** (avant ou après l'impression) : une étiquette ou un tampon portant le `copy_id`, le 3Code et, une fois l'endpoint individuel opérationnel, éventuellement un QR. Un jeu de 24 étiquettes par feuille A4 permet un pilote ; le même générateur sait aller jusqu'à 40 000.

L'individualisation complète de 40 000 exemplaires exige une tarification explicite de la **donnée variable** chez l'imprimeur ou un travail d'étiquetage important. Sans chiffrage, rien ne permet de présumer cette variante économique. **Référence conseillée pour le devis** : coût de 40 000 identiques vs 40 000 variés vs 40 000 identiques + 100/1 000/40 000 étiquettes ; mentions légales et coût de distribution séparés.

## 3. Quatre missions non coercitives

1. **Lire / contester** : découvrir l'argument, proposer une objection, corriger un fait.
2. **Transmettre** : faire circuler volontairement le tract ou son contenu numérique, sans chaîne imposée ni pression.
3. **Relier** : fournir, si souhaité, une référence **publique** vers un élu potentiellement habilité ou une institution, sans affirmer son soutien.
4. **Rendre compte** : faire revenir une observation ou une contribution dans le Corpus après qualification. La présentation éventuelle de l'élu reste un événement différent, observé par les canaux légitimes.

Une circulation qui ne revient jamais est `UNKNOWN`, et non un échec inféré. Une consultation du QR n'est ni consentement à être suivi, ni engagement politique. **Pas de lien individuel de traçage des personnes, pas de pixel ou identifiant navigateur imposé.**

## 4. Le 3Code est encore expérimental

Le protocole [3Code](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/3code.md) spécifie `3` plus huit caractères Base32 de Crockford, format `3XX-XXX-XXX`, avec collisions acceptées et résolution contextuelle. Le [MVP du registrar, Cogentia #323](https://github.com/JeanHuguesRobert/cogentia/issues/323) **n'a pas de preuve de déploiement au 18/11/2026**. Le générateur local :

- tire des références de 40 bits, uniformes par la projection cryptographique du SHA-256 sur 5 octets ;
- garantit seulement l'absence de doublon **à l'intérieur de son lot** (rééchantillonnage en cas de collision) ;
- conserve une identité `copy_id` indépendante et une graine d'exécution pour reproduire un lot ;
- marque tous les codes `unregistered` et les URL `inactive` jusqu'aux opérations réelles ;
- **ne réserve, n'enregistre ni ne résout aucun 3Code** et n'affirme pas le faire.

Le CSV généré n'est **pas** un registre fédéré 3Code. Les codes peuvent coïncider avec ceux de tiers ; un enregistrement ultérieur doit comporter sa propre autorité, provenance, métadonnées contextuelles et identité de record distincte. Ne pas publier 40 000 codes présentés comme activés avant recette effective.

**Test du Réel HTTP depuis Fracta2 (18/11/2026, lecture seule).** `https://capable.acorsica.org/` renvoie HTTP 200 et la page « Capable — Rendre possible, effectif et corrigible — Livre Vivant ». En revanche, `https://capable.acorsica.org/b/AV27-00001` renvoie HTTP 404 : **aucune fiche individuelle accessible à cette adresse**. `https://services.acorsica.org/3code` renvoie HTTP 200 mais sert une page titrée « Cogentia — PrivAI », **pas un registrar/résolveur 3Code attesté**. Un simple HTTP 200 ne suffit pas à identifier un service. Ces observations sont datées, sujettes à changement ; aucun déploiement n'a été effectué dans ce chantier.

## 5. Générateur de lot et maquettes (hors ligne)

**Dépendances :** Python 3.10+ ; bibliothèque standard pour le CSV ; `reportlab` et polices DejaVu Sans pour les PDF. Aucune connexion réseau ou donnée d'identification personnelle nécessaire.

```sh
# Un lot de 40 000, CSV + JSON (empreinte SHA-256, graine de reproduction, statut inactif)
python3 prepare_batch.py manifest --count 40000 --out sortie/manifest.csv

# Prototype A4 recto monochrome. Sans URL vérifiée : QR absent et avertissement visible
python3 prepare_batch.py master --out sortie/tract-prototype.pdf

# Prototype de 24 étiquettes (3 colonnes x 8 rangées)
python3 prepare_batch.py labels --manifest sortie/manifest.csv --out sortie/etiquettes-24.pdf --limit 24

# Test : aucun effet réseau, sans frais
python3 -m unittest discover -s . -p 'test_*.py' -v
```

Le rendu final ne doit utiliser `--url-template` et `--verified-url` **qu'après** vérification effective de l'adresse HTTPS de destination. Pour la variante individualisée, il faut avoir testé le handler exact sur au moins un exemplaire :

```sh
# Exemple de commande, non une URL déclarée opérationnelle
python3 prepare_batch.py labels --manifest sortie/manifest.csv \
  --out sortie/etiquettes-24-actives.pdf --limit 24 \
  --url-template 'https://capable.acorsica.org/b/{copy_id}' --verified-url
```

L'option `--verified-url` est une **attestation manuelle de l'opérateur**, pas un test HTTP intégré au programme. Son existence n'atteste pas le déploiement de `/b/`. Le QR direct doit fonctionner sans registrar 3Code, et une URL générique ne donne pas une biographie individuelle de l'objet. Le statut de 3Code non enregistré demeure visible même lorsque le QR a une URL vérifiée.

Les PDF sans URL vérifiée portent **PROTOTYPE — PAS POUR DISTRIBUTION** ou **QR inactif / essai**. Même avec un QR vers une URL testée, le tract maître porte **MAQUETTE — BON À TIRER NON VALIDÉ**. La maquette est une proposition de composition ; le contenu final, les mentions de l'imprimeur, du responsable et du mandataire, l'éditeur, le financement, l'identité des signataires, les coordonnées de contact et le bon à tirer demandent une revue spécifique.

## 6. Vie privée, état des objets et preuves

Un registre de biographie d'objet peut conserver des événements simples : `GENERATED`, `PRINTED`, `ISSUED`, `REOBSERVED`, `CONTRIBUTION_PROPOSED`, `CONTRIBUTION_QUALIFIED`, `RETIRED`, avec source, date, `copy_id`, qualification et révisions. **Seuls les deux premiers statuts sont disponibles après la fabrication correspondante**, jamais après la seule création d'un CSV. Le registre d'impressions et les actes électoraux sont distincts.

Les contributions individuelles passent par une interface de consentement et un espace de traitement non public avant qualification. Ne pas publier numéro de téléphone, adresse postale, identité de détenteur, position GPS ni corrélations de scans. La non-participation est autorisée. Un QR imprimé reste copiable et un événement auto-déclaré n'est pas une preuve de possession.

## 7. Financement politique — arrêt préalable à l'impression

L'[article L.52-8 du Code électoral](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000039446180) interdit le financement de la campagne d'un candidat par les personnes morales autres que les partis ou groupements politiques, y compris en nature et par avantages sous-évalués. Le [guide CNCCFP présidentielle 2027](https://cnccfp.fr/publication-du-guide-a-lusage-des-candidats-a-lelection-du-president-de-la-republique-et-de-leur-mandataire-edition-2026-2027/) indique une période de financement commencée le **1er avril 2026**. Les tracts sont généralement des dépenses électorales et doivent être imputés selon leur nature et les justificatifs ; le financement par un parti politique répond à un régime distinct, dont le statut juridique doit être établi.

**Avant commande/distribution** : déterminer qui commande, qui paie, quel est le statut légal d'A Voce, qui est le mandataire, quelle dépense sera imputée, quelle facture sera produite, et où figurent les mentions obligatoires. Ne pas utiliser la structure associative C.O.R.S.I.C.A. pour financer indirectement la candidature personnelle. Un devis ou un prototype préparé n'est pas une commande.

## 8. Tests du Réel et seuils de passage

| Étape | Résultat à constater | État au 18/11/2026 |
| --- | --- | --- |
| Prototype logiciel | CSV de 40 000 identités, contrôle de format, test PDF | Réalisé dans l'environnement de travail, sans impression |
| Prototype matériel | 24 étiquettes réellement imprimées, lecture humaine et QR éventuel | Non réalisé |
| Test public d'accès | Page cible et handler individuel HTTPS réellement consultables | Non attesté |
| Registrar 3Code | Premier enregistrement et résolution contradictoire vérifiés | Non attesté |
| Validation CNCCFP/mandataire | Qualification des moyens, identité du payeur, devis et mentions | Non réalisée |
| Bon à tirer | Validation texte, maquette, mentions et financement | Non donné |
| Impressions et émissions | Exemplaires effectivement imprimés et remis | Aucune observée |
| Résultats électoraux | Présentations officielles, selon les règles du CC | Aucun déduit de ce prototype |

**Contrôle éditorial / diffusion :** toute publication de la campagne au-delà de la préparation du code, tout message adressé à un élu ou partenaire, toute commande ou tout paiement exige son autorisation spécifique. Le mandat de développement sur `main` ne convertit pas la maquette en ordre d'impression.

## 9. Sources canoniques et continuité

- [Marche du Soleil](../marche-du-soleil.md) — finalité électorale, objets singuliers et observation.
- [Bouteille à la mer](../../../../musee-mariani/methodes/bouteille_a_la_mer.md) — biographie d'objet et contribution.
- [Cognitive Packet — incarnations et missions](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cognitive_packet_incarnations_and_missions.md).
- [3Code](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/3code.md), [Cogentia #323](https://github.com/JeanHuguesRobert/cogentia/issues/323) — spécification et état du registrar.
- [Observatoire des Présentations](../observatoire-presentations-2027.md) — états de preuve du parrainage.
- [CNCCFP — Présidentielle 2027](https://cnccfp.fr/elections/election-du-president-de-la-republique-2027/).

**Lentille Napoléon (analogie historique, non autorité) :** concentrer l'effort sur le goulot décisif — produire des rencontres vérifiables avec des élus habilités dans une diversité de territoires — plutôt que maximiser les scans ou le nombre abstrait d'objets. La diffusion de masse n'a de valeur opératoire qu'avec une continuité effective vers le bon acteur, libre de décider.