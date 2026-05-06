(function(){
  var style = document.createElement('style');
  style.textContent = `
    #donate-fab {
      position: fixed; bottom: 24px; right: 20px; z-index: 9999;
      display: flex; flex-direction: column; align-items: flex-end; gap: 10px;
      font-family: 'DM Sans', 'Syne', sans-serif;
      width: fit-content;
      pointer-events: none;
    }
    #donate-panel {
      display: flex; flex-direction: column; gap: 8px;
      opacity: 0; transform: translateY(12px) scale(0.95);
      pointer-events: none;
      transition: opacity 0.28s ease, transform 0.28s ease;
      width: fit-content;
    }
    #donate-panel.open {
      opacity: 1; transform: translateY(0) scale(1);
      pointer-events: auto;
    }
    .donate-btn {
      display: flex; align-items: center; gap: 10px;
      background: rgba(28,26,20,0.92); border: 1.5px solid #C8972A;
      border-radius: 10px; padding: 10px 16px;
      text-decoration: none; color: #F5F0E8;
      font-size: 0.82rem; font-weight: 500;
      white-space: nowrap; box-shadow: 0 4px 20px rgba(0,0,0,0.5);
      transition: background 0.2s, border-color 0.2s, color 0.2s;
      pointer-events: auto;
    }
    .donate-btn:hover {
      background: #C8972A !important; color: #1C1A14 !important;
      border-color: #C8972A !important;
    }
    .donate-btn-domain {
      font-size: 10px; opacity: 0.5; margin-left: auto; padding-left: 10px;
    }
    .donate-label {
      text-align: center; font-size: 0.6rem;
      color: rgba(200,151,42,0.5); letter-spacing: 1.5px;
      text-transform: uppercase; padding: 2px 0;
    }
    #donate-trigger {
      width: 52px; height: 52px; border-radius: 50%;
      background: #1C1A14; border: 1.5px solid #C8972A;
      cursor: pointer; font-size: 22px;
      display: flex; align-items: center; justify-content: center;
      box-shadow: 0 4px 20px rgba(0,0,0,0.6);
      animation: goldPulse 3s ease-in-out infinite;
      transition: transform 0.2s;
      pointer-events: auto;
    }
    #donate-trigger:hover { transform: scale(1.08); animation: none; }
    #donate-trigger:active { transform: scale(0.96); }
    @keyframes goldPulse {
      0%,100% { box-shadow: 0 4px 20px rgba(0,0,0,0.6), 0 0 0 0 rgba(200,151,42,0.4); }
      50%      { box-shadow: 0 4px 20px rgba(0,0,0,0.6), 0 0 0 8px rgba(200,151,42,0); }
    }
  `;
  document.head.appendChild(style);

  var fab = document.createElement('div');
  fab.id = 'donate-fab';
  fab.innerHTML = `
    <div id="donate-panel">
      <a class="donate-btn" href="https://trakteer.id/opanowski" target="_blank" rel="noopener">
        <span style="font-size:16px">🧇</span>
        <span>Trakteer Cendol</span>
        <span class="donate-btn-domain">trakteer.id</span>
      </a>
      <a class="donate-btn" href="https://saweria.co/opanowski" target="_blank" rel="noopener">
        <span style="font-size:16px">☕</span>
        <span>Saweria Kopi</span>
        <span class="donate-btn-domain">saweria.co</span>
      </a>
      <div class="donate-label">Traktir Om Opan ☕</div>
    </div>
    <button id="donate-trigger" title="Traktir Om Opan">☕</button>
  `;
  document.body.appendChild(fab);

  var open = false;
  document.getElementById('donate-trigger').addEventListener('click', function(e){
    e.stopPropagation();
    open = !open;
    var panel = document.getElementById('donate-panel');
    var btn = document.getElementById('donate-trigger');
    if(open){
      panel.classList.add('open');
      btn.style.background = '#C8972A';
      btn.style.animation = 'none';
    } else {
      panel.classList.remove('open');
      btn.style.background = '#1C1A14';
      btn.style.animation = 'goldPulse 3s ease-in-out infinite';
    }
  });
  document.addEventListener('click', function(e){
    if(!open) return;
    var fab = document.getElementById('donate-fab');
    if(fab && !fab.contains(e.target)){
      document.getElementById('donate-trigger').click();
    }
  });
})();
