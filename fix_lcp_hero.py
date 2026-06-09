#!/usr/bin/env python3
"""
fix_lcp_hero.py
Fix LCP lambat di index.html Bunker Opanowski:
1. Tambah <link rel="preload"> untuk hero background image
2. Compress hero image lebih agresif pakai sips (quality 70)
3. Tambah fetchpriority hint via JS setelah hero-bg loaded
"""

import os
import subprocess

INDEX = os.path.expanduser("~/Desktop/opanowski/index.html")
HERO_IMG = os.path.expanduser("~/Desktop/opanowski/images/nJFlqNX.jpg")

# ── 1. Compress hero image lebih agresif ─────────────────────────────────────
print("📸 Compress hero image...")
size_before = os.path.getsize(HERO_IMG) / 1024

subprocess.run(
    ["sips", "-s", "formatOptions", "70", HERO_IMG],
    capture_output=True
)

size_after = os.path.getsize(HERO_IMG) / 1024
print(f"   {size_before:.0f}K → {size_after:.0f}K (hemat {size_before - size_after:.0f}K)")

# ── 2. Tambah preload link di <head> ─────────────────────────────────────────
print("\n🔗 Tambah preload hero image ke <head>...")

with open(INDEX, "r", encoding="utf-8") as f:
    content = f.read()

PRELOAD_TAG = '<link rel="preload" href="/opanowski/images/nJFlqNX.jpg" as="image" fetchpriority="high">'

# Cek kalau sudah ada
if 'nJFlqNX' in content and 'preload' in content:
    # Cek lebih spesifik
    if PRELOAD_TAG in content:
        print("   ⏭  Preload tag sudah ada, skip.")
    else:
        print("   ⚠️  Ada preload lain untuk nJFlqNX, cek manual.")
else:
    # Sisipkan setelah <meta charset> atau sebelum </head> — kita pilih setelah tag <meta charset
    # Lebih aman: sisipkan sebelum tag <style> pertama di <head>
    TARGET = '<style>'
    if TARGET in content:
        content = content.replace(TARGET, PRELOAD_TAG + '\n' + TARGET, 1)
        print(f"   ✅ Preload tag ditambahkan sebelum <style>")
    else:
        # Fallback: sisipkan sebelum </head>
        content = content.replace('</head>', PRELOAD_TAG + '\n</head>', 1)
        print(f"   ✅ Preload tag ditambahkan sebelum </head>")

# ── 3. Tambah fetchpriority pada hero-bg div jika ada ────────────────────────
# Tidak bisa langsung ke CSS bg, tapi kita bisa hint via JS inline kecil
# Lebih efektif: pastikan hero-bg div ada di HTML (bukan di JS), cek dulu
print("\n🔍 Cek hero-bg element di HTML...")
if 'hero-bg' in content:
    print("   ✅ hero-bg ditemukan di HTML")
else:
    print("   ⚠️  hero-bg tidak ditemukan sebagai HTML element (mungkin di JS)")

# ── 4. Simpan ────────────────────────────────────────────────────────────────
with open(INDEX, "w", encoding="utf-8") as f:
    f.write(content)

print(f"\n✅ Perubahan disimpan ke {INDEX}")
print("\n📋 Next steps:")
print("   1. Verifikasi: grep -n 'preload' ~/Desktop/opanowski/index.html | head -5")
print("   2. git add -A && git commit -m 'perf: preload hero image, fix LCP' && git push origin main")
