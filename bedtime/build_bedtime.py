# -*- coding: utf-8 -*-
"""Generates historias-para-dormir.html — a print-ready 50-story bedtime
ebook (Bible retellings + original values fables). Run, then render to
PDF with Playwright (see render.js)."""

import itertools
import re

from stories_data import ALL_STORIES, BIBLE_STORIES, FABLE_STORIES, COLORS, COLOR_CYCLE, CLOSERS

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700;800&family=Nunito:wght@400;600;700;800&display=swap');

* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  font-family: 'Nunito', sans-serif;
  color: #3b3660;
  line-height: 1.55;
  background: #e9ecef;
}
h1, h2, h3 { font-family: 'Baloo 2', cursive; color: #2e2a5c; margin: 0 0 10px; line-height: 1.2; }
p { margin: 0 0 10px; }

.page {
  position: relative;
  width: 210mm;
  min-height: 297mm;
  margin: 0 auto;
  background: #fdfaff;
  padding: 20mm 18mm;
  overflow: hidden;
  page-break-after: always;
  display: flex;
  flex-direction: column;
}
.page-foot {
  margin-top: auto;
  text-align: center;
  font-size: 10px;
  letter-spacing: .5px;
  color: #b7b2d6;
  font-weight: 700;
  text-transform: uppercase;
  padding-top: 20px;
}

/* ---------- Cover & night dividers ---------- */
.night-page {
  background: linear-gradient(165deg, #1e1b4b 0%, #2a2566 45%, #12102a 100%);
  color: #fff; display: flex; flex-direction: column; align-items: center;
  justify-content: center; text-align: center;
}
.night-shape { position: absolute; border-radius: 50%; opacity: .14; background: #fff; }
.ns1 { width: 260px; height: 260px; top: -90px; left: -90px; }
.ns2 { width: 190px; height: 190px; bottom: -60px; right: -60px; background: #f5b942; opacity: .18; }
.ns3 { width: 130px; height: 130px; top: 80px; right: -40px; background: #a78bfa; opacity: .2; }
.night-stars { letter-spacing: 10px; font-size: 15px; opacity: .8; margin-bottom: 10px; }
.moon-badge {
  font-size: 66px; background: rgba(255,255,255,.12); border: 3px solid rgba(255,255,255,.35);
  width: 140px; height: 140px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center; margin-bottom: 18px;
}
.cover-kicker { text-transform: uppercase; letter-spacing: 2px; font-size: 12px; font-weight: 700; opacity: .85; margin-bottom: 6px; }
.cover-title { font-size: 60px; color: #fff; margin: 4px 0; }
.cover-subtitle { font-size: 16px; max-width: 480px; opacity: .92; margin-top: 8px; }
.cover-icons { font-size: 24px; letter-spacing: 10px; margin-top: 18px; }
.cover-brand { margin-top: 20px; font-family: 'Baloo 2', cursive; font-size: 14px; background: rgba(255,255,255,.14); padding: 6px 20px; border-radius: 50px; }

.divider-page h1 { color: #fff; font-size: 36px; max-width: 480px; }
.divider-page p { max-width: 420px; opacity: .9; font-size: 15px; }
.divider-emoji { font-size: 54px; margin-bottom: 10px; }

/* ---------- Letter / how-to / TOC (reused light style) ---------- */
.section-kicker {
  display: inline-flex; align-items: center; gap: 6px;
  background: var(--accent, #a78bfa); color: #fff;
  font-weight: 800; font-size: 11px; letter-spacing: 1px; text-transform: uppercase;
  padding: 6px 16px; border-radius: 50px; margin-bottom: 14px;
}
.letter-page h1, .toc-page h1 { font-size: 30px; }
.letter-page p { font-size: 15px; line-height: 1.7; }
.letter-list { list-style: none; padding: 0; margin: 16px 0; }
.letter-list li { display: flex; align-items: flex-start; gap: 12px; margin-bottom: 12px; font-size: 14.5px; }
.letter-ic {
  flex: 0 0 auto; width: 32px; height: 32px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center; color: #fff; font-size: 15px;
}
.letter-sign { margin-top: 20px; font-style: italic; color: #2e2a5c; }

.toc-columns { display: grid; grid-template-columns: 1fr 1fr; gap: 28px; margin-top: 10px; }
.toc-col h3 { font-size: 15px; margin: 0 0 8px; }
.toc-list { list-style: none; padding: 0; margin: 0; }
.toc-list li {
  display: flex; align-items: center; gap: 7px; font-size: 11px; font-weight: 700;
  line-height: 1.25; color: #3b3660; padding: 3.5px 0; border-bottom: 1px dashed #e7e3f6;
}
.toc-ic { font-size: 12px; flex: 0 0 auto; }
.toc-title { flex: 1 1 auto; }
.toc-num {
  flex: 0 0 auto; width: 18px; height: 18px; border-radius: 50%;
  background: #ede9fe; color: #6d28d9; font-size: 10px; font-weight: 800;
  display: flex; align-items: center; justify-content: center;
}

/* ---------- Story page ---------- */
.story-page { background: #fdfaff; }
.story-page .moon { position: absolute; top: 14mm; right: 16mm; font-size: 26px; opacity: .5; }
.story-page .stars-deco { position: absolute; top: 16mm; left: 16mm; font-size: 16px; opacity: .5; letter-spacing: 6px; }
.story-head { display: flex; align-items: center; gap: 20px; margin-bottom: 24px; }
.story-badge {
  flex: 0 0 auto; width: 88px; height: 88px; border-radius: 50%;
  background: var(--accent); display: flex; align-items: center; justify-content: center;
  font-size: 44px; box-shadow: 0 6px 0 rgba(0,0,0,.08);
}
.story-kicker {
  display: block; text-transform: uppercase; letter-spacing: 1px; font-size: 12px;
  font-weight: 800; color: var(--accent-text);
}
.story-head-text h2 { font-size: 30px; margin: 4px 0 0; }
.story-body {
  font-size: 17.5px; color: #3b3660; background: #fff;
  border-radius: 20px; padding: 28px 30px; border: 1.5px solid #f0edf9;
  margin-bottom: 22px; line-height: 1.85;
}
.moral-box {
  border-radius: 18px; padding: 22px 24px 22px 78px; position: relative;
  background: var(--accent-soft); border: 1.5px solid var(--accent-soft);
  margin-bottom: 20px;
}
.moral-ic { position: absolute; left: 22px; top: 22px; font-size: 32px; }
.moral-tag { display: block; font-weight: 800; font-size: 14px; margin-bottom: 6px; color: var(--accent-text); }
.moral-box p { margin: 0; font-size: 16.5px; color: #3b3660; line-height: 1.6; }
.story-stripe {
  text-align: center; font-size: 22px; letter-spacing: 12px; opacity: .16;
  white-space: nowrap; overflow: hidden; margin-bottom: 4px;
}
.closer-line {
  text-align: center; font-style: italic; font-size: 15px; color: #8781ac;
  margin-top: auto; padding-top: 16px;
}

@media (max-width: 640px) { .toc-columns { grid-template-columns: 1fr; } }
"""

COVER_PAGE = """
<section class="page night-page">
  <div class="night-shape ns1"></div>
  <div class="night-shape ns2"></div>
  <div class="night-shape ns3"></div>
  <div class="night-stars">✦ ⋆ ✧ ⋆ ✦ ⋆ ✧ ⋆ ✦</div>
  <div class="moon-badge">🌙</div>
  <span class="cover-kicker">um livro de boa noite para crianças</span>
  <h1 class="cover-title">Histórias Para<br>Dormir</h1>
  <p class="cover-subtitle">50 histórias — bíblicas e de valores — com começo, meio, fim<br>
     e uma linda lição para adormecer em paz</p>
  <div class="cover-icons">🌟 🐑 🕊️ 🧸 🌈 ☁️</div>
  <span class="cover-brand">Mapa Bíblico Kids</span>
</section>"""

LETTER_PAGE = """
<section class="page letter-page">
  <span class="section-kicker" style="--accent:#a78bfa">💜 antes de começar</span>
  <h1>Para os Pais e Cuidadores</h1>
  <p>Este livro foi feito para embalar o sono das crianças com histórias curtinhas,
  calmas e cheias de significado. São 50 histórias no total: 30 inspiradas em
  passagens da Bíblia e 20 fábulas originais sobre valores como gratidão,
  paciência, perdão e coragem.</p>
  <p>Cada história tem começo, meio e fim, e termina com uma pequena lição para
  conversar com a criança antes dela fechar os olhinhos:</p>
  <ul class="letter-list">
    <li><span class="letter-ic" style="background:#a78bfa">📖</span>
        <b>A história</b> — curtinha, calma, sem sustos, perfeita para ler em voz alta.</li>
    <li><span class="letter-ic" style="background:#f5b942">🌙</span>
        <b>A lição</b> — uma frase simples para fixar o valor da noite.</li>
  </ul>
  <p>Sugerimos ler uma história por noite, em voz baixa e tranquila, terminando com
  um abraço e, se quiser, uma oraçãozinha de agradecimento pelo dia.</p>
  <p class="letter-sign">Boa leitura e boas noites,<br><b>Equipe Mapa Bíblico Kids</b></p>
  <div class="page-foot">Histórias Para Dormir · @@PN@@</div>
</section>"""


def divider_page(title, subtitle, emoji):
    return f"""
<section class="page night-page divider-page">
  <div class="night-shape ns1"></div>
  <div class="night-shape ns2"></div>
  <div class="divider-emoji">{emoji}</div>
  <h1>{title}</h1>
  <p>{subtitle}</p>
</section>"""


def toc_page():
    bible_items = "".join(
        f'<li><span class="toc-num">{i}</span><span class="toc-ic">{s["icon"]}</span>'
        f'<span class="toc-title">{s["title"]}</span></li>'
        for i, s in enumerate(BIBLE_STORIES, start=1)
    )
    fable_items = "".join(
        f'<li><span class="toc-num">{i}</span><span class="toc-ic">{s["icon"]}</span>'
        f'<span class="toc-title">{s["title"]}</span></li>'
        for i, s in enumerate(FABLE_STORIES, start=31)
    )
    return f"""
<section class="page toc-page">
  <span class="section-kicker" style="--accent:#f5b942">🗺️ sumário</span>
  <h1>As 50 Histórias</h1>
  <div class="toc-columns">
    <div class="toc-col">
      <h3 style="color:#6d28d9">📖 Histórias Bíblicas (1–30)</h3>
      <ul class="toc-list">{bible_items}</ul>
    </div>
    <div class="toc-col">
      <h3 style="color:#be123c">🌙 Fábulas de Valores (31–50)</h3>
      <ul class="toc-list">{fable_items}</ul>
    </div>
  </div>
  <div class="page-foot">Histórias Para Dormir · @@PN@@</div>
</section>"""


CLOSING_PAGE = """
<section class="page night-page">
  <div class="night-shape ns1"></div>
  <div class="night-shape ns2"></div>
  <div class="night-stars">✦ ⋆ ✧ ⋆ ✦</div>
  <div class="moon-badge">😴</div>
  <h1 style="color:#fff; font-size:30px; max-width:460px;">Fim das Histórias de Hoje...<br>Até Amanhã!</h1>
  <p style="max-width:420px; opacity:.9; font-size:15px;">Cinquenta histórias, cinquenta noites de paz. Continue lendo,
  conversando e sonhando alto — o amor de Deus cabe em cada uma delas.</p>
  <span class="cover-brand">Mapa Bíblico Kids</span>
  <p style="margin-top:26px; font-size:11px; opacity:.7;">Histórias Para Dormir © 2026 — Todos os direitos reservados</p>
</section>"""


def story_page(idx, total, section_label, s, color_key):
    c = COLORS[color_key]
    closer = CLOSERS[(idx - 1) % len(CLOSERS)]
    ref_html = f'<span class="story-ref">📍 {s["ref"]}</span>' if s.get("ref") else ""
    return f"""
<section class="page story-page" style="--accent:{c['bg']}; --accent-soft:{c['soft']}; --accent-text:{c['text']}">
  <span class="moon">🌙</span>
  <span class="stars-deco">✦ ⋆ ✦</span>
  <header class="story-head">
    <div class="story-badge">{s['icon']}</div>
    <div class="story-head-text">
      <span class="story-kicker">{section_label} · História {idx} de {total}</span>
      <h2>{s['title']}</h2>
      {ref_html}
    </div>
  </header>
  <p class="story-body">{s['story']}</p>
  <div class="moral-box">
    <span class="moral-ic">🌙</span>
    <span class="moral-tag">Lição para guardar</span>
    <p>{s['moral']}</p>
  </div>
  <div class="story-stripe">{(s['icon'] + ' ') * 14}</div>
  <p class="closer-line">{closer}</p>
  <div class="page-foot">Histórias Para Dormir · @@PN@@</div>
</section>"""


def build():
    parts = [COVER_PAGE, LETTER_PAGE, toc_page()]
    parts.append(divider_page("Histórias Bíblicas", "Trinta histórias inspiradas na Bíblia, recontadas de um jeitinho calmo e gostoso para dormir.", "📖"))
    for i, s in enumerate(BIBLE_STORIES, start=1):
        color_key = COLOR_CYCLE[(i - 1) % len(COLOR_CYCLE)]
        parts.append(story_page(i, len(BIBLE_STORIES), "Histórias Bíblicas", s, color_key))
    parts.append(divider_page("Fábulas de Valores", "Vinte historinhas originais sobre bondade, coragem, gratidão e amor — para sonhar com um coração cheio de valores.", "🌈"))
    for i, s in enumerate(FABLE_STORIES, start=1):
        color_key = COLOR_CYCLE[(i - 1) % len(COLOR_CYCLE)]
        parts.append(story_page(i, len(FABLE_STORIES), "Fábulas de Valores", s, color_key))
    parts.append(CLOSING_PAGE)

    body = ''.join(parts)
    counter = itertools.count(1)
    body = re.sub(r'@@PN@@', lambda _m: str(next(counter)), body)

    html = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8" />
<title>Histórias Para Dormir — E-book</title>
<style>{CSS}</style>
</head>
<body>
{body}
</body>
</html>"""
    return html


if __name__ == "__main__":
    out = build()
    with open("historias-para-dormir.html", "w", encoding="utf-8") as f:
        f.write(out)
    print("wrote", len(out), "bytes")
