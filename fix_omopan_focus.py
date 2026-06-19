#!/usr/bin/env python3
"""
Fix cursor/focus bug widget chatbot "Om Opan".
Ganti: input.value="";input.blur();
Jadi : input.value="";if('ontouchstart' in window){input.blur();}else{input.focus();}

Exact string match (bukan regex looser) biar aman, gak salah replace bagian lain.
Scan folder: blog/, projects/, dan root (index.html, gudang.html, dll).
"""

import os
import glob

OLD = 'input.value="";input.blur();'
NEW = 'input.value="";if(\'ontouchstart\' in window){input.blur();}else{input.focus();}'

# Folder/file yang mau di-scan
SEARCH_GLOBS = [
    "blog/*.html",
    "projects/*.html",
    "index.html",
    "gudang.html",
]

def find_target_files():
    files = set()
    for pattern in SEARCH_GLOBS:
        for f in glob.glob(pattern):
            if os.path.isfile(f):
                files.add(f)
    return sorted(files)

def main():
    targets = find_target_files()
    if not targets:
        print("⚠️  Gak ada file HTML ketemu. Pastikan script ini dijalankan dari root repo ~/Desktop/opanowski/")
        return

    total_files_scanned = len(targets)
    total_fixed = 0
    fixed_files = []
    skipped_files = []

    for path in targets:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        count = content.count(OLD)

        if count == 0:
            skipped_files.append(path)
            continue

        new_content = content.replace(OLD, NEW)

        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)

        total_fixed += 1
        fixed_files.append((path, count))
        print(f"✅ FIXED  : {path}  ({count}x replaced)")

    print("\n" + "=" * 60)
    print(f"Total file di-scan   : {total_files_scanned}")
    print(f"Total file di-fix    : {total_fixed}")
    print(f"Total file di-skip   : {len(skipped_files)} (pattern gak ketemu / udah ke-fix sebelumnya)")
    print("=" * 60)

    if skipped_files:
        print("\nFile yang di-skip (pattern OLD gak ditemukan persis):")
        for f in skipped_files:
            print(f"  - {f}")

    if total_fixed == 0:
        print("\n⚠️  Gak ada satu file pun yang ke-fix. Cek lagi apakah pattern OLD masih sama persis dengan source code aslinya (mungkin udah pernah diedit manual).")
    else:
        print(f"\n🎉 Selesai. {total_fixed} file berhasil di-update.")
        print("Lanjut cek dengan: git diff")
        print("Lalu commit & push kalau hasilnya sudah sesuai.")

if __name__ == "__main__":
    main()
