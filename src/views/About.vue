<script setup lang="ts">
import { onMounted } from 'vue'
import gsap from 'gsap'
import { GSAP_EASE } from '@/lib/animations'

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

    gsap.fromTo('.about-cta',
      { y: 48, opacity: 0 },
      { y: 0, opacity: 1, duration: 0.7, ease: GSAP_EASE.out,
        scrollTrigger: { trigger: '.about-cta', start: 'top 85%' } }
    )
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

    <!-- ====== CTA ====== -->
    <section class="about-cta">
      <div class="container container-narrow">
        <div class="cta-card">
          <h2>认识我们的团队</h2>
          <p>四位来自不同专业领域的成员，将各自的专长与可持续发展目标紧密结合，分工协作，共同推进可持续发展事业。</p>
          <router-link to="/team-sdgs" class="btn btn-primary">
            查看团队SDG目标分工
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </router-link>
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

/* ====== CTA ====== */
.about-cta {
  padding: 72px 0;
  background: var(--color-cream, #fefcf9);
  border-top: 1px solid var(--color-border-light, #f0ebe4);
}

.cta-card {
  text-align: center;
  background: #fff;
  border: 1px solid var(--color-border-light, #f0ebe4);
  border-radius: var(--radius-xl, 20px);
  padding: 48px 32px;
  box-shadow: var(--shadow-md, 0 4px 12px rgba(28, 28, 36, 0.06));
}

.cta-card h2 {
  font-family: var(--font-display, Georgia, serif);
  font-size: 1.8rem;
  color: var(--color-ink, #1c1c24);
  margin-bottom: 12px;
}

.cta-card p {
  color: var(--color-text-muted, #6b6560);
  font-size: 1.05rem;
  line-height: 1.7;
  margin-bottom: 28px;
  max-width: 500px;
  margin-left: auto;
  margin-right: auto;
}

@media (max-width: 768px) {
  .mission-section,
  .vision-section,
  .objectives-section {
    padding: 24px 20px;
  }
}
</style>
