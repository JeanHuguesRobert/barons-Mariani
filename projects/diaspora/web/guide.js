(function () {
  var STORAGE_KEY = "diaspora-guide-conversation";
  var GUIDE_BASE = document.body.getAttribute("data-guide-base") || "https://cogentia.fractavolta.com";
  var GUIDE_PROFILE = document.body.getAttribute("data-guide-profile") || "diaspora";

  var log = document.getElementById("log");
  var form = document.getElementById("ask");
  var question = document.getElementById("question");
  var draftTo = document.getElementById("draft-to");
  var draftSubject = document.getElementById("draft-subject");
  var draftBody = document.getElementById("draft-body");
  var status = document.getElementById("draft-status");
  var turns = loadTurns();

  render();

  if (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      ask(question.value);
    });
  }
  var btnContrib = document.getElementById("prepare-contribution");
  if (btnContrib) {
    btnContrib.addEventListener("click", function () {
      prepare("submit-contribution");
    });
  }
  var btnCorr = document.getElementById("prepare-correction");
  if (btnCorr) {
    btnCorr.addEventListener("click", function () {
      prepare("report-correction");
    });
  }
  var btnCopy = document.getElementById("copy-draft");
  if (btnCopy) btnCopy.addEventListener("click", copyDraft);

  function ask(text) {
    var clean = String(text || "").trim();
    if (!clean || !question) return;
    var history = turns.slice();
    turns.push({ role: "user", content: clean });
    saveTurns();
    render();
    question.value = "";
    if (status) status.textContent = "Le Guide consulte le corpus DIASPORA. Rien n'est envoyé.";
    postJson("/guide/chat", {
      profile: GUIDE_PROFILE,
      locale: "fr",
      question: clean,
      history: history
    }).then(function (body) {
      var answer = body && body.answer ? String(body.answer) : "Le Guide n'a pas pu formuler de réponse basée sur le corpus. Rien n'a été enregistré.";
      turns.push({ role: "assistant", content: answer });
      saveTurns();
      render();
      if (status) status.textContent = "Réponse affichée. Ce n'est pas un conseil juridique ni une position officielle, et aucune donnée n'a été conservée.";
    }).catch(function () {
      if (status) status.textContent = "Le Guide distant ne répond pas. Aucun message n'a été transmis.";
    });
  }

  function prepare(act) {
    var context = lastUserText();
    if (!context) {
      if (status) status.textContent = "Posez d'abord une question ou formulez l'objet de votre observation.";
      return;
    }
    if (status) status.textContent = "Préparation du brouillon local. Aucune donnée n'est transmise.";
    postJson("/guide/prepare-act", {
      profile: GUIDE_PROFILE,
      act: act,
      locale: "fr",
      context: context,
      history: turns
    }).then(function (body) {
      var draft = body && body.prepared_act;
      if (!draft || draft.executed !== false) {
        if (status) status.textContent = "Préparation non autorisée par le profil.";
        return;
      }
      if (draftTo) draftTo.value = draft.to || "contact@corsica-diaspora.com";
      if (draftSubject) draftSubject.value = draft.subject || "[Observation DIASPORA]";
      if (draftBody) draftBody.value = draft.body || context;
      if (status) status.textContent = "Brouillon généré localement. Vous pouvez le modifier et le copier.";
    }).catch(function () {
      if (draftTo) draftTo.value = "contact@corsica-diaspora.com";
      if (draftSubject) draftSubject.value = "[Observation DIASPORA] " + context.slice(0, 50);
      if (draftBody) draftBody.value = "Contexte de l'observation / contribution :\n" + context + "\n\nSource vérifiable :\n";
      if (status) status.textContent = "Modèle de secours inséré localement.";
    });
  }

  function copyDraft() {
    var text = [
      "Brouillon — non envoyé",
      "Destinataire suggéré : " + (draftTo ? draftTo.value : ""),
      "Objet : " + (draftSubject ? draftSubject.value : ""),
      "",
      draftBody ? draftBody.value : ""
    ].join("\n");
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () {
        if (status) status.textContent = "Brouillon copié dans le presse-papier.";
      });
    } else {
      if (status) status.textContent = "Veuillez sélectionner le texte pour le copier manuellement.";
    }
  }

  function render() {
    if (!log) return;
    log.innerHTML = "";
    turns.forEach(function (t) {
      var card = document.createElement("div");
      card.className = "msg " + t.role;
      var roleLabel = t.role === "user" ? "Votre question :" : "Le Guide (corpus DIASPORA) :";
      card.innerHTML = "<strong>" + roleLabel + "</strong><p>" + escapeHtml(t.content) + "</p>";
      log.appendChild(card);
    });
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
      localStorage.setItem(STORAGE_KEY, JSON.stringify(turns.slice(-10)));
    } catch (e) {}
  }

  function lastUserText() {
    for (var i = turns.length - 1; i >= 0; i--) {
      if (turns[i].role === "user") return turns[i].content;
    }
    return question ? question.value : "";
  }

  function postJson(path, payload) {
    return fetch(GUIDE_BASE + path, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    }).then(function (res) {
      if (!res.ok) throw new Error("HTTP " + res.status);
      return res.json();
    });
  }

  function escapeHtml(str) {
    return String(str || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }
})();
