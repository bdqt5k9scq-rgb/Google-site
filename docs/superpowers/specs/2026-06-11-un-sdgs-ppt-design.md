# UN SDGs Academic Presentation — Design Spec

**Date**: 2026-06-11  
**Topic**: Generate a 22-slide English PPT from the UN SDGs promotional website  
**Tool**: `python-pptx` library → standard `.pptx` file

---

## 1. Requirements / Success Criteria

- **Output**: A single `.pptx` file (~22 slides, excl. optional appendix), openable in PowerPoint/WPS/Google Slides
- **Language**: English throughout
- **Audience**: Academic — course instructors and classmates evaluating the project
- **Content source**: All content extracted from the Vue 3 SPA (`src/views/`) and `google-sites/` HTML files
- **Visual identity**: Clean Academic style — consistent with the website's design language
- **Self-contained**: No external dependencies at presentation time; all text and styling baked into the `.pptx`

---

## 2. Visual Design System

### 2.1 Color Palette

| Role | Hex | Usage |
|------|-----|-------|
| Primary accent | `#c48b5c` | Section dividers, icons, highlights, CTA buttons |
| Background | `#fdfaf6` | Slide backgrounds (primary) |
| Surface | `#ffffff` | Cards, boxes on top of background |
| Text primary | `#1c1c24` | Headings, body text |
| Text secondary | `#6b6560` | Subtitles, captions, metadata |
| Border | `#f0ebe4` | Card borders, separators |
| Dark bg | `#0d0d18` | Section divider slides (optional contrast slides) |

### 2.2 Typography

| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| Slide title | Georgia | 28pt | 700 | `#1c1c24` |
| Section heading | Georgia | 22pt | 700 | `#1c1c24` |
| Body text | Segoe UI | 14pt | 400 | `#1c1c24` |
| Subtitle/caption | Segoe UI | 11pt | 400 | `#6b6560` |
| Accent label | Segoe UI | 10pt | 700 | `#c48b5c` |
| Stat number | Georgia | 36pt | 700 | `#c48b5c` |

### 2.3 Layout Constants

- Slide dimensions: Standard 16:9 (13.333" × 7.5" / widescreen)
- Content margins: 1.2" left/right, 1.0" top, 0.8" bottom
- Gold accent bar: 3px height, full width or left-aligned, used as section indicator
- Card style: white bg, `#f0ebe4` 1px border, 8px radius, subtle shadow

---

## 3. Slide-by-Slide Specification

### Section A: Opening (Slides 1–2)

**Slide 1 — Title**
- Dark background (`#0d0d18`) for drama, then rest of deck uses light bg
- Main title: "UN Sustainable Development Goals" (Georgia, 36pt, white)
- Subtitle: "Acting for Our Common Future" (Georgia, 20pt, `#c48b5c`)
- Bottom: Team member names, course name, date
- Decorative: thin gold line above subtitle

**Slide 2 — Agenda / Outline**
- 6 items in a 3×2 grid card layout
- Items: Introduction · The 17 Goals · Why SDGs Matter · Our Team & Project · Interactive Features · Conclusion
- Each card: white surface, numbered, gold left-border accent

### Section B: Background (Slides 3–5)

**Slide 3 — What Are the SDGs?**
- Brief definition: "17 interconnected global goals adopted by all UN Member States in 2015 as part of the 2030 Agenda"
- Timeline: 2015 (adopted) → 2023 (midpoint) → 2030 (target)
- Source: homepage hero section text

**Slide 4 — Key Statistics**
- 4 large stat cards in a horizontal row
- Numbers: 17 (Goals), 193 (Countries), 2030 (Target Year), 169 (Targets)
- Each: large Georgia number in gold, label below in gray
- Source: `Home.vue` `stats` array

**Slide 5 — Why the World Needs SDGs**
- 3-column card layout matching the homepage "why" cards
- Cards: "Unprecedented Global Challenges", "A Unified Action Framework", "Leave No One Behind"
- Each with numeric watermark (01, 02, 03) and gold left-border accent
- Source: `Home.vue` `whySDGs` array

### Section C: The 17 Goals (Slides 6–10)

**Slide 6 — Goals Overview Grid**
- 17 goals displayed in a grid (6+6+5 across 3 rows)
- Each: small colored dot + goal name + English subtitle
- Colors match official SDG colors from `Home.vue` `allSDGs`

**Slide 7 — Goals Grouped: People & Planet**
- 5P framework grouping: People (SDG 1-5), Planet (SDG 6, 12-15)
- Two-column layout with goal cards under each category

**Slide 8 — Goals Grouped: Prosperity, Peace, Partnership**
- Continuation: Prosperity (SDG 7-11), Peace (SDG 16), Partnership (SDG 17)
- Same two-column format

**Slide 9 — Spotlight: SDG 13 Climate Action**
- Deep dive on one key goal
- Icon, description, key facts about climate change
- "Take urgent action to combat climate change and its impacts"

**Slide 10 — Spotlight: SDG 4 Quality Education**
- Deep dive on education
- "Ensure inclusive and equitable quality education and promote lifelong learning opportunities for all"

### Section D: Team & Project (Slides 11–14)

**Slide 11 — Meet the Team**
- 4 member cards in a horizontal grid
- Each: avatar circle (initial), name, role, background, student ID
- Color-coded top border matching each member's color
- Source: `Home.vue` `teamMembers` array

**Slide 12 — Team SDG Assignments**
- Table mapping each member to their assigned SDGs
- Rationale for each assignment (connecting background to goals)
- Source: TeamSDGs.vue data

**Slide 13 — Project Mission & Vision**
- Two-column: Mission (left) + Vision (right)
- Below: 4 objective cards (awareness, education, collaboration, local action)
- Source: `About.vue` objectives

**Slide 14 — Website Showcase**
- Screenshots of key pages (3-4 thumbnails in a row)
- Labels: Homepage, SDGs Explorer, Carbon Calculator, Act Now
- Tech stack callout at bottom: Vue 3 + TypeScript + GSAP + Vite

### Section E: Interactive Features (Slides 15–17)

**Slide 15 — Carbon Footprint Calculator**
- Input categories: Transportation, Energy, Food, Waste
- Rating levels: Excellent (<3000), Good (<6000), Average (<10000), High (>10000)
- Sample tips output
- Source: `CarbonFootprint.vue`

**Slide 16 — Act Now: Individual Action Guide**
- Action categories with concrete steps
- Icon + action description format, 2-column grid
- Source: `ActNow.vue`

**Slide 17 — Technology & Architecture**
- Tech stack: Vue 3, TypeScript, Vue Router, GSAP animations, Vite
- Architecture diagram (simple boxes-and-arrows): 6 routes → views, no global store, scoped CSS
- Design principles: responsive, animated, accessible

### Section F: Closing (Slides 18–20)

**Slide 18 — Key Takeaways**
- 4-5 bullet points summarizing the project
- "SDGs are interconnected", "Everyone can contribute", "Technology amplifies awareness", "Local action drives global change"

**Slide 19 — Call to Action**
- Dark background slide (contrast)
- Bold quote: "Act for Our Common Future"
- Subtitle: "Start by calculating your carbon footprint. Every action counts."
- Source: homepage hero

**Slide 20 — Thank You & References**
- "Thank You" large centered text
- UN sources bullet list (UN SDG official site, IPCC reports)
- Team contact info
- Q&A prompt

### Section G: Appendix (Slides 21–22, optional)

**Slide 21 — Full 17 Goals Reference Table**
- Compact table: ID, Chinese name, English name, official color

**Slide 22 — Carbon Calculator Detailed Data**
- Formula summary, emission factors used

---

## 4. Implementation Approach

### 4.1 Tool: `python-pptx`

- Single Python script (`scripts/build-ppt.py`)
- Zero runtime dependencies beyond `python-pptx` (install: `pip install python-pptx`)
- Programmatic slide creation with helper functions for each slide "type"

### 4.2 Script Architecture

```
build-ppt.py
├── config/           # Colors, fonts, sizes constants
├── helpers/          # Reusable slide-building functions
│   ├── add_title_slide()
│   ├── add_card_slide()
│   ├── add_grid_slide()
│   ├── add_section_divider()
│   └── add_team_slide()
├── content/          # Data extracted from website source
│   ├── SDG_DATA      # 17 goals with names, colors
│   ├── TEAM_DATA     # 4 members
│   ├── STATS_DATA    # 4 key stats
│   └── WHY_DATA      # 3 reasons
└── main()            # Builds all 22 slides in sequence
```

### 4.3 Slide Type Templates

**Title Slide**: dark bg + centered text + gold line decoration
**Card Grid Slide**: section title + 3-4 cards in horizontal row
**Stats Slide**: 4 large number cards
**Grid Slide**: N×M grid of small items (for SDG overview)
**Section Divider**: dark bg, section number + title, gold accent
**Content Slide**: title + multi-paragraph body text
**Table Slide**: title + formatted table
**Team Slide**: 4 profile cards with avatar circles

---

## 5. Data Sources (within project)

| Data | Source File | Extract Method |
|------|-------------|----------------|
| 17 SDGs (names, colors) | `src/views/Home.vue` → `allSDGs` array | Hardcode into script as Python list |
| 4 team members | `src/views/Home.vue` → `teamMembers` array | Hardcode |
| 4 key stats | `src/views/Home.vue` → `stats` array | Hardcode |
| 3 "why SDGs" reasons | `src/views/Home.vue` → `whySDGs` array | Hardcode |
| Mission/vision/objectives | `src/views/About.vue` | Hardcode (translate to EN if needed) |
| Carbon calculator logic | `src/views/CarbonFootprint.vue` | Extract formulas and levels |
| Website screenshots | Browser screenshots (manual, optional) | Placeholder rectangles with labels; replace with real PNGs before presentation |

---

## 6. Out of Scope

- Live/animated content (pptx is static)
- Embedded video or audio
- Automatic data sync with live website (all data hardcoded for reproducibility)
- Translation of all Chinese content (only key terms translated; content is intentionally English per user request)

---

## 7. File Output

- **Script**: `scripts/build-ppt.py`
- **Output**: `output/UN-SDGs-Presentation.pptx`
- **Screenshots**: `output/screenshots/` (if embedded)
