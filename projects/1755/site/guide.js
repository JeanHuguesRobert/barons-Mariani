// Guide et Collecte interactive 1755 - Zéro rétention de données, côté client pur
document.addEventListener("DOMContentLoaded", () => {
  // 1. Guide Conversationnel Borné
  const guideForm = document.getElementById("guide-form");
  const guideInput = document.getElementById("guide-prompt");
  const guideResponse = document.getElementById("guide-response");

  if (guideForm && guideInput && guideResponse) {
    const knowledgeBase = [
      {
        keywords: ["femme", "femmes", "vote", "suffrage", "veuve"],
        response: "**Suffrage des femmes en 1755 :** Le texte de la Constitution mentionne l'élection par les « padri di famiglia » (chefs de famille). Les archives dépouillées par Dorothy Carrington et les récits de James Boswell attestent que les veuves et femmes cheffes de foyer votaient de plein droit dans les assemblées de pieve pour désigner les magistrats et députés. Il s'agissait d'un vote patrimonial lié à la responsabilité du foyer dans la *Terra di Comune*, non du suffrage individuel universel moderne."
      },
      {
        keywords: ["nobles douze", "dodici", "statuts", "1571", "gênes", "génois"],
        response: "**Les Nobles Douze (Nobili Dodici) :** Institués par les Statuts de 1571 pour représenter la Terra di Comune auprès du Gouverneur de Gênes à Bastia, ils ont subi une capture oligarchique progressive (Ostrom Mode 7). Lors de la crise fiscale du quattrino en 1729, leur refus de défendre les paysans a provoqué leur contournement direct et la réactivation des Cunsulte populaires, menant au pacte constituant de 1755."
      },
      {
        keywords: ["corte", "consulte", "dieta", "diète", "novembre"],
        response: "**La Consulte de Corte (16–18 novembre 1755) :** Assemblée générale constituante réunie au couvent Saint-François de Corte sous la présidence de Pascal Paoli. Elle proclame la souveraineté du peuple, vote la Constitution écrite de la République corse et institue la Diète générale annuelle comme organe législatif suprême."
      },
      {
        keywords: ["sindacato", "syndicat", "contrôle", "contre-pouvoir", "abus"],
        response: "**Le Sindacato (Chambre des Syndics) :** Tribunal suprême de contrôle indépendant du Général et du Conseil d'État. Tout citoyen pouvait y dénoncer les abus de pouvoir ou concussions de tout magistrat. C'est l'un des premiers tribunaux constitutionnels et de surveillance civique de l'histoire moderne."
      },
      {
        keywords: ["boswell", "ecosse", "livre", "1768"],
        response: "**James Boswell :** Écrivain écossais qui visite la Corse en 1765 avec une lettre d'introduction de Rousseau. Son ouvrage *An Account of Corsica* (1768), traduit dans toute l'Europe, fait de Pascal Paoli une figure mythique de la liberté et suscite l'enthousiasme des révolutionnaires américains."
      },
      {
        keywords: ["rousseau", "contrat social", "projet", "lumières"],
        response: "**Jean-Jacques Rousseau :** Écrit en 1762 dans *Du Contrat Social* que la Corse est le seul pays d'Europe capable de législation. Invité par Paoli et Buttafoco en 1764, il rédige son *Projet de constitution pour la Corse* en 1765, consacrant l'île comme laboratoire politique des Lumières."
      },
      {
        keywords: ["amérique", "états-unis", "sons of liberty", "paoli", "pennsylvanie"],
        response: "**L'écho américain :** Les *Sons of Liberty* portaient des toasts à Pascal Paoli dans les années 1760. Quatre localités portent son nom aux États-Unis (dont Paoli, PA, théâtre de la bataille de 1777). La réception américaine de Paoli est documentée, mais une influence directe de la Constitution de 1755 sur les textes constitutionnels américains n'est pas établie par cette seule réception."
      },
      {
        keywords: ["manuscrit", "archives", "cote", "unesco", "original"],
        response: "**Le Manuscrit original de 1755 (Act #1755-01) :** Un catalogue patrimonial attribue la cote 1 J 7/1 à une Constitution adoptée le 18 novembre 1755, aux Archives de Corse–Pumonti. La cote actuelle, la matérialité de la pièce et sa concordance avec le manuscrit décrit par Dorothy Carrington restent à confirmer directement auprès du service détenteur. Aucune copie précise à Gênes n'est établie. Une éventuelle démarche UNESCO demeure exploratoire et conditionnelle."
      }
    ];

    guideForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const query = guideInput.value.trim().toLowerCase();
      if (!query) return;

      guideResponse.innerHTML = "<p><em>Interrogation du corpus probatoire 1755 en cours...</em></p>";

      setTimeout(() => {
        let found = null;
        for (const item of knowledgeBase) {
          if (item.keywords.some((kw) => query.includes(kw))) {
            found = item;
            break;
          }
        }

        if (found) {
          guideResponse.innerHTML = `
            <div class="call">
              <p><strong>Réponse bornée au corpus :</strong></p>
              <p>${found.response}</p>
              <p class="muted" style="margin-top: 0.5rem; font-size: 0.85rem;">Source : Corpus 1755 (Level A/B). Aucun historique de question n'est conservé.</p>
            </div>
          `;
        } else {
          guideResponse.innerHTML = `
            <div class="warn">
              <p><strong>Hors périmètre ou question non résolue dans le corpus :</strong></p>
              <p>La question posée n'a pas trouvé de correspondance directe dans les dossiers probatoires actuels de 1755. Le Guide public applique le principe d'abstention stricte pour éviter toute hallucination historiographique.</p>
              <p>Vous pouvez consulter les chapitres du <a href="manuscrit.html">Manuscrit</a>, les <a href="annexes.html">Annexes</a> ou proposer un amendement via la page <a href="contribuer.html">Contribuer</a>.</p>
            </div>
          `;
        }
      }, 250);
    });
  }

  // 2. Générateur de Contribution & Objection (Collecte engageante)
  const contribForm = document.getElementById("contrib-form");
  const contribOutput = document.getElementById("contrib-output");

  if (contribForm && contribOutput) {
    contribForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const type = document.getElementById("contrib-type").value;
      const ref = document.getElementById("contrib-ref").value.trim();
      const text = document.getElementById("contrib-text").value.trim();
      const author = document.getElementById("contrib-author").value.trim() || "Chercheur / Citoyen anonyme";

      if (!text) return;

      const dateStr = new Date().toISOString().split("T")[0];
      const markdown = `---
type: contribution-1755
categorie: ${type}
reference_cible: "${ref}"
auteur: "${author}"
date: "${dateStr}"
---

### Objet de la contribution
${text}

---
*Généré localement via 1755.acorsica.org — Copiez ce bloc et collez-le dans une issue GitHub ou transmettez-le au comité scientifique.*`;

      contribOutput.value = markdown;
      document.getElementById("contrib-result-box").style.display = "block";
    });
  }
});
