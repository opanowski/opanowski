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
  {
    href: "blog/blog-kenangan-bandung-nyokap-bayu.html",
    badge: "#011",
    tags: ["Catatan Santai", "Keluarga", "In Memoriam"],
    tagColor: "#C8972A",
    tagBg: "rgba(200,151,42,0.15)",
    date: "10 Mei 2026",
    title: "Jejak Memori di Bandung: Tentang Ramen, Nyokap, dan Kepergian sang Bontot",
    desc: "Membuka folder lama, ketemu foto Nyokap nikmatin ramen di Bandung bareng almarhum adik bontot, Bayu. Foto diproses ulang pakai GIMP di Mac jadul — sebagai bentuk penghormatan untuk memori indah kami. Al-Fatihah."
  },
    href: "blog/blog-tablet-mac-workflow.html",
    badge: "#010",
    tags: ["Tips & Trik", "Mac", "Linux"],
    tagColor: "#4caf7d",
    tagBg: "rgba(76,175,125,",
    date: "9 Mei 2026",
    title: "Dua Device, Satu Bunker: Update Web dari Tablet Linux & Mac Jadul Bergantian",
    desc: "Siapa bilang update website harus dari device yang sama? MacBook Pro 2015 + Lenovo Xiaoxin Pad Debian Linux — satu repo, nol drama, workflow multi-device pertama Bunker Opanowski.",
  },
  {
  href: "blog/blog-log-009-mac-survival.html",
  badge: "#009",
  tags: ["Tips & Trik", "Mac"],
  tagColor: "#f5a623",
  tagBg: "rgba(245,166,35,",
  date: "9 Mei 2026",
  title: "SOP Survival Mac Jadul: Rahasia Ngoding 15 Jam Tanpa Meledak",
  desc: "MacBook Pro 2015 masih sanggup tempur 15 jam nonstop? Bisa bray. SOP kearifan lokal Ciracas buat jagain si Mac tetep adem dan performa Quad-Core-nya ga turun.",
},
  {
    href: "log-008-vscode-workflow.html",
    badge: "#008",
    tags: ["Web", "Tips & Trik"],
    tagColor: "#5b8dee",
    tagBg: "rgba(91,141,238,",
    date: "8 Mei 2026",
    title: "Upgrade Workflow: Dari Terminal Buta ke VSCode + Live Server",
    desc: "Drama git rejected, foto hilang, path gambar kacau — semua terjadi hari ini. Plus cara kerja Live Server yang akhirnya bikin workflow Bunker jauh lebih proper.",
  },
{
    href: "digital-legacy-bayu.html",
    badge: "#007",
    tags: ["Web", "Tips & Trik", "Personal"],
    tagColor: "#c8972a",
    tagBg: "rgba(200,151,42,",
    date: "8 Mei 2026",
    title: "Digital Legacy: Jurus Amankan Kenangan Si Bontot Biar Abadi di Dunia Maya",
    desc: "Cara gw menjaga kenangan digital almarhum Bayu (Si Bontot) biar tetap live. Dari backup 3-2-1, legacy contact Facebook, sampai bikin bunker khusus di GitHub Pages.",
  },
  // ──────────────────────────────────────────────
  // TAMBAH ENTRI BARU DI SINI (paling atas = paling baru)
  // ──────────────────────────────────────────────
  {
    href: "blog-pasang-tombol-donasi.html",
    badge: "DevLog",
    tags: ["DevLog", "Web"],
    tagColor: "#f5a623",
    tagBg: "rgba(245,166,35,",
    date: "7 Mei 2026",
    title: "Digital Swasembada: Sekarang Bisa Traktir Kopi di Bunker Opanowski!",
    desc: "Tombol donasi akhirnya landing di Bunker. Dari drama z-index terminal Mac sampai filosofi kenapa karya digital juga butuh 'pupuk'.",
  },
{
    href: "pajak_zonk.html", 
    badge: "#087",
    tags: ["Digital", "Pajak"], 
    tagColor: "#f5a623", 
    tagBg: "rgba(245,166,35,", 
    date: "5 Mei 2026",
    title: "Navigasi Sistem Coretax: Era Baru Perpajakan",
    desc: "Bedah tuntas tampilan dan alur sistem Coretax yang baru. Dokumentasi pengerjaan dari meja kerja Villa Ciracas.",
},
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
