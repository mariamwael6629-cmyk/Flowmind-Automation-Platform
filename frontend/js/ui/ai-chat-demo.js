const replies=[
  "Built! 4 steps: Typeform trigger → AI enrichment → HubSpot create → Slack notify. Estimated 3 min saved per lead. Activate?",
  "Done! I parallelised steps 3 & 4 for 40% faster execution. Also added a retry handler on the CRM step. Review it?",
  "Generated! I added error handling and a Slack alert if any step fails. Want me to add an analytics step too?",
  "Great idea — I found a matching template and customised it for your stack. 6 nodes, ~1.1s avg runtime. Deploy now?"
];
let ri=0;
function sendChat(){
  const i=document.getElementById('chatI'),m=document.getElementById('chatMsgs');
  const text=i.value.trim();
  if(!text)return;
  const um=document.createElement('div');um.className='mu';um.textContent=text;m.appendChild(um);
  const tm=document.createElement('div');tm.className='ma';
  tm.innerHTML='<div class="typing"><div class="td"></div><div class="td"></div><div class="td"></div></div>';
  m.appendChild(tm);i.value='';m.scrollTop=m.scrollHeight;
  apiFetch('/ai/chat',{method:'POST',body:JSON.stringify({message:text})})
    .then(data=>{tm.innerHTML=data.reply;m.scrollTop=m.scrollHeight;})
    .catch(()=>{setTimeout(()=>{tm.innerHTML=replies[ri%replies.length];ri++;m.scrollTop=m.scrollHeight;},900);});
}
