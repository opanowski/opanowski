#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix footer social-links untuk 13 file (kategori 1 + kategori 2).
Jalankan dari dalam folder blog/: python3 fix_footer_part2.py
Idempotent - aman dijalankan ulang, file yang udah ada .social-links di-skip.
"""

SOCIAL_LINKS_HTML = '''  <div class="social-links">
    <a href="https://www.facebook.com/opanowski.ajjah/" target="_blank" rel="noopener">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg> Facebook
    </a>
    <a href="https://www.instagram.com/opanowski/" target="_blank" rel="noopener">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="0.5" fill="currentColor"/></svg> Instagram
    </a>
    <a href="https://www.youtube.com/channel/UCgsJ-a0Cg20xdsn-e_42-yQ" target="_blank" rel="noopener">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.95-1.96C18.88 4 12 4 12 4s-6.88 0-8.59.46A2.78 2.78 0 0 0 1.46 6.42 29 29 0 0 0 1 12a29 29 0 0 0 .46 5.58 2.78 2.78 0 0 0 1.95 1.95C5.12 20 12 20 12 20s6.88 0 8.59-.47a2.78 2.78 0 0 0 1.95-1.95A29 29 0 0 0 23 12a29 29 0 0 0-.46-5.58z"/><polygon points="9.75 15.02 15.5 12 9.75 8.98 9.75 15.02"/></svg> YouTube
    </a>
    <a href="https://www.tiktok.com/@opanowski" target="_blank" rel="noopener">
      <svg width="12" height="12" viewBox="0 0 16 16" fill="currentColor"><path d="M9 0h1.98c.144.715.54 1.617 1.235 2.512C12.895 3.389 13.797 4 15 4v2c-1.753 0-3.07-.814-4-1.829V11a5 5 0 1 1-5-5v2a3 3 0 1 0 3 3z"/></svg> TikTok
    </a>
    <a href="https://www.threads.com/@opanowski" target="_blank" rel="noopener">
      <svg width="12" height="12" viewBox="0 0 16 16" fill="currentColor"><path d="M6.321 6.016c-.27-.18-1.166-.802-1.166-.802.756-1.081 1.753-1.502 3.132-1.502.975 0 1.803.327 2.394.948s.928 1.509 1.005 2.644q.492.207.905.484c1.109.745 1.719 1.86 1.719 3.137 0 2.716-2.226 5.075-6.256 5.075C4.594 16 1 13.987 1 7.994 1 2.034 4.482 0 8.044 0 9.69 0 13.55.243 15 5.036l-1.36.353C12.516 1.974 10.163 1.43 8.006 1.43c-3.565 0-5.582 2.171-5.582 6.79 0 4.143 2.254 6.343 5.63 6.343 2.777 0 4.847-1.443 4.847-3.556 0-1.438-1.208-2.127-1.27-2.127-.236 1.234-.868 3.31-3.644 3.31-1.618 0-3.013-1.118-3.013-2.582 0-2.09 1.984-2.847 3.55-2.847.586 0 1.294.04 1.663.114 0-.637-.54-1.728-1.9-1.728-1.25 0-1.566.405-1.967.868ZM8.716 8.19c-2.04 0-2.304.87-2.304 1.416 0 .878 1.043 1.168 1.6 1.168 1.02 0 2.067-.282 2.232-2.423a6.2 6.2 0 0 0-1.528-.161"/></svg> Threads
    </a>
    <a href="https://x.com/AjjahTyo93183" target="_blank" rel="noopener">
      <svg width="12" height="12" viewBox="0 0 16 16" fill="currentColor"><path d="M12.6.75h2.454l-5.36 6.142L16 15.25h-4.937l-3.867-5.07-4.425 5.07H.316l5.733-6.57L0 .75h5.063l3.495 4.633L12.601.75Zm-.86 13.028h1.36L4.323 2.145H2.865z"/></svg> X
    </a>
    <a href="https://open.spotify.com/show/0IjFXGMOWSwEfNLuZPrqxx" target="_blank" rel="noopener">
      <svg width="12" height="12" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0a8 8 0 1 0 0 16A8 8 0 0 0 8 0m3.669 11.538a.5.5 0 0 1-.686.165c-1.879-1.147-4.243-1.407-7.028-.77a.499.499 0 0 1-.222-.973c3.048-.696 5.662-.397 7.77.892a.5.5 0 0 1 .166.686m.979-2.178a.624.624 0 0 1-.858.205c-2.15-1.321-5.428-1.704-7.972-.932a.625.625 0 0 1-.362-1.194c2.905-.881 6.517-.454 8.986 1.063a.624.624 0 0 1 .206.858m.084-2.268C10.154 5.56 5.9 5.419 3.438 6.166a.748.748 0 1 1-.434-1.432c2.825-.857 7.523-.692 10.492 1.07a.747.747 0 1 1-.764 1.288"/></svg> Spotify
    </a>
  </div>
'''

# Pola A + C + D: gold theme (var(--gold), var(--cream), var(--font-body))
CSS_GOLD = '''.social-links{display:flex;gap:16px;justify-content:center;margin-top:1rem;flex-wrap:wrap}
.social-links a{font-family:var(--font-body);font-size:0.7rem;color:var(--cream);opacity:0.45;text-decoration:none;display:inline-flex;align-items:center;gap:5px;transition:opacity 0.2s,color 0.2s}
.social-links a:hover{opacity:1;color:var(--gold)}
'''

# Pola B: accent theme (var(--accent), var(--text-muted))
CSS_ACCENT = '''.social-links{display:flex;gap:16px;justify-content:center;margin-top:10px;flex-wrap:wrap}
.social-links a{font-family:'Space Mono',monospace;font-size:0.65rem;color:var(--text-muted);text-decoration:none;display:inline-flex;align-items:center;gap:5px;transition:color 0.2s}
.social-links a:hover{color:var(--accent)}
'''

# File eznet: no CSS variables at all, hardcoded hex colors
CSS_EZNET = '''.social-links{display:flex;gap:16px;justify-content:center;margin-top:10px;flex-wrap:wrap}
.social-links a{font-family:'JetBrains Mono',monospace;font-size:0.68rem;color:#3a4060;text-decoration:none;display:inline-flex;align-items:center;gap:5px;transition:color 0.2s}
.social-links a:hover{color:#C8972A}
'''

GROUP_GOLD = [
    "blog-brand-konsistensi.html",
    "blog-evolusi-digital-swasembada.html",
    "blog-evolusi-digital.html",
    "blog-log05-bye-kabel.html",
    "blog-pindah-gambar-ganti-warna.html",
]

GROUP_ACCENT = [
    "blog-log-001-peresmian-markas.html",
    "blog-log-006-analisis-dapur.html",
    "blog-pasang-tombol-donasi.html",
    "blog-seledri-organik.html",
]

GROUP_EZNET = ["blog-eznet-10mbps-bunker-opanowski.html"]


def inject_existing_footer(filename, css_block):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    if "social-links" in content:
        print(f"SKIP (udah ada social-links): {filename}")
        return

    style_idx = content.find("</style>")
    if style_idx == -1:
        print(f"GAGAL (gak ketemu </style>): {filename}")
        return
    content = content[:style_idx] + css_block + content[style_idx:]

    footer_count = content.count("</footer>")
    if footer_count != 1:
        print(f"WARNING ({footer_count}x </footer>, skip insert HTML): {filename}")
        return
    footer_idx = content.find("</footer>")
    content = content[:footer_idx] + SOCIAL_LINKS_HTML + content[footer_idx:]

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"DONE: {filename}")


# === Kategori 2: file yang BELUM punya <footer> sama sekali ===
NEW_FOOTER_CSS = (
    CSS_GOLD
    + """footer{padding:2rem;text-align:center;border-top:1px solid var(--gold-border);font-size:0.7rem;opacity:0.6;font-family:var(--font-body)}
.updated-tag{display:inline-block;background:rgba(255,255,255,0.05);border:1px solid var(--gold-border);border-radius:4px;padding:2px 8px;font-size:0.62rem;color:var(--gold);margin-left:6px}
.live-dot{display:inline-block;width:6px;height:6px;background:var(--green);border-radius:50%;margin-right:4px}
"""
)

NEW_FOOTER_FILES = {
    "blog-coretax-registrasi-drama.html": "5 Mei 2026",
    "blog-evolusi-swasembada.html": "3 Mei 2026",
    "blog-log086-pisang-telur.html": "3 Mei 2026",
}


def inject_brand_new_footer(filename, tanggal):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    if "<footer" in content or "social-links" in content:
        print(f"SKIP (udah ada footer/social-links): {filename}")
        return

    style_idx = content.find("</style>")
    if style_idx == -1:
        print(f"GAGAL (gak ketemu </style>): {filename}")
        return
    content = content[:style_idx] + NEW_FOOTER_CSS + content[style_idx:]

    anchor = '<script src="/opanowski/donate-widget.js"></script>'
    if anchor not in content:
        print(f"GAGAL (gak ketemu anchor donate-widget): {filename}")
        return

    footer_html = (
        "\n\n<footer>\n"
        "  Bunker Opanowski — Log Harian\n"
        f'  <span class="updated-tag"><span class="live-dot"></span>{tanggal}</span>\n'
        + SOCIAL_LINKS_HTML
        + "</footer>\n"
    )
    content = content.replace(anchor, anchor + footer_html, 1)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"DONE (footer baru): {filename}")


if __name__ == "__main__":
    print("--- Pola A/C (gold theme) ---")
    for f in GROUP_GOLD:
        inject_existing_footer(f, CSS_GOLD)

    print("\n--- Pola B (accent theme) ---")
    for f in GROUP_ACCENT:
        inject_existing_footer(f, CSS_ACCENT)

    print("\n--- Pola D (eznet, hardcoded hex) ---")
    for f in GROUP_EZNET:
        inject_existing_footer(f, CSS_EZNET)

    print("\n--- Kategori 2 (footer baru dari nol) ---")
    for f, tgl in NEW_FOOTER_FILES.items():
        inject_brand_new_footer(f, tgl)
