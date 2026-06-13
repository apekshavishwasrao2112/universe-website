const facts = [
  'The universe is still expanding, and galaxies are moving farther apart every second.',
  'A black hole can bend light so strongly that it acts like a cosmic lens.',
  'Some exoplanets orbit in the habitable zone, where liquid water could exist.',
  'Stars are born in giant clouds of gas and dust called nebulae.',
  'Our Sun is a medium-sized star, but it appears huge because it is so close to Earth.'
];

const themeToggle = document.getElementById('themeToggle');
const timeLabel = document.getElementById('timeLabel');
const factText = document.getElementById('factText');
const factButton = document.getElementById('factButton');
const searchInput = document.getElementById('searchInput');
const cards = document.querySelectorAll('.space-card');

function randomFact() {
  const index = Math.floor(Math.random() * facts.length);
  factText.textContent = facts[index];
}

function updateTime() {
  const now = new Date();
  timeLabel.textContent = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
}

function setTheme(mode) {
  document.documentElement.classList.toggle('light-theme', mode === 'light');
  localStorage.setItem('universe-theme', mode);
  themeToggle.textContent = mode === 'light' ? '🌙 Dark mode' : '☀️ Light mode';
}

function initTheme() {
  const saved = localStorage.getItem('universe-theme');
  setTheme(saved || 'dark');
}

function filterCards() {
  const query = searchInput.value.trim().toLowerCase();
  cards.forEach((card) => {
    const text = card.dataset.search || card.textContent.toLowerCase();
    card.style.display = text.includes(query) ? '' : 'none';
  });
}

if (themeToggle) {
  themeToggle.addEventListener('click', () => {
    const next = document.documentElement.classList.contains('light-theme') ? 'dark' : 'light';
    setTheme(next);
  });
}

if (factButton) {
  factButton.addEventListener('click', randomFact);
}

if (searchInput) {
  searchInput.addEventListener('input', filterCards);
}

updateTime();
setInterval(updateTime, 1000);
initTheme();
randomFact();
filterCards();

cards.forEach((card) => {
  card.addEventListener('mouseenter', () => {
    card.classList.add('active-card');
  });
  card.addEventListener('mouseleave', () => {
    card.classList.remove('active-card');
  });
});
