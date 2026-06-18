#!/usr/bin/env python3
"""
fix_facebook_url.py — Bunker Opanowski
Ganti semua URL Facebook lama (profile.php?id=...) jadi URL profil aktif
(facebook.com/opanowski.ajjah) di semua file blog/*.html.

Jalanin dari folder ~/Desktop/opanowski/ :
    python3 fix_facebook_url.py

Aman dijalanin berkali-kali — kalau gak ada lagi URL lama, otomatis di-skip.
"""
import glob

OLD_URL = "https://www.facebook.com/profile.php?id=61560342106832"
NEW_URL = "https://www.facebook.com/opanowski.ajjah/"

files = sorted(glob.glob("blog/*.html"))

if not files:
    print("⚠️  Gak ketemu file blog/*.html — pastiin lo jalanin script ini dari folder ~/Desktop/opanowski/")
    raise SystemExit(1)

updated = []
skipped = []

for fp in files:
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()

    count = content.count(OLD_URL)
    if count == 0:
        skipped.append(fp)
        continue

    new_content = content.replace(OLD_URL, NEW_URL)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated.append((fp, count))

print(f"\n✅ DIUPDATE ({len(updated)} file):")
for fp, count in updated:
    print(f"  - {fp}  ({count}x diganti)")

print(f"\n⏭️  GAK ADA URL LAMA, DI-SKIP ({len(skipped)} file):")
for fp in skipped:
    print("  -", fp)

print(f"\nTotal file diproses: {len(files)}")
print(f"Total replacement: {sum(c for _, c in updated)}")
