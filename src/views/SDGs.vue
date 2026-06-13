<script setup lang="ts">
import { ref, nextTick, onMounted } from 'vue'
import gsap from 'gsap'
import { GSAP_EASE } from '@/lib/animations'

const sdgs = [
  { id: 1, title: 'End Poverty', subtitle: 'No Poverty', color: '#e5243b', description: 'End poverty in all its forms everywhere. Ensure that all men and women, particularly the poor and vulnerable, have equal rights to economic resources, as well as access to basic services, ownership, and control over land and other forms of property.' },
  { id: 2, title: 'Zero Hunger', subtitle: 'Zero Hunger', color: '#dda63a', description: 'End hunger, achieve food security, improve nutrition, and promote sustainable agriculture. By 2030, ensure that all people have access to safe, nutritious, and sufficient food year-round.' },
  { id: 3, title: 'Good Health and Well-being', subtitle: 'Good Health and Well-being', color: '#4c9f38', description: 'Ensure healthy lives and promote well-being for all at all ages. By 2030, reduce the global maternal mortality ratio to less than 70 per 100,000 live births.' },
  { id: 4, title: 'Quality Education', subtitle: 'Quality Education', color: '#c5192d', description: 'Ensure inclusive and equitable quality education and promote lifelong learning opportunities for all. By 2030, ensure that all girls and boys complete free, equitable, and quality primary and secondary education leading to relevant and effective learning outcomes.' },
  { id: 5, title: 'Gender Equality', subtitle: 'Gender Equality', color: '#ff3a21', description: 'Achieve gender equality and empower all women and girls. End all forms of discrimination against all women and girls everywhere.' },
  { id: 6, title: 'Clean Water and Sanitation', subtitle: 'Clean Water and Sanitation', color: '#26bde2', description: 'Ensure availability and sustainable management of water and sanitation for all. By 2030, achieve universal and equitable access to safe and affordable drinking water for all.' },
  { id: 7, title: 'Affordable and Clean Energy', subtitle: 'Affordable and Clean Energy', color: '#fcc30b', description: 'Ensure access to affordable, reliable, sustainable, and modern energy for all. By 2030, ensure universal access to affordable, reliable, and modern energy services.' },
  { id: 8, title: 'Decent Work and Economic Growth', subtitle: 'Decent Work and Economic Growth', color: '#a21942', description: 'Promote sustained, inclusive, and sustainable economic growth, full and productive employment, and decent work for all.' },
  { id: 9, title: 'Industry, Innovation and Infrastructure', subtitle: 'Industry, Innovation and Infrastructure', color: '#fd6925', description: 'Build resilient infrastructure, promote inclusive and sustainable industrialization, and foster innovation.' },
  { id: 10, title: 'Reduced Inequalities', subtitle: 'Reduced Inequalities', color: '#dd1367', description: 'Reduce inequality within and among countries. By 2030, progressively achieve and sustain income growth of the bottom 40% of the population at a rate higher than the national average.' },
  { id: 11, title: 'Sustainable Cities and Communities', subtitle: 'Sustainable Cities and Communities', color: '#fd9d24', description: 'Make cities and human settlements inclusive, safe, resilient, and sustainable. By 2030, ensure access for all to adequate, safe, and affordable housing and basic services.' },
  { id: 12, title: 'Responsible Consumption and Production', subtitle: 'Responsible Consumption and Production', color: '#bf8b2e', description: 'Ensure sustainable consumption and production patterns. By 2030, achieve the sustainable management and efficient use of natural resources.' },
  { id: 13, title: 'Climate Action', subtitle: 'Climate Action', color: '#3f7e44', description: 'Take urgent action to combat climate change and its impacts. Strengthen resilience and adaptive capacity to climate-related hazards and natural disasters in all countries.' },
  { id: 14, title: 'Life Below Water', subtitle: 'Life Below Water', color: '#009444', description: 'Conserve and sustainably use the oceans, seas, and marine resources for sustainable development. End overfishing, illegal, unreported, and unregulated fishing.' },
  { id: 15, title: 'Life on Land', subtitle: 'Life on Land', color: '#00a651', description: 'Protect, restore, and promote sustainable use of terrestrial ecosystems, sustainably manage forests, combat desertification, halt and reverse land degradation, and halt biodiversity loss.' },
  { id: 16, title: 'Peace, Justice and Strong Institutions', subtitle: 'Peace, Justice and Strong Institutions', color: '#19489d', description: 'Promote peaceful and inclusive societies for sustainable development, provide access to justice for all, and build effective, accountable, and inclusive institutions at all levels.' },
  { id: 17, title: 'Partnerships for the Goals', subtitle: 'Partnerships for the Goals', color: '#192841', description: 'Strengthen the means of implementation and revitalize the global partnership for sustainable development. Enhance multi-stakeholder partnerships to mobilize and share knowledge, expertise, technology, and financial resources to achieve the Sustainable Development Goals.' }
]

const selectedSdg = ref<typeof sdgs[0] | null>(null)

const openModal = (sdg: typeof sdgs[0]) => {
  selectedSdg.value = sdg
  nextTick(() => {
    gsap.fromTo('.modal-overlay',
      { opacity: 0 },
      { opacity: 1, duration: 0.25 }
    )
    gsap.fromTo('.modal-content',
      { scale: 0.92, opacity: 0, y: 40 },
      { scale: 1, opacity: 1, y: 0, duration: 0.5, ease: GSAP_EASE.back }
    )
  })
}

const closeModal = () => {
  gsap.to('.modal-overlay', {
    opacity: 0, duration: 0.25,
    onComplete: () => { selectedSdg.value = null }
  })
  gsap.to('.modal-content', {
    scale: 0.92, opacity: 0, y: 20, duration: 0.2, ease: 'power2.in'
  })
}

onMounted(() => {
  gsap.context(() => {
    const header = document.querySelector('.sdgs-header')
    if (header) {
      gsap.fromTo(header.querySelector('h1'),
        { y: 48, opacity: 0 },
        { y: 0, opacity: 1, duration: 0.9, ease: GSAP_EASE.out }
      )
      gsap.fromTo(header.querySelector('p'),
        { y: 32, opacity: 0 },
        { y: 0, opacity: 1, duration: 0.7, delay: 0.15, ease: GSAP_EASE.out }
      )
    }

    // SDG cards — staggered reveal
    gsap.fromTo('.sdgs-grid .sdg-card',
      { y: 64, opacity: 0 },
      {
        y: 0, opacity: 1, duration: 0.5, stagger: 0.04, ease: GSAP_EASE.out,
        scrollTrigger: { trigger: '.sdgs-grid', start: 'top 92%' },
      }
    )

    gsap.fromTo('.sdgs-intro h2',
      { y: 40, opacity: 0 },
      { y: 0, opacity: 1, duration: 0.7, ease: GSAP_EASE.out,
        scrollTrigger: { trigger: '.sdgs-intro', start: 'top 85%' } }
    )
    gsap.fromTo('.sdgs-intro p',
      { y: 30, opacity: 0 },
      { y: 0, opacity: 1, duration: 0.6, stagger: 0.1, ease: GSAP_EASE.out,
        scrollTrigger: { trigger: '.sdgs-intro', start: 'top 85%' } }
    )

    // Card hover
    const cards = gsap.utils.toArray<HTMLElement>('.sdgs-grid .sdg-card')
    cards.forEach((card) => {
      card.addEventListener('mouseenter', () => {
        gsap.to(card, { y: -8, scale: 1.03, duration: 0.35, ease: 'power2.out' })
      })
      card.addEventListener('mouseleave', () => {
        gsap.to(card, { y: 0, scale: 1, duration: 0.4, ease: 'power2.out' })
      })
    })
  })
})
</script>

<template>
  <div class="sdgs">
    <!-- ====== Header ====== -->
    <section class="sdgs-header">
      <div class="container container-narrow">
        <p class="sdgs-eyebrow">United Nations &middot; 2015&ndash;2030</p>
        <h1>The 17 Sustainable Development Goals</h1>
        <p>Interconnected global goals designed to address our most pressing shared challenges by 2030</p>
      </div>
    </section>

    <!-- ====== Grid ====== -->
    <section class="sdgs-grid-section">
      <div class="container">
        <div class="sdgs-grid">
          <div
            v-for="sdg in sdgs"
            :key="sdg.id"
            class="sdg-card"
            :style="{ '--sdg-color': sdg.color }"
            @click="openModal(sdg)"
          >
            <span class="sdg-num">{{ String(sdg.id).padStart(2, '0') }}</span>
            <h3>{{ sdg.title }}</h3>
            <p class="sdg-sub">{{ sdg.subtitle }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ====== About ====== -->
    <section class="sdgs-intro">
      <div class="container container-narrow">
        <h2>About the Sustainable Development Goals</h2>
        <p>The UN Sustainable Development Goals (SDGs) are 17 global goals adopted by all 193 UN Member States in 2015, designed to address the most pressing challenges facing our world.</p>
        <p>These goals are interconnected — solving one often helps solve others. Improving education can help end poverty, and addressing climate change requires global cooperation and innovation.</p>
      </div>
    </section>

    <!-- ====== Modal ====== -->
    <Teleport to="body">
      <div v-if="selectedSdg" class="modal-overlay" @click="closeModal">
        <div class="modal-content" @click.stop>
          <div class="modal-header" :style="{ backgroundColor: selectedSdg.color }">
            <span class="modal-num">{{ String(selectedSdg.id).padStart(2, '0') }}</span>
            <div>
              <h2>{{ selectedSdg.title }}</h2>
              <p>{{ selectedSdg.subtitle }}</p>
            </div>
            <button class="modal-close" @click="closeModal" aria-label="Close">
              <svg width="20" height="20" viewBox="0 0 20 20"><path d="M5 5l10 10M15 5L5 15" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
            </button>
          </div>
          <div class="modal-body">
            <p>{{ selectedSdg.description }}</p>
          </div>
        </div>
      </div>
    </Teleport>
  </div>
</template>

<style scoped>
/* ====== Header ====== */
.sdgs-header {
  background: linear-gradient(165deg, #1c1c24 0%, #252530 40%, #1c1c24 100%);
  color: #fff;
  padding: 72px 0;
  text-align: center;
  position: relative;
  overflow: hidden;
}

.sdgs-header::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image:
    url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.025'/%3E%3C/svg%3E");
  pointer-events: none;
}

.sdgs-eyebrow {
  font-family: var(--font-body, sans-serif);
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--color-terracotta, #c48b5c);
  margin-bottom: 12px;
}

.sdgs-header h1 {
  font-family: var(--font-display, Georgia, serif);
  font-size: clamp(2.2rem, 4vw, 3rem);
  color: #fff;
  margin-bottom: 16px;
}

.sdgs-header p {
  color: rgba(255, 255, 255, 0.55);
  font-size: 1.08rem;
}

/* ====== Grid ====== */
.sdgs-grid-section {
  padding: 64px 0;
  background: var(--color-paper, #fdfaf6);
}

.sdgs-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(175px, 1fr));
  gap: 12px;
}

.sdg-card {
  background: #fff;
  border: 1px solid var(--color-border-light, #f0ebe4);
  border-radius: var(--radius-lg, 12px);
  padding: 24px 20px;
  cursor: pointer;
  transition: all 0.35s var(--ease-out, cubic-bezier(0.16, 1, 0.3, 1));
  position: relative;
  overflow: hidden;
}

.sdg-card::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--sdg-color);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.35s var(--ease-out, cubic-bezier(0.16, 1, 0.3, 1));
}

.sdg-card:hover {
  box-shadow: var(--shadow-lg, 0 12px 32px rgba(28, 28, 36, 0.08));
  border-color: transparent;
}

.sdg-card:hover::after {
  transform: scaleX(1);
}

.sdg-num {
  font-family: var(--font-display, Georgia, serif);
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  color: var(--sdg-color);
  opacity: 0.7;
  display: block;
  margin-bottom: 8px;
}

.sdg-card h3 {
  font-family: var(--font-display, Georgia, serif);
  font-size: 1rem;
  color: var(--color-ink, #1c1c24);
  margin-bottom: 4px;
}

.sdg-sub {
  font-size: 0.8rem;
  color: var(--color-text-light, #8c8782);
  font-style: italic;
}

/* ====== Intro ====== */
.sdgs-intro {
  padding: 64px 0;
  background: var(--color-cream, #fefcf9);
  border-top: 1px solid var(--color-border-light, #f0ebe4);
}

.sdgs-intro h2 {
  font-family: var(--font-display, Georgia, serif);
  text-align: center;
  margin-bottom: 24px;
  color: var(--color-ink, #1c1c24);
}

.sdgs-intro p {
  color: var(--color-text-muted, #6b6560);
  line-height: 1.8;
  margin-bottom: 16px;
}

/* ====== Modal ====== */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(28, 28, 36, 0.65);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 24px;
}

.modal-content {
  background: #fff;
  border-radius: var(--radius-xl, 20px);
  max-width: 560px;
  width: 100%;
  max-height: 80vh;
  overflow-y: auto;
  box-shadow: 0 32px 64px rgba(28, 28, 36, 0.25);
}

.modal-header {
  color: #fff;
  padding: 32px 28px;
  display: flex;
  gap: 20px;
  align-items: center;
  position: relative;
  border-radius: 20px 20px 0 0;
}

.modal-num {
  font-family: var(--font-display, Georgia, serif);
  font-size: 2.8rem;
  font-weight: 700;
  opacity: 0.85;
  line-height: 1;
}

.modal-header h2 {
  font-family: var(--font-display, Georgia, serif);
  font-size: 1.35rem;
  color: #fff;
  margin-bottom: 2px;
}

.modal-header p {
  opacity: 0.8;
  font-size: 0.9rem;
  font-style: italic;
}

.modal-close {
  position: absolute;
  top: 20px;
  right: 20px;
  width: 36px;
  height: 36px;
  border: none;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.15);
  color: #fff;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.25s ease;
}

.modal-close:hover {
  background: rgba(255, 255, 255, 0.28);
  transform: rotate(90deg);
}

.modal-body {
  padding: 32px 28px;
}

.modal-body p {
  color: var(--color-text-muted, #6b6560);
  line-height: 1.85;
  font-size: 1.05rem;
}

@media (max-width: 768px) {
  .sdgs-grid {
    grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
    gap: 8px;
  }

  .sdg-card {
    padding: 18px 14px;
  }

  .modal-header {
    flex-direction: column;
    text-align: center;
    padding: 24px 20px;
  }

  .modal-num {
    font-size: 2rem;
  }
}
</style>
