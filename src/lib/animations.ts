import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

// 全局注册 ScrollTrigger — 仅需一次
gsap.registerPlugin(ScrollTrigger)

// 全局 GSAP 默认值 — 统一缓动和时长
gsap.defaults({
  ease: 'power2.out',
  duration: 0.6,
  overwrite: 'auto',
})

// ======= GSAP 缓动预设 =======
export const GSAP_EASE = {
  out: 'power3.out',
  inOut: 'power2.inOut',
  smooth: 'power2.out',
  elastic: 'elastic.out(1, 0.4)',
  back: 'back.out(1.7)',
  in: 'power2.in',
} as const

// ======= 滚动触发工具函数 =======

/**
 * 元素从下方淡入 + 上移 — 滚动到视口时触发
 * 返回 ScrollTrigger 实例，用于手动 kill
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
 * 容器内子元素交错淡入 — 滚动到视口时触发
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
 * 元素从左侧滑入 — 滚动到视口时触发
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
