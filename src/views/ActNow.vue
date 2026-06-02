<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import gsap from 'gsap'
import { GSAP_EASE } from '@/lib/animations'

const actions = [
  { id: 1, title: '节约用电', description: '使用节能灯泡，关闭不必要的电器，使用太阳能设备', category: '能源', tips: ['使用LED灯泡替代传统照明', '关闭待机电器避免能耗', '考虑安装太阳能发电板'] },
  { id: 2, title: '绿色出行', description: '选择公共交通、骑行或步行，减少私家车使用', category: '交通', tips: ['优先乘坐公共交通', '短距离骑行或步行', '与同事朋友拼车出行'] },
  { id: 3, title: '减少浪费', description: '减少食物浪费，使用可重复使用的购物袋和水杯', category: '消费', tips: ['出门自带购物袋', '拒绝一次性餐具', '合理规划饮食避免浪费'] },
  { id: 4, title: '健康饮食', description: '减少肉类消费，多吃本地和有机食品', category: '饮食', tips: ['每周尝试素食一天', '优先购买本地农产品', '在家中种植蔬菜香草'] },
  { id: 5, title: '水资源保护', description: '节约用水，修复漏水设施，收集雨水', category: '资源', tips: ['缩短淋浴时间', '及时修复漏水龙头', '收集雨水浇灌植物'] },
  { id: 6, title: '植树造林', description: '参与植树活动，支持森林保护项目', category: '环境', tips: ['参加社区植树活动', '支持林业保护项目', '种植适合本地的树种'] },
  { id: 7, title: '垃圾分类', description: '正确分类垃圾，促进资源回收利用', category: '废物处理', tips: ['学习垃圾分类知识', '参与社区回收计划', '支持循环经济产品'] },
  { id: 8, title: '宣传教育', description: '向他人宣传可持续发展理念，鼓励更多人参与', category: '教育', tips: ['分享环保知识给朋友', '组织社区环保活动', '参与环保公益组织'] }
]

const categories = ['全部', '能源', '交通', '消费', '饮食', '资源', '环境', '废物处理', '教育']
const selectedCategory = ref('全部')

const filteredActions = computed(() => {
  if (selectedCategory.value === '全部') return actions
  return actions.filter(action => action.category === selectedCategory.value)
})

const currentYear = new Date().getFullYear()
const yearsLeft = 2030 - currentYear

const actStats = [
  { value: '193', label: '成员国承诺' },
  { value: '17', label: '可持续发展目标' },
  { value: '78亿', label: '全球人口' },
  { value: String(yearsLeft), label: '年时间窗口' }
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
        <p class="act-eyebrow">现在就行动</p>
        <h1>立即行动</h1>
        <p>每个人的小小行动，都能为地球带来改变。加入我们，共同迈向可持续发展的未来</p>
        <!-- Countdown -->
        <div class="countdown">
          <div class="countdown-item">
            <span class="countdown-num">{{ yearsLeft }}</span>
            <span class="countdown-label">年</span>
          </div>
          <span class="countdown-sep">:</span>
          <div class="countdown-item">
            <span class="countdown-num">12</span>
            <span class="countdown-label">月</span>
          </div>
          <span class="countdown-sep">:</span>
          <div class="countdown-item">
            <span class="countdown-num">31</span>
            <span class="countdown-label">天</span>
          </div>
          <p class="countdown-text">距离2030年目标期限</p>
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
        <h2 class="section-title">您可以采取的行动</h2>
        <p class="section-subtitle">选择适合您的领域，开始做出改变</p>

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
        <p class="cta-eyebrow">加入我们</p>
        <h2>每一个行动都很重要</h2>
        <p>从今天开始，做出改变，为可持续发展贡献您的力量。您的每一个选择，都在塑造未来。</p>
        <div class="cta-buttons">
          <a href="/sdgs" class="btn btn-primary">了解更多SDG目标</a>
          <a href="/carbon-footprint" class="btn btn-secondary">计算您的碳足迹</a>
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
