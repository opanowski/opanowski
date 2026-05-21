# TEMPLATE-BLOG — Bunker Opanowski
Referensi template blog untuk Claude. Lampirkan file ini tiap mau buat blog baru — **gantikan kebutuhan lampir blog-tablet-mac-workflow.html**.

---

## IDENTITAS TEMPLATE

- **Nama:** Bunker Opanowski Dark Theme v1
- **Bahasa:** Indonesia, gaya santai (gw/bray), suara "Om Opan"
- **Base URL:** `https://opanowski.github.io/opanowski/`
- **Lokasi:** Villa Ciracas, Jakarta Timur

---

## FONT & WARNA

```css
/* Google Fonts — selalu load ketiganya */
Syne (400/600/800)          → body text utama
Playfair Display (400/700)  → judul, h2, quote
Space Mono (400/700)        → label, tag, meta, kode

/* CSS Variables */
--bg:         #0f1117   /* background utama */
--surface:    #1a1d27   /* kartu, box */
--surface2:   #22263a   /* badge, tag */
--accent:     #f5a623   /* orange — warna utama */
--gold:       #C8972A   /* gold — aksen sekunder */
--cream:      #F5F0E8   /* teks heading terang */
--text:       #e8eaf0   /* body text */
--text-muted: #8b8fa8   /* teks redup */
--green:      #4caf7d   /* hijau — sukses/farming */
--border:     #2e3248   /* garis border */
--blue:       #5b8dee   /* biru — tech/info */
```

---

## STRUKTUR FILE

```
blog/blog-[slug].html     ← file blog baru
shared.css                ← CSS global (jangan diubah)
images/[foto].jpg         ← foto konten (kalau ada)
images/ekspresi/          ← 10 foto ekspresi Om Opan
```

Path gambar dari dalam folder `blog/`:
- Foto konten: `../images/nama-foto.jpg`
- Ekspresi: `../images/ekspresi/ekspresi_nama.jpg`

---

## STRUKTUR HTML (urutan wajib)

```
1. <head>          — meta, og:tags, fonts, shared.css, <style>
2. <header>        — sticky, back link ke Log Harian
3. .hero           — hero-bg-pattern + hero-emoji-bg + hero-overlay
                     (hero-tags: tag-pill, hero-title dengan <em>, hero-meta + live-dot)
4. .container      — max-width 720px, padding 3rem 1.5rem 5rem
   └ .artikel-body — konten blog
5. .post-nav       — navigasi prev/next
6. <footer>        — live-dot + tanggal + social links
7. Utterances      — komentar (repo: opanowski/opanowski, theme: github-dark)
8. donate-widget   — /opanowski/donate-widget.js
```

---

## KOMPONEN YANG TERSEDIA

| Komponen | Class/Tag | Warna aksen |
|---|---|---|
| Box spesifikasi | `.spek-box` + `.spek-box-label` + `.spek-item` | hijau |
| Terminal/kode | `.terminal-box` → `.terminal-header` + `.terminal-body` | github dark |
| Info box | `.info-box` / `.info-box.green` / `.info-box.blue` | sesuai varian |
| Warning box | `.warning-box` + `.warning-label` | merah |
| Quote box | `.quote-box` → `.quote-text` + `.quote-source` | hijau |
| Compare grid | `.compare-grid` → `.compare-card` + `.compare-item` | merah/hijau |
| Foto block | `.foto-block` → `<img>` + `.foto-caption` | — |
| Kesimpulan | `.kesimpulan-box` + `.sign-off` | gold |
| Hashtag | `.hashtag-block` → `.hashtag` | — |
| CTA block | `.cta-block` → `.cta-links` → `.cta-btn` | gold |
| SOP card | `.sop-card` + `.sop-card-label` | gold |

Terminal body colors: `.cmd` biru · `.out` abu · `.ok` hijau · `.warn` kuning · `.err` merah · `.highlight` gold

---

## EKSPRESI OM OPAN

10 foto tersedia di `images/ekspresi/`. Template HTML:

```html
<!-- EKSPRESI: [NAMA] -->
<div style="display:flex;align-items:center;gap:1rem;margin:1.2rem 0;padding:0.9rem 1.2rem;background:rgba(200,151,42,0.05);border:1px solid rgba(200,151,42,0.15);border-radius:10px;">
  <img src="../images/ekspresi/ekspresi_NAMA.jpg" alt="Om Opan NAMA" style="width:72px;height:72px;object-fit:cover;border-radius:8px;flex-shrink:0;border:2px solid rgba(200,151,42,0.3);">
  <p style="margin:0;font-size:0.85rem;color:var(--text-muted);font-style:italic;line-height:1.7;">"Caption di sini..."</p>
</div>
```

Variasi warna border sesuai mood:
- **Gold** `rgba(200,151,42,...)` → senang, tertawa, cool, kagum (netral/positif)
- **Hijau** `rgba(76,175,125,...)` → semangat, berhasil
- **Merah** `rgba(224,90,90,...)` → marah, sedih
- **Biru** `rgba(91,141,238,...)` → kagum, terkejut, bingung

Nama file ekspresi: `ekspresi_senang` · `ekspresi_tertawa` · `ekspresi_cool` · `ekspresi_kagum` · `ekspresi_marah` · `ekspresi_sedih` · `ekspresi_terkejut` · `ekspresi_bingung` · `ekspresi_lelah` · `ekspresi_semangat`

Aturan: maks 5 ekspresi per blog, jangan duplikat nama file dalam satu blog, jangan dua ekspresi berturut-turut tanpa teks di antaranya.

---

## ATURAN GAYA BAHASA

- Sapaan: **gw/bray**, santai, jujur, kadang humor
- Sign-off wajib: `"Tetap autodidak, tetap berkah! 🏴"`
- Heading h2 selalu punya `<em>` untuk bagian italic berwarna accent
- Bold penting pakai `<strong style="color:var(--cream)">`

---

## HERO TAG-PILL WARNA

```html
<span class="tag-pill">gold — default</span>
<span class="tag-pill green">hijau</span>
<span class="tag-pill blue">biru</span>
```

---

## CHECKLIST SEBELUM PUSH

- [ ] `og:url` sudah benar (pakai slug yang tepat)
- [ ] Hero emoji & tag sesuai tema
- [ ] Ekspresi tidak duplikat nama file
- [ ] `post-nav` prev/next sudah benar
- [ ] `latest-posts.js` diupdate (entry baru di posisi 1, hapus entry ke-4)
- [ ] `blog/index.html` log-card baru + counter +1
- [ ] Foto di-`git add` terpisah kalau ada

---

*Bunker Opanowski — TEMPLATE-BLOG.md v1.0 | Villa Ciracas, Mei 2026*
