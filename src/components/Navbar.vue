<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

const router = useRouter()
const isMenuOpen = ref(false)

onMounted(() => {
  ScrollTrigger.create({
    start: 'top -80px',
    toggleClass: { targets: '.navbar', className: 'navbar-scrolled' },
  })
})

const navItems = [
  { name: 'Home', path: '/' },
  { name: 'About Us', path: '/about' },
  { name: 'SDG Goals', path: '/sdgs' },
  { name: 'Team SDGs', path: '/team-sdgs' },
  { name: 'Carbon Footprint', path: '/carbon-footprint' },
  { name: 'Act Now', path: '/act-now' }
]

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

const closeMenu = () => {
  isMenuOpen.value = false
}
</script>

<template>
  <nav class="navbar">
    <div class="navbar-inner container">
      <div class="navbar-brand" @click="router.push('/')">
        <div class="logo-mark">
          <svg viewBox="0 0 40 40" class="logo-icon">
            <circle cx="20" cy="20" r="18" fill="none" stroke="currentColor" stroke-width="2.5" opacity="0.9"/>
            <circle cx="20" cy="20" r="13" fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.6"/>
            <circle cx="20" cy="20" r="6" fill="currentColor" opacity="0.85"/>
            <line x1="20" y1="4" x2="20" y2="36" stroke="currentColor" stroke-width="1" opacity="0.3"/>
            <line x1="4" y1="20" x2="36" y2="20" stroke="currentColor" stroke-width="1" opacity="0.3"/>
          </svg>
        </div>
        <span class="brand-text">SDG <span class="brand-text-light">Sustainable Development</span></span>
      </div>

      <div class="navbar-links">
        <a
          v-for="item in navItems"
          :key="item.path"
          :href="item.path"
          class="nav-link"
          :class="{ active: router.currentRoute.value.path === item.path }"
          @click.prevent="router.push(item.path); closeMenu()"
        >
          {{ item.name }}
        </a>
      </div>

      <button class="menu-toggle" @click="toggleMenu" :aria-label="isMenuOpen ? 'Close menu' : 'Open menu'">
        <span class="bar"></span>
        <span class="bar"></span>
      </button>
    </div>

    <Transition name="mobile-slide">
      <div v-if="isMenuOpen" class="mobile-menu">
        <a
          v-for="item in navItems"
          :key="item.path"
          :href="item.path"
          class="mobile-link"
          @click.prevent="router.push(item.path); closeMenu()"
        >
          <span class="mobile-link-num">{{ String(navItems.indexOf(item) + 1).padStart(2, '0') }}</span>
          {{ item.name }}
        </a>
      </div>
    </Transition>
  </nav>
</template>

<style scoped>
/* ---- Navbar Base ---- */
.navbar {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(253, 250, 246, 0.88);
  backdrop-filter: blur(16px) saturate(120%);
  -webkit-backdrop-filter: blur(16px) saturate(120%);
  border-bottom: 1px solid transparent;
  transition: all 0.4s var(--ease-out, cubic-bezier(0.16, 1, 0.3, 1));
}

.navbar-scrolled {
  background: rgba(253, 250, 246, 0.94);
  border-bottom-color: var(--color-border-light, #f0ebe4);
  box-shadow: 0 1px 8px rgba(28, 28, 36, 0.04);
}

.navbar-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 64px;
  transition: height 0.4s var(--ease-out, cubic-bezier(0.16, 1, 0.3, 1));
}

.navbar-scrolled .navbar-inner {
  height: 52px;
}

/* ---- Brand ---- */
.navbar-brand {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  user-select: none;
}

.logo-mark {
  width: 36px;
  height: 36px;
  color: var(--color-terracotta, #c48b5c);
  transition: color 0.3s var(--ease-out, cubic-bezier(0.16, 1, 0.3, 1));
}

.navbar-brand:hover .logo-mark {
  color: var(--color-rust, #b8573e);
}

.logo-icon {
  width: 100%;
  height: 100%;
  display: block;
}

.brand-text {
  font-family: var(--font-display, Georgia, serif);
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--color-ink, #1c1c24);
  letter-spacing: -0.01em;
}

.brand-text-light {
  font-weight: 400;
  color: var(--color-text-muted, #6b6560);
  font-size: 0.9rem;
}

/* ---- Desktop links ---- */
.navbar-links {
  display: flex;
  gap: 4px;
}

.nav-link {
  color: var(--color-text-muted, #6b6560);
  text-decoration: none;
  font-weight: 500;
  font-size: 0.9rem;
  padding: 8px 16px;
  border-radius: var(--radius-md, 8px);
  transition: all 0.25s var(--ease-out, cubic-bezier(0.16, 1, 0.3, 1));
  position: relative;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: 3px;
  left: 50%;
  transform: translateX(-50%) scaleX(0);
  width: 20px;
  height: 2px;
  background: var(--color-terracotta, #c48b5c);
  border-radius: 1px;
  transition: transform 0.3s var(--ease-out, cubic-bezier(0.16, 1, 0.3, 1));
}

.nav-link:hover {
  color: var(--color-ink, #1c1c24);
}

.nav-link:hover::after,
.nav-link.active::after {
  transform: translateX(-50%) scaleX(1);
}

.nav-link.active {
  color: var(--color-terracotta, #c48b5c);
}

/* ---- Mobile toggle ---- */
.menu-toggle {
  display: none;
  flex-direction: column;
  gap: 5px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 8px;
  width: 40px;
  height: 40px;
  align-items: center;
  justify-content: center;
}

.bar {
  display: block;
  width: 22px;
  height: 2px;
  background-color: var(--color-ink, #1c1c24);
  border-radius: 1px;
  transition: all 0.3s var(--ease-out, cubic-bezier(0.16, 1, 0.3, 1));
}

/* ---- Mobile menu ---- */
.mobile-menu {
  display: none;
  background: var(--color-paper, #fdfaf6);
  border-bottom: 1px solid var(--color-border-light, #f0ebe4);
  padding: 8px 20px 20px;
}

.mobile-link {
  display: flex;
  align-items: center;
  gap: 14px;
  color: var(--color-ink, #1c1c24);
  text-decoration: none;
  padding: 14px 0;
  font-size: 1.05rem;
  font-weight: 500;
  border-bottom: 1px solid var(--color-border-light, #f0ebe4);
  transition: color 0.2s ease;
}

.mobile-link:last-child {
  border-bottom: none;
}

.mobile-link-num {
  font-family: var(--font-display, Georgia, serif);
  font-size: 0.75rem;
  color: var(--color-terracotta, #c48b5c);
  min-width: 20px;
  opacity: 0.7;
}

.mobile-link:hover {
  color: var(--color-terracotta, #c48b5c);
}

/* ---- Mobile slide transition ---- */
.mobile-slide-enter-active,
.mobile-slide-leave-active {
  transition: all 0.3s var(--ease-out, cubic-bezier(0.16, 1, 0.3, 1));
}

.mobile-slide-enter-from,
.mobile-slide-leave-to {
  opacity: 0;
  transform: translateY(-8px);
}

/* ---- Responsive ---- */
@media (max-width: 768px) {
  .navbar-links {
    display: none;
  }

  .menu-toggle {
    display: flex;
  }

  .mobile-menu {
    display: block;
  }
}
</style>
