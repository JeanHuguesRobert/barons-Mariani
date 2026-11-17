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
  "compose-agent","copy-agent","agent-reply","add-agent-reply","include-agent","send-guide-history",
  "guide-status","guide-stream","cancel-guide"]) {
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
    Blob, TextEncoder, TextDecoder, AbortController, FileReader:class { readAsText(file){this.result=file.text;this.onload();} },
    fetch(url,options){
      const request=JSON.parse(options.body);
      requests.push({url,body:request,headers:options.headers});
      if (!url.endsWith("/guide/chat")) return Promise.resolve({ok:true,json:()=>Promise.resolve({})});
      if(request.question.includes("ANNULEZ_PROBE"))return new Promise((resolve,reject)=>{
        if(options.signal)options.signal.addEventListener("abort",()=>reject(Error("aborted")));
      });
      const absent=request.question.includes("sans source");
      const answer="Deux propositions à étudier : A et B ; coûts, objections et vérifications nécessaires.";
      const frames=[
        ["guide_status",{stage:"retrieval_batch",message:"Recherche publique..."}],
        ["guide_retrieval",{source_count:absent?0:1}],
        ["guide_delta",{content:"Deux propositions à "}],
        ["guide_delta",{content:"étudier..."}],
        ["guide_answer",{ok:true,answer,
          sources:absent?[]:[{source_id:"barons-Mariani:projects/capable/README.md#L1-L3"}],
          grounding:absent?"no_profile_sources":"sources_available"}],
        ["done",{ok:true}]
      ];
      const nl=String.fromCharCode(10);
      if(request.question.includes("BATCH_SSE_PROBE")) {
        for(let i=0;i<600;i++)frames.splice(4,0,["guide_delta",{content:"x".repeat(200)}]);
      }
      const bytes=new TextEncoder().encode(frames.map(([name,data])=>
        "event: "+name+nl+"data: "+JSON.stringify(data)+nl+nl).join(""));
      const chunks=[bytes.slice(0,31),bytes.slice(31,89),bytes.slice(89)];
      return Promise.resolve({ok:true,headers:{get:()=>"text/event-stream"},
        body:{getReader(){let i=0;return{read(){return Promise.resolve(i<chunks.length ?
          {done:false,value:chunks[i++]}:{done:true});}};}}});
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
assert.equal(requests[0].body.stream,true);
assert.equal(requests[0].headers.Accept,"text/event-stream");
assert(get("guide-status").textContent.includes("sources identifiées"));
assert.equal(get("guide-stream").textContent,"");
assert(!store.has("capable-guide-conversation"),"Unconsented retention");
assert.equal(requests.at(-1).body.history.length,0,"History must not leave by default");
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
get("send-guide-history").checked=true;
get("question").value="Objection supplémentaire";
get("ask").events.submit({preventDefault(){}});
await tick();
assert(JSON.stringify(requests.at(-1).body.history).includes("Résultat externe"),
  "Only explicit consent forwards pasted reply");
assert(JSON.stringify(requests.at(-1).body.history).includes("Prix de l'essence"),
  "Explicit opt-in forwards Guide history");
get("explore-switch").checked=true;
get("question").value="Prix de l'essence";
get("ask").events.submit({preventDefault(){}});
await tick();
assert(requests.at(-1).body.question.includes("au moins deux propositions à étudier"));
get("question").value="x".repeat(1199);
const beforeLong=requests.length;
get("ask").events.submit({preventDefault(){}});
await tick();
assert.equal(requests.length,beforeLong,"Oversize exploratory question must not be sent");
assert(get("guide-status").textContent.includes("trop long"));
assert.equal(get("question").value.length,1199);
get("explore-switch").checked=false;
get("question").value="Question sans source";
get("ask").events.submit({preventDefault(){}});
await tick();
assert(get("guide-status").textContent.includes("sans source admissible"));
assert(get("log").children.at(-1).innerHTML.includes("hypothèses non vérifiées"));
const beforeCancel=get("log").children.length;
get("question").value="ANNULEZ_PROBE";
get("ask").events.submit({preventDefault(){}});
assert.equal(get("log").children.length,beforeCancel+1);
get("cancel-guide").click();
await tick();
assert(get("guide-status").textContent.includes("annulée localement"));
assert.equal(get("guide-stream").textContent,"");
assert.equal(get("log").children.length,beforeCancel+1,
  "Cancellation must not create a misleading assistant turn");
get("question").value="BATCH_SSE_PROBE";
get("ask").events.submit({preventDefault(){}});
await tick();
assert(get("guide-status").textContent.includes("sources identifiées"),
  "Many small SSE frames in a single chunk must not trigger the per-frame limit");
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
// Migration from the prior Guide: no silent reading, no silent deletion.
store.set("capable-guide-conversation",JSON.stringify([{role:"user",content:"Ancien échange local"}]));
get=browser();
assert.equal(get("log").children.length,0);
assert(get("continuity-status").textContent.includes("ancien Guide"));
get("retain-local").checked=true;
get("retain-local").events.change();
assert.equal(get("log").children.length,1,"Explicit opt-in restores old conversation");
assert(store.get("capable-guide-conversation").includes("Ancien échange local"));
get("erase-local").click();
assert(!store.has("capable-guide-conversation"));
console.log("CAPABLE_GUIDE_BROWSER_CONTRACT_PASS",requests.length,"requests");
