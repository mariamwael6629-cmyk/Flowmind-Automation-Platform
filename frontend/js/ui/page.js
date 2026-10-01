function scrollSec(id){const el=document.getElementById(id);if(el)el.scrollIntoView({behavior:'smooth',block:'start'})}
function toggleTheme(){document.body.style.filter=document.body.style.filter?'':'invert(0.05) hue-rotate(6deg)'}

const obs=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting)e.target.classList.add('visible')})},{threshold:.12});
document.querySelectorAll('.reveal').forEach(el=>obs.observe(el));

document.addEventListener('click',e=>{
  const np=document.getElementById('notifPanel');
  if(np.classList.contains('open')&&!np.contains(e.target)&&!document.getElementById('bellBtn').contains(e.target))
    np.classList.remove('open');
});

function toggleMobileMenu(){document.getElementById('mobileMenu').classList.toggle('open')}
