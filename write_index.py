from pathlib import Path

html = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Universe Explorer</title>
  <meta name="description" content="An interactive universe showcase with featured space topics, live facts, and discovery cards." />
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css" rel="stylesheet" crossorigin="anonymous" />
  <link rel="stylesheet" href="style.css" />
  <link rel="shortcut icon" href="favicon_io (5)/android-chrome-192x192.png" type="image/x-icon" />
</head>
<body>
  <main class="site-shell">
    <header class="navbar-modern">
      <div class="brand-wrap">
        <div class="brand-mark" aria-hidden="true"></div>
        <div class="brand-copy">
          <h1>Universe Explorer</h1>
          <p>Interactive space discoveries, live facts, and launch sites.</p>
        </div>
      </div>
      <div class="nav-actions">
        <button id="themeToggle" class="theme-btn" type="button" aria-label="Toggle theme">☀️ Light mode</button>
        <a class="ghost-btn" href="#discover">Explore</a>
      </div>
    </header>

    <section class="hero-grid">
      <article class="hero-card glass-card">
        <span class="kicker">Live cosmic tour</span>
        <h2>See the universe in motion with a brighter, more interactive experience.</h2>
        <p>
          This updated page blends immersive visuals, quick facts, theme switching, a live clock,
          and searchable space content to make the website feel more alive and engaging.
        </p>
        <div class="hero-pills">
          <span class="pill">🌌 Galactic facts</span>
          <span class="pill">🔭 NASA links</span>
          <span class="pill">✨ Interactive cards</span>
        </div>
        <a class="glow-btn" href="#discover">Start exploring</a>
        <div class="stat-grid">
          <div class="stat-box"><strong>4</strong><span>Deep-space topics</span></div>
          <div class="stat-box"><strong>6</strong><span>Discovery cards</span></div>
          <div class="stat-box" id="timeLabel">--:--:--</div>
        </div>
      </article>

      <aside class="info-card glass-card">
        <div class="fact-box">
          <strong>Today’s fact</strong>
          <p id="factText">Loading a space fact…</p>
        </div>
        <div class="fact-box">
          <strong>What changed</strong>
          <p>The page now includes smooth visuals, stronger CSS, a theme toggle, live fact rotation, and search-based filtering for the content cards.</p>
        </div>
        <button id="factButton" class="glow-btn" type="button">Generate another fact</button>
      </aside>
    </section>

    <section class="section glass-card" id="discover">
      <div class="section-header">
        <div>
          <h3>Featured space highlights</h3>
          <p>Use the search box to quickly filter the topics you want to explore.</p>
        </div>
        <div class="filter-panel">
          <input id="searchInput" type="search" placeholder="Search for black holes, stars, universe…" aria-label="Search space topics" />
          <button class="ghost-btn" type="button" onclick="document.getElementById('searchInput').value=''; filterCards();">Reset</button>
        </div>
      </div>

      <div class="feature-grid">
        <article class="space-card" data-search="black hole gravity dark matter collapse">
          <img src="black hole.jpg" alt="Black hole illustration" />
          <div class="card-body">
            <h4>Black Holes</h4>
            <p>Gravity so powerful that even light cannot escape. These cosmic objects reveal how extreme physics shapes the universe.</p>
            <a href="https://science.nasa.gov/universe/black-holes/" target="_blank" rel="noreferrer">Read more →</a>
          </div>
        </article>

        <article class="space-card" data-search="stars fusion galaxies bright energy">
          <img src="stars.jpeg" alt="Stars in the night sky" />
          <div class="card-body">
            <h4>Stars</h4>
            <p>Stars create light and heat through nuclear fusion. They are the engines that build galaxies and shape the cosmos.</p>
            <a href="https://science.nasa.gov/universe/stars/" target="_blank" rel="noreferrer">Read more →</a>
          </div>
        </article>

        <article class="space-card" data-search="universe big bang expansion galaxies cosmic">
          <img src="uni.jpeg" alt="Universe image" />
          <div class="card-body">
            <h4>The Universe</h4>
            <p>Everything we know — space, time, matter, and energy — is expanding and still full of cosmic mysteries to uncover.</p>
            <a href="https://science.nasa.gov/universe/" target="_blank" rel="noreferrer">Read more →</a>
          </div>
        </article>

        <article class="space-card" data-search="exoplanets planets habitable zone life beyond earth">
          <img src="exoplanets.jpg" alt="Exoplanets illustration" />
          <div class="card-body">
            <h4>Exoplanets</h4>
            <p>Faraway worlds orbiting other stars. Some may sit in the habitable zone where liquid water could exist.</p>
            <a href="https://science.nasa.gov/exoplanets/" target="_blank" rel="noreferrer">Read more →</a>
          </div>
        </article>

        <article class="space-card" data-search="catalog planets data scientific research">
          <img src="e2.jpg" alt="Exoplanet catalog" />
          <div class="card-body">
            <h4>Exoplanet Catalog</h4>
            <p>Explore a continuously updated collection of confirmed planets and their scientific data from space missions.</p>
            <a href="https://science.nasa.gov/exoplanets/exoplanet-catalog/" target="_blank" rel="noreferrer">Read more →</a>
          </div>
        </article>

        <article class="space-card" data-search="habitable zone goldilocks liquid water life possible">
          <img src="habitable.jpg" alt="Habitable zone illustration" />
          <div class="card-body">
            <h4>Habitable Zone</h4>
            <p>Known as the Goldilocks zone, this region could be just right for liquid water and potentially life as we know it.</p>
            <a href="https://science.nasa.gov/exoplanets/habitable-zone/" target="_blank" rel="noreferrer">Read more →</a>
          </div>
        </article>
      </div>
    </section>

    <section class="section mission-grid">
      <article class="glass-card list-card">
        <h3>Why this version feels better</h3>
        <ul>
          <li>Custom CSS gives the page a polished, modern look.</li>
          <li>Interactive JavaScript adds live facts, a clock, and filtering.</li>
          <li>Better content organization makes the journey easier to scan.</li>
        </ul>
      </article>

      <article class="glass-card list-card">
        <h3>Quick launch highlights</h3>
        <p style="color: var(--muted);">Tap each center to reveal a quick description.</p>
        <div class="center-grid">
          <div class="center-card">
            <button type="button" data-bs-toggle="collapse" data-bs-target="#centerOne" aria-expanded="false">Kennedy Space Center</button>
            <div class="collapse collapse-body" id="centerOne">Florida’s iconic launch site for Apollo and the Artemis Moon program.</div>
          </div>
          <div class="center-card">
            <button type="button" data-bs-toggle="collapse" data-bs-target="#centerTwo" aria-expanded="false">ISRO</button>
            <div class="collapse collapse-body" id="centerTwo">India’s national space agency, leading satellites, missions, and space research from Bengaluru.</div>
          </div>
          <div class="center-card">
            <button type="button" data-bs-toggle="collapse" data-bs-target="#centerThree" aria-expanded="false">Tanegashima</button>
            <div class="collapse collapse-body" id="centerThree">Japan’s main spaceport focused on powerful launches and international satellite missions.</div>
          </div>
          <div class="center-card">
            <button type="button" data-bs-toggle="collapse" data-bs-target="#centerFour" aria-expanded="false">Vostochny</button>
            <div class="collapse collapse-body" id="centerFour">Russia’s modern cosmodrome built to support future launch and exploration missions.</div>
          </div>
        </div>
      </article>
    </section>

    <p class="footer-note">Updated for a more interactive, polished experience with HTML, CSS, and JavaScript.</p>
  </main>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/js/bootstrap.bundle.min.js" crossorigin="anonymous"></script>
  <script src="script.js"></script>
</body>
</html>
'''

Path('index.html').write_text(html, encoding='utf-8')
print('Updated index.html')
