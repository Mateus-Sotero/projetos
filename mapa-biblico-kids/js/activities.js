/* ===================================================================
   Renderizadores de atividades — cada função devolve uma string HTML
   pronta para entrar num bloco .activity-box.
=================================================================== */

function seededRandom(seedStr) {
  let h = 1779033703 ^ seedStr.length;
  for (let i = 0; i < seedStr.length; i++) {
    h = Math.imul(h ^ seedStr.charCodeAt(i), 3432918353);
    h = (h << 13) | (h >>> 19);
  }
  return function () {
    h = Math.imul(h ^ (h >>> 16), 2246822507);
    h = Math.imul(h ^ (h >>> 13), 3266489909);
    h ^= h >>> 16;
    return (h >>> 0) / 4294967296;
  };
}

function shuffle(arr, rnd) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(rnd() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

/* ---------- 1. Labirinto ---------- */
function renderMaze(seed, { cols = 9, rows = 7, prompt = "Ajude o personagem a encontrar o caminho!", startIcon = "person", endIcon = "star" } = {}) {
  const rnd = seededRandom(seed + "maze");
  const cellW = 40, cellH = 40;
  const w = cols * cellW, h = rows * cellH;
  // grid de paredes: cada célula tem 4 paredes (N,E,S,W)
  const cells = Array.from({ length: rows }, () => Array.from({ length: cols }, () => ({ N: true, E: true, S: true, W: true, v: false })));
  function carve(cx, cy) {
    cells[cy][cx].v = true;
    const dirs = shuffle([
      [0, -1, "N", "S"], [1, 0, "E", "W"], [0, 1, "S", "N"], [-1, 0, "W", "E"],
    ], rnd);
    for (const [dx, dy, a, b] of dirs) {
      const nx = cx + dx, ny = cy + dy;
      if (nx >= 0 && nx < cols && ny >= 0 && ny < rows && !cells[ny][nx].v) {
        cells[cy][cx][a] = false;
        cells[ny][nx][b] = false;
        carve(nx, ny);
      }
    }
  }
  carve(0, 0);
  let lines = "";
  for (let y = 0; y < rows; y++) {
    for (let x = 0; x < cols; x++) {
      const c = cells[y][x];
      const x0 = x * cellW, y0 = y * cellH, x1 = x0 + cellW, y1 = y0 + cellH;
      if (c.N) lines += `<line x1="${x0}" y1="${y0}" x2="${x1}" y2="${y0}"/>`;
      if (c.W) lines += `<line x1="${x0}" y1="${y0}" x2="${x0}" y2="${y1}"/>`;
      if (y === rows - 1 && c.S) lines += `<line x1="${x0}" y1="${y1}" x2="${x1}" y2="${y1}"/>`;
      if (x === cols - 1 && c.E) lines += `<line x1="${x1}" y1="${y0}" x2="${x1}" y2="${y1}"/>`;
    }
  }
  const startIconSvg = `<svg x="-4" y="-4" width="${cellH+8}" height="${cellH+8}" viewBox="0 0 100 100">${ICONS[startIcon]()}</svg>`;
  const endIconSvg = `<svg x="${w-cellH-4}" y="${h-cellH-4}" width="${cellH+8}" height="${cellH+8}" viewBox="0 0 100 100">${ICONS[endIcon]()}</svg>`;
  return `<p class="activity-prompt">${prompt}</p>
    <div class="maze-wrap">
      <svg viewBox="-6 -6 ${w+12} ${h+12}" class="maze-svg" stroke="#2b2b2b" stroke-width="3" stroke-linecap="round">
        ${startIconSvg}${endIconSvg}${lines}
      </svg>
    </div>`;
}

/* ---------- 2. Caça-palavras ---------- */
function renderWordSearch(seed, { words, size = 10, prompt = "Encontre as palavras escondidas!" }) {
  const rnd = seededRandom(seed + "ws");
  const letters = "AEIOU BCDFGHJKLMNPQRSTVXZ".replace(/ /g, "");
  const longest = Math.max(...words.map(w => w.length));
  size = Math.max(size, longest + 2);
  const grid = Array.from({ length: size }, () => Array.from({ length: size }, () => null));
  const dirs = [[1,0],[0,1],[1,1],[-1,1]];
  const placed = [];
  for (const wordRaw of words) {
    const word = wordRaw.toUpperCase().normalize("NFD").replace(/[̀-ͯ]/g, "");
    let ok = false;
    for (let attempt = 0; attempt < 60 && !ok; attempt++) {
      const [dx, dy] = dirs[Math.floor(rnd() * dirs.length)];
      const maxX = dx >= 0 ? size - word.length * Math.abs(dx || 1) : size;
      const startX = dx === -1 ? Math.floor(rnd() * (size - word.length)) + word.length - 1 : Math.floor(rnd() * Math.max(1, size - (dx ? word.length - 1 : 0)));
      const startY = Math.floor(rnd() * Math.max(1, size - (dy ? word.length - 1 : 0)));
      let fits = true;
      for (let i = 0; i < word.length; i++) {
        const x = startX + dx * i, y = startY + dy * i;
        if (x < 0 || x >= size || y < 0 || y >= size) { fits = false; break; }
        if (grid[y][x] && grid[y][x] !== word[i]) { fits = false; break; }
      }
      if (fits) {
        for (let i = 0; i < word.length; i++) {
          const x = startX + dx * i, y = startY + dy * i;
          grid[y][x] = word[i];
        }
        placed.push(word);
        ok = true;
      }
    }
  }
  for (let y = 0; y < size; y++)
    for (let x = 0; x < size; x++)
      if (!grid[y][x]) grid[y][x] = letters[Math.floor(rnd() * letters.length)];

  const table = `<table class="wordsearch">${grid.map(row => `<tr>${row.map(l => `<td>${l}</td>`).join("")}</tr>`).join("")}</table>`;
  const list = `<div class="word-list">${words.map(w => `<span class="word-chip">${w}</span>`).join("")}</div>`;
  return `<p class="activity-prompt">${prompt}</p>${table}${list}`;
}

/* ---------- 3. Múltipla escolha / Circule / Verdadeiro-Falso ---------- */
function renderChoice(seed, { question, options, prompt = "Circule a resposta certa!" }) {
  return `<p class="activity-prompt">${prompt}</p>
    <p class="activity-question">${question}</p>
    <div class="choice-list">
      ${options.map((o, i) => `<div class="choice-item"><span class="choice-letter">${String.fromCharCode(65 + i)}</span> ${o}</div>`).join("")}
    </div>`;
}

function renderTrueFalse(seed, { statements, prompt = "Marque V (verdadeiro) ou F (falso)." }) {
  return `<p class="activity-prompt">${prompt}</p>
    <div class="tf-list">
      ${statements.map(s => `<div class="tf-item"><span class="tf-boxes"><span class="tf-box">V</span><span class="tf-box">F</span></span><span>${s}</span></div>`).join("")}
    </div>`;
}

/* ---------- 4. Associação / Ligue as colunas ---------- */
function renderMatch(seed, { left, right, prompt = "Ligue cada item da coluna da esquerda ao par certo na direita!" }) {
  const rnd = seededRandom(seed + "match");
  const shuffled = shuffle(right, rnd);
  return `<p class="activity-prompt">${prompt}</p>
    <div class="match-wrap">
      <div class="match-col">${left.map((l, i) => `<div class="match-item"><span class="match-dot"></span>${l}</div>`).join("")}</div>
      <div class="match-col">${shuffled.map((r) => `<div class="match-item right"><span class="match-dot"></span>${r}</div>`).join("")}</div>
    </div>`;
}

/* ---------- 5. Contar / Encontrar objetos ---------- */
function renderCount(seed, { icon, color, count, question = "Quantos você encontrou?", extraIcon, extraCount }) {
  const rnd = seededRandom(seed + "count");
  const items = [];
  const total = count + (extraCount || 0);
  const positions = [];
  for (let i = 0; i < total; i++) positions.push({ x: 8 + rnd() * 84, y: 8 + rnd() * 74 });
  for (let i = 0; i < count; i++) {
    const p = positions[i];
    items.push(`<div class="count-icon" style="left:${p.x}%;top:${p.y}%"><svg viewBox="0 0 100 100">${ICONS[icon](color)}</svg></div>`);
  }
  if (extraIcon) {
    for (let i = 0; i < extraCount; i++) {
      const p = positions[count + i];
      items.push(`<div class="count-icon" style="left:${p.x}%;top:${p.y}%"><svg viewBox="0 0 100 100">${ICONS[extraIcon]()}</svg></div>`);
    }
  }
  return `<p class="activity-prompt">${question}</p>
    <div class="count-field">${items.join("")}</div>
    <p class="answer-line">Resposta: <span class="blank"></span></p>`;
}

/* ---------- 6. Completar frase ---------- */
function renderFill(seed, { sentence, wordBank, prompt = "Complete a frase com as palavras do quadro!" }) {
  const rnd = seededRandom(seed + "fill");
  return `<p class="activity-prompt">${prompt}</p>
    <p class="fill-sentence">${sentence}</p>
    <div class="word-bank">${shuffle(wordBank, rnd).map(w => `<span class="word-chip">${w}</span>`).join("")}</div>`;
}

/* ---------- 7. Sequência ---------- */
function renderSequence(seed, { events, prompt = "Numere os fatos na ordem certa (1, 2, 3...)" }) {
  const rnd = seededRandom(seed + "seq");
  const shuffled = shuffle(events, rnd);
  return `<p class="activity-prompt">${prompt}</p>
    <div class="seq-list">
      ${shuffled.map(e => `<div class="seq-item"><span class="seq-box"></span>${e}</div>`).join("")}
    </div>`;
}

/* ---------- 8. Desenhar ---------- */
function renderDraw(seed, { prompt = "Que tal desenhar?" }) {
  return `<p class="activity-prompt">${prompt}</p><div class="draw-box"></div>`;
}

/* ---------- 9. Jogo / Desafio livre (texto + caixa de resposta) ---------- */
function renderChallenge(seed, { text, prompt = "Desafio!" }) {
  return `<p class="activity-prompt">${prompt}</p><p class="activity-question">${text}</p><p class="answer-line">Resposta: <span class="blank"></span></p>`;
}

/* ---------- 10. Colorir ---------- */
function renderColoring(seed, { kinds, caption = "Capriche nas cores!" }) {
  return `<div class="coloring-wrap">${coloringScene(kinds)}</div><p class="activity-prompt center">${caption}</p>`;
}

/* ---------- Despachante ---------- */
function renderActivity(seed, activity) {
  switch (activity.type) {
    case "maze": return renderMaze(seed, activity);
    case "wordsearch": return renderWordSearch(seed, activity);
    case "quiz":
    case "circle": return renderChoice(seed, activity);
    case "truefalse": return renderTrueFalse(seed, activity);
    case "match":
    case "associate": return renderMatch(seed, activity);
    case "count":
    case "findobjects": return renderCount(seed, activity);
    case "fill":
    case "complete": return renderFill(seed, activity);
    case "sequence": return renderSequence(seed, activity);
    case "draw": return renderDraw(seed, activity);
    case "challenge":
    case "game": return renderChallenge(seed, activity);
    default: return "";
  }
}
