# TEMPLATE-BLOG — Bunker Opanowski
Referensi template blog untuk Claude. Lampirkan file ini tiap mau buat blog baru.

---

## IDENTITAS TEMPLATE

- **Nama:** Bunker Opanowski Dark Theme v1
- **Bahasa:** Indonesia, gaya santai (gw/bray), suara "Om Opan"
- **Base URL:** `https://opanowski.github.io/opanowski/`
- **Lokasi:** Villa Ciracas, Jakarta Timur

---

## FONT & WARNA

```css
/* Google Fonts — load via <link> di tiap blog (wajib, meski shared.css juga ada @import) */
Syne (400/600/800)          → body text utama
Playfair Display (400/700i) → judul, h2, quote
Space Mono (400/700/400i)   → label, tag, meta, kode

/* CSS Variables — WAJIB di-define ulang di <style> tiap blog */
/* shared.css punya nilai berbeda; override ini adalah SOP, bukan bug */
:root {
  --bg:         #0f1117;
  --surface:    #1a1d27;
  --surface2:   #22263a;
  --accent:     #f5a623;
  --gold:       #C8972A;
  --cream:      #F5F0E8;
  --text:       #e8eaf0;
  --text-muted: #8b8fa8;
  --green:      #4caf7d;
  --border:     #2e3248;
  --blue:       #5b8dee;
  --red:        #e05a5a;       /* ← tambahan wajib */
  --orange:     #f07833;       /* ← tambahan wajib */
  --font-display: 'Playfair Display', serif;   /* ← tambahan wajib */
  --font-mono:    'Space Mono', monospace;      /* ← tambahan wajib */
}
```

---

## STRUKTUR FILE

```
blog/blog-[slug].html     ← file blog baru
shared.css                ← CSS global (jangan diubah)
images/[foto].webp        ← foto konten
images/ekspresi/          ← 10 foto ekspresi Om Opan (.webp)
```

Path gambar dari dalam folder `blog/`:
- Foto konten: `../images/nama-foto.webp`
- Ekspresi: `../images/ekspresi/ekspresi_nama.webp`

---

## STRUKTUR `<head>`

```html
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>[Judul] — Bunker Opanowski</title>
<meta name="description" content="[120–150 karakter]">
<meta property="og:title" content="[Judul OG]">
<meta property="og:description" content="[Deskripsi OG]">
<meta property="og:type" content="article">
<meta property="og:url" content="https://opanowski.github.io/opanowski/blog/blog-[slug].html">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>[EMOJI]</text></svg>">
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Syne:wght@400;600;800&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../shared.css">
<style>
  :root { /* semua variables di atas */ }

  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { background: var(--bg); color: var(--text); font-family: 'Syne', sans-serif; min-height: 100vh; line-height: 1.8; }

  /* ... semua CSS komponen di bawah ... */
</style>
</head>
```

**Wajib ada:** `<link rel="icon">` emoji yang sesuai tema blog.

---

## STRUKTUR HTML (urutan wajib)

```
1. <head>          — meta, og:tags, icon emoji, fonts, shared.css, <style>
2. <header>        — sticky, back link ke Log Harian
3. .hero           — hero-bg-pattern + [hero-photo opsional] + hero-emoji-bg + hero-overlay
                     (hero-tags: tag-pill, hero-title dengan <em>, hero-meta + live-dot)
4. .container      — max-width 720px, padding 3rem 1.5rem 5rem
   └ .artikel-body — konten blog
5. .post-nav       — navigasi prev/next
6. <footer>        — live-dot + tanggal + social links
7. Utterances      — komentar
8. donate-widget   — /opanowski/donate-widget.js
```

---

## CSS WAJIB DI TIAP BLOG

CSS berikut **selalu di-define di `<style>`** tiap blog — tidak datang dari shared.css:

```css
/* RESET & BODY */
* { margin: 0; padding: 0; box-sizing: border-box; }
body { background: var(--bg); color: var(--text); font-family: 'Syne', sans-serif; min-height: 100vh; line-height: 1.8; }

/* HEADER */
header {
  background: linear-gradient(135deg, #1a1d27 0%, #0f1117 100%);
  border-bottom: 2px solid var(--accent); /* warna bisa ganti sesuai tema */
  padding: 22px 24px 18px;
  position: sticky; top: 0; z-index: 100;
}
.back-link {
  display: inline-flex; align-items: center; gap: 6px;
  font-family: var(--font-mono); font-size: 0.7rem;
  color: var(--text-muted); text-decoration: none; transition: color 0.2s;
}
.back-link:hover { color: var(--accent); }

/* HERO */
.hero { position: relative; background: [gradient sesuai tema]; min-height: 380px; display: flex; align-items: flex-end; overflow: hidden; }
.hero-bg-pattern { position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.05; background-image: repeating-linear-gradient(45deg, [warna] 0px, [warna] 1px, transparent 1px, transparent 35px); }
.hero-emoji-bg { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 13rem; opacity: 0.05; pointer-events: none; user-select: none; }
.hero-overlay { position: relative; z-index: 2; width: 100%; padding: 2.5rem 2rem; background: linear-gradient(to top, rgba(15,17,23,0.98) 0%, rgba(15,17,23,0.4) 80%, transparent 100%); }
.hero-tags { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 1rem; }
.tag-pill { background: rgba(200,151,42,0.15); border: 1px solid rgba(200,151,42,0.4); color: var(--gold); font-size: 0.6rem; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; padding: 3px 10px; border-radius: 20px; font-family: var(--font-mono); }
.tag-pill.green  { background: rgba(76,175,125,0.15);  border-color: rgba(76,175,125,0.4);  color: var(--green); }
.tag-pill.blue   { background: rgba(91,141,238,0.15);  border-color: rgba(91,141,238,0.4);  color: var(--blue); }
.tag-pill.red    { background: rgba(224,90,90,0.15);   border-color: rgba(224,90,90,0.4);   color: var(--red); }
.tag-pill.orange { background: rgba(240,120,51,0.15);  border-color: rgba(240,120,51,0.4);  color: var(--orange); }
.hero-title { font-family: var(--font-display); font-size: clamp(1.8rem, 4vw, 2.8rem); color: var(--cream); line-height: 1.2; margin-bottom: 0.75rem; }
.hero-title em { color: var(--accent); font-style: italic; } /* ganti warna sesuai tema */
.hero-meta { font-family: var(--font-mono); font-size: 0.68rem; color: var(--text-muted); display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }
.live-dot { display: inline-block; width: 6px; height: 6px; background: var(--accent); border-radius: 50%; animation: pulse 2s infinite; }
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.4} }

/* LAYOUT */
.container { max-width: 720px; margin: 0 auto; padding: 3rem 1.5rem 5rem; }
.artikel-body p { font-size: 0.95rem; line-height: 1.9; color: var(--text); margin-bottom: 1.5rem; opacity: 0.88; }
.artikel-body h2 { font-family: var(--font-display); font-size: 1.4rem; color: var(--cream); margin: 2.5rem 0 1rem; padding-bottom: 0.5rem; border-bottom: 1px solid var(--border); }
.artikel-body h2 em { color: var(--accent); font-style: italic; }

/* EKSPRESI CARD — selalu define ini */
.ekspresi-card { display: flex; align-items: center; gap: 1rem; margin: 1.2rem 0; padding: 0.9rem 1.2rem; border-radius: 10px; }
.ekspresi-card img { width: 72px; height: 72px; object-fit: cover; border-radius: 8px; flex-shrink: 0; border: 2px solid rgba(200,151,42,0.3); }
.ekspresi-card p { margin: 0 !important; font-size: 0.85rem !important; color: var(--text-muted) !important; font-style: italic; line-height: 1.7 !important; opacity: 1 !important; }
/* Modifier — border warna sesuai mood */
.ekspresi-card.marah    img { border-color: rgba(224,90,90,0.4); }
.ekspresi-card.semangat img { border-color: rgba(76,175,125,0.4); }
.ekspresi-card.biru     img { border-color: rgba(91,141,238,0.4); }
/* (tambah modifier lain kalau perlu) */

/* KESIMPULAN */
.kesimpulan-box { margin: 2.5rem 0 0; padding: 1.5rem 1.8rem; border-radius: 12px; border: 1px solid rgba(200,151,42,0.3); background: linear-gradient(135deg, rgba(200,151,42,0.05), rgba(200,151,42,0.02)); }
.kesimpulan-box h3 { font-family: var(--font-mono); font-size: 0.7rem; font-weight: 700; color: var(--accent); text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 0.9rem; }
.kesimpulan-box p { font-size: 0.87rem; color: var(--text-muted); line-height: 1.85; margin-bottom: 0.6rem; }
.sign-off { font-family: var(--font-display); font-size: 0.9rem; color: var(--accent); font-style: italic; margin-top: 1rem; display: block; }

/* HASHTAG */
.hashtag-block { margin-top: 2.5rem; padding-top: 1.5rem; border-top: 1px solid var(--border); display: flex; flex-wrap: wrap; gap: 8px; }
.hashtag { background: var(--surface); border: 1px solid var(--border); color: var(--text-muted); font-family: var(--font-mono); font-size: 0.68rem; padding: 4px 12px; border-radius: 20px; }

/* CTA */
.cta-block { margin-top: 2rem; background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 1.4rem; text-align: center; }
.cta-block p { font-size: 0.85rem !important; opacity: 0.6 !important; margin-bottom: 1rem !important; }
.cta-links { display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; }
.cta-btn { display: inline-flex; align-items: center; gap: 6px; background: rgba(200,151,42,0.1); border: 1px solid rgba(200,151,42,0.3); color: var(--gold); text-decoration: none; padding: 0.6rem 1.2rem; border-radius: 8px; font-size: 0.75rem; font-weight: 600; }

/* POST NAV */
.post-nav { display: flex; gap: 12px; padding: 20px 24px; border-top: 1px solid var(--border); flex-wrap: wrap; }
.post-nav a { font-family: var(--font-mono); font-size: 0.72rem; color: var(--text-muted); text-decoration: none; background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 8px 14px; transition: all 0.2s; }
.post-nav a:hover { border-color: var(--accent); color: var(--accent); }

/* FOOTER */
footer { padding: 24px; text-align: center; font-family: var(--font-mono); font-size: 0.65rem; color: var(--text-muted); border-top: 1px solid var(--border); }
.updated-tag { display: inline-block; background: var(--surface2); border: 1px solid var(--border); border-radius: 4px; padding: 2px 8px; font-size: 0.6rem; color: var(--accent); margin-left: 6px; }
.social-links { display: flex; gap: 16px; justify-content: center; margin-top: 10px; flex-wrap: wrap; }
.social-links a { font-family: var(--font-mono); font-size: 0.65rem; color: var(--text-muted); text-decoration: none; display: inline-flex; align-items: center; gap: 5px; }
.social-links a:hover { color: var(--accent); }
```

---

## KOMPONEN OPSIONAL (define kalau dipakai)

| Komponen | Class | Warna aksen |
|---|---|---|
| Spek box | `.spek-box` + `.spek-box-label` + `.spek-item` + `.spek-icon` | hijau |
| Terminal/kode | `.terminal-box` → `.terminal-header` + `.terminal-body` | github dark |
| Info box | `.info-box` + `.info-box-label` | accent/gold |
| Warning box | `.warning-box` + `.warning-label` | merah |
| Quote box | `.quote-box` → `.quote-text` + `.quote-source` | sesuai tema |
| Compare grid | `.compare-grid` → `.compare-card` | merah/hijau |
| SOP card | `.sop-card` + `.sop-card-label` + `.sop-card-title` | gold |
| Foto block | `<div class="foto-block"><img ...><div class="foto-caption" style="..."></div>` | — |
| Custom widget | Bebas — define sendiri sesuai tema blog | sesuai tema |

Terminal body colors: `.cmd` biru · `.out` abu · `.ok` hijau · `.warn` kuning · `.err` merah · `.highlight` gold

**Catatan foto-block:** `foto-caption` pakai inline style, bukan class terpisah:
```html
<div class="foto-block">
  <img src="../images/nama-foto.webp" alt="..." style="width:100%;border-radius:10px;display:block;">
  <div class="foto-caption" style="font-family:var(--font-mono);font-size:0.65rem;color:var(--text-muted);text-align:center;margin-top:0.6rem;letter-spacing:0.5px;">Caption di sini</div>
</div>
```

---

## HERO — OPSI FOTO vs EMOJI

**Opsi A — Hero dengan foto Om Opan (seperti blog-panas-jakarta):**
```html
<div class="hero">
  <div class="hero-bg-pattern"></div>
  <img src="../images/opan_XXX.webp" alt="Om Opan" class="hero-photo">
  <div class="hero-emoji-bg">[EMOJI]</div>
  <div class="hero-overlay">...</div>
</div>
```

CSS tambahan untuk hero-photo:
```css
.hero-photo {
  position: absolute; top: 0; right: 0;
  width: 55%; height: 100%;
  object-fit: cover; object-position: center top;
  mask-image: linear-gradient(to left, rgba(0,0,0,0.7) 0%, transparent 100%);
  -webkit-mask-image: linear-gradient(to left, rgba(0,0,0,0.7) 0%, transparent 100%);
  pointer-events: none;
}
```

**Opsi B — Hero emoji only (tanpa foto):**
```html
<div class="hero">
  <div class="hero-bg-pattern"></div>
  <div class="hero-emoji-bg">[EMOJI]</div>
  <div class="hero-overlay">...</div>
</div>
```

---

## EKSPRESI OM OPAN

10 foto tersedia di `images/ekspresi/` — semua format **`.webp`** (bukan .jpg).

```html
<!-- EKSPRESI: [NAMA] — inline style background/border sesuai mood -->
<div class="ekspresi-card [modifier]" style="background:rgba(X,X,X,0.05);border:1px solid rgba(X,X,X,0.2);">
  <img src="../images/ekspresi/ekspresi_NAMA.webp" alt="Om Opan NAMA">
  <p>"Caption di sini..."</p>
</div>
```

Kombinasi modifier + warna:

| Mood | Class modifier | Background rgba | Border rgba |
|---|---|---|---|
| Senang/cool/netral | *(tidak perlu)* | `rgba(200,151,42,0.05)` | `rgba(200,151,42,0.15)` |
| Semangat/berhasil | `.semangat` | `rgba(76,175,125,0.05)` | `rgba(76,175,125,0.2)` |
| Marah/frustrasi | `.marah` | `rgba(224,90,90,0.05)` | `rgba(224,90,90,0.2)` |
| Kagum/bingung/terkejut | `.biru` | `rgba(91,141,238,0.05)` | `rgba(91,141,238,0.2)` |

Nama file: `ekspresi_senang` · `ekspresi_tertawa` · `ekspresi_cool` · `ekspresi_kagum` · `ekspresi_marah` · `ekspresi_sedih` · `ekspresi_terkejut` · `ekspresi_bingung` · `ekspresi_lelah` · `ekspresi_semangat`

**Aturan:** maks 5 ekspresi per blog · jangan duplikat nama file dalam satu blog · jangan dua ekspresi berturut-turut tanpa teks di antaranya.

---

## TAG-PILL WARNA LENGKAP

```html
<span class="tag-pill">gold — default</span>
<span class="tag-pill green">hijau</span>
<span class="tag-pill blue">biru</span>
<span class="tag-pill red">merah</span>
<span class="tag-pill orange">oranye</span>
```

---

## FOOTER & POST-NAV HTML

```html
<div class="post-nav">
  <a href="https://opanowski.github.io/opanowski/blog/index.html">← Log Harian</a>
  <a href="[url-blog-sebelumnya]">← [Judul Blog Sebelumnya]</a>
  <a href="https://opanowski.github.io/opanowski/">🏠 Portal Utama</a>
</div>

<footer>
  Bunker Opanowski — [Tagline Blog Ini]
  <span class="updated-tag"><span class="live-dot"></span>[Bulan Tahun]</span>
  <div class="social-links">
    <a href="https://www.facebook.com/profile.php?id=61560342106832" target="_blank" rel="noopener">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg> Facebook
    </a>
    <a href="https://www.instagram.com/opanowski/" target="_blank" rel="noopener">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="0.5" fill="currentColor"/></svg> Instagram
    </a>
    <a href="https://www.youtube.com/channel/UCgsJ-a0Cg20xdsn-e_42-yQ" target="_blank" rel="noopener">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.95-1.96C18.88 4 12 4 12 4s-6.88 0-8.59.46A2.78 2.78 0 0 0 1.46 6.42 29 29 0 0 0 1 12a29 29 0 0 0 .46 5.58 2.78 2.78 0 0 0 1.95 1.95C5.12 20 12 20 12 20s6.88 0 8.59-.47a2.78 2.78 0 0 0 1.95-1.95A29 29 0 0 0 23 12a29 29 0 0 0-.46-5.58z"/><polygon points="9.75 15.02 15.5 12 9.75 8.98 9.75 15.02"/></svg> YouTube
    </a>
  </div>
</footer>
```

---

## KOMENTAR & DONATE

```html
<!-- KOMENTAR -->
<div style="max-width:720px;margin:0 auto;padding:0 1.5rem 3rem">
  <div style="border-top:1px solid #2e3248;padding-top:2rem;margin-top:1rem">
    <div style="font-family:'Space Mono',monospace;font-size:0.62rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#C8972A;margin-bottom:1.2rem">💬 Komentar</div>
    <script src="https://utteranc.es/client.js" repo="opanowski/opanowski" issue-term="pathname" theme="github-dark" crossorigin="anonymous" async></script>
  </div>
</div>
<script src="/opanowski/donate-widget.js"></script>
```

---

## ATURAN GAYA BAHASA

- Sapaan: **gw/bray**, santai, jujur, kadang humor
- Sign-off wajib: `"Tetap autodidak, tetap berkah! 🏴"`
- Heading h2 selalu punya `<em>` untuk bagian italic
- Bold penting pakai `<strong style="color:var(--cream)">`

---

## CUSTOM WIDGET PER TEMA

Setiap blog boleh punya komponen visual unik yang tema-spesifik (misal: thermometer widget di blog panas Jakarta, progress bar di blog coding, harvest counter di blog kebun). Define sendiri di `<style>` blog yang bersangkutan. Ini bukan bug atau inkonsistensi — ini fitur yang bikin tiap blog terasa hidup.

---

## CHECKLIST SEBELUM PUSH

- [ ] `:root` variables + `--red` + `--orange` + `--font-display` + `--font-mono` sudah di-define di `<style>`
- [ ] `<link rel="icon">` emoji sesuai tema sudah ada
- [ ] Google Fonts `<link>` sudah ada di `<head>`
- [ ] `og:url` sudah benar (pakai slug yang tepat)
- [ ] Ekspresi pakai `.webp` (bukan `.jpg`)
- [ ] Ekspresi tidak duplikat nama file
- [ ] `.ekspresi-card` CSS class sudah di-define (bukan pure inline)
- [ ] `post-nav`, `footer`, `.updated-tag`, `.social-links` sudah di-define di `<style>`
- [ ] `post-nav` prev/next sudah benar
- [ ] `latest-posts.js` diupdate (entry baru di posisi 1, hapus entry ke-4)
- [ ] `blog/index.html` log-card baru + counter +1
- [ ] Foto di-`git add` terpisah kalau ada

---

*Bunker Opanowski — TEMPLATE-BLOG.md v1.1 | Villa Ciracas, Juni 2026*
*Direvisi berdasarkan audit blog-panas-jakarta.html — 10 gap diperbaiki*
