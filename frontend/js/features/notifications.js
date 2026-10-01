/* ── Notifications ── */
async function loadNotifications(){
  try{
    const items=await apiFetch('/notifications');
    const panel=document.getElementById('notifPanel');
    const body=items.map(n=>`<div class="ni"><div class="ni-ic" style="background:${n.icon_bg};color:${n.icon_color}">${n.icon}</div><div><p>${n.message}</p><time>${n.time_ago}</time></div></div>`).join('');
    panel.innerHTML=`<div class="np-head"><span class="np-title">Notifications</span><span class="np-clear" onclick="markAllRead()">Mark all read</span></div>`+body;
    const unread=items.filter(n=>!n.read).length;
    const dot=document.getElementById('notifDot');
    if(dot)dot.style.display=unread>0?'block':'none';
  }catch(_){/* keep static fallback */}
}
async function markAllRead(){
  try{await apiFetch('/notifications/mark-read',{method:'PATCH'});await loadNotifications();showToast('All notifications marked read')}
  catch(_){closeNotif()}
}
