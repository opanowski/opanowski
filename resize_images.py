#!/usr/bin/env python3
"""
resize_images.py
Resize + compress gambar Bunker Opanowski pakai sips (native macOS).
- Max width/height: 1200px
- JPEG quality: 82
- Skip folder backup_original/
- Skip gambar yang sudah kecil (< 200K dan dimensi sudah OK)
- Backup otomatis ke images/backup_original/ sebelum overwrite
"""

import os
import subprocess
import shutil

IMAGES_DIR = os.path.expanduser("~/Desktop/opanowski/images")
BACKUP_DIR = os.path.join(IMAGES_DIR, "backup_original")
MAX_DIM = 1200       # px — max width atau height
QUALITY = 82         # JPEG quality (0-100)
SKIP_UNDER_KB = 150  # Skip jika filesize sudah < 150KB (sudah OK)

EXTENSIONS = (".jpg", ".jpeg", ".png")

os.makedirs(BACKUP_DIR, exist_ok=True)

def get_dims(filepath):
    """Return (width, height) menggunakan sips."""
    result = subprocess.run(
        ["sips", "-g", "pixelWidth", "-g", "pixelHeight", filepath],
        capture_output=True, text=True
    )
    width = height = 0
    for line in result.stdout.splitlines():
        if "pixelWidth" in line:
            width = int(line.strip().split()[-1])
        elif "pixelHeight" in line:
            height = int(line.strip().split()[-1])
    return width, height

def human_size(path):
    size = os.path.getsize(path)
    return f"{size/1024:.0f}K"

files = [
    f for f in os.listdir(IMAGES_DIR)
    if f.lower().endswith(EXTENSIONS)
    and os.path.isfile(os.path.join(IMAGES_DIR, f))
]

print(f"🔍 Ditemukan {len(files)} gambar di {IMAGES_DIR}\n")
print(f"{'File':<45} {'Before':>8} {'Dims':>12}  {'Action'}")
print("-" * 85)

total_before = 0
total_after = 0
processed = 0

for fname in sorted(files):
    fpath = os.path.join(IMAGES_DIR, fname)
    backup_path = os.path.join(BACKUP_DIR, fname)
    size_kb = os.path.getsize(fpath) / 1024
    w, h = get_dims(fpath)

    total_before += size_kb

    # Skip jika sudah kecil dan dimensi sudah OK
    if size_kb < SKIP_UNDER_KB and w <= MAX_DIM and h <= MAX_DIM:
        print(f"{fname:<45} {human_size(fpath):>8} {w}x{h:>6}  ⏭  skip (sudah OK)")
        total_after += size_kb
        continue

    # Backup dulu kalau belum ada
    if not os.path.exists(backup_path):
        shutil.copy2(fpath, backup_path)

    # Hitung dimensi target
    if w >= h:
        # landscape
        new_w = min(w, MAX_DIM)
        new_h = int(h * new_w / w)
    else:
        # portrait
        new_h = min(h, MAX_DIM)
        new_w = int(w * new_h / h)

    # Resize pakai sips
    subprocess.run(
        ["sips", "-z", str(new_h), str(new_w), fpath],
        capture_output=True
    )

    # Set quality (JPEG)
    if fname.lower().endswith((".jpg", ".jpeg")):
        subprocess.run(
            ["sips", "-s", "formatOptions", str(QUALITY), fpath],
            capture_output=True
        )

    size_after_kb = os.path.getsize(fpath) / 1024
    total_after += size_after_kb
    saved = size_kb - size_after_kb
    processed += 1

    print(f"{fname:<45} {human_size(fpath):>8} {new_w}x{new_h}  ✅ {size_kb:.0f}K → {size_after_kb:.0f}K (hemat {saved:.0f}K)")

print("-" * 85)
print(f"\n✅ {processed} gambar diproses")
print(f"📦 Total sebelum : {total_before/1024:.1f} MB")
print(f"📦 Total sesudah : {total_after/1024:.1f} MB")
print(f"💾 Total hemat   : {(total_before - total_after)/1024:.1f} MB")
print(f"\nBackup tersimpan di: {BACKUP_DIR}")
