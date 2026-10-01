/* ── Integrations ── */
async function loadIntegrations(){
  try{
    const items=await apiFetch('/integrations');
    const grid=document.querySelector('.int-grid');
    if(!grid||!items.length)return;
    grid.innerHTML=items.map(i=>`<div class="ic"><div class="icd" style="background:${i.color}"></div>${i.name}</div>`).join('')
      +'<div class="ic" style="border-color:rgba(88,130,255,.3);color:var(--el)"><span style="font-weight:700">+ 482 more →</span></div>';
  }catch(_){/* keep static fallback */}
}
