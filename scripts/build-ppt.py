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
from lxml import etree
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
SIZE_TITLE   = Pt(32)
SIZE_HEADING = Pt(26)
SIZE_BODY    = Pt(16)
SIZE_SMALL   = Pt(14)
SIZE_CAPTION = Pt(12)
SIZE_LABEL   = Pt(12)
SIZE_STAT    = Pt(42)

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
    """Add subtle page number at bottom-right and apply text entrance animations."""
    add_textbox(slide, Inches(11.8), Inches(7.05), Inches(1.2), Inches(0.35),
                str(num), font_name=FONT_BODY, font_size=Pt(11),
                color=C_BORDER, alignment=PP_ALIGN.RIGHT)
    # Apply staggered text animations (skip title slide and appendix)
    if num not in (1, 21, 22):
        add_text_animations(slide, delay_between_ms=100, duration_ms=350)

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

# ── Slide Transitions ──────────────────────────────────────────

def add_slide_transition(slide, trans_type="fade", speed="fast", duration_ms=300):
    """Add a smooth slide transition via XML manipulation."""
    NS = 'http://schemas.openxmlformats.org/presentationml/2006/main'
    NS14 = 'http://schemas.microsoft.com/office/powerpoint/2010/main'
    nsmap = {'p': NS, 'p14': NS14}

    cSld = slide._element
    for existing in cSld.findall('p:transition', nsmap):
        cSld.remove(existing)

    trans_el = etree.SubElement(cSld, f'{{{NS}}}transition')
    trans_el.set('spd', speed)
    # No advTm — slide advances on click only

    morph_types = ['morph']
    if trans_type in morph_types:
        etree.SubElement(trans_el, f'{{{NS14}}}{trans_type}')
    else:
        child = etree.SubElement(trans_el, f'{{{NS}}}{trans_type}')
        if trans_type in ('push', 'wipe', 'cover', 'uncover', 'reveal'):
            child.set('dir', 'l')

# ── Shape Animations ───────────────────────────────────────────

def add_text_animations(slide, delay_between_ms=120, duration_ms=400):
    """
    Add staggered fade-in entrance animations to all text shapes on a slide.
    Shapes animate one after another, creating a reveal sequence.
    Only animates shapes that contain text.
    """
    NS = 'http://schemas.openxmlformats.org/presentationml/2006/main'
    A = 'http://schemas.openxmlformats.org/drawingml/2006/main'

    # Collect text shapes with their shape IDs
    animated = []
    for shape in slide.shapes:
        if shape.has_text_frame and shape.text_frame.text.strip():
            shape_id = shape.shape_id
            if shape_id:
                animated.append(str(shape_id))

    if len(animated) < 2:
        return  # Not enough shapes to animate meaningfully

    # Remove existing timing
    cSld = slide._element
    nsmap_p = {'p': NS}
    for existing in cSld.findall('p:timing', nsmap_p):
        cSld.remove(existing)

    # Build the timing tree XML string
    # Structure: root → seq (main sequence) → parallel blocks (one per shape)
    # Each block: after previous, staggered by delay_between_ms

    shape_blocks = []
    for i, shape_id in enumerate(animated):
        delay = i * delay_between_ms
        node_id_base = 10 + i * 10

        block = f"""
        <p:par xmlns:p="{NS}">
          <p:cTn id="{node_id_base}" dur="{duration_ms}" fill="hold" grpId="0" nodeType="clickEffect">
            <p:stCondLst>
              <p:cond delay="{delay}"/>
            </p:stCondLst>
            <p:childTnLst>
              <p:animEffect transition="in" filter="fade">
                <p:cBhvr>
                  <p:cTn id="{node_id_base + 1}" dur="{duration_ms}" fill="hold"/>
                  <p:tgtEl>
                    <p:spTgt spid="{shape_id}"/>
                  </p:tgtEl>
                </p:cBhvr>
              </p:animEffect>
            </p:childTnLst>
          </p:cTn>
        </p:par>"""
        shape_blocks.append(block)

    # On the first shape, add a "with previous" trigger so it starts automatically
    # The rest already have delay offsets creating the stagger

    timing_xml = f"""<p:timing xmlns:p="{NS}" xmlns:a="{A}">
      <p:tnLst>
        <p:par>
          <p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot">
            <p:childTnLst>
              <p:seq concurrent="0" nextAc="seek">
                <p:cTn id="5" dur="indefinite" nodeType="mainSeq">
                  <p:childTnLst>
                    {''.join(shape_blocks)}
                  </p:childTnLst>
                </p:cTn>
              </p:seq>
            </p:childTnLst>
          </p:cTn>
        </p:par>
      </p:tnLst>
    </p:timing>"""

    timing_el = etree.fromstring(timing_xml)
    cSld.append(timing_el)

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
        "title": "The Problems Don't Stop at Borders",
        "text": "Temperatures are up about 1.1°C since the Industrial Revolution. Over 700 million people still live on less than $2.15 a day. Species are going extinct at rates not seen in millions of years. These aren't separate issues — they feed into each other, and no country can fix them by acting alone."
    },
    {
        "title": "A Framework That Connects the Dots",
        "text": "Before the SDGs, development goals tended to be siloed — health over here, environment over there. The 2030 Agenda explicitly links economic, social, and environmental dimensions. The idea is simple: you can't lift people out of poverty while destroying the ecosystems they depend on."
    },
    {
        "title": "Measurable, Not Just Nice Words",
        "text": "Unlike many international agreements, the SDGs come with teeth — 169 specific targets and 232 indicators that can be tracked. The 'Leave No One Behind' principle means looking past national averages to see who's being excluded: women, children, people with disabilities, and the extreme poor."
    },
]

TEAM_DATA = [
    {"name": "Li Shuhang",   "role": "Project Lead",     "bg": "Environmental Science", "id": "8168667", "color": RGBColor(0x2C, 0x5F, 0x2D), "photo": "public/images/team/li-shuhang.jpg", "bio": "Handles the big picture — keeps the project on track and digs into the environmental research behind the planet-related SDGs."},
    {"name": "Feng Jingyi",  "role": "Tech Development", "bg": "Computer Science",      "id": "8168308", "color": RGBColor(0x1A, 0x3A, 0x5C), "photo": "public/images/team/feng-jingyi.jpg", "bio": "Built the website from scratch using Vue and TypeScript. Wrote the carbon calculator logic and made sure everything actually works."},
    {"name": "Wang Luyang",  "role": "Policy Research",  "bg": "International Affairs", "id": "8168505", "color": RGBColor(0x5C, 0x2D, 0x6E), "photo": "public/images/team/wang-luyang.jpg", "bio": "Reads a lot of UN reports so we don't have to. Focused on how the SDGs fit into real international policy frameworks."},
    {"name": "Lu Jianning",  "role": "Data Analyst",     "bg": "Statistics",            "id": "8168379", "color": RGBColor(0xB8, 0x57, 0x3E), "photo": "public/images/team/lu-jianning.jpg", "bio": "Crunching numbers — validated our carbon calculator's emission factors and checked SDG progress data against official sources."},
]

TEAM_SDG_MAP = [
    {"name": "Li Shuhang",   "sdgs": "SDG 6, 7, 13, 14, 15", "rationale": "Environmental science expertise aligns directly with planet-focused goals covering water, energy, climate, and ecosystems"},
    {"name": "Feng Jingyi",  "sdgs": "SDG 8, 9, 11, 12",     "rationale": "Computer science background drives technology-enabled solutions for sustainable industry, smart cities, and responsible consumption"},
    {"name": "Wang Luyang",  "sdgs": "SDG 1, 2, 5, 10, 16",  "rationale": "International affairs knowledge underpins equity, justice, and human dignity goals across poverty, hunger, and gender equality"},
    {"name": "Lu Jianning",  "sdgs": "SDG 3, 4, 17",         "rationale": "Statistical analysis skills enable rigorous data-driven approaches to health, education outcomes, and partnership metrics"},
]

AGENDA_ITEMS = [
    ("01", "Introduction to the SDGs",      "Where they came from, what they cover, and how they're structured"),
    ("02", "The 17 Goals at a Glance",      "A walk through all 17 goals, how they group together, and two deep dives"),
    ("03", "Why the SDGs Exist",            "The problems they're trying to solve and how they approach them differently"),
    ("04", "Our Team & This Project",       "Four people, four backgrounds, one website about the SDGs"),
    ("05", "What We Built",                 "The carbon footprint calculator, action guides, and how the site works under the hood"),
    ("06", "What We Learned & What's Next", "Key takeaways from this project and how to get involved"),
]

OBJECTIVES_DATA = [
    {"title": "Make the SDGs Understandable", "desc": "Most people have heard of the SDGs but can't name more than two. We wanted to build something that makes all 17 easy to explore."},
    {"title": "Give People Tools, Not Just Information", "desc": "Reading about carbon footprints is one thing. Actually calculating yours and getting personalized tips is more useful."},
    {"title": "Work Across Disciplines", "desc": "You can't understand the SDGs from just one angle. Our team covers environmental science, CS, international affairs, and statistics."},
    {"title": "Make It Relevant to Daily Life", "desc": "Global goals feel abstract. We tried to connect each SDG to choices people actually make — what they eat, how they travel, what they buy."},
]

CARBON_CATEGORIES = [
    {"name": "Transportation", "icon": "", "factors": [
        "Private car: 0.2 kg CO₂ per km",
        "Public transport: 0.05 kg CO₂ per km",
        "Air travel: 250 kg CO₂ per flight",
        "Short-haul flights are worse per km than long-haul"
    ]},
    {"name": "Energy", "icon": "", "factors": [
        "Electricity: 0.5 kg CO₂ per kWh",
        "Natural gas: 2.3 kg CO₂ per m³",
        "Heating: 1.8 kg CO₂ per unit",
        "Switching to renewables cuts this category most"
    ]},
    {"name": "Food", "icon": "", "factors": [
        "Meat-heavy diet = higher footprint",
        "Eating more plant-based meals earns credits",
        "Locally sourced food: 0.1 kg CO₂ benefit",
        "Food production = ~26% of global emissions"
    ]},
    {"name": "Waste", "icon": "", "factors": [
        "Not recycling: +100 kg CO₂ penalty",
        "Not composting: +50 kg CO₂ penalty",
        "Methane from landfills is 25× worse than CO₂",
        "Better waste habits are the easiest win"
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
    {"category": "Transportation", "icon": "", "actions": [
        "Take the bus or subway instead of driving — even once a week adds up",
        "One fewer round-trip flight per year saves about 1.6 tonnes of CO₂",
        "If you need a car, carpool or look into electric options"
    ]},
    {"category": "Energy at Home", "icon": "", "actions": [
        "LED bulbs use 75% less energy and last years longer than incandescent",
        "Standby power from plugged-in devices can be 5-10% of your bill — unplug things",
        "If your area offers green power plans, they're often not much more expensive"
    ]},
    {"category": "Food Choices", "icon": "", "actions": [
        "Cutting meat consumption in half roughly cuts your food footprint by 40%",
        "Seasonal local produce doesn't need to be flown or trucked across continents",
        "A third of all food gets wasted — meal planning helps more than people think"
    ]},
    {"category": "Waste", "icon": "", "actions": [
        "Separate your trash: recyclables, kitchen scraps for compost, and actual landfill",
        "Composting turns food waste into soil instead of methane in a landfill",
        "Bring a reusable bag and water bottle — simple but effective over time"
    ]},
]

TECH_STACK = [
    {"layer": "Frontend Framework", "tech": "Vue 3 (Composition API)", "why": "Component-based, easy to refactor, good TypeScript support"},
    {"layer": "Type System",        "tech": "TypeScript (strict mode)", "why": "Catches mistakes before runtime, makes the code self-documenting"},
    {"layer": "Routing",            "tech": "Vue Router 4", "why": "Client-side routing with clean URLs, no page reloads"},
    {"layer": "Animations",         "tech": "GSAP + ScrollTrigger", "why": "Industry standard for scroll-linked animation, works reliably across browsers"},
    {"layer": "Build Tooling",      "tech": "Vite 6", "why": "Fast dev server, quick HMR, straightforward production builds"},
    {"layer": "Styling",            "tech": "Scoped CSS", "why": "Styles are tied to components so they don't leak or conflict"},
]

# ── Slide Builder Functions ────────────────────────────────────

def build_light_slide(prs, title_text, subtitle_text="", transition="fade"):
    """Light slide with title, optional subtitle, bottom line, and slide transition."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, C_BG)
    add_accent_bar(slide, MARGIN_L, Inches(0.85), Inches(0.6), Inches(0.04))
    add_textbox(slide, MARGIN_L, Inches(0.5), CONTENT_W, Inches(0.6),
                title_text, font_name=FONT_TITLE, font_size=SIZE_TITLE, color=C_TEXT, bold=True)
    if subtitle_text:
        add_subtitle_line(slide, subtitle_text, top=Inches(0.95))
    add_bottom_line(slide)
    add_slide_transition(slide, transition)
    return slide

def build_light_slide_no_accent(prs, title_text, subtitle_text="", transition="fade"):
    """Light slide without accent bar (continuation)."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, C_BG)
    add_textbox(slide, MARGIN_L, Inches(0.5), CONTENT_W, Inches(0.6),
                title_text, font_name=FONT_TITLE, font_size=SIZE_TITLE, color=C_TEXT, bold=True)
    if subtitle_text:
        add_subtitle_line(slide, subtitle_text, top=Inches(0.95))
    add_bottom_line(slide)
    add_slide_transition(slide, transition)
    return slide

def build_dark_slide(prs, title_text, subtitle_text="", transition="fade"):
    """Dark slide with centered title, subtitle, and slide transition."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, C_DARK_BG)
    add_accent_bar(slide, Inches(5.5), Inches(3.2), Inches(2.3), Inches(0.04), C_PRIMARY)
    add_textbox(slide, Inches(1.0), Inches(2.3), Inches(11.3), Inches(1.0),
                title_text, font_name=FONT_TITLE, font_size=Pt(32), color=C_WHITE, bold=True, alignment=PP_ALIGN.CENTER)
    if subtitle_text:
        add_textbox(slide, Inches(1.5), Inches(3.4), Inches(10.3), Inches(0.6),
                    subtitle_text, font_name=FONT_BODY, font_size=SIZE_BODY, color=C_TEXT_SEC, alignment=PP_ALIGN.CENTER)
    add_slide_transition(slide, transition)
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
                "A course project exploring all 17 goals, what they mean,\nand how technology can help people understand them better",
                font_name=FONT_BODY, font_size=SIZE_BODY, color=RGBColor(0xAA, 0xAA, 0xBB), alignment=PP_ALIGN.CENTER)
    # Bottom info
    _, tf = add_textbox(slide, Inches(2.0), Inches(5.2), Inches(9.3), Inches(1.6),
                        "Li Shuhang  ·  Feng Jingyi  ·  Wang Luyang  ·  Lu Jianning",
                        font_name=FONT_BODY, font_size=SIZE_SMALL, color=RGBColor(0x88, 0x88, 0x99),
                        alignment=PP_ALIGN.CENTER)
    add_paragraph(tf, "Academic Course Presentation  ·  June 2026", font_size=SIZE_CAPTION, color=C_TEXT_SEC, alignment=PP_ALIGN.CENTER)
    add_text_animations(slide, delay_between_ms=200, duration_ms=600)
    add_page_number(slide, page)

    # ── Slide 2: Agenda ──
    page += 1
    slide2 = build_light_slide(prs, "Presentation Outline", "What we'll cover in the next 20 minutes", transition="push")
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
    slide3 = build_light_slide(prs, "What Are the SDGs?", "A quick background on where they came from and what they're trying to do")
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
    slide4 = build_light_slide(prs, "Key Statistics", "The SDGs by the numbers")
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
    slide5 = build_light_slide(prs, "Why the SDGs Exist", "Three reasons the old approach wasn't working")
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
                               "From ending poverty to protecting the oceans — all 17 goals at a glance", transition="push")
    grid_item_w = Inches(1.55); grid_item_h = Inches(1.2); grid_gap_x = Inches(0.15); grid_gap_y = Inches(0.12)
    grid_cols = 6; grid_start_x = MARGIN_L; grid_start_y = Inches(1.7)
    for i, sdg in enumerate(SDG_DATA):
        col = i % grid_cols; row = i // grid_cols
        x = grid_start_x + col * (grid_item_w + grid_gap_x); y = grid_start_y + row * (grid_item_h + grid_gap_y)
        color = SDG_COLORS[sdg["id"]]
        add_rounded_rect(slide6, x, y, grid_item_w, grid_item_h, fill_color=color, border_color=color)
        add_textbox(slide6, x + Inches(0.1), y + Inches(0.08), Inches(0.4), Inches(0.3),
                    f"{sdg['id']:02d}", font_name=FONT_TITLE, font_size=Pt(14), color=C_WHITE, bold=True)
        add_textbox(slide6, x + Inches(0.1), y + Inches(0.42), grid_item_w - Inches(0.2), Inches(0.55),
                    sdg["en"], font_name=FONT_BODY, font_size=Pt(10), color=C_WHITE)
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
                        chips, font_name=FONT_BODY, font_size=Pt(11), color=C_TEXT)
        add_page_number(slide_obj, start_page_num)
        return slide_obj

    page += 1
    build_5p_slide(prs, "Goals Grouped — The 5P Framework",
                   "The 17 goals organized into five clusters — the UN calls this the 5P framework",
                   groups_list[:2], page)
    page += 1
    build_5p_slide(prs, "Goals Grouped — Prosperity, Peace & Partnership",
                   "The remaining groups: prosperity, peace, and the partnerships that make it all possible",
                   groups_list[2:], page)

    # ── Slide 9: Spotlight SDG 13 ──
    page += 1
    slide9 = build_light_slide(prs, "Spotlight: SDG 13 — Climate Action",
                                "The science is clear, the solutions exist — why this goal matters most")
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
                                 "Why education is the foundation for every other SDG")
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
                                 "Four students, four different majors, one project")
    # 4 portrait cards in a row — photos dominate, compact text below
    card_w = Inches(2.4)
    card_h = Inches(3.7)
    card_gap = Inches(0.35)
    total_w = 4 * card_w + 3 * card_gap
    start_x = (SLIDE_W - total_w) // 2
    start_y = Inches(1.65)

    for i, m in enumerate(TEAM_DATA):
        x = start_x + i * (card_w + card_gap)
        y = start_y

        # White card surface
        add_rounded_rect(slide11, x, y, card_w, card_h)

        # Photo — large, nearly full card width, portrait proportions
        photo_w = Inches(1.8); photo_h = Inches(2.15)
        px = x + (card_w - photo_w) / 2
        py = y + Inches(0.2)
        photo_path = m.get("photo", "")

        # Color accent border behind photo
        border_w = photo_w + Inches(0.08); border_h = photo_h + Inches(0.08)
        bx = x + (card_w - border_w) / 2
        border_rect = slide11.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            bx, py - Inches(0.04), border_w, border_h)
        border_rect.fill.solid(); border_rect.fill.fore_color.rgb = m["color"]
        border_rect.line.fill.background()

        if photo_path and os.path.exists(photo_path):
            slide11.shapes.add_picture(photo_path, px, py, photo_w, photo_h)
        else:
            fallback = slide11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, px, py, photo_w, photo_h)
            fallback.fill.solid(); fallback.fill.fore_color.rgb = m["color"]; fallback.line.fill.background()
            tf_fb = fallback.text_frame; p_fb = tf_fb.paragraphs[0]
            p_fb.text = m["name"][0]; p_fb.font.size = Pt(48); p_fb.font.color.rgb = C_WHITE
            p_fb.font.bold = True; p_fb.alignment = PP_ALIGN.CENTER

        # Info below photo
        info_y = py + photo_h + Inches(0.15)
        add_textbox(slide11, x + Inches(0.12), info_y, card_w - Inches(0.24), Inches(0.28),
                    m["name"], font_name=FONT_TITLE, font_size=Pt(18), color=C_TEXT, bold=True,
                    alignment=PP_ALIGN.CENTER)
        add_textbox(slide11, x + Inches(0.12), info_y + Inches(0.3), card_w - Inches(0.24), Inches(0.2),
                    m["role"], font_name=FONT_BODY, font_size=SIZE_LABEL, color=C_PRIMARY, bold=True,
                    alignment=PP_ALIGN.CENTER)
        add_textbox(slide11, x + Inches(0.12), info_y + Inches(0.5), card_w - Inches(0.24), Inches(0.35),
                    f"{m['bg']}\nID: {m['id']}", font_name=FONT_BODY, font_size=Pt(10), color=C_TEXT_SEC,
                    alignment=PP_ALIGN.CENTER)

    add_page_number(slide11, page)

    # ── Slide 12: Team SDG Assignments ──
    page += 1
    slide12 = build_light_slide(prs, "Team SDG Assignments",
                                 "Who worked on which goals, and why")
    rows, cols = 5, 4
    tbl_shape = slide12.shapes.add_table(rows, cols, MARGIN_L, Inches(1.8), CONTENT_W, Inches(3.8))
    tbl = tbl_shape.table
    headers = ["Team Member", "Assigned SDGs", "Rationale for Assignment", "Academic Background"]
    widths = [Inches(1.8), Inches(2.5), Inches(4.5), Inches(2.13)]
    for ci, h in enumerate(headers):
        tbl.columns[ci].width = widths[ci]
        cell = tbl.cell(0, ci); cell.text = h
        for p in cell.text_frame.paragraphs:
            p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = C_WHITE; p.font.name = FONT_BODY
        cell.fill.solid(); cell.fill.fore_color.rgb = C_DARK_BG
    for ri, m in enumerate(TEAM_SDG_MAP):
        bg_match = next(t["bg"] for t in TEAM_DATA if t["name"] == m["name"])
        row_data = [m["name"], m["sdgs"], m["rationale"], bg_match]
        for ci, val in enumerate(row_data):
            cell = tbl.cell(ri + 1, ci); cell.text = val
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(13); p.font.name = FONT_BODY; p.font.color.rgb = C_TEXT
            if ri % 2 == 0:
                cell.fill.solid(); cell.fill.fore_color.rgb = C_TINT
    style_table_cells(tbl)
    add_page_number(slide12, page)

    # ── Slide 13: Mission & Vision ──
    page += 1
    slide13 = build_light_slide(prs, "What We're Trying to Do",
                                 "The point of this project, honestly stated")
    col13_w = Inches(5.05)
    add_gold_left_accent_card(slide13, MARGIN_L, Inches(1.65), col13_w, Inches(2.15),
        title="What We Set Out to Do",
        body="Build a website that explains all 17 SDGs clearly, includes an interactive carbon "
             "calculator people can actually use, and shows how individual choices connect to "
             "global issues. Nothing revolutionary — just making the information accessible.")
    add_gold_left_accent_card(slide13, MARGIN_L + col13_w + Inches(0.35), Inches(1.65), col13_w, Inches(2.15),
        title="What We'd Like to See",
        body="More people understanding that the SDGs aren't just for governments and NGOs. "
             "The choices we make every day — what we eat, how we get around, what we throw away — "
             "are directly connected to global sustainability. Small changes at scale matter.")
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
    slide14 = build_light_slide(prs, "Website Walkthrough",
                                 "A quick tour of the main pages we built")
    # Screenshots with labels
    screenshots = [
        ("output/screenshots/home.png",   "Homepage"),
        ("output/screenshots/sdgs.png",   "SDGs Explorer"),
        ("output/screenshots/carbon.png", "Carbon Calculator"),
        ("output/screenshots/actnow.png", "Act Now"),
    ]
    img_w = Inches(2.35); img_h = Inches(1.55); img_gap = Inches(0.3)
    img_total_w = 4 * img_w + 3 * img_gap; img_start_x = (SLIDE_W - img_total_w) // 2
    img_y = Inches(1.7)
    for i, (img_path, label) in enumerate(screenshots):
        x = img_start_x + i * (img_w + img_gap)
        if os.path.exists(img_path):
            # Rounded rect background then image on top
            add_rounded_rect(slide14, x, img_y, img_w, img_h, fill_color=C_BORDER)
            slide14.shapes.add_picture(img_path, x + Inches(0.02), img_y + Inches(0.02),
                                       img_w - Inches(0.04), img_h - Inches(0.04))
        else:
            # Fallback placeholder
            add_rounded_rect(slide14, x, img_y, img_w, img_h, fill_color=RGBColor(0xEE, 0xEA, 0xE4))
            add_textbox(slide14, x + Inches(0.2), img_y + Inches(0.45), img_w - Inches(0.4), Inches(0.6),
                        f"[ {label} ]", font_name=FONT_BODY, font_size=SIZE_CAPTION,
                        color=C_TEXT_SEC, alignment=PP_ALIGN.CENTER)
        # Label below
        add_textbox(slide14, x, img_y + Inches(1.62), img_w, Inches(0.3),
                    label, font_name=FONT_TITLE, font_size=SIZE_SMALL, color=C_TEXT, bold=True, alignment=PP_ALIGN.CENTER)
    # Tech callout
    add_textbox(slide14, MARGIN_L, Inches(5.5), CONTENT_W, Inches(0.3),
                "Built with: Vue 3 + TypeScript + Vue Router 4 + GSAP + Vite 6",
                font_name=FONT_BODY, font_size=SIZE_CAPTION, color=C_PRIMARY, bold=True, alignment=PP_ALIGN.CENTER)
    add_page_number(slide14, page)

    # ═══ SECTION E: INTERACTIVE FEATURES ═══
    # ── Slide 15: Carbon Footprint Calculator ──
    page += 1
    slide15 = build_light_slide(prs, "Carbon Footprint Calculator",
                                 "How our interactive calculator estimates your annual CO₂ emissions")
    cat_w = Inches(2.5); cat_h = Inches(3.1); cat_gap = Inches(0.2)
    cat_total_w = 4 * cat_w + 3 * cat_gap; cat_start_x = (SLIDE_W - cat_total_w) // 2
    for i, cat in enumerate(CARBON_CATEGORIES):
        x = cat_start_x + i * (cat_w + cat_gap); y = Inches(1.65)
        add_rounded_rect(slide15, x, y, cat_w, cat_h)
        add_textbox(slide15, x + Inches(0.2), y + Inches(0.15), cat_w - Inches(0.4), Inches(0.3),
                    f"{cat['icon']}  {cat['name']}", font_name=FONT_TITLE, font_size=Pt(14), color=C_PRIMARY, bold=True)
        _, tf_cat = add_textbox(slide15, x + Inches(0.2), y + Inches(0.55), cat_w - Inches(0.4), Inches(0.3),
                                "", font_size=Pt(11), color=C_TEXT_SEC)
        for factor in cat["factors"]:
            add_paragraph(tf_cat, f"•  {factor}", font_size=Pt(11), color=C_TEXT_SEC, space_after=Pt(4))
    # Rating summary
    _, tf_ratings = add_textbox(slide15, MARGIN_L, Inches(5.05), CONTENT_W, Inches(0.3),
                                "Rating Thresholds:", font_name=FONT_BODY, font_size=SIZE_SMALL, color=C_TEXT, bold=True)
    for lv in CARBON_LEVELS:
        add_paragraph(tf_ratings, f"{lv['level']}: {lv['range']} — {lv['msg']}",
                      font_size=SIZE_CAPTION, color=lv["color"], bold=True)
    add_page_number(slide15, page)

    # ── Slide 16: Act Now ──
    page += 1
    slide16 = build_light_slide(prs, "What You Can Actually Do",
                                 "Simple changes that make a real difference — no heroics required")
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
    slide17 = build_light_slide(prs, "How We Built It",
                                 "The tech stack and architecture behind the website")
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
                p.font.size = Pt(12); p.font.name = FONT_BODY; p.font.color.rgb = C_TEXT
            if ri % 2 == 0:
                cell.fill.solid(); cell.fill.fore_color.rgb = C_TINT
    style_table_cells(tbl17)
    add_page_number(slide17, page)

    # ═══ SECTION F: CLOSING ═══
    # ── Slide 18: Key Takeaways ──
    page += 1
    slide18 = build_light_slide(prs, "What We Learned", "Five things this project taught us about the SDGs")
    takeaways = [
        ("Everything Is Connected",
         "You can't fix poverty without also addressing education, health, and gender equality. The SDGs work as a system, not a list. That's both the challenge and the point."),
        ("Everyone Is in This",
         "It's easy to think international goals are for governments and the UN. But businesses, local communities, and individual choices are how these goals actually get implemented — or don't."),
        ("Tech Helps, But It's Just a Tool",
         "Our carbon calculator makes an abstract concept feel personal. But the hard part isn't the technology — it's getting people to care enough to use it and act on the results."),
        ("Small Changes Compound",
         "One person switching to public transit doesn't matter. Millions doing it changes emissions trajectories. The scale problem cuts both ways — individual actions feel tiny, but they're the only lever we have."),
        ("2030 Is Close and We're Behind",
         "The UN's own midpoint review found only 15% of SDG targets are on track. Four years isn't much time. This isn't a future problem we're preparing for — it's happening now."),
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
    slide19 = build_dark_slide(prs, "So, What Can You Do?",
                                "The whole point of learning about the SDGs is doing something with that knowledge", transition="dissolve")
    add_textbox(slide19, Inches(2.0), Inches(4.3), Inches(9.3), Inches(0.5),
                "Check out the 17 goals on our site. Try the carbon calculator.\nPick one thing to change and see if it sticks.",
                font_name=FONT_BODY, font_size=SIZE_BODY, color=RGBColor(0xAA, 0xAA, 0xBB), alignment=PP_ALIGN.CENTER)
    add_textbox(slide19, Inches(2.5), Inches(5.1), Inches(8.3), Inches(0.5),
                "The SDGs aren't just for the UN. They're for everyone.",
                font_name=FONT_TITLE, font_size=SIZE_SMALL, color=C_PRIMARY, alignment=PP_ALIGN.CENTER)
    add_page_number(slide19, page)

    # ── Slide 20: Thank You & References ──
    page += 1
    slide20 = build_light_slide(prs, "Thanks", "Questions, comments, arguments — all welcome", transition="dissolve")
    add_textbox(slide20, Inches(2.0), Inches(1.6), Inches(9.3), Inches(0.8),
                "Thanks for Listening",
                font_name=FONT_TITLE, font_size=Pt(30), color=C_TEXT, bold=True, alignment=PP_ALIGN.CENTER)
    # References column
    _, tf_ref = add_textbox(slide20, MARGIN_L, Inches(2.8), Inches(5.5), Inches(0.3),
                            "Sources We Used", font_name=FONT_TITLE, font_size=SIZE_HEADING, color=C_TEXT, bold=True)
    refs = [
        "United Nations. (2015). Transforming Our World: The 2030 Agenda. A/RES/70/1.",
        "IPCC. (2023). Climate Change 2023: Synthesis Report.",
        "UN DESA. (2024). The Sustainable Development Goals Report 2024.",
        "UN Stats. SDG Indicators Database. https://unstats.un.org/sdgs",
    ]
    for ref in refs:
        add_paragraph(tf_ref, f"•  {ref}", font_size=SIZE_CAPTION, color=C_TEXT_SEC)
    # Team column
    _, tf_team = add_textbox(slide20, Inches(7.5), Inches(2.8), Inches(4.5), Inches(0.3),
                             "Team", font_name=FONT_TITLE, font_size=SIZE_HEADING, color=C_TEXT, bold=True)
    for m in TEAM_DATA:
        add_paragraph(tf_team, f"{m['name']} — {m['role']}", font_size=SIZE_SMALL, color=C_TEXT)
        add_paragraph(tf_team, f"{m['bg']}  ·  {m['id']}", font_size=SIZE_CAPTION, color=C_TEXT_SEC)
    add_textbox(slide20, Inches(2.0), Inches(5.8), Inches(9.3), Inches(0.4),
                "Happy to take questions — or just chat about the SDGs",
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
            p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = C_WHITE; p.font.name = FONT_BODY
        cell.fill.solid(); cell.fill.fore_color.rgb = C_DARK_BG
    for ri, sdg in enumerate(SDG_DATA):
        for ci, key in enumerate(["id", "en", "short"]):
            cell = tbl21.cell(ri + 1, ci); cell.text = str(sdg[key])
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(12); p.font.name = FONT_BODY; p.font.color.rgb = C_TEXT
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
        add_paragraph(tf_f, f"▹  {f}", font_name="Consolas", font_size=Pt(11), color=C_TEXT, space_after=Pt(3))
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
