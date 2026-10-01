/* ── Scheduler triggers ── */
async function loadTriggers(){
  try{
    const items=await apiFetch('/triggers');
    const list=document.getElementById('triggersList');
    if(!list||!items.length)return;
    list.innerHTML=items.map(t=>`
      <div class="tri"><div class="ti2" style="background:${t.icon_bg};color:${t.icon_color}">${t.icon}</div>
      <div><h5>${t.name}</h5><p>${t.detail}</p></div>
      <div class="ts2 ${t.active?'on':'off'}" onclick="toggleTrigger(${t.id},this)">${t.active?'ON':'PAUSED'}</div></div>`).join('');
  }catch(_){/* keep static fallback */}
}
async function toggleTrigger(id,el){
  const willActivate=!el.classList.contains('on');
  try{
    await apiFetch(`/triggers/${id}`,{method:'PATCH',body:JSON.stringify({active:willActivate})});
    el.classList.toggle('on',willActivate);el.classList.toggle('off',!willActivate);
    el.textContent=willActivate?'ON':'PAUSED';
  }catch(err){showToast('Could not update trigger: '+err.message)}
}
