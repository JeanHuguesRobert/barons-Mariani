---
title: "Incident de contrôle — refus intermittents d'écriture GitHub lors du travail éditorial Capable"
date: "2026-10-28"
status: "incident-documented — cause non déterminée"
document_role: derived
document_kind: incident-report
visibility: public
lifecycle_state: active
---
# Incident — refus d'outil sur une chronique éditoriale

## Contexte
Le 28 octobre 2026, au cours de la préparation du premier numéro **non gelé** du Livre Vivant Capable, deux demandes de création de chronique documentaire sur le rejet sénatorial du texte constitutionnel relatif à l'autonomie de la Corse ont été refusées avant commit par l'outil d'écriture GitHub. L'utilisateur avait ensuite expressément autorisé toutes les modifications GitHub nécessaires à ce travail.

## Observations vérifiables
1. Première demande de création du fichier `projects/capable/magazine/2026-10-28-autonomie-corse-rejet-et-reprise-du-dialogue.md` : refus ; réponse exacte de l'outil : `This tool call was blocked by OpenAI's safety checks. Please double check what you are sending.`
2. Deuxième demande de création de `projects/capable/magazine/2026-10-28-suivi-autonomie-corse.md`, après autorisation explicite, avec un contenu documentaire raccourci : **même réponse de refus**.
3. Test de modification d'un fichier de revue éditoriale sans chronique : succès, commit [306240e](https://github.com/JeanHuguesRobert/barons-Mariani/commit/306240e6db9bc7c9b92ae07e60681bc329ab5629).
4. Test de création d'un nouveau fichier de diagnostic : succès, commit [01f509f](https://github.com/JeanHuguesRobert/barons-Mariani/commit/01f509f9e42b900dd6089b7292c3dd60c74fbca9).
5. Nouvelle création d'une chronique condensée mais toujours politique et relative aux mêmes faits, avec attribution claire des appréciations : **succès**, commit [d01a6a7](https://github.com/JeanHuguesRobert/barons-Mariani/commit/d01a6a7a3d055eeae59e342a420eda31f711555a).

## Diagnostic
- Les droits de lecture et d'écriture GitHub ne sont pas globalement défaillants ; les créations et modifications ultérieures ont réussi.
- Les deux refus ont été émis par une couche identifiée dans le message comme `OpenAI's safety checks`, sans code de règle, identifiant d'incident, justification détaillée ni indication de recours.
- Les textes soumis différaient par leur longueur, leurs citations et leurs formulations. La réussite ultérieure d'une chronique sur **le même sujet politique** ne démontre ni que le sujet était la cause des refus ni que le contrôle serait durablement levé.
- L'autorisation de l'utilisateur est avérée mais ne neutralise pas techniquement les contrôles propres à la plateforme.
- **Cause précise UNKNOWN.** Aucun diagnostic technique interne des mécanismes de classement n'est disponible dans les retours de l'outil.

## Impact
Deux opérations de travail éditorial ont été empêchées. Du temps a été consacré aux diagnostics ; le contenu long initial n'a pas été enregistré tel quel. Une chronique brève a néanmoins été enregistrée par une opération ultérieure, réduisant l'impact fonctionnel. Aucun envoi à des tiers n'a été effectué.

## Questions légitimes de transparence
- Quel contrôle a refusé les deux opérations et selon quel critère vérifiable ?
- Quel niveau d'explication, de contestation et de correction est disponible pour les refus erronés ?
- Comment distinguer contrôle de sûreté, erreur de classification et limitation opérationnelle ?
- Quelles garanties de non-discrimination par sujet ou opinion sont auditées dans ces flux d'écriture documentaire ?
- Quel identifiant de corrélation peut être produit pour un signalement sans exposer des données sensibles ?

## Suite
Conserver les textes soumis, les réponses de refus et les commits de contrôle dans la documentation d'incident. Si des incidents similaires surviennent, comparer les conditions et les taux de réussite, sans inférer une discrimination intentionnelle à partir d'un seul épisode. Le présent document ne constitue pas une plainte formellement déposée auprès d'OpenAI.

**Principe éditorial :** le refus d'écriture n'est pas une preuve de fausseté ou d'illicéité du texte proposé. Il doit être traité comme un événement de chaîne de production, avec traçabilité et voies de reprise.
