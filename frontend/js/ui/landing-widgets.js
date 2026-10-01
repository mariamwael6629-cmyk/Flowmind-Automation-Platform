function miniBar(id,data,color){
  const el=document.getElementById(id);if(!el)return;
  const mx=Math.max(...data);
  data.forEach(v=>{const b=document.createElement('div');b.className='mb';
    b.style.cssText=`height:${Math.round((v/mx)*100)}%;background:${color};opacity:${(0.35+(v/mx)*0.65).toFixed(2)}`;el.appendChild(b)})
}
miniBar('ce',[65,80,70,90,85,75,95,88,92,100,78,85],'var(--el)');
miniBar('cs',[98,99,97,100,99,100,98,100,99,100,98,99],'var(--em)');
miniBar('cr',[60,70,55,80,65,72,58,90,68,74,62,70],'var(--am)');
miniBar('cw',[70,75,80,72,85,88,80,82,90,86,88,92],'var(--el)');

const logData=[
  ['s','HubSpot lead enrichment'],['s','Stripe webhook processed'],['s','Email sequence fired'],
  ['w','OpenAI rate limit — queuing'],['s','GitHub PR → Jira ticket'],['s','Shopify order fulfilled'],
  ['e','Salesforce auth expired'],['s','Daily report sent'],['s','Airtable record updated'],['s','Slack alert fired']
];
let li=0;
setInterval(()=>{
  const log=document.getElementById('execLog');if(!log)return;
  const[t,n]=logData[li%logData.length];li++;
  const row=document.createElement('div');row.className='li';
  row.style.cssText='opacity:0;transition:opacity .4s';
  row.innerHTML=`<div class="ld ${t}"></div><div class="ln">${n}</div><div class="lt">just now</div>`;
  log.prepend(row);setTimeout(()=>row.style.opacity='1',40);
  if(log.children.length>6)log.removeChild(log.lastChild);
},2800);

function faq(i){
  const a=document.getElementById('fa'+i),ic=document.getElementById('fi'+i);
  const open=a.classList.contains('open');
  document.querySelectorAll('.fq-a').forEach(x=>x.classList.remove('open'));
  document.querySelectorAll('.fq-icon').forEach(x=>{x.classList.remove('open');x.textContent='+'});
  if(!open){a.classList.add('open');ic.classList.add('open')}
}
