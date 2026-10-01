function showToast(msg){
  const wrap=document.getElementById('toastWrap');
  const t=document.createElement('div');t.className='toast';t.textContent=msg;
  wrap.appendChild(t);
  requestAnimationFrame(()=>t.classList.add('show'));
  setTimeout(()=>{t.classList.remove('show');setTimeout(()=>t.remove(),300)},3200);
}

function openApiDocs(){
  const base=API_BASE.replace(/\/api\/?$/,'');
  window.open(base+'/docs','_blank');
}

function cmdAction(type){
  closeCmd();
  if(type==='builder')scrollSec('builder');
  else if(type==='ai')document.getElementById('chatI')?.scrollIntoView({behavior:'smooth',block:'center'});
  else if(type==='integrations')scrollSec('integrations');
  else if(type==='analytics')document.querySelector('.an-grid')?.scrollIntoView({behavior:'smooth',block:'center'});
  else if(type==='team')inviteTeammate();
}

function inviteTeammate(){
  if(!currentUser){showToast('Log in to invite teammates');openAuth('login');return}
  showToast('Invite link copied to clipboard 🔗');
}
