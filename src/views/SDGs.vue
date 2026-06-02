<script setup lang="ts">
import { ref, nextTick, onMounted } from 'vue'
import gsap from 'gsap'
import { GSAP_EASE } from '@/lib/animations'

const sdgs = [
  { id: 1, title: '消除贫困', subtitle: 'No Poverty', color: '#e5243b', description: '在世界各地消除一切形式的贫困。确保所有男女，特别是赤贫人口，享有平等获得经济资源的权利，以及获得基本服务、所有权和对土地及其他形式财产的控制权。' },
  { id: 2, title: '零饥饿', subtitle: 'Zero Hunger', color: '#dda63a', description: '消除饥饿，实现粮食安全，改善营养状况和促进可持续农业。到2030年，确保所有人全年都能获得安全、营养和充足的食物。' },
  { id: 3, title: '良好健康与福祉', subtitle: 'Good Health and Well-being', color: '#4c9f38', description: '确保健康的生活方式，促进各年龄段人群的福祉。到2030年，将全球孕产妇死亡率降低到每10万活产140人以下。' },
  { id: 4, title: '优质教育', subtitle: 'Quality Education', color: '#c5192d', description: '确保包容和公平的优质教育，促进全民终身学习。到2030年，确保所有男女儿童完成免费、公平和优质的初等和中等教育，并取得相关和有效的学习成果。' },
  { id: 5, title: '性别平等', subtitle: 'Gender Equality', color: '#ff3a21', description: '实现性别平等，增强所有妇女和女童的权能。消除对妇女和女童的一切形式歧视。' },
  { id: 6, title: '清洁饮水', subtitle: 'Clean Water and Sanitation', color: '#26bde2', description: '确保清洁饮水和卫生设施。到2030年，普遍和公平地获得安全和负担得起的饮用水。' },
  { id: 7, title: '廉价清洁能源', subtitle: 'Affordable and Clean Energy', color: '#fcc30b', description: '确保获得负担得起的、可靠的、可持续的和现代的能源。到2030年，确保人人获得负担得起的、可靠的现代能源服务。' },
  { id: 8, title: '体面工作与经济增长', subtitle: 'Decent Work and Economic Growth', color: '#a21942', description: '促进持久、包容和可持续的经济增长，促进充分的生产性就业和体面工作。' },
  { id: 9, title: '产业、创新与基础设施', subtitle: 'Industry, Innovation and Infrastructure', color: '#fd6925', description: '建造具备抵御灾害能力的基础设施，促进包容和可持续的工业化，推动创新。' },
  { id: 10, title: '减少不平等', subtitle: 'Reduced Inequalities', color: '#dd1367', description: '减少国家内部和国家之间的不平等。到2030年，根据各国国情，逐步实现并维持最底层40%人口的收入增长率高于全国平均水平。' },
  { id: 11, title: '可持续城市和社区', subtitle: 'Sustainable Cities and Communities', color: '#fd9d24', description: '建设包容、安全、有抵御灾害能力和可持续的城市和人类住区。到2030年，使城市和人类住区具有包容性、安全、韧性和可持续性。' },
  { id: 12, title: '负责任消费和生产', subtitle: 'Responsible Consumption and Production', color: '#bf8b2e', description: '确保可持续消费和生产模式。到2030年，实现全球可持续消费和生产模式。' },
  { id: 13, title: '气候行动', subtitle: 'Climate Action', color: '#3f7e44', description: '采取紧急行动应对气候变化及其影响。加强各国应对气候变化影响的能力。' },
  { id: 14, title: '水下生物', subtitle: 'Life Below Water', color: '#009444', description: '保护和可持续利用海洋和海洋资源以促进可持续发展。制止过度捕捞、非法、未报告和无管制的捕捞活动。' },
  { id: 15, title: '陆地生物', subtitle: 'Life on Land', color: '#00a651', description: '保护、恢复和促进可持续利用陆地生态系统，可持续管理森林，防治荒漠化，制止和扭转土地退化，遏制生物多样性的丧失。' },
  { id: 16, title: '和平、正义与强大机构', subtitle: 'Peace, Justice and Strong Institutions', color: '#19489d', description: '促进有利于可持续发展的和平和包容社会，为所有人提供诉诸司法的机会，在各级建立有效、负责和包容的机构。' },
  { id: 17, title: '促进目标实现的伙伴关系', subtitle: 'Partnerships for the Goals', color: '#192841', description: '加强执行手段，重振可持续发展全球伙伴关系。加强多利益攸关方伙伴关系，调动和分享知识、专长、技术和财政资源，以实现可持续发展目标。' }
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
        <p class="sdgs-eyebrow">联合国 &middot; 2015&ndash;2030</p>
        <h1>17项可持续发展目标</h1>
        <p>相互关联的全球目标，旨在到2030年解决我们共同面临的最紧迫挑战</p>
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
        <h2>关于可持续发展目标</h2>
        <p>联合国可持续发展目标（SDGs）是2015年由联合国193个成员国共同通过的17项全球目标，旨在应对全球面临的最紧迫挑战。</p>
        <p>这些目标是相互关联的——解决一个问题往往有助于解决其他问题。改善教育可以帮助消除贫困，应对气候变化需要全球合作与创新。</p>
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
            <button class="modal-close" @click="closeModal" aria-label="关闭">
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
