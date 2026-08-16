const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const page = await browser.newPage();
  const filePath = 'file://' + path.join(__dirname, 'ebook-mapa-biblico-kids.html');
  await page.goto(filePath, { waitUntil: 'networkidle' });
  // IMPORTANT: margins must be 0 here. Each .page section in the HTML is
  // sized to exactly 297mm (A4) including its own footer text. Any nonzero
  // Playwright margin shrinks the usable print area below 297mm, which
  // pushes a sliver of every single section onto a near-blank following
  // page — that was the cause of the "blank pages" bug. Page numbers are
  // baked into the HTML (page-foot) instead of using a print footer.
  await page.pdf({
    path: path.join(__dirname, 'mapa-biblico-kids-ebook.pdf'),
    format: 'A4',
    printBackground: true,
    margin: { top: '0', bottom: '0', left: '0', right: '0' },
    displayHeaderFooter: false,
  });
  await browser.close();
  console.log('PDF written');
})();
