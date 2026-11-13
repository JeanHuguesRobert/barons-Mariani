---
title: "Réconciliation finale — stash du ThinkPad barons-Mariani"
date: "2026-11-13"
document_role: "operational"
document_kind: "cognitive-packet-reconciliation"
visibility: "public"
lifecycle_state: "working"
status: "reconciled"
review:
  status: "unreviewed"
  reviewed_by: []
related_issues:
  - "https://github.com/JeanHuguesRobert/barons-Mariani/issues/152"
  - "https://github.com/JeanHuguesRobert/barons-Mariani/issues/111"
  - "https://github.com/JeanHuguesRobert/barons-Mariani/issues/99"
  - "https://github.com/JeanHuguesRobert/cogentia/issues/273"
---

# Réconciliation du stash du ThinkPad

**Objet historique :** 229262b1f58c08fe2e31e705c934b7141b49a0f2.

**Référence principale examinée :** 54268c3c08fccefe4f0fb308af98c78b996de783.

Le contrôle compare les 73 chemins énumérés par Git dans le stash à la branche canonique après réconciliation. Deux entrées sont des suppressions anciennes sans contenu à restaurer. Ce document conserve les décisions et les empreintes ; il ne transforme pas les anciens brouillons en textes validés.

## Décisions de réconciliation

- **Capable #152 :** les cinq Cas du Réel, leur index et la chronique ont été réintroduits comme brouillons non relus. Les chapitres d'ouverture, de campagnes et de Capable Test ont repris les méthodes d'épreuve et de traçabilité EIM. La page des cas, débarrassée du domaine abandonné et des affirmations non étayées, est déployée sur le site canonique ; les deux anciennes variantes de noms de cas étaient des suppressions historiques.
- **1755 #111 :** les deux fiches inédites sont désormais des questions d'archives à vérifier, incluses dans l'assemblage en préparation. Leur existence ne prouve ni suffrage universel féminin ni transmission directe à la Révolution américaine.
- **Napoléon #99 :** une fiche d'archives de jeunesse, le registre des éditions et la doctrine de correction Janus ont été incorporés. La seconde architecture historique du stash a été réconciliée dans le document existant, sans duplication.
- **Commons :** la règle comptable universelle de l'ancien brouillon est corrigée en une grille de questions vérifiables sur les coûts, surplus et péréquations.
- **PrivAI :** l'article actuel ajoute les références historiques/juridiques Horizon et Robodebt et remplace un lien local obsolète. Les éditions de travail restent non gelées.
- **Potentics et doctrine :** les textes récents sont plus nuancés. Le Spirit of Synthesis reste une question de mécanismes, et un gain de performance quantitatif ne vaut pas preuve scientifique universelle. La maxime de Kudocracy sur la traçabilité proportionnée reste explicitement présente.
- **Vues générées et profils :** les fichiers fédérés, index de recherche, statut de Corpus et profils de presse disposent de versions canoniques plus récentes. Leur ancien état ne doit pas écraser les nouvelles structures de données.
- **Version rhétorique :** certains anciens chapitres Capable employaient un langage plus polémique que leurs révisions ; leur ancien style n'est pas arbitrairement déclaré incorrect, mais il ne justifie pas la restauration d'une version de travail concurrente et parfois doctrinalement contradictoire.

Le présent bordereau ne prétend pas valider scientifiquement ou juridiquement les travaux. Il permet de retirer la référence de stash sans revenir à ses anciennes représentations du Corpus. Les apports nécessitant encore des tests ou des sources restent suivis dans les issues existantes. Aucun livre gelé n'est modifié.

## Manifeste de concordance

Les empreintes SHA-256 abrégées portent sur les octets des versions historiques et canoniques examinées. Deux anciennes suppressions n'ont pas d'empreinte de contenu.

| Chemin Git | Classement | Historique SHA-256 | Main SHA-256 |
| --- | --- | --- | --- |
| `projects/1755/cases/case-01-dieta-generale-1755.md` | Source reprise et vérifiée | `82cc411be55a9586` | `323796135c83d020` |
| `projects/1755/cases/case-02-reception-transnationale-boswell.md` | Source reprise et vérifiée | `9fd202ec4215291c` | `fb84b739fffca005` |
| `projects/1755/magazine/federated/commons-2026-10-04-communs-energetiques-fractavolta.json` | Projection générée supersédée | `687646d180a27753` | `5bd215538a252a14` |
| `projects/1755/magazine/federated/institut-2026-10-04-fondation-du-livre-vivant-institut.json` | Projection générée supersédée | `2670a7329b4d3cf8` | `d77ff7c9132dc71c` |
| `projects/1755/press/profile.yml` | Schéma de presse modernisé | `9426b63500606d43` | `b04d2b4300659d06` |
| `projects/capable/cases/README.md` | Source de cas modernisée | `e5e35db2ae8d9efb` | `0934e4872f2be565` |
| `projects/capable/cases/case-01-kouchner-acces-dossier-medical.md` | Source de cas modernisée | `449713ffe8cc4029` | `112e555f69c2c6f1` |
| `projects/capable/cases/case-01-parrainages-presidentielle-2027.md` | Ancienne suppression | `—` | `—` |
| `projects/capable/cases/case-02-effectivite-service-public-rural.md` | Ancienne suppression | `—` | `—` |
| `projects/capable/cases/case-02-parrainages-presidentiels-verrou-rural.md` | Source de cas modernisée | `2e9c26495dce0540` | `a2ff13999ce6f21e` |
| `projects/capable/cases/case-03-dalo-droit-au-logement-sans-toit.md` | Source de cas modernisée | `e17fc1269bf61807` | `d4da439907680a60` |
| `projects/capable/cases/case-04-consignation-radars-automatiques.md` | Source de cas modernisée | `0c6beb068d76f1d0` | `1f96b45b7a8c5f20` |
| `projects/capable/cases/case-05-dematerialisation-service-public-rural.md` | Source de cas modernisée | `0627cb2aa1660f13` | `3fd7f15abc9326b9` |
| `projects/capable/magazine/2026-10-05-epreuve-de-l-effectivite.md` | Source plus récente conservée | `7e4d7b93cb556acd` | `ce22039d8fe0bcaf` |
| `projects/capable/manuscript/00-ouverture.md` | Fusion sémantique dans le Corpus | `1485536172065701` | `763f3c1240022149` |
| `projects/capable/manuscript/05-machines-et-correction.md` | Source plus récente conservée | `bd5eb0957e081fcc` | `86ee45a5052b66f4` |
| `projects/capable/manuscript/07-campagnes-comme-reality-tests.md` | Fusion sémantique dans le Corpus | `70c2426a369ff26f` | `f5645df16c6ac921` |
| `projects/capable/manuscript/08-presidentielle-2027.md` | Source plus récente conservée | `cb91d1324f1ad912` | `934107c43c9a6069` |
| `projects/capable/manuscript/10-capable-test.md` | Fusion sémantique dans le Corpus | `f1b8dad65a051693` | `c83bd1ed16d31e96` |
| `projects/capable/site/cases.html` | Source reprise et vérifiée | `93b74034e48aca1c` | `b6d8c24e3545ee1b` |
| `projects/commons/accounting/modele-economique-communs.md` | Fusion sémantique dans le Corpus | `6517ba5d9e1f2721` | `f880ed034388aba8` |
| `projects/commons/magazine/federated/privai-2026-10-04-illusion-electeur-synthetique.json` | Projection générée supersédée | `05c027dab0d5a303` | `1da61606b989f863` |
| `projects/commons/magazine/federated/village-2026-10-04-lancement-livre-vivant-mariani-village.json` | Projection générée supersédée | `98db37fa94a4bf16` | `00a819b581c9cab1` |
| `projects/commons/press/profile.yml` | Schéma de presse modernisé | `e230853ee94ca823` | `3febff2fb7794f18` |
| `projects/napoleon/cases/case-01-sources-jeunesse-bonaparte-ajaccio.md` | Source reprise et vérifiée | `8345968ddd00ebf7` | `1c5745b3bb3508ac` |
| `projects/napoleon/editions/index.md` | Source reprise et vérifiée | `ecc9f296aca21971` | `5006b9e9c1743a41` |
| `projects/napoleon/editorial-architecture.md` | Fusion sémantique dans le Corpus | `9896722e81a23005` | `—` |
| `projects/napoleon/press/profile.yml` | Schéma de presse modernisé | `4efd5a5ad57e54b5` | `1ff4f0e791fa5627` |
| `projects/privai/magazine/2026-10-05-de-horizon-a-robodebt-lepreuve-du-capable-test.md` | Fusion sémantique dans le Corpus | `e2181a8691619d44` | `eb5e04295035575e` |
| `projects/privai/magazine/federated/commons-2026-10-04-communs-energetiques-fractavolta.json` | Projection générée supersédée | `312d80ca77072b48` | `98791401fe376acc` |
| `projects/privai/magazine/federated/school-2026-10-04-ouverture-mariani-school-of-autonomy.json` | Projection générée supersédée | `d47811f61c8a9106` | `ebe55a37b7ba1590` |
| `projects/privai/press/profile.yml` | Schéma de presse modernisé | `e20401a2651fe697` | `543e450d8dc14bca` |
| `research/acorsica-institut-mariani.md` | Identique | `cb6274789f4069d9` | `cb6274789f4069d9` |
| `research/agile.md` | Identique | `54b03ab1040d0a41` | `54b03ab1040d0a41` |
| `research/alien_academic.md` | Identique | `7321d42274dcfd4b` | `7321d42274dcfd4b` |
| `research/alien_blogpost.md` | Identique | `2172ed5b1ae5f63e` | `2172ed5b1ae5f63e` |
| `research/applied_possibilism.md` | Identique | `c8530cbf92572fe0` | `c8530cbf92572fe0` |
| `research/autonomia.md` | Source plus récente conservée | `2feb1e9f1267dabe` | `5f306b3061b57472` |
| `research/autonomia/1755.md` | Source plus récente conservée | `6f15fddf69021896` | `181bbd0a7c025f0a` |
| `research/autonomia/grammaire_autonomie_de_capacite.md` | Source plus récente conservée | `cda883f270bd78bd` | `bd98e3da40b5fb4b` |
| `research/autonomia/impunite_par_obscurite_blogpost.md` | Identique | `6dda4c6b7820f444` | `6dda4c6b7820f444` |
| `research/autonomia/impunite_par_obscurite_cas_corse.md` | Identique | `93aa930baba9df69` | `93aa930baba9df69` |
| `research/autonomia/projet_1755.md` | Source plus récente conservée | `9dd4a664e092b2a2` | `fcc3772a1c753638` |
| `research/christianity_verticalization.md` | Identique | `7ae773aede99d934` | `7ae773aede99d934` |
| `research/christianity_verticalization_blogpost.md` | Identique | `980a918a56ffca9c` | `980a918a56ffca9c` |
| `research/cognitive_waves.md` | Identique | `c7bf33d906871e5d` | `c7bf33d906871e5d` |
| `research/concepts.md` | Source plus récente conservée | `c5b94f932490c147` | `44160cc4d0ce9e72` |
| `research/contribution_commission_lois_autonomie_capacite.md` | Source plus récente conservée | `7bd601f19ef84eb5` | `17b9c5a99c445156` |
| `research/corpus-status.md` | Projection générée supersédée | `854d073873519ba5` | `7a48e08f90e67ca2` |
| `research/democratic_ai_safety.md` | Identique | `ac5df7588d9cf932` | `ac5df7588d9cf932` |
| `research/gr20_autonomie_de_capacite.md` | Identique | `5babeb67322f4bfc` | `5babeb67322f4bfc` |
| `research/index.md` | Projection générée supersédée | `1ae06134bf1d4696` | `1d6d4d624a4e026c` |
| `research/invidia.md` | Identique | `e89ea3da63fd0ca0` | `e89ea3da63fd0ca0` |
| `research/kudocracy.md` | Fusion sémantique dans le Corpus | `09d11d438647e375` | `4d955673c8122246` |
| `research/kudos.md` | Source plus récente conservée | `e4f06255e65556fa` | `114b388a25c51643` |
| `research/methode_terrains_feconds.md` | Source plus récente conservée | `b2783424eb32e4da` | `18997365e949493b` |
| `research/mimetic_desynchronization.md` | Source plus récente conservée | `65f86af86e7ca47c` | `67358af1bdb9a756` |
| `research/pathologie_du_secret.md` | Identique | `31a2ea8d36368f04` | `31a2ea8d36368f04` |
| `research/patrimoine/bleu_chine_denim_article_academique.md` | Identique | `e2ce4da8f2840403` | `e2ce4da8f2840403` |
| `research/patrimoine/bleu_chine_denim_chronologie.md` | Identique | `718fe442d88eec2e` | `718fe442d88eec2e` |
| `research/patrimoine/bleu_chine_denim_nimes_corse_v0.2.md` | Source plus récente conservée | `79fd050e4b9c7a53` | `e587583df4b94a94` |
| `research/patrimoine/bleu_chine_denim_sources_annotees.md` | Identique | `4e8590331b3aae0f` | `4e8590331b3aae0f` |
| `research/possibilism_04_2026.md` | Identique | `4dd20f14bb4d383c` | `4dd20f14bb4d383c` |
| `research/potentics.md` | Fusion sémantique dans le Corpus | `9c793890740b3521` | `bed7e0a381c2aa95` |
| `research/second_method.md` | Source plus récente conservée | `76ac42bd5da3897c` | `e5e4936dc93adc58` |
| `research/stigmergie_sans_limite_haute.md` | Identique | `ec9eda7a5a69da82` | `ec9eda7a5a69da82` |
| `research/test_critere_rossignol.md` | Identique | `6361ca9dc5156136` | `6361ca9dc5156136` |
| `research/the_republic_of_donkeys.md` | Identique | `29676c1242a6ef5a` | `29676c1242a6ef5a` |
| `research/tocqueville_law.md` | Identique | `1860614cfca561ad` | `1860614cfca561ad` |
| `research/toy_story.md` | Identique | `32839afde855cb8e` | `32839afde855cb8e` |
| `research/traceabilite_civique_antimafia.md` | Identique | `8de7ad24d67708ba` | `8de7ad24d67708ba` |
| `research/traceabilite_des_actes.md` | Source plus récente conservée | `8f9f67cfea7e2237` | `2ac35cc3e5bb28d5` |
| `research/vigilia.md` | Identique | `5321906f76ee3d03` | `5321906f76ee3d03` |

## Paquets de continuation

Capable : https://github.com/JeanHuguesRobert/barons-Mariani/issues/152

1755 : https://github.com/JeanHuguesRobert/barons-Mariani/issues/111

Napoléon : https://github.com/JeanHuguesRobert/barons-Mariani/issues/99

Maintenance Git : https://github.com/JeanHuguesRobert/cogentia/issues/273
