#!/usr/bin/env node
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import http from "node:http";
import net from "node:net";
import {spawn} from "node:child_process";

import {fileURLToPath} from "node:url";
const root=process.env.GUIDE_REPO_ROOT || path.resolve(path.dirname(fileURLToPath(import.meta.url)),"../..");
const dir=fs.mkdtempSync(path.join(os.tmpdir(),"guide-cdp-"));
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
async function freePort(){
  const s=net.createServer();await new Promise(r=>s.listen(0,"127.0.0.1",r));
  const p=s.address().port;await new Promise(r=>s.close(r));return p;
}
const port=await freePort();
const server=http.createServer((req,res)=>{
  const url=new URL(req.url,"http://localhost");
  const m=/^\/(capable|privai)\/([a-z0-9-]+\.(html|js|css))$/.exec(url.pathname);
  if(!m){res.writeHead(404);return res.end("Not found")}
  const file=path.join(root,"projects",m[1],"site",m[2]);
  if(!fs.existsSync(file)){res.writeHead(404);return res.end("Missing")}
  const mime=m[3]==="html"?"text/html; charset=utf-8":m[3]==="js"?"text/javascript; charset=utf-8":"text/css";
  res.writeHead(200,{"Content-Type":mime,"Cache-Control":"no-store"});
  fs.createReadStream(file).pipe(res);
});
await new Promise(r=>server.listen(port,"127.0.0.1",r));
const cdpPort=await freePort();
const chromium=process.env.GUIDE_CHROMIUM_PATH ||
  (fs.existsSync("/usr/bin/chromium")?"/usr/bin/chromium":"/usr/bin/google-chrome");
const chrome=spawn(chromium,[
  "--headless=new","--no-sandbox","--disable-gpu","--disable-dev-shm-usage",
  "--disable-breakpad","--no-first-run","--no-default-browser-check",
  "--remote-allow-origins=*","--remote-debugging-port="+cdpPort,
  "--user-data-dir="+dir,"about:blank"
],{stdio:"ignore"});
let ws=null;
try{
  let endpoint=null;
  for(let i=0;i<120;i++){
    try{
      const r=await fetch("http://127.0.0.1:"+cdpPort+"/json/new?about:blank",{method:"PUT"});
      if(r.ok){endpoint=(await r.json()).webSocketDebuggerUrl;break}
    }catch{}
    await sleep(100);
  }
  assert(endpoint,"Chrome DevTools port did not become ready");
  ws=new WebSocket(endpoint);
  await new Promise((resolve,reject)=>{
    ws.addEventListener("open",resolve,{once:true});
    ws.addEventListener("error",reject,{once:true});
  });
  let seq=0;const pending=new Map();
  ws.addEventListener("message",ev=>{
    let packet;try{packet=JSON.parse(ev.data)}catch{return}
    if(!packet.id||!pending.has(packet.id))return;
    const p=pending.get(packet.id);pending.delete(packet.id);
    if(packet.error)p.reject(Error(JSON.stringify(packet.error)));
    else p.resolve(packet.result||{});
  });
  const cdp=(method,params={})=>new Promise((resolve,reject)=>{
    const id=++seq;pending.set(id,{resolve,reject});
    ws.send(JSON.stringify({id,method,params}));
    setTimeout(()=>{if(pending.has(id)){pending.delete(id);reject(Error("CDP timeout "+method))}},15000);
  });
  const evaluate=async expression=>{
    const result=await cdp("Runtime.evaluate",{expression,returnByValue:true,awaitPromise:true,userGesture:true});
    if(result.exceptionDetails)throw Error("Browser JS: "+JSON.stringify(result.exceptionDetails).slice(0,500));
    return result.result?.value;
  };
  const wait=async(expression,timeoutMs=6500)=>{
    for(let i=0;i<timeoutMs/100;i++){
      if(await evaluate(expression))return;
      await sleep(100);
    }
    throw Error("Browser condition failed: "+expression);
  };
  const url="/guide.html";
  await cdp("Page.enable");
  await cdp("Runtime.enable");
  await cdp("Emulation.setDeviceMetricsOverride",{width:390,height:844,deviceScaleFactor:1,mobile:true});
  const injection=[
    "window.confirm=()=>true;",
    "window.__guideTestCalls=[];",
    "window.fetch=async function(url,opts){",
    " if(String(url).endsWith('/guide/chat')){",
    "  const data=JSON.parse(opts.body);window.__guideTestCalls.push(data);",
    "  if(data.question.includes('CANCEL_PROBE'))return new Promise((resolve,reject)=>opts.signal.addEventListener('abort',()=>reject(new Error('aborted'))));",
    "  const absent=data.question.includes('NO_SOURCE');",
    "  const sourceId='barons-Mariani:projects/'+data.profile+'/README.md#L1-L4';",
    "  const answer='Réponse documentée pour '+data.profile+'.';",
    "  const events=[['guide_status',{stage:'retrieval',message:'Recherche en cours'}],",
    "    ['guide_retrieval',{source_count:absent?0:1}],",
    "    ['guide_delta',{content:'Réponse partielle'}],",
    "    ['guide_answer',{ok:true,answer,sources:absent?[]:[{source_id:sourceId}],grounding:absent?'no_profile_sources':'sources_available'}],",
    "    ['done',{ok:true}]];",
    "  const nl=String.fromCharCode(10);",
    "  const raw=events.map(([event,payload])=>'event: '+event+nl+'data: '+JSON.stringify(payload)+nl+nl).join('');",
    "  return new Response(new ReadableStream({start(c){const bytes=new TextEncoder().encode(raw);c.enqueue(bytes.slice(0,23));c.enqueue(bytes.slice(23));c.close();}}),",
    "  {status:200,headers:{'Content-Type':'text/event-stream'}});",
    " }",
    " return new Response('{}',{status:404,headers:{'Content-Type':'application/json'}});",
    "};"
  ].join("\n");
  await cdp("Page.addScriptToEvaluateOnNewDocument",{source:injection});
  async function visit(book){
    await cdp("Page.navigate",{url:"http://127.0.0.1:"+port+"/"+book+url});
    await wait("document.readyState==='complete' && !!document.getElementById('retain-local')");
    const summary=await evaluate("({title:document.title,width:window.innerWidth,scrollWidth:document.documentElement.scrollWidth,profile:document.body.getAttribute('data-guide-profile'),buttons:[...document.querySelectorAll('button')].length})");
    assert.equal(summary.profile,book);
    assert(summary.scrollWidth <= summary.width+4,"Horizontal mobile overflow "+book+": "+JSON.stringify(summary));
    console.log("MOBILE_RENDER",book,JSON.stringify(summary));
  }
  await visit("capable");
  assert.equal(await evaluate("localStorage.length"),0);
  await evaluate("document.getElementById('question').focus()");
  await cdp("Input.insertText",{text:"Quelle est la doctrine Capable ?"});
  await evaluate("document.querySelector('#ask button[type=submit]').click()");
  await wait("document.getElementById('log').children.length===2");
  assert.equal(await evaluate("window.__guideTestCalls[0].profile"),"capable");
  assert.equal(await evaluate("window.__guideTestCalls[0].history.length"),0);
  assert.equal(await evaluate("localStorage.getItem('capable-guide-conversation')"),null);
  await evaluate("document.getElementById('retain-local').click()");
  assert(await evaluate("!!localStorage.getItem('capable-guide-conversation')"));
  await evaluate("sessionStorage.setItem('privai-guide-conversation',JSON.stringify([{role:'user',content:'ANCIEN_PRIVAI'}]))");
  await visit("privai");
  assert.equal(await evaluate("document.getElementById('log').children.length"),0,"PrivAI must not inherit Capable transcript");
  assert.equal(await evaluate("localStorage.getItem('privai-guide-conversation')"),null);
  assert(await evaluate("document.getElementById('continuity-status').textContent.includes('ancien Guide')"));
  await evaluate("document.getElementById('retain-local').click()");
  assert.equal(await evaluate("document.getElementById('log').children.length"),1,"Explicit legacy migration");
  assert.equal(await evaluate("sessionStorage.getItem('privai-guide-conversation')"),null,"Session migrated");
  assert(await evaluate("!!localStorage.getItem('privai-guide-conversation')"));
  await evaluate("document.getElementById('question').value='Quelles sont les asymétries ?';document.querySelector('#ask button[type=submit]').click()");
  await wait("document.getElementById('log').children.length===3");
  assert.equal(await evaluate("window.__guideTestCalls[0].history.length"),0,"No automatic legacy history transmission");
  await evaluate("document.getElementById('agent-reply').value='AGENT_SECRET_SENTINEL';document.getElementById('add-agent-reply').click()");
  await evaluate("document.getElementById('question').value='Question suivante';document.querySelector('#ask button[type=submit]').click()");
  await wait("document.getElementById('log').children.length===6");
  assert.equal(await evaluate("window.__guideTestCalls[1].history.length"),0,"No implicit agent transmission");
  await evaluate("document.getElementById('include-agent').click()");
  await evaluate("document.getElementById('question').value='Question explicite';document.querySelector('#ask button[type=submit]').click()");
  await wait("document.getElementById('log').children.length===8");
  assert(await evaluate("JSON.stringify(window.__guideTestCalls[2].history).includes('AGENT_SECRET_SENTINEL')"),"Chosen agent context forwarded");
  await evaluate("document.getElementById('question').value='CANCEL_PROBE';document.querySelector('#ask button[type=submit]').click()");
  await wait("window.__guideTestCalls.length===4");
  await evaluate("document.getElementById('cancel-guide').click()");
  await wait("document.getElementById('guide-status').textContent.includes('annulée')");
  await evaluate("document.getElementById('erase-local').click()");
  assert.equal(await evaluate("localStorage.getItem('privai-guide-conversation')"),null);
  assert.equal(await evaluate("localStorage.getItem('privai-guide-opt-in')"),null);
  assert(await evaluate("!!localStorage.getItem('capable-guide-conversation')"),"PrivAI purge must not erase Capable");
  console.log("MOBILE_INTERACTION_PASS",JSON.stringify({book:"privai",requests:4,migration:true,consent:true,erase:true,cancel:true}));
  await cdp("Emulation.setDeviceMetricsOverride",{width:1280,height:800,deviceScaleFactor:1,mobile:false});
  await visit("capable");
  const desktop=await evaluate("({innerWidth:innerWidth,bodyWidth:document.documentElement.scrollWidth,buttons:document.querySelectorAll('button').length})");
  assert(desktop.innerWidth>=1200);
  console.log("DESKTOP_RENDER_PASS",JSON.stringify(desktop));
  console.log("LIVING_BOOK_GUIDE_REAL_CHROMIUM_PASS",JSON.stringify({mobile:2,desktop:1,profileIsolation:true,legacyMigration:true,localConsent:true,sessionPurge:true,agentConsent:true,cancel:true}));
}finally{
  try{ws?.close()}catch{}
  if(chrome.exitCode===null)chrome.kill("SIGTERM");
  await Promise.race([
    new Promise(resolve=>{if(chrome.exitCode!==null)resolve();else chrome.once("exit",resolve);}),
    sleep(3500)
  ]);
  await new Promise(r=>server.close(r));
  fs.rmSync(dir,{recursive:true,force:true,maxRetries:8,retryDelay:150});
}

