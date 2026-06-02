# Assessment 3 Completion — Design Specification

**Date:** 2026-06-02  
**Project:** UN SDGs Website — static HTML pages for Google Sites embedding  
**Scope:** Complete all 4 assessment instructions with 6 static HTML pages

---

## Architecture Decision

Work exclusively on **static HTML pages** (`index.html`, `about.html`, `sdgs.html`, `carbon-footprint.html`, `act-now.html`, plus new `reference-list.html`). Vue SPA (`src/`) is left untouched. This ensures Google Sites embedding works correctly and assessment submission is self-contained.

## Files in Scope

| File | Action | Assessment Coverage |
|------|--------|-------------------|
| `index.html` | Modify — add "Why SDGs" section + full 17-goal listing | Instruction 1 |
| `about.html` | Modify — restructure team cards with photo/name/bg/aspirations | Instruction 2 |
| `sdgs.html` | Modify — add 4 member deep-dive SDG reports | Instruction 3 |
| `carbon-footprint.html` | Modify — upgrade calculator to Household/Transport/Lifestyle | Instruction 4 |
| `act-now.html` | Modify — add 4 member action reports + carbon offset plans | Instruction 4 |
| `reference-list.html` | **Create** — APA 7th formatted reference list | All instructions |
| `css/style.css` | Modify — add styles for new sections | Cross-cutting |
| `js/carbon.js` | Modify — upgrade calculator logic | Instruction 4 |

## Detailed Spec per Page

### 1. `index.html` — Home Page (Instruction 1, 10 marks)

**Additions:**
- **"Why the world needs SDGs" section** (~300 words, 4 marks): Position after stats section, before SDG highlights. Explain global challenges (climate change, inequality, poverty) and why coordinated global guidance is needed. Include APA 7th inline citations.
- **Full 17-goal grid** (4 marks): Replace the current 6-card preview with all 17 SDGs in a responsive grid. Each card: number, Chinese name, English name, brief purpose. Cards link to `sdgs.html` for detail.
- **APA citations** inline throughout the new text sections.

**Layout order:**
1. Hero (existing)
2. Stats (existing)
3. **NEW: "Why the world needs SDGs"** — 2-3 paragraphs with citations
4. SDG Highlights (expanded to 17)
5. About Preview (existing)
6. Carbon Preview (existing)

### 2. `about.html` — About Us Page (Instruction 2, 5 marks)

**Restructure team cards.** Each card must have:
- Photo placeholder (circular, with file-upload note, using existing SVG avatar pattern)
- Name (bold, prominent)
- Background (major, experience — 1 mark)
- Future vocation aspirations (1 mark)

**4 member slots** using the existing team-card layout but with expanded content:
```
[Photo Placeholder]
Name: [Member Name]
Background: [e.g., Environmental Science major, 2 years volunteer experience]
Aspiration: [e.g., Become an environmental policy advisor]
```

**Keep existing:** Mission, Vision, Objectives sections (bonus content).

### 3. `sdgs.html` — SDG Goals Page (Instruction 3, 30 marks)

**Keep existing:** 17-goal grid with modal detail view.

**Add new section:** "Member SDG Research Reports" — 4 report cards, one per member.

Each member selects a DIFFERENT SDG (no repeats). Report structure:
- **SDG Goal purpose** (3 marks): ~150 words explaining what the SDG targets
- **Adverse impact analysis** (10 marks): Cover causation, who is affected, when/where it occurs, why it harms society/nation. ~400 words with APA citations.
- **Solution proposal** (15 marks): Actions to transform society from adversity to prosperity. ~500 words with specific, actionable steps.

Member-to-SDG mapping (suggested, no overlaps):
- Member 1 → SDG 1 (No Poverty) or SDG 4 (Quality Education)
- Member 2 → SDG 3 (Good Health) or SDG 13 (Climate Action)
- Member 3 → SDG 6 (Clean Water) or SDG 14 (Life Below Water)
- Member 4 → SDG 7 (Clean Energy) or SDG 16 (Peace & Justice)

### 4. `carbon-footprint.html` — Carbon Footprint Calculator (Instruction 4 partial, ~24 marks)

**Upgrade calculator** to match assessment structure:

Three sections matching the UN ActNow calculator pattern:
1. **Household** — number of people, country, housing size, housing type
2. **Transport** — car usage, public transport, flights
3. **Lifestyle** — diet, energy use, waste

**External tool recommendation:** Add a prominent section listing 2-3 recommended external carbon footprint calculators (e.g., UN Carbon Footprint Calculator, WWF Footprint Calculator, CarbonFootprint.com) with URLs. This is for the screenshot evidence requirement.

**Screenshot guidance:** Add a visual note area showing where users should take screenshots during the calculation process.

**Result display:**
- Total kg CO₂/year
- Comparison to 2-ton target
- Level indicator (excellent/good/fair/high)
- Personalized tips

### 5. `act-now.html` — Act Now Page (Instruction 4, 55 marks)

**Keep existing:** 10 action cards with category filtering, countdown, stats.

**Add new section:** "Member Action Reports" — 4 detailed reports.

Each member selects a DIFFERENT action from the 10 listed (no repeats). Report structure:
- **Action purpose** (4 marks): ~200 words explaining the action's significance
- **Carbon footprint calculation** (20 marks): Personal calculation results with screenshot placeholders (annotated image containers) showing each step of the calculator tool used. Include tool source/reference.
- **3 carbon offset solutions** (25 marks): Three specific, actionable steps to reduce/offset carbon. Must include a photo placeholder for "eating a carrot" style personal evidence photo.

**10 actions available (from assessment):**
1. Save energy at home
2. Walk, bike, or take public transport
3. Eat more vegetables
4. Consider your travel
5. Throw away less food
6. Reduce, reuse, repair, recycle
7. Change your home's source of energy
8. Switch to an electric vehicle
9. Make your money count
10. Speak up

### 6. `reference-list.html` — Reference List (NEW, required by all instructions)

**Standalone page** linked from all other pages' nav bars.

**APA 7th format** with hanging indent (via CSS `text-indent: -2em; padding-left: 2em`).

**Categories:**
- United Nations Documents (e.g., UN 2030 Agenda, SDG reports)
- Academic & Scientific Sources (e.g., IPCC reports, journal articles)
- Institutional Reports (e.g., UNEP, WHO, WWF)
- Online Resources (e.g., UN ActNow website, carbon calculators)
- Additional References (misc.)

**Content:** Pre-populated with common SDG-related references covering all 4 instructions. Each reference entry is properly formatted.

**Navigation:** Add "Reference List" link to the navbar of ALL 6 pages.

## CSS Additions

New styles needed in `css/style.css`:
- `.member-card-detailed` — expanded about-us team cards
- `.report-card` — member SDG/action report containers
- `.reference-entry` — APA 7th hanging indent entries
- `.calculator-advanced` — upgraded calculator form fields
- `.screenshot-placeholder` — dashed-border image placeholder for screenshot evidence
- `.photo-placeholder` — dashed-circle photo upload placeholder
- `.why-sdgs-section` — new homepage section
- `.carbon-offset-card` — individual offset solution cards

## Navbar Update

All 6 pages get a new nav link: `reference-list.html` → "参考文献"

## Build & Deployment

Add a post-build step (via npm script or shell script) to copy static files to `dist/`:
```
cp index.html about.html sdgs.html act-now.html carbon-footprint.html reference-list.html dist/
cp -r css dist/
cp -r js dist/
```

## What Stays

- Navbar (mobile menu, scroll shrink)
- Footer (quick links, contact)
- GSAP scroll animations
- Existing hero/visual elements
- `css/style.css` base styles (fonts, colors, layout)
- `js/main.js` (mobile menu, modal, filters)
- Vue SPA (`src/`) — untouched
