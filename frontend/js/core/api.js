/* ───────────────────────── BACKEND INTEGRATION ───────────────────────── */
const API_BASE=window.FLOWMIND_API_BASE||'http://localhost:8000/api';
let authToken=localStorage.getItem('fm_token')||null;
let currentUser=null;

async function apiFetch(path,opts={}){
  const headers=Object.assign({'Content-Type':'application/json'},opts.headers||{});
  if(authToken)headers['Authorization']='Bearer '+authToken;
  const res=await fetch(API_BASE+path,Object.assign({},opts,{headers}));
  if(!res.ok){
    let detail='Request failed';
    try{const j=await res.json();detail=j.detail||detail}catch(_){}
    throw new Error(detail);
  }
  if(res.status===204)return null;
  return res.json();
}
