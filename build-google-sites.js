/**
 * Build self-contained HTML files for Google Sites "Embed Code" blocks.
 *
 * Restructures each static HTML page so that:
 *   1. All body content (text, images, sections) is at the top, wrapped in
 *      clear "EDITABLE" markers — edit Chinese text between the markers.
 *   2. Inlined CSS sits in <head>.
 *   3. All scripts sit at the bottom, AFTER the editable block.
 *   4. GSAP CDN <script> tags load BEFORE inlined local JS, fixing the
 *      ordering bug where inline scripts referenced gsap/ScrollTrigger
 *      before the CDN had loaded.
 *   5. carbon.js is inlined only into carbon-footprint.html.
 */

import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const outDir = join(__dirname, 'google-sites');
const srcDir = __dirname;

// Read shared assets once
const css = readFileSync(join(srcDir, 'css', 'style.css'), 'utf-8');
const mainJs = readFileSync(join(srcDir, 'js', 'main.js'), 'utf-8');
const carbonJs = readFileSync(join(srcDir, 'js', 'carbon.js'), 'utf-8');

// Pages that need carbon.js inlined
const carbonPages = ['carbon-footprint.html'];

// All static HTML pages to process
const pages = [
  'index.html',
  'about.html',
  'sdgs.html',
  'act-now.html',
  'carbon-footprint.html',
  'reference-list.html',
  'team-sdgs.html',
];

// GSAP CDN URLs — preserved as external <script> tags (they're absolute)
const GSAP_CDN = 'https://cdn.jsdelivr.net/npm/gsap@3.12/dist/gsap.min.js';
const SCROLL_TRIGGER_CDN = 'https://cdn.jsdelivr.net/npm/gsap@3.12/dist/ScrollTrigger.min.js';

// Ensure output directory
if (!existsSync(outDir)) mkdirSync(outDir, { recursive: true });

for (const page of pages) {
  let html = readFileSync(join(srcDir, page), 'utf-8');

  // ── Step 1: Inline CSS in <head> ────────────────────────────────
  html = html.replace(
    '<link rel="stylesheet" href="css/style.css">',
    `<style>\n/* === Inlined from css/style.css === */\n${css}\n</style>`
  );

  // ── Step 2: Split body into content + scripts ───────────────────
  //    Find the first <script> tag inside <body> — everything before
  //    it is user-visible content.
  const bodyOpenIdx = html.indexOf('<body>');
  const firstScriptIdx = html.indexOf('<script', bodyOpenIdx);

  if (bodyOpenIdx === -1 || firstScriptIdx === -1) {
    console.error(`❌ ${page} — could not parse body/script structure`);
    continue;
  }

  // Content: everything between <body> (exclusive) and the first <script>
  const contentStart = bodyOpenIdx + '<body>'.length;
  let content = html.slice(contentStart, firstScriptIdx).trim();

  // Strip <nav> — Google Sites provides its own navigation
  content = content.replace(/<nav\b[^>]*>[\s\S]*?<\/nav>/gi, '<!-- navbar removed — use Google Sites navigation -->');

  // Scripts region: from first <script> to </body>
  const bodyCloseIdx = html.lastIndexOf('</body>');
  const scriptsRegion = html.slice(firstScriptIdx, bodyCloseIdx);

  // ── Step 3: Extract the inline animation <script> block ─────────
  //    Each page has an inline <script>…</script> at the very end
  //    that calls gsap.registerPlugin(ScrollTrigger) and sets up
  //    page-specific animations. We extract it so we can place it
  //    AFTER the GSAP CDN loads.
  const inlineScriptMatch = scriptsRegion.match(
    /<script>\s*\n\s*(gsap\.registerPlugin[\s\S]*?)<\/script>/i
  );
  const inlineAnimCode = inlineScriptMatch ? inlineScriptMatch[1].trim() : '';

  // ── Step 4: Build the final <body> ──────────────────────────────
  const needsCarbon = carbonPages.includes(page);

  const bodyContent =
    '\n' +
    '<!-- ═══════════════════════════════════════════════════════════ -->\n' +
    '<!-- 📝 EDITABLE CONTENT START                                  -->\n' +
    '<!--     改文字只需编辑这一块 HTML，下面的样式和脚本不要动       -->\n' +
    '<!-- ═══════════════════════════════════════════════════════════ -->\n' +
    content +
    '\n' +
    '<!-- ═══════════════════════════════════════════════════════════ -->\n' +
    '<!-- 📝 EDITABLE CONTENT END                                    -->\n' +
    '<!-- ═══════════════════════════════════════════════════════════ -->\n' +
    '\n' +
    '<!-- ═══════════════════════════════════════════════════════════ -->\n' +
    '<!-- 🔧 SCRIPTS — 编辑时不需要动下面的内容                       -->\n' +
    '<!-- ═══════════════════════════════════════════════════════════ -->\n' +
    '\n' +
    '<!-- GSAP library (must load first) -->\n' +
    `<script src="${GSAP_CDN}"></script>\n` +
    `<script src="${SCROLL_TRIGGER_CDN}"></script>\n` +
    '\n' +
    '<!-- Site shared JS -->\n' +
    `<script>\n/* === Inlined from js/main.js === */\n${mainJs}\n</script>\n` +
    (needsCarbon
      ? `\n<!-- Carbon calculator JS -->\n<script>\n/* === Inlined from js/carbon.js === */\n${carbonJs}\n</script>\n`
      : '') +
    '\n' +
    '<!-- Page-specific animations -->\n' +
    `<script>\n${inlineAnimCode}\n</script>\n`;

  // ── Step 5: Reassemble the full HTML ────────────────────────────
  const headCloseIdx = html.indexOf('</head>');
  const head = html.slice(0, headCloseIdx);
  const tail = html.slice(bodyCloseIdx); // </body>\n</html>

  const out = head + '\n</head>\n<body>' + bodyContent + tail;

  writeFileSync(join(outDir, page), out, 'utf-8');
  console.log(`✅ ${page} — ${(Buffer.byteLength(out, 'utf-8') / 1024).toFixed(1)} KB`);
}

console.log(`\n🎉 Done! Output: ${outDir}`);
console.log('   Paste each file\'s content into Google Sites → Embed Code.');
console.log('   Edit text between the 📝 EDITABLE markers.');
