#!/usr/bin/env node
/** Non-network browser-contract test for Capable's existing Guide page. */
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import vm from "node:vm";

const root = fileURLToPath(new URL("../../", import.meta.url));
const js = readFileSync(root + "projects/capable/site/guide.js", "utf8");
const html = readFileSync(root + "projects/capable/site/guide.html", "utf8");
for (const id of ["retain-local","export-text","export-json","import-json","erase-local",
  "compose-agent","copy-agent","agent-reply","add-agent-reply","include-agent"]) {
  assert(html.includes('id="' + id + '"'), "Missing UI control " + id);
}
assert(html.includes('value="explore"'));
assert(!js.includes("sendBeacon(") && !js.includes("window.open("));

const store = new Map(), requests = [], copied = [];
function browser() {
  const elements = new Map();
  function node() {
    const n = {
      value: "", textContent: "", checked: false, files: [], children: [], events: {},
      addEventListener(type, callback) { this.events[type] = callback; },
      appendChild(child) { this.children.push(child); },
      click() { if (this.events.click) this.events.click(); },
      focus() {}, select() {},
      get innerHTML() { return this.html || ""; },
      set innerHTML(value) { this.html = value; if (!value) this.children = []; },
    };
    return n;
  }
  const doc = {
    body: { getAttribute(key) { return key === "data-guide-profile" ? "capable" : null; } },
    getElementById(id) {
      if (!elements.has(id)) elements.set(id,node());
      return elements.get(id);
    },
    querySelector() {
      return {value:doc.getElementById("explore-switch").checked ? "explore" : "documentary"};
    },
    createElement() { return node(); },
  };
  const storage = {
    getItem(key) { return store.get(key) ?? null; },
    setItem(key,value) { store.set(key,value); },
    removeItem(key) { store.delete(key); },
  };
  vm.runInNewContext(js,{
    document:doc,localStorage:storage,window:{confirm:()=>true},
    navigator:{clipboard:{writeText(value){copied.push(value);return Promise.resolve();}}},
    URL:{createObjectURL:()=>"/blob",revokeObjectURL(){}},
    Blob, FileReader:class { readAsText(file){this.result=file.text;this.onload();} },
    fetch(url,options){
      requests.push({url,body:JSON.parse(options.body)});
      return Promise.resolve({ok:true,json:()=>Promise.resolve({
        answer:"Deux propositions à étudier : A et B ; coûts, objections et vérifications nécessaires.",
      })});
    },
  },{filename:"guide.js",timeout:3000});
  return (id)=>doc.getElementById(id);
}
const tick=()=>new Promise(resolve=>setImmediate(resolve));
let get=browser();
assert.equal(store.size,0,"No default local retention");
get("question").value="Prix de l'essence ?";
get("ask").events.submit({preventDefault(){}});
await tick();
assert.equal(requests.length,1);
assert(!store.has("capable-guide-conversation"),"Unconsented retention");
assert.equal(get("log").children.length,2);
get("retain-local").checked=true;
get("retain-local").events.change();
assert(store.has("capable-guide-conversation"));
get=browser();
assert.equal(get("log").children.length,2,"Reload continuity");
get("compose-agent").click();
assert(get("agent-prompt").value.includes("Prix de l'essence"));
assert(!get("agent-prompt").value.includes("Deux propositions"),"Unselected Guide content");
get("include-guide").checked=true;
get("compose-agent").click();
assert(get("agent-prompt").value.includes("Deux propositions"));
get("copy-agent").click();await tick();
assert.equal(copied.length,1);
get("agent-name").value="Claude";
get("agent-reply").value="Résultat externe non vérifié";
get("agent-note").value="Objection du visiteur";
get("add-agent-reply").click();
assert.equal(get("log").children.length,3);
get("question").value="Autre question";
get("ask").events.submit({preventDefault(){}});
await tick();
assert(!JSON.stringify(requests.at(-1).body.history).includes("Résultat externe"),
  "Agent response must stay local unless selected");
get("include-agent").checked=true;
get("question").value="Objection supplémentaire";
get("ask").events.submit({preventDefault(){}});
await tick();
assert(JSON.stringify(requests.at(-1).body.history).includes("Résultat externe"),
  "Only explicit consent forwards pasted reply");
get("explore-switch").checked=true;
get("question").value="Prix de l'essence";
get("ask").events.submit({preventDefault(){}});
await tick();
assert(requests.at(-1).body.question.includes("au moins deux propositions à étudier"));
const previous=store.get("capable-guide-conversation");
get("export-json").click();
assert(get("continuity-status").textContent.includes("Export"));
get("erase-local").click();
assert(!store.has("capable-guide-conversation"));
assert(!store.has("capable-guide-opt-in"));
assert.equal(get("log").children.length,0);
get("import-json").files=[{size:previous.length,text:previous}];
get("import-json").events.change();
assert.equal(get("log").children.length,JSON.parse(previous).turns.length);
get("erase-local").click();
get=browser();
assert.equal(get("log").children.length,0,"Purge persists after reload");
console.log("CAPABLE_GUIDE_BROWSER_CONTRACT_PASS",requests.length,"requests");
