<script setup lang="ts">
import { onMounted } from 'vue'
import gsap from 'gsap'
import { GSAP_EASE } from '@/lib/animations'

const memberSDGs = [
  {
    member: { id: 1, name: 'Li Shuhang', background: 'Finance', photo: '/images/team/li-shuhang.jpg', portrait: '/images/team/li-shuhang-portrait.jpg', bg: '#2c5f2d', studentId: '8168667' },
    focus: 'Focusing on ecological and environmental fields, exploring scientific solutions for climate change and biodiversity conservation',
    sdgs: [
      { id: 13, title: 'Climate Action', subtitle: 'Climate Action', color: '#3f7e44', description: 'Climate change is the most severe global challenge of the 21st century. Li Shuhang is dedicated to analyzing carbon emission trends through environmental science research, proposing practical emission reduction solutions, and driving urgent action across all sectors of society to combat climate change and its impacts.' },
      { id: 15, title: 'Life on Land', subtitle: 'Life on Land', color: '#00a651', description: 'Biodiversity loss is occurring at an unprecedented rate. Li Shuhang focuses on forest ecosystem protection, desertification prevention, and land degradation restoration, advocating for sustainable land management and ecological restoration practices.' },
      { id: 6, title: 'Clean Water and Sanitation', subtitle: 'Clean Water and Sanitation', color: '#26bde2', description: 'Water security is a core issue in environmental sustainability. Li Shuhang researches water resource management and aquatic ecosystem protection, promoting universal access to clean water and sanitation, ensuring safe and affordable drinking water for all.' }
    ]
  },
  {
    member: { id: 2, name: 'Feng Jingyi', background: 'Accounting', photo: '/images/team/feng-jingyi.jpg', portrait: '/images/team/feng-jingyi-portrait.jpg', bg: '#1a3a5c', studentId: '8168308' },
    focus: 'Driving sustainable development through technological innovation, developing environmental tech solutions to address global challenges',
    sdgs: [
      { id: 9, title: 'Industry, Innovation and Infrastructure', subtitle: 'Industry, Innovation and Infrastructure', color: '#fd6925', description: 'Technological innovation is a key driver for achieving the Sustainable Development Goals. Feng Jingyi focuses on applying computer science and technology to build intelligent environmental platforms, promoting inclusive industrialization and sustainable infrastructure development.' },
      { id: 7, title: 'Affordable and Clean Energy', subtitle: 'Affordable and Clean Energy', color: '#fcc30b', description: 'The energy transition is the core pathway to addressing the climate crisis. Feng Jingyi develops energy monitoring and optimization systems, using intelligent algorithms to improve energy efficiency and promote the widespread adoption of renewable energy.' },
      { id: 12, title: 'Responsible Consumption and Production', subtitle: 'Responsible Consumption and Production', color: '#bf8b2e', description: 'Technology can transform consumption patterns. Feng Jingyi develops carbon footprint tracking and sustainable consumption guidance systems, helping businesses and individuals make more responsible resource use and production decisions.' }
    ]
  },
  {
    member: { id: 3, name: 'Wang Luyang', background: 'Accounting', photo: '/images/team/wang-luyang.jpg', portrait: '/images/team/wang-luyang-portrait.jpg', bg: '#5c2d6e', studentId: '8168505' },
    focus: 'Advancing global sustainable development cooperation, promoting equity, justice, and partnership building',
    sdgs: [
      { id: 16, title: 'Peace, Justice and Strong Institutions', subtitle: 'Peace, Justice and Strong Institutions', color: '#19489d', description: 'Peace and justice are the foundations of sustainable development. Wang Luyang researches international rule of law and governance mechanisms, promoting effective, accountable, and inclusive institutions that provide access to justice for all.' },
      { id: 17, title: 'Partnerships for the Goals', subtitle: 'Partnerships for the Goals', color: '#192841', description: 'Global partnerships are the prerequisite for achieving all SDGs. Wang Luyang is dedicated to strengthening multi-stakeholder cooperation and promoting the cross-border flow and sharing of knowledge, technology, and financial resources.' },
      { id: 5, title: 'Gender Equality', subtitle: 'Gender Equality', color: '#ff3a21', description: 'Gender equality is not only a fundamental human right but also a necessary condition for sustainable development. Wang Luyang advocates for ending all forms of discrimination against women and girls and promoting equal participation of women in decision-making processes.' },
      { id: 10, title: 'Reduced Inequalities', subtitle: 'Reduced Inequalities', color: '#dd1367', description: 'Global inequality is becoming increasingly severe. Wang Luyang researches inclusive policy design, promoting substantial improvements in income distribution, social protection, and equality of opportunity across countries.' }
    ]
  },
  {
    member: { id: 4, name: 'Lu Jianning', background: 'Finance', photo: '/images/team/lu-jianning.jpg', portrait: '/images/team/lu-jianning-portrait.jpg', bg: '#2c4a3e', studentId: '8168379' },
    focus: 'Driving sustainable development assessment with data, using quantitative analysis to reveal problems and verify outcomes',
    sdgs: [
      { id: 4, title: 'Quality Education', subtitle: 'Quality Education', color: '#c5192d', description: 'Education is the most powerful tool for breaking the cycle of poverty. Lu Jianning uses data analysis to assess the equity of educational resource distribution, providing data-driven decision support for policymakers and promoting inclusive and equitable quality education.' },
      { id: 3, title: 'Good Health and Well-being', subtitle: 'Good Health and Well-being', color: '#4c9f38', description: 'Data has irreplaceable value in the field of public health. Lu Jianning applies statistical models to analyze health trends, disease distribution, and healthcare resource allocation, providing quantitative evidence for universal health coverage.' },
      { id: 1, title: 'End Poverty', subtitle: 'No Poverty', color: '#e5243b', description: 'Poverty is a complex, multidimensional issue. Lu Jianning builds poverty assessment indicator systems and monitoring frameworks, tracking poverty reduction progress, identifying root causes of poverty, and supporting the formulation and implementation of targeted poverty alleviation policies.' },
      { id: 2, title: 'Zero Hunger', subtitle: 'Zero Hunger', color: '#dda63a', description: 'Food security is the fundamental guarantee of sustainable development. Lu Jianning analyzes agricultural production data, food supply chain efficiency, and nutritional status indicators, providing scientific assessment and methodological support for achieving the Zero Hunger goal.' }
    ]
  }
]

onMounted(() => {
  gsap.context(() => {
    gsap.fromTo('.ts-header h1', { y: 48, opacity: 0 }, { y: 0, opacity: 1, duration: 0.9, ease: GSAP_EASE.out })
    gsap.fromTo('.ts-header p', { y: 32, opacity: 0 }, { y: 0, opacity: 1, duration: 0.7, delay: 0.15, ease: GSAP_EASE.out })
    gsap.fromTo('.member-block', { y: 64, opacity: 0 }, { y: 0, opacity: 1, duration: 0.7, stagger: 0.15, ease: GSAP_EASE.out, scrollTrigger: { trigger: '.ts-content', start: 'top 88%' } })

    const cards = gsap.utils.toArray<HTMLElement>('.ts-sdg-card')
    cards.forEach(card => {
      card.addEventListener('mouseenter', () => gsap.to(card, { y: -4, scale: 1.02, duration: 0.3, ease: 'power2.out' }))
      card.addEventListener('mouseleave', () => gsap.to(card, { y: 0, scale: 1, duration: 0.35, ease: 'power2.out' }))
    })
  })
})
</script>

<template>
  <div class="team-sdgs">
    <!-- ====== Header ====== -->
    <section class="ts-header">
      <div class="container">
        <p class="ts-eyebrow">Team & SDGs</p>
        <h1>Everyone Has Their Own Mission</h1>
        <p>Four team members integrating their expertise with the Sustainable Development Goals</p>
      </div>
    </section>

    <!-- ====== Members ====== -->
    <section class="ts-content">
      <div class="container">
        <div v-for="m in memberSDGs" :key="m.member.id" class="member-block">
          <!-- Profile header -->
          <div class="mh">
            <div class="mh-avatar" :style="{ borderColor: m.member.bg }">
              <img :src="m.member.photo" :alt="m.member.name" class="mh-photo" />
            </div>
            <div class="mh-info">
              <h2>{{ m.member.name }}</h2>
              <div class="mh-tags">
                <span class="tag-bg">{{ m.member.background }}</span>
                <span class="tag-id">Student ID: {{ m.member.studentId }}</span>
              </div>
            </div>
          </div>
          <p class="mh-focus">"{{ m.focus }}"</p>

          <!-- TEST: direct image -->
          <div class="ts-test-photo" :style="{ borderColor: m.member.bg }" style="border: 3px solid; padding: 4px; margin-bottom: 12px; width: 200px;">
            <img :src="m.member.photo" style="width:100%; display:block;" />
            <p style="text-align:center; margin:4px 0;">TEST {{ m.member.name }}</p>
          </div>

          <!-- SDG cards + portrait photo -->
          <div class="ts-grid">
            <div v-for="sdg in m.sdgs" :key="sdg.id" class="ts-sdg-card" :style="{ '--c': sdg.color, '--cl': sdg.color + '10' }">
              <div class="ts-sdg-head">
                <span class="ts-sdg-num" :style="{ color: sdg.color }">{{ String(sdg.id).padStart(2, '0') }}</span>
                <div>
                  <h3>{{ sdg.title }}</h3>
                  <p class="ts-sdg-sub">{{ sdg.subtitle }}</p>
                </div>
              </div>
              <p class="ts-sdg-desc">{{ sdg.description }}</p>
            </div>
            <div v-if="(m.member.id === 1 || m.member.id === 2) && m.member.portrait" class="ts-photo-card" :style="{ '--pc': m.member.bg }">
              <img :src="m.member.portrait" :alt="m.member.name" class="ts-photo-img" :style="m.member.id === 2 ? 'object-fit:contain; height:auto;' : ''" />
            </div>
          </div>
          <div v-if="(m.member.id === 3 || m.member.id === 4) && m.member.portrait" class="ts-photo-below" :style="{ '--pc': m.member.bg }">
            <img :src="m.member.portrait" :alt="m.member.name" class="ts-photo-img-below" :style="m.member.id === 4 ? 'object-fit:cover; object-position:top; width:100%; height:280px;' : ''" />
          </div>
        </div>
      </div>
    </section>

    <!-- ====== CTA ====== -->
    <section class="ts-cta">
      <div class="container">
        <div class="ts-cta-inner">
          <h2>Act Together, Change the World</h2>
          <p>Each member's goals are just the beginning. The 17 Sustainable Development Goals are interconnected and require everyone's participation.</p>
          <router-link to="/sdgs" class="btn btn-primary">
            Explore All 17 Goals
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* ====== Header ====== */
.ts-header {
  background: linear-gradient(165deg, #0d0d18 0%, #1a1a2e 40%, #0d0d18 100%);
  color: #fff; padding: 80px 0; text-align: center;
  position: relative; overflow: hidden;
}
.ts-header::before {
  content: ''; position: absolute; inset: 0;
  background: radial-gradient(ellipse 500px 200px at 50% 25%, rgba(196,139,92,0.05) 0%, transparent 70%);
  pointer-events: none;
}
.ts-eyebrow {
  font-size: 0.72rem; font-weight: 700; letter-spacing: 0.12em;
  text-transform: uppercase; color: #c48b5c; margin-bottom: 16px;
}
.ts-header h1 {
  font-family: Georgia, serif;
  font-size: clamp(2.2rem, 4vw, 3rem);
  color: #fff; margin-bottom: 16px;
}
.ts-header p { color: rgba(255,255,255,0.5); font-size: 1.1rem; }

/* ====== Content ====== */
.ts-content { padding: 80px 0; background: #fdfaf6; }

.member-block {
  margin-bottom: 80px;
  background: #fff;
  border-radius: 20px;
  padding: 48px 40px;
  border: 1px solid #f0ebe4;
}
.member-block:last-child { margin-bottom: 0; }

/* Member header */
.mh { display: flex; align-items: center; gap: 24px; margin-bottom: 20px; flex-wrap: wrap; }
.mh-avatar {
  width: 72px; height: 72px; min-width: 72px;
  border-radius: 50%;
  border: 3px solid;
  display: flex; align-items: center; justify-content: center;
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(28,28,36,0.15);
}
.mh-photo {
  width: 100%; height: 100%;
  object-fit: cover;
  border-radius: 50%;
}
/* Portrait photo card inside SDG grid */
.ts-photo-card {
  width: 200px;
  aspect-ratio: 3 / 4;
  border-radius: 14px;
  border: 2px solid var(--pc, #f0ebe4);
  overflow: hidden;
  box-shadow: 0 6px 20px rgba(28,28,36,0.10);
}
.ts-photo-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  border-radius: 12px;
}

/* Portrait photo below grid */
.ts-photo-below {
  margin-top: 14px;
  max-width: 240px;
  border-radius: 14px;
  border: 2px solid var(--pc, #f0ebe4);
  overflow: hidden;
  box-shadow: 0 6px 20px rgba(28,28,36,0.10);
}
.ts-photo-img-below {
  width: 100%;
  height: auto;
  display: block;
  border-radius: 12px;
}
.mh-info h2 {
  font-family: Georgia, serif;
  font-size: 1.6rem; color: #1c1c24; margin-bottom: 8px;
}
.mh-tags { display: flex; gap: 8px; flex-wrap: wrap; align-items: center; }
.tag-bg {
  font-size: 0.75rem; color: #6b6560;
  background: rgba(28,28,36,0.04);
  padding: 4px 12px; border-radius: 100px;
}
.tag-id {
  font-size: 0.72rem; color: #8c8782; font-family: monospace;
}
.mh-focus {
  font-size: 1.05rem; color: #6b6560; line-height: 1.7;
  font-style: italic; padding-left: 96px; margin-bottom: 36px;
}

/* SDG cards grid */
.ts-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 14px;
}
.ts-sdg-card {
  padding: 24px;
  border-radius: 14px;
  background: var(--cl, #fefcf9);
  border: 1px solid #f0ebe4;
  transition: all 0.3s ease;
}
.ts-sdg-card:hover {
  box-shadow: 0 8px 24px rgba(28,28,36,0.08);
  border-color: transparent;
}
.ts-sdg-head { display: flex; gap: 14px; align-items: flex-start; margin-bottom: 12px; }
.ts-sdg-num {
  font-family: Georgia, serif;
  font-size: 1.8rem; font-weight: 700; line-height: 1;
  opacity: 0.8; min-width: 40px;
}
.ts-sdg-head h3 {
  font-family: Georgia, serif;
  font-size: 1.05rem; color: #1c1c24; margin-bottom: 2px;
}
.ts-sdg-sub { font-size: 0.75rem; color: #8c8782; font-style: italic; }
.ts-sdg-desc { color: #6b6560; font-size: 0.9rem; line-height: 1.65; }

/* ====== CTA ====== */
.ts-cta {
  padding: 80px 0;
  background: linear-gradient(160deg, #1c1c24 0%, #252530 50%, #1c1c24 100%);
}
.ts-cta-inner { text-align: center; }
.ts-cta-inner h2 {
  font-family: Georgia, serif;
  font-size: 2rem; color: #fff; margin-bottom: 12px;
}
.ts-cta-inner p {
  color: rgba(255,255,255,0.5); font-size: 1.08rem; margin-bottom: 32px;
}

@media (max-width: 768px) {
  .mh { flex-direction: column; text-align: center; }
  .mh-photo-card { width: 100px; height: 125px; min-width: 100px; }
  .mh-focus { padding-left: 0; text-align: center; }
  .member-block { padding: 32px 20px; }
  .ts-grid { grid-template-columns: 1fr; }
}
</style>
