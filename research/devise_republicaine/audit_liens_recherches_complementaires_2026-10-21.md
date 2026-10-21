---
title: "Audit des liens secondaires et recherches complémentaires — devise républicaine"
date: "2026-10-21"
status: "working-audit — source-verified subset"
version: "0.1"
language: "fr"
document_role: "audit"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/devise_republicaine/audit_liens_recherches_complementaires_2026-10-21.md"
---

# Audit des liens secondaires et recherches complémentaires (21 octobre 2026)

## Périmètre et protocole

Cible : [draft public pour revue](histoire_devise_effectivite_autonomie_review_draft_2026-10-21.md), version 1.1-review-draft. Ce document enregistre les consultations **réellement réalisées**, distingue un succès de navigation de la pertinence probatoire, et ne présente pas comme vérifiés les liens non ouverts. Les liens GitHub internes du Corpus avaient fait l'objet d'un contrôle préalable ; les liens externes n'ont pas tous été testés individuellement.

La vérification inclut : contrôles de navigation par une consultation Web, confrontation ponctuelle du contenu à la proposition citée, recherche d'une source primaire équivalente lorsqu'un lien est obsolète, et réserve spécifique pour les liens qui exigent JavaScript ou interdisent une lecture automatisée. **Un 403 ou une page non extractible ne démontre pas une URL cassée pour un navigateur humain**.

## Résultats positifs directement contrôlés

| Ressource | URL | Résultat et portée |
| --- | --- | --- |
| OCDE, fiche France, Regulatory Policy Outlook 2025 | https://www.oecd.org/en/publications/oecd-regulatory-policy-outlook-2025_56b60e39-en/full-report/france_2b130ad5.html | Page officielle accessible, portant sur les pratiques de régulation ; ne prouve pas directement un manquement constitutionnel. |
| Commission de Venise, Rule of Law Checklist | https://www.coe.int/en/web/venice-commission/rule-of-law-checklist | Source officielle accessible : édition de 2016, révision adoptée en décembre 2025 et approbations institutionnelles en mai 2026 ; instrument d'évaluation, non norme directement contraignante en France. |
| Assemblée nationale, extraits art. 24 et 47-2 | https://www.assemblee-nationale.fr/14/controle/com_cec/textes_art_24_497.asp | Page officielle accessible, reproduit les articles utiles, mais historique (XIVe législature) ; pour le texte constitutionnel, préférer https://www.assemblee-nationale.fr/dyn/17/divers/texte_reference/01_constitution.html. |
| Élysée, notice de la devise | https://www.elysee.fr/la-presidence/liberte-egalite-fraternite | Page officielle accessible et affirme une inscription sur les frontons au 14 juillet 1880 ; c'est une **notice historique secondaire**. Elle ne remplace pas la preuve originale du texte ayant ordonné cette inscription. |
| Élysée, Constitution de la Ve République | https://www.elysee.fr/la-presidence/la-constitution-de-la-cinquieme-republique | Texte officiel accessible ; confirme devise à l'article 2 et organisation décentralisée à l'article premier. |
| Persée Éducation, Manuel général, 1892 | https://education.persee.fr/doc/magen_1257-5593_1892_num_59_28_49156 | Source d'époque consultable sur la présence de la devise sur les monuments publics ; témoigne de sa circulation, **pas du texte d'une décision de 1880**. |
| Persée Éducation, Manuel général, 1904 | https://education.persee.fr/doc/magen_1257-5593_1904_num_71_40_42649 | Source d'époque consultable sur l'écart entre l'inscription de la devise et sa mise en pratique ; rapprochement avec l'effectivité proposé par l'auteur. |
| Assemblée nationale, Constitution et évaluation | https://www.assemblee-nationale.fr/dyn/17/divers/texte_reference/01_constitution.html | Accès institutionnel et contrôle antérieur de la lettre des articles 24 et 47-2. |

## Liens non exploitables directement dans la consultation automatisée

- https://www.legifrance.gouv.fr/Droit-francais/Constitution/Declaration-des-Droits-de-l-Homme-et-du-Citoyen-de-1789 — réponse **403** de l'outil Web à la consultation. Ne pas conclure que la page est définitivement supprimée. Référence stable alternative : https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000697056/.
- https://qpc360.conseil-constitutionnel.fr/commentaire-decision-2018-717718-qpc — réponse **403** lors de la consultation. La décision elle-même est référencée séparément, https://qpc360.conseil-constitutionnel.fr/2018-07-06/decision-2018-717718-qpc-6-juillet-2018 ; vérifier le commentaire de décision par une recherche ciblée si ses formulations sont décisives.
- https://hudoc.echr.coe.int/eng?i=001-76253 — accès HUDOC sans contenu extractible par l'outil. L'URL peut fonctionner dans une interface JavaScript ; confirmer l'identification de l'affaire et son texte avant toute affirmation de fond fondée sur ce seul identifiant.

## Recherches complémentaires : avancées et limites

1. **1880, inscriptions publiques** — la notice de l'Élysée affirme l'inscription de la devise sur les frontons au 14 juillet 1880. Des sources pédagogiques de **1892** et **1904** confirment sa présence publique et son appropriation symbolique ultérieure. **Aucun acte administratif original de portée générale n'a été identifié au cours de cette passe** : ne pas transformer l'affirmation secondaire en référence normative primaire.
2. **1904, « prendre au mot » avant le concept** — le manuel scolaire insiste sur la nécessité que les pratiques concordent avec les mots de la devise. Cette source atteste l'existence historique d'une **critique de la devise simplement affichée**, pas une filiation directe avec le principe d'effectivité contemporain.
3. **OECD / Commission de Venise** — confirmer leurs usages comme diagnostics méthodologiques, non comme jurisprudences portant sur le régime corse.
4. **CEDH** — la vérification individualisée des liens HUDOC, de l'applicabilité de l'article 3 du Protocole n°1 et du détail des décisions demeure **non terminée** ; il faut conserver cette réserve dans toute diffusion académique.

## Décisions FBF et suite

- Source du projet constitutionnel et chiffres parlementaires : priorité à des documents officiels et à leurs statuts exacts.
- Sources historiques ajoutées au [draft v1.1](histoire_devise_effectivite_autonomie_review_draft_2026-10-21.md), commit documenté dans le paquet de suivi.
- **Statut du contrôle des liens : PARTIAL, vérifications nominatives effectuées et limites déclarées**. Un audit HTTP systématique indépendant de toutes les destinations reste possible mais n'est pas assimilable à une revue des arguments.
- Prochaine recherche ciblée : texte ou circulaire originale de 1880 ; vérification du commentaire QPC 2018 ; décisions HUDOC et applicabilité à un scrutin sénatorial ; établissement de citations page/paragraphe pour les sources secondaires seulement lorsqu'elles sont réellement utilisées.
