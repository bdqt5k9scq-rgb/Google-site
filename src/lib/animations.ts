import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

// Register ScrollTrigger globally — only once
gsap.registerPlugin(ScrollTrigger)

// Global GSAP defaults — unified easing and duration
gsap.defaults({
  ease: 'power2.out',
  duration: 0.6,
  overwrite: 'auto',
})

// ======= GSAP easing presets =======
export const GSAP_EASE = {
  out: 'power3.out',
  inOut: 'power2.inOut',
  smooth: 'power2.out',
  elastic: 'elastic.out(1, 0.4)',
  back: 'back.out(1.7)',
  in: 'power2.in',
} as const

// ======= Scroll trigger utility functions =======

/**
 * Fade in + move up from below — triggers on scroll into viewport
 * Returns ScrollTrigger instance for manual kill
 */
export function createScrollFade(
  target: gsap.DOMTarget,
  vars?: gsap.TweenVars
): ScrollTrigger {
  return gsap.fromTo(target,
    { y: 60, opacity: 0 },
    {
      y: 0, opacity: 1, duration: 0.8, ease: 'power3.out',
      scrollTrigger: { trigger: target, start: 'top 85%' },
      ...vars,
    }
  ).scrollTrigger as ScrollTrigger
}

/**
 * Staggered fade-in for child elements within a container — triggers on scroll into viewport
 */
export function createStaggerFade(
  target: gsap.DOMTarget,
  childSelector: string,
  vars?: gsap.TweenVars
): ScrollTrigger {
  return gsap.fromTo(childSelector,
    { y: 50, opacity: 0, scale: 0.95 },
    {
      y: 0, opacity: 1, scale: 1,
      duration: 0.6, stagger: 0.08, ease: 'power3.out',
      scrollTrigger: { trigger: target, start: 'top 85%' },
      ...vars,
    }
  ).scrollTrigger as ScrollTrigger
}

/**
 * Slide in from left — triggers on scroll into viewport
 */
export function createSlideLeft(
  target: gsap.DOMTarget,
  vars?: gsap.TweenVars
): ScrollTrigger {
  return gsap.fromTo(target,
    { x: -60, opacity: 0 },
    {
      x: 0, opacity: 1, duration: 0.7, ease: 'power3.out',
      scrollTrigger: { trigger: target, start: 'top 85%' },
      ...vars,
    }
  ).scrollTrigger as ScrollTrigger
}
