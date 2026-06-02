<script setup lang="ts">
import { ref, computed, nextTick, onMounted } from 'vue'
import gsap from 'gsap'
import { GSAP_EASE } from '@/lib/animations'

const formData = ref({
  transportation: { carDistance: 0, publicTransport: 0, flights: 0 },
  energy: { electricity: 0, gas: 0, heating: 0 },
  food: { meatDays: 0, localFood: 0 },
  waste: { recycling: false, composting: false }
})

const showResult = ref(false)

const calculateCarbonFootprint = () => {
  let total = 0
  total += formData.value.transportation.carDistance * 0.2
  total += formData.value.transportation.publicTransport * 0.05
  total += formData.value.transportation.flights * 250
  total += formData.value.energy.electricity * 0.5
  total += formData.value.energy.gas * 2.3
  total += formData.value.energy.heating * 1.8
  total += (21 - formData.value.food.meatDays) * 0.05
  total += formData.value.food.localFood * 0.1
  if (!formData.value.waste.recycling) total += 100
  if (!formData.value.waste.composting) total += 50
  return Math.round(total)
}

const result = computed(() => calculateCarbonFootprint())

const resultLevel = computed(() => {
  if (result.value < 3000) return { level: '优秀', color: '#5c8d6d', message: '您的碳足迹非常低，继续保持！' }
  if (result.value < 6000) return { level: '良好', color: '#2c5282', message: '您的碳足迹处于中等水平，可以进一步改善。' }
  if (result.value < 10000) return { level: '一般', color: '#c48b5c', message: '您的碳足迹较高，建议采取更多环保措施。' }
  return { level: '较高', color: '#b8573e', message: '您的碳足迹很高，请采取行动减少碳排放。' }
})

const tips = computed(() => {
  const tipsList = []
  if (formData.value.transportation.carDistance > 100) tipsList.push('考虑使用公共交通工具或骑行代替开车')
  if (formData.value.transportation.flights > 2) tipsList.push('减少长途飞行，考虑视频会议替代方案')
  if (formData.value.energy.electricity > 500) tipsList.push('使用节能电器，养成随手关灯的习惯')
  if (formData.value.food.meatDays > 14) tipsList.push('尝试减少肉类消费，多吃植物性食物')
  if (!formData.value.waste.recycling) tipsList.push('开始垃圾分类和回收')
  if (!formData.value.waste.composting) tipsList.push('尝试堆肥处理厨余垃圾')
  return tipsList.length > 0 ? tipsList : ['您做得很好！继续保持环保习惯。']
})

const handleCalculate = () => {
  showResult.value = true
  nextTick(() => {
    gsap.fromTo('.result-card',
      { y: 40, opacity: 0 },
      { y: 0, opacity: 1, duration: 0.7, ease: GSAP_EASE.back }
    )
    gsap.fromTo('.result-value',
      { scale: 0, opacity: 0 },
      { scale: 1, opacity: 1, duration: 0.6, delay: 0.3, ease: GSAP_EASE.elastic }
    )
    gsap.fromTo('.result-level',
      { y: 16, opacity: 0 },
      { y: 0, opacity: 1, duration: 0.4, delay: 0.5, ease: GSAP_EASE.out }
    )
    gsap.fromTo('.tips-section',
      { y: 24, opacity: 0 },
      { y: 0, opacity: 1, duration: 0.5, delay: 0.6, ease: GSAP_EASE.out }
    )
    document.querySelector('.result-section')?.scrollIntoView({ behavior: 'smooth' })
  })
}

const handleReset = () => {
  formData.value = {
    transportation: { carDistance: 0, publicTransport: 0, flights: 0 },
    energy: { electricity: 0, gas: 0, heating: 0 },
    food: { meatDays: 0, localFood: 0 },
    waste: { recycling: false, composting: false }
  }
  showResult.value = false
}

onMounted(() => {
  gsap.context(() => {
    const header = document.querySelector('.carbon-footprint .cf-header')
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

    gsap.fromTo('.form-section',
      { y: 40, opacity: 0 },
      { y: 0, opacity: 1, duration: 0.5, stagger: 0.08, ease: GSAP_EASE.out,
        scrollTrigger: { trigger: '.calculator-form', start: 'top 90%' } }
    )
  })
})
</script>

<template>
  <div class="carbon-footprint">
    <!-- ====== Header ====== -->
    <section class="cf-header">
      <div class="container container-narrow">
        <p class="cf-eyebrow">环境足迹</p>
        <h1>碳足迹计算器</h1>
        <p>了解您的日常活动对环境的影响，计算您的个人碳排放量</p>
      </div>
    </section>

    <!-- ====== Calculator ====== -->
    <section class="calculator-section">
      <div class="container container-narrow">
        <div v-if="!showResult" class="calculator-form">
          <div class="form-section">
            <div class="form-section-header">
              <span class="form-section-icon">🚗</span>
              <h3>交通出行</h3>
            </div>
            <div class="form-group">
              <label>每周驾车里程（公里）</label>
              <input type="number" v-model.number="formData.transportation.carDistance"
                placeholder="0" min="0" />
            </div>
            <div class="form-group">
              <label>每周公共交通次数</label>
              <input type="number" v-model.number="formData.transportation.publicTransport"
                placeholder="0" min="0" />
            </div>
            <div class="form-group">
              <label>每年长途飞行次数</label>
              <input type="number" v-model.number="formData.transportation.flights"
                placeholder="0" min="0" />
            </div>
          </div>

          <div class="form-section">
            <div class="form-section-header">
              <span class="form-section-icon">⚡</span>
              <h3>能源使用</h3>
            </div>
            <div class="form-group">
              <label>每月用电量（千瓦时）</label>
              <input type="number" v-model.number="formData.energy.electricity"
                placeholder="0" min="0" />
            </div>
            <div class="form-group">
              <label>每月用气量（立方米）</label>
              <input type="number" v-model.number="formData.energy.gas"
                placeholder="0" min="0" />
            </div>
            <div class="form-group">
              <label>每月供暖能耗（单位）</label>
              <input type="number" v-model.number="formData.energy.heating"
                placeholder="0" min="0" />
            </div>
          </div>

          <div class="form-section">
            <div class="form-section-header">
              <span class="form-section-icon">🥗</span>
              <h3>饮食习惯</h3>
            </div>
            <div class="form-group">
              <label>每周吃肉天数</label>
              <input type="number" v-model.number="formData.food.meatDays"
                placeholder="0" min="0" max="7" />
            </div>
            <div class="form-group">
              <label>每周本地食品消费比例（%）</label>
              <input type="number" v-model.number="formData.food.localFood"
                placeholder="0" min="0" max="100" />
            </div>
          </div>

          <div class="form-section">
            <div class="form-section-header">
              <span class="form-section-icon">♻️</span>
              <h3>废物处理</h3>
            </div>
            <div class="form-group">
              <label class="checkbox-label">
                <input type="checkbox" v-model="formData.waste.recycling" />
                <span class="checkbox-custom"></span>
                进行垃圾分类回收
              </label>
            </div>
            <div class="form-group">
              <label class="checkbox-label">
                <input type="checkbox" v-model="formData.waste.composting" />
                <span class="checkbox-custom"></span>
                进行厨余堆肥
              </label>
            </div>
          </div>

          <button class="btn btn-primary btn-calculate" @click="handleCalculate">
            计算碳足迹
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </button>
        </div>

        <div v-else class="result-section">
          <div class="result-card">
            <h2>您的碳足迹计算结果</h2>
            <div class="result-value" :style="{ color: resultLevel.color }">
              {{ result.toLocaleString() }}
              <span class="unit">kg CO₂/年</span>
            </div>
            <div class="result-level" :style="{ backgroundColor: resultLevel.color }">
              {{ resultLevel.level }}
            </div>
            <p class="result-message">{{ resultLevel.message }}</p>
          </div>

          <div class="tips-section">
            <h3>🌱 环保建议</h3>
            <ul>
              <li v-for="(tip, index) in tips" :key="index">
                <span class="tip-dot"></span>
                {{ tip }}
              </li>
            </ul>
          </div>

          <button class="btn btn-secondary" @click="handleReset">
            重新计算
          </button>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* ====== Header ====== */
.cf-header {
  background: linear-gradient(165deg, #1c1c24 0%, #252530 40%, #1c1c24 100%);
  color: #fff;
  padding: 72px 0;
  text-align: center;
  position: relative;
  overflow: hidden;
}

.cf-header::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image:
    url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.025'/%3E%3C/svg%3E");
  pointer-events: none;
}

.cf-eyebrow {
  font-family: var(--font-body, sans-serif);
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--color-sage, #5c8d6d);
  margin-bottom: 12px;
}

.cf-header h1 {
  font-family: var(--font-display, Georgia, serif);
  font-size: clamp(2.2rem, 4vw, 3rem);
  color: #fff;
  margin-bottom: 16px;
}

.cf-header p {
  color: rgba(255, 255, 255, 0.55);
  font-size: 1.08rem;
}

/* ====== Calculator ====== */
.calculator-section {
  padding: 64px 0;
  background: var(--color-paper, #fdfaf6);
}

.form-section {
  background: #fff;
  border: 1px solid var(--color-border-light, #f0ebe4);
  border-radius: var(--radius-lg, 12px);
  padding: 28px;
  margin-bottom: 16px;
  transition: border-color 0.3s ease;
}

.form-section:focus-within {
  border-color: var(--color-sage, #5c8d6d);
}

.form-section-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 20px;
}

.form-section-icon {
  font-size: 1.2rem;
}

.form-section h3 {
  font-family: var(--font-display, Georgia, serif);
  font-size: 1.1rem;
  color: var(--color-ink, #1c1c24);
}

.form-group {
  margin-bottom: 14px;
}

.form-group:last-child {
  margin-bottom: 0;
}

.form-group label {
  display: block;
  margin-bottom: 6px;
  font-weight: 500;
  font-size: 0.9rem;
  color: var(--color-text-muted, #6b6560);
}

.form-group input[type="number"] {
  width: 100%;
  padding: 12px 16px;
  border: 1px solid var(--color-border, #e6e0d8);
  border-radius: var(--radius-md, 8px);
  font-size: 1rem;
  font-family: var(--font-body, sans-serif);
  color: var(--color-ink, #1c1c24);
  background: var(--color-cream, #fefcf9);
  transition: all 0.25s ease;
}

.form-group input[type="number"]:focus {
  outline: none;
  border-color: var(--color-sage, #5c8d6d);
  box-shadow: 0 0 0 3px rgba(92, 141, 109, 0.08);
  background: #fff;
}

/* Custom checkbox */
.checkbox-label {
  display: flex !important;
  align-items: center;
  gap: 10px;
  cursor: pointer;
}

.checkbox-label input[type="checkbox"] {
  display: none;
}

.checkbox-custom {
  width: 20px;
  height: 20px;
  border: 2px solid var(--color-border, #e6e0d8);
  border-radius: 4px;
  flex-shrink: 0;
  transition: all 0.2s ease;
  position: relative;
}

.checkbox-label input:checked + .checkbox-custom {
  background: var(--color-sage, #5c8d6d);
  border-color: var(--color-sage, #5c8d6d);
}

.checkbox-label input:checked + .checkbox-custom::after {
  content: '';
  position: absolute;
  left: 5px;
  top: 1px;
  width: 6px;
  height: 10px;
  border: solid #fff;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
}

.btn-calculate {
  width: 100%;
  padding: 16px;
  font-size: 1.05rem;
  margin-top: 8px;
}

/* ====== Result ====== */
.result-section {
  text-align: center;
}

.result-card {
  background: #fff;
  border: 1px solid var(--color-border-light, #f0ebe4);
  border-radius: var(--radius-xl, 20px);
  padding: 44px 32px;
  margin-bottom: 24px;
}

.result-card h2 {
  font-family: var(--font-display, Georgia, serif);
  color: var(--color-ink, #1c1c24);
  margin-bottom: 24px;
}

.result-value {
  font-family: var(--font-display, Georgia, serif);
  font-size: clamp(2.8rem, 5vw, 4rem);
  font-weight: 700;
  line-height: 1;
  margin-bottom: 8px;
}

.unit {
  font-size: 1.1rem;
  font-weight: 400;
  color: var(--color-text-muted, #6b6560);
}

.result-level {
  display: inline-block;
  padding: 6px 20px;
  border-radius: 100px;
  color: #fff;
  font-weight: 600;
  font-size: 0.9rem;
  margin: 16px 0;
}

.result-message {
  color: var(--color-text-muted, #6b6560);
  font-size: 1.05rem;
}

/* Tips */
.tips-section {
  background: #fff;
  border: 1px solid var(--color-sage, #5c8d6d);
  border-left: 4px solid var(--color-sage, #5c8d6d);
  border-radius: var(--radius-lg, 12px);
  padding: 28px;
  margin-bottom: 24px;
  text-align: left;
}

.tips-section h3 {
  font-family: var(--font-display, Georgia, serif);
  color: var(--color-sage, #5c8d6d);
  margin-bottom: 20px;
  text-align: center;
}

.tips-section ul {
  list-style: none;
}

.tips-section li {
  padding: 10px 0;
  display: flex;
  align-items: flex-start;
  gap: 10px;
  border-bottom: 1px solid var(--color-border-light, #f0ebe4);
  color: var(--color-text-muted, #6b6560);
  font-size: 0.95rem;
  line-height: 1.6;
}

.tips-section li:last-child {
  border-bottom: none;
}

.tip-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--color-sage, #5c8d6d);
  margin-top: 7px;
  flex-shrink: 0;
}

@media (max-width: 768px) {
  .result-card {
    padding: 28px 20px;
  }
}
</style>
