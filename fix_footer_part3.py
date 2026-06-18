#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Patch 2 file yang udah punya social links tapi belum lengkap / domain lama.
Jalankan dari dalam folder blog/: python3 fix_footer_part3.py
"""

# ============================================================
# FILE 1: blog-panen-telur-batang-pisang.html
# - TikTok & Threads belum ada icon SVG (cuma teks)
# - Threads masih pakai domain lama threads.net
# - Belum ada X & Spotify
# ============================================================

FILE1 = "blog-panen-telur-batang-pisang.html"

OLD_TIKTOK_THREADS = '''    <a href="https://www.tiktok.com/@opanowski" target="_blank" rel="noopener">TikTok</a>
    <a href="https://www.threads.net/@opanowski" target="_blank" rel="noopener">Threads</a>
  </div>'''

NEW_TIKTOK_THREADS_X_SPOTIFY = '''    <a href="https://www.tiktok.com/@opanowski" target="_blank" rel="noopener">
      <svg width="11" height="11" viewBox="0 0 16 16" fill="currentColor"><path d="M9 0h1.98c.144.715.54 1.617 1.235 2.512C12.895 3.389 13.797 4 15 4v2c-1.753 0-3.07-.814-4-1.829V11a5 5 0 1 1-5-5v2a3 3 0 1 0 3 3z"/></svg> TikTok
    </a>
    <a href="https://www.threads.com/@opanowski" target="_blank" rel="noopener">
      <svg width="11" height="11" viewBox="0 0 16 16" fill="currentColor"><path d="M6.321 6.016c-.27-.18-1.166-.802-1.166-.802.756-1.081 1.753-1.502 3.132-1.502.975 0 1.803.327 2.394.948s.928 1.509 1.005 2.644q.492.207.905.484c1.109.745 1.719 1.86 1.719 3.137 0 2.716-2.226 5.075-6.256 5.075C4.594 16 1 13.987 1 7.994 1 2.034 4.482 0 8.044 0 9.69 0 13.55.243 15 5.036l-1.36.353C12.516 1.974 10.163 1.43 8.006 1.43c-3.565 0-5.582 2.171-5.582 6.79 0 4.143 2.254 6.343 5.63 6.343 2.777 0 4.847-1.443 4.847-3.556 0-1.438-1.208-2.127-1.27-2.127-.236 1.234-.868 3.31-3.644 3.31-1.618 0-3.013-1.118-3.013-2.582 0-2.09 1.984-2.847 3.55-2.847.586 0 1.294.04 1.663.114 0-.637-.54-1.728-1.9-1.728-1.25 0-1.566.405-1.967.868ZM8.716 8.19c-2.04 0-2.304.87-2.304 1.416 0 .878 1.043 1.168 1.6 1.168 1.02 0 2.067-.282 2.232-2.423a6.2 6.2 0 0 0-1.528-.161"/></svg> Threads
    </a>
    <a href="https://x.com/AjjahTyo93183" target="_blank" rel="noopener">
      <svg width="11" height="11" viewBox="0 0 16 16" fill="currentColor"><path d="M12.6.75h2.454l-5.36 6.142L16 15.25h-4.937l-3.867-5.07-4.425 5.07H.316l5.733-6.57L0 .75h5.063l3.495 4.633L12.601.75Zm-.86 13.028h1.36L4.323 2.145H2.865z"/></svg> X
    </a>
    <a href="https://open.spotify.com/show/0IjFXGMOWSwEfNLuZPrqxx" target="_blank" rel="noopener">
      <svg width="11" height="11" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0a8 8 0 1 0 0 16A8 8 0 0 0 8 0m3.669 11.538a.5.5 0 0 1-.686.165c-1.879-1.147-4.243-1.407-7.028-.77a.499.499 0 0 1-.222-.973c3.048-.696 5.662-.397 7.77.892a.5.5 0 0 1 .166.686m.979-2.178a.624.624 0 0 1-.858.205c-2.15-1.321-5.428-1.704-7.972-.932a.625.625 0 0 1-.362-1.194c2.905-.881 6.517-.454 8.986 1.063a.624.624 0 0 1 .206.858m.084-2.268C10.154 5.56 5.9 5.419 3.438 6.166a.748.748 0 1 1-.434-1.432c2.825-.857 7.523-.692 10.492 1.07a.747.747 0 1 1-.764 1.288"/></svg> Spotify
    </a>
  </div>'''

# ============================================================
# FILE 2: blog-swasembada-kreatif-otodidak.html
# - Cuma YouTube(URL beda/lama) + Instagram + Facebook, tanpa icon SVG
# - Belum ada TikTok, Threads, X, Spotify
# ============================================================

FILE2 = "blog-swasembada-kreatif-otodidak.html"

OLD_SOCIAL_BLOCK_F2 = '''  <div class="social-links">
    <a href="https://www.youtube.com/@bunkeropanowski" target="_blank" rel="noopener">▶ YouTube</a>
    <a href="https://www.instagram.com/opanowski/" target="_blank" rel="noopener">◉ Instagram</a>
    <a href="https://www.facebook.com/opanowski.ajjah" target="_blank" rel="noopener">f Facebook</a>
  </div>'''

NEW_SOCIAL_BLOCK_F2 = '''  <div class="social-links">
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
  </div>'''


def patch(filename, old, new, label):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    if new in content:
        print(f"SKIP (udah di-patch): {filename} [{label}]")
        return
    count = content.count(old)
    if count != 1:
        print(f"GAGAL ({count}x match, harus tepat 1x): {filename} [{label}]")
        return
    content = content.replace(old, new)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"DONE: {filename} [{label}]")


if __name__ == "__main__":
    patch(FILE1, OLD_TIKTOK_THREADS, NEW_TIKTOK_THREADS_X_SPOTIFY, "tiktok+threads+x+spotify")
    patch(FILE2, OLD_SOCIAL_BLOCK_F2, NEW_SOCIAL_BLOCK_F2, "full social block")
