<script setup lang="ts">
import { RouterView, useRouter } from 'vue-router'
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'

const router = useRouter()

// Refresh all ScrollTrigger positions after SPA route change
router.afterEach(() => {
  ScrollTrigger.refresh()
})

// ====== Page transition hooks ======
function onBeforeEnter(el: Element) {
  const target = el as HTMLElement
  gsap.set(target, { opacity: 0, y: 24 })
}

function onEnter(el: Element, done: () => void) {
  const target = el as HTMLElement
  gsap.to(target, {
    opacity: 1, y: 0, duration: 0.55, ease: 'power3.out',
    onComplete: done,
  })
}

function onLeave(el: Element, done: () => void) {
  const target = el as HTMLElement
  gsap.to(target, {
    opacity: 0, y: -16, duration: 0.25, ease: 'power2.in',
    onComplete: done,
  })
}
</script>

<template>
  <div class="app">
    <Navbar />
    <main>
      <router-view v-slot="{ Component, route }">
        <transition
          @before-enter="onBeforeEnter"
          @enter="onEnter"
          @leave="onLeave"
          mode="out-in"
        >
          <component :is="Component" :key="route.path" />
        </transition>
      </router-view>
    </main>
    <Footer />
  </div>
</template>

<style scoped>
.app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

main {
  flex: 1;
}
</style>
