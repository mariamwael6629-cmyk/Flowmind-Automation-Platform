/* ── Auth ── */
let authMode='login';
function openAuth(mode){
  setAuthTab(mode);
  document.getElementById('authBg').classList.add('open');
}
function closeAuth(){document.getElementById('authBg').classList.remove('open')}
function setAuthTab(mode){
  authMode=mode;
  document.getElementById('tabLogin').classList.toggle('active',mode==='login');
  document.getElementById('tabSignup').classList.toggle('active',mode==='signup');
  document.getElementById('nameField').style.display=mode==='signup'?'block':'none';
  document.getElementById('authSubmitBtn').textContent=mode==='signup'?'Create account':'Log In';
  document.getElementById('authErr').style.display='none';
}
async function submitAuth(e){
  e.preventDefault();
  const errEl=document.getElementById('authErr');
  errEl.style.display='none';
  const email=document.getElementById('authEmail').value.trim();
  const password=document.getElementById('authPassword').value;
  const name=document.getElementById('authName').value.trim();
  const btn=document.getElementById('authSubmitBtn');
  btn.disabled=true;
  try{
    if(authMode==='signup'){
      await apiFetch('/auth/signup',{method:'POST',body:JSON.stringify({email,password,full_name:name||email.split('@')[0]})});
    }
    const data=await apiFetch('/auth/login',{method:'POST',body:JSON.stringify({email,password})});
    authToken=data.access_token;
    localStorage.setItem('fm_token',authToken);
    await refreshAuthUI();
    closeAuth();
    showToast(authMode==='signup'?'Welcome to FlowMind! 🎉':'Welcome back!');
    document.getElementById('authForm').reset();
  }catch(err){
    errEl.textContent=err.message||'Something went wrong';
    errEl.style.display='block';
  }finally{
    btn.disabled=false;
  }
}
function logout(){
  authToken=null;currentUser=null;
  localStorage.removeItem('fm_token');
  refreshAuthUI();
  showToast('Logged out');
}
async function refreshAuthUI(){
  const slot=document.getElementById('navAuthSlot');
  if(!authToken){
    currentUser=null;
    slot.innerHTML='<button class="btn-p" onclick="openAuth(\'signup\')">Get Started Free</button>';
    return;
  }
  try{
    currentUser=await apiFetch('/auth/me');
    const initials=(currentUser.full_name||currentUser.email).split(/\s+/).map(w=>w[0]).join('').slice(0,2).toUpperCase();
    slot.innerHTML=`<div class="user-chip" onclick="logout()" title="Click to log out"><div class="ua">${initials}</div>${currentUser.full_name||currentUser.email}</div>`;
  }catch(_){
    authToken=null;localStorage.removeItem('fm_token');
    slot.innerHTML='<button class="btn-p" onclick="openAuth(\'signup\')">Get Started Free</button>';
  }
}
