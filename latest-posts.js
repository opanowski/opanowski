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
    number: "020",
    date: "18 Mei 2026",
    title: "Konversi M4A ke MP3 di Mac — Gratis, Cepat, Tanpa Drama",
    subtitle: "Tiga cara konversi audio M4A ke MP3 di Mac tanpa biaya sepeser pun: Terminal built-in, FFmpeg batch, sampai Audacity. MacBook 2015 gw masih sanggup handle semuanya.",
    tags: ["Audio", "Mac", "FFmpeg"],
    emoji: "🎙️",
    url: "/opanowski/blog/blog-konversi-m4a-mp3.html"
  },
  {
    number: "019",
    date: "17 Mei 2026",
    title: "Website Pribadi Ala Opanowski — 3 Hari, 3 AI, Tanpa Coding",
    subtitle: "Siapa bilang bikin website harus ngerti coding dulu? Autodidak dari Ciracas bikin website pribadi yang proper dalam 3 hari — modal tiga AI sekaligus dan secangkir kopi.",
    tags: ["AI", "Web", "Autodidak"],
    emoji: "🌐",
    url: "/opanowski/blog/blog-website-ai-3hari.html"
  },
  {
    number: "018",
    date: "17 Mei 2026",
    title: "Lalat Hijau Itu Lagi Ngurusin Bunga Gue — dan Gue Hampir Ngusirnya",
    subtitle: "Ternyata ada yang lebih tahu soal bunga kedondong gue daripada gue sendiri. Namanya lalat. Lalat hijau. Penyerbuk tanpa kredit, dari teras Villa Ciracas.",
    tags: ["Kebun & Alam", "Teras Rumah", "Fakta Random"],
    emoji: "🪰",
    url: "/opanowski/blog/blog-lalat-hijau-kedondong-mini.html"
  }
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
