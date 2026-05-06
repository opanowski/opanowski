(function(){
  var s = document.createElement('style');
  s.textContent = '#donate-fab{position:fixed;bottom:24px;right:20px;z-index:999999;display:flex;flex-direction:column;align-items:flex-end;gap:10px;font-family:sans-serif}'
  + '#donate-panel{display:flex;flex-direction:column;gap:8px;opacity:0;transform:translateY(12px);pointer-events:none;transition:all 0.25s ease}'
  + '#donate-panel.open{opacity:1!important;transform:translateY(0)!important;pointer-events:auto!important}'
  + '.dbtn{display:flex;align-items:center;gap:10px;background:#C8972A;border-radius:10px;padding:11px 18px;text-decoration:none;color:#1C1A14;font-size:13px;font-weight:700;white-space:nowrap;box-shadow:0 4px 16px rgba(0,0,0,0.8)}'
  + '.dbtn:hover{background:#e0aa30}'
  + '.dbtn-dom{font-size:10px;opacity:0.6;margin-left:auto;padding-left:10px}'
  + '.dlabel{text-align:center;font-size:10px;color:#C8972A;letter-spacing:2px;text-transform:uppercase;padding:2px 0}'
  + '#donate-trigger{width:52px;height:52px;border-radius:50%;background:#1C1A14;border:2px solid #C8972A;cursor:pointer;font-size:22px;line-height:1;box-shadow:0 4px 20px rgba(0,0,0,0.8);animation:gpulse 3s ease-in-out infinite}'
  + '#donate-trigger:hover{transform:scale(1.08);animation:none}'
  + '@keyframes gpulse{0%,100%{box-shadow:0 4px 20px rgba(0,0,0,0.8),0 0 0 0 rgba(200,151,42,0.5)}50%{box-shadow:0 4px 20px rgba(0,0,0,0.8),0 0 0 10px rgba(200,151,42,0)}}';
  document.head.appendChild(s);

  var fab = document.createElement('div');
  fab.id = 'donate-fab';
  fab.innerHTML = '<div id="donate-panel">'
  + '<a class="dbtn" href="https://trakteer.id/opanowski" target="_blank" rel="noopener"><span>🧇</span><span>Trakteer Cendol</span><span class="dbtn-dom">trakteer.id</span></a>'
  + '<a class="dbtn" href="https://saweria.co/opanowski" target="_blank" rel="noopener"><span>☕</span><span>Saweria Kopi</span><span class="dbtn-dom">saweria.co</span></a>'
  + '<div class="dlabel">Traktir Om Opan</div>'
  + '</div>'
  + '<button id="donate-trigger">☕</button>';
  document.body.appendChild(fab);

  var isOpen = false;

  document.getElementById('donate-trigger').onclick = function(e){
    e.stopPropagation();
    isOpen = !isOpen;
    var panel = document.getElementById('donate-panel');
    if(isOpen){
      panel.classList.add('open');
    } else {
      panel.classList.remove('open');
    }
  };

  document.addEventListener('click', function(e){
    if(!isOpen) return;
    var fab = document.getElementById('donate-fab');
    if(fab && !fab.contains(e.target)){
      isOpen = false;
      document.getElementById('donate-panel').classList.remove('open');
    }
  });
})();
