(function () {
  var STORAGE_KEY = "commons-guide-conversation";
  var GUIDE_BASE = document.body.getAttribute("data-guide-base") || "https://cogentia.fractavolta.com";
  var GUIDE_PROFILE = document.body.getAttribute("data-guide-profile") || "commons";

  var log = document.getElementById("log");
  var form = document.getElementById("ask");
  var question = document.getElementById("question");
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
  if (btnCopy) {
    btnCopy.addEventListener("click", copyDraft);
  }

  function ask(text) {
    var clean = String(text || "").trim();
    if (!clean) return;
    var history = turns.slice();
    turns.push({ role: "user", content: clean });
    saveTurns();
    render();
    if (question) question.value = "";
    if (status) status.textContent = "Le Guide consulte le corpus Commons. Aucune donnée n'est envoyée à des tiers.";

    postJson(GUIDE_BASE + "/guide/chat", {
      profile: GUIDE_PROFILE,
      locale: "fr",
      question: clean,
      history: history
    }).then(function (body) {
      var answer = body && body.answer ? String(body.answer) : "Le profil Commons est spécifié mais pas encore activé sur le serveur d'inférence commun (cogentia.fractavolta.com). Pour l'heure, veuillez consulter directement les pages Numéro 1, Cas, Magazine et Annexes.";
      turns.push({ role: "assistant", content: answer });
      saveTurns();
      render();
      if (status) status.textContent = "Réponse formulée à partir du corpus.";
    }).catch(function () {
      turns.push({
        role: "assistant",
        content: "Le service commun de Guide (cogentia.fractavolta.com) n'est pas joignable ou le profil 'commons' n'y est pas encore déployé. La spécification du profil est conservée dans projects/commons/guide-profile.yml."
      });
      saveTurns();
      render();
      if (status) status.textContent = "Service en cours de raccordement.";
    });
  }

  function prepare(type) {
    var subject = "[Observation Commons] ";
    var body = "Bonjour,\n\nJe souhaite soumettre l'observation suivante concernant le Livre Vivant Commons :\n\n- Sujet / Cas / Mouvement visé : \n- Source ou référence documentaire : \n- Proposition d'enrichissement ou d'analyse : \n\nCordialement,";
    if (type === "report-correction") {
      subject = "[Correction Commons] ";
      body = "Bonjour,\n\nJe signale une anomalie, une coquille ou une référence à préciser dans Commons :\n\n- Fichier ou page : \n- Texte ou mention actuelle : \n- Source ou correction suggérée : \n\nMerci,";
    }
    if (draftSubject) draftSubject.value = subject;
    if (draftBody) draftBody.value = body;
    if (status) status.textContent = "Brouillon préparé localement. Vous pouvez le copier pour ouvrir une issue sur GitHub ou envoyer un courriel.";
  }

  function copyDraft() {
    if (!draftBody) return;
    navigator.clipboard.writeText(draftBody.value).then(function () {
      if (status) status.textContent = "Brouillon copié dans le presse-papier !";
    }).catch(function () {
      if (status) status.textContent = "Sélectionnez et copiez le texte manuellement.";
    });
  }

  function render() {
    if (!log) return;
    log.innerHTML = "";
    turns.forEach(function (t) {
      var d = document.createElement("div");
      d.className = "card";
      d.style.marginBottom = "0.75rem";
      d.style.background = t.role === "user" ? "#f1f5f9" : "#ffffff";
      var p = document.createElement("p");
      p.style.margin = "0";
      p.innerHTML = "<strong>" + (t.role === "user" ? "Vous : " : "Guide Commons : ") + "</strong>" + escapeHtml(t.content);
      d.appendChild(p);
      log.appendChild(d);
    });
  }

  function escapeHtml(str) {
    return String(str || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/\n/g, "<br>");
  }

  function loadTurns() {
    try {
      var raw = sessionStorage.getItem(STORAGE_KEY);
      return raw ? JSON.parse(raw) : [];
    } catch (e) {
      return [];
    }
  }

  function saveTurns() {
    try {
      sessionStorage.setItem(STORAGE_KEY, JSON.stringify(turns));
    } catch (e) {}
  }

  function postJson(url, payload) {
    return fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    }).then(function (r) {
      if (!r.ok) throw new Error("HTTP " + r.status);
      return r.json();
    });
  }
})();
