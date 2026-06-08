document.addEventListener('DOMContentLoaded', function() {
  var calculateBtn = document.getElementById('calculateBtn');
  var resetBtn = document.getElementById('resetBtn');
  var resultSection = document.getElementById('resultSection');
  var resultValue = document.getElementById('resultValue');
  var resultLevel = document.getElementById('resultLevel');
  var resultMessage = document.getElementById('resultMessage');
  var tipsList = document.getElementById('tipsList');

  function getVal(id) { var el = document.getElementById(id); return el ? (el.value || 0) : 0; }
  function isChecked(id) { var el = document.getElementById(id); return el ? el.checked : false; }
  function getSelect(id) { var el = document.getElementById(id); return el ? (el.value || '') : ''; }

  function calculateCarbonFootprint() {
    var total = 0;

    // Household
    var housingSize = parseFloat(getVal('housingSize')) || 90;
    var housingType = getSelect('housingType');
    var electricity = parseFloat(getVal('electricity')) || 300;
    var heating = getSelect('heating');
    var greenEnergy = isChecked('greenEnergy');

    var housingFactor = 20;
    if (housingType === 'apartment') housingFactor = 15;
    if (housingType === 'studio') housingFactor = 12;
    if (housingType === 'detached') housingFactor = 25;
    total += housingSize * housingFactor;

    var elecFactor = greenEnergy ? 0.1 : 0.6;
    total += electricity * 12 * elecFactor;

    if (heating === 'coal') total += 3000;
    else if (heating === 'gas') total += 2000;
    else if (heating === 'electric') total += 1500;
    else if (heating === 'district') total += 1000;

    // Transport
    var carDistance = parseFloat(getVal('carDistance')) || 0;
    var carType = getSelect('carType');
    var publicTransport = parseFloat(getVal('publicTransport')) || 0;
    var flightsShort = parseFloat(getVal('flightsShort')) || 0;
    var flightsLong = parseFloat(getVal('flightsLong')) || 0;

    var carFactors = {
      'petrol_small': 120, 'petrol_medium': 160, 'petrol_large': 220,
      'diesel': 140, 'hybrid': 90, 'electric': 40
    };
    var carFactor = carFactors[carType] || 150;
    total += carDistance * 52 * carFactor / 1000;

    total += publicTransport * 52 * 3;

    total += flightsShort * 250;
    total += flightsLong * 900;

    // Lifestyle
    var dietType = getSelect('dietType');
    var localFood = parseFloat(getVal('localFood')) || 50;
    var foodWaste = parseFloat(getVal('foodWaste')) || 2;
    var clothingSpend = parseFloat(getVal('clothingSpend')) || 500;
    var recycling = isChecked('recycling');

    var dietFactors = {
      'vegan': 1000, 'vegetarian': 1500, 'pescatarian': 1800,
      'lowMeat': 2200, 'mediumMeat': 3000, 'highMeat': 4000
    };
    total += dietFactors[dietType] || 2500;

    total *= (1 - (localFood / 100) * 0.1);

    total += foodWaste * 52 * 2.5;

    total += clothingSpend * 12 * 0.02;

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
