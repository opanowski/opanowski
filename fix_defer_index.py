#!/usr/bin/env python3
"""
fix_defer_index.py
Tambah attribute 'defer' ke script tags render-blocking di index.html
Bunker Opanowski — PageSpeed optimization
"""

import os

FILE = os.path.expanduser("~/Desktop/opanowski/index.html")

# Pasangan: string lama → string baru
REPLACEMENTS = [
    (
        '<script src="latest-posts.js"></script>',
        '<script src="latest-posts.js" defer></script>'
    ),
    (
        '<script src="donate-widget.js"></script>',
        '<script src="donate-widget.js" defer></script>'
    ),
]

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

changed = 0
for old, new in REPLACEMENTS:
    if old in content:
        content = content.replace(old, new)
        print(f"✅ Fixed: {old}")
        print(f"       → {new}")
        changed += 1
    else:
        print(f"⚠️  Tidak ditemukan (skip): {old}")

if changed > 0:
    with open(FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"\n✅ {changed} perubahan disimpan ke {FILE}")
else:
    print("\n⚠️  Tidak ada perubahan — cek manual index.html")
