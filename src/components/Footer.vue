<script setup lang="ts">
import { onMounted } from 'vue'
import gsap from 'gsap'

const currentYear = new Date().getFullYear()

onMounted(() => {
  gsap.context(() => {
    gsap.fromTo('.footer-grid, .footer-bottom',
      { y: 40, opacity: 0 },
      {
        y: 0, opacity: 1, duration: 0.7, stagger: 0.1, ease: 'power3.out',
        scrollTrigger: { trigger: '.footer', start: 'top 90%' },
      }
    )
  })
})
</script>

<template>
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <!-- Brand column -->
        <div class="footer-col footer-col--brand">
          <div class="footer-brand-mark">
            <svg viewBox="0 0 40 40" class="footer-logo">
              <circle cx="20" cy="20" r="18" fill="none" stroke="currentColor" stroke-width="2"/>
              <circle cx="20" cy="20" r="10" fill="none" stroke="currentColor" stroke-width="1" opacity="0.5"/>
              <circle cx="20" cy="20" r="4" fill="currentColor" opacity="0.8"/>
            </svg>
          </div>
          <h3>UN Sustainable Development Goals</h3>
          <p>Working together for a better,<br>more sustainable future</p>
        </div>

        <!-- Links -->
        <div class="footer-col">
          <h4>Browse Pages</h4>
          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about">About Us</a></li>
            <li><a href="/sdgs">SDG Goals</a></li>
            <li><a href="/carbon-footprint">Carbon Footprint</a></li>
            <li><a href="/act-now">Act Now</a></li>
          </ul>
        </div>

        <!-- Contact -->
        <div class="footer-col">
          <h4>Contact</h4>
          <ul class="footer-contact">
            <li>
              <span class="contact-icon">✉</span>
              contact@sdg-website.org
            </li>
            <li>
              <span class="contact-icon">☎</span>
              +86 123 4567 8900
            </li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div class="footer-bottom-line"></div>
        <p>&copy; {{ currentYear }} SDG Website &mdash; All Rights Reserved</p>
        <p class="footer-bottom-sub">This website is dedicated to promoting the UN Sustainable Development Goals</p>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  background: var(--color-charcoal, #2d2d35);
  color: rgba(255, 255, 255, 0.8);
  padding: var(--space-3xl, 64px) 0 var(--space-lg, 24px);
  margin-top: var(--space-4xl, 96px);
  position: relative;
  overflow: hidden;
}

/* Subtle grain texture on dark footer */
.footer::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image:
    url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
  background-repeat: repeat;
  background-size: 200px 200px;
  pointer-events: none;
}

.footer-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr 1fr;
  gap: var(--space-2xl, 48px);
  margin-bottom: var(--space-2xl, 48px);
  position: relative;
  z-index: 1;
}

/* Brand */
.footer-col--brand h3 {
  font-family: var(--font-display, Georgia, serif);
  font-size: 1.25rem;
  color: #fff;
  margin-bottom: var(--space-sm, 8px);
}

.footer-col--brand p {
  color: rgba(255, 255, 255, 0.5);
  font-size: 0.9rem;
  line-height: 1.6;
}

.footer-brand-mark {
  width: 36px;
  height: 36px;
  color: var(--color-terracotta, #c48b5c);
  margin-bottom: var(--space-md, 16px);
}

.footer-logo {
  width: 100%;
  height: 100%;
}

/* Link columns */
.footer-col h4 {
  font-family: var(--font-body, sans-serif);
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: rgba(255, 255, 255, 0.4);
  margin-bottom: var(--space-md, 16px);
}

.footer-col ul {
  list-style: none;
}

.footer-col li {
  margin-bottom: var(--space-sm, 8px);
}

.footer-col a {
  color: rgba(255, 255, 255, 0.7);
  text-decoration: none;
  font-size: 0.95rem;
  transition: color 0.25s var(--ease-out, cubic-bezier(0.16, 1, 0.3, 1));
}

.footer-col a:hover {
  color: var(--color-terracotta, #c48b5c);
}

.footer-contact li {
  display: flex;
  align-items: center;
  gap: 8px;
  color: rgba(255, 255, 255, 0.6);
  font-size: 0.9rem;
}

.contact-icon {
  opacity: 0.5;
  font-size: 0.85rem;
}

/* Bottom bar */
.footer-bottom {
  position: relative;
  z-index: 1;
  text-align: center;
  padding-top: var(--space-lg, 24px);
}

.footer-bottom-line {
  height: 1px;
  background: linear-gradient(
    90deg,
    transparent 0%,
    rgba(255, 255, 255, 0.08) 30%,
    rgba(255, 255, 255, 0.12) 50%,
    rgba(255, 255, 255, 0.08) 70%,
    transparent 100%
  );
  margin-bottom: var(--space-lg, 24px);
}

.footer-bottom p {
  color: rgba(255, 255, 255, 0.35);
  font-size: 0.85rem;
  margin-bottom: 4px;
}

.footer-bottom-sub {
  font-size: 0.8rem;
  opacity: 0.7;
}

@media (max-width: 768px) {
  .footer-grid {
    grid-template-columns: 1fr;
    gap: var(--space-xl, 32px);
  }

  .footer-col--brand {
    text-align: center;
  }

  .footer-brand-mark {
    margin-inline: auto;
  }
}
</style>
