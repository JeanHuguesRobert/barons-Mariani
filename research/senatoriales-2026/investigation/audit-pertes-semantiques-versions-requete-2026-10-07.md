---
title: "Audit des pertes sémantiques entre versions de la requête"
author: "Jean Hugues Noël Robert"
date: "2026-10-07"
version: "0.1"
status: "active — semantic regression audit"
language: fr
document_role: "quality-control"
document_kind: "semantic-diff-audit"
visibility: public
related:
  - "../requete-conseil-constitutionnel.md"
  - "../requete-conseil-constitutionnel-projet-v0.20.md"
  - "../requete-conseil-constitutionnel-projet-v0.23.md"
  - "../requete-conseil-constitutionnel-projet-v0.26.md"
  - "../requete-conseil-constitutionnel-projet-v0.27.md"
---

# Audit des pertes sémantiques entre versions de la requête

## Principe

Les passes demandées par l'auteur visaient l'**intelligibilité sans réduction sémantique**.

Une réécriture plus courte ou plus fluide n'est donc acceptable que si toutes les propositions utiles, distinctions, réserves, conséquences et fonctions argumentatives restent présentes.

Le présent audit compare notamment les versions 0.20, 0.23, 0.26, 0.27 et la requête stable.

## Ce qui pouvait légitimement sortir du corps

Les éléments suivants relèvent du processus de fabrication et non de la substance juridictionnelle :

- changelogs de versions ;
- protocoles internes de revue adverse ;
- listes de contrôle de production ;
- intitulés « Grand public / Expert » lorsque leur contenu est fusionné sans perte ;
- vocabulaire interne de type « probe », « Cognitive Packet », passes de production ;
- numéros de versions internes ;
- tables ou schémas lorsqu'ils sont remplacés par une prose portant exactement le même sens ;
- nom interne « Principe de Talleyrand », à condition que sa règle utile — expliciter toute prémisse nécessaire — soit conservée dans le control plane et appliquée au texte.

Le retrait de ces éléments n'est pas une perte sémantique de la requête si leur contenu juridique utile reste présent.

## Pertes ou affaiblissements identifiés

### 1. Fonction de la demande subsidiaire de proclamation directe

Affaiblie lors de la passe d'intelligibilité v0.27.

La conclusion avait une fonction distincte de sa probabilité de succès : utiliser l'article 41 comme expérience de pensée pour distinguer :
- existence abstraite d'un pouvoir correctif ;
- applicabilité de ce pouvoir au cas concret ;
- impossibilité d'un remède particulier ;
- absence de tout remède.

**Statut : restauré dans la requête stable.**

### 2. Caractère général des QPC

Les développements récents avaient tendance à rattacher excessivement :
- L.299 à la seule situation de Mme Vernerey ;
- L.303 à la seule candidature Robert–Vernerey et à l'élection de M. Parigi.

Une QPC part d'un litige concret mais porte sur une disposition législative générale.

**Statut : restauré dans la requête stable et dans les deux notes QPC.**

### 3. Sens de la phrase d'ouverture

La v0.26 explicitait trois propositions :
- la formule « le mépris appelle le mépris » ne vise aucune personne ;
- elle exprime une réciprocité institutionnelle ;
- l'institution qui demande le respect de ses règles doit aussi manifester ce respect dans ses actes.

La v0.27 n'avait conservé que la dernière idée sous une forme abrégée.

**Statut : restauré dans la requête stable.**

### 4. Droit d'éligibilité, liberté de l'électeur et pluralisme

La v0.20 conservait explicitement, dans sa couverture doctrinale et sa check-list, les axes :
- droit d'éligibilité ;
- égalité devant le suffrage ;
- liberté de l'électeur ;
- pluralisme des courants d'idées et d'opinions.

Le passage vers les versions plus courtes a fait disparaître le terme « pluralisme » et a rendu le droit d'éligibilité moins explicite dans le corps.

Sources de contrôle :
- article 6 de la Déclaration de 1789 et jurisprudence constitutionnelle sur le droit d'éligibilité ;
- article 4 de la Constitution et jurisprudence constitutionnelle sur le pluralisme.

**Statut : restauré dans la section QPC de la requête stable.**

### 5. Symétrie des conséquences et des voies ultérieures

Les versions anciennes explicitaient davantage que la fermeture du recours interne après décision du Conseil vaut pour toute personne affectée par sa décision, notamment le requérant et le sénateur proclamé élu.

Cette symétrie avait été fortement comprimée mais non totalement supprimée.

**Statut : conservé dans la requête stable ; renforcé dans l'expérience de pensée sur l'article 41.**

## Sens contrôlé comme toujours présent

L'audit confirme que les éléments suivants ont survécu aux passes de réécriture :

- droit conventionnel de se porter candidat au titre de l'article 3 du Protocole n° 1 ;
- libre expression du choix du corps électoral ;
- distinction L.298 / L.299 ;
- consentement éclairé et demande faite au tiers ;
- contre-exemple du mandataire financier : demande précise, régularisation rapide, vérification ;
- absence de refus du candidat de se soumettre au contrôle ou de régulariser ;
- hypothèse de propagation d'une prémisse « originaux papier » de la préfecture vers le contrôle juridictionnel ;
- distinction entre deux conclusions concordantes et deux contrôles réellement indépendants ;
- traçabilité des transmissions et des actes ;
- incidence possible de l'offre électorale absente ;
- participation obligatoire des grands électeurs ;
- différence entre soutien public visible et vote secret ;
- distinction entre annulation, élection partielle et réformation de la proclamation ;
- préparation explicite d'une éventuelle saisine CEDH.

## Règle pour toute réécriture future

Avant de remplacer une version de lecture par une nouvelle :

1. établir la liste des propositions, distinctions, réserves, conséquences et demandes de la version source ;
2. vérifier que chacune possède un équivalent dans la version cible ;
3. si un élément est retiré parce qu'il relève du processus de fabrication, vérifier que son contenu juridique utile existe ailleurs ;
4. signaler explicitement toute suppression volontaire de sens à l'auteur avant de l'effectuer ;
5. en l'absence d'autorisation explicite, **une passe d'intelligibilité est tenue d'être sémantiquement conservative**.

Test canonique :

> **Plus clair ne signifie jamais moins complet.**
