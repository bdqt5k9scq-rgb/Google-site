# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

UN SDGs (可持续发展目标) promotional website — a Vue 3 SPA with static HTML fallbacks. Chinese-language site covering the 17 Sustainable Development Goals, carbon footprint calculator, and action guides.

## Commands

```bash
npm run dev       # Start Vite dev server (--host 0.0.0.0)
npm run build     # Type-check (vue-tsc) then Vite production build → dist/
npm run preview   # Preview production build locally
```

`vue-tsc` runs with `noEmit: true` — type errors block the build, not just warn. Vite's dev server does NOT type-check; run `vue-tsc` manually if you want type feedback during development.

No test runner is configured. There is no vitest, jest, or other testing framework in the project.

## Architecture

### Entry points

| File | Role |
|------|------|
| `vue-app.html` | **Vite SPA entry** — contains `<div id="app">` and `<script type="module" src="/src/main.ts">`. This is what Vite serves in dev and builds in production. |
| `index.html` | **Standalone static homepage** — a complete, self-contained HTML page with inline GSAP animations. Loads `css/style.css`, `js/main.js`, and GSAP from CDN. Does NOT mount the Vue app. |
| `about.html`, `sdgs.html`, `act-now.html`, `carbon-footprint.html` | Static HTML pages using `css/style.css` and `js/main.js`. |

### Two parallel rendering systems

1. **Vue 3 SPA** (`src/`) — the active development target. Uses `vue-app.html` as entry, `src/style.css` for global styles, Vue Router for navigation, and `src/lib/animations.ts` for GSAP.
2. **Static HTML** (`index.html`, `about.html`, `sdgs.html`, `act-now.html`, `carbon-footprint.html`) — older pages using `css/style.css` (a full ~1500-line stylesheet with Georgia/Helvetica fonts) and `js/main.js` + `js/carbon.js`. These are richer in some areas (references section, definitions, member reports, APA formatting).

Keep the two systems in sync only if explicitly asked.

### Two separate CSS systems

- **`src/style.css`** — minimal global styles for the Vue app (reset, `.container`, `.btn`, `.card`, `.section-title`). Font: Segoe UI. Colors are hardcoded (no CSS custom properties).
- **`css/style.css`** — comprehensive stylesheet for static HTML pages. Font: Georgia headings / Helvetica body. Different color values (e.g., `#0052cc` primary vs `#2563eb` in Vue). Contains styles for modals, countdown timers, definitions, references, member reports, and other static-page-only sections.

Vue component `<style scoped>` blocks duplicate much of the static-page styling independently. When adding new components, match the Vue app's visual conventions (Segoe UI font, `#2563eb` primary blue, `#1e3a5f` dark navy).

### Routing

5 routes in `src/router/index.ts` using `createWebHistory()`:

| Path | Name | View |
|------|------|------|
| `/` | Home | `views/Home.vue` |
| `/about` | About | `views/About.vue` |
| `/sdgs` | SDGs | `views/SDGs.vue` |
| `/carbon-footprint` | CarbonFootprint | `views/CarbonFootprint.vue` |
| `/act-now` | ActNow | `views/ActNow.vue` |

### State architecture

No Pinia/store — all state is local `ref`/`computed` within each view component.

### GSAP animation system

- **`src/lib/animations.ts`**: Central animation utility. Registers `ScrollTrigger` globally, sets `gsap.defaults({ ease: 'power2.out', duration: 0.6, overwrite: 'auto' })`. Exports `GSAP_EASE` presets and reusable functions (`createScrollFade`, `createStaggerFade`, `createSlideLeft`).
- **Pattern**: Each view uses `onMounted(() => { gsap.context(() => { ... }) })` for cleanup-safe animations. Do NOT use `const ctx =` — `gsap.context()` auto-reverts on unmount.
- **Page transitions**: `App.vue` wraps `<RouterView>` in `<Transition mode="out-in">` with GSAP JavaScript hooks (`onBeforeEnter/onEnter/onLeave`). `router.afterEach(() => ScrollTrigger.refresh())` ensures ScrollTrigger recalculates after SPA navigation.
- **Card hover**: GSAP-driven (`mouseenter`/`mouseleave` event listeners with `power2.out` easing) replaces CSS `transition: transform`. Cards have `will-change: transform` in CSS — remove any residual CSS `transition: transform` and `:hover { transform: translateY(...) }` rules from scoped styles when adding new cards.
- **Navbar**: `ScrollTrigger.create({ toggleClass })` toggles `.navbar-scrolled` for the shrink-on-scroll effect.

### TypeScript strictness

`tsconfig.json` has `strict: true`, `noUnusedLocals: true`, `noUnusedParameters: true`. All unused imports/variables cause build failures.

### Path aliases

`@/` maps to `src/` via Vite alias and `tsconfig.json` paths. Use `@/lib/animations` for imports.

### Build output

`npm run build` outputs to `dist/`. Vite processes `vue-app.html` as the entry point. Static assets from `public/` are copied to `dist/` as-is.

### Key dependencies

`vue@^3.4`, `vue-router@^4.3`, `gsap@^3.12`, `vite@^6.4`, `typescript@^5.4`
