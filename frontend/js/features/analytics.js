/* ── Analytics ── */
async function loadAnalytics(){
  try{
    const d=await apiFetch('/analytics/overview');
    const cards=document.querySelectorAll('.an-grid .anc .an-val');
    if(cards.length>=4){
      cards[0].textContent=d.time_saved;
      cards[1].textContent=d.tasks_automated.toLocaleString();
      cards[2].textContent=d.cost_saved;
      cards[3].textContent=d.error_rate+'%';
    }
  }catch(_){/* keep static fallback */}
}
