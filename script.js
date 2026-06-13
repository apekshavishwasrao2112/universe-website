const facts = [
  'Artemis aims to return astronauts to the Moon and build the foundation for long-term lunar exploration.',
  'Mars missions are studying ancient riverbeds and rocks to understand whether life ever existed there.',
  'Europa Clipper will investigate whether Jupiter’s moon Europa has the ingredients for life.',
  'The James Webb Space Telescope is revealing distant stars, planets, and early galaxies with unprecedented detail.',
  'Launch sites such as Kennedy and Vostochny make modern deep-space missions possible every year.'
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
