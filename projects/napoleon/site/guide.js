(function () {
  var STORAGE_KEY = "napoleon-guide-conversation";
  var GUIDE_BASE = document.body.getAttribute("data-guide-base") || "https://cogentia.fractavolta.com";
  var GUIDE_PROFILE = document.body.getAttribute("data-guide-profile") || "napoleon";

  var log = document.getElementById("log");
  var form = document.getElementById("ask");
  var questionInput = document.getElementById("question");
  var draftTo = document.getElementById("draft-to");
  var draftSubject = document.getElementById("draft-subject");
  var draftBody = document.getElementById("draft-body");
  var draftStatus = document.getElementById("draft-status");
  var clearBtn = document.getElementById("clear-log");
  var sampleBtns = document.querySelectorAll("[data-sample]");

  var turns = loadTurns();
  render();

  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var text = questionInput ? questionInput.value : "";
      ask(text);
    });
  }

  if (clearBtn) {
    clearBtn.addEventListener("click", function () {
      turns = [];
      saveTurns();
      render();
      if (draftStatus) draftStatus.textContent = "Historique local effacé.";
    });
  }

  sampleBtns.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var sample = btn.getAttribute("data-sample");
      if (questionInput) {
        questionInput.value = sample;
        ask(sample);
      }
    });
  });

  var btnObjection = document.getElementById("prepare-objection");
  if (btnObjection) {
    btnObjection.addEventListener("click", function () {
      prepareDraft("objection");
    });
  }

  var btnSource = document.getElementById("prepare-source");
  if (btnSource) {
    btnSource.addEventListener("click", function () {
      prepareDraft("source");
    });
  }

  var btnCopy = document.getElementById("copy-draft");
  if (btnCopy) {
    btnCopy.addEventListener("click", copyDraft);
  }

  function loadTurns() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      return raw ? JSON.parse(raw) : [];
    } catch (e) {
      return [];
    }
  }

  function saveTurns() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(turns));
    } catch (e) {}
  }

  function render() {
    if (!log) return;
    log.innerHTML = "";
    if (turns.length === 0) {
      var welcome = document.createElement("div");
      welcome.className = "chat-msg chat-assistant";
      welcome.innerHTML = "<div class=\"chat-role\">Guide Public — Napoléon</div>" +
        "<p>Bienvenue. Je suis le Guide conversationnel borné du Livre Vivant Napoléon. " +
        "Conformément à mes 8 invariants doctrinaux, je ne parle pas à la première personne comme Napoléon, " +
        "je n'invente aucune citation et j'ancre systématiquement mes analyses sur les sources d'archives et le registre des 10 campagnes. " +
        "Posez une question sur un fait, une controverse ou une hypothèse stratégique du Twin.</p>";
      log.appendChild(welcome);
      return;
    }

    turns.forEach(function (t) {
      var box = document.createElement("div");
      box.className = "chat-msg " + (t.role === "user" ? "chat-user" : "chat-assistant");
      var roleLabel = t.role === "user" ? "Visiteur" : "Guide Napoléon (Profil borné)";
      box.innerHTML = "<div class=\"chat-role\">" + roleLabel + "</div><div>" + formatMarkdown(t.content) + "</div>";
      log.appendChild(box);
    });
  }

  function formatMarkdown(text) {
    if (!text) return "";
    var escaped = text
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
    
    // Bold
    escaped = escaped.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
    // Italic
    escaped = escaped.replace(/\*(.*?)\*/g, "<em>$1</em>");
    // Line breaks
    escaped = escaped.replace(/\n\n/g, "</p><p>");
    escaped = escaped.replace(/\n/g, "<br>");
    return "<p>" + escaped + "</p>";
  }

  function ask(text) {
    var clean = String(text || "").trim();
    if (!clean) return;
    turns.push({ role: "user", content: clean });
    saveTurns();
    render();
    if (questionInput) questionInput.value = "";
    if (draftStatus) draftStatus.textContent = "Consultation du corpus en cours (sans rétention serveur)...";

    // Try remote guide endpoint first
    postJson(GUIDE_BASE + "/guide/chat", {
      profile: GUIDE_PROFILE,
      locale: "fr",
      question: clean,
      history: turns.slice(0, -1)
    }).then(function (body) {
      var ans = body && body.answer ? String(body.answer) : null;
      if (!ans) throw new Error("Empty response");
      turns.push({ role: "assistant", content: ans });
      saveTurns();
      render();
      if (draftStatus) draftStatus.textContent = "Réponse formulée selon les invariants du profil napoleon.";
    }).catch(function () {
      // Local invariant-respecting inference engine
      var localAnswer = generateLocalAnswer(clean);
      turns.push({ role: "assistant", content: localAnswer });
      saveTurns();
      render();
      if (draftStatus) draftStatus.textContent = "Réponse générée localement à partir du registre des campagnes et des invariants.";
    });
  }

  function generateLocalAnswer(q) {
    var lower = q.toLowerCase();

    // 1. Lignes intérieures / Italie
    if (lower.indexOf("lignes intérieures") !== -1 || lower.indexOf("italie") !== -1 || lower.indexOf("1796") !== -1) {
      return "**Plan A (Histoire) :** Durant la Première campagne d'Italie (1796-1797), l'Armée d'Italie commandée par Bonaparte s'interpose entre l'armée piémontaise de Colli et l'armée autrichienne de Beaulieu.\n\n" +
        "**Plan C (Hypothèse du Twin) :** Le modèle stratégique infère que Napoléon transforme une infériorité numérique globale en supériorité locale en battant successivement les composantes d'une coalition sur leur ligne de suture.\n\n" +
        "**Contre-exemple & Limite :** Cette doctrine cinétique repose sur une surexploitation des ressources locales, provoquant les insurrections paysannes de Pavie et Vérone en 1796. *Sources : Correspondance générale Fayard t. 1 ; Carl von Clausewitz, La Campagne d'Italie de 1796.*";
    }

    // 2. Russie / Logistique / 1812
    if (lower.indexOf("russie") !== -1 || lower.indexOf("1812") !== -1 || lower.indexOf("logistique") !== -1 || lower.indexOf("moscou") !== -1) {
      return "**Plan A (Histoire) :** La Grande Armée de 600 000 hommes franchit le Niémen en juin 1812. Malgré l'entrée à Moscou après Borodino, la retraite hivernale s'achève par l'anéantissement de la force opérationnelle (moins de 50 000 rescapés).\n\n" +
        "**Plan C (Hypothèse du Twin) :** Le modèle évalue la rupture logistique par dilatation spatiale non compressible : la masse devient vulnérable dès lors que la vitesse d'avancée excède la capacité d'approvisionnement.\n\n" +
        "**Contre-exemple & Réfutation :** Le refus russe d'une bataille décisive (stratégie de terre brûlée de Barclay et Koutouzov) invalide la doctrine napoléonienne de destruction rapide de l'adversaire en une seule confrontation. *Sources : 29e Bulletin de la Grande Armée ; Journal de Caulaincourt ; Dominic Lieven, Russia Against Napoleon.*";
    }

    // 3. Esclavage / 1802 / Colonies
    if (lower.indexOf("esclavage") !== -1 || lower.indexOf("1802") !== -1 || lower.indexOf("guadeloupe") !== -1 || lower.indexOf("saint-domingue") !== -1) {
      return "**Plan A (Histoire) :** La loi du 20 mai 1802 (30 floréal an X) et les arrêtés consulaires rétablissent l'esclavage et la traite négrière dans les colonies restituées et aux Antilles françaises, révoquant le décret d'émancipation de la Convention de 1794.\n\n" +
        "**Plan B (Historiographie) :** Le consensus académique contemporain (Yves Bénot, Jean-Pierre Le Glaunec) documente les pressions du lobby colonial portuaire et la brutalité des expéditions Leclerc à Saint-Domingue et Richepanse en Guadeloupe (mort de Delgrès), conduisant directement à l'indépendance d'Haïti en 1804.\n\n" +
        "**Qualification épistémique :** Il s'agit d'une régression anthropologique et institutionnelle majeure, constitutive de l'une des controverses centrales du Consulat. *Sources : Archives nationales (série AF IV) ; Bulletin des Lois de la République.*";
    }

    // 4. Acre / Égypte / 1799
    if (lower.indexOf("acre") !== -1 || lower.indexOf("égypte") !== -1 || lower.indexOf("aboukir") !== -1 || lower.indexOf("1798") !== -1) {
      return "**Plan A (Histoire) :** Siège de Saint-Jean-d'Acre (mars–mai 1799). Bonaparte échoue devant la garnison ottomane de Djezzar Pacha soutenue par la flotte britannique de Sidney Smith.\n\n" +
        "**Plan C (Hypothèse du Twin) :** Démonstration de la rupture de soutenabilité maritime. Même avec une supériorité tactique sur la terre ferme (victoire des Pyramides), l'asymétrie navale (destruction de la flotte à Aboukir) isole le corps de manœuvre et bloque définitivement la projection stratégique.\n\n" +
        "**Réfutation :** L'armée d'Orient ne peut s'affranchir de la mer fermée. *Sources : Dépêches du SHD ; Henry Laurens, L'Expédition d'Égypte.*";
    }

    // 5. Leipzig / 1813 / Allemagne
    if (lower.indexOf("leipzig") !== -1 || lower.indexOf("1813") !== -1 || lower.indexOf("trachenberg") !== -1) {
      return "**Plan A (Histoire) :** Bataille des Nations à Leipzig (16–19 octobre 1813). Défaite décisive de Napoléon face à la Sixième Coalition (Prusse, Russie, Autriche, Suède).\n\n" +
        "**Plan C (Hypothèse du Twin) :** Analyse du contre-apprentissage adverse. La coalition adopte le plan de Trachenberg : refuser l'affrontement direct avec Napoléon et isoler/anéantir ses maréchaux séparés (Oudinot, Macdonald, Ney).\n\n" +
        "**Limite :** La défection en pleine bataille des contingents alliés allemands (Saxe) révèle l'extrême fragilité des structures impériales satellitaires. *Sources : Rapports d'état-major coalisés ; Thierry Lentz, Nouvelle histoire du Premier Empire t. 2.*";
    }

    // 6. Waterloo / 1815
    if (lower.indexOf("waterloo") !== -1 || lower.indexOf("1815") !== -1 || lower.indexOf("cent-jours") !== -1) {
      return "**Plan A (Histoire) :** 18 juin 1815, plaine de Mont-Saint-Jean. Défaite finale de l'armée française face à la coalition anglo-hollandaise de Wellington et aux Prussiens de Blücher.\n\n" +
        "**Plan C (Hypothèse du Twin) :** Modélisation d'une extrême sensibilité aux frictions initiales : un retard de déploiement (terrain détrempé) conjugué à une défaillance de transmission (détachement de Grouchy) empêche la rupture des deux armées coalisées avant leur jonction.\n\n" +
        "**Sources :** *Ordres de bataille du SHD ; Carl von Clausewitz, La campagne de 1815 en France ; Alessandro Barbero, Waterloo.*";
    }

    // Default bounded response
    return "**Cadre épistémique (Guide borné) :** La question porte sur un élément analysé à travers les quatre plans étanches du Livre Vivant Napoléon.\n\n" +
      "- **Plan A (Faits & Sources) :** Tout événement doit être corroboré par la Correspondance générale ou les archives du SHD / Archives nationales.\n" +
      "- **Plan B (Historiographie) :** Les interprétations sont confrontées aux travaux universitaires contemporains (Tulard, Lentz, Boudon).\n" +
      "- **Plan C (Twin #103) :** Le modèle n'admet aucune maxime forgée et formule des hypothèses conditionnelles révisables adossées au registre des 10 campagnes.\n\n" +
      "Pour préciser votre recherche, vous pouvez explorer les [10 campagnes](campagnes.html), les [controverses](controverses.html) ou les [sources vérifiées](sources.html).";
  }

  function prepareDraft(kind) {
    var lastTurn = turns.length > 0 ? turns[turns.length - 1].content : "";
    if (kind === "objection") {
      if (draftSubject) draftSubject.value = "[Objection Twin Napoléon #103] Réfutation d'une hypothèse stratégique";
      if (draftBody) {
        draftBody.value = "Campagne / Thèse ciblée :\n\n" +
          "Élément contesté dans le modèle du Twin :\n" +
          (lastTurn ? "> " + lastTurn.slice(0, 140) + "...\n\n" : "\n") +
          "Contre-exemple historique documenté (sources primaires obligatoires) :\n\n" +
          "Niveau de confiance proposé : [Faible / Moyen / Élevé]\n";
      }
    } else {
      if (draftSubject) draftSubject.value = "[Contribution Source Napoléon] Signalement d'archive primaire";
      if (draftBody) {
        draftBody.value = "Référence de l'archive ou du document primaire :\n" +
          "- Fonds : [SHD Vincennes / Archives nationales / Autre]\n" +
          "- Cote / Édition : \n" +
          "- Date exacte : \n" +
          "- Extrait textuel authentifié : \n\n" +
          "Impact sur le Livre Vivant (Plan A, B ou C) :\n";
      }
    }
    if (draftStatus) draftStatus.textContent = "Brouillon préparé localement dans le formulaire ci-dessous. Modifiez-le puis copiez-le.";
  }

  function copyDraft() {
    var text = "Destinataire : " + (draftTo ? draftTo.value : "") + "\n" +
      "Objet : " + (draftSubject ? draftSubject.value : "") + "\n\n" +
      (draftBody ? draftBody.value : "");
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () {
        if (draftStatus) draftStatus.textContent = "Brouillon copié dans le presse-papier ! Vous pouvez le transmettre par e-mail ou sur GitHub.";
      }).catch(function () {
        fallbackCopy(text);
      });
    } else {
      fallbackCopy(text);
    }
  }

  function fallbackCopy(text) {
    if (draftBody) {
      draftBody.focus();
      draftBody.select();
      try {
        document.execCommand("copy");
        if (draftStatus) draftStatus.textContent = "Brouillon copié dans le presse-papier.";
      } catch (err) {
        if (draftStatus) draftStatus.textContent = "Veuillez sélectionner le texte ci-dessus et utiliser Ctrl+C pour le copier.";
      }
    }
  }

  function postJson(url, data) {
    return fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    }).then(function (res) {
      if (!res.ok) throw new Error("HTTP " + res.status);
      return res.json();
    });
  }

})();
