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
    title: "Dari Nol Sampai \"Tanya Om Opan\" Bisa Ngobrol Sendiri",
    subtitle: "Perjalanan 2 hari bikin AI chatbot gratis di web statis GitHub Pages. Dari bug 5 jam sampai berhasil deploy Cloudflare Workers AI dengan Llama 3.1 — total biaya: Rp 0.",
    tags: ["AI Chatbot", "Cloudflare Workers", "Tech"],
    emoji: "🤖",
    url: "/opanowski/blog/blog-tanya-om-opan.html"
  },
  {
    number: "026",
    date: "26 Mei 2026",
    title: "Labu Botol: Eksperimen Buah Kampung di Lahan 150m²",
    subtitle: "Banyak yang salah kira ini zucchini. Padahal ini Labu Botol — buah kampung yang gw eksperimenin sendiri di lahan sempit Villa Ciracas. Hasilnya? Diluar ekspektasi.",
    tags: ["Kebun", "Urban Farming", "Villa Ciracas"],
    emoji: "🫙",
    url: "/opanowski/blog/blog-labu-botol.html"
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
      '<h3 style="font-family:\'Playfair Display\',serif;font-size:1.08rem;color:var(--cream,#F5F0E8);line-height:1.4;margin-bottom:0.75rem;font-weight:700">' +
        post.title +
      '</h3>' +
      '<p style="font-size:0.82rem;color:var(--text-muted,#b0b5c8);line-height:1.85;margin-bottom:1rem">' +
        post.subtitle +
      '</p>' +
      '<div style="display:flex;flex-wrap:wrap;gap:0.4rem;margin-bottom:1.1rem">' + tagsHTML + '</div>' +
      '<div style="font-size:0.72rem;color:' + ac.readColor + ';font-weight:600;letter-spacing:0.5px">' +
        'Baca selengkapnya &rarr;' +
      '</div>';

    grid.appendChild(card);
  });
});
