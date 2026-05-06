(function(){
  var style = document.createElement('style');
  style.textContent = '#donate-fab{position:fixed;bottom:24px;right:20px;z-index:99999;display:flex;flex-direction:column;align-items:flex-end;gap:10px;font-family:sans-serif}'
  + '#donate-panel{display:flex;flex-direction:column;gap:8px;opacity:0;transform:translateY(12px);pointer-events:none;transition:all 0.25s ease}'
  + '#donate-panel.open{opacity:1;transform:translateY(0);pointer-events:auto}'
  + '.dbtn{display:flex;align-items:center;gap:10px;background:#C8972A;border:none;border-radius:10px;padding:11px 18px;text-decoration:none;color:#1C1A14;font-size:13px;font-weight:700;white-space:nowrap;box-shadow:0 4px 16px rgba(0,0,0,0.7);cursor:pointer}'
  + '.dbtn:hover{background:#e0aa30;color:#0f0e0a}'
  + '.dbtn span.ico{font-size:16px}'
  + '.dbtn span.dom{font-size:10px;opacity:0.6;margin-left:auto;padding-left:10px}'
  + '.dlabel{text-align:center;font-size:10px;color:#C8972A;letter-spacing:2px;text-transform:uppercase}'
  + '#donate-trigger{width:52px;height:52px;border-radius:50%;background:#C8972A;border:none;cursor:pointer;font-size:22px;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 20px rgba(0,0,0,0.8);animation:gpulse 3s ease-in-out infinite;transition:transform 0.2s}'
  + '#donate-trigger:hover{transform:scale(1.08);animation:none}'
  + '@keyframes gpulse{0%,100%{box-shadow:0 4px 20px rgba(0,0,0,0.8),0 0 0 0 rgba(200,151,42,0.5)}50%{box-shadow:0 4px 20px rgba(0,0,0,0.8),0 0 0 10px rgba(200,151,42,0)}}';
  document.head.appendChild(style);

  var fab = document.createElement('div');
  fab.id = 'donate-fab';
  fab.innerHTML = ''
    + '<div id="donate-panel">'
    + '<a class="dbtn" href="https://trakteer.id/opanowski" target="_blank" rel="noopener"><span class="ico">🧇</span><span>Trakteer Cendol</span><span class="dom">trakteer.id</span></a>'
    + '<a class="dbtn" href="https://saweria.co/opanowski" target="_blank" rel="noopener"><span class="ico">☕</span><span>Saweria Kopi</span><span class="dom">saweria.co</span></a>'
    + '<div class="dlabel">Traktir Om Opan</div>'
    + '</div>'
    + '<button id="donate-trigger">☕</button>';
  document.body.appendChild(fab);

  var open = false;
  document.getElementById('donate-trigger').addEventListener('click', function(e){
    e.stopPropagation();
    open = !open;
    document.getElementById('donate-panel').className = open ? 'open' : '';
    this.style.background = open ? '#1C1A14' : '#C8972A';
    this.style.border = open ? '2px solid #C8972A' : 'none';
  });
  document.addEventListener('click', function(e){
    if(!open) return;
    var fab = document.getElementById('donate-fab');
    if(fab && !fab.contains(e.target)){
      document.getElementById('donate-trigger').click();
    }
  });
})();
