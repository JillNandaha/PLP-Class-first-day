const lightBtn = document.getElementById('lightBtn');
const darkBtn = document.getElementById('darkBtn');
const box = document.getElementById('animatedBox');

// Function to set theme and store in localStorage
function setTheme(theme) {
  document.body.style.backgroundColor = theme === 'dark' ? '#222' : '#fff';
  document.body.style.color = theme === 'dark' ? '#fff' : '#000';

  // Save to localStorage
  localStorage.setItem('preferredTheme', theme);

  // Trigger animation
  box.classList.remove('bounce');
  void box.offsetWidth; // Trick to re-trigger animation
  box.classList.add('bounce');
}

// Event Listeners
lightBtn.addEventListener('click', () => setTheme('light'));
darkBtn.addEventListener('click', () => setTheme('dark'));

// On load, apply stored theme
window.addEventListener('DOMContentLoaded', () => {
  const savedTheme = localStorage.getItem('preferredTheme');
  if (savedTheme) setTheme(savedTheme);
});
