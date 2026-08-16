const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const page = await browser.newPage();
  const filePath = 'file://' + path.join(__dirname, 'ebook-mapa-biblico-kids.html');
  await page.goto(filePath, { waitUntil: 'networkidle' });
  await page.pdf({
    path: path.join(__dirname, 'mapa-biblico-kids-ebook.pdf'),
    format: 'A4',
    printBackground: true,
    margin: { top: '0', bottom: '10mm', left: '0', right: '0' },
    displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate: '<div style="font-size:9px; width:100%; text-align:center; color:#b3b0a8; font-family: Nunito, sans-serif;"><span class="pageNumber"></span> / <span class="totalPages"></span></div>',
  });
  await browser.close();
  console.log('PDF written');
})();
