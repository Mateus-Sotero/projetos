# -*- coding: utf-8 -*-
"""Generates mapa-do-coracao.html — a print-ready parenting guide on
common childhood behavioral challenges, Christian-framed. Run, then
render to PDF with Playwright (see render.js)."""

import itertools
import re

from topics_data import TOPICS, FAQ, QUICK_REFERENCE, COLORS, COLOR_CYCLE

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700;800&family=Nunito:wght@400;600;700;800&display=swap');

* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  font-family: 'Nunito', sans-serif;
  color: #3a352e;
  line-height: 1.55;
  background: #e9ecef;
}
h1, h2, h3 { font-family: 'Baloo 2', cursive; color: #2f3e2e; margin: 0 0 10px; line-height: 1.25; }
p { margin: 0 0 10px; }

.page {
  position: relative;
  width: 210mm;
  min-height: 297mm;
  margin: 0 auto;
  background: #fffaf3;
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
  color: #b8b0a0;
  font-weight: 700;
  text-transform: uppercase;
  padding-top: 20px;
}

/* ---------- Cover / dividers ---------- */
.earth-page {
  background: linear-gradient(160deg, #5f8d6e 0%, #3d6249 55%, #2a4632 100%);
  color: #fff; display: flex; flex-direction: column; align-items: center;
  justify-content: center; text-align: center;
}
.earth-shape { position: absolute; border-radius: 50%; opacity: .15; background: #fff; }
.es1 { width: 260px; height: 260px; top: -90px; left: -90px; }
.es2 { width: 190px; height: 190px; bottom: -60px; right: -60px; background: #c99a3e; opacity: .2; }
.es3 { width: 130px; height: 130px; top: 90px; right: -40px; background: #c07b8b; opacity: .2; }
.compass-badge {
  font-size: 60px; background: rgba(255,255,255,.12); border: 3px solid rgba(255,255,255,.35);
  width: 130px; height: 130px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center; margin-bottom: 18px;
}
.cover-kicker { text-transform: uppercase; letter-spacing: 2px; font-size: 12px; font-weight: 700; opacity: .85; margin-bottom: 6px; }
.cover-title { font-size: 56px; color: #fff; margin: 4px 0; }
.cover-subtitle { font-size: 16px; max-width: 480px; opacity: .94; margin-top: 8px; }
.cover-brand { margin-top: 20px; font-family: 'Baloo 2', cursive; font-size: 14px; background: rgba(255,255,255,.14); padding: 6px 20px; border-radius: 50px; }
.divider-page h1 { color: #fff; font-size: 34px; max-width: 480px; }
.divider-page p { max-width: 420px; opacity: .92; font-size: 15px; }
.divider-emoji { font-size: 50px; margin-bottom: 10px; }

/* ---------- Section kicker + generic light pages ---------- */
.section-kicker {
  display: inline-flex; align-items: center; gap: 6px;
  background: var(--accent, #5f8d6e); color: #fff;
  font-weight: 800; font-size: 11px; letter-spacing: 1px; text-transform: uppercase;
  padding: 6px 16px; border-radius: 50px; margin-bottom: 14px;
}
.letter-page h1, .toc-page h1, .faq-page h1 { font-size: 30px; }
.quickref-page h1 { font-size: 26px; }
.letter-page p { font-size: 15px; line-height: 1.7; }
.letter-list { list-style: none; padding: 0; margin: 16px 0; }
.letter-list li { display: flex; align-items: flex-start; gap: 12px; margin-bottom: 12px; font-size: 14.5px; }
.letter-ic { flex: 0 0 auto; width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #fff; font-size: 15px; }
.letter-sign { margin-top: 20px; font-style: italic; color: #2f3e2e; }

/* ---------- TOC ---------- */
.toc-list { list-style: none; padding: 0; margin: 14px 0 0; }
.toc-list li {
  display: flex; align-items: center; gap: 10px; font-size: 13px; font-weight: 700;
  color: #3a352e; padding: 6.5px 0; border-bottom: 1px dashed #ece5d8;
}
.toc-num {
  flex: 0 0 auto; width: 24px; height: 24px; border-radius: 50%;
  background: #eef5f0; color: #3d6249; font-size: 11px; font-weight: 800;
  display: flex; align-items: center; justify-content: center;
}
.toc-ic { font-size: 16px; }

/* ---------- Foundations page ---------- */
.foundation-cards { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 16px; }
.foundation-card {
  background: #fff; border: 2px solid #f1ece0; border-top: 6px solid var(--accent);
  border-radius: 16px; padding: 20px;
}
.foundation-card h3 { font-size: 17px; margin-bottom: 8px; }
.foundation-card p { font-size: 13.5px; color: #6b6355; margin: 0; }

/* ---------- Topic pages (2 per topic) ---------- */
.topic-page { background: #fffaf3; }
.topic-head { display: flex; align-items: center; gap: 18px; margin-bottom: 20px; }
.topic-badge {
  flex: 0 0 auto; width: 78px; height: 78px; border-radius: 50%;
  background: var(--accent); display: flex; align-items: center; justify-content: center;
  font-size: 38px; box-shadow: 0 5px 0 rgba(0,0,0,.08);
}
.topic-kicker { display: block; text-transform: uppercase; letter-spacing: 1px; font-size: 11px; font-weight: 800; color: var(--accent-text); }
.topic-head-text h2 { font-size: 27px; margin: 3px 0 0; }
.info-box {
  background: #fff; border: 1.5px solid #f1ece0; border-radius: 16px;
  padding: 18px 20px; margin-bottom: 14px;
}
.info-tag { display: block; font-weight: 800; font-size: 12px; margin-bottom: 6px; color: var(--accent-text); text-transform: uppercase; letter-spacing: .5px; }
.info-box p { margin: 0; font-size: 14.5px; color: #4a4438; line-height: 1.65; }

.verse-box {
  border-radius: 16px; padding: 18px 20px; margin-bottom: 16px;
  background: var(--accent-soft); border: 1.5px solid var(--accent-soft);
}
.verse-box .info-tag { color: var(--accent-text); }
.verse-box p { margin: 0 0 8px; font-size: 14.5px; color: #4a4438; font-style: italic; }
.verse-box .reflection { font-style: normal; margin: 0; }

.tips-title { font-size: 15px; font-weight: 800; color: #2f3e2e; margin-bottom: 10px; }
.tips-list { list-style: none; padding: 0; margin: 0 0 16px; }
.tips-list li {
  display: flex; align-items: flex-start; gap: 10px; font-size: 14px;
  color: #3a352e; margin-bottom: 10px; line-height: 1.5;
}
.tip-num {
  flex: 0 0 auto; width: 22px; height: 22px; border-radius: 50%;
  background: var(--accent); color: #fff; font-size: 11px; font-weight: 800;
  display: flex; align-items: center; justify-content: center; margin-top: 1px;
}
.prayer-box {
  border-radius: 16px; padding: 18px 20px 18px 66px; position: relative;
  background: #faf6ee; border: 1.5px dashed #e4dcc8; margin-top: auto;
}
.prayer-ic { position: absolute; left: 20px; top: 18px; font-size: 26px; }
.prayer-box p { margin: 0; font-size: 14px; color: #4a4438; font-style: italic; }

/* ---------- Quick reference ---------- */
.quickref-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 7px; margin-top: 6px; }
.quickref-card {
  background: #fff; border: 1.5px solid #f1ece0; border-radius: 11px;
  padding: 9px 10px; display: flex; flex-direction: column; gap: 3px;
}
.quickref-ic { font-size: 16px; }
.quickref-card b { display: block; font-size: 10.5px; color: #2f3e2e; line-height: 1.25; }
.quickref-card span { font-size: 9.5px; color: #6b6355; line-height: 1.3; }

/* ---------- FAQ ---------- */
.faq-item { border: 1.5px solid #f1ece0; border-radius: 14px; padding: 16px 20px; margin-bottom: 12px; background: #fff; }
.faq-q { font-weight: 800; font-size: 14.5px; color: #2f3e2e; margin-bottom: 6px; }
.faq-a { font-size: 13.5px; color: #4a4438; margin: 0; line-height: 1.6; }
"""

COVER_PAGE = """
<section class="page earth-page">
  <div class="earth-shape es1"></div>
  <div class="earth-shape es2"></div>
  <div class="earth-shape es3"></div>
  <div class="compass-badge">🧭</div>
  <span class="cover-kicker">um guia bíblico para os pais de hoje</span>
  <h1 class="cover-title">Mapa do<br>Coração</h1>
  <p class="cover-subtitle">18 desafios comportamentais comuns da infância, explicados com
     carinho, embasados na Bíblia e com dicas práticas para o dia a dia</p>
  <span class="cover-brand">Mapa Bíblico Kids</span>
</section>"""

LETTER_PAGE = """
<section class="page letter-page">
  <span class="section-kicker" style="--accent:#5f8d6e">💚 antes de começar</span>
  <h1>Para Você, Que Educa com Amor</h1>
  <p>Criar filhos é uma das jornadas mais bonitas — e mais desafiadoras — que existem. Birras,
  teimosia, ciúmes, medos... cada fase traz um novo território para explorar, e este guia
  quer ser uma bússola nesse caminho.</p>
  <p>Aqui você vai encontrar 18 dos desafios comportamentais mais comuns da infância,
  cada um com quatro partes:</p>
  <ul class="letter-list">
    <li><span class="letter-ic" style="background:#5f8d6e">🔍</span>
        <b>O que é e por que acontece</b> — entendendo a fase do seu filho.</li>
    <li><span class="letter-ic" style="background:#c99a3e">📖</span>
        <b>Uma base bíblica</b> — um versículo e uma reflexão para o seu coração.</li>
    <li><span class="letter-ic" style="background:#c76f4c">✅</span>
        <b>Dicas práticas</b> — atitudes que você pode aplicar ainda hoje.</li>
    <li><span class="letter-ic" style="background:#c07b8b">🙏</span>
        <b>Uma oração</b> — para pedir sabedoria e paciência a Deus.</li>
  </ul>
  <p>Você não precisa ser um pai ou mãe perfeito — precisa apenas de um coração disposto a
  aprender, e o guia certo para os dias mais difíceis.</p>
  <p class="letter-sign">Com carinho,<br><b>Equipe Mapa Bíblico Kids</b></p>
  <div class="page-foot">Mapa do Coração · @@PN@@</div>
</section>"""


def toc_page():
    items = "".join(
        f'<li><span class="toc-num">{i}</span><span class="toc-ic">{t["icon"]}</span>{t["title"]}</li>'
        for i, t in enumerate(TOPICS, start=1)
    )
    return f"""
<section class="page toc-page">
  <span class="section-kicker" style="--accent:#c99a3e">🗺️ sumário</span>
  <h1>Os 15 Desafios</h1>
  <ul class="toc-list">{items}
    <li><span class="toc-num">📋</span><span class="toc-ic"></span>Resumo rápido de todas as dicas</li>
    <li><span class="toc-num">❓</span><span class="toc-ic"></span>Perguntas frequentes dos pais</li>
  </ul>
  <div class="page-foot">Mapa do Coração · @@PN@@</div>
</section>"""


FOUNDATIONS_PAGE = """
<section class="page">
  <span class="section-kicker" style="--accent:#5f8d6e">🌱 fundamentos</span>
  <h1>Educar com Amor e Firmeza</h1>
  <p style="font-size:15px; line-height:1.7; max-width:600px;">Antes de entrar nos desafios
  específicos, vale lembrar de quatro princípios que sustentam todo o resto deste guia —
  eles funcionam como uma bússola para qualquer situação que a lista de tópicos não cobrir.</p>
  <div class="foundation-cards">
    <div class="foundation-card" style="--accent:#5f8d6e">
      <h3>💚 Amor Incondicional</h3>
      <p>O comportamento pode ser corrigido, mas o amor pelo filho nunca deve parecer
      condicional a esse comportamento. Ele precisa saber que é amado mesmo no seu pior dia.</p>
    </div>
    <div class="foundation-card" style="--accent:#c76f4c">
      <h3>🧱 Limites Claros</h3>
      <p>Regras poucas, claras e consistentes trazem mais segurança do que muitas regras
      aplicadas de forma inconsistente. Firmeza não é o oposto de amor — é parte dele.</p>
    </div>
    <div class="foundation-card" style="--accent:#c99a3e">
      <h3>🙏 Oração Constante</h3>
      <p>Educar é grande demais para fazermos sozinhos. Entregar cada fase, cada dificuldade
      e cada vitória a Deus em oração renova a paciência e a sabedoria do dia a dia.</p>
    </div>
    <div class="foundation-card" style="--accent:#c07b8b">
      <h3>🪞 O Exemplo</h3>
      <p>Crianças aprendem muito mais observando do que ouvindo. A forma como lidamos com
      nossa própria raiva, frustração e erros ensina mais do que qualquer discurso.</p>
    </div>
  </div>
  <div class="page-foot">Mapa do Coração · @@PN@@</div>
</section>"""


def topic_page_1(idx, total, t, color_key):
    c = COLORS[color_key]
    return f"""
<section class="page topic-page" style="--accent:{c['bg']}; --accent-soft:{c['soft']}; --accent-text:{c['text']}">
  <header class="topic-head">
    <div class="topic-badge">{t['icon']}</div>
    <div class="topic-head-text">
      <span class="topic-kicker">Desafio {idx} de {total}</span>
      <h2>{t['title']}</h2>
    </div>
  </header>
  <div class="info-box">
    <span class="info-tag">🔍 O que é</span>
    <p>{t['what']}</p>
  </div>
  <div class="info-box">
    <span class="info-tag">🧠 Por que acontece</span>
    <p>{t['why']}</p>
  </div>
  <div class="verse-box">
    <span class="info-tag">📖 Base bíblica</span>
    <p>{t['verse']}</p>
    <p class="reflection">{t['reflection']}</p>
  </div>
  <div class="page-foot">Mapa do Coração · @@PN@@</div>
</section>"""


def topic_page_2(idx, total, t, color_key):
    c = COLORS[color_key]
    tips_html = "".join(
        f'<li><span class="tip-num">{i}</span>{tip}</li>'
        for i, tip in enumerate(t["tips"], start=1)
    )
    return f"""
<section class="page topic-page" style="--accent:{c['bg']}; --accent-soft:{c['soft']}; --accent-text:{c['text']}">
  <span class="topic-kicker">Desafio {idx} de {total} · continuação</span>
  <h2 style="font-size:24px; margin:4px 0 20px;">{t['title']} — na prática</h2>
  <p class="tips-title">✅ Dicas práticas para o dia a dia</p>
  <ul class="tips-list">{tips_html}</ul>
  <div class="prayer-box">
    <span class="prayer-ic">🙏</span>
    <p>{t['prayer']}</p>
  </div>
  <div class="page-foot">Mapa do Coração · @@PN@@</div>
</section>"""


def quickref_page():
    cards = "".join(
        f'<div class="quickref-card"><span class="quickref-ic">{ic}</span>'
        f'<div><b>{title}</b><span>{tip}</span></div></div>'
        for ic, title, tip in QUICK_REFERENCE
    )
    return f"""
<section class="page quickref-page">
  <span class="section-kicker" style="--accent:#c76f4c">📋 resumo rápido</span>
  <h1 style="margin-bottom:6px;">Uma Dica de Cada Desafio</h1>
  <p style="font-size:13px; color:#6b6355; max-width:560px; margin-bottom:6px;">Para consultar rapidinho nos
  dias corridos — a dica principal de cada um dos 18 desafios deste guia.</p>
  <div class="quickref-grid">{cards}</div>
  <div class="page-foot">Mapa do Coração · @@PN@@</div>
</section>"""


def faq_page():
    items = "".join(
        f'<div class="faq-item"><p class="faq-q">{q}</p><p class="faq-a">{a}</p></div>'
        for q, a in FAQ
    )
    return f"""
<section class="page faq-page">
  <span class="section-kicker" style="--accent:#c07b8b">❓ perguntas frequentes</span>
  <h1>Dúvidas Comuns dos Pais</h1>
  {items}
  <div class="page-foot">Mapa do Coração · @@PN@@</div>
</section>"""


CLOSING_PAGE = """
<section class="page earth-page">
  <div class="earth-shape es1"></div>
  <div class="earth-shape es2"></div>
  <div class="compass-badge">💚</div>
  <h1 style="color:#fff; font-size:28px; max-width:460px;">Continue Nessa Jornada</h1>
  <p style="max-width:420px; opacity:.92; font-size:15px;">Nenhum pai ou mãe acerta sempre —
  e está tudo bem. O que importa é continuar tentando, aprendendo e orando por sabedoria a
  cada novo dia. Seu esforço já é, por si só, um ato de amor.</p>
  <span class="cover-brand">Mapa Bíblico Kids</span>
  <p style="margin-top:26px; font-size:11px; opacity:.7;">Mapa do Coração © 2026 — Todos os direitos reservados</p>
</section>"""


def build():
    parts = [COVER_PAGE, LETTER_PAGE, toc_page(), FOUNDATIONS_PAGE]
    for i, t in enumerate(TOPICS, start=1):
        color_key = COLOR_CYCLE[(i - 1) % len(COLOR_CYCLE)]
        parts.append(topic_page_1(i, len(TOPICS), t, color_key))
        parts.append(topic_page_2(i, len(TOPICS), t, color_key))
    parts.append(quickref_page())
    parts.append(faq_page())
    parts.append(CLOSING_PAGE)

    body = ''.join(parts)
    counter = itertools.count(1)
    body = re.sub(r'@@PN@@', lambda _m: str(next(counter)), body)

    html = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8" />
<title>Mapa do Coração — Guia dos Pais</title>
<style>{CSS}</style>
</head>
<body>
{body}
</body>
</html>"""
    return html


if __name__ == "__main__":
    out = build()
    with open("mapa-do-coracao.html", "w", encoding="utf-8") as f:
        f.write(out)
    print("wrote", len(out), "bytes")
