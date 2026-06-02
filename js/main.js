/**
 * SDG Website — shared JavaScript
 * Mobile menu toggle, active nav highlighting, modal handling, filters
 */
document.addEventListener('DOMContentLoaded', function() {
  /* ---- Mobile menu ---- */
  var menuToggle = document.querySelector('.menu-toggle');
  var mobileMenu = document.querySelector('.mobile-menu');

  if (menuToggle && mobileMenu) {
    menuToggle.addEventListener('click', function() {
      var isOpen = mobileMenu.style.display === 'block';
      mobileMenu.style.display = isOpen ? 'none' : 'block';
    });
  }

  var mobileLinks = document.querySelectorAll('.mobile-link');
  mobileLinks.forEach(function(link) {
    link.addEventListener('click', function() {
      if (mobileMenu) mobileMenu.style.display = 'none';
    });
  });

  /* ---- Active nav link ---- */
  var currentPage = window.location.pathname.split('/').pop() || 'index.html';
  var navLinks = document.querySelectorAll('.nav-link');
  navLinks.forEach(function(link) {
    var href = link.getAttribute('href');
    if (href === currentPage) link.classList.add('active');
  });

  /* ---- Navbar shrink on scroll (via GSAP ScrollTrigger if available) ---- */
  if (typeof ScrollTrigger !== 'undefined') {
    ScrollTrigger.create({
      start: 'top -80px',
      toggleClass: { targets: '.navbar', className: 'navbar-scrolled' }
    });
  }

  /* ---- SDG Modal (sdgs.html) ---- */
  var modalOverlay = document.getElementById('sdgModal');
  var closeBtn = document.querySelector('.close-btn');
  var modalHeader = document.querySelector('.modal-header');
  var modalNumber = document.querySelector('.modal-number');
  var modalTitle = document.querySelector('.modal-title h2');
  var modalSubtitle = document.querySelector('.modal-title p');
  var modalBody = document.querySelector('.modal-body p');

  var sdgs = [
    { id: 1, title: '消除贫困', subtitle: 'No Poverty', color: '#e5243b', description: '在世界各地消除一切形式的贫困。确保所有男女，特别是赤贫人口，享有平等获得经济资源的权利，以及获得基本服务、所有权和对土地及其他形式财产的控制权。' },
    { id: 2, title: '零饥饿', subtitle: 'Zero Hunger', color: '#dda63a', description: '消除饥饿，实现粮食安全，改善营养状况和促进可持续农业。到2030年，确保所有人全年都能获得安全、营养和充足的食物。' },
    { id: 3, title: '良好健康与福祉', subtitle: 'Good Health and Well-being', color: '#4c9f38', description: '确保健康的生活方式，促进各年龄段人群的福祉。到2030年，将全球孕产妇死亡率降低到每10万活产140人以下。' },
    { id: 4, title: '优质教育', subtitle: 'Quality Education', color: '#c5192d', description: '确保包容和公平的优质教育，促进全民终身学习。到2030年，确保所有男女儿童完成免费、公平和优质的初等和中等教育，并取得相关和有效的学习成果。' },
    { id: 5, title: '性别平等', subtitle: 'Gender Equality', color: '#ff3a21', description: '实现性别平等，增强所有妇女和女童的权能。消除对妇女和女童的一切形式歧视。' },
    { id: 6, title: '清洁饮水', subtitle: 'Clean Water and Sanitation', color: '#26bde2', description: '确保清洁饮水和卫生设施。到2030年，普遍和公平地获得安全和负担得起的饮用水。' },
    { id: 7, title: '廉价清洁能源', subtitle: 'Affordable and Clean Energy', color: '#fcc30b', description: '确保获得负担得起的、可靠的、可持续的和现代的能源。到2030年，确保人人获得负担得起的、可靠的现代能源服务。' },
    { id: 8, title: '体面工作与经济增长', subtitle: 'Decent Work and Economic Growth', color: '#a21942', description: '促进持久、包容和可持续的经济增长，促进充分的生产性就业和体面工作。' },
    { id: 9, title: '产业、创新与基础设施', subtitle: 'Industry, Innovation and Infrastructure', color: '#fd6925', description: '建造具备抵御灾害能力的基础设施，促进包容和可持续的工业化，推动创新。' },
    { id: 10, title: '减少不平等', subtitle: 'Reduced Inequalities', color: '#dd1367', description: '减少国家内部和国家之间的不平等。到2030年，根据各国国情，逐步实现并维持最底层40%人口的收入增长率高于全国平均水平。' },
    { id: 11, title: '可持续城市和社区', subtitle: 'Sustainable Cities and Communities', color: '#fd9d24', description: '建设包容、安全、有抵御灾害能力和可持续的城市和人类住区。到2030年，使城市和人类住区具有包容性、安全、韧性和可持续性。' },
    { id: 12, title: '负责任消费和生产', subtitle: 'Responsible Consumption and Production', color: '#bf8b2e', description: '确保可持续消费和生产模式。到2030年，实现全球可持续消费和生产模式。' },
    { id: 13, title: '气候行动', subtitle: 'Climate Action', color: '#3f7e44', description: '采取紧急行动应对气候变化及其影响。加强各国应对气候变化影响的能力。' },
    { id: 14, title: '水下生物', subtitle: 'Life Below Water', color: '#009444', description: '保护和可持续利用海洋和海洋资源以促进可持续发展。制止过度捕捞、非法、未报告和无管制的捕捞活动。' },
    { id: 15, title: '陆地生物', subtitle: 'Life on Land', color: '#00a651', description: '保护、恢复和促进可持续利用陆地生态系统，可持续管理森林，防治荒漠化，制止和扭转土地退化，遏制生物多样性的丧失。' },
    { id: 16, title: '和平、正义与强大机构', subtitle: 'Peace, Justice and Strong Institutions', color: '#19489d', description: '促进有利于可持续发展的和平和包容社会，为所有人提供诉诸司法的机会，在各级建立有效、负责和包容的机构。' },
    { id: 17, title: '促进目标实现的伙伴关系', subtitle: 'Partnerships for the Goals', color: '#192841', description: '加强执行手段，重振可持续发展全球伙伴关系。加强多利益攸关方伙伴关系，调动和分享知识、专长、技术和财政资源，以实现可持续发展目标。' }
  ];

  var sdgCards = document.querySelectorAll('.sdg-full-card');
  sdgCards.forEach(function(card) {
    card.addEventListener('click', function() {
      var id = parseInt(this.getAttribute('data-id'));
      var sdg = sdgs.find(function(s) { return s.id === id; });
      if (sdg && modalOverlay) {
        if (modalHeader) modalHeader.style.backgroundColor = sdg.color;
        if (modalNumber) modalNumber.textContent = sdg.id;
        if (modalTitle) modalTitle.textContent = sdg.title;
        if (modalSubtitle) modalSubtitle.textContent = sdg.subtitle;
        if (modalBody) modalBody.textContent = sdg.description;
        modalOverlay.classList.add('active');
        document.body.style.overflow = 'hidden';
      }
    });
  });

  if (closeBtn && modalOverlay) {
    closeBtn.addEventListener('click', function() {
      modalOverlay.classList.remove('active');
      document.body.style.overflow = '';
    });
    modalOverlay.addEventListener('click', function(e) {
      if (e.target === modalOverlay) {
        modalOverlay.classList.remove('active');
        document.body.style.overflow = '';
      }
    });
  }

  /* ---- Category filter (act-now.html) ---- */
  var filterBtns = document.querySelectorAll('.filter-btn');
  var actionCards = document.querySelectorAll('.action-card');

  filterBtns.forEach(function(btn) {
    btn.addEventListener('click', function() {
      var category = this.getAttribute('data-category');
      filterBtns.forEach(function(b) { b.classList.remove('active'); });
      this.classList.add('active');
      actionCards.forEach(function(card) {
        if (category === '全部' || card.getAttribute('data-category') === category) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
});
