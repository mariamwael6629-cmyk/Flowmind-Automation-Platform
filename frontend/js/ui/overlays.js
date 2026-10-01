function toggleCmd(){
  const b=document.getElementById('cmdBg');
  b.classList.toggle('open');
  if(b.classList.contains('open'))setTimeout(()=>document.getElementById('cmdInp').focus(),50);
}
function closeCmd(){document.getElementById('cmdBg').classList.remove('open')}
document.addEventListener('keydown',e=>{if((e.metaKey||e.ctrlKey)&&e.key==='k'){e.preventDefault();toggleCmd()}});

function toggleNotif(){document.getElementById('notifPanel').classList.toggle('open')}
function closeNotif(){document.getElementById('notifPanel').classList.remove('open')}
