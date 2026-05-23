// latest-posts.js — Bunker Opanowski
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
    number: "024",
    date: "26 Mei 2026",
    title: "Esensi Swasembada Kreatif: Menikmati Proses Otodidak Tanpa Harus Terbawa Arus",
    subtitle: "Ramai kursus AI instan di sosmed, tapi Om Opan tetep di jalur berdikari. Otodidak bukan soal pelit ilmu — ini soal ritme, kebebasan, dan momen nonton bareng Nyokap yang tak ternilai.",
    tags: ["Filosofi", "Otodidak", "Villa Ciracas"],
    emoji: "✍️",
    url: "/opanowski/blog/blog-swasembada-kreatif-otodidak.html"
  },
  {
    number: "023",
    date: "23 Mei 2026",
    title: "Siasat Urban Farming ala Bunker Opanowski: Angkat Konblok, Bio-Canopy Pare Liar",
    subtitle: "Angkat konblok, tanam langsung ke bumi, pare hutan jadi bio-canopy. Kebun multifungsi: sekalian bengkel, cucian motor, jemuran — semua bisa satu area asal manajemennya bener.",
    tags: ["Urban Farming", "Low Cost", "Villa Ciracas"],
    emoji: "🌿",
    url: "/opanowski/blog/blog-siasat-urban-farming.html"
  },
  {
    number: "022",
    date: "21 Mei 2026",
    title: "Pengangguran tapi Super Sibuk: Mengubah MacBook Jadul Jadi Mesin Kreatif Organik",
    subtitle: "Evaluasi 3 minggu balik lagi ngulik konten: dari yang tadinya cuma buka 7 tab, sekarang 3 windows × belasan tab aktif. Autentisitas > kamera 4K, retention rate tembus 300%.",
    tags: ["MacBook Jadul", "Konten", "Villa Ciracas"],
    emoji: "📊",
    url: "/opanowski/blog/blog-pengangguran-super-sibuk.html"
  },
];

// ─── Render ke div#latest-posts-grid ───────────────────────────
document.addEventListener("DOMContentLoaded", function () {
  const grid = document.getElementById("latest-posts-grid");
  if (!grid) return;

  grid.innerHTML = "";

  LATEST_POSTS.forEach(function (post, i) {
    var ac = CARD_ACCENTS[i % CARD_ACCENTS.length];

    var tagsHTML = post.tags
      .map(function (t) {
        return '<span style="' +
          'font-size:0.62rem;' +
          'background:' + ac.tagBg + ';' +
          'border:1px solid ' + ac.tagBorder + ';' +
          'color:' + ac.tagColor + ';' +
          'padding:0.2rem 0.65rem;' +
          'border-radius:20px;' +
          'letter-spacing:0.5px;' +
          'font-weight:600;' +
        '">' + t + '</span>';
      })
      .join("");

    var card = document.createElement("a");
    card.href = post.url;
    card.style.cssText =
      'display:block;' +
      'text-decoration:none;' +
      'background:' + ac.bg + ';' +
      'border:1px solid ' + ac.border + ';' +
      'border-radius:14px;' +
      'padding:1.6rem;' +
      'transition:all 0.25s ease;' +
      'box-shadow:0 0 18px ' + ac.border + ';';

    card.onmouseenter = function () {
      this.style.borderColor = ac.hoverBorder;
      this.style.background   = ac.hoverBg;
      this.style.boxShadow    = '0 0 28px ' + ac.hoverBorder;
      this.style.transform    = 'translateY(-3px)';
    };
    card.onmouseleave = function () {
      this.style.borderColor = ac.border;
      this.style.background   = ac.bg;
      this.style.boxShadow    = '0 0 18px ' + ac.border;
      this.style.transform    = 'translateY(0)';
    };

    card.innerHTML =
      '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.6rem">' +
        '<span style="font-size:0.65rem;color:' + ac.tagColor + ';letter-spacing:2px;text-transform:uppercase;font-weight:700">' +
          post.date + ' &middot; #' + post.number +
        '</span>' +
        '<span style="font-size:1.3rem">' + post.emoji + '</span>' +
      '</div>' +
      '<h3 style="font-family:\'Playfair Display\',serif;font-size:1.08rem;color:#F5F0E8;line-height:1.4;margin-bottom:0.75rem;font-weight:700">' +
        post.title +
      '</h3>' +
      '<p style="font-size:0.82rem;color:#b0b5c8;line-height:1.85;margin-bottom:1rem">' +
        post.subtitle +
      '</p>' +
      '<div style="display:flex;flex-wrap:wrap;gap:0.4rem;margin-bottom:1.1rem">' + tagsHTML + '</div>' +
      '<div style="font-size:0.72rem;color:' + ac.readColor + ';font-weight:600;letter-spacing:0.5px">' +
        'Baca selengkapnya &rarr;' +
      '</div>';

    grid.appendChild(card);
  });
});
