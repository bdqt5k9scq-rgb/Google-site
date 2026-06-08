<script setup lang="ts">
import { useRouter } from 'vue-router'
import { onMounted } from 'vue'
import gsap from 'gsap'
import { GSAP_EASE } from '@/lib/animations'

const router = useRouter()

const allSDGs = [
  { id: 1, title: '消除贫困', subtitle: 'No Poverty', color: '#e5243b' },
  { id: 2, title: '零饥饿', subtitle: 'Zero Hunger', color: '#dda63a' },
  { id: 3, title: '良好健康', subtitle: 'Good Health', color: '#4c9f38' },
  { id: 4, title: '优质教育', subtitle: 'Quality Education', color: '#c5192d' },
  { id: 5, title: '性别平等', subtitle: 'Gender Equality', color: '#ff3a21' },
  { id: 6, title: '清洁饮水', subtitle: 'Clean Water', color: '#26bde2' },
  { id: 7, title: '清洁能源', subtitle: 'Clean Energy', color: '#fcc30b' },
  { id: 8, title: '体面工作', subtitle: 'Decent Work', color: '#a21942' },
  { id: 9, title: '产业创新', subtitle: 'Industry & Innovation', color: '#fd6925' },
  { id: 10, title: '减少不平等', subtitle: 'Reduced Inequalities', color: '#dd1367' },
  { id: 11, title: '可持续城市', subtitle: 'Sustainable Cities', color: '#fd9d24' },
  { id: 12, title: '负责任消费', subtitle: 'Responsible Consumption', color: '#bf8b2e' },
  { id: 13, title: '气候行动', subtitle: 'Climate Action', color: '#3f7e44' },
  { id: 14, title: '水下生物', subtitle: 'Life Below Water', color: '#009444' },
  { id: 15, title: '陆地生物', subtitle: 'Life on Land', color: '#00a651' },
  { id: 16, title: '和平正义', subtitle: 'Peace & Justice', color: '#19489d' },
  { id: 17, title: '伙伴关系', subtitle: 'Partnerships', color: '#192841' }
]

const teamMembers = [
  { id: 1, name: 'Li Shuhang', background: '环境科学专业', careerGoal: '成为可持续发展领域专家', role: '项目负责人', studentId: '8168667', color: '#2c5f2d' },
  { id: 2, name: 'Feng Jingyi', background: '计算机科学专业', careerGoal: '开发环保科技解决方案', role: '技术开发', studentId: '8168308', color: '#1a3a5c' },
  { id: 3, name: 'Wang Luyang', background: '国际事务专业', careerGoal: '推动全球可持续发展合作', role: '政策研究', studentId: '8168505', color: '#5c2d6e' },
  { id: 4, name: 'Lu Jianning', background: '统计学专业', careerGoal: '数据分析与可持续发展评估', role: '数据分析师', studentId: '8168379', color: '#b8573e' }
]

const stats = [
  { number: '17', label: '可持续发展目标' },
  { number: '193', label: '成员国共同承诺' },
  { number: '2030', label: '目标实现年份' },
  { number: '169', label: '具体行动指标' }
]

const whySDGs = [
  { title: '前所未有的全球性挑战', text: '当今世界面临着前所未有的全球性挑战。气候变化导致极端天气事件频发，全球平均气温已比工业革命前上升约1.1°C。与此同时，全球仍有超过7亿人生活在极端贫困中。这些挑战不是单一国家能够独立解决的。' },
  { title: '统一的行动框架', text: '联合国可持续发展目标（SDGs）为全球社会提供了统一的行动框架。SDGs认识到经济发展、社会包容和环境保护是不可分割的整体，这种系统性思维确保解决一个问题时不会加剧另一个问题。' },
  { title: '不落下任何人', text: 'SDGs提供了明确的指标和时间表——169项具体目标和232项指标——让各国政府、企业、民间组织和个人能够协调行动，衡量进展。"不落下任何人"（Leave No One Behind）确保发展成果惠及最脆弱群体。' }
]

onMounted(() => {
  gsap.context(() => {
    // Hero animations
    gsap.fromTo('.hero h1', { y: 60, opacity: 0 }, { y: 0, opacity: 1, duration: 1, ease: GSAP_EASE.out })
    gsap.fromTo('.hero-subtitle', { y: 40, opacity: 0 }, { y: 0, opacity: 1, duration: 0.8, delay: 0.2, ease: GSAP_EASE.out })
    gsap.fromTo('.hero-buttons > *', { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, stagger: 0.12, delay: 0.4, ease: GSAP_EASE.out })
    gsap.fromTo('.hero-globe', { scale: 0.6, opacity: 0, rotate: -20 }, { scale: 1, opacity: 1, rotate: 0, duration: 1.4, delay: 0.15, ease: GSAP_EASE.inOut })

    // Stats
    gsap.fromTo('.stat-card', { y: 60, opacity: 0 }, { y: 0, opacity: 1, duration: 0.7, stagger: 0.1, ease: GSAP_EASE.out, scrollTrigger: { trigger: '.stats-section', start: 'top 85%' } })

    // Why SDGs
    gsap.fromTo('.why-card', { y: 56, opacity: 0 }, { y: 0, opacity: 1, duration: 0.65, stagger: 0.12, ease: GSAP_EASE.out, scrollTrigger: { trigger: '.why-section', start: 'top 85%' } })

    // SDG grid cards
    gsap.fromTo('.sdg-item', { y: 48, opacity: 0, scale: 0.95 }, { y: 0, opacity: 1, scale: 1, duration: 0.45, stagger: 0.03, ease: GSAP_EASE.out, scrollTrigger: { trigger: '.sdgs-full-grid', start: 'top 90%' } })

    // Team bios
    gsap.fromTo('.member-card', { y: 56, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, stagger: 0.1, ease: GSAP_EASE.out, scrollTrigger: { trigger: '.team-section', start: 'top 85%' } })

    // CTA sections
    gsap.fromTo('.cta-block', { y: 48, opacity: 0 }, { y: 0, opacity: 1, duration: 0.8, ease: GSAP_EASE.out, scrollTrigger: { trigger: '.cta-block', start: 'top 85%' } })

    // Card hover effects
    const hoverCards = gsap.utils.toArray<HTMLElement>('.sdg-item, .stat-card, .member-card, .why-card')
    hoverCards.forEach(card => {
      card.addEventListener('mouseenter', () => gsap.to(card, { y: -8, scale: 1.02, duration: 0.3, ease: 'power2.out' }))
      card.addEventListener('mouseleave', () => gsap.to(card, { y: 0, scale: 1, duration: 0.35, ease: 'power2.out' }))
    })
  })
})
</script>

<template>
  <div class="home">
    <!-- ====== HERO ====== -->
    <section class="hero">
      <div class="hero-bg-decor"></div>
      <div class="container hero-grid">
        <div class="hero-text">
          <p class="hero-eyebrow">United Nations &middot; 2015–2030</p>
          <h1>为我们共同的<br>未来而行动</h1>
          <p class="hero-subtitle">17项全球目标，应对人类最紧迫的挑战<br>为所有人创造更美好、更可持续的明天</p>
          <div class="hero-buttons">
            <button class="btn btn-primary" @click="router.push('/sdgs')">
              探索17项目标
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </button>
            <button class="btn btn-outline-light" @click="router.push('/act-now')">立即行动</button>
          </div>
        </div>
        <div class="hero-visual">
          <svg viewBox="0 0 340 340" class="hero-globe">
            <defs>
              <radialGradient id="globeGrad" cx="35%" cy="35%"><stop offset="0%" stop-color="#fdfaf6"/><stop offset="100%" stop-color="#d4c5b0"/></radialGradient>
              <filter id="globeShadow"><feDropShadow dx="0" dy="12" stdDeviation="20" flood-color="#0d0d14" flood-opacity="0.3"/></filter>
            </defs>
            <!-- orbit rings -->
            <circle cx="170" cy="170" r="155" fill="none" stroke="#c48b5c" stroke-width="1" opacity="0.15" stroke-dasharray="6 5"/>
            <circle cx="170" cy="170" r="140" fill="none" stroke="#c48b5c" stroke-width="0.6" opacity="0.08"/>
            <!-- globe -->
            <circle cx="170" cy="170" r="105" fill="url(#globeGrad)" stroke="#c48b5c" stroke-width="2.5" filter="url(#globeShadow)"/>
            <!-- latitude -->
            <ellipse cx="170" cy="170" rx="105" ry="38" fill="none" stroke="#c48b5c" stroke-width="0.7" opacity="0.2"/>
            <ellipse cx="170" cy="170" rx="105" ry="65" fill="none" stroke="#c48b5c" stroke-width="0.7" opacity="0.15"/>
            <line x1="65" y1="170" x2="275" y2="170" stroke="#c48b5c" stroke-width="0.7" opacity="0.2"/>
            <!-- longitude -->
            <ellipse cx="170" cy="170" rx="52" ry="105" fill="none" stroke="#c48b5c" stroke-width="0.7" opacity="0.15"/>
            <ellipse cx="170" cy="170" rx="85" ry="105" fill="none" stroke="#c48b5c" stroke-width="0.7" opacity="0.1"/>
            <!-- SDG badge -->
            <circle cx="170" cy="170" r="30" fill="#c48b5c" opacity="0.92"/>
            <text x="170" y="178" text-anchor="middle" fill="#fff" font-family="Georgia,serif" font-size="20" font-weight="700">SDG</text>
            <!-- orbit dots -->
            <circle cx="170" cy="38" r="3.5" fill="#d4a574" opacity="0.7"/>
            <circle cx="283" cy="200" r="3" fill="#c48b5c" opacity="0.5"/>
            <circle cx="65" cy="130" r="2.5" fill="#8b7355" opacity="0.5"/>
          </svg>
        </div>
      </div>
      <div class="hero-wave">
        <svg viewBox="0 0 1440 80" preserveAspectRatio="none"><path d="M0 80V25C240 55 480 8 720 16 960 24 1200 50 1440 24v56z" fill="#fdfaf6"/></svg>
      </div>
    </section>

    <!-- ====== STATS ====== -->
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

    <!-- ====== WHY SDGs ====== -->
    <section class="why-section">
      <div class="container">
        <h2 class="section-title">为什么世界需要 SDGs？</h2>
        <p class="section-subtitle">面对前所未有的挑战，我们需要共同的行动框架</p>
        <div class="why-grid">
          <div v-for="(item, i) in whySDGs" :key="i" class="why-card">
            <div class="why-num">{{ String(i + 1).padStart(2, '0') }}</div>
            <h3>{{ item.title }}</h3>
            <p>{{ item.text }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ====== ALL 17 SDGs ====== -->
    <section class="sdgs-section">
      <div class="container">
        <h2 class="section-title">17项可持续发展目标</h2>
        <p class="section-subtitle">每一项挑战都需要全球协作与行动</p>
        <div class="sdgs-full-grid">
          <div
            v-for="sdg in allSDGs"
            :key="sdg.id"
            class="sdg-item"
            :style="{ '--c': sdg.color, '--c-light': sdg.color + '12' }"
            @click="router.push('/sdgs')"
          >
            <span class="sdg-num">{{ String(sdg.id).padStart(2, '0') }}</span>
            <h3>{{ sdg.title }}</h3>
            <p class="sdg-en">{{ sdg.subtitle }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ====== TEAM ====== -->
    <section class="team-section">
      <div class="container">
        <h2 class="section-title">团队成员</h2>
        <p class="section-subtitle">多元化的专业背景，共同的目标与使命</p>
        <div class="team-grid">
          <div v-for="m in teamMembers" :key="m.id" class="member-card" :style="{ '--mc': m.color }">
            <div class="member-avatar">
              <span>{{ m.name.charAt(0) }}</span>
            </div>
            <h3 class="member-name">{{ m.name }}</h3>
            <span class="member-role">{{ m.role }}</span>
            <span class="member-bg">{{ m.background }}</span>
            <span class="member-id">学号: {{ m.studentId }}</span>
          </div>
        </div>
        <div class="text-center mt-xl">
          <button class="btn btn-primary" @click="router.push('/team-sdgs')">
            查看团队SDG分工
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </button>
        </div>
      </div>
    </section>

    <!-- ====== CTA DUAL ====== -->
    <section class="cta-dual">
      <div class="container">
        <div class="cta-grid">
          <div class="cta-block cta-about">
            <p class="cta-eyebrow">我们的使命</p>
            <h2>关于可持续发展目标</h2>
            <p>了解17项相互关联的全球目标如何改变世界</p>
            <button class="btn btn-secondary" @click="router.push('/about')">了解更多</button>
          </div>
          <div class="cta-block cta-carbon">
            <p class="cta-eyebrow">从自己做起</p>
            <h2>计算您的碳足迹</h2>
            <p>了解日常活动对环境的影响，获取减排建议</p>
            <button class="btn btn-primary" @click="router.push('/carbon-footprint')">
              开始计算
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </button>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* ====== HERO ====== */
.hero {
  background: linear-gradient(165deg, #0d0d18 0%, #1a1a2e 30%, #16213e 60%, #0d0d18 100%);
  color: #fff;
  padding: 100px 0 120px;
  position: relative;
  overflow: hidden;
}
.hero-bg-decor {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(ellipse 600px 400px at 75% 30%, rgba(196,139,92,0.08) 0%, transparent 70%),
    radial-gradient(ellipse 400px 300px at 20% 70%, rgba(37,99,235,0.05) 0%, transparent 70%);
  pointer-events: none;
}
.hero-grid {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 80px;
  align-items: center;
  position: relative;
  z-index: 1;
}
.hero-eyebrow {
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #c48b5c;
  margin-bottom: 20px;
}
.hero-text h1 {
  font-family: Georgia, serif;
  font-size: clamp(2.6rem, 5vw, 3.8rem);
  font-weight: 700;
  color: #fff;
  line-height: 1.1;
  margin-bottom: 24px;
  letter-spacing: -0.02em;
}
.hero-subtitle {
  font-size: 1.1rem;
  color: rgba(255,255,255,0.5);
  line-height: 1.7;
  margin-bottom: 40px;
}
.hero-buttons { display: flex; gap: 14px; flex-wrap: wrap; }
.btn-outline-light {
  color: rgba(255,255,255,0.8);
  border: 1.5px solid rgba(255,255,255,0.2);
  background: transparent;
  padding: 10px 24px;
  border-radius: 100px;
  font-size: 0.92rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}
.btn-outline-light:hover {
  border-color: #c48b5c;
  color: #c48b5c;
  background: rgba(196,139,92,0.08);
}
.hero-visual { display: flex; justify-content: center; }
.hero-globe { width: 300px; height: 300px; }
.hero-wave {
  position: absolute; bottom: 0; left: 0; width: 100%; height: 80px;
  overflow: hidden; line-height: 0;
}
.hero-wave svg { width: 100%; height: 80px; }

/* ====== STATS ====== */
.stats-section {
  background: #fdfaf6;
  padding: 64px 0;
  border-bottom: 1px solid #f0ebe4;
}
.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0;
}
.stat-card {
  text-align: center;
  padding: 32px 20px;
  position: relative;
  cursor: default;
}
.stat-card:not(:last-child)::after {
  content: ''; position: absolute; right: 0; top: 15%; height: 70%;
  width: 1px; background: #e8dfd5;
}
.stat-number {
  font-family: Georgia, serif;
  font-size: 3.2rem;
  font-weight: 700;
  color: #c48b5c;
  line-height: 1;
  margin-bottom: 8px;
}
.stat-label { color: #6b6560; font-size: 0.92rem; font-weight: 500; }

/* ====== WHY SDGs ====== */
.why-section {
  padding: 90px 0;
  background: #fefcf9;
  position: relative;
}
.why-section::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, #e8dfd5, transparent);
}
.why-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin-top: 40px;
}
.why-card {
  background: #fff;
  border: 1px solid #f0ebe4;
  border-radius: 16px;
  padding: 36px 28px;
  position: relative;
  overflow: hidden;
  transition: all 0.35s cubic-bezier(0.16,1,0.3,1);
}
.why-card::before {
  content: ''; position: absolute; top: 0; left: 0; width: 4px; height: 40%;
  background: #c48b5c; border-radius: 0 0 3px 0;
}
.why-card:hover {
  box-shadow: 0 16px 40px rgba(28,28,36,0.1);
  border-color: transparent;
}
.why-num {
  font-family: Georgia, serif;
  font-size: 2.5rem;
  font-weight: 700;
  color: #c48b5c;
  opacity: 0.12;
  position: absolute;
  top: 12px;
  right: 20px;
}
.why-card h3 {
  font-family: Georgia, serif;
  font-size: 1.2rem;
  color: #1c1c24;
  margin-bottom: 12px;
}
.why-card p {
  color: #6b6560;
  font-size: 0.94rem;
  line-height: 1.75;
}

/* ====== ALL 17 SDGs ====== */
.sdgs-section {
  padding: 90px 0;
  background: #fdfaf6;
  position: relative;
}
.sdgs-section::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, #e8dfd5, transparent);
}
.sdgs-full-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: 10px;
  margin-top: 36px;
}
.sdg-item {
  background: #fff;
  border: 1px solid #f0ebe4;
  border-radius: 14px;
  padding: 24px 16px;
  text-align: center;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: all 0.3s cubic-bezier(0.16,1,0.3,1);
}
.sdg-item::after {
  content: ''; position: absolute; bottom: 0; left: 0; right: 0; height: 3px;
  background: var(--c); transform: scaleX(0); transform-origin: left;
  transition: transform 0.35s cubic-bezier(0.16,1,0.3,1);
}
.sdg-item:hover {
  box-shadow: 0 12px 28px rgba(28,28,36,0.08);
  border-color: transparent;
  background: var(--c-light);
}
.sdg-item:hover::after { transform: scaleX(1); }
.sdg-num {
  font-family: Georgia, serif;
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  color: var(--c);
  opacity: 0.7;
  display: block;
  margin-bottom: 4px;
}
.sdg-item h3 {
  font-family: Georgia, serif;
  font-size: 0.95rem;
  color: #1c1c24;
  margin-bottom: 2px;
}
.sdg-en { font-size: 0.7rem; color: #8c8782; font-style: italic; }

/* ====== TEAM ====== */
.team-section {
  padding: 90px 0;
  background: #fefcf9;
  position: relative;
}
.team-section::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, #e8dfd5, transparent);
}
.team-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  margin-top: 36px;
}
.member-card {
  background: #fff;
  border: 1px solid #f0ebe4;
  border-radius: 16px;
  padding: 36px 24px;
  text-align: center;
  cursor: pointer;
  transition: all 0.35s cubic-bezier(0.16,1,0.3,1);
  position: relative;
  overflow: hidden;
}
.member-card::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px;
  background: var(--mc);
}
.member-card:hover {
  box-shadow: 0 16px 40px rgba(28,28,36,0.1);
  border-color: transparent;
}
.member-avatar {
  width: 68px; height: 68px;
  border-radius: 50%;
  background: var(--mc);
  display: flex; align-items: center; justify-content: center;
  margin: 0 auto 16px;
  font-size: 1.8rem; color: #fff;
  font-family: Georgia, serif;
}
.member-name {
  font-family: Georgia, serif;
  font-size: 1.15rem;
  color: #1c1c24;
  margin-bottom: 6px;
}
.member-role {
  display: block;
  font-size: 0.7rem; font-weight: 700; letter-spacing: 0.06em;
  text-transform: uppercase; color: #c48b5c;
  background: rgba(196,139,92,0.08);
  padding: 3px 12px; border-radius: 100px;
  margin-bottom: 6px;
}
.member-bg {
  display: block;
  font-size: 0.8rem; color: #6b6560;
  margin-bottom: 4px;
}
.member-id {
  font-size: 0.7rem; color: #8c8782; font-family: monospace;
}

/* ====== CTA DUAL ====== */
.cta-dual { padding: 80px 0; background: #fdfaf6; }
.cta-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
.cta-block {
  padding: 56px 40px; border-radius: 20px; text-align: center;
  transition: transform 0.35s ease;
}
.cta-block:hover { transform: translateY(-4px); }
.cta-about {
  background: linear-gradient(150deg, #fdfaf6 0%, #f3ede7 50%, #fdfaf6 100%);
  border: 1px solid #e8dfd5;
}
.cta-carbon {
  background: linear-gradient(150deg, #1c1c24 0%, #252530 50%, #1c1c24 100%);
  color: #fff;
}
.cta-eyebrow {
  font-size: 0.72rem; font-weight: 700; letter-spacing: 0.1em;
  text-transform: uppercase; color: #c48b5c; margin-bottom: 12px;
}
.cta-block h2 {
  font-family: Georgia, serif;
  font-size: 1.8rem; margin-bottom: 16px;
}
.cta-about h2 { color: #1c1c24; }
.cta-carbon h2 { color: #fff; }
.cta-block > p {
  font-size: 1rem; line-height: 1.7; margin-bottom: 28px;
}
.cta-about > p { color: #6b6560; }
.cta-carbon > p { color: rgba(255,255,255,0.5); }
.cta-about .btn-secondary {
  border-color: #c48b5c; color: #c48b5c;
  background: transparent; padding: 10px 28px;
  border-radius: 100px; font-size: 0.92rem; font-weight: 600;
  cursor: pointer; transition: all 0.3s ease;
}
.cta-about .btn-secondary:hover {
  background: #c48b5c; color: #fff;
}

/* ====== RESPONSIVE ====== */
@media (max-width: 768px) {
  .hero-grid { grid-template-columns: 1fr; text-align: center; gap: 48px; }
  .hero-buttons { justify-content: center; }
  .hero-globe { width: 220px; height: 220px; }
  .stats-grid { grid-template-columns: repeat(2, 1fr); }
  .stat-card:nth-child(2)::after { display: none; }
  .why-grid { grid-template-columns: 1fr; }
  .sdgs-full-grid { grid-template-columns: repeat(auto-fill, minmax(120px, 1fr)); }
  .team-grid { grid-template-columns: repeat(2, 1fr); }
  .cta-grid { grid-template-columns: 1fr; }
}
@media (max-width: 480px) {
  .team-grid { grid-template-columns: 1fr; }
  .sdgs-full-grid { grid-template-columns: repeat(3, 1fr); gap: 6px; }
  .sdg-item { padding: 16px 10px; }
  .sdg-icon { font-size: 1.2rem; }
  .sdg-item h3 { font-size: 0.78rem; }
}
</style>
