const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1080 }, deviceScaleFactor: 2 });
  await page.goto('file://' + path.join(__dirname, 'creative-square.html'), { waitUntil: 'networkidle' });
  await page.screenshot({ path: path.join(__dirname, 'mapa-biblico-kids-anuncio-1080x1080.png') });
  await browser.close();
  console.log('done');
})();
