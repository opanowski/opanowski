#!/usr/bin/env python3
"""
fix_blog_images.py
Bunker Opanowski — Fix hero images + insert inline images

Cara pakai:
1. Taruh script ini di root folder opanowski (sejajar folder /blog dan /images)
2. Jalankan: python3 fix_blog_images.py
3. Script akan edit file HTML langsung (in-place)
4. Git commit + push seperti biasa
"""

import re
import os

# ============================================================
# KONFIGURASI: semua fix per file
# ============================================================
FIXES = [
    {
        "file": "blog/blog-tebu-hitam-tabulampot.html",
        "hero_img": "tebu_manis.jpg",
        # YT short embed — sisipkan setelah foto tebu di dalam artikel
        "yt_short": "https://youtube.com/shorts/_hw6wZ49UCQ",
        "yt_anchor": '<div style="background:var(--surface);padding:0.6rem 1rem;font-family:var(--font-mono);font-size:0.62rem;color:var(--text-muted);letter-spacing:0.5px;">📸 Tebu hitam tabulampot — Villa Ciracas, Mei 2026</div>',
    },
    {
        "file": "blog/blog-konversi-m4a-mp3.html",
        "hero_img": "opan_009.jpg",
    },
    {
        "file": "blog/blog-website-ai-3hari.html",
        "hero_img": "opan_006.jpg",
    },
    {
        "file": "blog/blog-lalat-hijau-kedondong-mini.html",
        "hero_img": "cover_lalat.jpg",
    },
    {
        "file": "blog/blog-latte-tts-ffmpeg.html",
        "hero_img": "latte.jpg",
    },
    {
        "file": "blog/blog-eznet-10mbps-bunker-opanowski.html",
        "hero_img": "bunker_opanowski_tablet_workflow2.jpg",
        # Insert gambar sebelum heading "Hierarki Infrastruktur"
        "insert_images": [
            {
                "img": "bunker_opanowski_tablet_workflow2.jpg",
                "caption": "📸 Bunker Opanowski — tablet workflow setup",
                "before_text": "Hierarki Infrastruktur",
            }
        ],
    },
    {
        "file": "blog/blog-mancing-bambu-apus.html",
        "hero_img": "opan_005.jpg",
    },
    {
        "file": "blog/blog-anak-kelinci-jetpump.html",
        "hero_img": "opan_012.jpg",
    },
    {
        "file": "blog/blog-meta-ai-bunker-opanowski.html",
        "hero_img": "opan_016.jpg",
    },
    {
        "file": "blog/blog-tablet-mac-workflow.html",
        "hero_img": "opan_017.jpg",
    },
    # No. 11 (blog-log-006-analisis-dapur.html) tidak ada info hero img — skip dulu
    {
        "file": "blog/blog-coretax-registrasi-drama.html",
        "hero_img": "opan_016.jpg",
    },
    {
        "file": "blog/blog-evolusi-swasembada.html",
        "hero_img": "opan_017.jpg",
        "insert_images": [
            {
                "img": "opan_013.jpg",
                "caption": "📸 Om Opan — Villa Ciracas",
                "before_text": None,  # insert di tengah artikel (setelah h2 pertama)
                "after_h2_index": 0,  # setelah h2 ke-1
            },
            {
                "img": "opan_005.jpg",
                "caption": "📸 Om Opan — Villa Ciracas",
                "before_text": None,
                "after_h2_index": 2,  # setelah h2 ke-3
            },
        ],
    },
    {
        "file": "blog/blog-brand-konsistensi.html",
        "hero_img": "bunker_opanowski_tablet_workflow2.jpg",
        "insert_images": [
            {
                "img": "opan_003.jpg",
                "caption": "📸 Om Opan — Bunker Opanowski",
                "after_h2_index": 0,
            },
            {
                "img": "opan_012.jpg",
                "caption": "📸 Om Opan — Villa Ciracas",
                "after_h2_index": 2,
            },
            {
                "img": "opan_005.jpg",
                "caption": "📸 Om Opan — Villa Ciracas",
                "after_h2_index": 4,
            },
        ],
    },
    {
        "file": "blog/blog-log05-bye-kabel.html",
        "hero_img": "opan_006.jpg",
        "insert_images": [
            {
                "img": "opan_008.jpg",
                "caption": "📸 Om Opan — Villa Ciracas",
                "after_h2_index": 0,
            },
            {
                "img": "opan_009.jpg",
                "caption": "📸 Om Opan — Villa Ciracas",
                "after_h2_index": 2,
            },
        ],
    },
    {
        "file": "blog/blog-evolusi-digital.html",
        "hero_img": "opan_007.jpg",
    },
    {
        "file": "blog/blog-log-001-peresmian-markas.html",
        "hero_img": "opan_013.jpg",
    },
    {
        "file": "blog/blog-pindah-gambar-ganti-warna.html",
        "hero_img": "opan_006.jpg",
        "insert_images": [
            {
                "img": "opan_005.jpg",
                "caption": "📸 Om Opan — Villa Ciracas",
                "after_h2_index": 0,
            },
            {
                "img": "opan_009.jpg",
                "caption": "📸 Om Opan — Villa Ciracas",
                "after_h2_index": 2,
            },
        ],
    },
]

# ============================================================
# TEMPLATE: hero background-image style (inject ke div.hero)
# ============================================================
def make_hero_bg_style(img_filename):
    """Return inline style string untuk background-image hero."""
    return (
        f'background-image: url(../images/{img_filename}); '
        'background-size: cover; background-position: center; background-repeat: no-repeat;'
    )


# ============================================================
# TEMPLATE: inline image block (sisip di dalam artikel)
# ============================================================
def make_inline_img_block(img_filename, caption):
    """Return HTML block gambar yang disisipkan di dalam artikel."""
    return f'''
  <!-- INSERTED IMAGE -->
  <div style="margin:1.75rem 0;border-radius:12px;overflow:hidden;border:1px solid var(--border);">
    <img src="../images/{img_filename}" alt="{caption}" style="width:100%;display:block;object-fit:cover;max-height:420px;">
    <div style="background:var(--surface);padding:0.6rem 1rem;font-family:var(--font-mono);font-size:0.62rem;color:var(--text-muted);letter-spacing:0.5px;">{caption}</div>
  </div>'''


# ============================================================
# TEMPLATE: YouTube Short embed block
# ============================================================
def make_yt_embed(yt_url):
    """Return HTML embed block untuk YouTube Short."""
    # Extract video ID dari URL
    vid_id = yt_url.rstrip('/').split('/')[-1].split('?')[0]
    return f'''
  <!-- YT SHORT EMBED -->
  <div style="margin:1.75rem 0;border-radius:12px;overflow:hidden;border:1px solid var(--border);aspect-ratio:9/16;max-width:320px;margin-left:auto;margin-right:auto;">
    <iframe
      src="https://www.youtube.com/embed/{vid_id}"
      title="YouTube Short"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen
      style="width:100%;height:100%;display:block;">
    </iframe>
  </div>'''


# ============================================================
# HELPER: fix hero background-image di div.hero
# ============================================================
def fix_hero_bg(content, img_filename):
    """
    Tambahkan background-image ke div class="hero".
    Kalau sudah ada background-image, replace.
    """
    style_str = make_hero_bg_style(img_filename)

    # Pattern: <div class="hero" ...> atau <div class="hero">
    # Bisa ada style inline existing atau tidak
    def replace_hero(m):
        tag = m.group(0)
        if 'style=' in tag:
            # sudah ada style — inject background-image ke dalamnya
            # kalau sudah ada background-image, replace nilainya
            if 'background-image' in tag:
                tag = re.sub(
                    r'background-image:[^;"]*(;|(?="))',
                    f'background-image: url(../images/{img_filename});',
                    tag
                )
            else:
                # tambahkan ke awal style yang ada
                tag = re.sub(
                    r'style="',
                    f'style="{style_str} ',
                    tag
                )
        else:
            # belum ada style — tambahkan
            tag = tag.replace(
                'class="hero"',
                f'class="hero" style="{style_str}"'
            )
        return tag

    new_content = re.sub(
        r'<div\s+class="hero"[^>]*>',
        replace_hero,
        content,
        count=1
    )
    return new_content


# ============================================================
# HELPER: sisipkan gambar setelah h2 ke-N (0-indexed)
# ============================================================
def insert_after_h2(content, h2_index, img_block):
    """Sisipkan img_block setelah closing tag h2 ke-h2_index."""
    # Cari semua h2 closing tags
    pattern = r'</h2>'
    matches = list(re.finditer(pattern, content))
    
    if h2_index >= len(matches):
        print(f"    ⚠️  h2 index {h2_index} tidak ditemukan (total h2: {len(matches)}), skip.")
        return content
    
    insert_pos = matches[h2_index].end()
    content = content[:insert_pos] + img_block + content[insert_pos:]
    return content


# ============================================================
# HELPER: sisipkan gambar sebelum teks tertentu
# ============================================================
def insert_before_text(content, search_text, img_block):
    """Sisipkan img_block sebelum kemunculan pertama search_text."""
    idx = content.find(search_text)
    if idx == -1:
        print(f"    ⚠️  Teks '{search_text}' tidak ditemukan, skip.")
        return content
    # Mundur ke awal tag <h2> atau <p> yang mengandung teks ini
    # Cari tag pembuka sebelum idx
    tag_start = content.rfind('<', 0, idx)
    content = content[:tag_start] + img_block + content[tag_start:]
    return content


# ============================================================
# MAIN PROCESSOR
# ============================================================
def process_file(fix):
    filepath = fix["file"]
    
    if not os.path.exists(filepath):
        print(f"  ❌ File tidak ditemukan: {filepath}")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changed = False

    # 1. Fix hero background image
    if "hero_img" in fix:
        content = fix_hero_bg(content, fix["hero_img"])
        if content != original:
            print(f"  ✅ Hero image set: {fix['hero_img']}")
            changed = True
        else:
            print(f"  ℹ️  Hero sudah OK atau pattern tidak cocok: {fix['hero_img']}")

    # 2. Insert inline images
    if "insert_images" in fix:
        for ins in fix["insert_images"]:
            img_block = make_inline_img_block(ins["img"], ins["caption"])
            before = content
            
            if ins.get("before_text"):
                content = insert_before_text(content, ins["before_text"], img_block)
            elif "after_h2_index" in ins:
                content = insert_after_h2(content, ins["after_h2_index"], img_block)
            
            if content != before:
                print(f"  ✅ Gambar disisipkan: {ins['img']}")
                changed = True
            else:
                print(f"  ℹ️  Gambar tidak disisipkan (anchor tidak ketemu): {ins['img']}")

    # 3. Insert YouTube Short embed
    if "yt_short" in fix and "yt_anchor" in fix:
        anchor = fix["yt_anchor"]
        if anchor in content and "youtube.com/embed" not in content:
            yt_block = make_yt_embed(fix["yt_short"])
            content = content.replace(anchor, anchor + yt_block)
            print(f"  ✅ YT Short embed disisipkan: {fix['yt_short']}")
            changed = True
        elif "youtube.com/embed" in content:
            print(f"  ℹ️  YT embed sudah ada.")
        else:
            print(f"  ⚠️  YT anchor tidak ketemu — skip embed.")

    # Save jika ada perubahan
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  💾 File disimpan: {filepath}")
    else:
        print(f"  — Tidak ada perubahan: {filepath}")


# ============================================================
# RUN
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Bunker Opanowski — Blog Image Fixer")
    print("=" * 60)
    
    for fix in FIXES:
        print(f"\n📄 {fix['file']}")
        process_file(fix)
    
    print("\n" + "=" * 60)
    print("✅ Selesai! Sekarang git add, commit, push.")
    print("   git add blog/")
    print("   git commit -m 'fix: hero images + inline images semua blog'")
    print("   git push")
    print("=" * 60)
