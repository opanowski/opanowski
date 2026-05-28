#!/bin/bash

# ============================================================
# INJECT TANYA OM OPAN WIDGET
# Jalankan dari root folder opanowski di terminal VS Code
# Usage: bash inject-widget.sh
# ============================================================

# File yang di-skip
SKIP_LIST=(
  "./coming-soon.html"
  "./gudang.html"
  "./index-root.html"
  "./jadwal-konten-bunker-opanowski.html"
)

WIDGET='<!-- TANYA OM OPAN WIDGET -->
<style>
  #omopan-fab{position:fixed;bottom:24px;right:24px;width:56px;height:56px;border-radius:50%;background:#1a7f5a;border:none;cursor:pointer;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 16px rgba(0,0,0,0.22);z-index:9999;transition:transform 0.2s;font-size:24px;}
  #omopan-fab:hover{transform:scale(1.08);}
  #omopan-notif{position:absolute;top:-4px;right:-4px;background:#e24b4a;color:#fff;font-size:10px;border-radius:50%;width:16px;height:16px;display:flex;align-items:center;justify-content:center;font-weight:700;font-family:sans-serif;}
  #omopan-window{position:fixed;bottom:92px;right:24px;width:320px;height:420px;background:#fff;border-radius:16px;box-shadow:0 8px 32px rgba(0,0,0,0.18);display:flex;flex-direction:column;overflow:hidden;z-index:9998;font-family:sans-serif;transition:opacity 0.2s,transform 0.2s;}
  #omopan-window.omopan-hidden{opacity:0;pointer-events:none;transform:translateY(12px);}
  #omopan-header{background:#1a7f5a;padding:12px 14px;display:flex;align-items:center;gap:10px;flex-shrink:0;}
  .omopan-avatar{width:36px;height:36px;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:13px;color:#1a7f5a;flex-shrink:0;}
  .omopan-hname{margin:0;font-size:14px;font-weight:600;color:#fff;line-height:1.3;}
  .omopan-hstatus{margin:0;font-size:11px;color:#a8e6ce;line-height:1.3;}
  #omopan-close{margin-left:auto;background:none;border:none;color:#fff;cursor:pointer;font-size:22px;line-height:1;padding:0;}
  #omopan-messages{flex:1;overflow-y:auto;padding:12px;display:flex;flex-direction:column;gap:8px;background:#f5f5f0;}
  .omopan-bubble{max-width:82%;padding:8px 12px;border-radius:14px;font-size:13px;line-height:1.5;word-break:break-word;}
  .omopan-bot{background:#fff;color:#222;border-bottom-left-radius:4px;align-self:flex-start;box-shadow:0 1px 3px rgba(0,0,0,0.07);}
  .omopan-user{background:#1a7f5a;color:#fff;border-bottom-right-radius:4px;align-self:flex-end;}
  .omopan-typing{color:#888;font-style:italic;}
  #omopan-footer{padding:10px;background:#fff;border-top:0.5px solid #e0e0e0;display:flex;gap:8px;flex-shrink:0;}
  #omopan-input{flex:1;border:0.5px solid #d0d0d0;border-radius:20px;padding:8px 14px;font-size:13px;outline:none;font-family:sans-serif;}
  #omopan-send{background:#1a7f5a;border:none;border-radius:50%;width:36px;height:36px;cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
  #omopan-send svg{width:16px;height:16px;fill:none;stroke:#fff;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;}
</style>
<button id="omopan-fab" onclick="omopanToggle()" aria-label="Tanya Om Opan">🌿<span id="omopan-notif">1</span></button>
<div id="omopan-window" class="omopan-hidden">
  <div id="omopan-header">
    <div class="omopan-avatar">OP</div>
    <div><p class="omopan-hname">Om Opan</p><p class="omopan-hstatus">Online — siap ngobrol!</p></div>
    <button id="omopan-close" onclick="omopanToggle()">×</button>
  </div>
  <div id="omopan-messages">
    <div class="omopan-bubble omopan-bot">Halo bro! Gw Om Opan 👋 Ada yang mau ditanyain soal Bunker, urban farming, atau apapun? Santai aja!</div>
  </div>
  <div id="omopan-footer">
    <input id="omopan-input" placeholder="Ketik pesan..." onkeydown="if(event.key==='\''Enter'\'')omopanSend()" />
    <button id="omopan-send" onclick="omopanSend()" aria-label="Kirim"><svg viewBox="0 0 24 24"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg></button>
  </div>
</div>
<script>
  const OMOPAN_WORKER_URL="https://bunker-omopan.opanowski.workers.dev";
  let omopanHistory=[];
  function omopanToggle(){const w=document.getElementById("omopan-window");const n=document.getElementById("omopan-notif");w.classList.toggle("omopan-hidden");if(n)n.style.display="none";}
  function omopanAddBubble(text,role){const msgs=document.getElementById("omopan-messages");const div=document.createElement("div");div.className="omopan-bubble "+(role==="user"?"omopan-user":"omopan-bot");if(role==="typing"){div.classList.add("omopan-typing");div.id="omopan-typing";}div.textContent=text;msgs.appendChild(div);msgs.scrollTop=msgs.scrollHeight;return div;}
  async function omopanSend(){const input=document.getElementById("omopan-input");const msg=input.value.trim();if(!msg)return;omopanAddBubble(msg,"user");omopanHistory.push({role:"user",content:msg});input.value="";omopanAddBubble("Om Opan lagi mikir...","typing");try{const res=await fetch(OMOPAN_WORKER_URL,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({messages:omopanHistory})});const data=await res.json();const reply=data.reply||"Waduh, error nih gw. Coba lagi ya bro 😅";const t=document.getElementById("omopan-typing");if(t)t.remove();omopanAddBubble(reply,"bot");omopanHistory.push({role:"assistant",content:reply});}catch(e){const t=document.getElementById("omopan-typing");if(t)t.remove();omopanAddBubble("Koneksi error nih bro, coba lagi bentar 😅","bot");}}
</script>'

# ── MULAI PROSES ──────────────────────────────────────────────
echo ""
echo "🌿 Inject Tanya Om Opan Widget"
echo "================================"

COUNT=0
SKIPPED=0

while IFS= read -r -d '' file; do

  # Cek skip list
  SHOULD_SKIP=0
  for skip in "${SKIP_LIST[@]}"; do
    if [ "$file" = "$skip" ]; then
      SHOULD_SKIP=1
      break
    fi
  done
  if [ $SHOULD_SKIP -eq 1 ]; then
    echo "⏭  Skip (excluded): $file"
    ((SKIPPED++))
    continue
  fi

  # Skip kalau widget sudah ada
  if grep -q "omopan-fab" "$file"; then
    echo "⏭  Skip (sudah ada): $file"
    ((SKIPPED++))
    continue
  fi

  # Inject sebelum </body>
  if grep -qi "</body>" "$file"; then
    tmp=$(mktemp)
    awk -v widget="$WIDGET" '
      !done && tolower($0) ~ /<\/body>/ {
        print widget
        done=1
      }
      { print }
    ' "$file" > "$tmp" && mv "$tmp" "$file"
    echo "✅ Done: $file"
    ((COUNT++))
  else
    echo "⚠️  Skip (no </body>): $file"
    ((SKIPPED++))
  fi

done < <(find . -name "*.html" -not -path "./.git/*" -print0)

echo ""
echo "================================"
echo "✅ Berhasil inject : $COUNT file"
echo "⏭  Di-skip         : $SKIPPED file"
echo "================================"
echo ""
echo "Kalau hasilnya oke, jalankan:"
echo "  git add ."
echo '  git commit -m "feat: tambah widget Tanya Om Opan"'
echo "  git push"
echo ""
