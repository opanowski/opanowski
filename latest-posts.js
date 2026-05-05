/**
 * ============================================================
 *  BUNKER OPANOWSKI — Latest Posts Data
 *  File: latest-posts.js
 *  
 *  ✅ CARA UPDATE:
 *  Kalau ada log/artikel baru, cukup tambahkan object baru
 *  di bagian PALING ATAS array LATEST_POSTS di bawah ini.
 *  index.html akan otomatis nampilkan 3 yang paling atas.
 * ============================================================
 */

const LATEST_POSTS = [

  // ──────────────────────────────────────────────
  // TAMBAH ENTRI BARU DI SINI (paling atas = paling baru)
  // ──────────────────────────────────────────────

  {
    href: "blog-log086-pisang-telur.html",
    badge: "#086",
    tags: ["Urban Farming", "Zero Waste"],
    tagColor: "#4caf7d",       // warna dominan card (border-top & teks)
    tagBg: "rgba(76,175,125,", // prefix rgba untuk bg badge
    date: "3 Mei 2026",
    title: "Tebang Pisang, Mulsa Organik & Panen Telur",
    desc: "Batang pisang dicacah jadi mulsa 'kulkas alami', panen telur aviary lancar, dua Shorts di-crosspost ke belasan grup Urban Farming.",
  },

  {
    href: "blog-evolusi-digital-swasembada.html",
    badge: "Artikel",
    tags: ["Digital", "Filosofi"],
    tagColor: "#5b8dee",
    tagBg: "rgba(91,141,238,",
    date: "3 Mei 2026",
    title: "Evolusi Digital & Swasembada: Dari Ciracas ke Lingkar Arktik",
    desc: "Jangkauan profil meledak +9.622% — 99.8% penonton non-pengikut. Ada pengunjung dari Luleå, Swedia — 10.000km dari Ciracas.",
  },

  {
    href: "blog-seledri-organik.html",
    badge: "#004",
    tags: ["Kebun", "Lifestyle"],
    tagColor: "#4caf7d",
    tagBg: "rgba(76,175,125,",
    date: "4 Mei 2026",
    title: "Seledri di Pot, Healing di Pagi Hari",
    desc: "Secangkir Top Kopi Gula Aren, subuh di Villa Ciracas, dan seledri organik yang tumbuh diam-diam.",
  },

  // ── Entri lama (tidak akan tampil di homepage, tapi tetap disimpan) ──

  {
    href: "blog-brand-konsistensi.html",
    badge: "Artikel",
    tags: ["Filosofi", "Web"],
    tagColor: "#5b8dee",
    tagBg: "rgba(91,141,238,",
    date: "Mei 2026",
    title: "Konsistensi Brand & Optimasi Kerja Digital",
    desc: "Dari akun personal jadi Bunker Opanowski yang utuh — satu nama di 5 platform, baca data Facebook kayak baca kartu motor.",
  },

  {
    href: "blog-log05-bye-kabel.html",
    badge: "#003",
    tags: ["Gadget", "Branding"],
    tagColor: "#ffffff",
    tagBg: "rgba(255,255,255,",
    date: "2 Mei 2026",
    title: "Bye-bye Kabel! Optimasi Transfer Data & Branding Baru",
    desc: "LocalSend kirim 80MB video kebun, TikTok seragam jadi @opanowski, kenaikan tayangan 5.524%.",
  },

  {
    href: "blog-evolusi-digital.html",
    badge: "#002",
    tags: ["GitHub", "AI"],
    tagColor: "#f5a623",
    tagBg: "rgba(245,166,35,",
    date: "Mei 2026",
    title: "Evolusi Digital & Markas Global di GitHub",
    desc: "Migrasi total ke GitHub Pages. Video Sniper Bunglon tembus 14.900 menit tayang, pengunjung dari Singapura, AS, hingga Swedia.",
  },

  {
    href: "log-bunker-opanowski-01.html",
    badge: "#001",
    tags: ["YouTube"],
    tagColor: "#e05a5a",
    tagBg: "rgba(224,90,90,",
    date: "1 Mei 2026",
    title: "Peresmian Markas Digital",
    desc: "Hari bersejarah: 4 pilar konten YouTube resmi dibangun, video perdana diluncurkan, workflow perangkat diatur ulang.",
  },

];

// ============================================================
//  RENDERER — Jangan diubah kecuali mau ganti tampilan card
// ============================================================

(function renderLatestPosts() {
  const container = document.getElementById('latest-posts-grid');
  if (!container) return;

  // Ambil hanya 3 teratas
  const posts = LATEST_POSTS.slice(0, 3);

  container.innerHTML = posts.map(post => {
    const c = post.tagColor;
    const bg = post.tagBg;

    const tagsHTML = post.tags.map(t =>
      `<span style="background:${bg}0.1);color:${c};font-size:0.58rem;letter-spacing:1px;text-transform:uppercase;padding:2px 9px;border-radius:20px">${t}</span>`
    ).join('');

    return `
      <a href="${post.href}" style="text-decoration:none;display:flex;flex-direction:column;background:#0f0f12;border:1px solid rgba(200,151,42,0.18);border-top:3px solid ${c};border-radius:12px;padding:1.6rem;transition:all 0.3s;cursor:pointer"
         onmouseover="this.style.transform='translateY(-4px)';this.style.borderColor='rgba(200,151,42,0.4)'"
         onmouseout="this.style.transform='translateY(0)';this.style.borderColor='rgba(200,151,42,0.18)'">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:0.85rem;flex-wrap:wrap">
          <span style="background:${bg}0.15);color:${c};font-size:0.58rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;padding:2px 9px;border-radius:20px">${post.badge}</span>
          ${tagsHTML}
          <span style="margin-left:auto;font-size:0.6rem;color:${c};opacity:0.6">${post.date}</span>
        </div>
        <h3 style="font-family:'Playfair Display',serif;font-size:1.02rem;color:#F5F0E8;margin-bottom:0.6rem;line-height:1.4">${post.title}</h3>
        <p style="font-size:0.8rem;color:#c8cdd8;line-height:1.7;margin-bottom:1rem;flex:1">${post.desc}</p>
        <span style="font-size:0.7rem;color:${c};letter-spacing:1px;text-transform:uppercase;opacity:0.8">Baca →</span>
      </a>
    `;
  }).join('');
})();
