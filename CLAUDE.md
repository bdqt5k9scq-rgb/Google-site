# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

UN SDGs (可持续发展目标) promotional website — a Vue 3 SPA. Chinese-language site covering the 17 Sustainable Development Goals, carbon footprint calculator, and action guides.

## Commands

```bash
npm run dev       # Start Vite dev server (--host 0.0.0.0)
npm run build     # Type-check (vue-tsc) then Vite production build → dist/
npm run preview   # Preview production build locally
```

`vue-tsc` runs with `noEmit: true` — type errors block the build, not just warn. Vite's dev server does NOT type-check; run `vue-tsc` manually if you want type feedback during development.

No test runner is configured.

## Architecture

### Single rendering system

Vue 3 SPA only. `index.html` is the Vite entry point (`<div id="app">` + `<script type="module" src="/src/main.ts">`).

### Entry points

| File | Role |
|------|------|
| `index.html` | **Vite SPA entry** — the single HTML entry for dev and production builds. |
| `src/main.ts` | Vue app bootstrap — creates the app, registers router, mounts to `#app`. |

### Routing

6 routes in `src/router/index.ts` using `createWebHistory()`:

| Path | Name | View |
|------|------|------|
| `/` | Home | `views/Home.vue` |
| `/about` | About | `views/About.vue` |
| `/sdgs` | SDGs | `views/SDGs.vue` |
| `/team-sdgs` | TeamSDGs | `views/TeamSDGs.vue` |
| `/carbon-footprint` | CarbonFootprint | `views/CarbonFootprint.vue` |
| `/act-now` | ActNow | `views/ActNow.vue` |

### State architecture

No Pinia/store — all state is local `ref`/`computed` within each view component.

### CSS system

- **`src/style.css`** — global styles (reset, `.container`, `.btn`, `.card`, `.section-title`). Font: Segoe UI.
- **Vue scoped styles** — component-specific styles in each `.vue` file.

### GSAP animation system

- **`src/lib/animations.ts`**: Central animation utility. Registers `ScrollTrigger` globally, sets `gsap.defaults({ ease: 'power2.out', duration: 0.6, overwrite: 'auto' })`. Exports `GSAP_EASE` presets and reusable functions.
- **Pattern**: Each view uses `onMounted(() => { gsap.context(() => { ... }) })` for cleanup-safe animations.
- **Page transitions**: `App.vue` wraps `<RouterView>` in `<Transition mode="out-in">` with GSAP hooks.
- **Card hover**: GSAP-driven (`mouseenter`/`mouseleave` with `power2.out` easing). Cards use `will-change: transform`.
- **Navbar**: `ScrollTrigger.create({ toggleClass })` toggles `.navbar-scrolled`.

### TypeScript strictness

`tsconfig.json` has `strict: true`, `noUnusedLocals: true`, `noUnusedParameters: true`.

### Path aliases

`@/` maps to `src/` via Vite alias and `tsconfig.json` paths.

### Build output

`npm run build` outputs to `dist/`. `public/` assets are copied to `dist/` as-is.

### Key dependencies

`vue@^3.4`, `vue-router@^4.3`, `gsap@^3.12`, `vite@^6.4`, `typescript@^5.4`
