<script setup lang="ts">
import { useRouter } from 'vue-router'
import { onMounted } from 'vue'
import gsap from 'gsap'
import { GSAP_EASE } from '@/lib/animations'

const router = useRouter()

const sdgHighlights = [
  { id: 1, title: '消除贫困', description: '在世界各地消除一切形式的贫困', color: '#e5243b' },
  { id: 2, title: '零饥饿', description: '消除饥饿，实现粮食安全', color: '#dda63a' },
  { id: 3, title: '良好健康与福祉', description: '确保健康的生活方式', color: '#4c9f38' },
  { id: 4, title: '优质教育', description: '确保包容和公平的优质教育', color: '#c5192d' },
  { id: 5, title: '性别平等', description: '实现性别平等', color: '#ff3a21' },
  { id: 6, title: '清洁饮水', description: '确保清洁饮水和卫生设施', color: '#26bde2' }
]

const teamMembers = [
  { id: 1, name: 'Li Shuhang', background: '环境科学专业', careerGoal: '成为可持续发展领域专家', role: '项目负责人', studentId: '8168667' },
  { id: 2, name: 'Feng Jingyi', background: '计算机科学专业', careerGoal: '开发环保科技解决方案', role: '技术开发', studentId: '8168308' },
  { id: 3, name: 'Wang Luyang', background: '国际事务专业', careerGoal: '推动全球可持续发展合作', role: '政策研究', studentId: '8168505' },
  { id: 4, name: 'Lu Jianning', background: '统计学专业', careerGoal: '数据分析与可持续发展评估', role: '数据分析师', studentId: '8168379' }
]

const stats = [
  { number: '17', label: '可持续发展目标' },
  { number: '193', label: '成员国共同承诺' },
  { number: '2030', label: '目标实现年份' },
  { number: '169', label: '具体行动指标' }
]

const whySDGs = [
  {
    title: '前所未有的全球性挑战',
    text: '当今世界面临着前所未有的全球性挑战。气候变化导致极端天气事件频发，全球平均气温已比工业革命前上升约1.1°C，若不采取行动，到2100年可能上升2.7°C以上（IPCC, 2023）。与此同时，全球仍有超过7亿人生活在极端贫困中，每天生活费不足2.15美元（联合国, 2023）。这些挑战不是单一国家能够独立解决的——因为它们超越了国界，影响着地球上的每一个生命。'
  },
  {
    title: '统一的行动框架',
    text: '联合国可持续发展目标（SDGs）为全球社会提供了统一的行动框架。与以往的倡议不同，SDGs认识到经济发展、社会包容和环境保护是不可分割的整体——正如SDG 1（消除贫困）与SDG 4（优质教育）和SDG 8（体面工作）相互关联，气候行动（SDG 13）与清洁能源（SDG 7）和可持续城市（SDG 11）密不可分（Sachs et al., 2023）。这种系统性思维确保解决一个问题时不会加剧另一个问题。'
  },
  {
    title: '缺乏指引的代价',
    text: '没有SDGs的指引，全球发展将面临方向不一、资源分散、重复努力的风险。可持续发展目标提供了明确的指标和时间表——169项具体目标和232项指标——让各国政府、企业、民间组织和个人能够协调行动，衡量进展（联合国, 2015）。更重要的是，SDGs不落下任何人（Leave No One Behind）的核心承诺确保了发展的成果能够惠及最脆弱的群体。'
  }
]

onMounted(() => {
  gsap.context(() => {
    const hero = document.querySelector('.hero')
    if (hero) {
      gsap.fromTo(hero.querySelector('h1'),
        { y: 48, opacity: 0 },
        { y: 0, opacity: 1, duration: 0.9, ease: GSAP_EASE.out }
      )
      gsap.fromTo(hero.querySelector('.hero-subtitle'),
        { y: 32, opacity: 0 },
        { y: 0, opacity: 1, duration: 0.7, delay: 0.15, ease: GSAP_EASE.out }
      )
      gsap.fromTo(hero.querySelectorAll('.hero-buttons > *'),
        { y: 24, opacity: 0 },
        { y: 0, opacity: 1, duration: 0.5, stagger: 0.1, delay: 0.35, ease: GSAP_EASE.out }
      )
      gsap.fromTo('.hero-globe',
        { scale: 0.75, opacity: 0, rotate: -15 },
        { scale: 1, opacity: 1, rotate: 0, duration: 1.2, delay: 0.2, ease: GSAP_EASE.inOut }
      )
    }

    // Stats — staggered count-up feel
    gsap.fromTo('.stat-card',
      { y: 60, opacity: 0 },
      {
        y: 0, opacity: 1, duration: 0.7, stagger: 0.12, ease: GSAP_EASE.out,
        scrollTrigger: { trigger: '.stats-section', start: 'top 85%' },
      }
    )

    // Why SDGs cards
    gsap.fromTo('.why-sdgs-card',
      { y: 48, opacity: 0 },
      {
        y: 0, opacity: 1, duration: 0.6, stagger: 0.12, ease: GSAP_EASE.out,
        scrollTrigger: { trigger: '.why-sdgs-section', start: 'top 85%' },
      }
    )

    // SDG cards
    gsap.fromTo('.sdg-highlights .sdg-card',
      { y: 56, opacity: 0 },
      {
        y: 0, opacity: 1, duration: 0.55, stagger: 0.07, ease: GSAP_EASE.out,
        scrollTrigger: { trigger: '.sdg-highlights', start: 'top 85%' },
      }
    )

    // About preview
    gsap.fromTo('.about-preview .about-content',
      { y: 48, opacity: 0 },
      {
        y: 0, opacity: 1, duration: 0.8, ease: GSAP_EASE.out,
        scrollTrigger: { trigger: '.about-preview', start: 'top 85%' },
      }
    )

    // Team bios
    gsap.fromTo('.bio-card',
      { y: 56, opacity: 0 },
      {
        y: 0, opacity: 1, duration: 0.6, stagger: 0.1, ease: GSAP_EASE.out,
        scrollTrigger: { trigger: '.bios-grid', start: 'top 85%' },
      }
    )

    // Carbon preview
    gsap.fromTo('.carbon-preview .carbon-content',
      { y: 48, opacity: 0 },
      {
        y: 0, opacity: 1, duration: 0.8, ease: GSAP_EASE.out,
        scrollTrigger: { trigger: '.carbon-preview', start: 'top 85%' },
      }
    )

    // GSAP hover for cards
    const cards = gsap.utils.toArray<HTMLElement>('.sdg-card, .stat-card, .bio-card, .why-sdgs-card')
    cards.forEach((card) => {
      card.addEventListener('mouseenter', () => {
        gsap.to(card, { y: -6, duration: 0.3, ease: 'power2.out' })
      })
      card.addEventListener('mouseleave', () => {
        gsap.to(card, { y: 0, duration: 0.35, ease: 'power2.out' })
      })
    })

    // Hero buttons hover
    const heroBtns = gsap.utils.toArray<HTMLElement>('.hero-buttons .btn')
    heroBtns.forEach((btn) => {
      btn.addEventListener('mouseenter', () => {
        gsap.to(btn, { y: -2, scale: 1.03, duration: 0.25, ease: 'power2.out' })
      })
      btn.addEventListener('mouseleave', () => {
        gsap.to(btn, { y: 0, scale: 1, duration: 0.3, ease: 'power2.out' })
      })
    })
  })
})
</script>

<template>
  <div class="home">
    <!-- ====== Hero ====== -->
    <section class="hero">
      <div class="container">
        <div class="hero-content">
          <p class="hero-eyebrow">联合国可持续发展目标 &middot; 2015&ndash;2030</p>
          <h1>为我们共同的<br>未来而行动</h1>
          <p class="hero-subtitle">
            17项全球目标，旨在解决人类面临的最紧迫挑战<br>
            为所有人创造更美好、更可持续的明天
          </p>
          <div class="hero-buttons">
            <button class="btn btn-primary" @click="router.push('/sdgs')">
              了解17项目标
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </button>
            <button class="btn btn-secondary" @click="router.push('/act-now')">
              立即行动
            </button>
          </div>
        </div>
        <div class="hero-visual">
          <div class="hero-globe-wrapper">
            <svg viewBox="0 0 320 320" class="hero-globe">
              <defs>
                <linearGradient id="heroGlobeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#c48b5c"/>
                  <stop offset="40%" stop-color="#d4a574"/>
                  <stop offset="100%" stop-color="#8b7355"/>
                </linearGradient>
                <filter id="globeShadow">
                  <feDropShadow dx="0" dy="8" stdDeviation="16" flood-color="#1c1c24" flood-opacity="0.12"/>
                </filter>
              </defs>
              <!-- Organic decorative ring -->
              <circle cx="160" cy="160" r="145" fill="none" stroke="url(#heroGlobeGrad)" stroke-width="1.5" opacity="0.2" stroke-dasharray="8 4"/>
              <circle cx="160" cy="160" r="130" fill="none" stroke="url(#heroGlobeGrad)" stroke-width="1" opacity="0.15"/>
              <!-- Main globe -->
              <circle cx="160" cy="160" r="100" fill="#fdfaf6" stroke="#c48b5c" stroke-width="2.5" filter="url(#globeShadow)"/>
              <!-- Latitude lines -->
              <ellipse cx="160" cy="160" rx="100" ry="35" fill="none" stroke="#c48b5c" stroke-width="0.8" opacity="0.25"/>
              <ellipse cx="160" cy="160" rx="100" ry="60" fill="none" stroke="#c48b5c" stroke-width="0.8" opacity="0.2"/>
              <line x1="60" y1="160" x2="260" y2="160" stroke="#c48b5c" stroke-width="0.8" opacity="0.25"/>
              <!-- Longitude arcs -->
              <ellipse cx="160" cy="160" rx="50" ry="100" fill="none" stroke="#c48b5c" stroke-width="0.8" opacity="0.2"/>
              <ellipse cx="160" cy="160" rx="80" ry="100" fill="none" stroke="#c48b5c" stroke-width="0.8" opacity="0.15"/>
              <!-- Center mark -->
              <circle cx="160" cy="160" r="28" fill="var(--color-terracotta, #c48b5c)" opacity="0.9"/>
              <text x="160" y="168" text-anchor="middle" fill="#fff" font-family="Georgia, serif" font-size="22" font-weight="700">SDG</text>
              <!-- Orbiting dots -->
              <circle cx="160" cy="48" r="3" fill="#c48b5c" opacity="0.6"/>
              <circle cx="260" cy="200" r="2.5" fill="#8b7355" opacity="0.5"/>
              <circle cx="70" cy="120" r="2" fill="#d4a574" opacity="0.5"/>
            </svg>
          </div>
        </div>
      </div>
      <!-- Decorative bottom wave -->
      <div class="hero-wave">
        <svg viewBox="0 0 1440 60" preserveAspectRatio="none">
          <path d="M0 60V20C240 50 480 5 720 12 960 19 1200 45 1440 20v40z" fill="#fdfaf6"/>
        </svg>
      </div>
    </section>

    <!-- ====== Stats ====== -->
    <section class="stats-section">
      <div class="container">
        <div class="stats-grid">
          <div v-for="stat in stats" :key="stat.label" class="stat-card">
            <div class="stat-number">{{ stat.number }}</div>
            <div class="stat-rule"></div>
            <div class="stat-label">{{ stat.label }}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- ====== Why SDGs ====== -->
    <section class="why-sdgs-section">
      <div class="container container-narrow">
        <h2 class="section-title">世界为何需要联合国可持续发展目标的指引</h2>
        <div class="why-sdgs-content">
          <div
            v-for="(item, index) in whySDGs"
            :key="index"
            class="why-sdgs-card"
          >
            <span class="why-sdgs-num">{{ String(index + 1).padStart(2, '0') }}</span>
            <h3>{{ item.title }}</h3>
            <p>{{ item.text }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ====== SDG Highlights ====== -->
    <section class="sdg-highlights">
      <div class="container">
        <h2 class="section-title">可持续发展目标</h2>
        <p class="section-subtitle">每一项挑战都需要全球协作与行动</p>
        <div class="sdg-grid">
          <div
            v-for="sdg in sdgHighlights"
            :key="sdg.id"
            class="sdg-card"
            :style="{ '--sdg-color': sdg.color, '--sdg-color-light': sdg.color + '18' }"
          >
            <div class="sdg-card-number">{{ String(sdg.id).padStart(2, '0') }}</div>
            <h3>{{ sdg.title }}</h3>
            <p>{{ sdg.description }}</p>
            <div class="sdg-card-accent"></div>
          </div>
        </div>
        <div class="text-center mt-xl">
          <button class="btn btn-primary" @click="router.push('/sdgs')">
            查看全部17项目标
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </button>
        </div>
      </div>
    </section>

    <!-- ====== Team Bios ====== -->
    <section class="team-bios">
      <div class="container">
        <h2 class="section-title">团队成员</h2>
        <p class="section-subtitle">多元化的专业背景，共同的目标与使命</p>
        <div class="bios-grid">
          <div v-for="member in teamMembers" :key="member.id" class="bio-card">
            <div class="bio-avatar">
              <div class="bio-avatar-inner">{{ member.name.charAt(0) }}</div>
            </div>
            <div class="bio-info">
              <h3 class="bio-name">{{ member.name }}</h3>
              <span class="bio-role">{{ member.role }}</span>
              <span class="bio-bg">{{ member.background }}</span>
              <span class="bio-id">学号: {{ member.studentId }}</span>
            </div>
            <p class="bio-goal">{{ member.careerGoal }}</p>
          </div>
        </div>
        <div class="text-center mt-xl">
          <button class="btn btn-primary" @click="router.push('/team-sdgs')">
            查看团队SDG目标分工
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </button>
        </div>
      </div>
    </section>

    <!-- ====== About Preview ====== -->
    <section class="about-preview">
      <div class="container container-narrow">
        <div class="about-content">
          <p class="about-eyebrow">我们的使命</p>
          <h2>关于可持续发展目标</h2>
          <p>联合国可持续发展目标（SDGs）是17项相互关联的全球目标，于2015年由联合国成员国通过，旨在到2030年解决全球面临的最紧迫挑战。这些目标涵盖消除贫困、保护地球、促进繁荣等多个领域。</p>
          <button class="btn btn-secondary" @click="router.push('/about')">了解更多</button>
        </div>
      </div>
    </section>

    <!-- ====== Carbon Preview ====== -->
    <section class="carbon-preview">
      <div class="container container-narrow">
        <div class="carbon-content">
          <p class="carbon-eyebrow">从自己做起</p>
          <h2>计算您的碳足迹</h2>
          <p>了解您的日常活动对环境的影响，获取个性化的减排建议。每一个数字背后，都是改变的可能。</p>
          <button class="btn btn-primary" @click="router.push('/carbon-footprint')">
            开始计算
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </button>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* ====== Hero ====== */
.hero {
  background: linear-gradient(165deg, #1c1c24 0%, #252530 40%, #1c1c24 100%);
  color: #fff;
  padding: 80px 0 100px;
  position: relative;
  overflow: hidden;
}

/* Subtle grain overlay */
.hero::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image:
    url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.03'/%3E%3C/svg%3E");
  pointer-events: none;
}

/* Organic blob behind globe */
.hero::after {
  content: '';
  position: absolute;
  top: -120px;
  right: -80px;
  width: 500px;
  height: 500px;
  background: radial-gradient(ellipse at center, rgba(196, 139, 92, 0.12) 0%, transparent 70%);
  border-radius: 60% 40% 55% 45% / 45% 55% 40% 60%;
  pointer-events: none;
}

.hero .container {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 60px;
  align-items: center;
  position: relative;
  z-index: 1;
}

.hero-eyebrow {
  font-family: var(--font-body, sans-serif);
  font-size: 0.8rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--color-terracotta, #c48b5c);
  margin-bottom: 16px;
}

.hero-content h1 {
  font-family: var(--font-display, Georgia, serif);
  font-size: clamp(2.4rem, 4.5vw, 3.4rem);
  font-weight: 700;
  color: #fff;
  line-height: 1.15;
  margin-bottom: 20px;
  letter-spacing: -0.02em;
}

.hero-subtitle {
  font-size: 1.08rem;
  color: rgba(255, 255, 255, 0.6);
  line-height: 1.7;
  margin-bottom: 36px;
}

.hero-buttons {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.hero-buttons .btn-secondary {
  color: rgba(255, 255, 255, 0.8);
  border-color: rgba(255, 255, 255, 0.2);
}

.hero-buttons .btn-secondary:hover {
  border-color: var(--color-terracotta, #c48b5c);
  color: var(--color-terracotta, #c48b5c);
  background-color: rgba(196, 139, 92, 0.08);
}

.hero-visual {
  display: flex;
  justify-content: center;
}

.hero-globe-wrapper {
  position: relative;
}

.hero-globe {
  width: 280px;
  height: 280px;
}

/* Bottom wave transition */
.hero-wave {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 60px;
  overflow: hidden;
  line-height: 0;
}

.hero-wave svg {
  width: 100%;
  height: 60px;
}

/* ====== Stats ====== */
.stats-section {
  background: var(--color-paper, #fdfaf6);
  padding: 56px 0;
  position: relative;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0;
}

.stat-card {
  text-align: center;
  padding: 28px 16px;
  position: relative;
  cursor: default;
}

.stat-card:not(:last-child)::after {
  content: '';
  position: absolute;
  right: 0;
  top: 20%;
  height: 60%;
  width: 1px;
  background: var(--color-sand, #e8dfd5);
}

.stat-number {
  font-family: var(--font-display, Georgia, serif);
  font-size: 3rem;
  font-weight: 700;
  color: var(--color-terracotta, #c48b5c);
  line-height: 1;
  margin-bottom: 8px;
}

.stat-rule {
  width: 24px;
  height: 2px;
  background: var(--color-sand, #e8dfd5);
  margin: 0 auto 10px;
}

.stat-label {
  color: var(--color-text-muted, #6b6560);
  font-size: 0.9rem;
  font-weight: 500;
}

/* ====== Why SDGs ====== */
.why-sdgs-section {
  padding: 80px 0;
  background: var(--color-cream, #fefcf9);
  position: relative;
}

.why-sdgs-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--color-sand, #e8dfd5), transparent);
}

.why-sdgs-content {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-top: 32px;
}

.why-sdgs-card {
  background: #fff;
  border: 1px solid var(--color-border-light, #f0ebe4);
  border-radius: var(--radius-lg, 12px);
  padding: 32px 24px;
  transition: all 0.35s var(--ease-out, cubic-bezier(0.16, 1, 0.3, 1));
}

.why-sdgs-card:hover {
  box-shadow: var(--shadow-lg, 0 12px 32px rgba(28, 28, 36, 0.08));
  border-color: transparent;
}

.why-sdgs-num {
  font-family: var(--font-display, Georgia, serif);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  color: var(--color-terracotta, #c48b5c);
  opacity: 0.6;
  display: block;
  margin-bottom: 12px;
}

.why-sdgs-card h3 {
  font-family: var(--font-display, Georgia, serif);
  font-size: 1.15rem;
  color: var(--color-ink, #1c1c24);
  margin-bottom: 12px;
}

.why-sdgs-card p {
  color: var(--color-text-muted, #6b6560);
  font-size: 0.92rem;
  line-height: 1.7;
}

@media (max-width: 768px) {
  .why-sdgs-content {
    grid-template-columns: 1fr;
  }
}

/* ====== SDG Highlights ====== */
.sdg-highlights {
  padding: 80px 0;
  background: var(--color-cream, #fefcf9);
  position: relative;
}

.sdg-highlights::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--color-sand, #e8dfd5), transparent);
}

.sdg-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

.sdg-card {
  background: #fff;
  border: 1px solid var(--color-border-light, #f0ebe4);
  border-radius: var(--radius-lg, 12px);
  padding: 28px 24px;
  position: relative;
  overflow: hidden;
  cursor: pointer;
  transition: all 0.35s var(--ease-out, cubic-bezier(0.16, 1, 0.3, 1));
}

.sdg-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--sdg-color, #c48b5c);
  transform: scaleX(0.3);
  transform-origin: left;
  transition: transform 0.35s var(--ease-out, cubic-bezier(0.16, 1, 0.3, 1));
}

.sdg-card:hover {
  box-shadow: var(--shadow-lg, 0 12px 32px rgba(28, 28, 36, 0.08));
  border-color: transparent;
}

.sdg-card:hover::before {
  transform: scaleX(1);
}

.sdg-card-number {
  font-family: var(--font-display, Georgia, serif);
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  color: var(--sdg-color, #c48b5c);
  opacity: 0.7;
  margin-bottom: 12px;
}

.sdg-card h3 {
  font-family: var(--font-display, Georgia, serif);
  font-size: 1.2rem;
  color: var(--color-ink, #1c1c24);
  margin-bottom: 8px;
}

.sdg-card p {
  color: var(--color-text-muted, #6b6560);
  font-size: 0.9rem;
  line-height: 1.6;
}

/* ====== Team Bios ====== */
.team-bios {
  padding: 80px 0;
  background: var(--color-paper, #fdfaf6);
  position: relative;
}

.team-bios::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--color-sand, #e8dfd5), transparent);
}

.bios-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
}

.bio-card {
  background: #fff;
  border: 1px solid var(--color-border-light, #f0ebe4);
  border-radius: var(--radius-lg, 12px);
  padding: 32px 24px;
  text-align: center;
  cursor: pointer;
  transition: all 0.35s var(--ease-out, cubic-bezier(0.16, 1, 0.3, 1));
}

.bio-card:hover {
  box-shadow: var(--shadow-lg, 0 12px 32px rgba(28, 28, 36, 0.08));
  border-color: transparent;
}

.bio-avatar {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 16px;
}

.bio-avatar-inner {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--color-terracotta, #c48b5c), #8b7355);
  color: #fff;
  font-family: var(--font-display, Georgia, serif);
  font-size: 1.6rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.bio-info {
  margin-bottom: 12px;
}

.bio-name {
  font-family: var(--font-display, Georgia, serif);
  font-size: 1.15rem;
  color: var(--color-ink, #1c1c24);
  margin-bottom: 8px;
}

.bio-role {
  display: block;
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--color-terracotta, #c48b5c);
  margin-bottom: 6px;
}

.bio-bg {
  display: inline-block;
  font-size: 0.78rem;
  font-weight: 500;
  color: var(--color-text-muted, #6b6560);
  background: rgba(28, 28, 36, 0.04);
  padding: 3px 12px;
  border-radius: 100px;
}

.bio-id {
  display: block;
  font-size: 0.72rem;
  font-weight: 500;
  color: var(--color-text-light, #8c8782);
  margin-top: 8px;
  font-family: monospace;
}

.bio-goal {
  color: var(--color-text-muted, #6b6560);
  font-size: 0.88rem;
  line-height: 1.5;
  font-style: italic;
}

/* ====== About Preview ====== */
.about-preview {
  padding: 80px 0;
  background: var(--bg-warm-gradient);
  background: linear-gradient(160deg, var(--color-paper, #fdfaf6) 0%, var(--color-sand-light, #f3ede7) 50%, var(--color-paper, #fdfaf6) 100%);
}

.about-content {
  text-align: center;
}

.about-eyebrow {
  font-family: var(--font-body, sans-serif);
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--color-terracotta, #c48b5c);
  margin-bottom: 12px;
}

.about-content h2 {
  font-family: var(--font-display, Georgia, serif);
  font-size: clamp(1.8rem, 3vw, 2.4rem);
  color: var(--color-ink, #1c1c24);
  margin-bottom: 20px;
}

.about-content p {
  color: var(--color-text-muted, #6b6560);
  font-size: 1.08rem;
  line-height: 1.75;
  margin-bottom: 32px;
}

/* ====== Carbon Preview ====== */
.carbon-preview {
  padding: 80px 0;
  background: linear-gradient(160deg, #1c1c24 0%, #252530 30%, #1c1c24 70%, #1a1a22 100%);
  position: relative;
  overflow: hidden;
}

.carbon-preview::before {
  content: '';
  position: absolute;
  top: -60px;
  left: -80px;
  width: 350px;
  height: 350px;
  background: radial-gradient(ellipse at center, rgba(196, 139, 92, 0.1) 0%, transparent 70%);
  border-radius: 55% 45% 60% 40% / 50% 55% 45% 50%;
  pointer-events: none;
}

.carbon-content {
  text-align: center;
  position: relative;
  z-index: 1;
}

.carbon-eyebrow {
  font-family: var(--font-body, sans-serif);
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--color-terracotta, #c48b5c);
  margin-bottom: 12px;
}

.carbon-content h2 {
  font-family: var(--font-display, Georgia, serif);
  font-size: clamp(1.8rem, 3vw, 2.4rem);
  color: #fff;
  margin-bottom: 20px;
}

.carbon-content p {
  color: rgba(255, 255, 255, 0.55);
  font-size: 1.08rem;
  line-height: 1.7;
  margin-bottom: 32px;
}

/* ====== Responsive ====== */
@media (max-width: 768px) {
  .hero .container {
    grid-template-columns: 1fr;
    text-align: center;
    gap: 40px;
  }

  .hero-buttons {
    justify-content: center;
  }

  .hero-globe {
    width: 200px;
    height: 200px;
  }

  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .stat-card:nth-child(2)::after {
    display: none;
  }

  .sdg-grid {
    grid-template-columns: 1fr;
    gap: 12px;
  }

  .bios-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
  }
}

@media (max-width: 480px) {
  .bios-grid {
    grid-template-columns: 1fr;
  }
}
</style>
