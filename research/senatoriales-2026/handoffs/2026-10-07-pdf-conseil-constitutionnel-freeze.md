# Handoff — PDF transmis au Conseil constitutionnel — 7 octobre 2026

## État probatoire gelé

Le PDF effectivement transmis au Conseil constitutionnel dans le dossier **2026-6589 SEN** est identifié par ses octets exacts :

- taille : **200 935 octets**
- SHA-256 : `2968cbe0a5de0f5e279e70d28c0769d4a8dbf8ca8f6f7e4571864333ecaa02a0`
- source commit : `66f34d0cb32e94509988b6f83a87c8a215b3fb81`
- publication commit : `0f9901d4f260728d43abc8b39b28598bec99d02e`
- Git blob : `aa79a43be5bef5d109a9d9d1f4e314827c257d89`
- GitHub Actions run : `37644531891`
- artifact id : `11493347352`
- artifact ZIP digest : `sha256:e606c157e4556c1f45b3133fa1b0fa2ebb1daf066d4310364f27653fcd72277f`

Manifeste canonique de gel :
`research/senatoriales-2026/frozen/2026-6589-SEN.yml`

URL immuable du PDF effectivement transmis :
https://raw.githubusercontent.com/JeanHuguesRobert/barons-Mariani/0f9901d4f260728d43abc8b39b28598bec99d02e/research/senatoriales-2026/review-pdf/66f34d0cb32e94509988b6f83a87c8a215b3fb81/requete-conseil-constitutionnel-REVIEW.pdf

Sauvegarde indépendante :
`/Archives/Conseil-constitutionnel/2026-6589-SEN/cc-petition-66f34d0-build-artifact.zip`

La mention interne « BROUILLON DE REVUE - NON DEPOSE » faisait partie du fichier transmis. Elle décrit son état de build antérieur, pas son statut réel après transmission.

## URL canonique publique

L'intention fonctionnelle retenue est qu'une URL stable serve le PDF courant puis, après gel, les octets gelés sans changer d'URL :

https://jhn.baronsmariani.org/cc/requete-conseil-constitutionnel-haute-corse-2026.pdf

Le routage correspondant a été ajouté dans `JeanHuguesRobert/inseme` via :
- `apps/platform/netlify/profiles/jhn/functions/cc-petition-pdf.js`
- `apps/platform/netlify.toml`
- `apps/platform/netlify/profiles/jhn/functions/artifact-access.js`

## Résidu technique à traiter

Ne pas considérer la mécanique GitHub Release actuellement présente dans
`.github/workflows/cc-petition-review-pdf.yml`
comme correcte.

Deux faits ont été établis :
1. les GitHub Releases du dépôt sont immuables ; un asset déjà publié ne peut pas être remplacé à URL constante ;
2. la tentative de création de la Release de build par GitHub Actions a échoué avec `HTTP 403 Resource not accessible by integration`.

En conséquence :
- le PDF gelé probatoire doit rester identifié par son hash et son commit immuable ;
- la sauvegarde indépendante doit être conservée ;
- l'URL publique stable doit être découplée du mécanisme de Release ;
- le workflow `cc-petition-review-pdf.yml` doit être nettoyé ultérieurement pour supprimer la logique de Release devenue incohérente ;
- les anciens `research/senatoriales-2026/review-pdf/<sha>/` sont un héritage de transition, pas le modèle cible pour les futurs builds.

## Trace GitHub

Issue #90 :
- commentaire de dépôt « brouillon de revue » : `6041758928`
- commentaire de gel probatoire : `6043828209`

Ce fichier a précisément pour fonction d'éviter qu'une reprise ultérieure dépende de la conversation ChatGPT qui a conduit à ces décisions.
