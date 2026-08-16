const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const page = await browser.newPage();
  const filePath = 'file://' + path.join(__dirname, 'mapa-do-coracao.html');
  await page.goto(filePath, { waitUntil: 'networkidle' });
  await page.pdf({
    path: path.join(__dirname, 'mapa-do-coracao.pdf'),
    format: 'A4',
    printBackground: true,
    margin: { top: '0', bottom: '0', left: '0', right: '0' },
    displayHeaderFooter: false,
  });
  await browser.close();
  console.log('PDF written');
})();
