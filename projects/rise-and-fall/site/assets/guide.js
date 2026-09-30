(function () {
  var STORAGE_KEY = "rise-and-fall-guide-conversation";
  var GUIDE_BASE = document.body.getAttribute("data-guide-base") || "https://cogentia.fractavolta.com";
  var GUIDE_PROFILE = document.body.getAttribute("data-guide-profile") || "rise-and-fall";

  var log = document.getElementById("log");
  var form = document.getElementById("ask");
  var question = document.getElementById("question");
  var draftTo = document.getElementById("draft-to");
  var draftSubject = document.getElementById("draft-subject");
  var draftBody = document.getElementById("draft-body");
  var status = document.getElementById("draft-status");
  var turns = loadTurns();

  render();

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    ask(question.value);
  });
  
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
    question.value = "";
    status.textContent = "Le Guide réfléchit à partir du corpus public. Rien n'est envoyé.";
    
    postJson("/guide/chat", {
      profile: GUIDE_PROFILE,
      locale: "fr",
      question: clean,
      history: history,
    }).then(function (body) {
      var answer = body && body.answer ? String(body.answer) : "Le Guide n'a pas retourné de réponse spécifique. Aucun message n'a été envoyé.";
      turns.push({ role: "assistant", content: answer });
      saveTurns();
      render();
      status.textContent = "Réponse affichée. Ce n'est pas un message officiel, et rien n'a été envoyé.";
    }).catch(function () {
      // Local fallback in case the guide endpoint is temporarily unreachable
      var fallbackAnswer = "Le Guide est actuellement en cours de synchronisation avec le corpus. Pour toute question ou apport documentaire, vous pouvez vous référer à la page Contribuer ou adresser un message directement à jhr@baronsmariani.org.";
      turns.push({ role: "assistant", content: fallbackAnswer });
      saveTurns();
      render();
      status.textContent = "Mode hors-ligne : réponse locale. Aucun message n'a été envoyé.";
    });
  }

  function prepare(act) {
    status.textContent = "Préparation du brouillon en cours...";
    var latestUser = lastUserText();

    postJson("/guide/prepare-act", {
      profile: GUIDE_PROFILE,
      act: act,
      locale: "fr",
      context: latestUser,
      history: turns,
    }).then(function (body) {
      var draft = body && body.prepared_act;
      if (!draft || draft.executed !== false) {
        useLocalTemplate(act, latestUser);
        return;
      }
      draftTo.value = draft.to || "jhr@baronsmariani.org, institutmariani@gmail.com";
      draftSubject.value = draft.subject || "[Contribution Rise & Fall] " + (act === "report-correction" ? "Observation sur une source" : "Apport documentaire");
      draftBody.value = draft.body || "";
      status.textContent = "Brouillon généré — non envoyé. Vous pouvez le modifier, le copier ou l'annuler.";
    }).catch(function () {
      useLocalTemplate(act, latestUser);
    });
  }

  function useLocalTemplate(act, context) {
    draftTo.value = "jhr@baronsmariani.org, institutmariani@gmail.com";
    if (act === "report-correction") {
      draftSubject.value = "[Rise & Fall] Observation / Correction sur une source";
      draftBody.value = [
        "Bonjour,",
        "",
        "Dans le cadre de l'enquête Rise & Fall of the Mariani Family, je souhaite porter à votre attention l'observation suivante :",
        "",
        "> " + (context || "[Précisez ici l'élément, la date ou la source concernée]"),
        "",
        "Éléments contradictoires ou source primaire complémentaire :",
        "- [Référence archivistique, acte ou lien]",
        "",
        "Cordialement,",
        "[Votre nom / fonction ou pseudonyme]"
      ].join("\n");
    } else {
      draftSubject.value = "[Rise & Fall] Contribution / Apport d'archives";
      draftBody.value = [
        "Bonjour,",
        "",
        "Je souhaite vous signaler ou transmettre une pièce utile pour l'enquête Rise & Fall :",
        "",
        "1. Nature du document (notarié, cadastral, familial, presse) :",
        "[Précisez ici]",
        "",
        "2. Période ou personnalité concernée (ex. Antoine Dominique Mariani, Minesteggio, élection 1863, donation 1924) :",
        "[Précisez ici]",
        "",
        "3. Description et cote éventuelle :",
        "> " + (context || "[Détaillez ici votre apport]"),
        "",
        "Modalités de communication souhaitées :",
        "[ ] Échange privé et confidentiel par courriel",
        "[ ] Contribution publique sur le dépôt GitHub",
        "",
        "Cordialement,",
        "[Votre nom / contact]"
      ].join("\n");
    }
    status.textContent = "Brouillon modèle généré localement — non envoyé.";
  }

  function copyDraft() {
    var text = [
      "--- BROUILLON RISE & FALL (NON ENVOYÉ) ---",
      "Destinataire : " + draftTo.value,
      "Objet : " + draftSubject.value,
      "",
      draftBody.value,
    ].join("\n");
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () {
        status.textContent = "Brouillon copié dans le presse-papier avec succès ! Rien n'a été envoyé.";
      }).catch(selectDraft);
      return;
    }
    selectDraft();
  }

  function selectDraft() {
    draftBody.focus();
    draftBody.select();
    status.textContent = "Texte sélectionné. Vous pouvez le copier manuellement (Ctrl+C). Rien n'a été envoyé.";
  }

  function postJson(route, payload) {
    return fetch(GUIDE_BASE + route, {
      method: "POST",
      headers: { "Content-Type": "application/json", Accept: "application/json" },
      body: JSON.stringify(payload),
    }).then(function (response) {
      if (!response.ok) throw new Error("guide_http_" + response.status);
      return response.json();
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
    sessionStorage.setItem(STORAGE_KEY, JSON.stringify(turns.slice(-16)));
  }

  function render() {
    log.replaceChildren();
    if (turns.length === 0) {
      var hint = document.createElement("p");
      hint.style.color = "#777";
      hint.style.fontStyle = "italic";
      hint.style.fontSize = "0.9rem";
      hint.textContent = "Aucun échange pour l'instant. Posez une question ci-dessous ou préparez un brouillon.";
      log.appendChild(hint);
      return;
    }
    turns.forEach(function (turn) {
      var item = document.createElement("div");
      item.className = "turn";
      var who = document.createElement("div");
      who.className = "who";
      who.textContent = turn.role === "assistant" ? "Guide Public" : "Vous";
      var body = document.createElement("p");
      body.textContent = turn.content;
      item.append(who, body);
      log.append(item);
    });
  }

  function lastUserText() {
    for (var i = turns.length - 1; i >= 0; i -= 1) {
      if (turns[i].role === "user" && turns[i].content) return turns[i].content;
    }
    return "";
  }

  function isTurn(item) {
    return item && (item.role === "user" || item.role === "assistant") && typeof item.content === "string";
  }
}());
