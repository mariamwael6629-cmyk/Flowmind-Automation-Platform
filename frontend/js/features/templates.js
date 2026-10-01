/* ── Templates ── */
async function loadTemplates(all){
  try{
    const items=await apiFetch('/templates'+(all?'?limit=100':''));
    const grid=document.querySelector('.tpl-grid');
    if(!grid||!items.length)return;
    const tagClass={popular:'p','new':'n',ai:'a'};
    grid.innerHTML=items.map(t=>`
      <div class="tc"><span class="tt ${tagClass[t.category]||'p'}">${t.category}</span><h4>${t.title}</h4><p>${t.description}</p>
      <div class="tnodes">${t.tags.map(tg=>`<span class="tn">${tg}</span>`).join('')}</div></div>`).join('');
  }catch(_){/* keep static fallback */}
}
