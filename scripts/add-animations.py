"""Add slide transitions and shape animations to the PPTX file by manipulating the underlying XML."""
from pptx import Presentation
from pptx.util import Inches, Pt
from lxml import etree
from copy import deepcopy
import os

# Constants for transition speeds
SLOW = "slow"
MED = "med"
FAST = "fast"

# Transition types that PowerPoint supports
TRANSITIONS = {
    "fade": "fade",
    "push": "push",
    "wipe": "wipe",
    "cover": "cover",
    "uncover": "uncover",
    "dissolve": "dissolve",
    "split": "split",
    "reveal": "reveal",
    "random": "random",
    "zoom": "zoom",
    "glitter": "glitter",
    "vortex": "vortex",
    "ripple": "ripple",
    "comb": "comb",
    "fracture": "fracture",
    "crush": "crush",
    "peel": "peelOff",
    "pageCurl": "pageCurl",
    "wind": "wind",
    "warp": "warp",
    "morph": "morph",
}

def add_slide_transition(slide, trans_type="fade", speed="fast", duration_ms=400):
    """Add a slide transition effect to a slide."""
    nsmap = {
        'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
        'p14': 'http://schemas.microsoft.com/office/powerpoint/2010/main',
    }

    cSld = slide._element
    # Remove existing transitions
    for existing in cSld.findall('p:transition', nsmap):
        cSld.remove(existing)

    # Create transition element
    trans_el = etree.SubElement(cSld, f'{{{nsmap["p"]}}}transition')
    trans_el.set('spd', speed)
    trans_el.set('advTm', str(duration_ms))

    # Add the specific transition type
    # Map friendly names to their XML namespace
    trans_ns14 = ['morph']
    if trans_type in trans_ns14:
        child = etree.SubElement(trans_el, f'{{{nsmap["p14"]}}}{trans_type}')
    else:
        child = etree.SubElement(trans_el, f'{{{nsmap["p"]}}}{trans_type}')

    # Add optional attributes for directional transitions
    if trans_type in ('push', 'wipe', 'cover', 'uncover', 'reveal', 'comb', 'fracture'):
        child.set('dir', 'l')  # from left

    slide._element = cSld


def add_element_animation(slide, shape_idx, anim_type="fade", delay_ms=0, duration_ms=500):
    """
    Add an entrance animation to a specific shape on a slide.

    Args:
        slide: The slide object
        shape_idx: Index of the shape in slide.shapes (0-based)
        anim_type: "fade", "flyIn", "floatIn", "grow", "zoom", "swivel", "bounce", "wipe"
        delay_ms: Delay before animation starts
        duration_ms: Duration of the animation
    """
    nsmap = {
        'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
        'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    }

    # Build the animation type string
    anim_type_map = {
        "fade": "animEffectFade",
        "flyIn": "animEffectFly",
        "floatIn": "animEffectFloat",
        "grow": "animEffectGrow",
        "zoom": "animEffectZoom",
        "swivel": "animEffectSwivel",
        "bounce": "animEffectBounce",
        "wipe": "animEffectWipe",
        "wheel": "animEffectWheel",
    }

    ppt_anim = anim_type_map.get(anim_type, "animEffectFade")

    cSld = slide._element

    # Get or create timing section
    timing = cSld.find('p:timing', nsmap)
    if timing is None:
        timing = etree.SubElement(cSld, f'{{{nsmap["p"]}}}timing')

    # Create the animation tree
    # Build a simple animation: one element fades/enters
    anim_xml = f"""
    <p:timing xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"
              xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
        <p:tnLst>
            <p:par>
                <p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot">
                    <p:childTnLst>
                        <p:seq concurrent="1" nextAc="seek">
                            <p:cTn id="2" dur="indefinite" nodeType="mainSeq">
                                <p:childTnLst>
                                    <p:par>
                                        <p:cTn id="3" fill="hold">
                                            <p:stCondLst>
                                                <p:cond delay="{delay_ms}"/>
                                            </p:stCondLst>
                                            <p:childTnLst>
                                                <p:par>
                                                    <p:cTn id="4" dur="{duration_ms}" fill="hold">
                                                        <p:childTnLst>
                                                            <p:animEffect transition="in" filter="fade">
                                                                <p:cBhvr>
                                                                    <p:cTn id="5" dur="{duration_ms}" fill="hold"/>
                                                                    <p:tgtEl>
                                                                        <p:spTgt spid="{shape_idx}"/>
                                                                    </p:tgtEl>
                                                                </p:cBhvr>
                                                            </p:animEffect>
                                                        </p:childTnLst>
                                                    </p:cTn>
                                                </p:par>
                                            </p:childTnLst>
                                        </p:cTn>
                                    </p:par>
                                </p:childTnLst>
                            </p:cTn>
                        </p:seq>
                    </p:childTnLst>
                </p:cTn>
            </p:par>
        </p:tnLst>
    </p:timing>
    """

    # Remove existing timing
    for existing in cSld.findall('p:timing', nsmap):
        cSld.remove(existing)

    # Parse and append new timing
    timing_el = etree.fromstring(anim_xml)
    cSld.append(timing_el)


def apply_animations_to_pptx(input_path, output_path):
    """Read the generated PPTX, apply slide transitions and element animations, save new file."""
    prs = Presentation(input_path)

    total = len(prs.slides)

    for i, slide in enumerate(prs.slides):
        slide_num = i + 1

        # ── Slide transitions ──
        if slide_num == 1:
            # Title slide: no transition (first slide)
            pass
        elif slide_num in (3, 6, 11, 15, 18, 21):
            # Section openers: push from left
            add_slide_transition(slide, "push", FAST, 500)
        elif slide_num in (9, 10):
            # Spotlight slides: morph-like zoom
            add_slide_transition(slide, "cover", MED, 600)
        elif slide_num == 19:
            # CTA dark slide: fade
            add_slide_transition(slide, "fade", MED, 800)
        elif slide_num == 20:
            # Thank you: dissolve
            add_slide_transition(slide, "dissolve", FAST, 500)
        else:
            # Regular content: quick fade
            add_slide_transition(slide, "fade", FAST, 300)

    prs.save(output_path)
    print(f"Applied transitions to {total} slides → {output_path}")


if __name__ == "__main__":
    src = "output/UN-SDGs-Presentation.pptx"
    dst = "output/UN-SDGs-Presentation.pptx"
    apply_animations_to_pptx(src, dst)
