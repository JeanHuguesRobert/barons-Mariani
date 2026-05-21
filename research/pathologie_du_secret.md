---
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
license: "CC BY-SA 4.0"
---
<!-- BEGIN_AUTO: trails -->
> 🧭 **Trail: From Autonomia to DHITL**
> ⬅️ Previous: [Democratic AI Safety](democratic_ai_safety.md) | ➡️ Next: [DHITL — Democratic Humans in the Loop](https://github.com/JeanHuguesRobert/marenostrum/blob/main/DHITL.md)

<!-- END_AUTO: trails -->

---
canonical_url: https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/pathologie_du_secret.md
last_stamped_at: 2026-05-20
---
# La pathologie du secret
## Imputabilité humaine, traçabilité démocratique et refus de l’irresponsabilité artificielle

**Statut :** Working paper v0.4  
**Dépôt suggéré :** `barons-Mariani/research/`  
**Nom de fichier suggéré :** `pathologie_du_secret.md`  
**Auteur :** Jean Hugues Robert  
**Licence suggérée :** CC BY 4.0  
**Date :** 20 mai 2026  
**Note de version :** v0.4 intègre un cas d’usage français majeur — DataJust —, renforce l’ancrage dans le droit positif français et européen, traite plus sérieusement les risques de cybersécurité et de chaîne d’approvisionnement, et applique plus explicitement la seconde méthode.

---

## Abstract

Recent legal developments concerning AI-generated inventions and works establish a clear institutional boundary: artificial intelligence may assist, generate, suggest or optimize, but it cannot be designated as an inventor, an author, or a responsible legal subject. Patent and copyright law thus preserve a requirement of human imputability when private rights are claimed.

This paper argues that the same requirement must apply even more strongly to public acts, commons, administrative decisions, judicial assistance systems, and digital infrastructures. If a human must be identified in order to own, a human — or an accountable human chain of mandate — must also be identified when algorithmic systems act upon citizens, public resources, judicial processes, or shared institutions.

The French DataJust project illustrates the problem in a particularly sensitive domain: the Ministry of Justice was authorized in 2020 to develop an algorithmic system intended to extract and exploit data from court decisions on bodily injury compensation, with possible uses for informing parties and documenting judges. Even when such a system is lawful, experimental, and presented as merely indicative, it raises the central democratic question: who remains accountable when an algorithmic artifact influences the conditions under which justice is understood, negotiated, or rendered?

Security by secrecy aggravates the problem. Tactical secrecy can be legitimate. Structural opacity is different: it often protects those who administer systems from democratic scrutiny. A democratic digital infrastructure should not promise invulnerability; it should guarantee that violations, abuses, failures and distortions can be detected, evidenced, attributed, contested, corrected, repaired and sanctioned.

The central thesis is simple: **we cannot require a human to own, then accept a machine to govern.**

---

## Résumé

Les jurisprudences et positions institutionnelles récentes relatives aux inventions et aux œuvres produites avec l’assistance de l’intelligence artificielle établissent une ligne claire : une IA peut être un outil, mais elle ne peut pas être désignée comme inventeur ou comme auteur.

Dans les affaires DABUS, les offices et juridictions ont refusé qu’une machine soit nommée inventeur d’un brevet. En droit d’auteur américain, les décisions relatives à *Thaler v. Perlmutter* et les positions du U.S. Copyright Office confirment qu’une œuvre générée par IA n’est protégeable que si une contribution humaine suffisante peut être identifiée.

Cette exigence n’est pas seulement une survivance anthropocentrique. Elle révèle un principe institutionnel plus profond : lorsqu’un acte produit des effets juridiques, économiques, sociaux ou politiques, il doit pouvoir être rattaché à un sujet humain, une institution ou une chaîne de mandat identifiable.

Dès lors, il serait incohérent d’exiger un humain pour revendiquer un brevet privé ou une œuvre privée, tout en tolérant que des actes publics, administratifs, judiciaires ou collectifs soient attribués à “l’algorithme”, “au système” ou “à l’IA”, sans responsable humain clairement désigné.

Le cas français DataJust donne à cette question une gravité particulière. Par décret du 27 mars 2020, le ministère de la justice a été autorisé à développer un traitement automatisé de données destiné à extraire et exploiter des décisions relatives à l’indemnisation des préjudices corporels, avec pour finalités notamment l’information des parties et la documentation des juges. Même légal, expérimental et présenté comme indicatif, un tel dispositif touche à la manière dont une institution judiciaire peut être informée, orientée ou standardisée.

Ce texte défend une thèse simple :

> **On ne peut pas exiger un humain pour posséder, puis accepter une machine pour gouverner.**

La protection par le secret aggrave cette incohérence. Elle prétend sécuriser les infrastructures, mais elle protège souvent les gardiens du système contre le contrôle démocratique. Le secret peut être légitime comme exception tactique. Il devient dangereux lorsqu’il devient régime d’irresponsabilité.

---

## 1. Introduction : le privé exige l’humain, le public tolérerait-il l’irresponsable ?

Le droit de la propriété intellectuelle est en train de poser une limite nette à l’intelligence artificielle.

Une IA peut assister.  
Une IA peut générer.  
Une IA peut proposer.  
Une IA peut combiner.  
Une IA peut optimiser.

Mais une IA ne peut pas être inventeur.  
Une IA ne peut pas être auteur.  
Une IA ne peut pas être sujet responsable.

En Europe, l’Office européen des brevets a confirmé, dans les recours J 8/20 et J 9/20 relatifs à DABUS, qu’une machine ne peut pas être désignée comme inventeur dans une demande de brevet européen. L’inventeur doit être une personne physique, c’est-à-dire un sujet juridiquement capable d’être désigné, identifié et rattaché à une revendication.

Au Royaume-Uni, la Supreme Court a confirmé en 2023 que DABUS ne pouvait pas être inventeur au sens du droit britannique des brevets.

Aux États-Unis, l’USPTO a rappelé que seuls des êtres humains peuvent être nommés inventeurs, même lorsque des systèmes d’IA ont contribué au processus inventif. L’IA peut être un outil ; elle ne devient pas inventeur.

En droit d’auteur américain, le U.S. Copyright Office a confirmé en 2025 que les productions d’IA générative ne sont protégeables que lorsqu’un auteur humain a déterminé des éléments expressifs suffisants. Le simple fait de fournir des prompts ne suffit généralement pas à établir cette contribution créative. La Cour d’appel du District of Columbia, dans *Thaler v. Perlmutter*, a confirmé en 2025 qu’une œuvre générée exclusivement par une machine ne peut pas être protégée par copyright en l’absence d’auteur humain.

La question politique surgit immédiatement :

> **Si le droit exige une personne humaine pour attribuer une propriété privée, pourquoi accepterait-on moins lorsqu’il s’agit d’actes publics, de communs, de décisions administratives, judiciaires ou d’infrastructures collectives ?**

Il serait absurde que la propriété privée bénéficie d’un régime d’imputabilité plus exigeant que le bien commun.

---

## 2. Une analogie, non une déduction mécanique

Il faut être précis. Les jurisprudences relatives aux brevets et au droit d’auteur ne règlent pas directement la question des décisions administratives, des actes publics algorithmiques, des outils judiciaires ou des infrastructures communes.

Elles appartiennent à des domaines particuliers :

- le droit des brevets ;
- le droit d’auteur ;
- les conditions d’attribution d’un droit de propriété intellectuelle ;
- la désignation d’un inventeur ou d’un auteur.

Il ne s’agit donc pas d’en déduire mécaniquement une règle de droit public.

L’intérêt est ailleurs. Ces décisions révèlent une intuition juridique et institutionnelle plus générale : **un effet opposable aux tiers ne doit pas être attribué à une entité incapable de répondre**.

Un brevet produit un droit d’exclusion.  
Une œuvre protégée produit un droit opposable.  
Une décision publique produit des effets sur des droits, des accès, des ressources, des libertés ou des obligations.  
Un outil judiciaire indicatif peut influencer les représentations, les négociations, les montants attendus, les comportements des parties et, indirectement, les décisions.

Dans tous ces cas, il faut pouvoir répondre à des questions élémentaires :

- qui agit ?
- qui revendique ?
- qui bénéficie ?
- qui décide ?
- qui peut être contesté ?
- qui peut répondre ?
- qui peut réparer ?
- qui peut être sanctionné ?

Une IA ne peut répondre à aucune de ces questions. Elle ne possède ni volonté juridique, ni responsabilité morale, ni patrimoine propre, ni capacité ordinaire à répondre d’un dommage, ni devoir envers autrui.

Le droit refuse donc une fiction dangereuse : celle d’un effet juridique sans sujet imputable.

Cette intuition doit être prise au sérieux bien au-delà de la propriété intellectuelle.

---

## 3. Le principe d’imputabilité humaine

Les décisions récentes sur l’IA ne disent pas seulement : “une machine n’est pas un auteur”.

Elles disent plus profondément :

> **Un acte ou un effet opposable aux tiers ne doit pas naître d’une origine irresponsable.**

Dans un brevet, le droit demande : qui a inventé ?  
Dans une œuvre, le droit demande : qui a créé ?  
Dans une administration, il faut demander : qui a décidé ?  
Dans une infrastructure commune, il faut demander : qui a conçu, validé, déployé, supervisé, corrigé et assumé ?  
Dans un outil judiciaire, il faut demander : qui a produit la règle implicite, le référentiel, la donnée, la pondération, le nettoyage, le modèle et l’usage ?

Formule centrale :

> **Humain exigé pour la propriété. Humain exigé pour la responsabilité.**

Ou, plus directement :

> **Pas de brevet sans inventeur humain.  
> Pas d’œuvre protégée sans auteur humain.  
> Pas d’acte public algorithmique sans responsable humain.  
> Pas d’outil judiciaire sans chaîne humaine d’imputabilité.**

---

## 4. Cas principal : DataJust, quand l’algorithme approche l’institution judiciaire

Le cas DataJust est probablement l’un des exemples français les plus sensibles, non parce qu’il serait nécessairement illégal ou mal intentionné, mais parce qu’il touche à la justice elle-même.

Le décret n° 2020-356 du 27 mars 2020 a autorisé le garde des sceaux, ministre de la justice, à mettre en œuvre, pour une durée de deux ans, un traitement automatisé de données à caractère personnel dénommé **DataJust**. Sa finalité était le développement d’un algorithme destiné notamment à :

1. réaliser des évaluations rétrospectives et prospectives des politiques publiques en matière de responsabilité civile ou administrative ;
2. élaborer un référentiel indicatif d’indemnisation des préjudices corporels ;
3. informer les parties et aider à l’évaluation du montant de l’indemnisation à laquelle les victimes peuvent prétendre, notamment pour favoriser un règlement amiable ;
4. informer ou documenter les juges appelés à statuer sur des demandes d’indemnisation des préjudices corporels.

Ce n’est pas un détail technique. L’indemnisation des préjudices corporels concerne des victimes, des assureurs, des avocats, des magistrats, des fonds d’indemnisation, des expertises médicales, des vies brisées et des montants parfois décisifs pour la survie matérielle d’une personne.

Un référentiel indicatif n’est pas une décision juridictionnelle. Mais il peut exercer une force normative indirecte : il oriente les attentes, stabilise des fourchettes, influence les négociations, modifie les stratégies des parties, contribue à une forme de standardisation et peut, à terme, produire un effet de gravité autour de ce qui paraît “normal”.

La question n’est donc pas seulement : DataJust était-il légal ?

La question est :

> **Quand un algorithme contribue à structurer l’environnement cognitif d’une décision judiciaire, quelle chaîne d’imputabilité doit être exigée ?**

Le Conseil d’État a été saisi de recours contre le décret DataJust et les a joints pour statuer par une décision du 30 décembre 2021. La solidité juridique ponctuelle du décret ne suffit cependant pas à épuiser la question institutionnelle. L’enjeu démocratique commence précisément là où la légalité minimale cesse d’être suffisante.

Il faut pouvoir répondre :

- qui a choisi les décisions sources ?
- qui a défini les catégories de préjudices ?
- qui a nettoyé les données ?
- qui a arbitré les cas ambigus ?
- qui a conçu le modèle ?
- qui a validé les sorties ?
- qui a évalué les biais possibles ?
- qui a contrôlé les effets sur les victimes ?
- qui répond si le référentiel tire les montants vers le bas ?
- qui répond si un assureur s’en sert comme pression ?
- qui répond si un juge s’y conforme par facilité ou par effet d’ancrage ?

La réponse ne peut pas être : “l’algorithme”.

Elle ne peut pas davantage être : “le système”.

Elle doit être une chaîne humaine et institutionnelle claire : ministère, direction responsable, équipe projet, prestataires éventuels, autorités de contrôle, magistrats utilisateurs, règles de supervision, modalités de contestation, conditions de retrait ou de correction.

DataJust montre donc le point critique de ce texte : **plus l’objet public est sensible, plus l’imputabilité doit être exigeante**.

Dans une démocratie, la justice ne peut pas devenir un environnement où l’on exige des humains pour créer des droits privés, mais où l’on accepte des machines comme sources opaques de normalisation publique.

---

## 5. Le droit positif n’est pas absent : il faut l’étendre, non l’inventer

Ce texte ne prétend pas créer ex nihilo une exigence de transparence algorithmique. Le droit français et européen connaît déjà plusieurs éléments de cette exigence.

Le Code des relations entre le public et l’administration impose déjà, dans certaines conditions, l’information relative aux décisions administratives individuelles prises sur le fondement d’un traitement algorithmique. Il impose aussi la publication en ligne des règles définissant les principaux traitements algorithmiques utilisés par les administrations lorsqu’ils fondent des décisions individuelles, sous réserve des secrets protégés.

Le RGPD encadre les décisions individuelles automatisées et les traitements de données personnelles.

Le règlement européen sur l’intelligence artificielle renforce encore cette logique pour les systèmes à haut risque : documentation, journalisation, supervision humaine, gestion des risques, robustesse et traçabilité.

La Défenseure des droits a toutefois souligné en 2024 que l’algorithmisation des services publics soulève encore des risques importants pour les droits des usagers, notamment lorsque l’intervention humaine est insuffisante, formelle ou mal définie. Elle insiste sur la nécessité d’une intervention humaine réelle et sur le renforcement de la transparence.

Le présent texte ne dit donc pas : “rien n’existe”.

Il dit :

> **Ce qui existe déjà partiellement doit être élevé au rang de principe général d’imputabilité démocratique.**

Il ne suffit pas d’avoir des obligations dispersées. Il faut une doctrine générale : lorsqu’un système algorithmique contribue à produire un effet public, l’imputabilité humaine et institutionnelle doit être explicite, documentée, vérifiable et contestable.

---

## 6. De la propriété privée au commun

Le raisonnement doit être étendu au public et aux communs.

Si une personne humaine doit être désignée pour revendiquer un brevet, alors une personne humaine — ou une chaîne humaine de mandat — doit être désignée lorsqu’un système algorithmique produit, recommande ou exécute un acte engageant le public.

Si une personne humaine doit être identifiable pour revendiquer une œuvre, alors une personne humaine doit être identifiable lorsqu’une IA oriente :

- une décision administrative ;
- une allocation de ressources ;
- une priorisation d’accès ;
- une recommandation publique ;
- une sanction ;
- une exclusion ;
- un classement ;
- une décision de police ;
- une décision sociale ;
- une politique territoriale ;
- une aide à la décision judiciaire ;
- un référentiel public ou quasi-public.

Le commun n’est pas seulement ce qui appartient à l’État. Le commun est ce dont dépend la capacité d’agir d’une communauté.

Il peut être :

- public ;
- associatif ;
- territorial ;
- open source ;
- informationnel ;
- judiciaire ;
- administratif ;
- infrastructurel ;
- hybride public-privé.

Une plateforme privée peut gouverner de fait un commun numérique. Un modèle d’IA peut structurer un accès au savoir. Un système de paiement peut conditionner la vie économique. Un cloud peut devenir une dépendance territoriale. Un algorithme de classement peut orienter la visibilité politique.

Le commun est souvent plus fragile que le privé parce qu’il n’a pas toujours de propriétaire direct, vigilant et intéressé à sa défense. C’est précisément pourquoi il exige davantage de traçabilité, non moins.

---

## 7. L’asymétrie dangereuse

Le danger serait de construire une asymétrie au profit du privé.

| Domaine privé | Domaine public ou commun |
|---|---|
| Le droit exige un inventeur humain | On accepterait une décision “de l’algorithme” |
| Le droit exige un auteur humain | On tolérerait une recommandation sans auteur |
| Le droit protège la chaîne de propriété | On négligerait la chaîne de responsabilité |
| Le droit refuse l’IA comme sujet de droit | On utiliserait l’IA comme écran d’irresponsabilité |

Cette asymétrie serait politiquement toxique.

Le privé obtiendrait :

> attribution, propriété, exclusivité, recours.

Le public subirait :

> automatisation, opacité, dilution, irresponsabilité.

Il faut refuser cette inversion.

---

## 8. L’IA comme paravent

Le vrai risque n’est pas seulement que l’IA soit reconnue comme auteur ou inventeur.

Le vrai risque est qu’elle devienne un paravent.

On dira :

> “Ce n’est pas moi, c’est le système.”

Ou :

> “La décision résulte de l’algorithme.”

Ou encore :

> “L’IA a recommandé cette action.”

Mais une machine ne comparaît pas politiquement.  
Une machine ne rend pas de comptes.  
Une machine ne peut pas être révoquée par les citoyens.  
Une machine ne porte pas la honte d’un abus.  
Une machine ne répond pas devant une assemblée, un tribunal ou une communauté.

L’IA peut être un outil d’action.  
Elle ne doit jamais devenir un dispositif d’effacement de la responsabilité.

Principe :

> **L’IA ne doit pas devenir le masque technique d’un pouvoir humain qui refuse de se nommer.**

---

## 9. Le responsable humain ne doit pas devenir un fusible

Il ne suffit pas de désigner un humain.

Le responsable humain peut devenir un alibi, un signataire de façade, un agent subalterne, un validateur automatique ou un fusible sacrifié après l’incident.

L’imputabilité humaine ne doit donc pas produire un lampiste humain. Elle doit rendre visible la chaîne réelle des pouvoirs, des mandats, des décisions, des bénéfices et des responsabilités.

| Mauvais modèle | Bon modèle |
|---|---|
| responsable nominal | chaîne réelle d’imputabilité |
| signataire de façade | pouvoir effectif de contrôle |
| validation formelle | supervision substantielle |
| humain-alibi | humain capable d’interrompre, corriger, refuser |
| culpabilité individuelle isolée | responsabilité graduée de conception, choix, usage et supervision |

Formule :

> **L’enjeu n’est pas de remplacer l’irresponsabilité artificielle par un lampiste humain. L’enjeu est de rendre visible la chaîne réelle des pouvoirs.**

---

## 10. La protection par le secret aggrave le problème

Cette question rejoint directement la pathologie du secret.

Lorsqu’un système algorithmique est opaque, il devient difficile de savoir :

- qui l’a conçu ;
- qui l’a choisi ;
- qui l’a financé ;
- qui l’a paramétré ;
- qui l’a validé ;
- qui l’utilise ;
- qui le corrige ;
- qui bénéficie de ses biais ;
- qui répond en cas de dommage.

Le secret prétend alors protéger la sécurité.  
Mais il protège aussi l’irresponsabilité.

Le mécanisme est simple :

> Quand personne ne peut voir, personne ne peut prouver.  
> Quand personne ne peut prouver, personne ne peut imputer.  
> Quand personne ne peut imputer, personne ne peut sanctionner.  
> Quand personne ne peut sanctionner, l’abus devient rationnel.

La protection par le secret devient donc pire que le mal lorsqu’elle protège davantage les gardiens du système que le système lui-même.

---

## 11. Le paradoxe du gardien

Ceux qui prétendent garantir la sécurité exigent souvent l’opacité nécessaire à leur propre impunité.

Le raisonnement sécuritaire devient circulaire :

1. Faites-nous confiance, nous protégeons le système.
2. Nous ne pouvons pas expliquer comment, pour des raisons de sécurité.
3. Vous ne pouvez donc pas vérifier.
4. Si vous critiquez, vous fragilisez la sécurité.

Cette structure est incompatible avec une démocratie adulte.

Elle transforme la sécurité en privilège de non-reddition de comptes.

Principe :

> **Celui qui sécurise ne doit pas être le seul à dire si la sécurité est réelle.**

---

## 12. Secret tactique, obscurité structurelle

Il ne s’agit pas de nier toute légitimité au secret.

Certains secrets sont nécessaires :

- clés privées ;
- mots de passe ;
- identités protégées ;
- vulnérabilités temporairement non corrigées ;
- opérations sensibles en cours ;
- éléments relevant de la défense nationale ou du renseignement ;
- informations dont la divulgation immédiate accroîtrait un risque réel.

Mais autre chose est l’obscurité structurelle.

Doivent être vérifiables, au moins par des autorités habilitées :

- les règles du système ;
- les critères de décision ;
- les responsabilités ;
- les mandats ;
- les chaînes de sous-traitance ;
- les audits ;
- les incidents ;
- les corrections ;
- les recours.

Formule :

> **Le secret doit protéger les vulnérabilités temporaires, non les responsabilités permanentes.**

Ou encore :

> **Le secret est acceptable comme clé. Il devient dangereux comme régime.**

---

## 13. Le secret démocratique est un secret contrôlé

La critique de l’obscurité structurelle ne signifie pas transparence totale.

Un secret peut être démocratiquement acceptable s’il est :

1. nécessaire ;
2. proportionné ;
3. limité dans le temps lorsque c’est possible ;
4. contrôlé par un tiers habilité ;
5. réexaminable ;
6. compatible avec un recours ultérieur ;
7. documenté sans exposer ce qui doit rester protégé.

Formule :

> **Un secret démocratique n’est pas un secret sans contrôle ; c’est un secret contrôlé autrement.**

Il ne faut donc pas opposer naïvement secret et transparence. Il faut distinguer :

- ce qui doit être public ;
- ce qui doit être accessible à des auditeurs habilités ;
- ce qui doit être traçable sans être exposé ;
- ce qui doit rester temporairement confidentiel ;
- ce qui ne doit jamais servir à masquer une responsabilité.

---

## 14. De la trace au moyen de preuve

La traçabilité ne consiste pas à accumuler des logs.

Une trace peut être inutile, manipulable, illisible, trop volumineuse, juridiquement inexploitable ou contrôlée par celui qu’elle devrait contrôler.

Il faut donc distinguer la trace technique de la preuve démocratique.

Une trace utile doit tendre à être :

- horodatée ;
- signée ;
- conservée selon une durée déterminée ;
- protégée contre l’effacement opportuniste ;
- vérifiable par des tiers ;
- exploitable par une autorité de contrôle ;
- compatible avec les droits de la défense ;
- proportionnée à la sensibilité de l’acte ;
- minimisée pour ne pas devenir surveillance inutile.

Formule :

> **Une trace qui ne peut pas devenir preuve n’est qu’un bruit administratif.**

Ou encore :

> **La traçabilité démocratique n’est pas l’accumulation de logs ; c’est la production de preuves contrôlables.**

---

## 15. Cybersécurité : l’open source ne suffit pas, la transparence brute non plus

L’argument ne doit pas être naïf. La transparence peut augmenter certains risques si elle est mal conçue.

Les chaînes d’approvisionnement logicielles sont devenues des surfaces d’attaque majeures : dépendances compromises, paquets malveillants, mainteneurs infiltrés, attaques sur les registres, modèles piégés, données d’entraînement empoisonnées, prompt injection, détournement de workflows CI/CD.

L’open source n’est donc pas une garantie suffisante. Un code ouvert peut contenir une faille. Un paquet populaire peut être compromis. Une dépendance transitive peut devenir le point d’entrée d’une attaque. Un modèle public peut être utilisé comme cheval de Troie.

Mais cette objection ne réfute pas la thèse. Elle la précise.

La réponse n’est pas : tout publier sans contrôle.

La réponse est :

- publication des règles quand c’est possible ;
- audit habilité quand la publication brute serait dangereuse ;
- journaux signés et append-only pour les actes sensibles ;
- attestations de versions ;
- suivi des dépendances ;
- reproductibilité des builds quand elle est possible ;
- contrôle des accès administrateurs ;
- gestion stricte des secrets ;
- preuves cryptographiques ou quasi-cryptographiques lorsque l’exposition des données serait illégitime.

Formule :

> **L’open source n’est pas une garantie suffisante, mais l’invérifiabilité est une faiblesse structurelle.**

La doctrine défendue ici n’est donc pas “tout ouvrir”. Elle est :

> **rendre contrôlable ce qui engage autrui, par le bon niveau de publicité, d’audit, de preuve et de responsabilité.**

---

## 16. Vie privée, vie publique : ne pas confondre protection et impunité

La critique du secret ne signifie pas transparence générale des personnes.

La vie privée doit être protégée.  
La vie publique doit être contrôlable.  
Les actes de pouvoir doivent être traçables.  
Les atteintes doivent être sanctionnables.

Ni la vie privée ni la vie publique ne sont robustes par nature.

La vie privée peut être violée.  
La vie publique peut être capturée.  
Le commun peut être pillé.  
Le public peut être privatisé.  
Les responsabilités peuvent être effacées.

La robustesse vient donc d’une architecture :

- règles claires ;
- traces qualifiées ;
- mandats explicites ;
- recours effectifs ;
- sanctions réelles ;
- réparations possibles ;
- apprentissage collectif après incident.

Formule :

> **La robustesse démocratique ne consiste pas à rendre tout visible. Elle consiste à rendre toute atteinte aux frontières légitimes détectable, prouvable et punissable.**

---

## 17. Surveiller les puissants, pas les faibles

L’enjeu n’est pas de produire une société de surveillance généralisée.

L’enjeu est inverse :

> **empêcher que les puissants se cachent derrière les systèmes qu’ils imposent aux faibles.**

Une démocratie numérique ne doit pas produire un crédit social des citoyens.  
Elle doit produire une traçabilité des actes de pouvoir.

Ce qu’il faut éviter :

> citoyens visibles, pouvoirs opaques.

Ce qu’il faut construire :

> citoyens protégés, pouvoirs contrôlables.

Formule politique :

> **Surveiller les puissants, pas les faibles.**

Ou plus précisément :

> **Protéger l’intimité des personnes ; rendre contrôlables les actes qui engagent autrui.**

---

## 18. IA, agents et mandats

Plus les agents numériques deviennent autonomes, plus les mandats doivent devenir traçables.

Pour tout agent algorithmique utilisé dans un contexte public ou commun, il faut pouvoir répondre à des questions simples :

- Qui a autorisé l’action ?
- Au nom de qui ?
- Sur quel fondement ?
- Avec quelles données ?
- Selon quelles règles ?
- Avec quels effets ?
- Sous quelle responsabilité ?
- Avec quel recours ?
- Avec quelle trace ?

Un mandat est l’autorisation explicite donnée à un acteur, humain ou institutionnel, d’agir au nom d’autrui, dans un périmètre déterminé, avec des limites, des traces, des conditions de contrôle et des conditions de révocation.

Un agent IA ne doit jamais effacer le mandat. Il doit au contraire le rendre plus explicite.

L’IA peut calculer.  
L’IA peut recommander.  
L’IA peut générer.  
L’IA peut simuler.

Mais l’acte qui engage autrui doit rester imputable.

Principe :

> **Plus l’action est automatisée, plus la responsabilité humaine doit être explicite.**

---

## 19. Responsabilité graduée : éviter la paralysie

Une objection sérieuse doit être traitée : si tout devient imputable, plus personne n’osera agir.

La réponse n’est pas de produire une responsabilité illimitée. C’est de construire une responsabilité graduée.

Il faut distinguer :

- responsabilité de conception ;
- responsabilité de choix ;
- responsabilité de financement ;
- responsabilité de paramétrage ;
- responsabilité d’usage ;
- responsabilité de supervision ;
- responsabilité de correction ;
- responsabilité de dissimulation ;
- responsabilité de non-retrait après alerte.

L’objectif n’est pas de punir l’erreur honnête. L’objectif est de rendre impossible l’irresponsabilité organisée.

Formule :

> **La responsabilité démocratique ne doit pas paralyser l’action publique ; elle doit empêcher que l’action publique devienne inexplicable.**

---

## 20. La souveraineté numérique comme capacité de vérification

La souveraineté numérique ne peut pas se réduire à la localisation des serveurs ou à la nationalité des prestataires.

Une donnée hébergée localement peut être mal protégée.  
Une administration publique peut être opaque.  
Un prestataire national peut être négligent.  
Une infrastructure “chez nous” peut rester invérifiable pour ceux qu’elle engage.

La souveraineté numérique doit être définie comme capacité collective de vérification :

- savoir qui agit ;
- selon quelles règles ;
- au bénéfice de qui ;
- avec quels risques ;
- avec quels recours ;
- sous quelle responsabilité.

Formule :

> **La souveraineté numérique n’est pas seulement le contrôle des machines. C’est le contrôle démocratique des actes accomplis par les machines et par ceux qui les administrent.**

---

## 21. Doctrine démocratique de la robustesse numérique

Une infrastructure démocratique robuste ne promet pas qu’aucune brèche ne surviendra.

Cette promesse serait fausse.

Elle promet autre chose :

> que les atteintes pourront être détectées, qualifiées, imputées, contestées, réparées et sanctionnées.

Cette doctrine repose sur huit principes.

| Principe | Exigence |
|---|---|
| **Auditabilité** | Les systèmes critiques doivent pouvoir être vérifiés par des tiers qualifiés. |
| **Traçabilité qualifiée** | Les actes sensibles doivent laisser des traces exploitables et proportionnées. |
| **Minimisation** | Ce qui n’a pas besoin d’être collecté ne doit pas l’être. |
| **Compartimentation** | Une brèche ne doit pas devenir immédiatement systémique. |
| **Imputabilité** | Chaque acte significatif doit être rattaché à une responsabilité identifiable. |
| **Recours** | Les personnes affectées doivent pouvoir contester et obtenir réparation. |
| **Secret limité** | Le secret doit être justifié, proportionné, contrôlé et réexaminable. |
| **Publicité des mandats** | Les actes accomplis au nom d’autrui doivent être encadrés par des mandats explicites. |

---

## 22. Passage au crible de la seconde méthode

Cette section applique au présent texte les principes de la seconde méthode : publier le processus, rendre les objections productives, distinguer faits, hypothèses et décisions, et ouvrir les continuations possibles.

### 22.1 Thèse centrale à tester

> Une infrastructure numérique démocratique est plus robuste lorsqu’elle repose sur l’imputabilité humaine, la traçabilité qualifiée et le secret contrôlé que lorsqu’elle repose sur l’obscurité structurelle.

### 22.2 Claims vérifiables

| Claim | Vérification possible |
|---|---|
| Les offices et juridictions refusent l’IA comme inventeur ou auteur autonome. | Vérifier DABUS, USPTO, OEB, UK Supreme Court, Thaler v. Perlmutter. |
| Le droit français impose déjà certaines obligations relatives aux algorithmes publics. | Vérifier CRPA L311-3-1, L312-1-3, avis CADA, rapports Défenseure des droits. |
| L’AI Act impose journalisation et supervision humaine pour les systèmes à haut risque. | Vérifier articles 12 et 14 du règlement européen. |
| DataJust touche un domaine institutionnel sensible. | Vérifier décret 2020-356, page justice.fr, décision CE 440376. |
| Les logs ordinaires ne suffisent pas toujours à produire une preuve démocratique. | Tester des systèmes réels : logs modifiables, inexploitables, incomplets, non horodatés ou non corrélés. |

### 22.3 Objections de premier rang

**Objection 1 — Le droit positif existe déjà.**  
Réponse : oui. Le texte ne prétend pas inventer l’exigence. Il cherche à transformer des obligations partielles en doctrine générale d’imputabilité démocratique.

**Objection 2 — La transparence augmente la surface d’attaque.**  
Réponse : parfois. C’est pourquoi le texte ne défend pas la transparence brute, mais une combinaison de publicité, secret contrôlé, audit habilité, traçabilité probatoire et minimisation.

**Objection 3 — La responsabilité humaine peut devenir un lampiste.**  
Réponse : c’est un risque central. La bonne exigence porte sur la chaîne réelle d’imputabilité, non sur un responsable nominal.

**Objection 4 — La doctrine peut paralyser l’action publique.**  
Réponse : la responsabilité doit être graduée. L’objectif n’est pas de punir l’erreur honnête, mais d’empêcher l’irresponsabilité organisée.

**Objection 5 — L’analogie brevets / œuvres ne vaut pas pour le droit public.**  
Réponse : ce n’est pas une déduction juridique mécanique. C’est une analogie institutionnelle qui révèle une exigence commune : pas d’effet opposable sans sujet capable de répondre.

### 22.4 Conditions de révision

Le texte devra être révisé si :

- une jurisprudence reconnaît explicitement une IA comme auteur ou inventeur autonome ;
- des dispositifs publics démontrent une robustesse supérieure sans traçabilité ni imputabilité ;
- la traçabilité qualifiée produit empiriquement plus de dommages démocratiques que l’obscurité qu’elle remplace ;
- le coût administratif rend la doctrine impraticable même dans des systèmes à haut risque ;
- les mécanismes de secret contrôlé se révèlent systématiquement capturés par ceux qu’ils doivent contrôler.

### 22.5 Tests empiriques possibles

- comparer des administrations publiant leurs algorithmes et celles qui ne les publient pas ;
- mesurer la correction des erreurs après réclamation selon le degré de traçabilité ;
- analyser les délais d’imputation après incident ;
- tester la lisibilité des explications algorithmiques par des juristes, usagers, journalistes et associations ;
- étudier DataJust comme cas de normalisation algorithmique judiciaire, même en l’absence de décision automatisée directe.

---

## 23. Autres possibles à explorer

### 23.1 Registre public des systèmes algorithmiques

Créer un registre public des systèmes algorithmiques utilisés par les administrations et acteurs gérant des communs critiques, avec niveau de publicité variable selon les risques.

### 23.2 Transparence différée

Certains éléments pourraient rester confidentiels pendant une durée définie, puis devenir accessibles après disparition du risque opérationnel.

### 23.3 Preuves cryptographiques sans exposition des données

Explorer les preuves à divulgation nulle de connaissance, journaux append-only, signatures, horodatages, attestations de version et preuves de conformité sans exposition des données privées.

### 23.4 Fiducie ou fondation du commun numérique

Imaginer des institutions gardiennes des traces : indépendantes, mandatées, auditables, capables de conserver des preuves sans les exposer publiquement.

### 23.5 Mandats numériques révocables

Développer des mandats explicites, signés, limités et révocables pour tout agent ou système agissant au nom d’une personne, d’une collectivité ou d’un commun.

### 23.6 DataJust comme étude de cas approfondie

Produire une note séparée :

```text
research/datajust_et_imputabilite_judiciaire.md
```

Objectif : analyser DataJust comme cas limite entre information des parties, référentiel indicatif, aide à la décision et normalisation algorithmique de la justice.

---

## 24. Conclusion : pas de responsable artificiel pour le commun

Les jurisprudences récentes sur l’IA, les brevets et les œuvres enseignent une chose essentielle : une machine peut produire, mais elle ne peut pas répondre.

Elle ne peut donc pas être le sujet ultime d’un droit, d’un acte ou d’une responsabilité.

Ce que le juge refuse pour la propriété intellectuelle privée doit être refusé plus encore pour les infrastructures publiques et les communs.

Formule finale :

> **Pas d’auteur artificiel pour les œuvres.  
> Pas d’inventeur artificiel pour les brevets.  
> Pas de responsable artificiel pour le commun.  
> Pas de lampiste humain pour les puissants.**

Ou, plus politique :

> **On ne peut pas exiger un humain pour posséder, puis accepter une machine pour gouverner.**

La protection par le secret peut être nécessaire comme exception tactique.  
Elle devient dangereuse comme régime.

La robustesse démocratique ne réside pas dans la promesse fausse qu’aucune atteinte ne surviendra. Elle réside dans la capacité institutionnelle de voir, prouver, imputer, contester, corriger, réparer et sanctionner.

---

## 25. Continuation auto-descriptive

```markdown
# CONTINUATION PACKET — pathologie_du_secret v0.4 → v0.5

## Protocol Header
This block is a cognitive packet: a structured unit of cognitive work intended to let a human, AI agent, tool, or repository resume work.

It is not an ordinary summary. It distinguishes established state, decisions, assumptions, constraints, next action, traces, and resumption risks.

Two transmission modes exist:
- by copy: the necessary context is embedded;
- by reference: the packet points to a shared, stable, accessible context.

After using this packet, the receiver may produce a new continuation packet according to the same convention.

Self-describing does not mean self-validating. The receiver must still verify the packet's claims, references, assumptions, and decisions.

## Object
Faire passer `pathologie_du_secret.md` de v0.4 à v0.5, en renforçant l’étude de cas DataJust et en préparant les fichiers compagnons.

## State
La v0.4 intègre DataJust comme cas principal, ajoute un ancrage dans le droit positif français et européen, traite les risques supply-chain/open source, distingue secret contrôlé et obscurité structurelle, et applique la seconde méthode.

## Decisions
- Conserver le français comme langue principale.
- Garder l’abstract anglais.
- Conserver la thèse : humain pour posséder, humain pour gouverner.
- Présenter l’argument brevets/œuvres comme analogie institutionnelle, non déduction juridique mécanique.
- Garder DataJust comme cas principal, sous réserve de vérification juridique approfondie.

## Constraints
- Ne pas affirmer que DataJust était illégal si la source ne le démontre pas.
- Ne pas transformer l’article en pamphlet anti-administration.
- Ne pas défendre la transparence brute.
- Préserver la distinction entre secret tactique légitime et obscurité structurelle.
- Éviter que le responsable humain devienne un simple fusible.

## Assumptions
- DataJust est le cas français le plus sensible parce qu’il touche à la justice et aux préjudices corporels.
- Le droit positif existant est insuffisant non par absence totale de règles, mais par dispersion, application imparfaite et défaut de doctrine générale.
- La traçabilité probatoire peut être conçue sans sacrifier la vie privée si elle est proportionnée, contrôlée et minimisée.

## Next Action
Créer trois fichiers compagnons :
1. `claims_pathologie_du_secret.md`
2. `objections_pathologie_du_secret.md`
3. `datajust_et_imputabilite_judiciaire.md`

## Traces
- `pathologie_du_secret.md` v0.4
- Décret n° 2020-356 du 27 mars 2020 relatif à DataJust
- Décision Conseil d’État n° 440376 du 30 décembre 2021
- Page Justice.fr DataJust
- CRPA L311-3-1 et L312-1-3
- AI Act, articles 12 et 14
- Rapport Défenseure des droits 2024 sur algorithmes, IA et services publics
- `cogentia/research/cognitive_packets.md`
- `barons-Mariani/second_method.md`

## Resumption Risks
- Surjouer DataJust comme scandale alors que l’intérêt est institutionnel, non accusatoire.
- Confondre légalité d’un décret et suffisance démocratique du dispositif.
- Confondre logs techniques et preuve démocratique.
- Sous-estimer la cybersécurité réelle des chaînes d’approvisionnement.
```

---

## Références initiales

### IA, brevets, œuvres

- European Patent Office, décisions DABUS J 8/20 et J 9/20 : une machine n’est pas inventeur au sens de la Convention sur le brevet européen.  
  https://www.epo.org/en/boards-of-appeal/decisions/j200008eu1

- UK Supreme Court, *Thaler v Comptroller-General of Patents, Designs and Trade Marks*, 20 décembre 2023 : DABUS ne peut pas être désigné inventeur.  
  https://supremecourt.uk/cases/uksc-2021-0201

- USPTO, *Inventorship Guidance for AI-Assisted Inventions*, 2024/2025.  
  https://www.uspto.gov/subscription-center/2025/revised-inventorship-guidance-ai-assisted-inventions

- U.S. Copyright Office, *Copyright and Artificial Intelligence, Part 2: Copyrightability*, 2025.  
  https://www.copyright.gov/newsnet/2025/1060.html

- D.C. Circuit, *Thaler v. Perlmutter*, 18 mars 2025.  
  https://law.justia.com/cases/federal/appellate-courts/cadc/23-5233/23-5233-2025-03-18.html

### DataJust et droit français

- Décret n° 2020-356 du 27 mars 2020 portant création du traitement automatisé de données à caractère personnel dénommé DataJust.  
  https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000041763205

- Justice.fr, page DataJust.  
  https://www.justice.fr/donnees-personnelles/datajust

- Conseil d’État, décision n° 440376 et requêtes jointes, 30 décembre 2021.  
  https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2021-12-30/440376

- CNIL, délibération n° 2020-002 du 9 janvier 2020 portant avis sur DataJust.  
  https://www.cnil.fr/fr/deliberations

- Code des relations entre le public et l’administration, article L312-1-3.  
  https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033205516

### IA publique et supervision

- Règlement européen sur l’intelligence artificielle, Regulation (EU) 2024/1689, notamment articles 12 et 14.  
  https://eur-lex.europa.eu/eli/reg/2024/1689/oj

- Défenseure des droits, rapport 2024 sur algorithmes, intelligence artificielle et services publics.  
  https://www.defenseurdesdroits.fr/algorithmes-intelligence-artificielle-et-services-publics-2024

### Sécurité, secret, transparence

- Auguste Kerckhoffs, principe de Kerckhoffs : un système cryptographique doit rester sûr même si tout est public sauf la clé.
- Claude Shannon, maxime associée : l’ennemi connaît le système.
- Lawrence Lessig, *Code and Other Laws of Cyberspace* : le code informatique régule les comportements et porte donc une dimension politique.
- David Brin, *The Transparent Society* : nécessité de contrôler ceux qui surveillent.
- Bruce Schneier : critique de la sécurité par l’obscurité et défense d’une sécurité vérifiable.
- Michel Foucault, *Surveiller et punir* : visibilité asymétrique et pouvoir disciplinaire.
- Steve Mann : sousveillance comme capacité de documenter les abus du pouvoir depuis le bas.

### Chaîne d’approvisionnement logicielle

- ReversingLabs, *2026 Software Supply Chain Security Report*, signalant une forte hausse des paquets open source malveillants en 2025.  
  https://www.reversinglabs.com/press-releases/reversinglabs-2026-software-supply-chain-security-report-identifies-73-increase-in-malicious-open-source-packages

---

## Formules à isoler

> **On ne peut pas exiger un humain pour posséder, puis accepter une machine pour gouverner.**

> **Humain exigé pour la propriété. Humain exigé pour la responsabilité.**

> **Pas d’auteur artificiel pour les œuvres. Pas d’inventeur artificiel pour les brevets. Pas de responsable artificiel pour le commun.**

> **Pas d’outil judiciaire sans chaîne humaine d’imputabilité.**

> **L’IA ne doit pas devenir le masque technique d’un pouvoir humain qui refuse de se nommer.**

> **Le secret est acceptable comme clé. Il devient dangereux comme régime.**

> **Le secret doit protéger les vulnérabilités temporaires, non les responsabilités permanentes.**

> **Une trace qui ne peut pas devenir preuve n’est qu’un bruit administratif.**

> **La protection par le secret peut être une sécurité opérationnelle. L’obscurité structurelle est une irresponsabilité politique.**


<!-- BEGIN_AUTO: backlinks -->
### Backlinks

*These documents link to this file:*
- [Corpus Status — barons-Mariani](corpus-status.md)
- [Research Index — barons-Mariani](index.md)
- [Democratic AI Safety](democratic_ai_safety.md)

<!-- END_AUTO: backlinks -->
