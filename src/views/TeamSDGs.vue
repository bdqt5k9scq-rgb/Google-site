<script setup lang="ts">
import { onMounted } from 'vue'
import gsap from 'gsap'
import { GSAP_EASE } from '@/lib/animations'

const memberSDGs = [
  {
    member: { id: 1, name: 'Li Shuhang', role: '项目负责人', background: '环境科学专业', photo: '', bg: '#2c5f2d', studentId: '8168667' },
    focus: '聚焦生态环境领域，探索气候变化与生物多样性保护的科学解决方案',
    sdgs: [
      { id: 13, title: '气候行动', subtitle: 'Climate Action', color: '#3f7e44', description: '气候变化是21世纪最严峻的全球性挑战。Li Shuhang致力于通过环境科学研究，分析碳排放趋势，提出切实可行的减排方案，推动社会各界采取紧急行动应对气候变化及其影响。' },
      { id: 15, title: '陆地生物', subtitle: 'Life on Land', color: '#00a651', description: '生物多样性丧失正在以前所未有的速度发生。Li Shuhang关注森林生态系统保护、荒漠化防治和土地退化修复，倡导可持续的土地管理和生态恢复实践。' },
      { id: 6, title: '清洁饮水', subtitle: 'Clean Water and Sanitation', color: '#26bde2', description: '水资源安全是环境可持续发展的核心议题。Li Shuhang研究水资源管理与水生态系统保护，推动清洁饮水和卫生设施的普及，确保所有人获得安全、可负担的饮用水。' }
    ]
  },
  {
    member: { id: 2, name: 'Feng Jingyi', role: '技术开发', background: '计算机科学专业', photo: '', bg: '#1a3a5c', studentId: '8168308' },
    focus: '用技术创新驱动可持续发展，开发环保科技解决方案应对全球挑战',
    sdgs: [
      { id: 9, title: '产业、创新与基础设施', subtitle: 'Industry, Innovation and Infrastructure', color: '#fd6925', description: '技术创新是实现可持续发展目标的关键驱动力。Feng Jingyi专注于运用计算机科学技术，构建智慧环保平台，推动包容性工业化和可持续基础设施建设。' },
      { id: 7, title: '廉价清洁能源', subtitle: 'Affordable and Clean Energy', color: '#fcc30b', description: '能源转型是应对气候危机的核心路径。Feng Jingyi研发能源监测与优化系统，通过智能算法提升能源使用效率，推动可再生能源的普及应用。' },
      { id: 12, title: '负责任消费和生产', subtitle: 'Responsible Consumption and Production', color: '#bf8b2e', description: '技术可以改变消费模式。Feng Jingyi开发碳足迹追踪与可持续消费引导系统，帮助企业和个人实现更负责任的资源使用和生产决策。' }
    ]
  },
  {
    member: { id: 3, name: 'Wang Luyang', role: '政策研究', background: '国际事务专业', photo: '', bg: '#5c2d6e', studentId: '8168505' },
    focus: '推动全球可持续发展合作，促进公平正义与伙伴关系建设',
    sdgs: [
      { id: 16, title: '和平、正义与强大机构', subtitle: 'Peace, Justice and Strong Institutions', color: '#19489d', description: '和平与正义是可持续发展的基石。Wang Luyang研究国际法治与治理机制，推动建立有效、负责和包容的机构，为所有人提供诉诸司法的机会。' },
      { id: 17, title: '促进目标实现的伙伴关系', subtitle: 'Partnerships for the Goals', color: '#192841', description: '全球伙伴关系是实现所有SDGs的前提。Wang Luyang致力于加强多利益攸关方合作，促进知识、技术和财政资源的跨境流动与共享。' },
      { id: 5, title: '性别平等', subtitle: 'Gender Equality', color: '#ff3a21', description: '性别平等不仅是基本人权，更是可持续发展的必要条件。Wang Luyang倡导消除对妇女和女童的一切形式歧视，推动女性在决策过程中的平等参与。' },
      { id: 10, title: '减少不平等', subtitle: 'Reduced Inequalities', color: '#dd1367', description: '全球不平等问题日益严峻。Wang Luyang研究包容性政策设计，推动各国在收入分配、社会保护和机会平等方面实现实质性改善。' }
    ]
  },
  {
    member: { id: 4, name: 'Lu Jianning', role: '数据分析师', background: '统计学专业', photo: '', bg: '#2c4a3e', studentId: '8168379' },
    focus: '以数据驱动可持续发展评估，用量化分析揭示问题、验证成效',
    sdgs: [
      { id: 4, title: '优质教育', subtitle: 'Quality Education', color: '#c5192d', description: '教育是打破贫困循环最有力的工具。Lu Jianning通过数据分析评估教育资源分配的公平性，为政策制定者提供数据驱动的决策支持，推动包容和公平的优质教育。' },
      { id: 3, title: '良好健康与福祉', subtitle: 'Good Health and Well-being', color: '#4c9f38', description: '数据在公共卫生领域具有不可替代的价值。Lu Jianning运用统计模型分析健康趋势、疾病分布和医疗资源配置，为全民健康覆盖提供量化依据。' },
      { id: 1, title: '消除贫困', subtitle: 'No Poverty', color: '#e5243b', description: '贫困是多维度的复杂问题。Lu Jianning构建贫困评估指标体系和监测框架，追踪减贫进展，识别贫困根源，助力精准脱贫政策的制定与实施。' },
      { id: 2, title: '零饥饿', subtitle: 'Zero Hunger', color: '#dda63a', description: '粮食安全是可持续发展的基础保障。Lu Jianning分析农业生产数据、粮食供应链效率和营养状况指标，为实现零饥饿目标提供科学评估和方法支持。' }
    ]
  }
]

onMounted(() => {
  gsap.context(() => {
    const header = document.querySelector('.team-sdgs-header')
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

    gsap.fromTo('.member-section',
      { y: 64, opacity: 0 },
      {
        y: 0, opacity: 1, duration: 0.7, stagger: 0.15, ease: GSAP_EASE.out,
        scrollTrigger: { trigger: '.team-sdgs-content', start: 'top 85%' },
      }
    )

    // SDG card hover
    const cards = gsap.utils.toArray<HTMLElement>('.team-sdg-card')
    cards.forEach((card) => {
      card.addEventListener('mouseenter', () => {
        gsap.to(card, { y: -4, scale: 1.02, duration: 0.3, ease: 'power2.out' })
      })
      card.addEventListener('mouseleave', () => {
        gsap.to(card, { y: 0, scale: 1, duration: 0.35, ease: 'power2.out' })
      })
    })
  })
})
</script>

<template>
  <div class="team-sdgs">
    <!-- ====== Header ====== -->
    <section class="team-sdgs-header">
      <div class="container container-narrow">
        <p class="team-sdgs-eyebrow">团队成员 &middot; SDG 目标分工</p>
        <h1>每个人都有自己的使命</h1>
        <p>四位来自不同专业领域的团队成员，将各自专长与可持续发展目标紧密结合</p>
      </div>
    </section>

    <!-- ====== Member SDG sections ====== -->
    <section class="team-sdgs-content">
      <div class="container container-narrow">
        <div
          v-for="m in memberSDGs"
          :key="m.member.id"
          class="member-section"
        >
          <!-- Member intro -->
          <div class="member-header" :style="{ '--member-bg': m.member.bg }">
            <div class="member-avatar-lg">
              <div class="avatar-initial-lg">{{ m.member.name.charAt(0) }}</div>
            </div>
            <div class="member-info">
              <h2 class="member-name-lg">{{ m.member.name }}</h2>
              <span class="member-role-tag">{{ m.member.role }}</span>
              <span class="member-bg-tag">{{ m.member.background }}</span>
              <span class="member-id-tag">学号: {{ m.member.studentId }}</span>
            </div>
          </div>
          <p class="member-focus">{{ m.focus }}</p>

          <!-- SDG cards for this member -->
          <div class="team-sdg-grid">
            <div
              v-for="sdg in m.sdgs"
              :key="sdg.id"
              class="team-sdg-card card"
              :style="{ '--sdg-color': sdg.color, '--sdg-color-light': sdg.color + '15' }"
            >
              <div class="team-sdg-top">
                <span class="team-sdg-num" :style="{ color: sdg.color }">
                  {{ String(sdg.id).padStart(2, '0') }}
                </span>
                <div class="team-sdg-titles">
                  <h3>{{ sdg.title }}</h3>
                  <p class="team-sdg-sub">{{ sdg.subtitle }}</p>
                </div>
              </div>
              <p class="team-sdg-desc">{{ sdg.description }}</p>
              <div class="team-sdg-accent" :style="{ background: sdg.color }"></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ====== Call to action ====== -->
    <section class="team-sdgs-cta">
      <div class="container container-narrow">
        <div class="cta-card">
          <h2>一起行动</h2>
          <p>每位团队成员的目标只是起点。17项可持续发展目标相互关联，需要每个人的参与和贡献。</p>
          <router-link to="/sdgs" class="btn btn-primary">
            了解全部17项目标
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* ====== Header ====== */
.team-sdgs-header {
  background: linear-gradient(165deg, #1c1c24 0%, #252530 40%, #1c1c24 100%);
  color: #fff;
  padding: 72px 0;
  text-align: center;
  position: relative;
  overflow: hidden;
}

.team-sdgs-header::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image:
    url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.025'/%3E%3C/svg%3E");
  pointer-events: none;
}

.team-sdgs-eyebrow {
  font-family: var(--font-body, sans-serif);
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--color-terracotta, #c48b5c);
  margin-bottom: 12px;
}

.team-sdgs-header h1 {
  font-family: var(--font-display, Georgia, serif);
  font-size: clamp(2.2rem, 4vw, 3rem);
  color: #fff;
  margin-bottom: 16px;
}

.team-sdgs-header p {
  color: rgba(255, 255, 255, 0.55);
  font-size: 1.08rem;
}

/* ====== Content ====== */
.team-sdgs-content {
  padding: 64px 0;
  background: var(--color-paper, #fdfaf6);
}

.member-section {
  margin-bottom: 72px;
}

.member-section:last-child {
  margin-bottom: 0;
}

/* ====== Member Header ====== */
.member-header {
  display: flex;
  align-items: center;
  gap: 24px;
  margin-bottom: 20px;
}

.avatar-initial-lg {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--member-bg, #c48b5c), color-mix(in srgb, var(--member-bg, #c48b5c) 70%, #fff));
  color: #fff;
  font-family: var(--font-display, Georgia, serif);
  font-size: 2.2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  box-shadow: 0 8px 24px rgba(28, 28, 36, 0.12);
}

.member-name-lg {
  font-family: var(--font-display, Georgia, serif);
  font-size: 1.6rem;
  color: var(--color-ink, #1c1c24);
  margin-bottom: 6px;
}

.member-role-tag {
  display: inline-block;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--color-terracotta, #c48b5c);
  background: rgba(196, 139, 92, 0.1);
  padding: 3px 12px;
  border-radius: 100px;
  margin-right: 8px;
  margin-bottom: 4px;
}

.member-bg-tag {
  display: inline-block;
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  color: var(--color-text-muted, #6b6560);
  background: rgba(28, 28, 36, 0.05);
  padding: 3px 12px;
  border-radius: 100px;
}

.member-id-tag {
  display: block;
  font-size: 0.72rem;
  font-weight: 500;
  color: var(--color-text-light, #8c8782);
  margin-top: 6px;
  font-family: monospace;
}

.member-focus {
  font-size: 1.05rem;
  color: var(--color-text-muted, #6b6560);
  line-height: 1.7;
  margin-bottom: 28px;
  padding-left: 104px;
  font-style: italic;
}

/* ====== SDG cards ====== */
.team-sdg-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 16px;
}

.team-sdg-card {
  padding: 24px;
  position: relative;
  overflow: hidden;
  cursor: default;
}

.team-sdg-top {
  display: flex;
  gap: 14px;
  align-items: flex-start;
  margin-bottom: 14px;
}

.team-sdg-num {
  font-family: var(--font-display, Georgia, serif);
  font-size: 1.8rem;
  font-weight: 700;
  line-height: 1;
  opacity: 0.8;
  flex-shrink: 0;
}

.team-sdg-titles h3 {
  font-family: var(--font-display, Georgia, serif);
  font-size: 1.05rem;
  color: var(--color-ink, #1c1c24);
  margin-bottom: 2px;
}

.team-sdg-sub {
  font-size: 0.78rem;
  color: var(--color-text-light, #8c8782);
  font-style: italic;
}

.team-sdg-desc {
  color: var(--color-text-muted, #6b6560);
  font-size: 0.92rem;
  line-height: 1.7;
}

.team-sdg-accent {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 3px;
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.35s var(--ease-out, cubic-bezier(0.16, 1, 0.3, 1));
}

.team-sdg-card:hover .team-sdg-accent {
  transform: scaleX(1);
}

/* ====== CTA ====== */
.team-sdgs-cta {
  padding: 64px 0 80px;
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

/* ====== Responsive ====== */
@media (max-width: 768px) {
  .member-header {
    flex-direction: column;
    text-align: center;
    gap: 16px;
  }

  .member-focus {
    padding-left: 0;
    text-align: center;
  }

  .team-sdg-grid {
    grid-template-columns: 1fr;
  }

  .avatar-initial-lg {
    width: 64px;
    height: 64px;
    font-size: 1.6rem;
  }

  .member-name-lg {
    font-size: 1.3rem;
  }
}
</style>
