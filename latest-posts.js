// latest-posts.js — Bunker Opanowski
// Update otomatis setiap tambah post baru
// Selalu tampilkan 3 post TERBARU (urutan: terbaru di atas)

const LATEST_POSTS = [
  {
    number: "012",
    date: "10 Mei 2026",
    title: "Ketika AI Meta Ngacak Bunker",
    subtitle: "Kronologi, investigasi, dan misi penyelamatan website yang hampir lenyap gara-gara AI yang kelewat \"helpful\".",
    tags: ["Incident Report", "Git Rescue", "AI Meta"],
    emoji: "💀",
    url: "blog/blog-meta-ai-bunker-opanowski.html"
  },
  {
    number: "011",
    date: "9 Mei 2026",
    title: "Dua Device, Satu Bunker",
    subtitle: "Update web dari Tablet Linux & Mac Jadul bergantian — satu repo, nol drama, asal ingat pull dulu.",
    tags: ["Multi-Device", "Git Workflow", "Linux"],
    emoji: "📱",
    url: "blog/blog-tablet-mac-workflow.html"
  },
  {
    number: "010",
    date: "sebelumnya",
    title: "Mac Survival Mode",
    subtitle: "Ngerawat MacBook Pro 2015 biar tetap jalan kenceng — thermal paste, storage, dan ritual harian Om Opan.",
    tags: ["MacBook", "Tips", "Hardware"],
    emoji: "🍎",
    url: "blog/blog-log-009-mac-survival.html"
  }
];

// ─── Render ke div#latest-posts-grid ───────────────────────────
document.addEventListener("DOMContentLoaded", function () {
  const grid = document.getElementById("latest-posts-grid");
  if (!grid) return;

  // Kosongkan dulu kalau ada konten hardcode sebelumnya
  grid.innerHTML = "";

  LATEST_POSTS.forEach(function (post) {
    const tagsHTML = post.tags
      .map(function (t) { return '<span class="post-tag">' + t + '</span>'; })
      .join("");

    const card = document.createElement("a");
    card.href = post.url;
    card.className = "post-card";
    card.innerHTML =
      '<div class="post-card-header">' +
        '<span class="post-number">#' + post.number + '</span>' +
        '<span class="post-emoji">' + post.emoji + '</span>' +
      '</div>' +
      '<div class="post-date">' + post.date + '</div>' +
      '<div class="post-title">' + post.title + '</div>' +
      '<div class="post-subtitle">' + post.subtitle + '</div>' +
      '<div class="post-tags">' + tagsHTML + '</div>';

    grid.appendChild(card);
  });
});
