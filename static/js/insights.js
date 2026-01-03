(function () {
  let chartsInitialized = false;
  let mapInitialized = false;
  let initScheduled = false;

  const statusEl = () => document.getElementById('insights-status');
  const setStatus = (txt) => { const el = statusEl(); if (el) el.textContent = txt; };

  function logLoaded() {
    console.log('insights.js loaded OK');
    console.log('Chart available:', typeof Chart !== 'undefined');
    console.log('Leaflet available:', typeof L !== 'undefined');
  }

  function ensureChartLib() {
    if (typeof Chart === 'undefined') {
      const msg = 'Chart.js missing (tjek /static/vendor/chartjs/chart.umd.min.js)';
      setStatus(msg);
      throw new Error(msg);
    }
    return true;
  }

  function ensureLeafletLib() {
    if (typeof L === 'undefined') {
      const msg = 'Leaflet missing (tjek /static/vendor/leaflet/leaflet.js)';
      setStatus(msg);
      throw new Error(msg);
    }
    return true;
  }

  function hideFallbacks(section) {
    section.querySelectorAll('.insight-fallback').forEach((el) => {
      el.style.display = 'none';
    });
  }

  function ensureDomElements() {
    const requiredIds = ['chart-price-hour', 'chart-price-range', 'chart-faster', 'dk-map'];
    const missing = requiredIds.filter((id) => !document.getElementById(id));
    if (missing.length) {
      const msg = `Missing element(s): ${missing.join(', ')}`;
      setStatus(msg);
      throw new Error(msg);
    }
  }

  function sanityChart() {
    const canvas = document.getElementById('chart-price-hour');
    if (!canvas) throw new Error('Missing canvas #chart-price-hour');
    const ctx = canvas.getContext('2d');
    return new Chart(ctx, {
      type: 'bar',
      data: { labels: ['A', 'B'], datasets: [{ data: [1, 2], backgroundColor: ['#1f2937', '#9ca3af'], borderRadius: 6 }] },
      options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } }, scales: { x: { grid: { display: false } }, y: { beginAtZero: true } } }
    });
  }

  function initPricePerHourChart() {
    const canvas = document.getElementById('chart-price-hour');
    if (!canvas) throw new Error('Missing canvas #chart-price-hour');
    const ctx = canvas.getContext('2d');
    
    // Fulde navne
    const fullNames = ['Optimatix', 'Konkurrent A', 'Konkurrent B'];
    
    // Custom plugin til at tegne label over Optimatix-søjlen
    const optimatixLabelPlugin = {
      id: 'optimatixLabel',
      afterDatasetsDraw: (chart) => {
        const ctx = chart.ctx;
        const meta = chart.getDatasetMeta(0);
        const bar = meta.data[0]; // Første søjle (Optimatix)
        
        if (bar) {
          const value = chart.data.datasets[0].data[0];
          const text = `${value} kr`;
          
          ctx.save();
          ctx.font = '400 10px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif';
          ctx.fillStyle = 'rgba(31, 41, 55, 0.7)';
          ctx.textAlign = 'center';
          ctx.textBaseline = 'bottom';
          
          // Tegn tekst lige over søjlen
          ctx.fillText(text, bar.x, bar.y - 4);
          ctx.restore();
        }
      }
    };
    
    const chartConfig = {
      type: 'bar',
      data: {
        labels: fullNames,
        datasets: [
          {
            label: 'kr/time',
            data: [260, 500, 600],
            backgroundColor: ['#1f2937', '#d1d5db', '#d1d5db'],
            borderRadius: 6,
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        layout: {
          padding: {
            left: 0,
            right: 8,
            top: 0,
            bottom: 8,
          },
        },
        onResize: (chart, size) => {
          // Dynamisk rotation og font size baseret på chart width
          const width = size.width;
          const isSmall = width < 420;
          chart.options.scales.x.ticks.maxRotation = isSmall ? 25 : 0;
          chart.options.scales.x.ticks.minRotation = isSmall ? 25 : 0;
          chart.options.scales.x.ticks.font.size = isSmall ? 11 : 12;
          chart.update('none');
        },
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              title: (context) => {
                const index = context[0].dataIndex;
                return fullNames[index];
              },
              label: (ctx) => `${ctx.formattedValue} kr/time`,
            },
          },
        },
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: 'kr/time',
              color: '#1f2937',
              font: { size: 12, weight: '500' },
            },
            ticks: {
              padding: 8,
              stepSize: 300,
              callback: (value) => `${value}`,
              color: '#9ca3af',
              font: { size: 11 },
            },
            grid: { color: '#f3f4f6', drawBorder: false },
          },
          x: {
            grid: { display: false },
            ticks: {
              autoSkip: false,
              maxRotation: 0,
              minRotation: 0,
              font: { size: 12, weight: '500' },
              padding: 6,
            },
          },
        },
      },
      plugins: [optimatixLabelPlugin],
    };
    
    const chart = new Chart(ctx, chartConfig);
  }

  function initPriceRangeChart() {
    const canvas = document.getElementById('chart-price-range');
    if (!canvas) throw new Error('Missing canvas #chart-price-range');
    const ctx = canvas.getContext('2d');
    const chartData = {
      labels: [
        'Automatiseringsflow',
        'Simpel hjemmeside',
        'Forecasting model',
        'Simpel app',
      ],
      datasets: [
        {
          label: 'Prisinterval (kr)',
          data: [
            [5000, 10000],
            [6000, 8000],
            [8000, 12000],
            [10000, 15000],
          ],
          backgroundColor: '#1f2937',
          borderRadius: 6,
          borderSkipped: false,
        },
      ],
    };
    
    new Chart(ctx, {
      type: 'bar',
      data: chartData,
      options: {
        responsive: true,
        maintainAspectRatio: false,
        indexAxis: 'y',
        layout: {
          padding: {
            left: 0,
            right: 8,
            top: 0,
            bottom: 0,
          },
        },
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              label: (ctx) => {
                const [min, max] = ctx.raw;
                return `${min.toLocaleString('da-DK')} – ${max.toLocaleString('da-DK')} kr`;
              },
            },
          },
        },
        scales: {
          x: {
            beginAtZero: true,
            title: {
              display: true,
              text: 'kr',
              color: '#1f2937',
              font: { size: 12, weight: '500' },
            },
            ticks: {
              autoSkip: true,
              maxTicksLimit: 5,
              padding: 6,
              callback: (value) => {
                if (value >= 1000) {
                  return `${(value / 1000).toFixed(0)}k`;
                }
                return `${value}`;
              },
            },
            grid: { color: '#f3f4f6', drawBorder: false },
          },
          y: {
            grid: { display: false },
            ticks: {
              padding: 8,
              color: '#1f2937',
              font: { size: 11, weight: '500' },
              callback: function(value) {
                const label = chartData.labels[value];
                if (!label) return '';
                // Splitter lange labels i 2 linjer
                if (label.length > 20) {
                  const parts = label.split(' ');
                  const mid = Math.ceil(parts.length / 2);
                  return [parts.slice(0, mid).join(' '), parts.slice(mid).join(' ')];
                }
                return label;
              },
            },
          },
        },
      },
    });
  }

  function initFasterProjectsChart() {
    const canvas = document.getElementById('chart-faster');
    if (!canvas) throw new Error('Missing canvas #chart-faster');
    const ctx = canvas.getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Konkurrenter', 'Optimatix'],
        datasets: [
          {
            label: 'Uger (illustrativ)',
            data: [10, 7],
            backgroundColor: ['#d1d5db', '#1f2937'],
            borderRadius: 6,
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              label: (ctx) => {
                const value = ctx.parsed.y;
                return `${value} uger`;
              },
            },
          },
        },
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: 'uger',
              color: '#1f2937',
              font: { size: 12, weight: '500' },
            },
            ticks: {
              stepSize: 5,
              callback: (value) => `${value}`,
              color: '#9ca3af',
              font: { size: 11 },
            },
            grid: { color: '#f3f4f6', drawBorder: false },
          },
          x: { grid: { display: false } },
        },
      },
    });
  }

  function initCharts() {
    if (chartsInitialized) return;
    ensureChartLib();
    // sanity chart to prove Chart.js works
    const temp = sanityChart();
    temp.destroy();
    initPricePerHourChart();
    initPriceRangeChart();
    initFasterProjectsChart();
    chartsInitialized = true;
  }

  function initMap() {
    if (mapInitialized) return;
    ensureLeafletLib();
    const mapEl = document.getElementById('dk-map');
    if (!mapEl) throw new Error('Missing map container #dk-map');

    const map = L.map('dk-map', {
      center: [56.0, 11.5],
      zoom: 6,
      minZoom: 5,
      maxZoom: 9,
      scrollWheelZoom: false,
      zoomControl: false, // Skjul zoom-kontroller (tilføjes manuelt senere)
    });

    // Tilføj zoom-kontroller (skjules på desktop via CSS)
    L.control.zoom({
      position: 'topright'
    }).addTo(map);

    // CARTO Positron: minimalistisk tile-layer uden havdybde-linjer
    L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
      maxZoom: 19,
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="https://carto.com/attributions">CARTO</a>',
    }).addTo(map);
    
    // Gør attribution diskret
    map.attributionControl.setPosition('bottomright');

    // Fallback tileLayer (OpenStreetMap) - kommenteret
    // L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    //   maxZoom: 19,
    //   attribution: '&copy; OpenStreetMap contributors',
    // }).addTo(map);

    const cities = [
      { name: 'København', coords: [55.6761, 12.5683] },
      { name: 'Roskilde', coords: [55.6419, 12.0878] },
      { name: 'Odense', coords: [55.4038, 10.4024] },
      { name: 'Aarhus', coords: [56.1629, 10.2039] },
      { name: 'Vejle', coords: [55.7093, 9.5357] },
      { name: 'Sønderborg', coords: [54.9093, 9.7926] },
    ];

    cities.forEach((city) => {
      L.circleMarker(city.coords, {
        radius: 4,
        color: '#1f2937',
        weight: 0,
        opacity: 0,
        fillColor: '#1f2937',
        fillOpacity: 0.75,
      })
        .addTo(map)
        .bindPopup(`${city.name} – Leverede projekter`);
    });

    mapInitialized = true;
  }

  function initInsights() {
    if (initScheduled) return;
    initScheduled = true;

    try {
      ensureDomElements();

      const section = document.getElementById('insights');
      if (section) hideFallbacks(section);

      initCharts();
      initMap();
      if (chartsInitialized && mapInitialized) {
        // Skjul status når alt er klar
        const statusEl = document.getElementById('insights-status');
        if (statusEl) statusEl.style.display = 'none';
      }
    } catch (err) {
      setStatus(`Init error: ${err.message}`);
      console.error('[Insights] init error', err);
      throw err;
    }
  }

  document.addEventListener('DOMContentLoaded', function () {
    console.log('[Insights] DOMContentLoaded fired');
    setStatus('Libraries loading...');
    
    // Wait a tiny bit for deferred scripts to fully execute
    setTimeout(() => {
      try {
        logLoaded();
        setStatus('DOM ready');

        const insightsSection = document.getElementById('insights');
        if (!insightsSection) {
          console.warn('[Insights] #insights section not found');
          return;
        }

        // IntersectionObserver init
        if ('IntersectionObserver' in window) {
          const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
              if (entry.isIntersecting) {
                try {
                  initInsights();
                } catch (err) {
                  setStatus(`Init error: ${err.message}`);
                  console.error('[Insights] init error (IO)', err);
                }
                observer.disconnect();
              }
            });
          }, { threshold: 0.15 });

          observer.observe(insightsSection);
        }

        // Fallback: init efter 500ms hvis IO ikke trigges
        setTimeout(() => {
          if (!chartsInitialized || !mapInitialized) {
            try {
              initInsights();
            } catch (err) {
              setStatus(`Init error: ${err.message}`);
              console.error('[Insights] init error (timeout)', err);
            }
          }
        }, 500);
      } catch (err) {
        setStatus(`Init exception: ${err.message}`);
        console.error('[Insights] exception in timeout', err);
      }
    }, 50);
  });
})();
