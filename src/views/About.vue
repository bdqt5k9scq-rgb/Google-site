<script setup lang="ts">
import { onMounted } from 'vue'
import gsap from 'gsap'
import { GSAP_EASE } from '@/lib/animations'

const teamMembers = [
  { id: 1, name: '张明', background: '环境科学专业', careerGoal: '成为可持续发展领域专家', role: '项目负责人' },
  { id: 2, name: '李华', background: '计算机科学专业', careerGoal: '开发环保科技解决方案', role: '技术开发' },
  { id: 3, name: '王芳', background: '国际事务专业', careerGoal: '推动全球可持续发展合作', role: '政策研究' },
  { id: 4, name: '陈伟', background: '统计学专业', careerGoal: '数据分析与可持续发展评估', role: '数据分析师' }
]

const aboutInfo = {
  mission: '我们致力于促进联合国可持续发展目标的普及与实践，通过教育、宣传和行动，推动个人和组织参与到可持续发展的全球进程中。',
  vision: '构建一个人人参与、共同发展的可持续未来，让地球成为人类和自然和谐共处的美好家园。',
  objectives: [
    '提高公众对可持续发展目标的认识',
    '提供教育资源和工具支持',
    '促进跨学科合作与知识共享',
    '推动本地化的可持续发展行动'
  ]
}

onMounted(() => {
  gsap.context(() => {
    const header = document.querySelector('.about-header')
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

    gsap.fromTo('.mission-section',
      { y: 48, opacity: 0 },
      { y: 0, opacity: 1, duration: 0.7, ease: GSAP_EASE.out,
        scrollTrigger: { trigger: '.mission-section', start: 'top 85%' } }
    )
    gsap.fromTo('.vision-section',
      { y: 48, opacity: 0 },
      { y: 0, opacity: 1, duration: 0.7, ease: GSAP_EASE.out,
        scrollTrigger: { trigger: '.vision-section', start: 'top 85%' } }
    )

    gsap.fromTo('.objectives-section li',
      { x: -32, opacity: 0 },
      { x: 0, opacity: 1, duration: 0.5, stagger: 0.1, ease: GSAP_EASE.out,
        scrollTrigger: { trigger: '.objectives-section', start: 'top 85%' } }
    )

    gsap.fromTo('.team-card',
      { y: 56, opacity: 0 },
      {
        y: 0, opacity: 1, duration: 0.6, stagger: 0.1, ease: GSAP_EASE.out,
        scrollTrigger: { trigger: '.team-grid', start: 'top 85%' },
      }
    )

    const cards = gsap.utils.toArray<HTMLElement>('.team-card')
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
  <div class="about">
    <!-- ====== Header ====== -->
    <section class="about-header">
      <div class="container container-narrow">
        <p class="about-eyebrow">我们的团队</p>
        <h1>关于我们</h1>
        <p>来自不同领域的专业人才，共同推动可持续发展事业</p>
      </div>
    </section>

    <!-- ====== Content ====== -->
    <section class="about-content">
      <div class="container container-narrow">
        <div class="mission-section card">
          <span class="section-label">使命</span>
          <h2>我们的使命</h2>
          <p>{{ aboutInfo.mission }}</p>
        </div>

        <div class="vision-section card">
          <span class="section-label">愿景</span>
          <h2>我们的愿景</h2>
          <p>{{ aboutInfo.vision }}</p>
        </div>

        <div class="objectives-section card">
          <span class="section-label">目标</span>
          <h2>我们的目标</h2>
          <ul>
            <li v-for="(obj, index) in aboutInfo.objectives" :key="index">
              <span class="obj-num">{{ String(index + 1).padStart(2, '0') }}</span>
              {{ obj }}
            </li>
          </ul>
        </div>
      </div>
    </section>

    <!-- ====== Team ====== -->
    <section class="team-section">
      <div class="container">
        <h2 class="section-title">团队成员</h2>
        <p class="section-subtitle">多元化的专业背景，共同的目标与使命</p>
        <div class="team-grid">
          <div v-for="member in teamMembers" :key="member.id" class="team-card">
            <div class="member-avatar">
              <div class="avatar-initial">{{ member.name.charAt(0) }}</div>
            </div>
            <h3 class="member-name">{{ member.name }}</h3>
            <span class="member-role">{{ member.role }}</span>
            <p class="member-bg">{{ member.background }}</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* ====== Header ====== */
.about-header {
  background: linear-gradient(165deg, #1c1c24 0%, #252530 40%, #1c1c24 100%);
  color: #fff;
  padding: 72px 0;
  text-align: center;
  position: relative;
  overflow: hidden;
}

.about-header::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image:
    url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.025'/%3E%3C/svg%3E");
  pointer-events: none;
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

.about-header h1 {
  font-family: var(--font-display, Georgia, serif);
  font-size: clamp(2.2rem, 4vw, 3rem);
  color: #fff;
  margin-bottom: 16px;
}

.about-header p {
  color: rgba(255, 255, 255, 0.55);
  font-size: 1.08rem;
}

/* ====== Content Sections ====== */
.about-content {
  padding: 64px 0;
  background: var(--color-paper, #fdfaf6);
}

.mission-section,
.vision-section,
.objectives-section {
  margin-bottom: 24px;
  padding: 36px 32px;
}

.section-label {
  display: inline-block;
  font-family: var(--font-body, sans-serif);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--color-terracotta, #c48b5c);
  background: rgba(196, 139, 92, 0.08);
  padding: 4px 12px;
  border-radius: 100px;
  margin-bottom: 12px;
}

.mission-section h2,
.vision-section h2,
.objectives-section h2 {
  font-family: var(--font-display, Georgia, serif);
  font-size: 1.5rem;
  color: var(--color-ink, #1c1c24);
  margin-bottom: 16px;
}

.mission-section p,
.vision-section p {
  color: var(--color-text-muted, #6b6560);
  font-size: 1.05rem;
  line-height: 1.75;
}

.objectives-section ul {
  list-style: none;
  padding: 0;
}

.objectives-section li {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 14px 0;
  border-bottom: 1px solid var(--color-border-light, #f0ebe4);
  color: var(--color-text, #1c1c24);
  font-size: 1rem;
}

.objectives-section li:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

.obj-num {
  font-family: var(--font-display, Georgia, serif);
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--color-terracotta, #c48b5c);
  opacity: 0.6;
  min-width: 20px;
}

/* ====== Team ====== */
.team-section {
  padding: 72px 0;
  background: var(--color-cream, #fefcf9);
  border-top: 1px solid var(--color-border-light, #f0ebe4);
}

.team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}

.team-card {
  background: #fff;
  border: 1px solid var(--color-border-light, #f0ebe4);
  border-radius: var(--radius-lg, 12px);
  padding: 32px 24px;
  text-align: center;
  transition: all 0.35s var(--ease-out, cubic-bezier(0.16, 1, 0.3, 1));
}

.team-card:hover {
  box-shadow: var(--shadow-lg, 0 12px 32px rgba(28, 28, 36, 0.08));
  border-color: transparent;
}

.avatar-initial {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--color-terracotta, #c48b5c), var(--color-earth, #8b7355));
  color: #fff;
  font-family: var(--font-display, Georgia, serif);
  font-size: 1.6rem;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 16px;
}

.member-name {
  font-family: var(--font-display, Georgia, serif);
  font-size: 1.15rem;
  color: var(--color-ink, #1c1c24);
  margin-bottom: 4px;
}

.member-role {
  display: inline-block;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--color-terracotta, #c48b5c);
  background: rgba(196, 139, 92, 0.08);
  padding: 3px 12px;
  border-radius: 100px;
  margin-bottom: 12px;
}

.member-bg {
  color: var(--color-text-muted, #6b6560);
  font-size: 0.88rem;
  line-height: 1.5;
}

@media (max-width: 768px) {
  .team-grid {
    grid-template-columns: 1fr;
  }

  .mission-section,
  .vision-section,
  .objectives-section {
    padding: 24px 20px;
  }
}
</style>
