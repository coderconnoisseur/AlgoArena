
// Dark mode functionality
function initDarkMode() {
  const darkModeToggle = document.getElementById('darkModeToggle');
  
  // Check for saved theme preference or default to system preference
  const savedTheme = localStorage.getItem('theme');
  const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  
  let isDark = false;
  if (savedTheme) {
    isDark = savedTheme === 'dark';
  } else {
    isDark = systemPrefersDark;
  }
  
  // Apply initial theme
  updateTheme(isDark);
  if (darkModeToggle) {
    darkModeToggle.checked = isDark;
  }
  
  // Add event listener for toggle
  if (darkModeToggle) {
    darkModeToggle.addEventListener('change', function() {
      const newIsDark = this.checked;
      updateTheme(newIsDark);
      localStorage.setItem('theme', newIsDark ? 'dark' : 'light');
    });
  }
}

function updateTheme(isDark) {
  if (isDark) {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
  initDarkMode();
  
  // Add smooth scrolling for anchor links
  const links = document.querySelectorAll('a[href^="#"]');
  links.forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
  
  // Add animation on scroll (optional enhancement)
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };
  
  const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.animationPlayState = 'running';
      }
    });
  }, observerOptions);
  
  // Observe elements with animation classes
  const animatedElements = document.querySelectorAll('.animate-fade-in, .animate-slide-up, .animate-scale-in');
  animatedElements.forEach(el => {
    el.style.animationPlayState = 'paused';
    observer.observe(el);
  });
});

// System theme change listener
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) {
  // Only auto-update if user hasn't manually set a preference
  if (!localStorage.getItem('theme')) {
    updateTheme(e.matches);
    const darkModeToggle = document.getElementById('darkModeToggle');
    if (darkModeToggle) {
      darkModeToggle.checked = e.matches;
    }
  }
});
