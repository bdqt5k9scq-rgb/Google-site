<script setup lang="ts">
import { onMounted } from 'vue'
import gsap from 'gsap'
import { GSAP_EASE } from '@/lib/animations'

const objectives = [
  { title: 'Raise Public Awareness', desc: 'Increase public awareness and understanding of the Sustainable Development Goals' },
  { title: 'Educational Resources', desc: 'Provide educational resources and tools to empower individuals and organizations' },
  { title: 'Interdisciplinary Collaboration', desc: 'Foster interdisciplinary collaboration and knowledge sharing' },
  { title: 'Localized Action', desc: 'Promote localized sustainable development actions and practices' }
]

onMounted(() => {
  gsap.context(() => {
    gsap.fromTo('.about-header h1', { y: 48, opacity: 0 }, { y: 0, opacity: 1, duration: 0.9, ease: GSAP_EASE.out })
    gsap.fromTo('.about-header p', { y: 32, opacity: 0 }, { y: 0, opacity: 1, duration: 0.7, delay: 0.15, ease: GSAP_EASE.out })
    gsap.fromTo('.mission-card', { y: 56, opacity: 0 }, { y: 0, opacity: 1, duration: 0.7, ease: GSAP_EASE.out, scrollTrigger: { trigger: '.mission-card', start: 'top 85%' } })
    gsap.fromTo('.obj-card', { y: 48, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, stagger: 0.1, ease: GSAP_EASE.out, scrollTrigger: { trigger: '.objectives-grid', start: 'top 85%' } })
    gsap.fromTo('.about-cta', { y: 48, opacity: 0 }, { y: 0, opacity: 1, duration: 0.7, ease: GSAP_EASE.out, scrollTrigger: { trigger: '.about-cta', start: 'top 85%' } })
  })
})
</script>

<template>
  <div class="about">
    <!-- ====== Header ====== -->
    <section class="about-header">
      <div class="container">
        <p class="about-eyebrow">About Us</p>
        <h1>About Us</h1>
        <p>Professionals from diverse fields, united in advancing sustainable development</p>
      </div>
    </section>

    <!-- ====== Mission & Vision ====== -->
    <section class="about-content">
      <div class="container">
        <div class="mission-card">
          <div class="mission-grid">
            <div class="mission-block">
              <span class="block-label">Mission</span>
              <h2>Our Mission</h2>
              <p>We are dedicated to promoting the awareness and practice of the UN Sustainable Development Goals. Through education, advocacy, and action, we empower individuals and organizations to participate in the global process of sustainable development.</p>
            </div>
            <div class="mission-block">
              <span class="block-label">Vision</span>
              <h2>Our Vision</h2>
              <p>To build a sustainable future where everyone participates and develops together, making our planet a beautiful home where humanity and nature coexist in harmony.</p>
            </div>
          </div>
        </div>

        <!-- Objectives -->
        <div class="objectives-section">
          <h2 class="section-title">Our Objectives</h2>
          <div class="objectives-grid">
            <div v-for="(obj, i) in objectives" :key="i" class="obj-card">
              <span class="obj-num">{{ String(i + 1).padStart(2, '0') }}</span>
              <h3>{{ obj.title }}</h3>
              <p>{{ obj.desc }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ====== CTA ====== -->
    <section class="about-cta">
      <div class="container">
        <div class="cta-inner">
          <h2>Meet Our Team</h2>
          <p>Four team members from diverse academic backgrounds, each bringing their expertise to the Sustainable Development Goals</p>
          <router-link to="/team-sdgs" class="btn btn-primary">
            View Team SDG Assignments
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
  background: linear-gradient(165deg, #0d0d18 0%, #1a1a2e 40%, #0d0d18 100%);
  color: #fff;
  padding: 80px 0;
  text-align: center;
  position: relative;
  overflow: hidden;
}
.about-header::before {
  content: ''; position: absolute; inset: 0;
  background: radial-gradient(ellipse 400px 200px at 50% 30%, rgba(196,139,92,0.06) 0%, transparent 70%);
  pointer-events: none;
}
.about-eyebrow {
  font-size: 0.72rem; font-weight: 700; letter-spacing: 0.12em;
  text-transform: uppercase; color: #c48b5c; margin-bottom: 16px;
}
.about-header h1 {
  font-family: Georgia, serif;
  font-size: clamp(2.4rem, 4.5vw, 3.2rem);
  color: #fff; margin-bottom: 16px;
}
.about-header p { color: rgba(255,255,255,0.5); font-size: 1.1rem; }

/* ====== Content ====== */
.about-content { padding: 80px 0 0; background: #fdfaf6; }

.mission-card {
  background: #fff;
  border: 1px solid #f0ebe4;
  border-radius: 20px;
  padding: 0;
  overflow: hidden;
  box-shadow: 0 4px 16px rgba(28,28,36,0.04);
}
.mission-grid { display: grid; grid-template-columns: 1fr 1fr; }
.mission-block { padding: 48px 40px; }
.mission-block:first-child { border-right: 1px solid #f0ebe4; }
.block-label {
  display: inline-block;
  font-size: 0.7rem; font-weight: 700; letter-spacing: 0.08em;
  text-transform: uppercase; color: #c48b5c;
  background: rgba(196,139,92,0.08);
  padding: 4px 14px; border-radius: 100px; margin-bottom: 16px;
}
.mission-block h2 {
  font-family: Georgia, serif;
  font-size: 1.5rem; color: #1c1c24; margin-bottom: 16px;
}
.mission-block p {
  color: #6b6560; font-size: 1.05rem; line-height: 1.8;
}

/* ====== Objectives ====== */
.objectives-section { padding: 72px 0; }
.objectives-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-top: 36px;
}
.obj-card {
  background: #fff;
  border: 1px solid #f0ebe4;
  border-radius: 16px;
  padding: 36px 24px;
  text-align: center;
  position: relative;
  transition: all 0.35s cubic-bezier(0.16,1,0.3,1);
}
.obj-card:hover {
  box-shadow: 0 12px 32px rgba(28,28,36,0.08);
  border-color: transparent;
  transform: translateY(-4px);
}
.obj-num {
  font-family: Georgia, serif;
  font-size: 0.7rem; font-weight: 700; letter-spacing: 0.06em;
  color: #c48b5c; opacity: 0.6;
  display: block; margin-bottom: 8px;
}
.obj-card h3 {
  font-family: Georgia, serif;
  font-size: 1.1rem; color: #1c1c24; margin-bottom: 8px;
}
.obj-card p { color: #6b6560; font-size: 0.9rem; line-height: 1.6; }

/* ====== CTA ====== */
.about-cta {
  padding: 80px 0;
  background: linear-gradient(160deg, #1c1c24 0%, #252530 50%, #1c1c24 100%);
}
.cta-inner { text-align: center; }
.cta-inner h2 {
  font-family: Georgia, serif;
  font-size: 2rem; color: #fff; margin-bottom: 12px;
}
.cta-inner p {
  color: rgba(255,255,255,0.5); font-size: 1.08rem; margin-bottom: 32px;
}

@media (max-width: 768px) {
  .mission-grid { grid-template-columns: 1fr; }
  .mission-block:first-child { border-right: none; border-bottom: 1px solid #f0ebe4; }
  .objectives-grid { grid-template-columns: repeat(2, 1fr); }
  .mission-block { padding: 32px 24px; }
}
@media (max-width: 480px) {
  .objectives-grid { grid-template-columns: 1fr; }
}
</style>
