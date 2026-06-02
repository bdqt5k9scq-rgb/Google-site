document.addEventListener('DOMContentLoaded', function() {
  const calculateBtn = document.getElementById('calculateBtn');
  const resetBtn = document.getElementById('resetBtn');
  const resultSection = document.getElementById('resultSection');
  const resultValue = document.getElementById('resultValue');
  const resultLevel = document.getElementById('resultLevel');
  const resultMessage = document.getElementById('resultMessage');
  const tipsList = document.getElementById('tipsList');
  
  const formInputs = {
    carDistance: document.getElementById('carDistance'),
    publicTransport: document.getElementById('publicTransport'),
    flights: document.getElementById('flights'),
    electricity: document.getElementById('electricity'),
    gas: document.getElementById('gas'),
    heating: document.getElementById('heating'),
    meatDays: document.getElementById('meatDays'),
    localFood: document.getElementById('localFood'),
    recycling: document.getElementById('recycling'),
    composting: document.getElementById('composting')
  };
  
  function calculateCarbonFootprint() {
    let total = 0;
    
    total += parseFloat(formInputs.carDistance.value || 0) * 0.2;
    total += parseFloat(formInputs.publicTransport.value || 0) * 0.05;
    total += parseFloat(formInputs.flights.value || 0) * 250;
    
    total += parseFloat(formInputs.electricity.value || 0) * 0.5;
    total += parseFloat(formInputs.gas.value || 0) * 2.3;
    total += parseFloat(formInputs.heating.value || 0) * 1.8;
    
    total += (21 - parseFloat(formInputs.meatDays.value || 0)) * 0.05;
    total += parseFloat(formInputs.localFood.value || 0) * 0.1;
    
    if (!formInputs.recycling.checked) total += 100;
    if (!formInputs.composting.checked) total += 50;
    
    return Math.round(total);
  }
  
  function getResultLevel(total) {
    if (total < 3000) return { level: '优秀', color: '#10b981', message: '您的碳足迹非常低，继续保持！' };
    if (total < 6000) return { level: '良好', color: '#3b82f6', message: '您的碳足迹处于中等水平，可以进一步改善。' };
    if (total < 10000) return { level: '一般', color: '#f59e0b', message: '您的碳足迹较高，建议采取更多环保措施。' };
    return { level: '较高', color: '#ef4444', message: '您的碳足迹很高，请采取行动减少碳排放。' };
  }
  
  function getTips() {
    const tips = [];
    if (parseFloat(formInputs.carDistance.value || 0) > 100) {
      tips.push('考虑使用公共交通工具或骑行代替开车');
    }
    if (parseFloat(formInputs.flights.value || 0) > 2) {
      tips.push('减少长途飞行，考虑视频会议');
    }
    if (parseFloat(formInputs.electricity.value || 0) > 500) {
      tips.push('使用节能电器，养成随手关灯的习惯');
    }
    if (parseFloat(formInputs.meatDays.value || 0) > 14) {
      tips.push('尝试减少肉类消费，多吃植物性食物');
    }
    if (!formInputs.recycling.checked) {
      tips.push('开始垃圾分类和回收');
    }
    if (!formInputs.composting.checked) {
      tips.push('尝试堆肥处理厨余垃圾');
    }
    return tips.length > 0 ? tips : ['您做得很好！继续保持环保习惯。'];
  }
  
  if (calculateBtn) {
    calculateBtn.addEventListener('click', function() {
      const result = calculateCarbonFootprint();
      const level = getResultLevel(result);
      const tips = getTips();
      
      resultValue.innerHTML = result + ' <span class="unit">kg CO₂/年</span>';
      resultValue.style.color = level.color;
      resultLevel.textContent = level.level;
      resultLevel.style.backgroundColor = level.color;
      resultMessage.textContent = level.message;
      
      tipsList.innerHTML = '';
      tips.forEach(tip => {
        const li = document.createElement('li');
        li.innerHTML = '<span class="tip-icon">💡</span> ' + tip;
        tipsList.appendChild(li);
      });
      
      resultSection.classList.add('active');
      resultSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  }
  
  if (resetBtn) {
    resetBtn.addEventListener('click', function() {
      Object.values(formInputs).forEach(input => {
        if (input.type === 'checkbox') {
          input.checked = false;
        } else {
          input.value = '';
        }
      });
      resultSection.classList.remove('active');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }
});
