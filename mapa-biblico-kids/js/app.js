/* ===================================================================
   App principal — monta o livro inteiro dentro de #book.
=================================================================== */

const STORAGE_KEY = "mbk_passport_v1";

function loadProgress() {
  try { return JSON.parse(localStorage.getItem(STORAGE_KEY)) || {}; }
  catch (e) { return {}; }
}
function saveProgress(p) {
  try { localStorage.setItem(STORAGE_KEY, JSON.stringify(p)); } catch (e) {}
}

function iconSVGSmall(kind, size = 56) {
  return `<svg viewBox="0 0 100 100" width="${size}" height="${size}">${ICONS[kind] ? ICONS[kind]() : ""}</svg>`;
}

function stickerTitle(text, small = false) {
  const chars = text.split("");
  const spans = chars.map(ch => ch === " "
    ? `<span class="sp" style="background:none;border:none;box-shadow:none;width:10px;padding:0"></span>`
    : `<span>${ch}</span>`).join("");
  return `<div class="sticker-title${small ? " small" : ""}">${spans}</div>`;
}

function infoBox(label, text) {
  return `<div class="info-box"><span class="info-label">${label}</span><p>${text}</p></div>`;
}

function bookSceneHTML(book) {
  const s = SECTIONS[book.section];
  return scene(book.icons, { bg: s.bg, ground: s.ground });
}

const ACTIVITY_META = {
  maze: { emoji: "🧩", label: "Labirinto" },
  wordsearch: { emoji: "🔎", label: "Caça-palavras" },
  quiz: { emoji: "❓", label: "Circule a resposta" },
  circle: { emoji: "⭕", label: "Circule a resposta" },
  truefalse: { emoji: "✅", label: "Verdadeiro ou Falso" },
  match: { emoji: "🔗", label: "Ligue as colunas" },
  associate: { emoji: "🔗", label: "Associação" },
  count: { emoji: "🔢", label: "Encontre e conte" },
  findobjects: { emoji: "🔢", label: "Encontre e conte" },
  fill: { emoji: "✏️", label: "Complete a frase" },
  complete: { emoji: "✏️", label: "Complete a frase" },
  sequence: { emoji: "🔁", label: "Coloque em ordem" },
  draw: { emoji: "🎨", label: "Desenhe" },
  challenge: { emoji: "⭐", label: "Desafio" },
  game: { emoji: "⭐", label: "Desafio" },
};

function activityBoxHTML(seed, activity) {
  const meta = ACTIVITY_META[activity.type] || { emoji: "⭐", label: "Atividade" };
  return `<div class="activity-box">
    <span class="activity-badge">${meta.emoji} ${meta.label}</span>
    ${renderActivity(seed, activity)}
  </div>`;
}

let PAGE_COUNTER = 0;
function pageShell(inner, { sectionLabel = "", extraClass = "" } = {}) {
  PAGE_COUNTER++;
  return `<section class="page ${extraClass}" id="p-${PAGE_COUNTER}">
    ${sectionLabel ? `<span class="section-tag">${sectionLabel}</span>` : ""}
    ${inner}
    <span class="page-number">${PAGE_COUNTER}</span>
  </section>`;
}

/* ---------------- construção das páginas ---------------- */

function buildCover() {
  return pageShell(`
    <div class="cover-page">
      ${stickerTitle("MAPA BÍBLICO KIDS")}
      <div class="cover-illustration">${scene(["sun", "tree", "ark"], { bg: "#BEE3F8", ground: "#CDEAC0" })}</div>
      <p class="cover-sub">Uma jornada divertida pelos 66 livros da Bíblia!</p>
      <span class="cover-badge">📖 Do Gênesis ao Apocalipse ✨</span>
    </div>`, { sectionLabel: "Capa" });
}

function buildSimplePage(title, body, icons, sectionLabel) {
  return pageShell(`
    <div class="book-header">${stickerTitle(title, true)}</div>
    ${icons ? `<div style="max-width:340px;margin:10px auto;">${scene(icons, { bg: "#FFF6E5", ground: "#E9F7EF" })}</div>` : ""}
    <div class="info-box"><p style="font-size:1.05rem">${body}</p></div>
  `, { sectionLabel });
}

function buildLegendPage(page) {
  const items = Object.values(ACTIVITY_META).filter((v, i, arr) => arr.findIndex(x => x.label === v.label) === i);
  return pageShell(`
    <div class="book-header">${stickerTitle(page.title, true)}</div>
    <p style="text-align:center">${page.body}</p>
    <div class="legend-grid">
      ${items.map(it => `<div class="legend-item"><span class="legend-emoji">${it.emoji}</span><span>${it.label}</span></div>`).join("")}
    </div>
  `, { sectionLabel: "Como usar" });
}

function buildTrailPage() {
  const stops = [
    { icon: "sun", label: "Criação" }, { icon: "ark", label: "Noé" }, { icon: "tablets", label: "Moisés" },
    { icon: "crown", label: "Reis" }, { icon: "scroll", label: "Profetas" }, { icon: "manger", label: "Jesus nasce" },
    { icon: "cross", label: "Jesus salva" }, { icon: "dove", label: "Igreja" }, { icon: "rainbow", label: "Promessa final" },
  ];
  return pageShell(`
    <div class="book-header">${stickerTitle("A GRANDE JORNADA", true)}</div>
    <p style="text-align:center">A Bíblia inteira é uma grande história, do começo ao fim. Siga a trilha!</p>
    <div class="trail-wrap">
      ${stops.map((s, i) => `<div class="trail-stop"><div class="trail-icon">${iconSVGSmall(s.icon, 60)}</div><span class="trail-label">${s.label}</span></div>${i < stops.length - 1 ? '<div class="trail-dash"></div>' : ""}`).join("")}
    </div>
    <div class="two-col" style="margin-top:26px">
      <div class="info-box"><span class="info-label">📜 Antigo Testamento</span><p>39 livros — do começo do mundo até a espera pelo Salvador.</p></div>
      <div class="info-box"><span class="info-label">✝️ Novo Testamento</span><p>27 livros — a vida de Jesus e o começo da igreja.</p></div>
    </div>
  `, { sectionLabel: "Mapa da Bíblia" });
}

function buildSectionMapPage(title, entries, sectionLabel) {
  return pageShell(`
    <div class="book-header">${stickerTitle(title, true)}</div>
    ${entries.map(e => {
      const s = SECTIONS[e.key];
      return `<div class="section-map-item" style="border-color:${s.accent}">
        <h3 style="color:${s.accent}">${s.label}</h3>
        <p class="books-list">${e.books}</p>
        <p>${e.text}</p>
      </div>`;
    }).join("")}
  `, { sectionLabel });
}

function buildDividerPage(title, sub, icons) {
  return pageShell(`
    <div class="cover-page">
      ${stickerTitle(title)}
      <div class="cover-illustration">${scene(icons, { bg: "#EDE7F6", ground: "#D8CCF0" })}</div>
      <p class="cover-sub">${sub}</p>
    </div>
  `, { sectionLabel: "Divisor" });
}

function buildBookPage(book) {
  const s = SECTIONS[book.section];
  return pageShell(`
    <span id="book-${book.id}" style="position:absolute;top:0"></span>
    <div class="book-header">
      <span class="book-number-badge">Livro ${book.n} de 66 • ${book.test === "AT" ? "Antigo Testamento" : "Novo Testamento"} • ${s.label}</span>
      ${stickerTitle(book.name.toUpperCase(), true)}
    </div>
    <div class="two-col">
      <div>
        ${bookSceneHTML(book)}
      </div>
      <div>
        ${infoBox("💡 Você sabia?", book.sabia)}
        ${infoBox("🎯 Tema principal", book.tema)}
      </div>
    </div>
    ${activityBoxHTML(book.id, book.activity)}
  `, { sectionLabel: s.label });
}

function buildBookExtraPage(book) {
  const s = SECTIONS[book.section];
  return pageShell(`
    <div class="book-header">
      <span class="book-number-badge">Mais uma aventura em ${book.name}!</span>
      ${stickerTitle(book.name.toUpperCase() + " +", true)}
    </div>
    <div style="max-width:320px;margin:8px auto;">${scene(book.extra.icons, { bg: s.bg, ground: s.ground })}</div>
    ${activityBoxHTML(book.id + "-extra", book.extra.activity)}
  `, { sectionLabel: s.label });
}

function buildExtraGamePage(game, i) {
  return pageShell(`
    <div class="book-header">
      <span class="book-number-badge">Jogo Extra</span>
      ${stickerTitle(game.title, true)}
    </div>
    <div style="max-width:300px;margin:8px auto;">${scene(game.icons, { bg: "#FFF6E5", ground: "#E9F7EF" })}</div>
    ${activityBoxHTML("extra-" + i, game.activity)}
  `, { sectionLabel: "Jogos Extras" });
}

function buildColoringPage(page) {
  return pageShell(`
    <div class="book-header">${stickerTitle(page.title, true)}</div>
    <div class="coloring-wrap">${coloringScene(page.icons)}</div>
    <p class="activity-prompt center">Capriche nas cores! 🎨</p>
  `, { sectionLabel: "Para Colorir" });
}

function buildChallengePage(c) {
  return pageShell(`
    <div class="challenge-card">
      <div style="font-size:2.6rem">🏆</div>
      <div class="big">${c.text}</div>
      <p class="sub">${c.sub}</p>
    </div>
  `, { sectionLabel: "Desafio" });
}

function buildPassportPages() {
  const progress = loadProgress();
  const chunkSize = 22;
  const chunks = [];
  for (let i = 0; i < BIBLE_BOOKS.length; i += chunkSize) chunks.push(BIBLE_BOOKS.slice(i, i + chunkSize));
  return chunks.map((chunk, ci) => pageShell(`
    <div class="book-header">${stickerTitle(ci === 0 ? "MEU PASSAPORTE BÍBLICO" : "PASSAPORTE (continuação)", true)}</div>
    ${ci === 0 ? `<p style="text-align:center">Marque cada livro que você já conheceu nesta jornada!</p>` : ""}
    <div class="passport-grid">
      ${chunk.map(b => `<div class="passport-item"><span class="passport-num">${b.n}.</span>
        <span class="passport-check${progress[b.id] ? " checked" : ""}" data-id="${b.id}"></span> ${b.name}</div>`).join("")}
    </div>
  `, { sectionLabel: "Passaporte" })).join("");
}

function buildCertificate() {
  return pageShell(`
    <div class="certificate">
      <div style="font-size:2.4rem">🎉📖🏆</div>
      <div class="cert-title">Certificado de Explorador(a) da Bíblia</div>
      <p>Este certificado comprova que</p>
      <div class="cert-line"></div>
      <p class="cert-name-label">conheceu os 66 livros da Bíblia, do Gênesis ao Apocalipse!</p>
      <div class="cert-line" style="width:40%;margin-top:40px"></div>
      <p class="cert-name-label">Data</p>
    </div>
  `, { sectionLabel: "Certificado" });
}

/* ---------------- montagem final ---------------- */

function buildBook() {
  const parts = [];
  parts.push(buildCover());
  INTRO_PAGES.slice(1).forEach(p => parts.push(buildSimplePage(p.title, p.body, p.icons, "Introdução")));
  HOWTO_PAGES.forEach(p => parts.push(p.legend ? buildLegendPage(p) : buildSimplePage(p.title, p.body, p.icons, "Como usar")));
  parts.push(buildTrailPage());

  parts.push(buildDividerPage("ANTIGO TESTAMENTO", "39 livros — do começo do mundo até a promessa de um Salvador.", ["sun", "tree", "tablets"]));
  parts.push(buildSectionMapPage("Como o Antigo Testamento é dividido?", AT_SECTIONS_MAP.slice(0, 3), "Mapa do AT"));
  parts.push(buildSectionMapPage("Como o Antigo Testamento é dividido? (parte 2)", AT_SECTIONS_MAP.slice(3), "Mapa do AT"));

  const atBooks = BIBLE_BOOKS.filter(b => b.test === "AT");
  atBooks.forEach(b => { parts.push(buildBookPage(b)); if (b.extra) parts.push(buildBookExtraPage(b)); });

  parts.push(buildDividerPage("NOVO TESTAMENTO", "27 livros — a vida de Jesus e o início da igreja.", ["manger", "cross", "dove"]));
  parts.push(buildSectionMapPage("Como o Novo Testamento é dividido?", NT_SECTIONS_MAP.slice(0, 2), "Mapa do NT"));
  parts.push(buildSectionMapPage("Como o Novo Testamento é dividido? (parte 2)", NT_SECTIONS_MAP.slice(2), "Mapa do NT"));

  const ntBooks = BIBLE_BOOKS.filter(b => b.test === "NT");
  ntBooks.forEach(b => { parts.push(buildBookPage(b)); if (b.extra) parts.push(buildBookExtraPage(b)); });

  parts.push(buildDividerPage("JOGOS EXTRAS", "Mais desafios e brincadeiras pela Bíblia toda!", ["star", "road"]));
  EXTRA_GAMES.forEach((g, i) => parts.push(buildExtraGamePage(g, i)));

  parts.push(buildDividerPage("PÁGINAS PARA COLORIR", "Capriche nas cores dessas cenas bíblicas!", ["rainbow", "sun"]));
  COLORING_PAGES.forEach(p => parts.push(buildColoringPage(p)));

  parts.push(buildDividerPage("DESAFIOS E CONQUISTAS", "Celebre cada etapa da sua jornada!", ["crown", "star"]));
  CHALLENGE_PAGES.forEach(c => parts.push(buildChallengePage(c)));

  parts.push(buildDividerPage("MEU PASSAPORTE BÍBLICO", "Marque cada livro conhecido nessa grande aventura!", ["scroll", "road"]));
  parts.push(buildPassportPages());

  parts.push(buildCertificate());

  document.getElementById("book").innerHTML = parts.join("");
  buildTOC();
  attachPassportEvents();
  updateProgressUI();
}

function buildTOC() {
  const toc = document.getElementById("toc");
  const select = document.getElementById("jump-select");
  const groups = [
    { label: "Antigo Testamento", items: BIBLE_BOOKS.filter(b => b.test === "AT") },
    { label: "Novo Testamento", items: BIBLE_BOOKS.filter(b => b.test === "NT") },
  ];
  let html = `<h4>Início</h4><a href="#p-1">Capa</a>`;
  let options = `<option value="">Ir para o livro...</option>`;
  groups.forEach(g => {
    html += `<h4>${g.label}</h4>`;
    options += `<optgroup label="${g.label}">`;
    g.items.forEach(b => {
      html += `<a href="#book-${b.id}">${b.n}. ${b.name}</a>`;
      options += `<option value="#book-${b.id}">${b.n}. ${b.name}</option>`;
    });
    options += `</optgroup>`;
  });
  toc.innerHTML = html;
  if (select) select.innerHTML = options;
}

function attachPassportEvents() {
  document.querySelectorAll(".passport-check").forEach(el => {
    el.addEventListener("click", () => {
      const progress = loadProgress();
      const id = el.dataset.id;
      progress[id] = !progress[id];
      saveProgress(progress);
      el.classList.toggle("checked", !!progress[id]);
      updateProgressUI();
    });
  });
}

function updateProgressUI() {
  const progress = loadProgress();
  const count = Object.values(progress).filter(Boolean).length;
  const label = document.getElementById("progress-label");
  const bar = document.getElementById("progress-fill");
  if (label) label.textContent = `${count}/66 livros`;
  if (bar) bar.style.width = `${Math.round((count / 66) * 100)}%`;
}

document.addEventListener("DOMContentLoaded", () => {
  buildBook();
  document.getElementById("print-btn").addEventListener("click", () => window.print());
  document.getElementById("jump-select").addEventListener("change", (e) => {
    if (e.target.value) location.hash = e.target.value;
  });
});
