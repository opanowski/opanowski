(function(){
  var s = document.createElement('style');
  s.textContent = '#donate-fab{position:fixed;bottom:24px;right:20px;z-index:99999;display:flex;flex-direction:column;align-items:flex-end;gap:8px;font-family:sans-serif}'
  + '#donate-panel{display:flex;flex-direction:column;gap:7px;opacity:0;transform:translateY(10px);pointer-events:none;transition:all 0.25s ease}'
  + '#donate-panel.open{opacity:1;transform:translateY(0);pointer-events:auto}'
  + '.dbtn{display:flex;align-items:center;gap:9px;background:#1C1A14;border:1.5px solid #C8972A;border-radius:10px;padding:9px 14px;text-decoration:none;color:#F5F0E8;font-size:12px;font-weight:600;white-space:nowrap;box-shadow:0 4px 16px rgba(0,0,0,0.7);transition:background 0.2s,color 0.2s}'
  + '.dbtn:hover{background:#C8972A;color:#1C1A14}'
  + '.dbtn2{border-color:rgba(200,151,42,0.45)}'
  + '.dbtn-dom{font-size:9px;opacity:0.45;margin-left:auto;padding-left:12px}'
  + '.dlabel{text-align:center;font-size:9px;color:rgba(200,151,42,0.5);letter-spacing:2px;text-transform:uppercase;padding:1px 0}'
  + '#donate-trigger{width:48px;height:48px;border-radius:50%;background:#1C1A14;border:2px solid #C8972A;cursor:pointer;font-size:20px;line-height:1;box-shadow:0 4px 20px rgba(0,0,0,0.8);animation:gpulse 3s ease-in-out infinite;transition:transform 0.2s}'
  + '#donate-trigger:hover{transform:scale(1.08);animation:none}'
  + '@keyframes gpulse{0%,100%{box-shadow:0 4px 20px rgba(0,0,0,0.8),0 0 0 0 rgba(200,151,42,0.5)}50%{box-shadow:0 4px 20px rgba(0,0,0,0.8),0 0 0 10px rgba(200,151,42,0)}}';
  document.head.appendChild(s);

  var fab = document.createElement('div');
  fab.id = 'donate-fab';
  fab.innerHTML = '<div id="donate-panel">'
  + '<a class="dbtn" href="https://trakteer.id/opanowski" target="_blank" rel="noopener"><span style="font-size:15px">🧇</span><span>Trakteer Cendol</span><span class="dbtn-dom">trakteer.id</span></a>'
  + '<a class="dbtn dbtn2" href="https://saweria.co/opanowski" target="_blank" rel="noopener"><span style="font-size:15px">☕</span><span>Saweria Kopi</span><span class="dbtn-dom">saweria.co</span></a>'
  + '<div class="dlabel">Traktir Om Opan</div>'
  + '</div>'
  + '<button id="donate-trigger">☕</button>';
  document.body.appendChild(fab);

  var isOpen = false;

  document.getElementById('donate-trigger').onclick = function(e){
    e.stopPropagation();
    isOpen = !isOpen;
    document.getElementById('donate-panel').classList[isOpen ? 'add' : 'remove']('open');
  };

  document.addEventListener('click', function(e){
    if(!isOpen) return;
    if(!document.getElementById('donate-fab').contains(e.target)){
      isOpen = false;
      document.getElementById('donate-panel').classList.remove('open');
    }
  });
})();
