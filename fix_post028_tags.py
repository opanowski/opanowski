#!/usr/bin/env python3
"""
fix_post028_tags.py
Perbaiki HTML card #028 (Anggur Bali Veraison) yang rusak di blog/index.html

Bug: baris section-pill ke-3 + closing tags (</div>, log-arrow, </div>)
ke-mangled jadi satu baris "Vi Vi Vi <span cladiv>" — kemungkinan multi-cursor
edit di VSCode yang ke-interrupt di tengah jalan.

Jalanin dari folder root repo (~/Desktop/opanowski/):
    python3 fix_post028_tags.py
"""

path = "blog/index.html"

with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

fixed_lines = []
found = False

for line in lines:
    if "cladiv" in line:
        found = True
        fixed_lines.append('        <span class="section-pill">Veraison</span>\n')
        fixed_lines.append('        <span class="section-pill">Anggur Bali</span>\n')
        fixed_lines.append('        <span class="section-pill">Villa Ciracas</span>\n')
        fixed_lines.append("      </div>\n")
        fixed_lines.append('      <span class="log-arrow">Baca \u2192</span>\n')
        fixed_lines.append("    </div>\n")
    else:
        fixed_lines.append(line)

if not found:
    print("\u26a0\ufe0f  Baris rusak ('cladiv') nggak ketemu di", path)
    print("   Mungkin udah kepatch duluan atau lokasinya beda — cek manual.")
else:
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(fixed_lines)
    print("\u2705 Card #028 berhasil diperbaiki di", path)
    print("   Tag ke-3 gw isi 'Villa Ciracas' (tebakan berdasarkan pola tags di latest-posts.js).")
    print("   Kalau aslinya beda, tinggal edit manual di section-pill ketiga.")
