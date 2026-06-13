<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import gsap from 'gsap'
import { GSAP_EASE } from '@/lib/animations'

const actions = [
  { id: 1, title: 'Save Electricity', description: 'Use energy-efficient bulbs, turn off unnecessary appliances, use solar-powered devices', category: 'Energy', tips: ['Replace traditional lighting with LED bulbs', 'Turn off standby appliances to save energy', 'Consider installing solar panels'] },
  { id: 2, title: 'Green Transportation', description: 'Choose public transport, cycling, or walking; reduce private car use', category: 'Transport', tips: ['Prioritize public transportation', 'Cycle or walk for short distances', 'Carpool with colleagues and friends'] },
  { id: 3, title: 'Reduce Waste', description: 'Reduce food waste, use reusable shopping bags and water bottles', category: 'Consumption', tips: ['Bring your own shopping bags', 'Refuse disposable tableware', 'Plan meals wisely to avoid waste'] },
  { id: 4, title: 'Healthy Eating', description: 'Reduce meat consumption, eat more local and organic food', category: 'Diet', tips: ['Try one meat-free day per week', 'Prioritize buying local produce', 'Grow vegetables and herbs at home'] },
  { id: 5, title: 'Water Conservation', description: 'Save water, fix leaks, collect rainwater', category: 'Resources', tips: ['Shorten your shower time', 'Fix leaky faucets promptly', 'Collect rainwater for watering plants'] },
  { id: 6, title: 'Tree Planting', description: 'Participate in tree planting, support forest conservation projects', category: 'Environment', tips: ['Join community tree planting events', 'Support forestry conservation projects', 'Plant native tree species'] },
  { id: 7, title: 'Waste Sorting', description: 'Sort waste properly, promote resource recycling', category: 'Waste', tips: ['Learn about waste sorting', 'Participate in community recycling programs', 'Support circular economy products'] },
  { id: 8, title: 'Education & Advocacy', description: 'Share sustainable development ideas with others, encourage more people to get involved', category: 'Education', tips: ['Share environmental knowledge with friends', 'Organize community environmental activities', 'Join environmental non-profit organizations'] }
]

const categories = ['All', 'Energy', 'Transport', 'Consumption', 'Diet', 'Resources', 'Environment', 'Waste', 'Education']
const selectedCategory = ref('All')

const filteredActions = computed(() => {
  if (selectedCategory.value === 'All') return actions
  return actions.filter(action => action.category === selectedCategory.value)
})

const currentYear = new Date().getFullYear()
const yearsLeft = 2030 - currentYear

const actStats = [
  { value: '193', label: 'Member States Committed' },
  { value: '17', label: 'Sustainable Development Goals' },
  { value: '7.8 Billion', label: 'Global Population' },
  { value: String(yearsLeft), label: 'Years Remaining' }
]

onMounted(() => {
  gsap.context(() => {
    const header = document.querySelector('.act-now .act-header')
    if (header) {
      gsap.fromTo(header.querySelector('h1'),
        { y: 48, opacity: 0 },
        { y: 0, opacity: 1, duration: 0.9, ease: GSAP_EASE.out }
      )
      gsap.fromTo(header.querySelector('p'),
        { y: 32, opacity: 0 },
        { y: 0, opacity: 1, duration: 0.7, delay: 0.15, ease: GSAP_EASE.out }
      )
      gsap.fromTo('.countdown-item',
        { y: 48, opacity: 0 },
        { y: 0, opacity: 1, duration: 0.7, stagger: 0.12, delay: 0.4, ease: GSAP_EASE.back }
      )
    }

    gsap.fromTo('.stat-item',
      { y: 48, opacity: 0 },
      { y: 0, opacity: 1, duration: 0.6, stagger: 0.1, ease: GSAP_EASE.out,
        scrollTrigger: { trigger: '.act-stats', start: 'top 85%' } }
    )

    gsap.fromTo('.filter-btn',
      { y: 24, opacity: 0 },
      { y: 0, opacity: 1, duration: 0.4, stagger: 0.04, ease: GSAP_EASE.out,
        scrollTrigger: { trigger: '.category-filter', start: 'top 90%' } }
    )

    gsap.fromTo('.action-card',
      { y: 56, opacity: 0 },
      { y: 0, opacity: 1, duration: 0.6, stagger: 0.07, ease: GSAP_EASE.out,
        scrollTrigger: { trigger: '.actions-grid', start: 'top 85%' } }
    )

    gsap.fromTo('.call-to-action',
      { y: 48, opacity: 0 },
      { y: 0, opacity: 1, duration: 0.8, ease: GSAP_EASE.out,
        scrollTrigger: { trigger: '.call-to-action', start: 'top 85%' } }
    )

    const cards = gsap.utils.toArray<HTMLElement>('.action-card, .stat-item')
    cards.forEach((card) => {
      card.addEventListener('mouseenter', () => {
        gsap.to(card, { y: -6, duration: 0.3, ease: 'power2.out' })
      })
      card.addEventListener('mouseleave', () => {
        gsap.to(card, { y: 0, duration: 0.35, ease: 'power2.out' })
      })
    })
  })
})
</script>

<template>
  <div class="act-now">
    <!-- ====== Header ====== -->
    <section class="act-header">
      <div class="container container-narrow">
        <p class="act-eyebrow">Act Now</p>
        <h1>Take Action Now</h1>
        <p>Every small action can make a difference for our planet. Join us in moving toward a sustainable future.</p>
        <!-- Countdown -->
        <div class="countdown">
          <div class="countdown-item">
            <span class="countdown-num">{{ yearsLeft }}</span>
            <span class="countdown-label">Years</span>
          </div>
          <span class="countdown-sep">:</span>
          <div class="countdown-item">
            <span class="countdown-num">12</span>
            <span class="countdown-label">Months</span>
          </div>
          <span class="countdown-sep">:</span>
          <div class="countdown-item">
            <span class="countdown-num">31</span>
            <span class="countdown-label">Days</span>
          </div>
          <p class="countdown-text">Until the 2030 deadline</p>
        </div>
      </div>
    </section>

    <!-- ====== Stats ====== -->
    <section class="act-stats">
      <div class="container">
        <div class="stats-grid">
          <div v-for="stat in actStats" :key="stat.label" class="stat-item">
            <div class="stat-value">{{ stat.value }}</div>
            <div class="stat-label">{{ stat.label }}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- ====== Actions ====== -->
    <section class="actions-section">
      <div class="container">
        <h2 class="section-title">Actions You Can Take</h2>
        <p class="section-subtitle">Choose an area that suits you and start making a difference</p>

        <div class="category-filter">
          <button
            v-for="category in categories"
            :key="category"
            class="filter-btn"
            :class="{ active: selectedCategory === category }"
            @click="selectedCategory = category"
          >
            {{ category }}
          </button>
        </div>

        <div class="actions-grid">
          <div
            v-for="action in filteredActions"
            :key="action.id"
            class="action-card"
          >
            <span class="action-num">{{ String(action.id).padStart(2, '0') }}</span>
            <h3>{{ action.title }}</h3>
            <p>{{ action.description }}</p>
            <span class="action-category">{{ action.category }}</span>
            <ul class="action-tips">
              <li v-for="(tip, index) in action.tips" :key="index">
                <span class="tip-dot"></span> {{ tip }}
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- ====== CTA ====== -->
    <section class="call-to-action">
      <div class="container container-narrow">
        <p class="cta-eyebrow">Join Us</p>
        <h2>Every Action Matters</h2>
        <p>Start today, make a change, and contribute to sustainable development. Every choice you make is shaping the future.</p>
        <div class="cta-buttons">
          <a href="/sdgs" class="btn btn-primary">Learn More About the SDGs</a>
          <a href="/carbon-footprint" class="btn btn-secondary">Calculate Your Carbon Footprint</a>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* ====== Header ====== */
.act-header {
  background: linear-gradient(165deg, #1c1c24 0%, #252530 40%, #1c1c24 100%);
  color: #fff;
  padding: 72px 0;
  text-align: center;
  position: relative;
  overflow: hidden;
}

.act-header::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image:
    url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.025'/%3E%3C/svg%3E");
  pointer-events: none;
}

.act-eyebrow {
  font-family: var(--font-body, sans-serif);
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--color-sage, #5c8d6d);
  margin-bottom: 12px;
}

.act-header h1 {
  font-family: var(--font-display, Georgia, serif);
  font-size: clamp(2.2rem, 4vw, 3rem);
  color: #fff;
  margin-bottom: 16px;
}

.act-header > .container > p {
  color: rgba(255, 255, 255, 0.55);
  font-size: 1.08rem;
  max-width: 560px;
  margin: 0 auto 36px;
}

/* Countdown */
.countdown {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  flex-wrap: wrap;
  margin-top: 32px;
}

.countdown-item {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.08);
  padding: 20px 24px;
  border-radius: var(--radius-lg, 12px);
  text-align: center;
  min-width: 90px;
  backdrop-filter: blur(8px);
}

.countdown-num {
  font-family: var(--font-display, Georgia, serif);
  font-size: 2.4rem;
  font-weight: 700;
  display: block;
  line-height: 1;
}

.countdown-label {
  font-size: 0.8rem;
  opacity: 0.55;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin-top: 4px;
  display: block;
}

.countdown-sep {
  font-size: 1.8rem;
  opacity: 0.3;
  font-weight: 300;
}

.countdown-text {
  width: 100%;
  margin-top: 16px;
  opacity: 0.45;
  font-size: 0.9rem;
}

/* ====== Stats ====== */
.act-stats {
  background: var(--color-paper, #fdfaf6);
  padding: 48px 0;
  border-bottom: 1px solid var(--color-border-light, #f0ebe4);
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0;
}

.stat-item {
  text-align: center;
  padding: 24px 16px;
  position: relative;
  cursor: default;
}

.stat-item:not(:last-child)::after {
  content: '';
  position: absolute;
  right: 0;
  top: 20%;
  height: 60%;
  width: 1px;
  background: var(--color-sand, #e8dfd5);
}

.stat-value {
  font-family: var(--font-display, Georgia, serif);
  font-size: 2.6rem;
  font-weight: 700;
  color: var(--color-terracotta, #c48b5c);
  line-height: 1;
  margin-bottom: 6px;
}

.stat-label {
  color: var(--color-text-muted, #6b6560);
  font-size: 0.88rem;
  font-weight: 500;
}

/* ====== Actions ====== */
.actions-section {
  padding: 72px 0;
  background: var(--color-cream, #fefcf9);
}

.category-filter {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  justify-content: center;
  margin-bottom: 36px;
}

.filter-btn {
  padding: 8px 20px;
  border: 1.5px solid var(--color-border, #e6e0d8);
  background: #fff;
  color: var(--color-text-muted, #6b6560);
  border-radius: 100px;
  cursor: pointer;
  font-size: 0.88rem;
  font-weight: 500;
  transition: all 0.25s ease;
  font-family: var(--font-body, sans-serif);
}

.filter-btn:hover {
  border-color: var(--color-terracotta, #c48b5c);
  color: var(--color-terracotta, #c48b5c);
}

.filter-btn.active {
  background: var(--color-terracotta, #c48b5c);
  color: #fff;
  border-color: var(--color-terracotta, #c48b5c);
}

.actions-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(290px, 1fr));
  gap: 16px;
}

.action-card {
  background: #fff;
  border: 1px solid var(--color-border-light, #f0ebe4);
  border-radius: var(--radius-lg, 12px);
  padding: 28px;
  transition: all 0.35s var(--ease-out, cubic-bezier(0.16, 1, 0.3, 1));
  cursor: default;
}

.action-card:hover {
  box-shadow: var(--shadow-lg, 0 12px 32px rgba(28, 28, 36, 0.08));
  border-color: transparent;
}

.action-num {
  font-family: var(--font-display, Georgia, serif);
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  color: var(--color-terracotta, #c48b5c);
  opacity: 0.6;
  display: block;
  margin-bottom: 10px;
}

.action-card h3 {
  font-family: var(--font-display, Georgia, serif);
  font-size: 1.15rem;
  color: var(--color-ink, #1c1c24);
  margin-bottom: 8px;
}

.action-card p {
  color: var(--color-text-muted, #6b6560);
  font-size: 0.9rem;
  margin-bottom: 12px;
  line-height: 1.6;
}

.action-category {
  display: inline-block;
  padding: 3px 12px;
  background: rgba(196, 139, 92, 0.07);
  color: var(--color-terracotta, #c48b5c);
  border-radius: 100px;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.03em;
  margin-bottom: 14px;
}

.action-tips {
  list-style: none;
}

.action-tips li {
  padding: 6px 0;
  display: flex;
  align-items: flex-start;
  gap: 8px;
  color: var(--color-text-muted, #6b6560);
  font-size: 0.85rem;
  line-height: 1.5;
}

.tip-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: var(--color-sand, #e8dfd5);
  margin-top: 6px;
  flex-shrink: 0;
}

/* ====== CTA ====== */
.call-to-action {
  background: linear-gradient(165deg, #1c1c24 0%, #252530 40%, #1c1c24 100%);
  color: #fff;
  padding: 72px 0;
  text-align: center;
  position: relative;
  overflow: hidden;
}

.call-to-action::before {
  content: '';
  position: absolute;
  top: -80px;
  left: -60px;
  width: 350px;
  height: 350px;
  background: radial-gradient(ellipse at center, rgba(92, 141, 109, 0.1) 0%, transparent 70%);
  border-radius: 50% 55% 45% 50% / 60% 45% 55% 40%;
  pointer-events: none;
}

.cta-eyebrow {
  font-family: var(--font-body, sans-serif);
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--color-sage, #5c8d6d);
  margin-bottom: 12px;
}

.call-to-action h2 {
  font-family: var(--font-display, Georgia, serif);
  font-size: clamp(1.8rem, 3.5vw, 2.4rem);
  color: #fff;
  margin-bottom: 16px;
}

.call-to-action p {
  color: rgba(255, 255, 255, 0.55);
  font-size: 1.08rem;
  max-width: 520px;
  margin: 0 auto 32px;
  line-height: 1.7;
}

.cta-buttons {
  display: flex;
  gap: 12px;
  justify-content: center;
  flex-wrap: wrap;
  position: relative;
  z-index: 1;
}

.cta-buttons .btn-secondary {
  color: rgba(255, 255, 255, 0.8);
  border-color: rgba(255, 255, 255, 0.2);
}

.cta-buttons .btn-secondary:hover {
  border-color: var(--color-terracotta, #c48b5c);
  color: var(--color-terracotta, #c48b5c);
  background-color: rgba(196, 139, 92, 0.08);
}

@media (max-width: 768px) {
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .stat-item:nth-child(2)::after {
    display: none;
  }

  .actions-grid {
    grid-template-columns: 1fr;
  }

  .countdown-item {
    min-width: 70px;
    padding: 14px 16px;
  }

  .countdown-num {
    font-size: 1.8rem;
  }
}
</style>
