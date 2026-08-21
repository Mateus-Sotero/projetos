/* ===================================================================
   Biblioteca de ilustrações — formas simples, coloridas e originais.
   Cada função devolve um <g> num sistema de coordenadas 0-100 x 0-100,
   pronto para ser posicionado dentro de uma cena por scene().
=================================================================== */

const ICONS = {

  sun(c = "#FFC93C") {
    return `<g>
      ${[0,45,90,135,180,225,270,315].map(a=>`<line x1="50" y1="16" x2="50" y2="4" stroke="${c}" stroke-width="6" stroke-linecap="round" transform="rotate(${a} 50 50)"/>`).join("")}
      <circle cx="50" cy="50" r="26" fill="${c}" stroke="#2b2b2b" stroke-width="4"/>
      <circle cx="41" cy="46" r="3" fill="#2b2b2b"/><circle cx="59" cy="46" r="3" fill="#2b2b2b"/>
      <path d="M40 58 Q50 66 60 58" stroke="#2b2b2b" stroke-width="4" fill="none" stroke-linecap="round"/>
    </g>`;
  },

  cloud(c = "#ffffff") {
    return `<g stroke="#2b2b2b" stroke-width="4" fill="${c}">
      <ellipse cx="35" cy="55" rx="20" ry="14"/>
      <ellipse cx="60" cy="48" rx="24" ry="18"/>
      <ellipse cx="82" cy="58" rx="16" ry="12"/>
    </g>`;
  },

  tree(c = "#4CAF50") {
    return `<g stroke="#2b2b2b" stroke-width="4">
      <rect x="44" y="60" width="12" height="32" rx="4" fill="#A9673A"/>
      <circle cx="50" cy="46" r="30" fill="${c}"/>
      <circle cx="30" cy="58" r="16" fill="${c}"/>
      <circle cx="70" cy="58" r="16" fill="${c}"/>
    </g>`;
  },

  mountain(c = "#8D8FB3") {
    return `<g stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round">
      <path d="M5 90 L38 30 L58 60 L72 40 L96 90 Z" fill="${c}"/>
      <path d="M38 30 L46 44 L30 44 Z" fill="#fff"/>
      <path d="M72 40 L78 50 L66 50 Z" fill="#fff"/>
    </g>`;
  },

  star(c = "#FFD54F") {
    return `<path d="M50 6 L61 38 L95 38 L67 58 L78 90 L50 70 L22 90 L33 58 L5 38 L39 38 Z"
      fill="${c}" stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round"/>`;
  },

  rainbow() {
    const cols=["#EF476F","#FFB703","#FFD166","#06D6A0","#118AB2","#7B61FF"];
    return `<g fill="none" stroke-width="7">
      ${cols.map((col,i)=>`<path d="M${5+i*3} 95 A${45-i*7} ${45-i*7} 0 0 1 ${95-i*3} 95" stroke="${col}"/>`).join("")}
    </g>`;
  },

  water(c = "#4FC3F7") {
    return `<g stroke="#2b2b2b" stroke-width="4" fill="${c}">
      <path d="M0 70 Q15 58 30 70 T60 70 T90 70 T120 70 V100 H0 Z"/>
      <path d="M0 84 Q15 74 30 84 T60 84 T90 84 T120 84 V100 H0 Z" opacity=".7"/>
    </g>`;
  },

  ark(c = "#B5651D") {
    return `<g stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round">
      <path d="M10 62 Q50 82 90 62 L80 82 Q50 92 20 82 Z" fill="${c}"/>
      <rect x="28" y="38" width="44" height="26" rx="8" fill="#D8A05E"/>
      <rect x="38" y="46" width="10" height="10" rx="2" fill="#EAF6FF"/>
      <rect x="52" y="46" width="10" height="10" rx="2" fill="#EAF6FF"/>
      <path d="M28 38 Q50 22 72 38" fill="#8B4A22"/>
      ${ICONS.rainbowSmall()}
    </g>`;
  },
  rainbowSmall(){
    const cols=["#EF476F","#FFD166","#06D6A0","#118AB2"];
    return `<g fill="none" stroke-width="3" transform="translate(0,-8)">
      ${cols.map((col,i)=>`<path d="M${20+i*2} 30 A${18-i*4} ${18-i*4} 0 0 1 ${80-i*2} 30" stroke="${col}"/>`).join("")}
    </g>`;
  },

  boat(c = "#B5651D") {
    return `<g stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round">
      <path d="M10 68 L90 68 L76 88 L24 88 Z" fill="${c}"/>
      <rect x="47" y="20" width="6" height="48" fill="#8B4A22"/>
      <path d="M53 24 L82 60 L53 60 Z" fill="#FFF7E0"/>
      <path d="M47 30 L26 60 L47 60 Z" fill="#FFF7E0"/>
    </g>`;
  },

  fish(c = "#4FC3F7") {
    return `<g stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round" fill="${c}">
      <ellipse cx="45" cy="50" rx="34" ry="22"/>
      <path d="M79 50 L98 34 L98 66 Z"/>
      <circle cx="30" cy="44" r="4" fill="#2b2b2b"/>
      <path d="M20 58 Q30 66 40 58" fill="none" stroke="#2b2b2b" stroke-width="3"/>
    </g>`;
  },

  bigFish(c = "#3F7CAC") {
    return `<g stroke="#2b2b2b" stroke-width="5" stroke-linejoin="round">
      <path d="M84 30 L100 12 L92 50 L100 88 L84 70 Z" fill="${c}"/>
      <path d="M8 52 Q10 14 50 14 Q92 14 92 52 Q92 90 50 90 Q10 90 8 52 Z" fill="${c}"/>
      <path d="M40 20 Q50 4 62 18" fill="${c}"/>
      <circle cx="28" cy="46" r="6" fill="#fff" stroke="#2b2b2b" stroke-width="3"/>
      <circle cx="27" cy="46" r="2.6" fill="#2b2b2b"/>
      <path d="M18 64 Q28 74 40 64" fill="none" stroke="#2b2b2b" stroke-width="3"/>
    </g>`;
  },

  person(c = "#F2A65A", opts = {}) {
    const {crown=false, halo=false, staff=false, wings=false, sad=false} = opts;
    return `<g stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
      ${halo?'<ellipse cx="50" cy="14" rx="14" ry="6" fill="#FFEB99" stroke="#2b2b2b" stroke-width="3"/>':''}
      ${wings?'<path d="M30 40 Q4 30 10 60 Q22 54 34 50 Z" fill="#fff"/><path d="M70 40 Q96 30 90 60 Q78 54 66 50 Z" fill="#fff"/>':''}
      <path d="M32 96 L34 60 Q50 48 66 60 L68 96 Z" fill="${c}"/>
      <circle cx="50" cy="34" r="18" fill="#F6C9A0"/>
      ${crown?'<path d="M34 22 L38 8 L46 18 L50 6 L54 18 L62 8 L66 22 Z" fill="#FFD54F" stroke="#2b2b2b" stroke-width="3"/>':'<path d="M32 26 Q50 8 68 26 Q68 14 50 12 Q32 14 32 26 Z" fill="#6D4C41"/>'}
      <circle cx="44" cy="36" r="2.4" fill="#2b2b2b"/><circle cx="56" cy="36" r="2.4" fill="#2b2b2b"/>
      <path d="${sad?'M44 44 Q50 40 56 44':'M43 42 Q50 48 57 42'}" fill="none" stroke="#2b2b2b" stroke-width="3"/>
      ${staff?'<line x1="76" y1="20" x2="76" y2="94" stroke="#8B4A22" stroke-width="5"/><path d="M76 20 Q66 20 66 30" fill="none" stroke="#8B4A22" stroke-width="5"/>':''}
    </g>`;
  },

  sheep(c = "#F7F5EB") {
    return `<g stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round">
      <ellipse cx="50" cy="55" rx="30" ry="22" fill="${c}"/>
      <circle cx="24" cy="46" r="12" fill="#5D4037"/>
      <circle cx="20" cy="42" r="2.4" fill="#fff"/>
      <rect x="30" y="76" width="8" height="16" rx="3" fill="#5D4037"/>
      <rect x="62" y="76" width="8" height="16" rx="3" fill="#5D4037"/>
    </g>`;
  },

  lion(c = "#F0A93A") {
    return `<g stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round">
      <circle cx="50" cy="50" r="26" fill="#C9791C"/>
      <circle cx="50" cy="50" r="16" fill="${c}"/>
      <circle cx="43" cy="47" r="2.4" fill="#2b2b2b"/><circle cx="57" cy="47" r="2.4" fill="#2b2b2b"/>
      <path d="M46 56 Q50 60 54 56" fill="none" stroke="#2b2b2b" stroke-width="3"/>
      <path d="M50 52 L46 56 M50 52 L54 56" stroke="#2b2b2b" stroke-width="2"/>
    </g>`;
  },

  dove(c = "#ffffff") {
    return `<g stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round" fill="${c}">
      <ellipse cx="46" cy="52" rx="26" ry="16"/>
      <circle cx="70" cy="42" r="12"/>
      <path d="M78 40 L92 36 L80 46 Z" fill="#FFC93C"/>
      <path d="M30 48 Q10 40 18 58 Q28 56 34 54 Z"/>
      <path d="M40 66 L34 82" stroke="#4CAF50" stroke-width="3" fill="none"/>
      <circle cx="72" cy="38" r="2" fill="#2b2b2b"/>
    </g>`;
  },

  camel(c = "#D9A566") {
    return `<g stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round" fill="${c}">
      <path d="M14 70 Q14 46 30 46 Q34 34 44 40 Q50 30 58 40 Q66 34 68 46 Q86 48 86 70 Z"/>
      <path d="M68 46 Q78 20 88 34 Q84 42 76 46 Z"/>
      <circle cx="82" cy="30" r="3" fill="#2b2b2b"/>
      <rect x="26" y="70" width="8" height="18" fill="${c}"/><rect x="66" y="70" width="8" height="18" fill="${c}"/>
    </g>`;
  },

  tablets(c = "#E8DCC0") {
    return `<g stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round" fill="${c}">
      <path d="M18 30 Q18 20 28 20 L38 20 L38 90 L18 90 Z"/>
      <path d="M82 30 Q82 20 72 20 L62 20 L62 90 L82 90 Z"/>
      ${[34,44,54,64,74].map(y=>`<line x1="22" y1="${y}" x2="34" y2="${y}" stroke="#8D8FB3" stroke-width="3"/><line x1="66" y1="${y}" x2="78" y2="${y}" stroke="#8D8FB3" stroke-width="3"/>`).join("")}
    </g>`;
  },

  scroll(c = "#F3E3C3") {
    return `<g stroke="#2b2b2b" stroke-width="4">
      <rect x="20" y="34" width="60" height="32" fill="${c}"/>
      <circle cx="20" cy="34" r="8" fill="#C9A15A"/><circle cx="20" cy="66" r="8" fill="#C9A15A"/>
      <circle cx="80" cy="34" r="8" fill="#C9A15A"/><circle cx="80" cy="66" r="8" fill="#C9A15A"/>
      <line x1="30" y1="44" x2="70" y2="44" stroke="#B08B4F" stroke-width="3"/>
      <line x1="30" y1="52" x2="70" y2="52" stroke="#B08B4F" stroke-width="3"/>
      <line x1="30" y1="60" x2="60" y2="60" stroke="#B08B4F" stroke-width="3"/>
    </g>`;
  },

  crown(c = "#FFD54F") {
    return `<g stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round" fill="${c}">
      <path d="M14 80 L20 34 L38 56 L50 26 L62 56 L80 34 L86 80 Z"/>
      <circle cx="20" cy="34" r="5" fill="#EF476F"/><circle cx="50" cy="26" r="5" fill="#06D6A0"/><circle cx="80" cy="34" r="5" fill="#118AB2"/>
      <rect x="14" y="80" width="72" height="10" fill="${c}"/>
    </g>`;
  },

  harp(c = "#C9791C") {
    return `<g stroke="#2b2b2b" stroke-width="4" fill="none">
      <path d="M22 90 Q18 30 52 14" stroke-width="6" fill="none"/>
      <line x1="22" y1="90" x2="70" y2="90" stroke-width="6"/>
      <line x1="70" y1="90" x2="52" y2="14" stroke-width="6"/>
      ${[0,1,2,3,4,5].map(i=>`<line x1="${28+i*7}" y1="86" x2="${44+i*1.4}" y2="20" stroke="#C9791C" stroke-width="2"/>`).join("")}
    </g>`;
  },

  music() {
    return `<g stroke="#2b2b2b" stroke-width="4" fill="#7B61FF">
      <circle cx="26" cy="76" r="12"/><circle cx="66" cy="66" r="12"/>
      <line x1="38" y1="76" x2="38" y2="20" stroke-width="5"/>
      <line x1="78" y1="66" x2="78" y2="16" stroke-width="5"/>
      <path d="M38 20 L78 16 L78 34 L38 38 Z"/>
    </g>`;
  },

  trumpet(c = "#FFD166") {
    return `<g stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round" fill="${c}">
      <path d="M10 46 L60 40 L60 60 L10 54 Z"/>
      <path d="M60 30 Q95 30 95 50 Q95 70 60 70 Q75 50 60 30 Z"/>
    </g>`;
  },

  wall(c = "#E0A96D") {
    return `<g stroke="#2b2b2b" stroke-width="4">
      <rect x="6" y="40" width="88" height="46" fill="${c}"/>
      ${[0,1,2].map(r=>`<line x1="6" y1="${40+r*15}" x2="94" y2="${40+r*15}" stroke="#2b2b2b" stroke-width="3"/>`).join("")}
      ${[26,56,86].map((x,i)=>`<line x1="${x}" y1="${40+((i%2)?0:15)}" x2="${x}" y2="${55+((i%2)?0:15)}" stroke="#2b2b2b" stroke-width="3"/>`).join("")}
      <rect x="4" y="26" width="10" height="14" fill="${c}" stroke="#2b2b2b" stroke-width="3"/>
      <rect x="20" y="20" width="10" height="20" fill="${c}" stroke="#2b2b2b" stroke-width="3"/>
      <rect x="86" y="26" width="10" height="14" fill="${c}" stroke="#2b2b2b" stroke-width="3"/>
    </g>`;
  },

  wheat(c = "#E4B448") {
    return `<g stroke="#2b2b2b" stroke-width="3">
      ${[18,38,58,78].map((x,i)=>`<g transform="translate(${x} ${i%2?10:0})">
        <line x1="0" y1="90" x2="0" y2="30" stroke="#7CB342" stroke-width="4"/>
        ${[0,1,2,3,4].map(j=>`<ellipse cx="${j%2?-8:8}" cy="${30+j*10}" rx="6" ry="10" fill="${c}"/>`).join("")}
      </g>`).join("")}
    </g>`;
  },

  vine(c = "#7E57C2") {
    return `<g stroke="#2b2b2b" stroke-width="3">
      <path d="M10 90 Q50 10 90 90" fill="none" stroke="#7CB342" stroke-width="5"/>
      ${[20,35,50,65,80].map((x,i)=>`<circle cx="${x}" cy="${90-Math.sin((x-10)/80*Math.PI)*70}" r="7" fill="${c}"/>`).join("")}
      <path d="M50 20 Q40 10 30 18" fill="#7CB342" stroke="#2b2b2b" stroke-width="2"/>
    </g>`;
  },

  well(c = "#C9A15A") {
    return `<g stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round">
      <path d="M50 12 L14 30 L86 30 Z" fill="#8B4A22"/>
      <rect x="20" y="30" width="60" height="40" fill="${c}"/>
      <ellipse cx="50" cy="70" rx="30" ry="8" fill="#4FC3F7"/>
      <line x1="50" y1="16" x2="50" y2="60" stroke="#8B4A22" stroke-width="3"/>
    </g>`;
  },

  tent(c = "#D9A566") {
    return `<g stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round" fill="${c}">
      <path d="M50 14 L92 88 L58 88 L58 60 L42 60 L42 88 L8 88 Z"/>
      <line x1="50" y1="14" x2="50" y2="60" stroke="#8B4A22" stroke-width="3"/>
    </g>`;
  },

  key(c = "#FFD54F") {
    return `<g stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round" fill="${c}">
      <circle cx="28" cy="40" r="16"/><circle cx="28" cy="40" r="6" fill="#fff"/>
      <rect x="42" y="36" width="46" height="8"/>
      <rect x="70" y="44" width="8" height="12"/><rect x="82" y="44" width="8" height="16"/>
    </g>`;
  },

  candle(c = "#FFB703") {
    return `<g stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round">
      <path d="M50 8 Q60 24 50 32 Q40 24 50 8 Z" fill="${c}"/>
      <rect x="40" y="32" width="20" height="50" fill="#F7F1E1"/>
      <rect x="24" y="82" width="52" height="10" rx="4" fill="#C9A15A"/>
    </g>`;
  },

  throne(c = "#7E57C2") {
    return `<g stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round" fill="${c}">
      <rect x="26" y="30" width="48" height="50"/>
      <rect x="14" y="34" width="12" height="46"/><rect x="74" y="34" width="12" height="46"/>
      <path d="M30 30 L36 10 L44 30 M56 30 L64 10 L70 30" fill="${c}"/>
      <circle cx="36" cy="14" r="3" fill="#FFD54F"/><circle cx="64" cy="14" r="3" fill="#FFD54F"/>
    </g>`;
  },

  altar(c = "#B0A18F") {
    return `<g stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round">
      <rect x="18" y="60" width="64" height="24" fill="${c}"/>
      <path d="M40 60 Q50 30 60 60" fill="#FFC93C"/>
      <path d="M46 60 Q50 42 54 60" fill="#EF476F"/>
    </g>`;
  },

  cityWall(c = "#E0A96D") {
    return `<g stroke="#2b2b2b" stroke-width="4">
      <rect x="4" y="46" width="92" height="42" fill="${c}"/>
      ${[10,28,46,64,82].map(x=>`<rect x="${x}" y="34" width="12" height="12" fill="${c}"/>`).join("")}
      <path d="M40 88 L40 62 Q50 52 60 62 L60 88 Z" fill="#6D4C41"/>
    </g>`;
  },

  manger() {
    return `<g stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round">
      <path d="M14 60 L86 60 L78 80 L22 80 Z" fill="#B5651D"/>
      <path d="M20 60 Q50 44 80 60" fill="none" stroke="#E4B448" stroke-width="5"/>
      <circle cx="50" cy="14" r="8" fill="#FFD54F"/>
      ${[0,45,90,135,180,225,270,315].map(a=>`<line x1="50" y1="14" x2="${50+16*Math.cos(a*Math.PI/180)}" y2="${14+16*Math.sin(a*Math.PI/180)}" stroke="#FFD54F" stroke-width="3"/>`).join("")}
    </g>`;
  },

  cross(c = "#EF476F") {
    return `<g stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round" fill="${c}">
      <rect x="42" y="10" width="16" height="80" rx="4"/>
      <rect x="18" y="34" width="64" height="16" rx="4"/>
      ${[0,45,90,135,180,225,270,315].map(a=>`<line x1="50" y1="50" x2="${50+40*Math.cos(a*Math.PI/180)}" y2="${50+40*Math.sin(a*Math.PI/180)}" stroke="#FFD54F" stroke-width="3" opacity=".6"/>`).join("")}
    </g>`;
  },

  tomb() {
    return `<g stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round">
      <path d="M10 88 L10 40 Q50 4 90 40 L90 88 Z" fill="#C9BBA8"/>
      <circle cx="76" cy="70" r="18" fill="#8D8FB3"/>
      <path d="M40 88 L40 46 Q50 34 60 46 L60 88 Z" fill="#2b2b2b" opacity=".55"/>
      ${[0,30,60,90,120,150].map(a=>`<line x1="50" y1="20" x2="${50+30*Math.cos((a-90)*Math.PI/180)}" y2="${20+30*Math.sin((a-90)*Math.PI/180)}" stroke="#FFD54F" stroke-width="3"/>`).join("")}
    </g>`;
  },

  basketBread() {
    return `<g stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round">
      <path d="M16 56 L84 56 L74 88 L26 88 Z" fill="#C9A15A"/>
      <ellipse cx="36" cy="52" rx="12" ry="8" fill="#D9A566"/>
      <ellipse cx="60" cy="50" rx="14" ry="9" fill="#D9A566"/>
      ${ICONS.fish("#4FC3F7")}
    </g>`;
  },

  letter(c = "#EAF2FF") {
    return `<g stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round" fill="${c}">
      <rect x="12" y="26" width="76" height="52"/>
      <path d="M12 26 L50 58 L88 26" fill="none"/>
    </g>`;
  },

  book(c = "#7E57C2") {
    return `<g stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round">
      <path d="M50 22 Q30 12 12 20 L12 80 Q30 72 50 82 Z" fill="${c}"/>
      <path d="M50 22 Q70 12 88 20 L88 80 Q70 72 50 82 Z" fill="${c}"/>
      <line x1="50" y1="22" x2="50" y2="82" stroke="#2b2b2b" stroke-width="3"/>
    </g>`;
  },

  heart(c = "#EF476F") {
    return `<path d="M50 88 C10 60 8 30 30 20 C42 14 50 24 50 32 C50 24 58 14 70 20 C92 30 90 60 50 88 Z"
      fill="${c}" stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round"/>`;
  },

  balance(c = "#8D8FB3") {
    return `<g stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round" fill="none">
      <line x1="50" y1="10" x2="50" y2="80"/>
      <line x1="16" y1="30" x2="84" y2="30"/>
      <path d="M16 30 L4 54 Q16 64 28 54 Z" fill="${c}"/>
      <path d="M84 30 L72 54 Q84 64 96 54 Z" fill="${c}"/>
      <path d="M32 88 L68 88" stroke-width="6"/>
    </g>`;
  },

  road() {
    return `<g stroke="#2b2b2b" stroke-width="4">
      <path d="M30 92 Q45 40 40 8 L60 8 Q58 40 70 92 Z" fill="#C9A15A"/>
      <line x1="50" y1="16" x2="50" y2="34" stroke="#fff" stroke-width="4"/>
      <line x1="50" y1="46" x2="50" y2="64" stroke="#fff" stroke-width="4"/>
      <line x1="50" y1="76" x2="50" y2="88" stroke="#fff" stroke-width="4"/>
    </g>`;
  },

  jar(c = "#C9791C") {
    return `<g stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round" fill="${c}">
      <path d="M38 20 L62 20 L68 34 L70 82 Q50 92 30 82 L32 34 Z"/>
      <rect x="40" y="12" width="20" height="10" fill="#8B4A22"/>
    </g>`;
  },

  seed(c = "#7CB342") {
    return `<g stroke="#2b2b2b" stroke-width="4">
      <path d="M20 90 Q20 60 50 60 Q80 60 80 90 Z" fill="#A9673A"/>
      <path d="M50 60 L50 24" stroke="#4CAF50" stroke-width="5" fill="none"/>
      <ellipse cx="50" cy="20" rx="14" ry="10" fill="${c}"/>
      <path d="M50 44 Q34 34 24 44" fill="#4CAF50"/>
      <path d="M50 50 Q66 40 76 50" fill="#4CAF50"/>
    </g>`;
  },

  shield(c = "#4FC3F7") {
    return `<g stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round" fill="${c}">
      <path d="M50 10 L88 24 Q88 66 50 92 Q12 66 12 24 Z"/>
      <path d="M50 30 L50 74 M30 46 L70 46" stroke="#fff" stroke-width="6"/>
    </g>`;
  },

  angel() {
    return `${ICONS.person("#EAF2FF",{halo:true,wings:true})}`;
  },

  basket() {
    return `<g stroke="#2b2b2b" stroke-width="4" stroke-linejoin="round">
      <path d="M20 50 Q50 34 80 50 L74 78 Q50 88 26 78 Z" fill="#D9A566"/>
      ${[30,42,54,66].map(x=>`<line x1="${x}" y1="52" x2="${x}" y2="78" stroke="#8B4A22" stroke-width="2"/>`).join("")}
      <path d="M20 50 Q50 62 80 50" fill="none" stroke="#8B4A22" stroke-width="2"/>
    </g>`;
  },

  path_feet() {
    return `<g fill="#2b2b2b" opacity=".55">
      <ellipse cx="30" cy="30" rx="7" ry="12"/><ellipse cx="55" cy="55" rx="7" ry="12"/><ellipse cx="30" cy="80" rx="7" ry="12"/>
    </g>`;
  },
};

function scene(kinds, { bg = "#BEE3F8", ground = "#CDEAC0", width = 400, height = 260 } = {}) {
  const positions = [
    { x: 40, y: 40, s: 1.1 },
    { x: 210, y: 30, s: 0.85 },
    { x: 250, y: 100, s: 0.95 },
  ];
  const items = kinds.map((k, i) => {
    const fn = typeof k === "string" ? ICONS[k] : k.fn;
    const color = typeof k === "object" ? k.color : undefined;
    const p = positions[i] || positions[positions.length - 1];
    const size = 130 * p.s;
    return `<g transform="translate(${p.x - size/2},${p.y - size/2})">
      <svg x="0" y="0" width="${size}" height="${size}" viewBox="0 0 100 100">${fn(color)}</svg>
    </g>`;
  }).join("");

  return `<svg viewBox="0 0 ${width} ${height}" class="scene-svg" xmlns="http://www.w3.org/2000/svg">
    <rect x="0" y="0" width="${width}" height="${height*0.68}" fill="${bg}"/>
    <rect x="0" y="${height*0.68}" width="${width}" height="${height*0.32}" fill="${ground}"/>
    ${items}
  </svg>`;
}

function coloringScene(kinds, { width = 500, height = 380 } = {}) {
  // versão "para colorir": mesmas formas, sem preenchimento colorido (apenas contorno)
  const positions = [{x:250,y:150,s:2.1},{x:120,y:280,s:1.1},{x:380,y:280,s:1.1}];
  const items = kinds.map((k,i)=>{
    const fn = typeof k === "string" ? ICONS[k] : k.fn;
    const p = positions[i] || positions[positions.length-1];
    const size = 130*p.s;
    return `<g transform="translate(${p.x-size/2},${p.y-size/2})">
      <svg x="0" y="0" width="${size}" height="${size}" viewBox="0 0 100 100">${fn("#ffffff")}</svg>
    </g>`;
  }).join("");
  return `<svg viewBox="0 0 ${width} ${height}" class="scene-svg coloring" xmlns="http://www.w3.org/2000/svg">
    <rect x="2" y="2" width="${width-4}" height="${height-4}" rx="18" fill="#fff" stroke="#2b2b2b" stroke-width="4" stroke-dasharray="2 0"/>
    ${items}
  </svg>`;
}
