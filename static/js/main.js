/**
 * Plastic Reimagined — Core Client-Side Utilities
 * Vanilla JavaScript (No heavy frameworks, highly optimized)
 */

document.addEventListener('DOMContentLoaded', () => {
  initMobileNavigation();
  initAlertDismissals();
  logPlatformFoundationReady();
});

/**
 * Responsive Mobile Navigation Drawer Toggle
 */
function initMobileNavigation() {
  const toggleBtn = document.getElementById('mobileNavToggle');
  const mainNav = document.getElementById('mainNav');

  if (!toggleBtn || !mainNav) return;

  toggleBtn.addEventListener('click', () => {
    const isExpanded = toggleBtn.getAttribute('aria-expanded') === 'true';
    toggleBtn.setAttribute('aria-expanded', String(!isExpanded));
    mainNav.classList.toggle('is-open', !isExpanded);
  });

  // Close mobile nav on escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && mainNav.classList.contains('is-open')) {
      mainNav.classList.remove('is-open');
      toggleBtn.setAttribute('aria-expanded', 'false');
      toggleBtn.focus();
    }
  });
}

/**
 * Dismissible alert messages
 */
function initAlertDismissals() {
  const alertDismissButtons = document.querySelectorAll('[data-dismiss-alert]');
  alertDismissButtons.forEach((btn) => {
    btn.addEventListener('click', () => {
      const alert = btn.closest('.alert');
      if (alert) {
        alert.style.transition = 'opacity 200ms ease, transform 200ms ease';
        alert.style.opacity = '0';
        alert.style.transform = 'translateY(-6px)';
        setTimeout(() => alert.remove(), 200);
      }
    });
  });
}

/**
 * Architecture readiness logging
 */
function logPlatformFoundationReady() {
  console.info(
    '%c🌿 Plastic Reimagined %c— Production Foundation Initialized',
    'background: #10b981; color: #04211b; font-weight: bold; padding: 4px 8px; border-radius: 4px;',
    'color: #34d399; font-weight: 500;'
  );
}
