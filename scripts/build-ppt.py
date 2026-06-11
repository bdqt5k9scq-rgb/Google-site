"""
UN SDGs Academic Presentation Builder v2
Generates a richly detailed 22-slide .pptx presentation.
All English, Clean Academic style, enhanced content density.
Output: output/UN-SDGs-Presentation.pptx
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn
import os

# ── Color Palette ──────────────────────────────────────────────
C_PRIMARY      = RGBColor(0xC4, 0x8B, 0x5C)  # Antique Gold
C_BG           = RGBColor(0xFD, 0xFA, 0xF6)  # Warm Cream
C_SURFACE      = RGBColor(0xFF, 0xFF, 0xFF)  # White
C_TEXT         = RGBColor(0x1C, 0x1C, 0x24)  # Dark Charcoal
C_TEXT_SEC     = RGBColor(0x6B, 0x65, 0x60)  # Warm Gray
C_BORDER       = RGBColor(0xF0, 0xEB, 0xE4)  # Light border
C_DARK_BG      = RGBColor(0x0D, 0x0D, 0x18)  # Deep Navy
C_WHITE        = RGBColor(0xFF, 0xFF, 0xFF)
C_TINT         = RGBColor(0xF9, 0xF7, 0xF4)  # Subtle warm tint

# SDG official colors
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
SIZE_SMALL   = Pt(12)
SIZE_CAPTION = Pt(11)
SIZE_LABEL   = Pt(10)
SIZE_STAT    = Pt(36)

# ── Layout ──────────────────────────────────────────────────────
SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)
MARGIN_L = Inches(1.2)
MARGIN_R = Inches(1.2)
CONTENT_W = Inches(13.333 - 1.2 - 1.2)  # ~10.93"

# ── Helpers ────────────────────────────────────────────────────

def set_slide_bg(slide, color):
    bg = slide.background; fill = bg.fill; fill.solid()
    fill.fore_color.rgb = color

def add_textbox(slide, left, top, width, height, text="",
                font_name=FONT_BODY, font_size=SIZE_BODY,
                color=C_TEXT, bold=False, alignment=PP_ALIGN.LEFT,
                line_spacing=1.15, anchor=MSO_ANCHOR.TOP,
                margins=None, auto_size=None):
    """Add a text box with precise layout control. Returns (shape, text_frame)."""
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    tf.auto_size = auto_size

    # Set internal margins
    if margins:
        tf.margin_left = margins[0]
        tf.margin_right = margins[1]
        tf.margin_top = margins[2]
        tf.margin_bottom = margins[3]

    p = tf.paragraphs[0]
    p.text = text
    p.font.name = font_name
    p.font.size = font_size
    p.font.color.rgb = color
    p.font.bold = bold
    p.alignment = alignment
    p.space_after = Pt(4)
    p.line_spacing = Pt(font_size.pt * line_spacing)

    # Vertical anchor
    txBox.text_frame._txBody.bodyPr.set('anchor', {
        MSO_ANCHOR.TOP: 't',
        MSO_ANCHOR.MIDDLE: 'ctr',
        MSO_ANCHOR.BOTTOM: 'b',
    }.get(anchor, 't'))

    return txBox, tf

def add_paragraph(tf, text, font_name=FONT_BODY, font_size=SIZE_BODY,
                  color=C_TEXT, bold=False, alignment=PP_ALIGN.LEFT,
                  space_after=Pt(6), line_spacing=None):
    """Add a new paragraph to an existing text frame."""
    p = tf.add_paragraph()
    p.text = text
    p.font.name = font_name
    p.font.size = font_size
    p.font.color.rgb = color
    p.font.bold = bold
    p.alignment = alignment
    p.space_after = space_after
    if line_spacing:
        p.line_spacing = line_spacing
    else:
        p.line_spacing = Pt(font_size.pt * 1.15)
    return p

def add_rounded_rect(slide, left, top, width, height, fill_color=C_SURFACE,
                     border_color=C_BORDER, border_width=Pt(1)):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid(); shape.fill.fore_color.rgb = fill_color
    shape.line.color.rgb = border_color; shape.line.width = border_width
    return shape

def add_accent_bar(slide, left, top, width, height=Inches(0.05), color=C_PRIMARY):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    shape.fill.solid(); shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    return shape

def add_page_number(slide, num):
    """Add subtle page number at bottom-right."""
    add_textbox(slide, Inches(11.8), Inches(7.05), Inches(1.2), Inches(0.35),
                str(num), font_name=FONT_BODY, font_size=Pt(9),
                color=C_BORDER, alignment=PP_ALIGN.RIGHT)

def add_subtitle_line(slide, text, top=Inches(1.05)):
    """Add a subtitle under the main title."""
    add_textbox(slide, MARGIN_L, top, CONTENT_W, Inches(0.45),
                text, font_name=FONT_BODY, font_size=SIZE_CAPTION,
                color=C_TEXT_SEC)

def add_bottom_line(slide):
    """Subtle bottom separator."""
    add_accent_bar(slide, MARGIN_L, Inches(6.85), CONTENT_W, Inches(0.01), C_BORDER)

def set_cell_margins(cell, left=Pt(4), right=Pt(4), top=Pt(3), bottom=Pt(3)):
    """Set internal margins/padding on a table cell for better text breathing room."""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcPr.set('marL', str(int(left)))
    tcPr.set('marR', str(int(right)))
    tcPr.set('marT', str(int(top)))
    tcPr.set('marB', str(int(bottom)))

def set_cell_vertical_anchor(cell, anchor=MSO_ANCHOR.MIDDLE):
    """Set vertical text alignment in a table cell."""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    anchor_map = {MSO_ANCHOR.TOP: 't', MSO_ANCHOR.MIDDLE: 'ctr', MSO_ANCHOR.BOTTOM: 'b'}
    tcPr.set('anchor', anchor_map.get(anchor, 'ctr'))

def style_table_cells(table, header_rows=1):
    """Apply consistent cell padding and vertical centering to all table cells."""
    for ri in range(len(table.rows)):
        for ci in range(len(table.columns)):
            cell = table.cell(ri, ci)
            pad = Pt(8) if ri < header_rows else Pt(5)
            set_cell_margins(cell, Pt(8), Pt(6), pad, pad)
            set_cell_vertical_anchor(cell, MSO_ANCHOR.MIDDLE if ri >= header_rows else MSO_ANCHOR.MIDDLE)

# ── Data (all English) ─────────────────────────────────────────

SDG_DATA = [
    {"id": 1,  "en": "No Poverty",            "short": "End poverty in all its forms everywhere"},
    {"id": 2,  "en": "Zero Hunger",           "short": "End hunger, achieve food security and promote sustainable agriculture"},
    {"id": 3,  "en": "Good Health & Well-being","short": "Ensure healthy lives and promote well-being for all at all ages"},
    {"id": 4,  "en": "Quality Education",     "short": "Ensure inclusive and equitable quality education for all"},
    {"id": 5,  "en": "Gender Equality",       "short": "Achieve gender equality and empower all women and girls"},
    {"id": 6,  "en": "Clean Water & Sanitation","short": "Ensure availability of water and sanitation for all"},
    {"id": 7,  "en": "Clean Energy",          "short": "Ensure access to affordable, reliable, sustainable energy for all"},
    {"id": 8,  "en": "Decent Work & Economic Growth","short": "Promote sustained, inclusive economic growth and decent work"},
    {"id": 9,  "en": "Industry, Innovation & Infrastructure","short": "Build resilient infrastructure and foster innovation"},
    {"id": 10, "en": "Reduced Inequalities",  "short": "Reduce inequality within and among countries"},
    {"id": 11, "en": "Sustainable Cities & Communities","short": "Make cities inclusive, safe, resilient and sustainable"},
    {"id": 12, "en": "Responsible Consumption & Production","short": "Ensure sustainable consumption and production patterns"},
    {"id": 13, "en": "Climate Action",        "short": "Take urgent action to combat climate change and its impacts"},
    {"id": 14, "en": "Life Below Water",      "short": "Conserve and sustainably use the oceans, seas and marine resources"},
    {"id": 15, "en": "Life on Land",          "short": "Protect, restore and promote sustainable use of terrestrial ecosystems"},
    {"id": 16, "en": "Peace, Justice & Strong Institutions","short": "Promote peaceful and inclusive societies for sustainable development"},
    {"id": 17, "en": "Partnerships for the Goals","short": "Strengthen the means of implementation and revitalize global partnerships"},
]

SDG_GROUPS = {
    "People":       {"goals": [1, 2, 3, 4, 5],   "desc": "End poverty and hunger in all forms, and ensure dignity and equality for every human being"},
    "Planet":       {"goals": [6, 12, 13, 14, 15], "desc": "Protect Earth's natural resources and climate to sustain future generations"},
    "Prosperity":   {"goals": [7, 8, 9, 10, 11], "desc": "Ensure all human beings can enjoy prosperous and fulfilling lives in harmony with nature"},
    "Peace":        {"goals": [16],               "desc": "Foster peaceful, just, and inclusive societies free from fear and violence"},
    "Partnership":  {"goals": [17],               "desc": "Mobilize the means required to implement this agenda through global solidarity"},
}

STATS_DATA = [
    {"number": "17",  "label": "Global Goals",     "sub": "Interconnected objectives"},
    {"number": "193", "label": "Member States",    "sub": "Unanimously adopted in 2015"},
    {"number": "2030","label": "Target Year",      "sub": "Only 4 years remaining"},
    {"number": "169", "label": "Specific Targets", "sub": "Measured by 232 indicators"},
]

WHY_DATA = [
    {
        "title": "Unprecedented Global Challenges",
        "text": "Global temperatures have risen ~1.1°C since pre-industrial times. Over 700 million people live in extreme poverty. Biodiversity is declining faster than at any time in human history. These interconnected crises transcend borders — no single nation can solve them alone."
    },
    {
        "title": "A Unified Action Framework",
        "text": "The 2030 Agenda provides a shared blueprint for peace and prosperity. It recognizes that ending poverty must go hand-in-hand with strategies that improve health and education, reduce inequality, and spur economic growth — all while tackling climate change."
    },
    {
        "title": "Leave No One Behind",
        "text": "With 169 targets and 232 indicators across 17 goals, the SDGs provide measurable benchmarks for progress. The pledge to 'Leave No One Behind' ensures development reaches the most vulnerable — women, children, persons with disabilities, and marginalized communities."
    },
]

TEAM_DATA = [
    {"name": "Li Shuhang",   "role": "Project Lead",     "bg": "Environmental Science", "id": "8168667", "color": RGBColor(0x2C, 0x5F, 0x2D), "bio": "Coordinates project strategy and leads research on environmental sustainability and ecological conservation."},
    {"name": "Feng Jingyi",  "role": "Tech Development", "bg": "Computer Science",      "id": "8168308", "color": RGBColor(0x1A, 0x3A, 0x5C), "bio": "Architects the Vue 3 web platform and develops interactive tools for carbon footprint calculation."},
    {"name": "Wang Luyang",  "role": "Policy Research",  "bg": "International Affairs", "id": "8168505", "color": RGBColor(0x5C, 0x2D, 0x6E), "bio": "Analyzes SDG policy frameworks and maps goal interconnections across international development agendas."},
    {"name": "Lu Jianning",  "role": "Data Analyst",     "bg": "Statistics",            "id": "8168379", "color": RGBColor(0xB8, 0x57, 0x3E), "bio": "Performs data-driven SDG progress analysis and validates the carbon calculator emission models."},
]

TEAM_SDG_MAP = [
    {"name": "Li Shuhang",   "sdgs": "SDG 6, 7, 13, 14, 15", "rationale": "Environmental science expertise aligns directly with planet-focused goals covering water, energy, climate, and ecosystems"},
    {"name": "Feng Jingyi",  "sdgs": "SDG 8, 9, 11, 12",     "rationale": "Computer science background drives technology-enabled solutions for sustainable industry, smart cities, and responsible consumption"},
    {"name": "Wang Luyang",  "sdgs": "SDG 1, 2, 5, 10, 16",  "rationale": "International affairs knowledge underpins equity, justice, and human dignity goals across poverty, hunger, and gender equality"},
    {"name": "Lu Jianning",  "sdgs": "SDG 3, 4, 17",         "rationale": "Statistical analysis skills enable rigorous data-driven approaches to health, education outcomes, and partnership metrics"},
]

AGENDA_ITEMS = [
    ("01", "Introduction to the SDGs",      "Origins, structure, and global significance of the 2030 Agenda"),
    ("02", "The 17 Sustainable Development Goals", "A comprehensive overview of all 17 interconnected goals"),
    ("03", "Why the World Needs SDGs",      "The urgent case for coordinated global action"),
    ("04", "Our Team & Project Mission",    "Who we are and what we aim to achieve"),
    ("05", "Interactive Features & Technology", "Carbon calculator, action guides, and technical architecture"),
    ("06", "Key Takeaways & Call to Action","What we've learned and how you can make a difference"),
]

OBJECTIVES_DATA = [
    {"title": "Public Awareness", "desc": "Increase public understanding of the 17 SDGs and their relevance to everyday life through accessible digital content"},
    {"title": "Educational Resources", "desc": "Provide interactive tools and learning materials that empower individuals and organizations to take action"},
    {"title": "Cross-Disciplinary Collaboration", "desc": "Bridge environmental science, computer science, international affairs, and statistics for holistic solutions"},
    {"title": "Local Action", "desc": "Translate global goals into local practice — helping communities identify and implement sustainable development initiatives"},
]

CARBON_CATEGORIES = [
    {"name": "Transportation", "icon": "🚗", "factors": [
        "Private car: 0.2 kg CO₂ per km driven",
        "Public transport: 0.05 kg CO₂ per km",
        "Air travel: 250 kg CO₂ per flight",
        "Short-haul flights have highest per-km impact"
    ]},
    {"name": "Energy", "icon": "⚡", "factors": [
        "Electricity: 0.5 kg CO₂ per kWh consumed",
        "Natural gas: 2.3 kg CO₂ per m³",
        "Heating: 1.8 kg CO₂ per unit",
        "Renewable energy switch can cut this by 80%+"
    ]},
    {"name": "Food", "icon": "🍽", "factors": [
        "Meat-heavy diet: higher footprint",
        "Plant-based days earn reduction credits",
        "Local food: 0.1 kg CO₂ benefit per item",
        "Food systems account for ~26% of global emissions"
    ]},
    {"name": "Waste", "icon": "♻", "factors": [
        "No recycling: +100 kg CO₂ penalty",
        "No composting: +50 kg CO₂ penalty",
        "Landfill methane is 25× more potent than CO₂",
        "Circular economy principles reduce total footprint"
    ]},
]

CARBON_LEVELS = [
    {"level": "Excellent", "range": "Below 3,000 kg CO₂/year", "msg": "Your footprint is well below average — keep it up!",
     "color": RGBColor(0x5C, 0x8D, 0x6D)},
    {"level": "Good",      "range": "3,000 – 6,000 kg CO₂/year", "msg": "Moderate footprint with clear room for improvement",
     "color": RGBColor(0x2C, 0x52, 0x82)},
    {"level": "Average",   "range": "6,000 – 10,000 kg CO₂/year", "msg": "Above sustainable levels — consider targeted reductions",
     "color": C_PRIMARY},
    {"level": "High",      "range": "Above 10,000 kg CO₂/year","msg": "Urgent action needed to reduce environmental impact",
     "color": RGBColor(0xB8, 0x57, 0x3E)},
]

ACTION_ITEMS = [
    {"category": "Transportation", "icon": "🚲", "actions": [
        "Switch to public transit, cycling, or walking for daily commutes",
        "Reduce air travel — one fewer long-haul flight saves ~1.6 tonnes CO₂",
        "Carpool or use electric vehicles where available"
    ]},
    {"category": "Energy at Home", "icon": "💡", "actions": [
        "Switch to LED bulbs and energy-efficient appliances (Energy Star rated)",
        "Unplug devices when not in use — standby power wastes 5-10% of home energy",
        "Consider switching to a renewable energy provider or installing solar panels"
    ]},
    {"category": "Food Choices", "icon": "🥗", "actions": [
        "Adopt Meatless Mondays — reducing meat by 50% cuts food footprint by ~40%",
        "Choose seasonal, locally sourced produce to reduce transport emissions",
        "Minimize food waste — if food waste were a country, it would be the 3rd largest emitter"
    ]},
    {"category": "Waste & Circularity", "icon": "♻", "actions": [
        "Implement full waste sorting: recyclables, compost, and landfill",
        "Compost kitchen scraps — reduces methane and creates valuable soil",
        "Choose reusable products over single-use plastics"
    ]},
]

TECH_STACK = [
    {"layer": "Frontend Framework", "tech": "Vue 3 with Composition API", "why": "Reactive, component-based architecture for maintainable UI"},
    {"layer": "Type System",        "tech": "TypeScript — Strict Mode",   "why": "Compile-time error detection and self-documenting code"},
    {"layer": "Routing",            "tech": "Vue Router 4 — History Mode","why": "Clean URLs and seamless SPA page transitions"},
    {"layer": "Animations",         "tech": "GSAP with ScrollTrigger",    "why": "High-performance scroll-linked animations and micro-interactions"},
    {"layer": "Build Tooling",      "tech": "Vite 6 with HMR",            "why": "Sub-second dev server startup and optimized production builds"},
    {"layer": "Styling",            "tech": "Scoped CSS + Design Tokens",  "why": "Component-isolated styles with consistent design system"},
]

# ── Slide Builder Functions ────────────────────────────────────

def build_light_slide(prs, title_text, subtitle_text=""):
    """Light slide with title, optional subtitle, bottom line, and page number."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, C_BG)
    add_accent_bar(slide, MARGIN_L, Inches(0.85), Inches(0.6), Inches(0.04))
    add_textbox(slide, MARGIN_L, Inches(0.5), CONTENT_W, Inches(0.6),
                title_text, font_name=FONT_TITLE, font_size=SIZE_TITLE, color=C_TEXT, bold=True)
    if subtitle_text:
        add_subtitle_line(slide, subtitle_text, top=Inches(0.95))
    add_bottom_line(slide)
    return slide

def build_light_slide_no_accent(prs, title_text, subtitle_text=""):
    """Light slide without accent bar (continuation)."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, C_BG)
    add_textbox(slide, MARGIN_L, Inches(0.5), CONTENT_W, Inches(0.6),
                title_text, font_name=FONT_TITLE, font_size=SIZE_TITLE, color=C_TEXT, bold=True)
    if subtitle_text:
        add_subtitle_line(slide, subtitle_text, top=Inches(0.95))
    add_bottom_line(slide)
    return slide

def build_dark_slide(prs, title_text, subtitle_text=""):
    """Dark slide with centered title."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, C_DARK_BG)
    add_accent_bar(slide, Inches(5.5), Inches(3.2), Inches(2.3), Inches(0.04), C_PRIMARY)
    add_textbox(slide, Inches(1.0), Inches(2.3), Inches(11.3), Inches(1.0),
                title_text, font_name=FONT_TITLE, font_size=Pt(32), color=C_WHITE, bold=True, alignment=PP_ALIGN.CENTER)
    if subtitle_text:
        add_textbox(slide, Inches(1.5), Inches(3.4), Inches(10.3), Inches(0.6),
                    subtitle_text, font_name=FONT_BODY, font_size=SIZE_BODY, color=C_TEXT_SEC, alignment=PP_ALIGN.CENTER)
    return slide

def add_gold_left_accent_card(slide, left, top, width, height, title="", body=""):
    """Card with gold left border accent and optimized text layout."""
    add_rounded_rect(slide, left, top, width, height)
    accent = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, Inches(0.06), height)
    accent.fill.solid(); accent.fill.fore_color.rgb = C_PRIMARY; accent.line.fill.background()
    inner_x = left + Inches(0.35); inner_w = width - Inches(0.55)
    add_textbox(slide, inner_x, top + Inches(0.2), inner_w, Inches(0.45),
                title, font_name=FONT_TITLE, font_size=Pt(17), color=C_TEXT, bold=True,
                line_spacing=1.1, anchor=MSO_ANCHOR.MIDDLE)
    add_textbox(slide, inner_x, top + Inches(0.7), inner_w, height - Inches(0.9),
                body, font_name=FONT_BODY, font_size=SIZE_SMALL, color=C_TEXT_SEC,
                line_spacing=1.25)
    return None

# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════

def main():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    page = 0

    # ═══ SECTION A: OPENING ═══
    # ── Slide 1: Title ──
    page += 1
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, C_DARK_BG)
    # Decorative elements
    add_accent_bar(slide, Inches(1.0), Inches(0.0), Inches(0.0), Inches(7.5), RGBColor(0x1A, 0x1A, 0x2E))
    add_accent_bar(slide, Inches(5.0), Inches(2.7), Inches(3.3), Inches(0.04), C_PRIMARY)
    # UN emblem hint
    add_textbox(slide, Inches(1.5), Inches(1.0), Inches(10.3), Inches(0.4),
                "UNITED NATIONS · 2030 AGENDA", font_name=FONT_BODY, font_size=SIZE_LABEL,
                color=C_PRIMARY, bold=True, alignment=PP_ALIGN.CENTER)
    add_textbox(slide, Inches(1.5), Inches(1.8), Inches(10.3), Inches(1.6),
                "The Sustainable\nDevelopment Goals",
                font_name=FONT_TITLE, font_size=Pt(42), color=C_WHITE, bold=True, alignment=PP_ALIGN.CENTER)
    add_textbox(slide, Inches(1.5), Inches(3.4), Inches(10.3), Inches(0.7),
                "A Comprehensive Overview of the 17 Global Goals\nand Our Project to Promote Awareness and Action",
                font_name=FONT_BODY, font_size=SIZE_BODY, color=RGBColor(0xAA, 0xAA, 0xBB), alignment=PP_ALIGN.CENTER)
    # Bottom info
    _, tf = add_textbox(slide, Inches(2.0), Inches(5.2), Inches(9.3), Inches(1.6),
                        "Li Shuhang  ·  Feng Jingyi  ·  Wang Luyang  ·  Lu Jianning",
                        font_name=FONT_BODY, font_size=SIZE_SMALL, color=RGBColor(0x88, 0x88, 0x99),
                        alignment=PP_ALIGN.CENTER)
    add_paragraph(tf, "Academic Course Presentation  ·  June 2026", font_size=SIZE_CAPTION, color=C_TEXT_SEC, alignment=PP_ALIGN.CENTER)
    add_page_number(slide, page)

    # ── Slide 2: Agenda ──
    page += 1
    slide2 = build_light_slide(prs, "Presentation Outline", "Navigating our exploration of the Sustainable Development Goals")
    card_w = Inches(3.2); card_h = Inches(2.05); gap = Inches(0.25)
    start_x = MARGIN_L; start_y = Inches(1.65)
    for i, (num, item, desc) in enumerate(AGENDA_ITEMS):
        col = i % 3; row = i // 3
        x = start_x + col * (card_w + gap); y = start_y + row * (card_h + gap)
        add_gold_left_accent_card(slide2, x, y, card_w, card_h, title=f"{num}  {item}", body=desc)
    add_page_number(slide2, page)

    # ═══ SECTION B: BACKGROUND ═══
    # ── Slide 3: What Are the SDGs ──
    page += 1
    slide3 = build_light_slide(prs, "What Are the SDGs?", "Understanding the 2030 Agenda for Sustainable Development")
    _, tf3 = add_textbox(slide3, MARGIN_L, Inches(1.6), CONTENT_W, Inches(0.9),
        "The Sustainable Development Goals are 17 interconnected global objectives adopted unanimously "
        "by all 193 United Nations Member States in September 2015. They form the core of the 2030 Agenda "
        "for Sustainable Development — a shared blueprint for peace and prosperity for people and the planet. "
        "The goals balance the three dimensions of sustainable development: economic, social, and environmental.",
        font_size=SIZE_BODY, color=C_TEXT)
    # Timeline
    timeline = [
        ("2015", "SDGs Adopted", "193 countries sign\nUN General Assembly"),
        ("2023", "Midpoint Review", "Progress at 15%\nOff-track on most goals"),
        ("2030", "Target Deadline", "Goals to be achieved\nUrgent acceleration needed"),
    ]
    for i, (year, phase, desc) in enumerate(timeline):
        x = Inches(2.0) + i * Inches(3.5); y = Inches(3.8)
        circ = slide3.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.55), y, Inches(1.2), Inches(1.2))
        circ.fill.solid(); circ.fill.fore_color.rgb = C_PRIMARY; circ.line.fill.background()
        tf_c = circ.text_frame; tf_c.word_wrap = True
        p_c = tf_c.paragraphs[0]; p_c.text = year; p_c.font.size = Pt(18)
        p_c.font.color.rgb = C_WHITE; p_c.font.bold = True; p_c.alignment = PP_ALIGN.CENTER
        add_textbox(slide3, x, y + Inches(1.4), Inches(2.3), Inches(0.35),
                    phase, font_name=FONT_TITLE, font_size=SIZE_SMALL, color=C_TEXT, bold=True, alignment=PP_ALIGN.CENTER)
        add_textbox(slide3, x, y + Inches(1.75), Inches(2.3), Inches(0.6),
                    desc, font_size=SIZE_CAPTION, color=C_TEXT_SEC, alignment=PP_ALIGN.CENTER)
    add_page_number(slide3, page)

    # ── Slide 4: Key Statistics ──
    page += 1
    slide4 = build_light_slide(prs, "Key Statistics", "The scale and ambition of the 2030 Agenda in numbers")
    stat_w = Inches(2.35); stat_h = Inches(2.8); stat_gap = Inches(0.35)
    stat_total_w = 4 * stat_w + 3 * stat_gap; stat_start_x = (SLIDE_W - stat_total_w) // 2
    for i, stat in enumerate(STATS_DATA):
        x = stat_start_x + i * (stat_w + stat_gap); y = Inches(2.0)
        add_rounded_rect(slide4, x, y, stat_w, stat_h)
        add_textbox(slide4, x + Inches(0.2), y + Inches(0.3), stat_w - Inches(0.4), Inches(1.2),
                    stat["number"], font_name=FONT_TITLE, font_size=Pt(44), color=C_PRIMARY, bold=True, alignment=PP_ALIGN.CENTER)
        add_textbox(slide4, x + Inches(0.2), y + Inches(1.5), stat_w - Inches(0.4), Inches(0.4),
                    stat["label"], font_name=FONT_TITLE, font_size=SIZE_SMALL, color=C_TEXT, bold=True, alignment=PP_ALIGN.CENTER)
        add_textbox(slide4, x + Inches(0.2), y + Inches(1.95), stat_w - Inches(0.4), Inches(0.6),
                    stat["sub"], font_name=FONT_BODY, font_size=SIZE_CAPTION, color=C_TEXT_SEC, alignment=PP_ALIGN.CENTER)
    add_page_number(slide4, page)

    # ── Slide 5: Why SDGs ──
    page += 1
    slide5 = build_light_slide(prs, "Why the World Needs SDGs", "Three compelling reasons for coordinated global action")
    why_w = Inches(3.3); why_h = Inches(4.0); why_gap = Inches(0.35)
    why_total_w = 3 * why_w + 2 * why_gap; why_start_x = (SLIDE_W - why_total_w) // 2
    for i, why in enumerate(WHY_DATA):
        x = why_start_x + i * (why_w + why_gap); y = Inches(1.9)
        add_gold_left_accent_card(slide5, x, y, why_w, why_h, title=why["title"], body=why["text"])
    add_page_number(slide5, page)

    # ═══ SECTION C: THE 17 GOALS ═══
    # ── Slide 6: Goals Overview Grid ──
    page += 1
    slide6 = build_light_slide(prs, "The 17 Sustainable Development Goals",
                               "Each goal addresses a critical dimension of human and planetary well-being — click any goal on our website to explore in depth")
    grid_item_w = Inches(1.55); grid_item_h = Inches(1.2); grid_gap_x = Inches(0.15); grid_gap_y = Inches(0.12)
    grid_cols = 6; grid_start_x = MARGIN_L; grid_start_y = Inches(1.7)
    for i, sdg in enumerate(SDG_DATA):
        col = i % grid_cols; row = i // grid_cols
        x = grid_start_x + col * (grid_item_w + grid_gap_x); y = grid_start_y + row * (grid_item_h + grid_gap_y)
        color = SDG_COLORS[sdg["id"]]
        add_rounded_rect(slide6, x, y, grid_item_w, grid_item_h, fill_color=color, border_color=color)
        add_textbox(slide6, x + Inches(0.1), y + Inches(0.08), Inches(0.4), Inches(0.3),
                    f"{sdg['id']:02d}", font_name=FONT_TITLE, font_size=Pt(12), color=C_WHITE, bold=True)
        add_textbox(slide6, x + Inches(0.1), y + Inches(0.42), grid_item_w - Inches(0.2), Inches(0.55),
                    sdg["en"], font_name=FONT_BODY, font_size=Pt(8), color=C_WHITE)
    add_page_number(slide6, page)

    # ── Slides 7-8: 5P Framework ──
    groups_list = list(SDG_GROUPS.items())
    col_w5 = Inches(5.05); col_h5 = Inches(2.3)

    def build_5p_slide(prs_obj, title, subtitle, group_slice, start_page_num):
        slide_obj = build_light_slide(prs_obj, title, subtitle)
        for gi, (gname, gdata) in enumerate(group_slice):
            col_gi = gi % 2; row_gi = gi // 2
            x = MARGIN_L + col_gi * (col_w5 + Inches(0.35))
            y = Inches(1.7) + row_gi * (col_h5 + Inches(0.25))
            add_rounded_rect(slide_obj, x, y, col_w5, col_h5)
            add_textbox(slide_obj, x + Inches(0.3), y + Inches(0.18), col_w5 - Inches(0.6), Inches(0.35),
                        gname, font_name=FONT_TITLE, font_size=Pt(20), color=C_PRIMARY, bold=True)
            add_textbox(slide_obj, x + Inches(0.3), y + Inches(0.55), col_w5 - Inches(0.6), Inches(0.4),
                        gdata["desc"], font_name=FONT_BODY, font_size=SIZE_CAPTION, color=C_TEXT_SEC)
            chips = " · ".join([SDG_DATA[gid-1]["en"] for gid in gdata["goals"]])
            add_textbox(slide_obj, x + Inches(0.3), y + Inches(1.15), col_w5 - Inches(0.6), Inches(0.9),
                        chips, font_name=FONT_BODY, font_size=Pt(9), color=C_TEXT)
        add_page_number(slide_obj, start_page_num)
        return slide_obj

    page += 1
    build_5p_slide(prs, "Goals Grouped — The 5P Framework",
                   "The 17 goals are organized into five critical areas for people and the planet",
                   groups_list[:2], page)
    page += 1
    build_5p_slide(prs, "Goals Grouped — Prosperity, Peace & Partnership",
                   "Completing the 5P framework: building thriving, peaceful, and collaborative societies",
                   groups_list[2:], page)

    # ── Slide 9: Spotlight SDG 13 ──
    page += 1
    slide9 = build_light_slide(prs, "Spotlight: SDG 13 — Climate Action",
                                "Take urgent action to combat climate change and its impacts")
    sdg13_color = SDG_COLORS[13]
    add_accent_bar(slide9, MARGIN_L, Inches(1.6), Inches(0.15), Inches(4.0), sdg13_color)
    add_textbox(slide9, MARGIN_L + Inches(0.4), Inches(1.6), Inches(5.0), Inches(0.5),
                "Why Climate Action Matters", font_name=FONT_TITLE, font_size=Pt(22), color=C_TEXT, bold=True)
    facts_13 = [
        ("Rising Temperatures", "Global average temperature has risen ~1.1°C above pre-industrial levels. The past decade (2014–2024) was the warmest on record."),
        ("Extreme Weather", "Climate-related disasters have increased over 80% in the last decade, affecting millions and costing billions in damages globally."),
        ("Emissions Gap", "To limit warming to 1.5°C, global greenhouse gas emissions must peak before 2025 and decline 43% by 2030 from 2019 levels."),
        ("Sea Level Rise", "The difference between 1.5°C and 2°C of warming means 10 million more people at risk from coastal flooding and saltwater intrusion."),
        ("Ecosystem Impact", "Coral reefs could decline 70–90% at 1.5°C warming, and over 99% at 2°C — threatening marine biodiversity and coastal livelihoods."),
    ]
    _, tf9 = add_textbox(slide9, MARGIN_L + Inches(0.4), Inches(2.3), Inches(8.5), Inches(0.3),
                         "", font_size=SIZE_CAPTION, color=C_TEXT)
    for title, detail in facts_13:
        add_paragraph(tf9, title, font_name=FONT_BODY, font_size=SIZE_BODY, color=C_TEXT, bold=True)
        add_paragraph(tf9, detail, font_name=FONT_BODY, font_size=SIZE_SMALL, color=C_TEXT_SEC, space_after=Pt(10))
    add_page_number(slide9, page)

    # ── Slide 10: Spotlight SDG 4 ──
    page += 1
    slide10 = build_light_slide(prs, "Spotlight: SDG 4 — Quality Education",
                                 "Ensure inclusive and equitable quality education and promote lifelong learning for all")
    sdg4_color = SDG_COLORS[4]
    add_accent_bar(slide10, MARGIN_L, Inches(1.6), Inches(0.15), Inches(4.0), sdg4_color)
    add_textbox(slide10, MARGIN_L + Inches(0.4), Inches(1.6), Inches(5.0), Inches(0.5),
                "Why Quality Education Matters", font_name=FONT_TITLE, font_size=Pt(22), color=C_TEXT, bold=True)
    edu_facts = [
        ("Learning Crisis", "Before COVID-19, 258 million children and youth were out of school. Only 58% of students worldwide achieve minimum proficiency in reading and math."),
        ("Gender Disparity", "Girls in conflict-affected areas are 2.5× more likely to be out of school. Education reduces child marriage and improves health outcomes."),
        ("Economic Multiplier", "Each additional year of schooling raises individual earnings by ~10%. Education is the single most powerful driver of economic mobility."),
        ("Digital Divide", "Over 1.3 billion school-age children lack home internet access, creating a homework gap that widens inequality in the digital era."),
        ("Foundational Goal", "Quality education underpins every other SDG — from poverty reduction (SDG 1) to innovation (SDG 9) and climate awareness (SDG 13)."),
    ]
    _, tf10 = add_textbox(slide10, MARGIN_L + Inches(0.4), Inches(2.3), Inches(8.5), Inches(0.3),
                          "", font_size=SIZE_CAPTION, color=C_TEXT)
    for title, detail in edu_facts:
        add_paragraph(tf10, title, font_name=FONT_BODY, font_size=SIZE_BODY, color=C_TEXT, bold=True)
        add_paragraph(tf10, detail, font_name=FONT_BODY, font_size=SIZE_SMALL, color=C_TEXT_SEC, space_after=Pt(10))
    add_page_number(slide10, page)

    # ═══ SECTION D: TEAM & PROJECT ═══
    # ── Slide 11: Meet the Team ──
    page += 1
    slide11 = build_light_slide(prs, "Meet the Team",
                                 "Four members bringing diverse expertise to the SDG mission")
    tcard_w = Inches(2.45); tcard_h = Inches(4.2); tcard_gap = Inches(0.3)
    tcard_total_w = 4 * tcard_w + 3 * tcard_gap; tcard_start_x = (SLIDE_W - tcard_total_w) // 2
    tcard_y = Inches(1.65)
    for i, m in enumerate(TEAM_DATA):
        x = tcard_start_x + i * (tcard_w + tcard_gap)
        add_rounded_rect(slide11, x, tcard_y, tcard_w, tcard_h)
        # Color top bar
        top_bar = slide11.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, tcard_y, tcard_w, Inches(0.08))
        top_bar.fill.solid(); top_bar.fill.fore_color.rgb = m["color"]; top_bar.line.fill.background()
        # Avatar
        avatar = slide11.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.78), tcard_y + Inches(0.35), Inches(0.9), Inches(0.9))
        avatar.fill.solid(); avatar.fill.fore_color.rgb = m["color"]; avatar.line.fill.background()
        tf_av = avatar.text_frame; p_av = tf_av.paragraphs[0]
        p_av.text = m["name"][0]; p_av.font.size = Pt(24); p_av.font.color.rgb = C_WHITE
        p_av.font.bold = True; p_av.alignment = PP_ALIGN.CENTER
        # Info
        add_textbox(slide11, x + Inches(0.18), tcard_y + Inches(1.5), tcard_w - Inches(0.36), Inches(0.35),
                    m["name"], font_name=FONT_TITLE, font_size=Pt(15), color=C_TEXT, bold=True, alignment=PP_ALIGN.CENTER)
        add_textbox(slide11, x + Inches(0.18), tcard_y + Inches(1.88), tcard_w - Inches(0.36), Inches(0.25),
                    m["role"], font_name=FONT_BODY, font_size=SIZE_LABEL, color=C_PRIMARY, bold=True, alignment=PP_ALIGN.CENTER)
        add_textbox(slide11, x + Inches(0.18), tcard_y + Inches(2.2), tcard_w - Inches(0.36), Inches(0.25),
                    m["bg"], font_name=FONT_BODY, font_size=SIZE_CAPTION, color=C_TEXT_SEC, alignment=PP_ALIGN.CENTER)
        add_textbox(slide11, x + Inches(0.18), tcard_y + Inches(2.5), tcard_w - Inches(0.36), Inches(0.2),
                    f"ID: {m['id']}", font_name="Consolas", font_size=Pt(8), color=C_BORDER, alignment=PP_ALIGN.CENTER)
        add_textbox(slide11, x + Inches(0.18), tcard_y + Inches(2.85), tcard_w - Inches(0.36), Inches(1.1),
                    m["bio"], font_name=FONT_BODY, font_size=Pt(9), color=C_TEXT_SEC, alignment=PP_ALIGN.CENTER)
    add_page_number(slide11, page)

    # ── Slide 12: Team SDG Assignments ──
    page += 1
    slide12 = build_light_slide(prs, "Team SDG Assignments",
                                 "Each member focuses on goals aligned with their academic expertise and career aspirations")
    rows, cols = 5, 4
    tbl_shape = slide12.shapes.add_table(rows, cols, MARGIN_L, Inches(1.8), CONTENT_W, Inches(3.8))
    tbl = tbl_shape.table
    headers = ["Team Member", "Assigned SDGs", "Rationale for Assignment", "Academic Background"]
    widths = [Inches(1.8), Inches(2.5), Inches(4.5), Inches(2.13)]
    for ci, h in enumerate(headers):
        tbl.columns[ci].width = widths[ci]
        cell = tbl.cell(0, ci); cell.text = h
        for p in cell.text_frame.paragraphs:
            p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = C_WHITE; p.font.name = FONT_BODY
        cell.fill.solid(); cell.fill.fore_color.rgb = C_DARK_BG
    for ri, m in enumerate(TEAM_SDG_MAP):
        bg_match = next(t["bg"] for t in TEAM_DATA if t["name"] == m["name"])
        row_data = [m["name"], m["sdgs"], m["rationale"], bg_match]
        for ci, val in enumerate(row_data):
            cell = tbl.cell(ri + 1, ci); cell.text = val
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(11); p.font.name = FONT_BODY; p.font.color.rgb = C_TEXT
            if ri % 2 == 0:
                cell.fill.solid(); cell.fill.fore_color.rgb = C_TINT
    style_table_cells(tbl)
    add_page_number(slide12, page)

    # ── Slide 13: Mission & Vision ──
    page += 1
    slide13 = build_light_slide(prs, "Project Mission & Vision",
                                 "What drives our work and where we hope to make an impact")
    col13_w = Inches(5.05)
    add_gold_left_accent_card(slide13, MARGIN_L, Inches(1.65), col13_w, Inches(2.15),
        title="Our Mission",
        body="To promote awareness and understanding of the UN Sustainable Development Goals through "
             "accessible digital education, interactive tools, and community engagement. We believe "
             "knowledge is the first step toward meaningful action.")
    add_gold_left_accent_card(slide13, MARGIN_L + col13_w + Inches(0.35), Inches(1.65), col13_w, Inches(2.15),
        title="Our Vision",
        body="A world where every individual — regardless of background — understands their role in "
             "sustainable development and is empowered with the knowledge and tools to take meaningful "
             "action toward a just, peaceful, and environmentally sustainable future.")
    obj_w = Inches(2.45); obj_h = Inches(2.0); obj_gap = Inches(0.25)
    obj_total_w = 4 * obj_w + 3 * obj_gap; obj_start_x = (SLIDE_W - obj_total_w) // 2
    obj_y = Inches(4.2)
    for i, obj in enumerate(OBJECTIVES_DATA):
        x = obj_start_x + i * (obj_w + obj_gap)
        add_rounded_rect(slide13, x, obj_y, obj_w, obj_h)
        add_textbox(slide13, x + Inches(0.18), obj_y + Inches(0.15), obj_w - Inches(0.36), Inches(0.25),
                    f"0{i+1}", font_name=FONT_TITLE, font_size=SIZE_LABEL, color=C_PRIMARY, bold=True)
        add_textbox(slide13, x + Inches(0.18), obj_y + Inches(0.38), obj_w - Inches(0.36), Inches(0.35),
                    obj["title"], font_name=FONT_TITLE, font_size=SIZE_SMALL, color=C_TEXT, bold=True)
        add_textbox(slide13, x + Inches(0.18), obj_y + Inches(0.78), obj_w - Inches(0.36), Inches(1.05),
                    obj["desc"], font_name=FONT_BODY, font_size=SIZE_CAPTION, color=C_TEXT_SEC)
    add_page_number(slide13, page)

    # ── Slide 14: Website Showcase ──
    page += 1
    slide14 = build_light_slide(prs, "Website Showcase",
                                 "A Vue 3 single-page application bringing the SDGs to life through interactive design")
    pages_info = [
        ("Homepage", "Hero banner, key statistics,\n17-goal interactive grid,\nteam introduction"),
        ("SDGs Explorer", "Detailed goal-by-goal\ninformation pages with\nvisual data presentation"),
        ("Carbon Calculator", "Interactive footprint tool:\ntransport, energy, food,\nwaste — with tailored tips"),
        ("Act Now Guide", "Actionable individual steps\norganized by category:\ntransport, energy, food, waste"),
    ]
    showcase_w = Inches(2.45); showcase_gap = Inches(0.25)
    showcase_total_w = 4 * showcase_w + 3 * showcase_gap; showcase_start_x = (SLIDE_W - showcase_total_w) // 2
    showcase_y = Inches(1.7)
    for i, (pname, pdesc) in enumerate(pages_info):
        x = showcase_start_x + i * (showcase_w + showcase_gap)
        # Placeholder
        ph = add_rounded_rect(slide14, x, showcase_y, showcase_w, Inches(1.5), fill_color=RGBColor(0xEE, 0xEA, 0xE4))
        add_textbox(slide14, x + Inches(0.2), showcase_y + Inches(0.45), showcase_w - Inches(0.4), Inches(0.6),
                    f"[ {pname}\n  Screenshot ]", font_name=FONT_BODY, font_size=SIZE_CAPTION,
                    color=C_TEXT_SEC, alignment=PP_ALIGN.CENTER)
        add_textbox(slide14, x, showcase_y + Inches(1.65), showcase_w, Inches(0.3),
                    pname, font_name=FONT_TITLE, font_size=SIZE_SMALL, color=C_TEXT, bold=True, alignment=PP_ALIGN.CENTER)
        add_textbox(slide14, x, showcase_y + Inches(1.98), showcase_w, Inches(0.9),
                    pdesc, font_name=FONT_BODY, font_size=SIZE_CAPTION, color=C_TEXT_SEC, alignment=PP_ALIGN.CENTER)
    # Tech callout
    add_textbox(slide14, MARGIN_L, Inches(5.5), CONTENT_W, Inches(0.3),
                "Tech Stack: Vue 3 + TypeScript + Vue Router 4 + GSAP Animations + Vite 6",
                font_name=FONT_BODY, font_size=SIZE_CAPTION, color=C_PRIMARY, bold=True, alignment=PP_ALIGN.CENTER)
    add_page_number(slide14, page)

    # ═══ SECTION E: INTERACTIVE FEATURES ═══
    # ── Slide 15: Carbon Footprint Calculator ──
    page += 1
    slide15 = build_light_slide(prs, "Carbon Footprint Calculator",
                                 "An interactive tool estimating annual CO₂ emissions across four lifestyle categories")
    cat_w = Inches(2.5); cat_h = Inches(3.1); cat_gap = Inches(0.2)
    cat_total_w = 4 * cat_w + 3 * cat_gap; cat_start_x = (SLIDE_W - cat_total_w) // 2
    for i, cat in enumerate(CARBON_CATEGORIES):
        x = cat_start_x + i * (cat_w + cat_gap); y = Inches(1.65)
        add_rounded_rect(slide15, x, y, cat_w, cat_h)
        add_textbox(slide15, x + Inches(0.2), y + Inches(0.15), cat_w - Inches(0.4), Inches(0.3),
                    f"{cat['icon']}  {cat['name']}", font_name=FONT_TITLE, font_size=Pt(14), color=C_PRIMARY, bold=True)
        _, tf_cat = add_textbox(slide15, x + Inches(0.2), y + Inches(0.55), cat_w - Inches(0.4), Inches(0.3),
                                "", font_size=Pt(9), color=C_TEXT_SEC)
        for factor in cat["factors"]:
            add_paragraph(tf_cat, f"•  {factor}", font_size=Pt(9), color=C_TEXT_SEC, space_after=Pt(4))
    # Rating summary
    _, tf_ratings = add_textbox(slide15, MARGIN_L, Inches(5.05), CONTENT_W, Inches(0.3),
                                "Rating Thresholds:", font_name=FONT_BODY, font_size=SIZE_SMALL, color=C_TEXT, bold=True)
    for lv in CARBON_LEVELS:
        add_paragraph(tf_ratings, f"{lv['level']}: {lv['range']} — {lv['msg']}",
                      font_size=SIZE_CAPTION, color=lv["color"], bold=True)
    add_page_number(slide15, page)

    # ── Slide 16: Act Now ──
    page += 1
    slide16 = build_light_slide(prs, "Act Now — Individual Action Guide",
                                 "Practical steps every person can take starting today to reduce their environmental footprint")
    act_col_w = Inches(5.05); act_h = Inches(2.25)
    for i, cat in enumerate(ACTION_ITEMS):
        col = i % 2; row = i // 2
        x = MARGIN_L + col * (act_col_w + Inches(0.35))
        y = Inches(1.6) + row * (act_h + Inches(0.2))
        body_text = "\n".join([f"✓  {a}" for a in cat["actions"]])
        add_gold_left_accent_card(slide16, x, y, act_col_w, act_h,
            title=f"{cat['icon']}  {cat['category']}", body=body_text)
    add_page_number(slide16, page)

    # ── Slide 17: Technology & Architecture ──
    page += 1
    slide17 = build_light_slide(prs, "Technology & Architecture",
                                 "How our Vue 3 single-page application is built and organized")
    # Architecture flow
    arch_boxes = [
        ("Browser", "User Interface\nVue 3 SPA"),
        ("Router", "Vue Router 4\n6 Route Views"),
        ("View Layer", "Home · About\nSDGs · Team\nCarbon · Act Now"),
        ("Core Features", "GSAP Animations\nScoped CSS Modules\nTypeScript Types"),
    ]
    abox_w = Inches(2.2); abox_h = Inches(1.55); abox_gap = Inches(0.5)
    arch_total_w = 4 * abox_w + 3 * abox_gap; arch_start_x = (SLIDE_W - arch_total_w) // 2
    arch_y = Inches(1.65)
    for i, (label, content) in enumerate(arch_boxes):
        x = arch_start_x + i * (abox_w + abox_gap)
        is_first = (i == 0)
        add_rounded_rect(slide17, x, arch_y, abox_w, abox_h,
                         fill_color=C_PRIMARY if is_first else C_SURFACE,
                         border_color=C_PRIMARY if is_first else C_BORDER)
        add_textbox(slide17, x + Inches(0.15), arch_y + Inches(0.1), abox_w - Inches(0.3), Inches(0.3),
                    label, font_name=FONT_BODY, font_size=SIZE_LABEL, bold=True,
                    color=C_WHITE if is_first else C_PRIMARY)
        add_textbox(slide17, x + Inches(0.15), arch_y + Inches(0.45), abox_w - Inches(0.3), Inches(1.0),
                    content, font_name=FONT_BODY, font_size=SIZE_CAPTION, color=C_WHITE if is_first else C_TEXT)
        if i < 3:
            add_textbox(slide17, x + abox_w, arch_y + Inches(0.5), abox_gap, Inches(0.3),
                        "▸", font_size=Pt(22), color=C_PRIMARY, alignment=PP_ALIGN.CENTER)
    # Tech stack table
    tbl17_shape = slide17.shapes.add_table(len(TECH_STACK) + 1, 3, MARGIN_L, Inches(3.65), Inches(9.0), Inches(2.8))
    tbl17 = tbl17_shape.table
    tbl17.columns[0].width = Inches(2.2); tbl17.columns[1].width = Inches(3.3); tbl17.columns[2].width = Inches(3.5)
    for ci, h in enumerate(["Layer", "Technology", "Why We Chose It"]):
        cell = tbl17.cell(0, ci); cell.text = h
        for p in cell.text_frame.paragraphs:
            p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = C_WHITE; p.font.name = FONT_BODY
        cell.fill.solid(); cell.fill.fore_color.rgb = C_DARK_BG
    for ri, row in enumerate(TECH_STACK):
        for ci, key in enumerate(["layer", "tech", "why"]):
            cell = tbl17.cell(ri + 1, ci); cell.text = row[key]
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(10); p.font.name = FONT_BODY; p.font.color.rgb = C_TEXT
            if ri % 2 == 0:
                cell.fill.solid(); cell.fill.fore_color.rgb = C_TINT
    style_table_cells(tbl17)
    add_page_number(slide17, page)

    # ═══ SECTION F: CLOSING ═══
    # ── Slide 18: Key Takeaways ──
    page += 1
    slide18 = build_light_slide(prs, "Key Takeaways", "What we hope you remember from this presentation")
    takeaways = [
        ("Interconnected Framework",
         "Progress on one SDG accelerates progress on others. Poverty reduction (SDG 1) improves health (SDG 3) and education (SDG 4). Climate action (SDG 13) protects life below water (SDG 14) and on land (SDG 15)."),
        ("Everyone Has a Role",
         "Governments set policy, businesses drive innovation, civil society holds institutions accountable, and individuals make daily choices. The SDG framework creates space for all actors to contribute meaningfully."),
        ("Technology Amplifies Impact",
         "Digital tools — from our carbon calculator to global data dashboards — make SDG awareness accessible at scale. Technology converts abstract goals into personal, actionable insights."),
        ("Local Action, Global Change",
         "Every sustainable choice — how we travel, what we eat, how we consume — ripples outward. Individual action multiplied across billions of people is the engine of transformation the SDGs envision."),
        ("2030 Is Now",
         "With only 4 years remaining to the target deadline, urgent acceleration is essential. The midpoint review showed only 15% of targets are on track. This is not a distant future — it is our present responsibility."),
    ]
    for i, (title, detail) in enumerate(takeaways):
        y_pos = Inches(1.55) + i * Inches(1.05)
        circ = slide18.shapes.add_shape(MSO_SHAPE.OVAL, MARGIN_L, y_pos, Inches(0.55), Inches(0.55))
        circ.fill.solid(); circ.fill.fore_color.rgb = C_PRIMARY; circ.line.fill.background()
        tf_c = circ.text_frame; p_c = tf_c.paragraphs[0]
        p_c.text = str(i + 1); p_c.font.size = Pt(16); p_c.font.color.rgb = C_WHITE
        p_c.font.bold = True; p_c.alignment = PP_ALIGN.CENTER
        add_textbox(slide18, MARGIN_L + Inches(0.75), y_pos, Inches(1.5), Inches(0.5),
                    title, font_name=FONT_TITLE, font_size=SIZE_SMALL, color=C_TEXT, bold=True)
        add_textbox(slide18, MARGIN_L + Inches(2.3), y_pos + Inches(0.02), Inches(8.5), Inches(0.85),
                    detail, font_name=FONT_BODY, font_size=SIZE_CAPTION, color=C_TEXT_SEC)
    add_page_number(slide18, page)

    # ── Slide 19: Call to Action ──
    page += 1
    slide19 = build_dark_slide(prs, "Act for Our Common Future",
                                "\"The future is not something that happens to us — it is something we create.\"")
    add_textbox(slide19, Inches(2.0), Inches(4.3), Inches(9.3), Inches(0.5),
                "Start by visiting our website. Explore the 17 goals. Calculate your carbon footprint.",
                font_name=FONT_BODY, font_size=SIZE_BODY, color=RGBColor(0xAA, 0xAA, 0xBB), alignment=PP_ALIGN.CENTER)
    add_textbox(slide19, Inches(2.5), Inches(5.0), Inches(8.3), Inches(0.5),
                "Every action counts. Every voice matters. Every choice shapes our common future.",
                font_name=FONT_TITLE, font_size=SIZE_SMALL, color=C_PRIMARY, alignment=PP_ALIGN.CENTER)
    add_page_number(slide19, page)

    # ── Slide 20: Thank You & References ──
    page += 1
    slide20 = build_light_slide(prs, "Thank You", "We appreciate your attention and welcome your questions")
    add_textbox(slide20, Inches(2.0), Inches(1.6), Inches(9.3), Inches(0.8),
                "Thank You for Your Time and Attention",
                font_name=FONT_TITLE, font_size=Pt(30), color=C_TEXT, bold=True, alignment=PP_ALIGN.CENTER)
    # References column
    _, tf_ref = add_textbox(slide20, MARGIN_L, Inches(2.8), Inches(5.5), Inches(0.3),
                            "Key References", font_name=FONT_TITLE, font_size=SIZE_HEADING, color=C_TEXT, bold=True)
    refs = [
        "United Nations. (2015). Transforming Our World: The 2030 Agenda for Sustainable Development. A/RES/70/1.",
        "IPCC. (2023). Climate Change 2023: Synthesis Report. Contribution of Working Groups I, II and III.",
        "UN DESA. (2024). The Sustainable Development Goals Report 2024. United Nations Publications.",
        "UN Statistics Division. SDG Indicators Global Database. https://unstats.un.org/sdgs",
    ]
    for ref in refs:
        add_paragraph(tf_ref, f"•  {ref}", font_size=SIZE_CAPTION, color=C_TEXT_SEC)
    # Team column
    _, tf_team = add_textbox(slide20, Inches(7.5), Inches(2.8), Inches(4.5), Inches(0.3),
                             "Project Team", font_name=FONT_TITLE, font_size=SIZE_HEADING, color=C_TEXT, bold=True)
    for m in TEAM_DATA:
        add_paragraph(tf_team, f"{m['name']} — {m['role']}", font_size=SIZE_SMALL, color=C_TEXT)
        add_paragraph(tf_team, f"{m['bg']}  ·  {m['id']}", font_size=SIZE_CAPTION, color=C_TEXT_SEC)
    add_textbox(slide20, Inches(2.0), Inches(5.8), Inches(9.3), Inches(0.4),
                "Questions & Discussion Welcome  ·  Thank you for engaging with the SDGs",
                font_name=FONT_BODY, font_size=SIZE_CAPTION, color=C_PRIMARY, alignment=PP_ALIGN.CENTER)
    add_page_number(slide20, page)

    # ═══ SECTION G: APPENDIX ═══
    # ── Slide 21: Full Goals Reference ──
    page += 1
    slide21 = build_light_slide(prs, "Appendix A: Complete SDG Reference",
                                 "All 17 Sustainable Development Goals with official short descriptions")
    tbl21_shape = slide21.shapes.add_table(18, 3, Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.3))
    tbl21 = tbl21_shape.table
    tbl21.columns[0].width = Inches(0.7); tbl21.columns[1].width = Inches(4.5); tbl21.columns[2].width = Inches(6.5)
    for ci, h in enumerate(["#", "Goal", "Official Short Description"]):
        cell = tbl21.cell(0, ci); cell.text = h
        for p in cell.text_frame.paragraphs:
            p.font.size = Pt(12); p.font.bold = True; p.font.color.rgb = C_WHITE; p.font.name = FONT_BODY
        cell.fill.solid(); cell.fill.fore_color.rgb = C_DARK_BG
    for ri, sdg in enumerate(SDG_DATA):
        for ci, key in enumerate(["id", "en", "short"]):
            cell = tbl21.cell(ri + 1, ci); cell.text = str(sdg[key])
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(10); p.font.name = FONT_BODY; p.font.color.rgb = C_TEXT
            if ri % 2 == 0:
                cell.fill.solid(); cell.fill.fore_color.rgb = C_TINT
    style_table_cells(tbl21)
    add_page_number(slide21, page)

    # ── Slide 22: Carbon Calculator Methodology ──
    page += 1
    slide22 = build_light_slide(prs, "Appendix B: Carbon Calculator Methodology",
                                 "Emission factors, calculation logic, and rating thresholds used in our interactive tool")
    # Formulas
    add_textbox(slide22, MARGIN_L, Inches(1.55), Inches(5.5), Inches(0.35),
                "Calculation Formula", font_name=FONT_TITLE, font_size=SIZE_HEADING, color=C_TEXT, bold=True)
    formulas = [
        "Car: carDistance × 0.2 kg CO₂ / km",
        "Public Transport: publicTransport × 0.05 kg CO₂ / km",
        "Flights: flights × 250 kg CO₂ per flight",
        "Electricity: electricity × 0.5 kg CO₂ / kWh",
        "Natural Gas: gas × 2.3 kg CO₂ / m³",
        "Heating: heating × 1.8 kg CO₂ per unit",
        "Meat Offset: (21 − meatDays) × 0.05 kg CO₂ credit",
        "Local Food: localFood × 0.1 kg CO₂ benefit",
        "No Recycling Penalty: +100 kg CO₂",
        "No Composting Penalty: +50 kg CO₂",
    ]
    _, tf_f = add_textbox(slide22, MARGIN_L, Inches(2.0), Inches(5.5), Inches(0.3),
                          "", font_name="Consolas", font_size=SIZE_CAPTION, color=C_TEXT)
    for f in formulas:
        add_paragraph(tf_f, f"▹  {f}", font_name="Consolas", font_size=Pt(10), color=C_TEXT, space_after=Pt(3))
    # Ratings
    add_textbox(slide22, Inches(7.0), Inches(1.55), Inches(5.0), Inches(0.35),
                "Rating Thresholds & Interpretation", font_name=FONT_TITLE, font_size=SIZE_HEADING, color=C_TEXT, bold=True)
    _, tf_r = add_textbox(slide22, Inches(7.0), Inches(2.0), Inches(5.5), Inches(0.3),
                          "", font_size=SIZE_SMALL, color=C_TEXT)
    for lv in CARBON_LEVELS:
        add_paragraph(tf_r, f"{lv['level']} ({lv['range']})", font_size=SIZE_SMALL, color=lv["color"], bold=True)
        add_paragraph(tf_r, f"    {lv['msg']}", font_size=SIZE_CAPTION, color=C_TEXT_SEC, space_after=Pt(8))
    add_textbox(slide22, Inches(7.0), Inches(4.5), Inches(5.5), Inches(0.3),
                "Data Sources", font_name=FONT_TITLE, font_size=SIZE_HEADING, color=C_TEXT, bold=True)
    add_textbox(slide22, Inches(7.0), Inches(4.9), Inches(5.5), Inches(1.2),
                "IPCC Fifth & Sixth Assessment Reports\n"
                "EPA Greenhouse Gas Equivalencies Calculator\n"
                "World Bank CO₂ Emissions Data\n"
                "UNEP Emissions Gap Reports",
                font_name=FONT_BODY, font_size=SIZE_CAPTION, color=C_TEXT_SEC)
    # Global average context
    add_textbox(slide22, MARGIN_L, Inches(4.85), Inches(5.5), Inches(0.3),
                "Global Context", font_name=FONT_TITLE, font_size=SIZE_HEADING, color=C_TEXT, bold=True)
    add_textbox(slide22, MARGIN_L, Inches(5.25), Inches(5.5), Inches(1.4),
                "Global average: ~4,000 kg CO₂/person/year\n"
                "Sustainable target: < 2,000 kg CO₂/person/year\n"
                "China average: ~7,400 kg CO₂/person/year\n"
                "USA average: ~14,700 kg CO₂/person/year",
                font_name=FONT_BODY, font_size=SIZE_CAPTION, color=C_TEXT_SEC)
    add_page_number(slide22, page)

    # ── Save ──
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "UN-SDGs-Presentation.pptx")
    prs.save(output_path)
    print(f"Saved: {output_path}")
    print(f"Total slides: {len(prs.slides)}")
    print("v2 — Enhanced with richer content, all English, page numbers, subtitles")

if __name__ == "__main__":
    main()
