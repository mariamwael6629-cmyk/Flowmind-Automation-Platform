/* ── Init ── */
document.addEventListener('DOMContentLoaded',()=>{
  refreshAuthUI();
  loadTemplates(false);
  loadIntegrations();
  loadMonitoring();
  loadAnalytics();
  loadNotifications();
  loadTriggers();
  pollExecutions();
  setInterval(pollExecutions,6000);
  setInterval(loadMonitoring,15000);
});
