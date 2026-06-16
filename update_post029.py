#!/usr/bin/env python3
"""
update_post029.py
Update latest-posts.js + blog/index.html untuk post #029: Panas Jakarta
Jalanin dari folder: ~/Desktop/opanowski/
"""

import re

# ── 1. UPDATE latest-posts.js ─────────────────────────────────────────────────

JS_PATH = "latest-posts.js"

new_js = """// latest-posts.js — Bunker Opanowski
// Update otomatis setiap tambah post baru
// Selalu tampilkan 3 post TERBARU (urutan: terbaru di atas)

// Accent per kartu: biru, gold, orange — berulang kalau lebih dari 3
const CARD_ACCENTS = [
  {
    border:      "rgba(91,141,238,0.5)",
    bg:          "rgba(91,141,238,0.06)",
    tagBg:       "rgba(91,141,238,0.12)",
    tagBorder:   "rgba(91,141,238,0.35)",
    tagColor:    "#5b8dee",
    readColor:   "#5b8dee",
    hoverBorder: "rgba(91,141,238,0.85)",
    hoverBg:     "rgba(91,141,238,0.11)"
  },
  {
    border:      "rgba(200,151,42,0.55)",
    bg:          "rgba(200,151,42,0.06)",
    tagBg:       "rgba(200,151,42,0.12)",
    tagBorder:   "rgba(200,151,42,0.35)",
    tagColor:    "#C8972A",
    readColor:   "#C8972A",
    hoverBorder: "rgba(200,151,42,0.85)",
    hoverBg:     "rgba(200,151,42,0.11)"
  },
  {
    border:      "rgba(245,166,35,0.50)",
    bg:          "rgba(245,166,35,0.05)",
    tagBg:       "rgba(245,166,35,0.12)",
    tagBorder:   "rgba(245,166,35,0.35)",
    tagColor:    "#f5a623",
    readColor:   "#f5a623",
    hoverBorder: "rgba(245,166,35,0.80)",
    hoverBg:     "rgba(245,166,35,0.10)"
  }
];

const LATEST_POSTS = [
  {
    number: "029",
    date: "11 Jun 2026",
    title: "Ngoding Rasa Sauna: Jakarta 35° dan Semangat yang Gak Kendor",
    subtitle: "Termometer 35 derajat di dalam Bunker, kipas cuma mindahin udara panas, Mac jadul berasa heater. Tapi pejuang konten Ciracas pantang mundur — ini cerita survive ngoding di Jakarta yang lagi menyala.",
    tags: ["Lifestyle", "Jakarta", "Villa Ciracas"],
    emoji: "🔥",
    url: "/opanowski/blog/blog-panas-jakarta.html"
  },
  {
    number: "028",
    date: "3 Jun 2026",
    title: "Anggur Bali Masuk Fase Veraison — Deg-degan Nunggu yang Siap",
    subtitle: "Sebagian udah ungu tua, sebagian masih hijau. Nggak bisa dipaksa, nggak bisa diakali. Fase veraison ini titik balik sebelum panen — tinggal sabar & amatin.",
    tags: ["Urban Farming", "Kebun", "Villa Ciracas"],
    emoji: "🍇",
    url: "/opanowski/blog/blog-anggur-bali-veraison.html"
  },
  {
    number: "027",
    date: "29 Mei 2026",
    title: "Dari Nol Sampai \\"Tanya Om Opan\\" Bisa Ngobrol Sendiri",
    subtitle: "Perjalanan 2 hari bikin AI chatbot gratis di web statis GitHub Pages. Dari bug 5 jam sampai berhasil deploy Cloudflare Workers AI dengan Llama 3.1 — total biaya: Rp 0.",
    tags: ["AI Chatbot", "Cloudflare Workers", "Tech"],
    emoji: "🤖",
    url: "/opanowski/blog/blog-tanya-om-opan.html"
  },
];
"""

# Baca file asli, ambil bagian render (dari "// ─── Render" sampai akhir)
with open(JS_PATH, "r", encoding="utf-8") as f:
    original = f.read()

render_start = original.find("// ─── Render")
if render_start == -1:
    render_start = original.find("document.addEventListener")

render_block = original[render_start:]
final_js = new_js + "\n" + render_block

with open(JS_PATH, "w", encoding="utf-8") as f:
    f.write(final_js)

print("✅ latest-posts.js updated — #029 masuk posisi 1")


# ── 2. UPDATE blog/index.html ─────────────────────────────────────────────────

INDEX_PATH = "blog/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 2a. Counter Total Entri: 27 → 28
html = html.replace(
    '<div class="stat-num">27</div><div class="stat-label">Total Entri</div>',
    '<div class="stat-num">28</div><div class="stat-label">Total Entri</div>'
)
print("✅ Counter Total Entri: 27 → 28")

# 2b. stat-visible: 28 → 29
html = html.replace(
    '<div class="stat-num" id="stat-visible">28</div>',
    '<div class="stat-num" id="stat-visible">29</div>'
)
print("✅ stat-visible: 28 → 29")

# 2c. visible-count span: 28 entri → 29 entri
html = html.replace(
    '<span class="count" id="visible-count">28 entri</span>',
    '<span class="count" id="visible-count">29 entri</span>'
)
print("✅ visible-count: 28 → 29 entri")

# 2d. Tambah log-card #029 setelah anchor komentar TAMBAH ENTRI BARU
new_log_card = """
<!-- LOG #029 — Panas Jakarta -->
  <a class="log-card" id="entry-log029" href="blog-panas-jakarta.html" data-tags="santai">
    <div class="log-card-top">
      <span class="log-num-badge">#029</span>
      <span class="log-date"><span class="live-dot"></span>Rabu, 11 Jun 2026</span>
      <div class="log-tags">
        <span class="tag tag-santai">🔥 Lifestyle</span>
        <span class="tag tag-santai">☕ Catatan Santai</span>
      </div>
    </div>
    <div class="log-title">Ngoding Rasa Sauna: Jakarta 35° dan Semangat yang Gak Kendor</div>
    <div class="log-desc">Termometer 35 derajat di dalam Bunker, kipas cuma mindahin udara panas, Mac jadul berasa heater. Tapi pejuang konten Ciracas pantang mundur. 🔥</div>
    <div class="log-card-bottom">
      <div class="log-sections">
        <span class="section-pill">Jakarta 35°C</span>
        <span class="section-pill">Survive Ngoding</span>
        <span class="section-pill">Lifestyle Bunker</span>
      </div>
      <span class="log-arrow">Baca →</span>
    </div>
  </a>

"""

anchor = "<!-- LOG #028 — Anggur Bali Veraison -->"
if anchor in html:
    html = html.replace(anchor, new_log_card + anchor)
    print("✅ log-card #029 ditambahkan sebelum #028")
else:
    print("⚠️  Anchor LOG #028 tidak ditemukan — cek manual!")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("\n🎉 Selesai! Cek di Live Server, lalu:")
print("   git pull origin main")
print("   git add blog/blog-panas-jakarta.html latest-posts.js blog/index.html")
print("   git commit -m 'Add post #029: Ngoding Rasa Sauna — Jakarta 35 Derajat'")
print("   git push origin main")
print("   (tunggu 1-2 menit) → python3 update_knowledge.py")
