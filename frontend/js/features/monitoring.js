/* ── Monitoring ── */
async function loadMonitoring(){
  try{
    const d=await apiFetch('/analytics/monitoring');
    const set=(sel,val)=>{const el=document.querySelector(sel);if(el)el.textContent=val};
    set('.mon-grid .mc:nth-child(1) .mv',d.executions_today.toLocaleString());
    set('.mon-grid .mc:nth-child(2) .mv',d.success_rate+'%');
    set('.mon-grid .mc:nth-child(3) .mv',d.avg_response+'s');
    set('.mon-grid .mc:nth-child(4) .mv',d.active_workflows);
    ['ce','cs','cr','cw'].forEach(id=>{const el=document.getElementById(id);if(el)el.innerHTML=''});
    miniBar('ce',d.sparklines.executions,'var(--el)');
    miniBar('cs',d.sparklines.success,'var(--em)');
    miniBar('cr',d.sparklines.response,'var(--am)');
    miniBar('cw',d.sparklines.workflows,'var(--el)');
  }catch(_){/* keep static fallback */}
}

async function pollExecutions(){
  try{
    const items=await apiFetch('/executions/recent?limit=6');
    const log=document.getElementById('execLog');
    if(!log||!items.length)return;
    log.innerHTML=items.map(it=>`<div class="li"><div class="ld ${it.status}"></div><div class="ln">${it.message}</div><div class="lt">${it.time_ago}</div></div>`).join('');
  }catch(_){/* local simulation continues */}
}
