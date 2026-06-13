# UN SDGs PPT Generator — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** A single Python script (`scripts/build-ppt.py`) that generates a 22-slide `.pptx` academic presentation using `python-pptx`, styled in Clean Academic aesthetic matching the website's design language.

**Architecture:** Single-file script with inline data and reusable builder functions. No external data files — all SDG data, team info, and text content is hardcoded as Python constants at the top of the script. The script builds slides sequentially: setup → section A (opening) → section B (background) → section C (goals) → section D (team) → section E (features) → section F (closing) → section G (appendix) → save.

**Tech Stack:** Python 3, `python-pptx` (latest), standard library only

---

## File Map

| File | Role |
|------|------|
| `scripts/build-ppt.py` | **Single script** — config constants, data, helpers, slide builders, main() |
| `output/UN-SDGs-Presentation.pptx` | **Generated output** — the 22-slide presentation |
| `output/screenshots/` | **Optional** — placeholder for manual screenshots |

---

### Task 1: Project Setup — Install dependency and scaffold

**Files:**
- Create: `scripts/build-ppt.py` (skeleton only)

- [ ] **Step 1: Install python-pptx**

```bash
pip install python-pptx
```
Expected: `Successfully installed python-pptx-X.X.X`

- [ ] **Step 2: Create script skeleton with docstring**

```python
"""
UN SDGs Academic Presentation Builder
Generates a 22-slide .pptx presentation from hardcoded data.
Output: output/UN-SDGs-Presentation.pptx
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
import os

def main():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    # TODO: build slides
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "UN-SDGs-Presentation.pptx")
    prs.save(output_path)
    print(f"Saved: {output_path}")

if __name__ == "__main__":
    main()
```

- [ ] **Step 3: Run to verify it produces a valid empty pptx**

```bash
python scripts/build-ppt.py
```
Expected: `Saved: output/UN-SDGs-Presentation.pptx` and file exists (~28KB, one blank slide).

- [ ] **Step 4: Commit**

```bash
git add scripts/build-ppt.py output/.gitkeep
git commit -m "feat: scaffold ppt builder with python-pptx dependency"
```

---

### Task 2: Configuration constants and color palette

**Files:**
- Modify: `scripts/build-ppt.py` (add config section after imports)

- [ ] **Step 1: Add all color and typography constants**

Replace `# TODO: build slides` with:

```python
# ── Color Palette ──────────────────────────────────────────────
C_PRIMARY      = RGBColor(0xC4, 0x8B, 0x5C)  # Antique Gold
C_BG           = RGBColor(0xFD, 0xFA, 0xF6)  # Warm Cream
C_SURFACE      = RGBColor(0xFF, 0xFF, 0xFF)  # White
C_TEXT         = RGBColor(0x1C, 0x1C, 0x24)  # Dark Charcoal
C_TEXT_SEC     = RGBColor(0x6B, 0x65, 0x60)  # Warm Gray
C_BORDER       = RGBColor(0xF0, 0xEB, 0xE4)  # Light border
C_DARK_BG      = RGBColor(0x0D, 0x0D, 0x18)  # Deep Navy
C_WHITE        = RGBColor(0xFF, 0xFF, 0xFF)

# SDG official colors (from Home.vue allSDGs)
SDG_COLORS = {
    1:  RGBColor(0xE5, 0x24, 0x3B), 2:  RGBColor(0xDD, 0xA6, 0x3A),
    3:  RGBColor(0x4C, 0x9F, 0x38), 4:  RGBColor(0xC5, 0x19, 0x2D),
    5:  RGBColor(0xFF, 0x3A, 0x21), 6:  RGBColor(0x26, 0xBD, 0xE2),
    7:  RGBColor(0xFC, 0xC3, 0x0B), 8:  RGBColor(0xA2, 0x19, 0x42),
    9:  RGBColor(0xFD, 0x69, 0x25), 10: RGBColor(0xDD, 0x13, 0x67),
    11: RGBColor(0xFD, 0x9D, 0x24), 12: RGBColor(0xBF, 0x8B, 0x2E),
    13: RGBColor(0x3F, 0x7E, 0x44), 14: RGBColor(0x00, 0x94, 0x44),
    15: RGBColor(0x00, 0xA6, 0x51), 16: RGBColor(0x19, 0x48, 0x9D),
    17: RGBColor(0x19, 0x28, 0x41),
}

# ── Typography ──────────────────────────────────────────────────
FONT_TITLE   = "Georgia"
FONT_BODY    = "Segoe UI"
SIZE_TITLE   = Pt(28)
SIZE_HEADING = Pt(22)
SIZE_BODY    = Pt(14)
SIZE_CAPTION = Pt(11)
SIZE_LABEL   = Pt(10)
SIZE_STAT    = Pt(36)

# ── Layout ──────────────────────────────────────────────────────
SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)
MARGIN_L = Inches(1.2)
MARGIN_R = Inches(1.2)
MARGIN_T = Inches(1.0)
CONTENT_W = Inches(13.333 - 1.2 - 1.2)  # ~10.93"
```

- [ ] **Step 2: Run script to verify no import/syntax errors**

```bash
python scripts/build-ppt.py
```
Expected: Same output as before (no errors).

- [ ] **Step 3: Commit**

```bash
git add scripts/build-ppt.py
git commit -m "feat: add color palette, typography, and layout config"
```

---

### Task 3: Helper functions — background, text, shapes

**Files:**
- Modify: `scripts/build-ppt.py` (add helpers after config, before main)

- [ ] **Step 1: Add slide-level helper functions**

Insert after layout constants, before `main()`:

```python
# ── Helpers ────────────────────────────────────────────────────

def set_slide_bg(slide, color):
    """Set solid background color on a slide."""
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_textbox(slide, left, top, width, height, text="",
                font_name=FONT_BODY, font_size=SIZE_BODY,
                color=C_TEXT, bold=False, alignment=PP_ALIGN.LEFT,
                line_spacing=1.3):
    """Add a text box and return (shape, text_frame)."""
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.name = font_name
    p.font.size = font_size
    p.font.color.rgb = color
    p.font.bold = bold
    p.alignment = alignment
    p.space_after = Pt(line_spacing * 2)
    return txBox, tf

def add_paragraph(tf, text, font_name=FONT_BODY, font_size=SIZE_BODY,
                  color=C_TEXT, bold=False, alignment=PP_ALIGN.LEFT,
                  space_after=Pt(6)):
    """Add a new paragraph to an existing text frame."""
    p = tf.add_paragraph()
    p.text = text
    p.font.name = font_name
    p.font.size = font_size
    p.font.color.rgb = color
    p.font.bold = bold
    p.alignment = alignment
    p.space_after = space_after
    return p

def add_rounded_rect(slide, left, top, width, height, fill_color=C_SURFACE,
                     border_color=C_BORDER, border_width=Pt(1)):
    """Add a rounded rectangle shape, return the shape."""
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    shape.line.color.rgb = border_color
    shape.line.width = border_width
    return shape

def add_accent_bar(slide, left, top, width, height=Inches(0.05), color=C_PRIMARY):
    """Add a thin gold accent bar."""
    shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, left, top, width, height
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()  # no border
    return shape
```

- [ ] **Step 2: Run script to verify no errors**

```bash
python scripts/build-ppt.py
```
Expected: No errors. (Helpers defined but not yet called.)

- [ ] **Step 3: Commit**

```bash
git add scripts/build-ppt.py
git commit -m "feat: add slide helper functions (bg, textbox, shapes)"
```

---

### Task 4: Data — SDGs, team, stats, and text content

**Files:**
- Modify: `scripts/build-ppt.py` (add data section after helpers, before main)

- [ ] **Step 1: Add all hardcoded data**

Insert after helpers, before `main()`:

```python
# ── Data ───────────────────────────────────────────────────────

SDG_DATA = [
    {"id": 1,  "name": "End Poverty",         "en": "No Poverty"},
    {"id": 2,  "name": "Zero Hunger",           "en": "Zero Hunger"},
    {"id": 3,  "name": "Good Health",         "en": "Good Health"},
    {"id": 4,  "name": "Quality Education",         "en": "Quality Education"},
    {"id": 5,  "name": "Gender Equality",         "en": "Gender Equality"},
    {"id": 6,  "name": "Clean Water",         "en": "Clean Water"},
    {"id": 7,  "name": "Clean Energy",         "en": "Clean Energy"},
    {"id": 8,  "name": "Decent Work",         "en": "Decent Work"},
    {"id": 9,  "name": "Industry & Innovation",         "en": "Industry & Innovation"},
    {"id": 10, "name": "Reduced Inequalities",       "en": "Reduced Inequalities"},
    {"id": 11, "name": "Sustainable Cities",       "en": "Sustainable Cities"},
    {"id": 12, "name": "Responsible Consumption",       "en": "Responsible Consumption"},
    {"id": 13, "name": "Climate Action",         "en": "Climate Action"},
    {"id": 14, "name": "Life Below Water",         "en": "Life Below Water"},
    {"id": 15, "name": "Life on Land",         "en": "Life on Land"},
    {"id": 16, "name": "Peace & Justice",         "en": "Peace & Justice"},
    {"id": 17, "name": "Partnerships",         "en": "Partnerships"},
]

# 5P framework groupings
SDG_GROUPS = {
    "People":       {"goals": [1, 2, 3, 4, 5],   "desc": "End poverty and hunger, ensure dignity and equality"},
    "Planet":       {"goals": [6, 12, 13, 14, 15], "desc": "Protect natural resources and climate for future generations"},
    "Prosperity":   {"goals": [7, 8, 9, 10, 11], "desc": "Ensure prosperous and fulfilling lives in harmony with nature"},
    "Peace":        {"goals": [16],               "desc": "Foster peaceful, just, and inclusive societies"},
    "Partnership":  {"goals": [17],               "desc": "Strengthen global solidarity and means of implementation"},
}

STATS_DATA = [
    {"number": "17",  "label": "Sustainable Development Goals"},
    {"number": "193", "label": "Member States Committed"},
    {"number": "2030","label": "Target Year for Achievement"},
    {"number": "169", "label": "Specific Action Targets"},
]

WHY_DATA = [
    {
        "title": "Unprecedented Global Challenges",
        "text": "Climate change drives extreme weather with global temperatures up 1.1°C since pre-industrial times. Over 700 million people still live in extreme poverty. No single nation can solve these challenges alone."
    },
    {
        "title": "A Unified Action Framework",
        "text": "The SDGs provide an integrated framework recognizing that economic development, social inclusion, and environmental protection are inseparable. This systemic thinking ensures solving one problem does not worsen another."
    },
    {
        "title": "Leave No One Behind",
        "text": "With 169 specific targets and 232 indicators, the SDGs enable coordinated action across governments, businesses, civil society, and individuals — ensuring development reaches the most vulnerable populations."
    },
]

TEAM_DATA = [
    {"name": "Li Shuhang",   "role": "Project Lead",      "bg": "Environmental Science",  "id": "8168667", "color": RGBColor(0x2C, 0x5F, 0x2D)},
    {"name": "Feng Jingyi",  "role": "Tech Development",  "bg": "Computer Science",       "id": "8168308", "color": RGBColor(0x1A, 0x3A, 0x5C)},
    {"name": "Wang Luyang",  "role": "Policy Research",   "bg": "International Affairs",  "id": "8168505", "color": RGBColor(0x5C, 0x2D, 0x6E)},
    {"name": "Lu Jianning",  "role": "Data Analyst",      "bg": "Statistics",             "id": "8168379", "color": RGBColor(0xB8, 0x57, 0x3E)},
]

TEAM_SDG_MAP = [
    {"name": "Li Shuhang",   "sdgs": "SDG 6, 7, 13, 14, 15", "rationale": "Environmental science background aligns with planet-focused goals"},
    {"name": "Feng Jingyi",  "sdgs": "SDG 8, 9, 11, 12",     "rationale": "CS expertise drives tech-enabled sustainable industry and cities"},
    {"name": "Wang Luyang",  "sdgs": "SDG 1, 2, 5, 10, 16",  "rationale": "International affairs knowledge supports equity and justice goals"},
    {"name": "Lu Jianning",  "sdgs": "SDG 3, 4, 17",         "rationale": "Statistics background enables data-driven health and education analysis"},
]

AGENDA_ITEMS = [
    "Introduction to the SDGs",
    "The 17 Sustainable Development Goals",
    "Why the World Needs SDGs",
    "Our Team & Project Mission",
    "Interactive Features & Technology",
    "Key Takeaways & Call to Action",
]

OBJECTIVES_DATA = [
    {"title": "Public Awareness", "desc": "Increase public awareness and understanding of the SDGs"},
    {"title": "Educational Resources", "desc": "Provide educational tools and resources for individuals and organizations"},
    {"title": "Cross-Disciplinary Collaboration", "desc": "Promote interdisciplinary cooperation and knowledge sharing"},
    {"title": "Localized Action", "desc": "Drive localized sustainable development action and practice"},
]

CARBON_CATEGORIES = [
    {"name": "Transportation", "factors": ["Car distance: 0.2 kg CO₂/km", "Public transport: 0.05 kg/km", "Flights: 250 kg/flight"]},
    {"name": "Energy", "factors": ["Electricity: 0.5 kg/kWh", "Gas: 2.3 kg/m³", "Heating: 1.8 kg/unit"]},
    {"name": "Food", "factors": ["Meat consumption: reduction credit", "Local food sourcing: 0.1 kg benefit"]},
    {"name": "Waste", "factors": ["Recycling: -100 kg if not done", "Composting: -50 kg if not done"]},
]

CARBON_LEVELS = [
    {"level": "Excellent", "range": "< 3,000 kg/year", "color": RGBColor(0x5C, 0x8D, 0x6D)},
    {"level": "Good",      "range": "3,000 – 6,000",    "color": RGBColor(0x2C, 0x52, 0x82)},
    {"level": "Average",   "range": "6,000 – 10,000",   "color": C_PRIMARY},
    {"level": "High",      "range": "> 10,000 kg/year",  "color": RGBColor(0xB8, 0x57, 0x3E)},
]

ACTION_ITEMS = [
    {"category": "Transport", "actions": ["Use public transit or bicycle instead of driving", "Reduce long-distance flights; consider video conferencing"]},
    {"category": "Energy",    "actions": ["Use energy-efficient appliances", "Turn off lights and devices when not in use"]},
    {"category": "Food",      "actions": ["Reduce meat consumption; eat more plant-based foods", "Choose locally sourced food products"]},
    {"category": "Waste",     "actions": ["Start waste sorting and recycling", "Try composting kitchen waste"]},
]

TECH_STACK = [
    {"layer": "Frontend Framework", "tech": "Vue 3 (Composition API)"},
    {"layer": "Language",           "tech": "TypeScript (strict mode)"},
    {"layer": "Routing",            "tech": "Vue Router 4 (history mode)"},
    {"layer": "Animations",         "tech": "GSAP + ScrollTrigger"},
    {"layer": "Build Tool",         "tech": "Vite 6"},
    {"layer": "Styling",            "tech": "Scoped CSS + Global Styles"},
]
```

- [ ] **Step 2: Run script to verify no syntax errors**

```bash
python scripts/build-ppt.py
```
Expected: No errors, same blank output.

- [ ] **Step 3: Commit**

```bash
git add scripts/build-ppt.py
git commit -m "feat: add all data constants (SDGs, team, stats, carbon, actions)"
```

---

### Task 5: Slide builder functions — title, agenda, content templates

**Files:**
- Modify: `scripts/build-ppt.py` (add builder functions after data, before main)

- [ ] **Step 1: Add slide type builders**

Insert after data section, before `main()`:

```python
# ── Slide Builders ─────────────────────────────────────────────

def build_title_slide(prs):
    """Slide 1: Dark title slide."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank
    set_slide_bg(slide, C_DARK_BG)

    # Gold accent line
    add_accent_bar(slide, Inches(5.0), Inches(2.8), Inches(3.3), Inches(0.04), C_PRIMARY)

    # Main title
    add_textbox(slide, Inches(1.5), Inches(1.2), Inches(10.3), Inches(1.5),
                "UN Sustainable Development Goals",
                font_name=FONT_TITLE, font_size=Pt(38), color=C_WHITE,
                bold=True, alignment=PP_ALIGN.CENTER)

    # Subtitle
    add_textbox(slide, Inches(1.5), Inches(3.1), Inches(10.3), Inches(0.8),
                "Acting for Our Common Future",
                font_name=FONT_TITLE, font_size=Pt(22), color=C_PRIMARY,
                alignment=PP_ALIGN.CENTER)

    # Team info
    _, tf = add_textbox(slide, Inches(2.0), Inches(5.0), Inches(9.3), Inches(1.5),
                        "Li Shuhang · Feng Jingyi · Wang Luyang · Lu Jianning",
                        font_name=FONT_BODY, font_size=SIZE_BODY, color=RGBColor(0xAA, 0xAA, 0xBB),
                        alignment=PP_ALIGN.CENTER)
    add_paragraph(tf, "Course Presentation · June 2026",
                  font_size=SIZE_CAPTION, color=C_TEXT_SEC, alignment=PP_ALIGN.CENTER)

    return slide

def build_light_slide(prs, title_text):
    """Create a light-bg slide with a title and return (slide, content_top)."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank
    set_slide_bg(slide, C_BG)

    # Gold left accent bar
    add_accent_bar(slide, MARGIN_L, Inches(0.95), Inches(0.6), Inches(0.04))

    # Title
    add_textbox(slide, MARGIN_L, Inches(0.6), CONTENT_W, Inches(0.7),
                title_text, font_name=FONT_TITLE, font_size=SIZE_TITLE,
                color=C_TEXT, bold=True)

    return slide

def build_light_slide_no_accent(prs, title_text):
    """Create a light-bg slide without the accent bar (for continuation slides)."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, C_BG)
    add_textbox(slide, MARGIN_L, Inches(0.6), CONTENT_W, Inches(0.7),
                title_text, font_name=FONT_TITLE, font_size=SIZE_TITLE,
                color=C_TEXT, bold=True)
    return slide

def build_dark_slide(prs, title_text):
    """Create a dark-bg slide with centered title."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, C_DARK_BG)
    add_accent_bar(slide, Inches(5.5), Inches(3.3), Inches(2.3), Inches(0.04), C_PRIMARY)
    add_textbox(slide, Inches(1.0), Inches(2.6), Inches(11.3), Inches(1.0),
                title_text, font_name=FONT_TITLE, font_size=Pt(32),
                color=C_WHITE, bold=True, alignment=PP_ALIGN.CENTER)
    return slide

def add_card(slide, left, top, width, height, title="", body="",
             title_color=C_TEXT, body_color=C_TEXT_SEC, fill_color=C_SURFACE):
    """Add a white card with title and body text; returns the card shape."""
    card = add_rounded_rect(slide, left, top, width, height, fill_color=fill_color)
    # Title inside card
    inner_l = left + Inches(0.25)
    inner_t = top + Inches(0.2)
    inner_w = width - Inches(0.5)
    add_textbox(slide, inner_l, inner_t, inner_w, Inches(0.5),
                title, font_name=FONT_TITLE, font_size=SIZE_HEADING,
                color=title_color, bold=True)
    # Body inside card
    add_textbox(slide, inner_l, inner_t + Inches(0.55), inner_w, height - Inches(0.85),
                body, font_name=FONT_BODY, font_size=SIZE_CAPTION,
                color=body_color)
    return card

def add_gold_left_accent_card(slide, left, top, width, height, title="", body=""):
    """Card with a gold left border accent (like homepage why-cards)."""
    card = add_rounded_rect(slide, left, top, width, height)
    # Gold accent on left side
    accent = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, left, top, Inches(0.06), height
    )
    accent.fill.solid()
    accent.fill.fore_color.rgb = C_PRIMARY
    accent.line.fill.background()
    # Text
    add_textbox(slide, left + Inches(0.35), top + Inches(0.2),
                width - Inches(0.55), Inches(0.5),
                title, font_name=FONT_TITLE, font_size=Pt(18), color=C_TEXT, bold=True)
    add_textbox(slide, left + Inches(0.35), top + Inches(0.65),
                width - Inches(0.55), height - Inches(0.85),
                body, font_name=FONT_BODY, font_size=SIZE_CAPTION, color=C_TEXT_SEC)
    return card
```

- [ ] **Step 2: Run script to verify no errors**

```bash
python scripts/build-ppt.py
```

- [ ] **Step 3: Commit**

```bash
git add scripts/build-ppt.py
git commit -m "feat: add slide builder functions (title, light/dark, card templates)"
```

---

### Task 6: Build Section A — Opening slides (1–2)

**Files:**
- Modify: `scripts/build-ppt.py` (replace `# TODO: build slides` in main())

- [ ] **Step 1: Add Slide 1 (Title) and Slide 2 (Agenda) calls in main()**

Replace `# TODO: build slides` with:

```python
    # ── Section A: Opening ──
    build_title_slide(prs)                       # Slide 1

    # Slide 2: Agenda
    slide2 = build_light_slide(prs, "Presentation Outline")
    card_w = Inches(3.2)
    card_h = Inches(1.7)
    gap = Inches(0.25)
    start_x = MARGIN_L
    start_y = Inches(1.8)
    for i, item in enumerate(AGENDA_ITEMS):
        col = i % 3
        row = i // 3
        x = start_x + col * (card_w + gap)
        y = start_y + row * (card_h + gap)
        add_gold_left_accent_card(slide2, x, y, card_w, card_h,
                                  title=f"0{i+1}. {item}",
                                  body="" if i < 3 else "")
```

- [ ] **Step 2: Run and verify 2 slides generated**

```bash
python scripts/build-ppt.py
```

- [ ] **Step 3: Commit**

```bash
git add scripts/build-ppt.py
git commit -m "feat: build Section A — title slide and agenda"
```

---

### Task 7: Build Section B — Background slides (3–5)

**Files:**
- Modify: `scripts/build-ppt.py` (append to main())

- [ ] **Step 1: Add Slides 3–5**

Insert after Slide 2 code in main():

```python
    # ── Section B: Background ──
    # Slide 3: What Are the SDGs?
    slide3 = build_light_slide(prs, "What Are the SDGs?")
    _, tf3 = add_textbox(slide3, MARGIN_L, Inches(1.6), CONTENT_W, Inches(1.0),
                         "The Sustainable Development Goals (SDGs) are 17 interconnected global goals "
                         "adopted by all United Nations Member States in 2015 as part of the 2030 Agenda "
                         "for Sustainable Development — a shared blueprint for peace and prosperity for "
                         "people and the planet, now and into the future.",
                         font_size=SIZE_BODY, color=C_TEXT)
    # Timeline boxes
    timeline = [("2015", "SDGs Adopted\nby 193 countries"), ("2023", "Midpoint Review\nProgress assessed"), ("2030", "Target Year\nGoals to be achieved")]
    for i, (year, desc) in enumerate(timeline):
        x = Inches(2.0) + i * Inches(3.5)
        y = Inches(4.0)
        # Year circle
        circ = slide3.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.6), y, Inches(1.1), Inches(1.1))
        circ.fill.solid(); circ.fill.fore_color.rgb = C_PRIMARY
        circ.line.fill.background()
        tf_c = circ.text_frame; tf_c.word_wrap = True
        p_c = tf_c.paragraphs[0]; p_c.text = year; p_c.font.size = Pt(14)
        p_c.font.color.rgb = C_WHITE; p_c.font.bold = True
        p_c.alignment = PP_ALIGN.CENTER
        # Description below
        add_textbox(slide3, x, y + Inches(1.3), Inches(2.3), Inches(0.8),
                    desc, font_size=SIZE_CAPTION, color=C_TEXT_SEC, alignment=PP_ALIGN.CENTER)

    # Slide 4: Key Statistics
    slide4 = build_light_slide(prs, "Key Statistics")
    stat_w = Inches(2.3); stat_h = Inches(2.5)
    stat_gap = Inches(0.4)
    stat_total_w = 4 * stat_w + 3 * stat_gap
    stat_start_x = (SLIDE_W - stat_total_w) // 2
    for i, stat in enumerate(STATS_DATA):
        x = stat_start_x + i * (stat_w + stat_gap)
        y = Inches(2.5)
        card = add_rounded_rect(slide4, x, y, stat_w, stat_h)
        add_textbox(slide4, x + Inches(0.2), y + Inches(0.3), stat_w - Inches(0.4), Inches(1.2),
                    stat["number"], font_name=FONT_TITLE, font_size=Pt(40),
                    color=C_PRIMARY, bold=True, alignment=PP_ALIGN.CENTER)
        add_textbox(slide4, x + Inches(0.2), y + Inches(1.6), stat_w - Inches(0.4), Inches(0.8),
                    stat["label"], font_name=FONT_BODY, font_size=SIZE_CAPTION,
                    color=C_TEXT_SEC, alignment=PP_ALIGN.CENTER)

    # Slide 5: Why the World Needs SDGs
    slide5 = build_light_slide(prs, "Why the World Needs SDGs")
    why_w = Inches(3.4); why_h = Inches(3.8)
    why_gap = Inches(0.3)
    why_total_w = 3 * why_w + 2 * why_gap
    why_start_x = (SLIDE_W - why_total_w) // 2
    for i, why in enumerate(WHY_DATA):
        x = why_start_x + i * (why_w + why_gap)
        y = Inches(2.2)
        add_gold_left_accent_card(slide5, x, y, why_w, why_h,
                                  title=why["title"], body=why["text"])
```

- [ ] **Step 2: Run and verify 5 slides**

```bash
python scripts/build-ppt.py
```

- [ ] **Step 3: Commit**

```bash
git add scripts/build-ppt.py
git commit -m "feat: build Section B — what are SDGs, stats, why SDGs matter"
```

---

### Task 8: Build Section C — The 17 Goals (slides 6–10)

**Files:**
- Modify: `scripts/build-ppt.py` (append to main())

- [ ] **Step 1: Add Slides 6–10**

Insert after Slide 5 code in main():

```python
    # ── Section C: The 17 Goals ──
    # Slide 6: Goals Overview Grid
    slide6 = build_light_slide(prs, "The 17 Sustainable Development Goals")
    grid_item_w = Inches(1.55); grid_item_h = Inches(1.05)
    grid_gap_x = Inches(0.15); grid_gap_y = Inches(0.15)
    grid_cols = 6
    grid_start_x = MARGIN_L; grid_start_y = Inches(1.8)
    for i, sdg in enumerate(SDG_DATA):
        col = i % grid_cols
        row = i // grid_cols
        x = grid_start_x + col * (grid_item_w + grid_gap_x)
        y = grid_start_y + row * (grid_item_h + grid_gap_y)
        color = SDG_COLORS[sdg["id"]]
        # Card with color tint
        card = add_rounded_rect(slide6, x, y, grid_item_w, grid_item_h,
                                fill_color=color, border_color=color)
        # Number
        add_textbox(slide6, x + Inches(0.1), y + Inches(0.05), Inches(0.4), Inches(0.35),
                    f"{sdg['id']:02d}", font_name=FONT_TITLE, font_size=Pt(11),
                    color=RGBColor(0xFF,0xFF,0xFF), bold=True)
        # English name
        add_textbox(slide6, x + Inches(0.1), y + Inches(0.45), grid_item_w - Inches(0.2), Inches(0.55),
                    sdg["en"], font_name=FONT_BODY, font_size=Pt(8),
                    color=RGBColor(0xFF,0xFF,0xFF))

    # Slide 7: Goals Grouped — People & Planet
    slide7 = build_light_slide(prs, "Goals Grouped — The 5P Framework")
    groups_list = list(SDG_GROUPS.items())
    col_w = Inches(5.1); col_h = Inches(2.4)
    for i, (group_name, group_data) in enumerate(groups_list[:2]):
        col = i % 2
        row = i // 2
        x = MARGIN_L + col * (col_w + Inches(0.3))
        y = Inches(1.8) + row * (col_h + Inches(0.2))
        card = add_rounded_rect(slide7, x, y, col_w, col_h)
        add_textbox(slide7, x + Inches(0.25), y + Inches(0.15), col_w - Inches(0.5), Inches(0.4),
                    group_name, font_name=FONT_TITLE, font_size=Pt(18), color=C_PRIMARY, bold=True)
        add_textbox(slide7, x + Inches(0.25), y + Inches(0.5), col_w - Inches(0.5), Inches(0.4),
                    group_data["desc"], font_name=FONT_BODY, font_size=SIZE_CAPTION, color=C_TEXT_SEC)
        # Goal chips
        chip_text = " · ".join([f"SDG {gid}" for gid in group_data["goals"]])
        add_textbox(slide7, x + Inches(0.25), y + Inches(1.0), col_w - Inches(0.5), Inches(0.8),
                    chip_text, font_name=FONT_BODY, font_size=SIZE_CAPTION, color=C_TEXT)

    # Slide 8: Goals Grouped — Prosperity, Peace, Partnership
    slide8 = build_light_slide_no_accent(prs, "Goals Grouped — Prosperity, Peace & Partnership")
    for i, (group_name, group_data) in enumerate(groups_list[2:]):
        col = i % 2
        row = i // 2
        x = MARGIN_L + col * (col_w + Inches(0.3))
        y = Inches(1.8) + row * (col_h + Inches(0.2))
        card = add_rounded_rect(slide8, x, y, col_w, col_h)
        add_textbox(slide8, x + Inches(0.25), y + Inches(0.15), col_w - Inches(0.5), Inches(0.4),
                    group_name, font_name=FONT_TITLE, font_size=Pt(18), color=C_PRIMARY, bold=True)
        add_textbox(slide8, x + Inches(0.25), y + Inches(0.5), col_w - Inches(0.5), Inches(0.4),
                    group_data["desc"], font_name=FONT_BODY, font_size=SIZE_CAPTION, color=C_TEXT_SEC)
        chip_text = " · ".join([f"SDG {gid}" for gid in group_data["goals"]])
        add_textbox(slide8, x + Inches(0.25), y + Inches(1.0), col_w - Inches(0.5), Inches(0.8),
                    chip_text, font_name=FONT_BODY, font_size=SIZE_CAPTION, color=C_TEXT)

    # Slide 9: Spotlight — SDG 13 Climate Action
    slide9 = build_light_slide(prs, "Spotlight: SDG 13 — Climate Action")
    # Left: color block with SDG number
    sdg13_color = SDG_COLORS[13]
    block = slide9.shapes.add_shape(MSO_SHAPE.RECTANGLE, MARGIN_L, Inches(1.8), Inches(0.15), Inches(3.5))
    block.fill.solid(); block.fill.fore_color.rgb = sdg13_color; block.line.fill.background()
    add_textbox(slide9, MARGIN_L + Inches(0.4), Inches(1.8), Inches(4.0), Inches(0.5),
                "SDG 13: Climate Action", font_name=FONT_TITLE, font_size=Pt(24), color=C_TEXT, bold=True)
    facts = [
        "Global average temperature has risen approximately 1.1°C above pre-industrial levels",
        "Climate-related disasters have increased by over 80% in the last decade",
        "To limit warming to 1.5°C, global emissions must decline by 45% by 2030",
        "Every fraction of a degree matters — the difference between 1.5°C and 2°C means 10 million more people at risk from sea-level rise"
    ]
    _, tf9 = add_textbox(slide9, MARGIN_L + Inches(0.4), Inches(2.5), Inches(7.0), Inches(0.5),
                         "Key Facts:", font_name=FONT_BODY, font_size=SIZE_BODY, color=C_TEXT, bold=True)
    for fact in facts:
        add_paragraph(tf9, f"•  {fact}", font_size=SIZE_BODY, color=C_TEXT)

    # Slide 10: Spotlight — SDG 4 Quality Education
    slide10 = build_light_slide(prs, "Spotlight: SDG 4 — Quality Education")
    sdg4_color = SDG_COLORS[4]
    block4 = slide10.shapes.add_shape(MSO_SHAPE.RECTANGLE, MARGIN_L, Inches(1.8), Inches(0.15), Inches(3.5))
    block4.fill.solid(); block4.fill.fore_color.rgb = sdg4_color; block4.line.fill.background()
    add_textbox(slide10, MARGIN_L + Inches(0.4), Inches(1.8), Inches(4.0), Inches(0.5),
                "SDG 4: Quality Education", font_name=FONT_TITLE, font_size=Pt(24), color=C_TEXT, bold=True)
    edu_facts = [
        "Before COVID-19, 258 million children and youth were out of school globally",
        "Only 58% of students worldwide achieve minimum proficiency in reading and mathematics",
        "Quality education is the foundation for improving people’s lives and sustainable development",
        "Education empowers individuals to escape poverty, fosters tolerance, and drives economic growth"
    ]
    _, tf10 = add_textbox(slide10, MARGIN_L + Inches(0.4), Inches(2.5), Inches(7.0), Inches(0.5),
                          "Key Facts:", font_name=FONT_BODY, font_size=SIZE_BODY, color=C_TEXT, bold=True)
    for fact in edu_facts:
        add_paragraph(tf10, f"•  {fact}", font_size=SIZE_BODY, color=C_TEXT)
```

- [ ] **Step 2: Run and verify 10 slides**

```bash
python scripts/build-ppt.py
```

- [ ] **Step 3: Commit**

```bash
git add scripts/build-ppt.py
git commit -m "feat: build Section C — 17 goals overview, 5P groups, climate and education spotlights"
```

---

### Task 9: Build Section D — Team & Project (slides 11–14)

**Files:**
- Modify: `scripts/build-ppt.py` (append to main())

- [ ] **Step 1: Add Slides 11–14**

Insert after Slide 10 code in main():

```python
    # ── Section D: Team & Project ──
    # Slide 11: Meet the Team
    slide11 = build_light_slide(prs, "Meet the Team")
    team_card_w = Inches(2.45); team_card_h = Inches(3.8)
    team_gap = Inches(0.3)
    team_total_w = 4 * team_card_w + 3 * team_gap
    team_start_x = (SLIDE_W - team_total_w) // 2
    team_y = Inches(2.0)
    for i, m in enumerate(TEAM_DATA):
        x = team_start_x + i * (team_card_w + team_gap)
        card = add_rounded_rect(slide11, x, team_y, team_card_w, team_card_h)
        # Color top bar
        top_bar = slide11.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, team_y, team_card_w, Inches(0.08))
        top_bar.fill.solid(); top_bar.fill.fore_color.rgb = m["color"]; top_bar.line.fill.background()
        # Avatar circle
        avatar = slide11.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.8), team_y + Inches(0.4), Inches(0.85), Inches(0.85))
        avatar.fill.solid(); avatar.fill.fore_color.rgb = m["color"]; avatar.line.fill.background()
        tf_av = avatar.text_frame; p_av = tf_av.paragraphs[0]
        p_av.text = m["name"][0]; p_av.font.size = Pt(22); p_av.font.color.rgb = C_WHITE
        p_av.font.bold = True; p_av.alignment = PP_ALIGN.CENTER
        # Name
        add_textbox(slide11, x + Inches(0.2), team_y + Inches(1.5), team_card_w - Inches(0.4), Inches(0.4),
                    m["name"], font_name=FONT_TITLE, font_size=Pt(16), color=C_TEXT, bold=True, alignment=PP_ALIGN.CENTER)
        # Role
        add_textbox(slide11, x + Inches(0.2), team_y + Inches(1.95), team_card_w - Inches(0.4), Inches(0.3),
                    m["role"], font_name=FONT_BODY, font_size=SIZE_LABEL, color=C_PRIMARY, bold=True, alignment=PP_ALIGN.CENTER)
        # Background
        add_textbox(slide11, x + Inches(0.2), team_y + Inches(2.35), team_card_w - Inches(0.4), Inches(0.3),
                    m["bg"], font_name=FONT_BODY, font_size=SIZE_CAPTION, color=C_TEXT_SEC, alignment=PP_ALIGN.CENTER)
        # Student ID
        add_textbox(slide11, x + Inches(0.2), team_y + Inches(2.65), team_card_w - Inches(0.4), Inches(0.3),
                    f"ID: {m['id']}", font_name="Consolas", font_size=Pt(9), color=C_TEXT_SEC, alignment=PP_ALIGN.CENTER)

    # Slide 12: Team SDG Assignments
    slide12 = build_light_slide(prs, "Team SDG Assignments")
    # Table
    rows = 5; cols = 4
    tbl_shape = slide12.shapes.add_table(rows, cols, MARGIN_L, Inches(2.0), CONTENT_W, Inches(3.6))
    tbl = tbl_shape.table
    headers = ["Member", "SDG Focus", "Rationale", "Background"]
    tbl_widths = [Inches(2.0), Inches(3.0), Inches(4.5), Inches(1.93)]
    for ci, h in enumerate(headers):
        tbl.columns[ci].width = tbl_widths[ci]
        cell = tbl.cell(0, ci)
        cell.text = h
        for p in cell.text_frame.paragraphs:
            p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = C_WHITE
            p.font.name = FONT_BODY
        cell.fill.solid(); cell.fill.fore_color.rgb = C_DARK_BG
    for ri, m in enumerate(TEAM_SDG_MAP):
        for ci, key in enumerate(["name", "sdgs", "rationale", "name"]):
            cell = tbl.cell(ri + 1, ci)
            if ci == 3:
                # find background from TEAM_DATA
                bg = next(t["bg"] for t in TEAM_DATA if t["name"] == m["name"])
                cell.text = bg
            else:
                cell.text = m[["name", "sdgs", "rationale"][ci]]
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(11); p.font.name = FONT_BODY
                p.font.color.rgb = C_TEXT
            if ri % 2 == 0:
                cell.fill.solid(); cell.fill.fore_color.rgb = RGBColor(0xF9, 0xF7, 0xF4)

    # Slide 13: Project Mission & Vision
    slide13 = build_light_slide(prs, "Project Mission & Vision")
    # Two-column mission/vision
    col13_w = Inches(5.1)
    # Mission
    add_gold_left_accent_card(slide13, MARGIN_L, Inches(1.8), col13_w, Inches(2.2),
        title="Mission",
        body="Promote awareness and action around the UN SDGs through education, "
             "digital tools, and community engagement. We aim to make sustainable "
             "development knowledge accessible to all.")
    # Vision
    add_gold_left_accent_card(slide13, MARGIN_L + col13_w + Inches(0.3), Inches(1.8), col13_w, Inches(2.2),
        title="Vision",
        body="A future where every individual understands their role in sustainable "
             "development and takes meaningful action toward a just, peaceful, and "
             "environmentally responsible world.")
    # 4 objective cards below
    obj_w = Inches(2.45); obj_h = Inches(1.5)
    obj_gap = Inches(0.25)
    obj_total_w = 4 * obj_w + 3 * obj_gap
    obj_start_x = (SLIDE_W - obj_total_w) // 2
    obj_y = Inches(4.4)
    for i, obj in enumerate(OBJECTIVES_DATA):
        x = obj_start_x + i * (obj_w + obj_gap)
        card = add_rounded_rect(slide13, x, obj_y, obj_w, obj_h)
        add_textbox(slide13, x + Inches(0.15), obj_y + Inches(0.15), obj_w - Inches(0.3), Inches(0.3),
                    f"0{i+1}", font_name=FONT_TITLE, font_size=SIZE_LABEL, color=C_PRIMARY, bold=True)
        add_textbox(slide13, x + Inches(0.15), obj_y + Inches(0.35), obj_w - Inches(0.3), Inches(0.35),
                    obj["title"], font_name=FONT_TITLE, font_size=Pt(14), color=C_TEXT, bold=True)
        add_textbox(slide13, x + Inches(0.15), obj_y + Inches(0.75), obj_w - Inches(0.3), Inches(0.65),
                    obj["desc"], font_name=FONT_BODY, font_size=SIZE_CAPTION, color=C_TEXT_SEC)

    # Slide 14: Website Showcase
    slide14 = build_light_slide(prs, "Website Showcase")
    pages = [
        ("Homepage", "Hero, stats, 17-goal grid"),
        ("SDGs Explorer", "Detailed goal information"),
        ("Carbon Calculator", "Interactive footprint tool"),
        ("Act Now", "Individual action guide"),
    ]
    showcase_w = Inches(2.45); showcase_h = Inches(2.5)
    showcase_gap = Inches(0.25)
    showcase_total_w = 4 * showcase_w + 3 * showcase_gap
    showcase_start_x = (SLIDE_W - showcase_total_w) // 2
    for i, (page_name, page_desc) in enumerate(pages):
        x = showcase_start_x + i * (showcase_w + showcase_gap)
        y = Inches(2.0)
        # Placeholder rectangle for screenshot
        placeholder = add_rounded_rect(slide14, x, y, showcase_w, Inches(1.6),
                                        fill_color=RGBColor(0xF0, 0xEB, 0xE4))
        add_textbox(slide14, x + Inches(0.2), y + Inches(0.5), showcase_w - Inches(0.4), Inches(0.6),
                    f"[{page_name}\nScreenshot]", font_name=FONT_BODY, font_size=SIZE_CAPTION,
                    color=C_TEXT_SEC, alignment=PP_ALIGN.CENTER)
        # Label
        add_textbox(slide14, x, y + Inches(1.75), showcase_w, Inches(0.35),
                    page_name, font_name=FONT_TITLE, font_size=Pt(14), color=C_TEXT, bold=True, alignment=PP_ALIGN.CENTER)
        add_textbox(slide14, x, y + Inches(2.1), showcase_w, Inches(0.3),
                    page_desc, font_name=FONT_BODY, font_size=SIZE_CAPTION, color=C_TEXT_SEC, alignment=PP_ALIGN.CENTER)
    # Tech stack callout
    add_textbox(slide14, MARGIN_L, Inches(5.2), CONTENT_W, Inches(0.4),
                "Built with: Vue 3 + TypeScript + GSAP Animations + Vite",
                font_name=FONT_BODY, font_size=SIZE_CAPTION, color=C_PRIMARY,
                bold=True, alignment=PP_ALIGN.CENTER)
```

- [ ] **Step 2: Run and verify 14 slides**

```bash
python scripts/build-ppt.py
```

- [ ] **Step 3: Commit**

```bash
git add scripts/build-ppt.py
git commit -m "feat: build Section D — team, SDG assignments, mission, website showcase"
```

---

### Task 10: Build Section E — Interactive Features (slides 15–17)

**Files:**
- Modify: `scripts/build-ppt.py` (append to main())

- [ ] **Step 1: Add Slides 15–17**

Insert after Slide 14 code in main():

```python
    # ── Section E: Interactive Features ──
    # Slide 15: Carbon Footprint Calculator
    slide15 = build_light_slide(prs, "Carbon Footprint Calculator")
    # 4 category cards
    cat_w = Inches(2.5); cat_h = Inches(2.6); cat_gap = Inches(0.2)
    cat_total_w = 4 * cat_w + 3 * cat_gap
    cat_start_x = (SLIDE_W - cat_total_w) // 2
    for i, cat in enumerate(CARBON_CATEGORIES):
        x = cat_start_x + i * (cat_w + cat_gap)
        y = Inches(1.8)
        card = add_rounded_rect(slide15, x, y, cat_w, cat_h)
        add_textbox(slide15, x + Inches(0.2), y + Inches(0.15), cat_w - Inches(0.4), Inches(0.35),
                    cat["name"], font_name=FONT_TITLE, font_size=Pt(16), color=C_PRIMARY, bold=True)
        _, tf_cat = add_textbox(slide15, x + Inches(0.2), y + Inches(0.55), cat_w - Inches(0.4), Inches(0.3),
                                "", font_size=SIZE_CAPTION, color=C_TEXT_SEC)
        for factor in cat["factors"]:
            add_paragraph(tf_cat, f"•  {factor}", font_size=SIZE_CAPTION, color=C_TEXT_SEC)
    # Rating levels below
    _, tf_ratings = add_textbox(slide15, MARGIN_L, Inches(4.7), CONTENT_W, Inches(0.4),
                                "Rating Levels:  ", font_name=FONT_BODY, font_size=SIZE_BODY, color=C_TEXT, bold=True)
    for lv in CARBON_LEVELS:
        add_paragraph(tf_ratings, f"{lv['level']}: {lv['range']}", font_size=SIZE_CAPTION, color=lv["color"], bold=True)

    # Slide 16: Act Now — Action Guide
    slide16 = build_light_slide(prs, "Act Now — Individual Action Guide")
    action_col_w = Inches(5.1)
    for i, cat in enumerate(ACTION_ITEMS):
        col = i % 2; row = i // 2
        x = MARGIN_L + col * (action_col_w + Inches(0.3))
        y = Inches(1.8) + row * Inches(2.3)
        add_gold_left_accent_card(slide16, x, y, action_col_w, Inches(1.9),
            title=cat["category"],
            body="\n".join([f"✓  {a}" for a in cat["actions"]]))

    # Slide 17: Technology & Architecture
    slide17 = build_light_slide(prs, "Technology & Architecture")
    # Architecture diagram — simple boxes
    arch_boxes = [
        ("Browser", "Vue 3 SPA"),
        ("Vue Router", "6 Routes"),
        ("Views", "Home · About · SDGs\nTeam · Carbon · Act"),
        ("Features", "GSAP Animations\nScoped CSS\nTypeScript"),
    ]
    box_w = Inches(2.2); box_h = Inches(1.4); box_gap = Inches(0.5)
    arch_total_w = 4 * box_w + 3 * box_gap
    arch_start_x = (SLIDE_W - arch_total_w) // 2
    arch_y = Inches(2.0)
    for i, (label, content) in enumerate(arch_boxes):
        x = arch_start_x + i * (box_w + box_gap)
        box = add_rounded_rect(slide17, x, arch_y, box_w, box_h, fill_color=C_PRIMARY if i == 0 else C_SURFACE)
        add_textbox(slide17, x + Inches(0.15), arch_y + Inches(0.1), box_w - Inches(0.3), Inches(0.3),
                    label, font_name=FONT_BODY, font_size=SIZE_LABEL, bold=True,
                    color=C_WHITE if i == 0 else C_PRIMARY)
        add_textbox(slide17, x + Inches(0.15), arch_y + Inches(0.45), box_w - Inches(0.3), Inches(0.85),
                    content, font_name=FONT_BODY, font_size=SIZE_CAPTION,
                    color=C_WHITE if i == 0 else C_TEXT)
        # Arrow between boxes (except last)
        if i < 3:
            add_textbox(slide17, x + box_w, arch_y + Inches(0.45), box_gap, Inches(0.3),
                        "→", font_size=Pt(20), color=C_PRIMARY, alignment=PP_ALIGN.CENTER)
    # Tech stack table below
    tbl17_shape = slide17.shapes.add_table(len(TECH_STACK) + 1, 2, MARGIN_L, Inches(3.9), Inches(6.0), Inches(2.5))
    tbl17 = tbl17_shape.table
    tbl17.columns[0].width = Inches(2.5); tbl17.columns[1].width = Inches(3.5)
    for ci, h in enumerate(["Layer", "Technology"]):
        cell = tbl17.cell(0, ci); cell.text = h
        for p in cell.text_frame.paragraphs:
            p.font.size = Pt(12); p.font.bold = True; p.font.color.rgb = C_WHITE; p.font.name = FONT_BODY
        cell.fill.solid(); cell.fill.fore_color.rgb = C_DARK_BG
    for ri, row in enumerate(TECH_STACK):
        for ci, key in enumerate(["layer", "tech"]):
            cell = tbl17.cell(ri + 1, ci); cell.text = row[key]
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(11); p.font.name = FONT_BODY; p.font.color.rgb = C_TEXT
            if ri % 2 == 0:
                cell.fill.solid(); cell.fill.fore_color.rgb = RGBColor(0xF9, 0xF7, 0xF4)
```

- [ ] **Step 2: Run and verify 17 slides**

```bash
python scripts/build-ppt.py
```

- [ ] **Step 3: Commit**

```bash
git add scripts/build-ppt.py
git commit -m "feat: build Section E — carbon calculator, act now, tech architecture"
```

---

### Task 11: Build Section F — Closing (slides 18–20)

**Files:**
- Modify: `scripts/build-ppt.py` (append to main())

- [ ] **Step 1: Add Slides 18–20**

Insert after Slide 17 code in main():

```python
    # ── Section F: Closing ──
    # Slide 18: Key Takeaways
    slide18 = build_light_slide(prs, "Key Takeaways")
    takeaways = [
        "The SDGs are an interconnected framework — progress on one goal accelerates others",
        "Everyone has a role to play — governments, businesses, communities, and individuals",
        "Technology and education are powerful tools for SDG awareness and action",
        "Local actions drive global change — start with your own carbon footprint",
        "2030 is only 4 years away — urgent, coordinated action is essential",
    ]
    for i, t in enumerate(takeaways):
        y_pos = Inches(1.8) + i * Inches(1.0)
        # Number circle
        circ = slide18.shapes.add_shape(MSO_SHAPE.OVAL, MARGIN_L, y_pos, Inches(0.55), Inches(0.55))
        circ.fill.solid(); circ.fill.fore_color.rgb = C_PRIMARY; circ.line.fill.background()
        tf_c = circ.text_frame; p_c = tf_c.paragraphs[0]
        p_c.text = str(i + 1); p_c.font.size = Pt(16); p_c.font.color.rgb = C_WHITE
        p_c.font.bold = True; p_c.alignment = PP_ALIGN.CENTER
        # Text
        add_textbox(slide18, MARGIN_L + Inches(0.8), y_pos + Inches(0.05), Inches(9.0), Inches(0.8),
                    t, font_name=FONT_BODY, font_size=SIZE_BODY, color=C_TEXT)

    # Slide 19: Call to Action
    slide19 = build_dark_slide(prs, "Act for Our Common Future")
    add_textbox(slide19, Inches(2.0), Inches(3.8), Inches(9.3), Inches(0.6),
                "Start by calculating your carbon footprint. Every action counts.",
                font_name=FONT_BODY, font_size=SIZE_BODY, color=C_TEXT_SEC, alignment=PP_ALIGN.CENTER)
    add_textbox(slide19, Inches(2.0), Inches(4.5), Inches(9.3), Inches(0.6),
                "Visit our website to explore the 17 goals and take action today.",
                font_name=FONT_BODY, font_size=SIZE_CAPTION, color=C_PRIMARY, alignment=PP_ALIGN.CENTER)

    # Slide 20: Thank You & References
    slide20 = build_light_slide(prs, "Thank You")
    add_textbox(slide20, Inches(3.0), Inches(1.8), Inches(7.3), Inches(1.0),
                "Thank You for Your Attention",
                font_name=FONT_TITLE, font_size=Pt(32), color=C_TEXT, bold=True, alignment=PP_ALIGN.CENTER)
    # References
    _, tf_ref = add_textbox(slide20, Inches(2.0), Inches(3.0), Inches(9.3), Inches(0.5),
                            "References:", font_name=FONT_BODY, font_size=SIZE_BODY, color=C_TEXT, bold=True)
    refs = [
        "United Nations. (2015). Transforming Our World: The 2030 Agenda for Sustainable Development. UN General Assembly.",
        "IPCC. (2023). Climate Change 2023: Synthesis Report. Intergovernmental Panel on Climate Change.",
        "UN Statistics Division. SDG Indicators Global Database. https://unstats.un.org/sdgs",
        "UN SDG Official Website. https://sdgs.un.org",
    ]
    for ref in refs:
        add_paragraph(tf_ref, f"•  {ref}", font_size=SIZE_CAPTION, color=C_TEXT_SEC)
    # Team contact
    add_textbox(slide20, Inches(2.0), Inches(5.5), Inches(9.3), Inches(0.4),
                "Team: Li Shuhang · Feng Jingyi · Wang Luyang · Lu Jianning",
                font_name=FONT_BODY, font_size=SIZE_CAPTION, color=C_PRIMARY, alignment=PP_ALIGN.CENTER)
    add_textbox(slide20, Inches(2.0), Inches(5.9), Inches(9.3), Inches(0.4),
                "Questions & Discussion Welcome",
                font_name=FONT_BODY, font_size=SIZE_BODY, color=C_TEXT_SEC, alignment=PP_ALIGN.CENTER)
```

- [ ] **Step 2: Run and verify 20 slides**

```bash
python scripts/build-ppt.py
```

- [ ] **Step 3: Commit**

```bash
git add scripts/build-ppt.py
git commit -m "feat: build Section F — key takeaways, call to action, thank you"
```

---

### Task 12: Build Section G — Appendix (slides 21–22) + final polish

**Files:**
- Modify: `scripts/build-ppt.py` (append to main())

- [ ] **Step 1: Add Slides 21–22**

Insert after Slide 20 code in main():

```python
    # ── Section G: Appendix ──
    # Slide 21: Full 17 Goals Reference Table
    slide21 = build_light_slide(prs, "Appendix: Full 17 Goals Reference")
    tbl21_shape = slide21.shapes.add_table(18, 3, MARGIN_L, Inches(1.8), Inches(8.5), Inches(5.3))
    tbl21 = tbl21_shape.table
    tbl21.columns[0].width = Inches(0.8); tbl21.columns[1].width = Inches(3.5)
    tbl21.columns[2].width = Inches(4.2)
    for ci, h in enumerate(["#", "Chinese Name", "English Name"]):
        cell = tbl21.cell(0, ci); cell.text = h
        for p in cell.text_frame.paragraphs:
            p.font.size = Pt(11); p.font.bold = True; p.font.color.rgb = C_WHITE; p.font.name = FONT_BODY
        cell.fill.solid(); cell.fill.fore_color.rgb = C_DARK_BG
    for ri, sdg in enumerate(SDG_DATA):
        for ci, key in enumerate(["id", "cn", "en"]):
            cell = tbl21.cell(ri + 1, ci)
            cell.text = str(sdg[key])
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(10); p.font.name = FONT_BODY; p.font.color.rgb = C_TEXT
            if ri % 2 == 0:
                cell.fill.solid(); cell.fill.fore_color.rgb = RGBColor(0xF9, 0xF7, 0xF4)

    # Slide 22: Carbon Calculator Reference
    slide22 = build_light_slide(prs, "Appendix: Carbon Calculator Methodology")
    add_textbox(slide22, MARGIN_L, Inches(1.8), CONTENT_W, Inches(0.5),
                "Emission Factors & Calculation Logic",
                font_name=FONT_TITLE, font_size=SIZE_HEADING, color=C_TEXT, bold=True)
    formulas = [
        "Car: carDistance (km) × 0.2 kg CO₂/km",
        "Public Transport: publicTransport (km) × 0.05 kg CO₂/km",
        "Flights: flights × 250 kg CO₂/flight",
        "Electricity: electricity (kWh) × 0.5 kg CO₂/kWh",
        "Gas: gas (m³) × 2.3 kg CO₂/m³",
        "Heating: heating (units) × 1.8 kg CO₂/unit",
        "Meat: (21 - meatDays) × 0.05 kg CO₂ (reduction credit)",
        "Local Food: localFood × 0.1 kg CO₂ (benefit)",
        "Recycling: +100 kg CO₂ if NOT recycling",
        "Composting: +50 kg CO₂ if NOT composting",
    ]
    _, tf_formulas = add_textbox(slide22, MARGIN_L, Inches(2.5), Inches(5.0), Inches(0.5),
                                 "Calculation Formula:",
                                 font_name=FONT_BODY, font_size=SIZE_BODY, color=C_TEXT, bold=True)
    for f in formulas:
        add_paragraph(tf_formulas, f"•  {f}", font_size=SIZE_CAPTION, color=C_TEXT, font_name="Consolas")
    # Rating thresholds
    add_textbox(slide22, Inches(7.0), Inches(2.5), Inches(5.0), Inches(0.5),
                "Rating Thresholds:", font_name=FONT_BODY, font_size=SIZE_BODY, color=C_TEXT, bold=True)
    _, tf_r = add_textbox(slide22, Inches(7.0), Inches(3.1), Inches(5.0), Inches(0.5),
                          "", font_size=SIZE_CAPTION, color=C_TEXT)
    for lv in CARBON_LEVELS:
        add_paragraph(tf_r, f"{lv['level']}: {lv['range']}", font_size=SIZE_BODY, color=lv["color"], bold=True)
    add_paragraph(tf_r, "", font_size=Pt(4))
    add_paragraph(tf_r, "Source: IPCC emission factors and\npeer-reviewed methodologies",
                  font_size=SIZE_CAPTION, color=C_TEXT_SEC)
```

- [ ] **Step 2: Run final build — verify all 22 slides**

```bash
python scripts/build-ppt.py
```
Expected: `Saved: output/UN-SDGs-Presentation.pptx`

- [ ] **Step 3: Commit**

```bash
git add scripts/build-ppt.py
git commit -m "feat: build Section G — appendix slides, finalize 22-slide deck"
```

---

### Task 13: Verification — Open and validate the PPT

**Files:**
- Verify: `output/UN-SDGs-Presentation.pptx`

- [ ] **Step 1: Check slide count programmatically**

```bash
python -c "
from pptx import Presentation
prs = Presentation('output/UN-SDGs-Presentation.pptx')
print(f'Total slides: {len(prs.slides)}')
for i, slide in enumerate(prs.slides):
    shapes = len(slide.shapes)
    print(f'  Slide {i+1}: {shapes} shapes')
"
```
Expected: 22 slides, with meaningful shape counts per slide.

- [ ] **Step 2: Verify file size is reasonable**

```bash
ls -lh output/UN-SDGs-Presentation.pptx
```
Expected: ~50-150 KB (text-only, no embedded images).

- [ ] **Step 3: Manual verification**

Open `output/UN-SDGs-Presentation.pptx` in PowerPoint or WPS. Verify:
- All 22 slides render correctly
- Colors match the Clean Academic design
- Text is readable and properly aligned
- Fonts (Georgia, Segoe UI) render correctly
- No placeholder text or obvious errors

- [ ] **Step 4: Final commit with any fixes**

```bash
git add scripts/build-ppt.py
git commit -m "chore: final polish and verification of PPT builder"
```
```

## Summary

| Task | Slides | Description |
|------|--------|-------------|
| 1 | — | Install python-pptx, scaffold |
| 2 | — | Config constants (colors, fonts, layout) |
| 3 | — | Helper functions (bg, text, shapes, cards) |
| 4 | — | Data (SDGs, team, stats, carbon, actions) |
| 5 | — | Slide builder functions (title, light/dark, card) |
| 6 | 1–2 | Section A: Title + Agenda |
| 7 | 3–5 | Section B: What, Stats, Why |
| 8 | 6–10 | Section C: 17 Goals, Groups, Spotlights |
| 9 | 11–14 | Section D: Team, Assignments, Mission, Showcase |
| 10 | 15–17 | Section E: Carbon, Actions, Tech |
| 11 | 18–20 | Section F: Takeaways, CTA, Thanks |
| 12 | 21–22 | Section G: Appendix slides |
| 13 | ALL | Verification + polish |

**Total: 13 tasks, 22 slides, ~1 script file**

## Post-Implementation

After all tasks complete:
1. Open `output/UN-SDGs-Presentation.pptx` in PowerPoint/WPS
2. Add screenshots to Slide 14 (Website Showcase) if desired — replace placeholder rectangles
3. Adjust any text that needs localization or customization
4. The `.pptx` is standard format — present directly or export to PDF
