/* ── Save demo workflow ── */
async function saveDemoWorkflow(){
  if(!currentUser){openAuth('signup');showToast('Log in to save workflows');return}
  try{
    await apiFetch('/workflows',{method:'POST',body:JSON.stringify({
      name:'Product Launch Automation',
      description:'Webhook → GPT-4o → Branch → Delay/Slack → HubSpot',
      status:'draft',
      nodes:[{type:'trigger',label:'Webhook'},{type:'ai',label:'GPT-4o'},{type:'logic',label:'Branch'},
             {type:'action',label:'Wait 1hr'},{type:'action',label:'Slack'},{type:'action',label:'HubSpot'}]
    })});
    document.getElementById('builderStatus').textContent='● Saved';
    showToast('Workflow saved to your account ✅');
  }catch(err){showToast('Could not save: '+err.message)}
}
