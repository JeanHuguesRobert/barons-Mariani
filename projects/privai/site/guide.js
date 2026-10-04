(function () {
  var STORAGE_KEY = "privai-guide-conversation";
  var GUIDE_BASE = document.body.getAttribute("data-guide-base") || "https://cogentia.fractavolta.com";
  var GUIDE_PROFILE = document.body.getAttribute("data-guide-profile") || "privai";

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
    if (status) status.textContent = "Le Guide consulte le corpus PrivAI. Rien n'est envoyé.";

    postJson(GUIDE_BASE + "/guide/chat", {
      profile: GUIDE_PROFILE,
      locale: "fr",
      question: clean,
      history: history
    }).then(function (body) {
      var answer = body && body.answer ? String(body.answer) : "Le profil PrivAI est spécifié mais pas encore actif sur le serveur d'inférence commun (cogentia.fractavolta.com). Pour l'heure, veuillez consulter directement les pages n°1, Doctrine et Sources.";
      turns.push({ role: "assistant", content: answer });
      saveTurns();
      render();
      if (status) status.textContent = "Réponse formulée à partir du corpus.";
    }).catch(function () {
      turns.push({
        role: "assistant",
        content: "Le service commun de Guide (cogentia.fractavolta.com) n'est pas joignable ou le profil 'privai' n'y est pas encore déployé. La spécification du profil est conservée dans projects/privai/guide-profile.yml."
      });
      saveTurns();
      render();
      if (status) status.textContent = "Service en cours de raccordement.";
    });
  }

  function prepare(type) {
    var subject = "[Objection PrivAI] ";
    var body = "Bonjour,\n\nJe souhaite soumettre l'observation suivante concernant le Livre Vivant PrivAI :\n\n- Passage ou document visé : \n- Source ou fait contradictoire : \n- Proposition de révision : \n\nCordialement,";
    if (type === "report-correction") {
      subject = "[Correction PrivAI] ";
      body = "Bonjour,\n\nJe signale une coquille ou une citation inexacte dans PrivAI :\n\n- Fichier / page : \n- Texte actuel : \n- Correction suggérée : \n\nMerci,";
    }
    if (draftSubject) draftSubject.value = subject;
    if (draftBody) draftBody.value = body;
    if (status) status.textContent = "Brouillon préparé localement. Vous pouvez le copier pour ouvrir une issue ou envoyer un courriel.";
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
      d.className = "msg msg-" + t.role;
      var p = document.createElement("p");
      p.textContent = (t.role === "user" ? "Vous : " : "Guide : ") + t.content;
      d.appendChild(p);
      log.appendChild(d);
    });
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
