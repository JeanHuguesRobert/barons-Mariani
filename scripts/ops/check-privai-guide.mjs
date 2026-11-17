#!/usr/bin/env node
/** Privacy and triangulation contract of the second Living Book Reality Case. */
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const html = fs.readFileSync(path.join(root,"projects/privai/site/guide.html"),"utf8");
const js = fs.readFileSync(path.join(root,"projects/privai/site/guide.js"),"utf8");
const capable = fs.readFileSync(path.join(root,"projects/capable/site/guide.js"),"utf8");
assert.equal(js,capable,"Two Guides must reuse exactly the same browser runtime");
for (const id of ["retain-local","export-text","export-json","import-json",
  "erase-local","compose-agent","copy-agent","agent-reply","add-agent-reply",
  "include-agent","include-guide","include-history","send-guide-history",
  "guide-status","guide-stream","cancel-guide","draft-status"]) {
  assert(html.includes('id="'+id+'"'),"Missing PrivAI control "+id);
}
assert(html.includes('data-guide-profile="privai"'));
assert(!html.includes("n'enregistre rien sur un serveur"));
assert(!html.includes("Aucun journal de questions"));

const local = new Map();
const legacy = new Map([["privai-guide-conversation",
  JSON.stringify([{role:"user",content:"Ancien échange PrivAI"}])]]);
const calls = [];
const getStore = map => ({
  getItem:k=>map.get(k)??null,
  setItem:(k,v)=>map.set(k,v),
  removeItem:k=>map.delete(k)
});
function boot() {
  const els = new Map();
  function node() {
    return {
      value:"",checked:false,textContent:"",files:[],children:[],events:{},
      addEventListener(type,cb){this.events[type]=cb;},
      click(){this.events.click?.();},
      appendChild(child){this.children.push(child);},
      replaceChildren(){this.children=[];},
      focus(){},select(){},
      get innerHTML(){return this.html||"";},
      set innerHTML(v){this.html=v;if(!v)this.children=[];}
    };
  }
  const doc = {
    body:{getAttribute:k=>k==="data-guide-profile"?"privai":
      k==="data-guide-title"?"PrivAI":null},
    getElementById(id) {if(!els.has(id))els.set(id,node());return els.get(id);},
    createElement(){return node();},
    querySelector(){return null}
  };
  const nl=String.fromCharCode(10);
  vm.runInNewContext(js,{
    document:doc,
    localStorage:getStore(local),sessionStorage:getStore(legacy),
    window:{confirm:()=>true},
    navigator:{clipboard:{writeText:()=>Promise.resolve()}},
    URL:{createObjectURL:()=>"/blob",revokeObjectURL(){}},Blob,TextDecoder,TextEncoder,
    AbortController,
    FileReader:class {readAsText(file){this.result=file.text;this.onload();}},
    fetch(url,options){
      const body=JSON.parse(options.body);calls.push({url,body});
      const events=[
        ["guide_status",{stage:"retrieval",message:"Recherche..."}],
        ["guide_retrieval",{source_count:1}],
        ["guide_delta",{content:"Réponse initiale"}],
        ["guide_answer",{ok:true,answer:"Analyse PrivAI avec citation.",
          sources:[{source_id:"barons-Mariani:projects/privai/README.md#L1-L5",
            title:"PrivAI — Présentation",
            github_url:"https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/privai/README.md#L1-L5"}],
          grounding:"sources_available"}],
        ["done",{ok:true}]
      ];
      const bytes=new TextEncoder().encode(events.map(([name,data])=>
        "event: "+name+nl+"data: "+JSON.stringify(data)+nl+nl).join(""));
      return Promise.resolve({ok:true,headers:{get:()=>"text/event-stream"},
        body:{getReader(){let i=0;return{read:()=>Promise.resolve(i++===0?
          {done:false,value:bytes}:{done:true})};}}});
    },
  },{filename:"guide.js",timeout:3000});
  return id=>doc.getElementById(id);
}
const tick=()=>new Promise(resolve=>setImmediate(resolve));
let get=boot();
assert.equal(get("log").children.length,0,"No implicit legacy session reading");
assert(get("continuity-status").textContent.includes("ancien Guide"));
assert.equal(local.size,0);
get("question").value="Quels contre-pouvoirs cognitifs ?";
get("ask").events.submit({preventDefault(){}});
await tick();
assert.equal(calls.length,1);
assert.equal(calls[0].body.profile,"privai");
assert.equal(calls[0].body.history.length,0,"No implicit history transmission");
assert.equal(get("log").children.length,2);
assert(!local.has("privai-guide-conversation"),"No implicit local retention");
get("erase-local").click();
assert(!legacy.has("privai-guide-conversation"),"Erase must clear old sessionStorage");
get("question").value="Nouvel échange";
get("ask").events.submit({preventDefault(){}});
await tick();
get("retain-local").checked=true;
get("retain-local").events.change();
assert(local.has("privai-guide-conversation"));
get=boot();
assert.equal(get("log").children.length,2,"Opt-in continuity after reload");
assert.equal(get("log").children.at(-1).children[0].children[1].href,
  "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/privai/README.md#L1-L5",
  "Source URL must survive reload");
get("agent-reply").value="Réponse non vérifiée d'un agent externe";
get("add-agent-reply").click();
get("question").value="Suite documentaire";
get("ask").events.submit({preventDefault(){}});
await tick();
assert(!JSON.stringify(calls.at(-1).body.history).includes("Réponse non vérifiée"),
  "No implicit forwarding of an external agent");
get("include-agent").checked=true;
get("question").value="Autre suite";
get("ask").events.submit({preventDefault(){}});
await tick();
assert(JSON.stringify(calls.at(-1).body.history).includes("Réponse non vérifiée"),
  "Forwarding explicitly chosen by visitor");
get("erase-local").click();
assert(!local.has("privai-guide-conversation"));
assert(!local.has("privai-guide-opt-in"));
get=boot();
assert.equal(get("log").children.length,0);
console.log("PRIVAI_GUIDE_CONTRACT_PASS",calls.length,"requests");
