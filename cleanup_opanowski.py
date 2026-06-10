import os

BASE = os.path.expanduser("~/Desktop/opanowski")

files_to_delete = [
    # Script fix one-time yang udah selesai
    "fix3.py",
    "fix-donate.sh",
    "fix_accessibility.py",
    "fix_accessibility.py ",  # ada spasi di belakang nama (file corrupt)
    "fix_blog_images.py",
    "fix_defer_index.py",
    "fix_fonts_preconnect.py",
    "fix_lcp_hero.py",
    "fix_main_landmark.py",
    "inject-donate.sh",
    "inject-widget.sh",
    "remove-widget.py",
    "resize_images.py",
    "update_html_to_webp.py",
    "convert_to_webp.py",

    # Backup index numpuk
    "index.html.bak",
    "index_asli.html",
    "index_fix.html",
    "index-root.html",

    # Temp/junk
    ":tmp:fix_log001.py",
    "blog/placeholder.txt",
    "blog-index-snippet.txt",
    "SOP-hero-image-blog.txt",

    # Bak jadwal konten
    "jadwal-konten-bunker-opanowski.html.bak",
]

print("=" * 55)
print("CLEANUP REPO OPANOWSKI")
print("=" * 55)

deleted = []
not_found = []
errors = []

for f in files_to_delete:
    full_path = os.path.join(BASE, f)
    if os.path.exists(full_path):
        try:
            os.remove(full_path)
            deleted.append(f)
            print(f"  [HAPUS] {f}")
        except Exception as e:
            errors.append((f, str(e)))
            print(f"  [ERROR] {f} → {e}")
    else:
        not_found.append(f)
        print(f"  [SKIP]  {f} (tidak ditemukan)")

print()
print("=" * 55)
print(f"✅ Dihapus    : {len(deleted)} file")
print(f"⚠️  Tidak ada  : {len(not_found)} file")
print(f"❌ Error      : {len(errors)} file")
print("=" * 55)

if deleted:
    print("\nLangkah selanjutnya:")
    print("  cd ~/Desktop/opanowski")
    print("  git add -A")
    print('  git commit -m "chore: cleanup file sampah dan backup lama"')
    print("  git push origin main")
