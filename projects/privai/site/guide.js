(function () {
  var STORAGE_KEY = "privai-guide-conversation";
  var GUIDE_BASE = document.body.getAttribute("data-guide-base") || "https://cogentia.fractavolta.com";
  var GUIDE_PROFILE = document.body.getAttribute("data-guide-profile") || "privai";

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
    if (status) status.textContent = "Le Guide consulte le corpus. Rien n'est envoyé.";
    postJson("/guide/chat", {
      profile: GUIDE_PROFILE,
      locale: "fr",
      question: clean,
      history: history
    }).then(function (body) {
      var answer = body && body.answer ? String(body.answer) : "Le Guide n'a pas fourni de réponse. Rien n'a été envoyé.";
      turns.push({ role: "assistant", content: answer });
      saveTurns();
      render();
      if (status) status.textContent = "Réponse affichée. Ce n'est pas une contribution, et rien n'a été envoyé.";
    }).catch(function () {
      if (status) status.textContent = "Le Guide n'a pas répondu. Aucun message n'a été envoyé.";
    });
  }

  function prepare(act) {
    var context = lastUserText();
    if (!context) {
      if (status) status.textContent = "Écrivez d'abord la phrase à reprendre. Rien n'est envoyé.";
      return;
    }
    if (status) status.textContent = "Préparation du brouillon. Rien n'est envoyé.";
    postJson("/guide/prepare-act", {
      profile: GUIDE_PROFILE,
      act: act,
      locale: "fr",
      context: context,
      history: turns
    }).then(function (body) {
      var draft = body && body.prepared_act;
      if (!draft || draft.executed !== false) {
        if (status) status.textContent = "Préparation refusée. Rien n'a été envoyé.";
        return;
      }
      if (draftTo) draftTo.value = draft.to || "";
      if (draftSubject) draftSubject.value = draft.subject || "";
      if (draftBody) draftBody.value = draft.body || "";
      if (status) status.textContent = "Brouillon — non envoyé. Vous pouvez le modifier et le copier.";
    }).catch(function () {
      if (status) status.textContent = "Le brouillon n'a pas pu être préparé. Rien n'a été envoyé.";
    });
  }

  function copyDraft() {
    var text = [
      "Brouillon — non envoyé",
      "Destinataire : " + (draftTo ? draftTo.value : ""),
      "Objet : " + (draftSubject ? draftSubject.value : ""),
      "",
      draftBody ? draftBody.value : ""
    ].join("\n");
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () {
        if (status) status.textContent = "Brouillon copié. Rien n'a été envoyé.";
      }).catch(selectDraft);
      return;
    }
    selectDraft();
  }

  function selectDraft() {
    if (!draftBody) return;
    draftBody.focus();
    draftBody.select();
    if (status) status.textContent = "Copie automatique indisponible. Le texte est sélectionné. Rien n'a été envoyé.";
  }

  function lastUserText() {
    for (var i = turns.length - 1; i >= 0; i -= 1) {
      if (turns[i].role === "user" && turns[i].content) return turns[i].content;
    }
    return "";
  }

  function render() {
    if (!log) return;
    log.replaceChildren();
    turns.forEach(function (turn) {
      var item = document.createElement("div");
      item.className = "msg msg-" + (turn.role === "user" ? "user" : "assistant");
      var paragraph = document.createElement("p");
      paragraph.textContent = (turn.role === "user" ? "Vous — " : "Guide — ") + turn.content;
      item.appendChild(paragraph);
      log.appendChild(item);
    });
  }

  function loadTurns() {
    try {
      var parsed = JSON.parse(sessionStorage.getItem(STORAGE_KEY) || "[]");
      if (!Array.isArray(parsed)) return [];
      return parsed.filter(isTurn).slice(-16);
    } catch (error) {
      return [];
    }
  }

  function saveTurns() {
    try {
      sessionStorage.setItem(STORAGE_KEY, JSON.stringify(turns.slice(-16)));
    } catch (error) {}
  }

  function isTurn(item) {
    return item && (item.role === "user" || item.role === "assistant") && typeof item.content === "string";
  }

  function postJson(route, payload) {
    return fetch(GUIDE_BASE + route, {
      method: "POST",
      headers: { "Content-Type": "application/json", Accept: "application/json" },
      body: JSON.stringify(payload)
    }).then(function (response) {
      if (!response.ok) throw new Error("guide_http_" + response.status);
      return response.json();
    });
  }
})();
