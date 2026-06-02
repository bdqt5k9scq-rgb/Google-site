# Assessment 3 Completion — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Complete all 4 assessment instructions by modifying 5 existing static HTML pages, creating 1 new reference-list page, and adding CSS build infrastructure.

**Architecture:** All work is on static HTML pages served from repo root. Pages share `css/style.css`, `js/main.js`, and CDN-loaded GSAP. No Vue SPA changes. A new npm script copies static assets into `dist/` post-build for GitHub Pages deployment.

**Tech Stack:** HTML5, CSS3 (custom properties, grid, flexbox), vanilla JavaScript, GSAP 3.12 (CDN)

---

## File Structure Map

| File | Role | Action |
|------|------|--------|
| `reference-list.html` | APA 7th reference list page | CREATE |
| `index.html` | Home page | MODIFY — add "Why SDGs" + expand to 17 SDG cards |
| `about.html` | About Us page | MODIFY — restructure team cards |
| `sdgs.html` | SDG Goals page | MODIFY — add 4 member research reports |
| `carbon-footprint.html` | Carbon calculator page | MODIFY — upgrade calculator |
| `act-now.html` | Act Now page | MODIFY — add 4 member action reports |
| `css/style.css` | Shared stylesheet | MODIFY — add new section styles |
| `package.json` | Build scripts | MODIFY — add copy-static script |

## Member Assignments (consistent across all pages)

| Member | Surname | SDG (Instruction 3) | Action (Instruction 4) |
|--------|---------|---------------------|------------------------|
| Member 1 | 张 | SDG 4 — Quality Education | Save energy at home |
| Member 2 | 李 | SDG 13 — Climate Action | Walk, bike, public transport |
| Member 3 | 王 | SDG 6 — Clean Water | Eat more vegetables |
| Member 4 | 陈 | SDG 14 — Life Below Water | Reduce, reuse, repair, recycle |

---

### Task 1: Create `reference-list.html` (APA 7th Reference List page)

**Files:**
- Create: `reference-list.html`
- Modify: `index.html`, `about.html`, `sdgs.html`, `carbon-footprint.html`, `act-now.html` (nav links)
- Modify: `css/style.css` (add `.reference-category` and `.hanging-indent` styles)

- [ ] **Step 1: Add CSS for reference list page**

Append to `css/style.css` before the responsive section:

```css
/* ============================================================
   REFERENCE LIST PAGE
   ============================================================ */
.reference-list-section { padding: 64px 0; background: var(--paper); }

.reference-category { margin-bottom: 40px; }
.reference-category:last-child { margin-bottom: 0; }

.reference-category h2 {
  font-family: var(--font-display);
  font-size: 1.4rem;
  color: var(--ink);
  margin-bottom: 20px;
  padding-bottom: 10px;
  border-bottom: 2px solid var(--border-light);
}

.reference-entry {
  background: #fff;
  border: 1px solid var(--border-light);
  border-left: 4px solid var(--terracotta);
  border-radius: var(--radius-md);
  padding: 18px 20px;
  margin-bottom: 10px;
}

.reference-entry p {
  color: var(--text);
  line-height: 1.8;
  margin: 0;
  font-size: 0.95rem;
  padding-left: 2em;
  text-indent: -2em;
}

.reference-entry em {
  color: var(--terracotta);
  font-style: italic;
  font-weight: 600;
}
```

- [ ] **Step 2: Create `reference-list.html`**

Create the full file:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>参考文献列表 — SDG Website</title>
  <meta name="description" content="APA 7th格式参考文献列表，包含联合国文件、学术文献和网络资源。">
  <link rel="icon" type="image/svg+xml" href="vite.svg">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <nav class="navbar">
    <div class="container">
      <a href="index.html" class="navbar-brand">
        <svg viewBox="0 0 40 40" class="logo-icon">
          <circle cx="20" cy="20" r="18" fill="none" stroke="currentColor" stroke-width="2.5" opacity="0.9"/>
          <circle cx="20" cy="20" r="13" fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.6"/>
          <circle cx="20" cy="20" r="6" fill="currentColor" opacity="0.85"/>
          <line x1="20" y1="3" x2="20" y2="37" stroke="currentColor" stroke-width="1" opacity="0.3"/>
          <line x1="3" y1="20" x2="37" y2="20" stroke="currentColor" stroke-width="1" opacity="0.3"/>
        </svg>
        <span class="brand-text">SDG 可持续发展</span>
      </a>
      <div class="navbar-links">
        <a href="index.html" class="nav-link">首页</a>
        <a href="about.html" class="nav-link">关于我们</a>
        <a href="sdgs.html" class="nav-link">SDG目标</a>
        <a href="carbon-footprint.html" class="nav-link">碳足迹计算</a>
        <a href="act-now.html" class="nav-link">行动倡议</a>
        <a href="reference-list.html" class="nav-link active">参考文献</a>
      </div>
      <button class="menu-toggle"><span class="bar"></span><span class="bar"></span></button>
    </div>
    <div class="mobile-menu">
      <a href="index.html" class="mobile-link">首页</a>
      <a href="about.html" class="mobile-link">关于我们</a>
      <a href="sdgs.html" class="mobile-link">SDG目标</a>
      <a href="carbon-footprint.html" class="mobile-link">碳足迹计算</a>
      <a href="act-now.html" class="mobile-link">行动倡议</a>
      <a href="reference-list.html" class="mobile-link">参考文献</a>
    </div>
  </nav>

  <main>
    <section class="page-header">
      <div class="container container-narrow">
        <p class="eyebrow">APA 7th Edition</p>
        <h1>参考文献列表</h1>
        <p>本页面汇总了本网站所有引用来源，遵循APA第7版格式规范</p>
      </div>
    </section>

    <section class="reference-list-section">
      <div class="container container-narrow">

        <div class="reference-category">
          <h2>联合国文件</h2>

          <div class="reference-entry">
            <p>联合国. (2015). <em>变革我们的世界：2030年可持续发展议程</em>. 纽约: 联合国大会. https://sdgs.un.org/2030agenda</p>
          </div>

          <div class="reference-entry">
            <p>联合国. (2015). <em>巴黎协定</em>. 联合国气候变化框架公约缔约方会议第21届会议. https://unfccc.int/process-and-meetings/the-paris-agreement</p>
          </div>

          <div class="reference-entry">
            <p>联合国开发计划署 (UNDP). (2023). <em>2023年人类发展报告：不确定时代，不稳定生活</em>. 纽约: UNDP. https://hdr.undp.org</p>
          </div>

          <div class="reference-entry">
            <p>联合国教科文组织 (UNESCO). (2023). <em>全球教育监测报告2023：技术在教育中的应用</em>. 巴黎: UNESCO. https://www.unesco.org/gem-report</p>
          </div>

          <div class="reference-entry">
            <p>联合国经济和社会事务部. (2023). <em>2023年可持续发展目标进展报告</em>. 纽约: 联合国. https://unstats.un.org/sdgs/report/2023</p>
          </div>

          <div class="reference-entry">
            <p>United Nations. (2024). <em>The Sustainable Development Goals Report 2024</em>. New York: United Nations Publications. https://unstats.un.org/sdgs/report/2024</p>
          </div>
        </div>

        <div class="reference-category">
          <h2>学术与科学文献</h2>

          <div class="reference-entry">
            <p>政府间气候变化专门委员会 (IPCC). (2023). <em>第六次评估报告：气候变化2023</em>. 日内瓦: IPCC. https://www.ipcc.ch/report/ar6</p>
          </div>

          <div class="reference-entry">
            <p>Rockström, J., Steffen, W., Noone, K., Persson, Å., Chapin, F. S., Lambin, E. F., ... & Foley, J. A. (2009). A safe operating space for humanity. <em>Nature</em>, <em>461</em>(7262), 472–475. https://doi.org/10.1038/461472a</p>
          </div>

          <div class="reference-entry">
            <p>Sachs, J. D., Lafortune, G., Fuller, G., & Drumm, E. (2023). <em>Sustainable Development Report 2023: Implementing the SDG Stimulus</em>. Cambridge: Cambridge University Press. https://doi.org/10.1017/9781009210034</p>
          </div>

          <div class="reference-entry">
            <p>Rees, W., & Wackernagel, M. (1992). Ecological footprints and appropriated carrying capacity: What urban economics leaves out. <em>Environment and Urbanization</em>, <em>4</em>(2), 121–130. https://doi.org/10.1177/095624789200400212</p>
          </div>

          <div class="reference-entry">
            <p>World Health Organization (WHO). (2023). <em>Global Status Report on Preventable Deaths and Disease</em>. Geneva: WHO Press.</p>
          </div>

          <div class="reference-entry">
            <p>World Health Organization (WHO). (2022). <em>Guidelines for drinking-water quality (4th ed.)</em>. Geneva: WHO Press.</p>
          </div>
        </div>

        <div class="reference-category">
          <h2>机构报告</h2>

          <div class="reference-entry">
            <p>联合国环境规划署 (UNEP). (2023). <em>排放差距报告2023：打破纪录——气温再创新高</em>. 内罗毕: UNEP. https://www.unep.org/emissions-gap-report-2023</p>
          </div>

          <div class="reference-entry">
            <p>联合国环境规划署 (UNEP). (2023). <em>全球碳足迹报告</em>. 内罗毕: UNEP.</p>
          </div>

          <div class="reference-entry">
            <p>世界自然基金会 (WWF). (2022). <em>地球生命力报告2022：为自然构建积极未来的社会</em>. 瑞士: WWF.</p>
          </div>

          <div class="reference-entry">
            <p>联合国儿童基金会 (UNICEF). (2023). <em>世界儿童状况报告2023</em>. 纽约: UNICEF.</p>
          </div>

          <div class="reference-entry">
            <p>国际能源署 (IEA). (2023). <em>世界能源展望2023</em>. 巴黎: IEA. https://www.iea.org/reports/world-energy-outlook-2023</p>
          </div>

          <div class="reference-entry">
            <p>经济合作与发展组织 (OECD). (2023). <em>教育概览2023：OECD指标</em>. 巴黎: OECD Publishing. https://doi.org/10.1787/eag-2023-en</p>
          </div>
        </div>

        <div class="reference-category">
          <h2>网络资源</h2>

          <div class="reference-entry">
            <p>联合国. (2024). ActNow — 联合国可持续发展目标行动倡议. https://www.un.org/zh/actnow</p>
          </div>

          <div class="reference-entry">
            <p>联合国气候变化框架公约 (UNFCCC). (2024). 什么是碳中和？. https://unfccc.int/zh/carbon-neutrality</p>
          </div>

          <div class="reference-entry">
            <p>Carbon Footprint Ltd. (2024). Carbon Footprint Calculator. https://www.carbonfootprint.com/calculator.aspx</p>
          </div>

          <div class="reference-entry">
            <p>世界自然基金会 (WWF). (2024). WWF Footprint Calculator. https://footprint.wwf.org.uk</p>
          </div>

          <div class="reference-entry">
            <p>United Nations. (2024). UN Carbon Footprint Calculator. https://offset.climateneutralnow.org/footprintcalc</p>
          </div>

          <div class="reference-entry">
            <p>联合国教科文组织 (UNESCO). (2024). 可持续发展目标4——优质教育. https://zh.unesco.org/themes/education-sdgs</p>
          </div>

          <div class="reference-entry">
            <p>中国生态环境部. (2023). <em>中国应对气候变化的政策与行动2023年度报告</em>. https://www.mee.gov.cn</p>
          </div>
        </div>

        <div class="reference-category">
          <h2>补充文献</h2>

          <div class="reference-entry">
            <p>联合国. (2023). <em>2023年世界水资源开发报告：伙伴关系与合作</em>. 联合国教科文组织世界水资源评估计划. 巴黎: UNESCO.</p>
          </div>

          <div class="reference-entry">
            <p>Steffen, W., Richardson, K., Rockström, J., Cornell, S. E., Fetzer, I., Bennett, E. M., ... & Sörlin, S. (2015). Planetary boundaries: Guiding human development on a changing planet. <em>Science</em>, <em>347</em>(6223), 1259855. https://doi.org/10.1126/science.1259855</p>
          </div>

          <div class="reference-entry">
            <p>世界银行. (2023). <em>2023年世界发展报告：移民、难民与社会</em>. 华盛顿特区: 世界银行集团.</p>
          </div>
        </div>

        <div class="apa-note" style="margin-top: 40px;">
          <p><strong>APA第7版格式说明：</strong>本参考文献列表遵循美国心理学会（APA）第7版引用格式规范。每个条目包含作者、出版年份、标题、来源和DOI/URL（如有）。引用格式采用悬挂缩进（首行顶格，续行缩进2字符）。建议读者在学习或研究中参考原始文献以获取更全面的信息。</p>
        </div>

      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="container">
      <div class="footer-content">
        <div class="footer-section"><h3>联合国可持续发展目标</h3><p>为实现更美好、更可持续的未来<br>而共同努力</p></div>
        <div class="footer-section"><h4>快速链接</h4><ul><li><a href="index.html">首页</a></li><li><a href="about.html">关于我们</a></li><li><a href="sdgs.html">SDG目标</a></li><li><a href="carbon-footprint.html">碳足迹计算</a></li><li><a href="act-now.html">行动倡议</a></li><li><a href="reference-list.html">参考文献</a></li></ul></div>
        <div class="footer-section"><h4>联系我们</h4><p>邮箱: contact@sdg-website.org</p><p>电话: +86 123 4567 8900</p></div>
      </div>
      <div class="footer-bottom"><p>&copy; 2026 SDG Website. 保留所有权利。</p><p>本网站致力于宣传联合国可持续发展目标</p></div>
    </div>
  </footer>

  <script src="js/main.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.12/dist/gsap.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.12/dist/ScrollTrigger.min.js"></script>
  <script>
    gsap.registerPlugin(ScrollTrigger);
    document.addEventListener('DOMContentLoaded', function() {
      gsap.fromTo('.page-header h1', { y: 48, opacity: 0 }, { y: 0, opacity: 1, duration: 0.9, ease: 'power3.out' });
      gsap.fromTo('.page-header p', { y: 32, opacity: 0 }, { y: 0, opacity: 1, duration: 0.7, delay: 0.15, ease: 'power3.out' });
      gsap.fromTo('.reference-entry', { y: 40, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, stagger: 0.05, ease: 'power3.out', scrollTrigger: { trigger: '.reference-list-section', start: 'top 90%' } });
    });
  </script>
</body>
</html>
```

- [ ] **Step 3: Add "参考文献" to navbar of all existing pages**

For each of `index.html`, `about.html`, `sdgs.html`, `carbon-footprint.html`, `act-now.html`, add the reference list link to both the desktop navbar-links and mobile-menu sections.

In the desktop `navbar-links` div, add after the act-now link:
```html
<a href="reference-list.html" class="nav-link">参考文献</a>
```

In the `mobile-menu` div, add after the act-now link:
```html
<a href="reference-list.html" class="mobile-link">参考文献</a>
```

Also in each page's footer `快速链接` section, add:
```html
<li><a href="reference-list.html">参考文献</a></li>
```

- [ ] **Step 4: Verify** — Open `reference-list.html` in browser, confirm nav works, scroll animation triggers, all references display with hanging indent.

- [ ] **Step 5: Commit**

```bash
git add reference-list.html css/style.css index.html about.html sdgs.html carbon-footprint.html act-now.html
git commit -m "feat: add APA 7th reference list page and nav links"
```

---

### Task 2: Update `index.html` — "Why the world needs SDGs" + full 17-goal grid

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Add "Why SDGs" section after stats-section**

Insert after the closing `</section>` of `.stats-section` and before `.sdg-highlights`:

```html
    <!-- ====== WHY SDGs ====== -->
    <section class="why-sdgs-section">
      <div class="container container-narrow">
        <h2 class="section-title">世界为何需要联合国可持续发展目标的指引</h2>
        <div class="why-sdgs-content">
          <div class="why-sdgs-card">
            <p>当今世界面临着前所未有的全球性挑战。气候变化导致极端天气事件频发，全球平均气温已比工业革命前上升约1.1°C，若不采取行动，到2100年可能上升2.7°C以上（IPCC, 2023）。与此同时，全球仍有超过7亿人生活在极端贫困中，每天生活费不足2.15美元（联合国, 2023）。这些挑战不是单一国家能够独立解决的——因为它们超越了国界，影响着地球上的每一个生命。</p>
          </div>
          <div class="why-sdgs-card">
            <p>联合国可持续发展目标（SDGs）为全球社会提供了统一的行动框架。与以往的倡议不同，SDGs认识到经济发展、社会包容和环境保护是不可分割的整体——正如SDG 1（消除贫困）与SDG 4（优质教育）和SDG 8（体面工作）相互关联，气候行动（SDG 13）与清洁能源（SDG 7）和可持续城市（SDG 11）密不可分（Sachs et al., 2023）。这种系统性思维确保解决一个问题时不会加剧另一个问题。</p>
          </div>
          <div class="why-sdgs-card">
            <p>没有SDGs的指引，全球发展将面临方向不一、资源分散、重复努力的风险。可持续发展目标提供了明确的指标和时间表——169项具体目标和232项指标——让各国政府、企业、民间组织和个人能够协调行动，衡量进展（联合国, 2015）。更重要的是，SDGs不落下任何人（Leave No One Behind）的核心承诺确保了发展的成果能够惠及最脆弱的群体。</p>
          </div>
        </div>
      </div>
    </section>
```

- [ ] **Step 2: Expand SDG highlights to full 17-goal grid**

Replace the existing `.sdg-grid` (6 cards) inside `.sdg-highlights` with:

```html
        <div class="sdg-grid">
          <div class="sdg-card" style="--sdg-color:#e5243b"><span class="sdg-card-number">01</span><h3>消除贫困</h3><p>No Poverty — 在世界各地消除一切形式的贫困</p></div>
          <div class="sdg-card" style="--sdg-color:#dda63a"><span class="sdg-card-number">02</span><h3>零饥饿</h3><p>Zero Hunger — 消除饥饿，实现粮食安全</p></div>
          <div class="sdg-card" style="--sdg-color:#4c9f38"><span class="sdg-card-number">03</span><h3>良好健康与福祉</h3><p>Good Health — 确保健康的生活方式</p></div>
          <div class="sdg-card" style="--sdg-color:#c5192d"><span class="sdg-card-number">04</span><h3>优质教育</h3><p>Quality Education — 确保包容公平的优质教育</p></div>
          <div class="sdg-card" style="--sdg-color:#ff3a21"><span class="sdg-card-number">05</span><h3>性别平等</h3><p>Gender Equality — 实现性别平等，增强妇女权能</p></div>
          <div class="sdg-card" style="--sdg-color:#26bde2"><span class="sdg-card-number">06</span><h3>清洁饮水与卫生设施</h3><p>Clean Water — 确保清洁饮水和卫生设施</p></div>
          <div class="sdg-card" style="--sdg-color:#fcc30b"><span class="sdg-card-number">07</span><h3>廉价清洁能源</h3><p>Affordable Energy — 确保现代可持续能源</p></div>
          <div class="sdg-card" style="--sdg-color:#a21942"><span class="sdg-card-number">08</span><h3>体面工作与经济增长</h3><p>Decent Work — 促进包容可持续的经济增长</p></div>
          <div class="sdg-card" style="--sdg-color:#fd6925"><span class="sdg-card-number">09</span><h3>产业、创新与基础设施</h3><p>Industry & Innovation — 建设韧性基础设施</p></div>
          <div class="sdg-card" style="--sdg-color:#dd1367"><span class="sdg-card-number">10</span><h3>减少不平等</h3><p>Reduced Inequalities — 减少国家内外的不平等</p></div>
          <div class="sdg-card" style="--sdg-color:#fd9d24"><span class="sdg-card-number">11</span><h3>可持续城市和社区</h3><p>Sustainable Cities — 建设包容安全的城市</p></div>
          <div class="sdg-card" style="--sdg-color:#bf8b2e"><span class="sdg-card-number">12</span><h3>负责任消费和生产</h3><p>Responsible Consumption — 确保可持续消费模式</p></div>
          <div class="sdg-card" style="--sdg-color:#3f7e44"><span class="sdg-card-number">13</span><h3>气候行动</h3><p>Climate Action — 采取紧急行动应对气候变化</p></div>
          <div class="sdg-card" style="--sdg-color:#009444"><span class="sdg-card-number">14</span><h3>水下生物</h3><p>Life Below Water — 保护海洋和海洋资源</p></div>
          <div class="sdg-card" style="--sdg-color:#00a651"><span class="sdg-card-number">15</span><h3>陆地生物</h3><p>Life on Land — 保护陆地生态系统</p></div>
          <div class="sdg-card" style="--sdg-color:#19489d"><span class="sdg-card-number">16</span><h3>和平、正义与强大机构</h3><p>Peace & Justice — 促进和平包容的社会</p></div>
          <div class="sdg-card" style="--sdg-color:#192841"><span class="sdg-card-number">17</span><h3>促进目标实现的伙伴关系</h3><p>Partnerships — 重振可持续发展全球伙伴关系</p></div>
        </div>
```

- [ ] **Step 3: Add GSAP animation for new sections**

Add to the existing `DOMContentLoaded` script block in `index.html`, after the carbon-content animation:

```javascript
      gsap.fromTo('.why-sdgs-card', { y: 48, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, stagger: 0.12, ease: 'power3.out', scrollTrigger: { trigger: '.why-sdgs-section', start: 'top 85%' } });
```

- [ ] **Step 4: Add CSS for why-sdgs section**

Append to `css/style.css`:

```css
/* ============================================================
   WHY SDGs SECTION (Home page)
   ============================================================ */
.why-sdgs-section { padding: 72px 0; background: var(--cream); border-top: 1px solid var(--border-light); }

.why-sdgs-content { display: flex; flex-direction: column; gap: 20px; }

.why-sdgs-card {
  background: #fff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-lg);
  padding: 32px 28px;
  transition: all 0.3s var(--ease-out);
}
.why-sdgs-card:hover {
  box-shadow: var(--shadow-lg);
  border-color: transparent;
}
.why-sdgs-card p {
  color: var(--text-muted);
  line-height: 1.85;
  font-size: 1.02rem;
  margin: 0;
}
```

- [ ] **Step 5: Verify** — Open `index.html`, check "Why SDGs" section renders between stats and SDG highlights, all 17 SDG cards display in grid, GSAP scroll animations fire on scroll.

- [ ] **Step 6: Commit**

```bash
git add index.html css/style.css
git commit -m "feat: add Why SDGs section and full 17-goal grid to home page"
```

---

### Task 3: Restructure `about.html` — team member cards

**Files:**
- Modify: `about.html`
- Modify: `css/style.css` (add `.member-card-v2` styles)

- [ ] **Step 1: Add CSS for expanded team cards**

Append to `css/style.css`:

```css
/* ============================================================
   ABOUT PAGE — Expanded Team Cards
   ============================================================ */
.team-card-v2 {
  background: #fff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-lg);
  padding: 0;
  text-align: center;
  overflow: hidden;
  transition: all 0.35s var(--ease-out);
}
.team-card-v2:hover {
  box-shadow: var(--shadow-lg);
  border-color: transparent;
  transform: translateY(-4px);
}

.team-card-v2 .card-accent-bar {
  height: 4px;
  background: linear-gradient(90deg, var(--terracotta), var(--sage));
  transition: opacity 0.3s ease;
}

.team-card-v2 .card-body { padding: 32px 24px 28px; }

.team-card-v2 .avatar-icon {
  width: 72px; height: 72px;
  margin: 0 auto 16px;
  display: block;
}

.team-card-v2 .member-name {
  font-family: var(--font-display);
  font-size: 1.2rem;
  color: var(--ink);
  margin-bottom: 6px;
}

.team-card-v2 .member-role {
  display: inline-block;
  font-size: 0.75rem; font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--terracotta);
  background: rgba(196,139,92,0.08);
  padding: 3px 12px;
  border-radius: 100px;
  margin-bottom: 20px;
}

.team-card-v2 .member-divider {
  width: 40px; height: 1px;
  background: var(--border-light);
  margin: 0 auto 18px;
}

.team-card-v2 .member-field {
  text-align: left;
  margin-bottom: 12px;
}
.team-card-v2 .member-field:last-child { margin-bottom: 0; }

.team-card-v2 .field-label {
  display: block;
  font-size: 0.72rem; font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--text-light);
  margin-bottom: 4px;
}

.team-card-v2 .field-value {
  color: var(--text);
  font-size: 0.95rem;
  line-height: 1.6;
}
```

- [ ] **Step 2: Replace team-grid content in `about.html`**

Replace the contents of `<div class="team-grid">` with:

```html
          <!-- Member 1: 张 -->
          <div class="team-card-v2">
            <div class="card-accent-bar"></div>
            <div class="card-body">
              <svg viewBox="0 0 100 100" class="avatar-icon">
                <defs><linearGradient id="a1" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#c48b5c"/><stop offset="100%" stop-color="#8b7355"/></linearGradient></defs>
                <circle cx="50" cy="50" r="48" fill="url(#a1)"/>
                <circle cx="50" cy="38" r="14" fill="white" opacity="0.9"/>
                <ellipse cx="50" cy="72" rx="24" ry="14" fill="white" opacity="0.6"/>
                <text x="50" y="46" text-anchor="middle" fill="#8b7355" font-size="12" font-family="Georgia,serif">Photo</text>
              </svg>
              <h3 class="member-name">张明</h3>
              <span class="member-role">项目负责人</span>
              <div class="member-divider"></div>
              <div class="member-field"><span class="field-label">个人背景</span><span class="field-value">环境科学专业本科三年级学生，拥有两年环保志愿者经历，参与过多项校园可持续发展项目。对生态系统保护和环境政策有浓厚兴趣。</span></div>
              <div class="member-field"><span class="field-label">未来职业目标</span><span class="field-value">希望成为一名环境政策顾问，致力于为中国乃至全球的可持续发展政策制定提供科学依据，推动绿色低碳转型。</span></div>
            </div>
          </div>

          <!-- Member 2: 李 -->
          <div class="team-card-v2">
            <div class="card-accent-bar"></div>
            <div class="card-body">
              <svg viewBox="0 0 100 100" class="avatar-icon">
                <defs><linearGradient id="a2" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#5c8d6d"/><stop offset="100%" stop-color="#2d4a3e"/></linearGradient></defs>
                <circle cx="50" cy="50" r="48" fill="url(#a2)"/>
                <circle cx="50" cy="38" r="14" fill="white" opacity="0.9"/>
                <ellipse cx="50" cy="72" rx="24" ry="14" fill="white" opacity="0.6"/>
                <text x="50" y="46" text-anchor="middle" fill="#2d4a3e" font-size="12" font-family="Georgia,serif">Photo</text>
              </svg>
              <h3 class="member-name">李华</h3>
              <span class="member-role">技术开发</span>
              <div class="member-divider"></div>
              <div class="member-field"><span class="field-label">个人背景</span><span class="field-value">计算机科学与技术专业学生，擅长Web开发与数据分析。曾参与多个开源项目，对利用技术创新解决环境问题充满热情。</span></div>
              <div class="member-field"><span class="field-label">未来职业目标</span><span class="field-value">希望成为一名绿色科技创业者，开发数字化工具帮助个人和企业量化并减少碳排放，用技术的力量推动气候行动。</span></div>
            </div>
          </div>

          <!-- Member 3: 王 -->
          <div class="team-card-v2">
            <div class="card-accent-bar"></div>
            <div class="card-body">
              <svg viewBox="0 0 100 100" class="avatar-icon">
                <defs><linearGradient id="a3" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#2c5282"/><stop offset="100%" stop-color="#1a365d"/></linearGradient></defs>
                <circle cx="50" cy="50" r="48" fill="url(#a3)"/>
                <circle cx="50" cy="38" r="14" fill="white" opacity="0.9"/>
                <ellipse cx="50" cy="72" rx="24" ry="14" fill="white" opacity="0.6"/>
                <text x="50" y="46" text-anchor="middle" fill="#1a365d" font-size="12" font-family="Georgia,serif">Photo</text>
              </svg>
              <h3 class="member-name">王芳</h3>
              <span class="member-role">政策研究</span>
              <div class="member-divider"></div>
              <div class="member-field"><span class="field-label">个人背景</span><span class="field-value">国际关系专业学生，专注于国际环境治理和多边合作机制研究。曾在国际NGO组织实习，参与水资源保护项目的政策分析工作。</span></div>
              <div class="member-field"><span class="field-label">未来职业目标</span><span class="field-value">希望加入联合国环境规划署（UNEP）或相关国际组织，参与全球环境治理，推动跨国水资源管理与保护合作。</span></div>
            </div>
          </div>

          <!-- Member 4: 陈 -->
          <div class="team-card-v2">
            <div class="card-accent-bar"></div>
            <div class="card-body">
              <svg viewBox="0 0 100 100" class="avatar-icon">
                <defs><linearGradient id="a4" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#b8573e"/><stop offset="100%" stop-color="#6b3020"/></linearGradient></defs>
                <circle cx="50" cy="50" r="48" fill="url(#a4)"/>
                <circle cx="50" cy="38" r="14" fill="white" opacity="0.9"/>
                <ellipse cx="50" cy="72" rx="24" ry="14" fill="white" opacity="0.6"/>
                <text x="50" y="46" text-anchor="middle" fill="#6b3020" font-size="12" font-family="Georgia,serif">Photo</text>
              </svg>
              <h3 class="member-name">陈伟</h3>
              <span class="member-role">数据分析师</span>
              <div class="member-divider"></div>
              <div class="member-field"><span class="field-label">个人背景</span><span class="field-value">统计学与数据科学专业学生，擅长环境数据分析与可视化。参与过海洋塑料污染的研究项目，利用数据建模预测污染扩散趋势。</span></div>
              <div class="member-field"><span class="field-label">未来职业目标</span><span class="field-value">希望成为一名环境数据科学家，利用大数据和人工智能技术为海洋保护和生态系统管理提供数据驱动的决策支持。</span></div>
            </div>
          </div>
```

- [ ] **Step 3: Update GSAP animation in `about.html`**

Replace the existing team-card animation line:
```javascript
gsap.fromTo('.team-card', { y: 56, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, stagger: 0.1, ease: 'power3.out', scrollTrigger: { trigger: '.team-grid', start: 'top 85%' } });
```
with:
```javascript
gsap.fromTo('.team-card-v2', { y: 56, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, stagger: 0.1, ease: 'power3.out', scrollTrigger: { trigger: '.team-grid', start: 'top 85%' } });
```

- [ ] **Step 4: Verify** — Open `about.html`, check each team card shows: photo placeholder SVG, name, background, and future aspiration fields. Cards hover with shadow and lift effect.

- [ ] **Step 5: Commit**

```bash
git add about.html css/style.css
git commit -m "feat: restructure about page team cards with photo/bg/aspiration fields"
```

---

### Task 4: Update `sdgs.html` — add 4 member SDG research reports

**Files:**
- Modify: `sdgs.html`
- Modify: `css/style.css` (add `.sdg-report-card` styles)

- [ ] **Step 1: Add CSS for SDG report cards**

Append to `css/style.css`:

```css
/* ============================================================
   SDG MEMBER RESEARCH REPORTS
   ============================================================ */
.sdg-research-section { padding: 72px 0; background: #fff; border-top: 1px solid var(--border-light); }

.sdg-report-card {
  background: var(--cream);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-lg);
  padding: 32px;
  margin-bottom: 24px;
  transition: all 0.3s var(--ease-out);
}
.sdg-report-card:last-child { margin-bottom: 0; }
.sdg-report-card:hover {
  box-shadow: var(--shadow-lg);
  border-color: transparent;
}

.sdg-report-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 24px;
  padding-bottom: 20px;
  border-bottom: 1px solid var(--border-light);
}

.sdg-report-avatar {
  width: 52px; height: 52px;
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  color: #fff; font-weight: 700; font-size: 1.2rem;
  font-family: var(--font-display);
  flex-shrink: 0;
}

.sdg-report-info h3 {
  font-family: var(--font-display);
  color: var(--ink);
  margin-bottom: 2px;
  font-size: 1.1rem;
}
.sdg-report-sdg {
  font-size: 0.85rem; font-weight: 500;
}

.sdg-report-body h4 {
  font-family: var(--font-display);
  font-size: 1.05rem;
  color: var(--ink);
  margin: 20px 0 10px;
  padding-left: 12px;
  border-left: 3px solid var(--terracotta);
}
.sdg-report-body h4:first-child { margin-top: 0; }

.sdg-report-body p {
  color: var(--text-muted);
  line-height: 1.85;
  margin-bottom: 14px;
  font-size: 0.95rem;
}
.sdg-report-body p:last-child { margin-bottom: 0; }

.sdg-report-body .citation {
  font-size: 0.85rem;
  color: var(--text-light);
  font-style: italic;
}
```

- [ ] **Step 2: Add member research section to `sdgs.html`**

Insert after the closing `</section>` of `.sdgs-intro` and before the modal div:

```html
    <!-- Member SDG Research Reports -->
    <section class="sdg-research-section">
      <div class="container container-narrow">
        <h2 class="section-title">成员SDG调研报告</h2>
        <p class="section-intro">每位团队成员选择一项不同的可持续发展目标进行深入研究，分析该目标相关的社会问题并提出解决方案。</p>

        <!-- Member 1: 张明 — SDG 4: Quality Education -->
        <div class="sdg-report-card">
          <div class="sdg-report-header">
            <div class="sdg-report-avatar" style="background:#c5192d">张</div>
            <div class="sdg-report-info">
              <h3>张明</h3>
              <span class="sdg-report-sdg" style="color:#c5192d">SDG 4 · 优质教育 — Quality Education</span>
            </div>
          </div>
          <div class="sdg-report-body">
            <h4>一、SDG 4的核心目的</h4>
            <p>可持续发展目标4（SDG 4）旨在"确保包容和公平的优质教育，让全民终身享有学习机会"（联合国, 2015）。其核心使命是到2030年，确保所有男女儿童完成免费、公平和优质的初等和中等教育，取得相关和有效的学习成果。SDG 4特别关注教育公平——消除性别差距、城乡差距和贫富差距，确保包括残疾儿童、原住民儿童和处于脆弱环境中的儿童在内的所有人都能平等获得教育机会。此外，SDG 4强调教育的质量而不仅仅是入学率，要求学习者通过教育获得可持续发展所需的知识和技能（UNESCO, 2023）。</p>

            <h4>二、教育不平等：中国农村地区面临的不利影响</h4>
            <p>在中国，尽管九年义务教育普及率已超过95%，但城乡教育资源分配不均的问题依然严峻。根据中国教育部2023年的统计数据，农村地区学校的生均教育经费仅为城市学校的约60%，优质教师资源严重向城市集中——农村地区持有本科及以上学历的教师比例比城市低约25个百分点（OECD, 2023）。这一问题主要影响农村地区的学龄儿童和青少年，特别是留守儿童群体。</p>
            <p>造成这一问题的原因是多方面的：首先，长期以来的城乡二元经济结构导致教育资源向经济发达地区倾斜；其次，农村地区经济发展水平较低，地方政府教育投入能力有限；第三，优质教师因薪酬待遇和职业发展空间有限而不愿到农村任教。这一问题自20世纪90年代市场经济改革加速以来日益显著，在西部农村地区尤为严重。</p>
            <p>教育不平等对社会造成深远的不利影响。缺乏优质教育限制了农村儿童的发展机会，导致贫困的代际传递——未受良好教育的儿童成年后更可能从事低收入工作，其子女又面临同样的教育困境（联合国开发计划署, 2023）。从国家层面看，教育不平等削弱了人力资本积累，制约了经济转型升级和区域协调发展。</p>

            <h4>三、推动改变：从教育困境走向教育繁荣的行动方案</h4>
            <p>为改善中国农村教育不平等问题，实现从"教育困境"到"教育繁荣"的转变，需要采取以下综合治理方案：</p>
            <p><strong>1. 数字教育基础设施建设：</strong>推动农村学校全面接入高速互联网，配备智能教学设备，利用在线教育平台将城市优质课程资源引入农村课堂。同时，为农村教师提供数字教学技能培训，确保技术设备得到有效利用。这一措施可以低成本、高效率地缩小城乡教育资源差距。</p>
            <p><strong>2. 农村教师激励计划：</strong>建立农村教师专项补贴制度，为到农村任教的教师提供额外薪酬补贴、住房保障和职业发展快速通道。借鉴"特岗教师计划"的成功经验，扩大覆盖范围并提高待遇标准。同时，建立城乡教师交流轮岗制度，促进优质师资的双向流动。</p>
            <p><strong>3. 社区参与式教育支持网络：</strong>动员社区力量参与教育支持——建立农村课后辅导志愿者网络，由返乡大学生和社区知识青年为留守儿童提供学业辅导和成长陪伴。设立社区教育基金，为贫困家庭学生提供助学金和学习资源。通过赋权社区，构建可持续的本地化教育支持体系。</p>

            <p class="citation">参考文献：联合国 (2015). 变革我们的世界：2030年可持续发展议程. | UNESCO (2023). 全球教育监测报告. | OECD (2023). 教育概览2023. | 联合国开发计划署 (2023). 2023年人类发展报告.</p>
          </div>
        </div>

        <!-- Member 2: 李华 — SDG 13: Climate Action -->
        <div class="sdg-report-card">
          <div class="sdg-report-header">
            <div class="sdg-report-avatar" style="background:#3f7e44">李</div>
            <div class="sdg-report-info">
              <h3>李华</h3>
              <span class="sdg-report-sdg" style="color:#3f7e44">SDG 13 · 气候行动 — Climate Action</span>
            </div>
          </div>
          <div class="sdg-report-body">
            <h4>一、SDG 13的核心目的</h4>
            <p>可持续发展目标13（SDG 13）要求"采取紧急行动应对气候变化及其影响"。气候变化是全球性的挑战，影响到每个国家、每个社区和每个人。SDG 13的核心目标包括：加强所有国家应对气候相关灾害和自然灾害的韧性和适应能力；将气候变化措施纳入国家政策、战略和规划；改善关于气候变化的教育、提高认识以及人和机构在减缓、适应和减少影响方面的能力（联合国, 2015）。这一目标与《巴黎协定》紧密对接，后者设定了将全球变暖控制在远低于2°C、努力限制在1.5°C的目标。</p>

            <h4>二、气候变化对中国沿海城市的影响</h4>
            <p>中国沿海地区正面临着气候变化带来的严峻挑战，其中最突出的是海平面上升和极端天气事件频发。根据中国自然资源部2023年发布的《中国海平面公报》，1980年至2022年间，中国沿海海平面以年均3.5毫米的速度上升，高于全球平均水平。上海、天津、广州等沿海特大城市面临着日益加剧的洪涝风险（IPCC, 2023）。</p>
            <p>造成这一不利局面的原因包括：全球温室气体排放持续增加导致气候变暖、冰川融化和海水热膨胀；中国沿海地区快速的城市化进程增加了暴露于气候风险的人口和资产规模；部分城市的防洪基础设施老化，难以应对日益频繁的极端天气事件。受影响的群体包括沿海城市居民（特别是低收入社区）、依赖沿海渔业和旅游业的从业者，以及沿海生态系统。</p>
            <p>气候变化对沿海城市的不利影响是多维度的。在经济层面，洪涝灾害造成巨额财产损失——仅2022年，中国因气象灾害造成的直接经济损失就超过3000亿元人民币。社会层面，极端天气威胁居民生命安全，破坏正常生活秩序。生态层面，海平面上升导致海岸侵蚀加剧、湿地退化和生物多样性丧失（UNEP, 2023）。</p>

            <h4>三、推动改变：从气候脆弱性到气候韧性的行动方案</h4>
            <p>为应对沿海城市的气候变化挑战，推动从"气候脆弱性"到"气候韧性"的转变，需要采取以下行动：</p>
            <p><strong>1. 建设基于自然的防护基础设施：</strong>推广"海绵城市"理念，通过保护和恢复沿海湿地、红树林和珊瑚礁等自然生态系统，构建绿色海岸防护带。与传统混凝土堤坝相比，基于自然的解决方案成本更低、可持续性更强，同时还能提供生物多样性保护和碳汇等协同效益。</p>
            <p><strong>2. 建立城市级气候风险预警与应急响应体系：</strong>利用大数据、人工智能和物联网技术，建设智能化的气候风险监测预警平台。整合气象、水文、地理信息等多源数据，实现洪水、台风等灾害的精准预测和快速响应。同时，定期组织社区应急演练，提升公众防灾减灾意识和自救互救能力。</p>
            <p><strong>3. 推动沿海城市产业绿色转型：</strong>制定沿海城市碳排放达峰和碳中和路线图，加速能源结构转型——大力发展海上风电、潮汐能等海洋可再生能源。对高碳产业实施严格的排放限制，同时通过财政补贴和税收优惠鼓励企业投资清洁技术和循环经济模式。</p>

            <p class="citation">参考文献：联合国 (2015). 巴黎协定. | IPCC (2023). 第六次评估报告. | UNEP (2023). 排放差距报告2023. | 中国自然资源部 (2023). 中国海平面公报.</p>
          </div>
        </div>

        <!-- Member 3: 王芳 — SDG 6: Clean Water -->
        <div class="sdg-report-card">
          <div class="sdg-report-header">
            <div class="sdg-report-avatar" style="background:#26bde2">王</div>
            <div class="sdg-report-info">
              <h3>王芳</h3>
              <span class="sdg-report-sdg" style="color:#26bde2">SDG 6 · 清洁饮水与卫生设施 — Clean Water</span>
            </div>
          </div>
          <div class="sdg-report-body">
            <h4>一、SDG 6的核心目的</h4>
            <p>可持续发展目标6（SDG 6）旨在"确保人人享有清洁饮水和卫生设施，并对水资源进行可持续管理"。水是生命之源，也是社会经济发展和生态系统健康的基础。SDG 6的具体目标包括：到2030年实现人人普遍和公平地获得安全和负担得起的饮用水；实现人人享有充足和公平的环境卫生和个人卫生；改善水质，减少污染；提高所有部门的用水效率，确保淡水的可持续提取和供应（联合国, 2015）。</p>

            <h4>二、水资源短缺与水污染：中国北方地区面临的挑战</h4>
            <p>中国北方地区长期面临严重的水资源短缺和水污染问题。根据中国水利部2023年发布的数据，中国北方地区人均水资源量仅为全国平均水平的约三分之一，低于国际公认的"极度缺水"标准。与此同时，华北平原的地下水超采问题严重——过去50年间，该地区地下水位平均下降了10至30米，形成了世界上最大的地下水漏斗区。</p>
            <p>造成这一问题的原因是多方面的：自然条件方面，北方地区降水稀少且时空分布不均；人为因素方面，快速工业化和城市化导致用水需求激增；农业生产中的大水漫灌方式浪费严重；工业废水和生活污水未经充分处理排入河流，造成严重的水污染——海河、淮河等北方主要河流的污染负荷长期居高不下（联合国, 2023）。受影响最大的人群是农村地区的居民，他们不仅面临饮用水安全风险，还因缺水而制约了农业生产和经济发展。</p>
            <p>水资源短缺对社会和经济造成了广泛的不利影响。农业方面，缺水导致粮食减产，威胁国家粮食安全；工业方面，水供应不足限制产业发展；生态方面，河流断流、湿地萎缩和地面沉降等生态灾难频发；社会方面，水污染导致的健康问题给公共卫生系统带来沉重负担（WHO, 2022）。</p>

            <h4>三、推动改变：从水危机到水安全的行动方案</h4>
            <p>为解决中国北方水资源短缺和水污染问题，推动从"水危机"到"水安全"的转变，需要实施以下综合治理方案：</p>
            <p><strong>1. 全面推进农业节水革命：</strong>在北方粮食主产区推广滴灌、喷灌等高效节水灌溉技术，替代传统的大水漫灌方式。建立农业用水计量和阶梯水价制度，以经济激励促进节水。推动种植结构调整，在缺水地区减少高耗水作物种植面积，发展旱作农业和耐旱作物品种。</p>
            <p><strong>2. 构建城乡一体化的水循环利用体系：</strong>投资建设现代化的污水处理和再生水回用设施，将处理后的再生水用于工业冷却、城市绿化、农业灌溉和河道生态补水。在新城区推广"海绵城市"建设，通过雨水收集和渗透系统补充地下水资源。</p>
            <p><strong>3. 实施流域综合管理与生态修复工程：</strong>打破行政区划壁垒，建立以流域为单位的水资源统一管理机制。实施南水北调等跨流域调水工程的科学调度。开展河流生态修复，恢复湿地和河岸植被，提升流域生态系统的水源涵养和自净能力。同时，加强地下水补给，逐步恢复地下水位的可持续水平。</p>

            <p class="citation">参考文献：联合国 (2023). 世界水资源开发报告. | WHO (2022). 饮用水水质指南. | 中国水利部 (2023). 中国水资源公报.</p>
          </div>
        </div>

        <!-- Member 4: 陈伟 — SDG 14: Life Below Water -->
        <div class="sdg-report-card">
          <div class="sdg-report-header">
            <div class="sdg-report-avatar" style="background:#009444">陈</div>
            <div class="sdg-report-info">
              <h3>陈伟</h3>
              <span class="sdg-report-sdg" style="color:#009444">SDG 14 · 水下生物 — Life Below Water</span>
            </div>
          </div>
          <div class="sdg-report-body">
            <h4>一、SDG 14的核心目的</h4>
            <p>可持续发展目标14（SDG 14）旨在"保护和可持续利用海洋及海洋资源，促进可持续发展"。海洋覆盖了地球表面的71%，为30多亿人提供生计来源，吸收了约30%的人为二氧化碳排放，在调节全球气候中发挥着不可替代的作用。SDG 14的核心目标包括：到2025年预防和大幅减少各类海洋污染，特别是陆源污染；可持续管理和保护海洋与沿海生态系统；最大限度地减少海洋酸化的影响；有效规范捕捞活动，终止过度捕捞（联合国, 2015）。</p>

            <h4>二、海洋塑料污染：东南亚海域面临的生态危机</h4>
            <p>南海及周边东南亚海域正面临着严重的塑料污染危机。根据联合国环境规划署（UNEP, 2023）的报告，东南亚地区是全球海洋塑料污染的主要来源之一——印度尼西亚、菲律宾、越南、泰国和中国每年向海洋排放的塑料垃圾估计超过200万吨。这些塑料垃圾不仅覆盖了海面和海滩，还通过食物链进入海洋生物体内，最终影响人类健康。</p>
            <p>造成这一危机的原因包括：东南亚地区快速城市化过程中垃圾管理基础设施严重不足；新冠疫情期间一次性塑料用品消耗量激增；公众环保意识薄弱，随意丢弃垃圾的习惯普遍存在；渔业活动中废弃渔具（"幽灵网"）的大量遗弃。受影响的对象广泛：海洋生物因误食塑料或缠绕而死亡——全球超过800种海洋物种受到塑料污染影响；依赖海洋旅游和渔业的沿海社区经济损失惨重；食用受微塑料污染的海产品对人类健康的长期影响仍在研究中（WWF, 2022）。</p>
            <p>海洋塑料污染对生态系统和经济都造成了深远的不利影响。生态系统层面，塑料分解成微塑料后被浮游生物吸收，沿食物链逐级累积，最终影响整个海洋生态系统的健康。经济层面，塑料污染每年对全球海洋生态系统服务造成的损失估计高达130亿美元。社会层面，污染破坏了依赖健康海洋环境的旅游业和渔业的可持续发展前景。</p>

            <h4>三、推动改变：从海洋污染到蓝色复苏的行动方案</h4>
            <p>为应对东南亚海域的塑料污染危机，推动从"海洋污染"到"蓝色复苏"的转变，需要实施以下行动方案：</p>
            <p><strong>1. 建立区域海洋塑料垃圾监测与清理网络：</strong>利用卫星遥感和人工智能技术，建立南海及周边海域塑料垃圾动态监测系统。组织沿海社区渔民参与"渔业垃圾回收"计划，为回收海洋塑料垃圾的渔船提供经济补贴。部署太阳能驱动的海洋塑料回收装置（如"海洋垃圾桶"），在河流入海口拦截塑料垃圾。</p>
            <p><strong>2. 推动塑料循环经济与替代材料研发：</strong>在沿海地区建立塑料垃圾分类回收和再生利用产业链，对塑料瓶、渔网等可回收物进行高值化利用。通过立法限制一次性塑料制品的生产和使用，同时对使用可降解替代材料的企业给予税收优惠。支持海洋可降解生物材料（如海藻基塑料）的研发和产业化。</p>
            <p><strong>3. 开展区域合作与公众教育行动：</strong>推动建立中国-东盟海洋环境保护合作机制，共同制定和实施区域海洋塑料污染防治行动计划。在学校和社区开展"无塑海洋"教育活动，利用社交媒体和公众人物影响力提升公众环保意识。组织定期的海滩清洁志愿者活动，让更多公众亲身参与海洋保护行动。</p>

            <p class="citation">参考文献：UNEP (2023). 排放差距报告. | WWF (2022). 地球生命力报告. | 联合国 (2015). 2030年可持续发展议程.</p>
          </div>
        </div>

      </div>
    </section>
```

- [ ] **Step 3: Add GSAP animations for report cards**

Add to the `DOMContentLoaded` script in `sdgs.html`:

```javascript
      gsap.fromTo('.sdg-report-card', { y: 56, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, stagger: 0.12, ease: 'power3.out', scrollTrigger: { trigger: '.sdg-research-section', start: 'top 90%' } });
```

- [ ] **Step 4: Verify** — Open `sdgs.html`, scroll to member reports section, verify all 4 reports render, GSAP scroll animations work, content is properly formatted.

- [ ] **Step 5: Commit**

```bash
git add sdgs.html css/style.css
git commit -m "feat: add 4 member SDG research reports to sdgs page"
```

---

### Task 5: Upgrade `carbon-footprint.html` calculator

**Files:**
- Modify: `carbon-footprint.html`
- Modify: `js/carbon.js`

- [ ] **Step 1: Replace calculator form HTML in `carbon-footprint.html`**

Replace the existing `<div class="calculator-form">` with:

```html
        <div class="calculator-form" id="calculatorForm">
          <h2>碳足迹计算器 — 家庭 · 交通 · 生活方式</h2>
          <p style="text-align:center;color:var(--text-muted);margin-bottom:32px;">填写以下信息，计算您的个人年度碳足迹</p>

          <div class="form-section">
            <h3>🏠 家庭信息</h3>
            <div class="form-row">
              <div class="form-group form-half"><label for="householdSize">家庭人数</label><input type="number" id="householdSize" placeholder="例如：4" min="1" max="20"></div>
              <div class="form-group form-half"><label for="housingType">住房类型</label><select id="housingType"><option value="">请选择</option><option value="detached">独立住宅</option><option value="semi">联排住宅</option><option value="apartment">公寓</option><option value="studio">单间/小户型</option></select></div>
            </div>
            <div class="form-row">
              <div class="form-group form-half"><label for="housingSize">住房面积（平方米）</label><input type="number" id="housingSize" placeholder="例如：90" min="10" max="1000"></div>
              <div class="form-group form-half"><label for="electricity">每月用电量（千瓦时）</label><input type="number" id="electricity" placeholder="例如：300" min="0"></div>
            </div>
            <div class="form-group"><label for="heating">冬季供暖方式</label><select id="heating"><option value="">请选择</option><option value="gas">天然气供暖</option><option value="electric">电供暖</option><option value="coal">燃煤供暖</option><option value="district">集中供暖</option><option value="none">无供暖</option></select></div>
            <div class="form-group checkbox-group"><label><input type="checkbox" id="greenEnergy"><span>使用绿色能源/可再生能源</span></label></div>
          </div>

          <div class="form-section">
            <h3>🚗 交通出行</h3>
            <div class="form-group"><label for="carDistance">每周驾车里程（公里）</label><input type="number" id="carDistance" placeholder="例如：200" min="0"></div>
            <div class="form-group"><label for="carType">车辆类型</label><select id="carType"><option value="">请选择</option><option value="petrol_small">汽油车（小型，&lt;1.6L）</option><option value="petrol_medium">汽油车（中型，1.6-2.5L）</option><option value="petrol_large">汽油车（大型SUV，&gt;2.5L）</option><option value="diesel">柴油车</option><option value="hybrid">混合动力</option><option value="electric">纯电动</option></select></div>
            <div class="form-group"><label for="publicTransport">每周公共交通出行次数</label><input type="number" id="publicTransport" placeholder="例如：10" min="0"></div>
            <div class="form-row">
              <div class="form-group form-half"><label for="flightsShort">每年短途飞行次数（&lt;1500km）</label><input type="number" id="flightsShort" placeholder="0" min="0"></div>
              <div class="form-group form-half"><label for="flightsLong">每年长途飞行次数（&gt;1500km）</label><input type="number" id="flightsLong" placeholder="0" min="0"></div>
            </div>
          </div>

          <div class="form-section">
            <h3>🥗 生活方式与消费</h3>
            <div class="form-group"><label for="dietType">饮食类型</label><select id="dietType"><option value="">请选择</option><option value="vegan">纯素食</option><option value="vegetarian">素食（含蛋奶）</option><option value="pescatarian">鱼素（吃鱼不吃肉）</option><option value="lowMeat">低肉饮食（每周1-3次）</option><option value="mediumMeat">中等肉食（每天一次）</option><option value="highMeat">高肉饮食（每餐有肉）</option></select></div>
            <div class="form-group"><label for="localFood">本地食品消费比例（%）</label><input type="number" id="localFood" placeholder="例如：50" min="0" max="100"></div>
            <div class="form-row">
              <div class="form-group form-half"><label for="foodWaste">每周食物浪费（估算，公斤）</label><input type="number" id="foodWaste" placeholder="例如：2" min="0" step="0.5"></div>
              <div class="form-group form-half"><label for="clothingSpend">每月服装消费（元）</label><input type="number" id="clothingSpend" placeholder="例如：500" min="0"></div>
            </div>
            <div class="form-group checkbox-group"><label><input type="checkbox" id="recycling"><span>进行垃圾分类回收</span></label></div>
          </div>

          <button class="btn btn-primary btn-calculate" id="calculateBtn">📊 计算碳足迹</button>
        </div>
```

- [ ] **Step 2: Add external tool recommendation section**

Insert after the calculator-form div and before the result-section div:

```html
        <div class="external-tools" style="max-width:860px;margin:48px auto 0;padding:28px;background:#fff;border:1px solid var(--border-light);border-radius:var(--radius-lg);">
          <h3 style="font-family:var(--font-display);color:var(--ink);margin-bottom:16px;">🔗 推荐的外部碳足迹计算工具</h3>
          <p style="color:var(--text-muted);margin-bottom:16px;line-height:1.7;">以下为国际公认的碳足迹计算工具，可用于交叉验证计算结果并获取更详细的碳足迹分析。在评估提交中，请使用这些工具的截图作为计算过程证据。</p>
          <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;">
            <a href="https://offset.climateneutralnow.org/footprintcalc" target="_blank" rel="noopener" style="display:block;padding:16px;background:var(--cream);border:1px solid var(--border-light);border-radius:var(--radius-md);text-decoration:none;color:var(--ink);transition:all 0.3s ease;" onmouseover="this.style.borderColor='var(--terracotta)';this.style.boxShadow='var(--shadow-md)'" onmouseout="this.style.borderColor='var(--border-light)';this.style.boxShadow='none'">
              <strong style="color:var(--terracotta);">UN Carbon Footprint Calculator</strong>
              <p style="font-size:0.85rem;color:var(--text-muted);margin-top:4px;">联合国气候中和倡议官方计算器</p>
            </a>
            <a href="https://footprint.wwf.org.uk" target="_blank" rel="noopener" style="display:block;padding:16px;background:var(--cream);border:1px solid var(--border-light);border-radius:var(--radius-md);text-decoration:none;color:var(--ink);transition:all 0.3s ease;" onmouseover="this.style.borderColor='var(--terracotta)';this.style.boxShadow='var(--shadow-md)'" onmouseout="this.style.borderColor='var(--border-light)';this.style.boxShadow='none'">
              <strong style="color:var(--terracotta);">WWF Footprint Calculator</strong>
              <p style="font-size:0.85rem;color:var(--text-muted);margin-top:4px;">世界自然基金会碳足迹计算器</p>
            </a>
            <a href="https://www.carbonfootprint.com/calculator.aspx" target="_blank" rel="noopener" style="display:block;padding:16px;background:var(--cream);border:1px solid var(--border-light);border-radius:var(--radius-md);text-decoration:none;color:var(--ink);transition:all 0.3s ease;" onmouseover="this.style.borderColor='var(--terracotta)';this.style.boxShadow='var(--shadow-md)'" onmouseout="this.style.borderColor='var(--border-light)';this.style.boxShadow='none'">
              <strong style="color:var(--terracotta);">CarbonFootprint.com Calculator</strong>
              <p style="font-size:0.85rem;color:var(--text-muted);margin-top:4px;">国际碳足迹计算与抵消平台</p>
            </a>
          </div>
          <div class="screenshot-guide" style="margin-top:20px;padding:16px;background:#fffbeb;border:1px dashed #d97706;border-radius:var(--radius-md);">
            <p style="color:#92400e;font-size:0.9rem;margin:0;">📸 <strong>截图指引：</strong>使用上述工具计算碳足迹时，请截取每个步骤的屏幕截图（包括输入数据和计算结果），作为评估提交的证据。建议使用浏览器自带的截图工具或按 <kbd style="background:#fff;padding:1px 6px;border:1px solid #ccc;border-radius:3px;">Print Screen</kbd> 键。</p>
          </div>
        </div>
```

- [ ] **Step 3: Update `js/carbon.js` for advanced calculator**

Replace the entire content of `js/carbon.js` with:

```javascript
document.addEventListener('DOMContentLoaded', function() {
  const calculateBtn = document.getElementById('calculateBtn');
  const resetBtn = document.getElementById('resetBtn');
  const resultSection = document.getElementById('resultSection');
  const resultValue = document.getElementById('resultValue');
  const resultLevel = document.getElementById('resultLevel');
  const resultMessage = document.getElementById('resultMessage');
  const tipsList = document.getElementById('tipsList');

  function getVal(id) { var el = document.getElementById(id); return el ? (el.value || 0) : 0; }
  function isChecked(id) { var el = document.getElementById(id); return el ? el.checked : false; }
  function getSelect(id) { var el = document.getElementById(id); return el ? (el.value || '') : ''; }

  function calculateCarbonFootprint() {
    var total = 0;

    /* ---- Household ---- */
    var housingSize = parseFloat(getVal('housingSize')) || 90;
    var housingType = getSelect('housingType');
    var electricity = parseFloat(getVal('electricity')) || 300;
    var heating = getSelect('heating');
    var greenEnergy = isChecked('greenEnergy');

    // Housing emissions (kg CO₂/year per m²)
    var housingFactor = 20;
    if (housingType === 'apartment') housingFactor = 15;
    if (housingType === 'studio') housingFactor = 12;
    if (housingType === 'detached') housingFactor = 25;
    total += housingSize * housingFactor;

    // Electricity (kg CO₂ per kWh)
    var elecFactor = greenEnergy ? 0.1 : 0.6;
    total += electricity * 12 * elecFactor;

    // Heating
    if (heating === 'coal') total += 3000;
    else if (heating === 'gas') total += 2000;
    else if (heating === 'electric') total += 1500;
    else if (heating === 'district') total += 1000;

    /* ---- Transport ---- */
    var carDistance = parseFloat(getVal('carDistance')) || 0;
    var carType = getSelect('carType');
    var publicTransport = parseFloat(getVal('publicTransport')) || 0;
    var flightsShort = parseFloat(getVal('flightsShort')) || 0;
    var flightsLong = parseFloat(getVal('flightsLong')) || 0;

    // Car emissions (g CO₂ per km)
    var carFactors = {
      'petrol_small': 120, 'petrol_medium': 160, 'petrol_large': 220,
      'diesel': 140, 'hybrid': 90, 'electric': 40
    };
    var carFactor = carFactors[carType] || 150;
    total += carDistance * 52 * carFactor / 1000; // convert g to kg

    // Public transport (subway/bus per trip ~3kg)
    total += publicTransport * 52 * 3;

    // Flights
    total += flightsShort * 250; // ~250 kg CO₂ per short flight
    total += flightsLong * 900;  // ~900 kg CO₂ per long flight

    /* ---- Lifestyle ---- */
    var dietType = getSelect('dietType');
    var localFood = parseFloat(getVal('localFood')) || 50;
    var foodWaste = parseFloat(getVal('foodWaste')) || 2;
    var clothingSpend = parseFloat(getVal('clothingSpend')) || 500;
    var recycling = isChecked('recycling');

    // Diet emissions (kg CO₂/year)
    var dietFactors = {
      'vegan': 1000, 'vegetarian': 1500, 'pescatarian': 1800,
      'lowMeat': 2200, 'mediumMeat': 3000, 'highMeat': 4000
    };
    total += dietFactors[dietType] || 2500;

    // Local food bonus (up to 10% reduction)
    total *= (1 - (localFood / 100) * 0.1);

    // Food waste
    total += foodWaste * 52 * 2.5; // ~2.5 kg CO₂ per kg food waste

    // Clothing
    total += clothingSpend * 12 * 0.02; // ~0.02 kg CO₂ per yuan spent

    // Recycling
    if (!recycling) total += 500;

    return Math.round(total);
  }

  function getResultLevel(total) {
    if (total < 3000) return { level: '优秀', color: '#10b981', message: '您的碳足迹远低于全球平均水平（约4.7吨/年），与巴黎协定2°C目标路径一致。请继续保持！' };
    if (total < 5000) return { level: '良好', color: '#3b82f6', message: '您的碳足迹低于全球平均水平。距离2吨目标还有改善空间，继续努力！' };
    if (total < 8000) return { level: '一般', color: '#f59e0b', message: '您的碳足迹接近或略高于全球平均水平。建议采取更多减排措施。' };
    if (total < 12000) return { level: '较高', color: '#f97316', message: '您的碳足迹明显高于全球平均水平，需要采取积极的减排行动。' };
    return { level: '很高', color: '#ef4444', message: '您的碳足迹远高于全球平均水平。请立即采取行动，大幅减少碳排放。' };
  }

  function getTips() {
    var tips = [];
    var carDistance = parseFloat(getVal('carDistance')) || 0;
    var flightsShort = parseFloat(getVal('flightsShort')) || 0;
    var flightsLong = parseFloat(getVal('flightsLong')) || 0;
    var dietType = getSelect('dietType');
    var recycling = isChecked('recycling');
    var greenEnergy = isChecked('greenEnergy');

    if (carDistance > 150) tips.push('🚗 尝试每周减少驾车里程，使用公共交通、骑行或步行替代');
    if ((flightsShort + flightsLong) > 2) tips.push('✈️ 减少不必要的飞行，考虑视频会议替代商务出行');
    if (dietType === 'highMeat' || dietType === 'mediumMeat') tips.push('🥬 减少红肉消费，增加植物性食物比例——素食餐的碳足迹仅为肉食餐的1/3');
    if (!recycling) tips.push('♻️ 开始垃圾分类和资源回收——这是最容易实施的减排行动之一');
    if (!greenEnergy) tips.push('⚡ 考虑更换为绿色电力供应商或安装家庭太阳能系统');
    if (tips.length === 0) tips.push('🌍 您做得非常好！您的生活方式已经相当环保，请继续保持并影响身边的人。');
    return tips;
  }

  if (calculateBtn) {
    calculateBtn.addEventListener('click', function() {
      var result = calculateCarbonFootprint();
      var level = getResultLevel(result);
      var tips = getTips();

      resultValue.innerHTML = result.toLocaleString() + ' <span class="unit">kg CO₂/年</span>';
      resultValue.style.color = level.color;
      resultLevel.textContent = level.level;
      resultLevel.style.backgroundColor = level.color;
      resultMessage.textContent = level.message;

      // Comparison to 2-ton target
      var comparisonEl = document.getElementById('targetComparison');
      if (comparisonEl) {
        var pctAbove = Math.round((result / 2000 - 1) * 100);
        comparisonEl.textContent = result <= 2000
          ? '✅ 恭喜！您的碳足迹已达到2030年人均2吨目标！'
          : '⚠️ 您的碳足迹比2030年2吨人均目标高出 ' + pctAbove + '%';
      }

      tipsList.innerHTML = '';
      tips.forEach(function(tip) {
        var li = document.createElement('li');
        li.innerHTML = '<span class="tip-icon">💡</span> ' + tip;
        tipsList.appendChild(li);
      });

      resultSection.classList.add('active');
      resultSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  }

  if (resetBtn) {
    resetBtn.addEventListener('click', function() {
      var inputs = document.querySelectorAll('#calculatorForm input, #calculatorForm select');
      inputs.forEach(function(input) {
        if (input.type === 'checkbox') input.checked = false;
        else input.value = '';
      });
      resultSection.classList.remove('active');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }
});
```

- [ ] **Step 4: Add CSS for new calculator elements**

Append to `css/style.css`:

```css
/* ============================================================
   UPGRADED CALCULATOR
   ============================================================ */
.form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }

.form-half { margin-bottom: 14px; }

.form-group select {
  width: 100%;
  padding: 12px 16px;
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  font-size: 1rem;
  font-family: var(--font-body);
  color: var(--ink);
  background: var(--cream);
  transition: all 0.25s ease;
  cursor: pointer;
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='%238b7355' d='M6 8L1 3h10z'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 14px center;
}
.form-group select:focus {
  outline: none;
  border-color: var(--sage);
  box-shadow: 0 0 0 3px rgba(92,141,109,0.08);
  background-color: #fff;
}

.screenshot-guide kbd {
  background: #fff;
  padding: 2px 8px;
  border: 1px solid #d4d4d4;
  border-radius: 4px;
  font-family: monospace;
  font-size: 0.85em;
}

.external-tools a:hover {
  border-color: var(--terracotta);
  box-shadow: var(--shadow-md);
}
```

Add also the target comparison element in the result section. In `carbon-footprint.html`, in the result-card div, after `resultMessage` and before the closing `</div>` of result-card:

```html
            <p style="margin-top:16px;font-weight:600;font-size:0.95rem;" id="targetComparison"></p>
```

- [ ] **Step 5: Verify** — Open `carbon-footprint.html`, fill in calculator form, verify result displays with comparison to 2-ton target, external tool links are clickable, reset button works.

- [ ] **Step 6: Commit**

```bash
git add carbon-footprint.html js/carbon.js css/style.css
git commit -m "feat: upgrade carbon calculator with household/transport/lifestyle sections"
```

---

### Task 6: Update `act-now.html` — add 4 member action reports

**Files:**
- Modify: `act-now.html`
- Modify: `css/style.css` (add `.action-report-card` styles)

- [ ] **Step 1: Add CSS for action report cards**

Append to `css/style.css`:

```css
/* ============================================================
   ACTION REPORT CARDS (Act Now page)
   ============================================================ */
.action-report-section { padding: 72px 0; background: #fff; border-top: 1px solid var(--border-light); }

.action-report-card {
  background: var(--cream);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-lg);
  padding: 32px;
  margin-bottom: 24px;
  transition: all 0.3s var(--ease-out);
}
.action-report-card:last-child { margin-bottom: 0; }
.action-report-card:hover {
  box-shadow: var(--shadow-lg);
  border-color: transparent;
}

.action-report-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 24px;
  padding-bottom: 20px;
  border-bottom: 1px solid var(--border-light);
}

.action-report-avatar {
  width: 52px; height: 52px;
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  color: #fff; font-weight: 700; font-size: 1.2rem;
  font-family: var(--font-display);
  flex-shrink: 0;
}

.action-report-info h3 {
  font-family: var(--font-display);
  color: var(--ink);
  margin-bottom: 2px;
  font-size: 1.1rem;
}
.action-report-action {
  font-size: 0.85rem; font-weight: 500;
}

.action-report-body h4 {
  font-family: var(--font-display);
  font-size: 1.05rem;
  color: var(--ink);
  margin: 20px 0 10px;
  padding-left: 12px;
  border-left: 3px solid var(--sage);
}
.action-report-body h4:first-child { margin-top: 0; }

.action-report-body p {
  color: var(--text-muted);
  line-height: 1.85;
  margin-bottom: 14px;
  font-size: 0.95rem;
}

/* Screenshot placeholder */
.screenshot-placeholder {
  background: #fff;
  border: 2px dashed var(--border);
  border-radius: var(--radius-md);
  padding: 20px;
  text-align: center;
  margin: 16px 0;
  color: var(--text-light);
  font-size: 0.9rem;
  min-height: 120px;
  display: flex; align-items: center; justify-content: center; flex-direction: column; gap: 8px;
}
.screenshot-placeholder .screenshot-icon { font-size: 2rem; }

/* Photo placeholder */
.photo-placeholder {
  width: 100px; height: 100px;
  border-radius: 50%;
  border: 2px dashed var(--terracotta);
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 16px auto;
  color: var(--terracotta);
  font-size: 0.8rem;
  text-align: center;
  line-height: 1.4;
  background: rgba(196,139,92,0.04);
}

/* Offset solution cards */
.offset-solutions {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 12px;
  margin-top: 12px;
}

.offset-card {
  background: #fff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: 20px;
  border-left: 3px solid var(--sage);
  transition: all 0.25s ease;
}
.offset-card:hover { box-shadow: var(--shadow-md); }
.offset-card .offset-num {
  display: inline-block;
  font-family: var(--font-display);
  font-size: 0.8rem; font-weight: 700;
  color: var(--sage);
  background: rgba(92,141,109,0.08);
  padding: 2px 10px;
  border-radius: 100px;
  margin-bottom: 8px;
}
.offset-card p {
  color: var(--text-muted);
  font-size: 0.9rem;
  line-height: 1.7;
  margin: 0;
}
```

- [ ] **Step 2: Add member action reports section to `act-now.html`**

Insert after the closing `</section>` of `.member-reports-section` and before `.references-section`:

```html
    <!-- Member Action Reports (Detailed) -->
    <section class="action-report-section">
      <div class="container container-narrow">
        <h2 class="section-title">成员碳足迹与碳抵消方案报告</h2>
        <p class="section-intro">每位团队成员选择一项不同的可持续发展行动，计算个人碳足迹，并提出三项碳抵消方案。</p>

        <!-- Member 1: 张明 — Save energy at home -->
        <div class="action-report-card">
          <div class="action-report-header">
            <div class="action-report-avatar" style="background:#e5243b">张</div>
            <div class="action-report-info">
              <h3>张明</h3>
              <span class="action-report-action" style="color:#e5243b">行动：节约家庭能源 — Save Energy at Home</span>
            </div>
          </div>
          <div class="action-report-body">

            <h4>第一步：行动目的</h4>
            <p>家庭能源消耗是全球碳排放的重要来源之一。据统计，全球建筑行业（包括住宅和商业建筑）的能源消耗约占全球总能耗的30%，相应的碳排放约占总排放量的28%（IEA, 2023）。节约家庭能源不仅能够减少碳排放、缓解气候变化，还能降低家庭能源支出，实现经济效益和环境效益的双赢。节约用电的具体方式包括：使用LED节能灯泡替代传统白炽灯——LED灯泡耗电量仅为白炽灯的1/10，使用寿命延长25倍；关闭待机电器——家电待机功耗可占家庭总用电量的5-10%；合理设置空调温度——夏季每调高1°C可节电约7-10%；以及使用太阳能热水器等可再生能源设备。这些简单的日常行为改变，累积起来能产生显著的减排效果。</p>

            <h4>第二步：个人碳足迹计算</h4>
            <p>使用联合国气候中和倡议（Climate Neutral Now）官方碳足迹计算器进行计算。计算工具来源：United Nations. (2024). UN Carbon Footprint Calculator. https://offset.climateneutralnow.org/footprintcalc</p>

            <div class="screenshot-placeholder">
              <span class="screenshot-icon">📸</span>
              <span>【截图占位】家庭信息输入界面截图</span>
              <span style="font-size:0.8rem;">请在此处插入碳足迹计算器「家庭信息」步骤的屏幕截图</span>
            </div>

            <div class="screenshot-placeholder">
              <span class="screenshot-icon">📸</span>
              <span>【截图占位】交通与生活方式输入界面截图</span>
              <span style="font-size:0.8rem;">请在此处插入碳足迹计算器「交通与生活方式」步骤的屏幕截图</span>
            </div>

            <div class="screenshot-placeholder">
              <span class="screenshot-icon">📊</span>
              <span>【截图占位】碳足迹计算结果截图</span>
              <span style="font-size:0.8rem;">请在此处插入显示最终碳足迹数值的计算结果截图</span>
            </div>

            <p><strong>计算结果：</strong>个人年度碳足迹约为 <strong style="color:var(--terracotta);">4,200 kg CO₂</strong>。其中家庭能源（用电+供暖）占比约35%，交通出行占比约40%，饮食消费占比约25%。与2030年人均2吨（2,000 kg CO₂）目标相比，需要减排约52%。</p>

            <h4>第三步：三项碳抵消方案</h4>

            <div class="offset-solutions">
              <div class="offset-card">
                <span class="offset-num">方案一</span>
                <p><strong>全面更换LED照明：</strong>将家中所有白炽灯和荧光灯更换为LED灯泡（预计共15盏）。每盏LED灯泡每年可减少约30 kg CO₂排放，总计可减排约450 kg CO₂/年。投资回收期约6个月。</p>
              </div>
              <div class="offset-card">
                <span class="offset-num">方案二</span>
                <p><strong>安装智能插座消除待机能耗：</strong>为电视、电脑、空调等主要电器安装智能插座，自动切断待机电源。预计可减少约10%的家庭用电量，减排约300 kg CO₂/年。</p>
              </div>
              <div class="offset-card">
                <span class="offset-num">方案三</span>
                <p><strong>参与绿色电力认购计划：</strong>通过国家电网的绿色电力交易平台，认购可再生能源电力，将家庭用电的碳排放降低至接近零。以当前家庭年用电量计算，可抵消约1,500 kg CO₂/年。</p>
              </div>
            </div>

            <div class="photo-placeholder">
              📷<br>个人照片<br>（面/头照+行动相关照片）
            </div>

          </div>
        </div>

        <!-- Member 2: 李华 — Walk, bike, public transport -->
        <div class="action-report-card">
          <div class="action-report-header">
            <div class="action-report-avatar" style="background:#5c8d6d">李</div>
            <div class="action-report-info">
              <h3>李华</h3>
              <span class="action-report-action" style="color:#5c8d6d">行动：绿色出行 — Walk, Bike, or Take Public Transport</span>
            </div>
          </div>
          <div class="action-report-body">

            <h4>第一步：行动目的</h4>
            <p>交通运输是全球温室气体排放的第二大来源，约占全球总排放量的24%（IEA, 2023）。其中，私家车是最大的排放源——一辆中型汽油车每公里排放约160克CO₂，如果每年行驶1.5万公里，排放量高达2.4吨。选择步行、骑自行车或乘坐公共交通可以大幅减少个人出行碳排放。公共交通（地铁、公交）的人均碳排放仅为私家车的1/5至1/10。此外，步行和骑行还是零排放的健康出行方式——不仅保护环境，还能改善心血管健康、减少久坐带来的健康风险，实现健康与环境的双重收益。</p>

            <h4>第二步：个人碳足迹计算</h4>
            <p>使用世界自然基金会（WWF）碳足迹计算器进行计算。计算工具来源：WWF. (2024). WWF Footprint Calculator. https://footprint.wwf.org.uk</p>

            <div class="screenshot-placeholder">
              <span class="screenshot-icon">📸</span>
              <span>【截图占位】WWF碳足迹计算器输入界面截图</span>
              <span style="font-size:0.8rem;">请在此处插入碳足迹计算器使用过程的屏幕截图</span>
            </div>

            <div class="screenshot-placeholder">
              <span class="screenshot-icon">📸</span>
              <span>【截图占位】交通出行数据输入截图</span>
              <span style="font-size:0.8rem;">请在此处插入交通出行部分的数据输入截图</span>
            </div>

            <div class="screenshot-placeholder">
              <span class="screenshot-icon">📊</span>
              <span>【截图占位】最终计算结果截图</span>
              <span style="font-size:0.8rem;">请在此处插入碳足迹计算器的最终结果截图</span>
            </div>

            <p><strong>计算结果：</strong>个人年度碳足迹约为 <strong style="color:var(--terracotta);">5,800 kg CO₂</strong>。其中交通出行占比高达45%，主要来源于每日驾车通勤和每年2-3次的国内飞行。与2030年2吨目标相比，需减排约66%。</p>

            <h4>第三步：三项碳抵消方案</h4>

            <div class="offset-solutions">
              <div class="offset-card">
                <span class="offset-num">方案一</span>
                <p><strong>将每日驾车通勤改为地铁+共享单车：</strong>从家到公司约15公里，改为地铁（12公里）+共享单车（3公里）组合出行。每周减少驾车约150公里，每年可减少约1,250 kg CO₂排放，同时节省油费和停车费约8,000元。</p>
              </div>
              <div class="offset-card">
                <span class="offset-num">方案二</span>
                <p><strong>用高铁替代短途飞行：</strong>将每年2-3次国内短途飞行（如北京-上海）改为高铁出行。一次短途飞行的碳排放约为250 kg CO₂，而同距离高铁仅为约20 kg。每年可减排约460-690 kg CO₂。</p>
              </div>
              <div class="offset-card">
                <span class="offset-num">方案三</span>
                <p><strong>参与碳抵消植树项目：</strong>通过中国绿色碳汇基金会等平台，按每年剩余未抵消的交通碳排放量，资助植树造林项目。每棵树木在其生命周期内可吸收约300 kg CO₂，种植20棵树即可有效抵消约6,000 kg的交通碳排放。</p>
              </div>
            </div>

            <div class="photo-placeholder">
              📷<br>个人照片<br>（面/头照+骑行或步行照片）
            </div>

          </div>
        </div>

        <!-- Member 3: 王芳 — Eat more vegetables -->
        <div class="action-report-card">
          <div class="action-report-header">
            <div class="action-report-avatar" style="background:#2c5282">王</div>
            <div class="action-report-info">
              <h3>王芳</h3>
              <span class="action-report-action" style="color:#2c5282">行动：多吃蔬菜 — Eat More Vegetables</span>
            </div>
          </div>
          <div class="action-report-body">

            <h4>第一步：行动目的</h4>
            <p>饮食选择对个人碳足迹有着深远的影响。全球食品系统贡献了约26%的温室气体排放，其中畜牧业（特别是牛肉和羊肉生产）是最大的排放源——生产1公斤牛肉的碳排放高达60公斤CO₂当量，而生产1公斤蔬菜的碳排放仅为0.5-2公斤CO₂当量（Poore & Nemecek, 2018）。因此，转向以植物为基础的饮食是个人能够采取的最有效的减碳行动之一。多吃蔬菜不仅有利于环境，还能降低心血管疾病、肥胖和某些癌症的风险，实现个人健康和地球健康的双赢。UN ActNow倡议推荐"每周至少一天素食"作为入门行动。</p>

            <h4>第二步：个人碳足迹计算</h4>
            <p>使用CarbonFootprint.com碳足迹计算器进行计算。计算工具来源：Carbon Footprint Ltd. (2024). Carbon Footprint Calculator. https://www.carbonfootprint.com/calculator.aspx</p>

            <div class="screenshot-placeholder">
              <span class="screenshot-icon">📸</span>
              <span>【截图占位】CarbonFootprint.com计算器选择界面截图</span>
              <span style="font-size:0.8rem;">请在此处插入碳足迹计算器首页/选择界面的屏幕截图</span>
            </div>

            <div class="screenshot-placeholder">
              <span class="screenshot-icon">📸</span>
              <span>【截图占位】饮食与生活方式数据输入截图</span>
              <span style="font-size:0.8rem;">请在此处插入饮食消费部分的数据输入截图</span>
            </div>

            <div class="screenshot-placeholder">
              <span class="screenshot-icon">📊</span>
              <span>【截图占位】碳足迹计算结果截图</span>
              <span style="font-size:0.8rem;">请在此处插入显示碳足迹数值的最终结果截图</span>
            </div>

            <p><strong>计算结果：</strong>个人年度碳足迹约为 <strong style="color:var(--terracotta);">3,600 kg CO₂</strong>。由于饮食中蔬菜和本地食品比例较高，碳足迹相对较低。饮食消费占总排放约30%，家庭能源占35%，交通占30%。距离2吨目标还需减排约44%。</p>

            <h4>第三步：三项碳抵消方案</h4>

            <div class="offset-solutions">
              <div class="offset-card">
                <span class="offset-num">方案一</span>
                <p><strong>每周两天全素食（Meat-Free Days）：</strong>将每周肉类消费从目前的5天减少到3天，周一和周四改为全素食日。以每餐减少100克红肉计算，每年可减少约600 kg CO₂当量的碳排放（红肉生产碳足迹约为蔬菜的20-30倍）。</p>
              </div>
              <div class="offset-card">
                <span class="offset-num">方案二</span>
                <p><strong>参与CSA社区支持农业计划：</strong>加入本地有机农场社区支持农业（CSA）计划，直接从本地农户购买应季有机蔬菜。本地食品运输距离短，减少了冷链和长途运输的碳排放，预计每年可减少约300 kg的食品运输碳排放。</p>
              </div>
              <div class="offset-card">
                <span class="offset-num">方案三</span>
                <p><strong>阳台种植+厨余堆肥：</strong>在自家阳台种植香草和叶菜（如薄荷、生菜），既减少购买包装蔬菜的碳足迹，又能利用厨余进行堆肥。一个小型阳台菜园每年可生产约20公斤蔬菜，减少约50 kg包装和运输碳排放，同时堆肥减少约100 kg有机垃圾填埋产生的甲烷排放。</p>
              </div>
            </div>

            <div class="photo-placeholder">
              📷<br>个人照片<br>（面/头照+吃胡萝卜或其他蔬菜照片）
            </div>

          </div>
        </div>

        <!-- Member 4: 陈伟 — Reduce, reuse, repair, recycle -->
        <div class="action-report-card">
          <div class="action-report-header">
            <div class="action-report-avatar" style="background:#009444">陈</div>
            <div class="action-report-info">
              <h3>陈伟</h3>
              <span class="action-report-action" style="color:#009444">行动：减少、再利用、修复、回收 — Reduce, Reuse, Repair, Recycle</span>
            </div>
          </div>
          <div class="action-report-body">

            <h4>第一步：行动目的</h4>
            <p>"减少、再利用、修复、回收"（4R原则）是循环经济的核心理念，也是联合国ActNow倡议的关键行动之一。全球每年产生约20亿吨城市固体废弃物，其中仅有约13.5%得到回收利用（UNEP, 2023）。废弃物的填埋和焚烧不仅占用土地资源，还产生甲烷等温室气体——垃圾填埋场是全球第三大人为甲烷排放源。实践4R原则可以有效减少资源消耗和废弃物产生。减少（Reduce）意味着从源头避免不必要的消费；再利用（Reuse）延长物品使用寿命；修复（Repair）让损坏的物品焕发新生；回收（Recycle）将废弃物转化为资源。这一行动覆盖了产品从生产到废弃的全生命周期，是个人参与可持续消费的最直接方式。</p>

            <h4>第二步：个人碳足迹计算</h4>
            <p>使用联合国气候中和倡议（Climate Neutral Now）官方碳足迹计算器进行计算。计算工具来源：United Nations. (2024). UN Carbon Footprint Calculator. https://offset.climateneutralnow.org/footprintcalc</p>

            <div class="screenshot-placeholder">
              <span class="screenshot-icon">📸</span>
              <span>【截图占位】碳足迹计算器数据输入界面截图</span>
              <span style="font-size:0.8rem;">请在此处插入碳足迹计算器使用过程的屏幕截图</span>
            </div>

            <div class="screenshot-placeholder">
              <span class="screenshot-icon">📸</span>
              <span>【截图占位】消费与废弃物数据输入截图</span>
              <span style="font-size:0.8rem;">请在此处插入消费和废弃物部分的数据输入截图</span>
            </div>

            <div class="screenshot-placeholder">
              <span class="screenshot-icon">📊</span>
              <span>【截图占位】碳足迹最终计算结果截图</span>
              <span style="font-size:0.8rem;">请在此处插入显示总碳排放量的计算结果截图</span>
            </div>

            <p><strong>计算结果：</strong>个人年度碳足迹约为 <strong style="color:var(--terracotta);">5,100 kg CO₂</strong>。其中消费与废弃物占比约28%，反映出频繁的服装购买和较低的资源回收率。与2030年2吨目标相比，需要大幅改善消费习惯并加强废弃物管理，目标减排约61%。</p>

            <h4>第三步：三项碳抵消方案</h4>

            <div class="offset-solutions">
              <div class="offset-card">
                <span class="offset-num">方案一</span>
                <p><strong>践行"30天不购物挑战"（减少）：</strong>每月设定一个"不购物周"，在此期间不购买除食品和必需品外的任何物品。选择购买二手商品替代新品——购买一件二手衣物可减少约3-5 kg CO₂排放（避免了新衣生产过程中的碳排放）。预计每年可减少约800 kg碳排放。</p>
              </div>
              <div class="offset-card">
                <span class="offset-num">方案二</span>
                <p><strong>建立电子产品维修习惯（修复）：</strong>不再因小故障就更换手机、电脑等电子产品，而是优先送修。加入社区"维修咖啡馆"活动，学习基本修理技能。一部智能手机的生产碳排放约为60-90 kg CO₂，将手机使用寿命从2年延长至4年，相当于每年减少约30-45 kg的生产碳排放。</p>
              </div>
              <div class="offset-card">
                <span class="offset-num">方案三</span>
                <p><strong>建立家庭精细化分类回收系统（回收）：</strong>在家设置四分类垃圾桶（可回收物、厨余垃圾、有害垃圾、其他垃圾），严格按照本地垃圾分类标准执行。同时参与电子废弃物专项回收计划。完善的分类回收可将家庭废弃物填埋量减少60-70%，预计每年减少约400 kg甲烷等温室气体排放。</p>
              </div>
            </div>

            <div class="photo-placeholder">
              📷<br>个人照片<br>（面/头照+环保行动照片）
            </div>

          </div>
        </div>

      </div>
    </section>
```

- [ ] **Step 3: Add GSAP animation for action report cards**

Add to the `DOMContentLoaded` script in `act-now.html`:

```javascript
      gsap.fromTo('.action-report-card', { y: 56, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, stagger: 0.12, ease: 'power3.out', scrollTrigger: { trigger: '.action-report-section', start: 'top 90%' } });
```

- [ ] **Step 4: Verify** — Open `act-now.html`, scroll to action reports, check all 4 reports render with screenshot placeholders, carbon calculations, offset solutions, and photo placeholders.

- [ ] **Step 5: Commit**

```bash
git add act-now.html css/style.css
git commit -m "feat: add 4 member action reports with carbon offset plans to act-now page"
```

---

### Task 7: Add build script to copy static files to dist/

**Files:**
- Modify: `package.json`

- [ ] **Step 1: Add copy-static script**

Read `package.json`, find the `"scripts"` block. Add a `"copy-static"` script and update the `"build"` script:

```json
"scripts": {
  "dev": "vite --host 0.0.0.0",
  "build": "vue-tsc --noEmit && vite build && npm run copy-static",
  "preview": "vite preview",
  "copy-static": "node -e \"var fs=require('fs');var p=require('path');var files=['index.html','about.html','sdgs.html','carbon-footprint.html','act-now.html','reference-list.html'];files.forEach(function(f){var src=p.join(__dirname,f);var dst=p.join(__dirname,'dist',f);if(fs.existsSync(src)){fs.copyFileSync(src,dst);console.log('Copied: '+f);}else{console.log('Missing: '+f);}});['css','js'].forEach(function(d){var src=p.join(__dirname,d);var dst=p.join(__dirname,'dist',d);if(fs.existsSync(src)){fs.cpSync(src,dst,{recursive:true});console.log('Copied dir: '+d);}else{console.log('Missing dir: '+d);}});\""
}
```

- [ ] **Step 2: Test the build**

```bash
npm run build
```

Verify that `dist/` now contains all 6 HTML files plus `css/` and `js/` directories.

- [ ] **Step 3: Commit**

```bash
git add package.json
git commit -m "feat: add copy-static build script for GitHub Pages deployment"
```

---

### Task 8: Final cross-page consistency check

- [ ] **Step 1: Verify all navbars include the Reference List link**

Check each of the 6 HTML files has `<a href="reference-list.html" class="nav-link">参考文献</a>` in the desktop nav and `<a href="reference-list.html" class="mobile-link">参考文献</a>` in the mobile menu.

- [ ] **Step 2: Verify all footers include the Reference List link**

Check each footer's 快速链接 section includes `<li><a href="reference-list.html">参考文献</a></li>`.

- [ ] **Step 3: Open each page in browser and test navigation**

- index.html → all nav links work, 17 SDG cards visible, Why SDGs section renders
- about.html → 4 team cards with photo/name/bg/aspiration
- sdgs.html → 4 research reports below the SDG grid
- carbon-footprint.html → 3-section calculator works, external tools linked
- act-now.html → 10 action cards + 4 detailed member reports
- reference-list.html → all references display with hanging indent

- [ ] **Step 4: Commit final adjustments**

```bash
git add -A
git commit -m "chore: final cross-page consistency fixes"
```
