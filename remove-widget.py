import os
import re

SKIP_LIST = {
    "./coming-soon.html",
    "./gudang.html",
    "./index-root.html",
    "./jadwal-konten-bunker-opanowski.html",
}

def remove(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if "OMOPAN-CHAT-INJECTED" not in content:
        print(f"⏭  Skip (tidak ada widget): {filepath}")
        return "skip"

    # Hapus semua dari <!-- OMOPAN-CHAT-INJECTED --> sampai </script> penutup widget
    new_content = re.sub(
        r'<!-- OMOPAN-CHAT-INJECTED -->.*?</script>',
        '',
        content,
        flags=re.DOTALL
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"✅ Removed: {filepath}")
    return "done"

print("\n🧹 Remove Widget Tanya Om Opan (lama)")
print("======================================")

count = 0
skipped = 0

for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d != ".git"]
    for fname in sorted(files):
        if not fname.endswith(".html"):
            continue
        filepath = os.path.join(root, fname).replace("\\", "/")
        if not filepath.startswith("./"):
            filepath = "./" + filepath

        if filepath in SKIP_LIST:
            print(f"⏭  Skip (excluded): {filepath}")
            skipped += 1
            continue

        result = remove(filepath)
        if result == "done":
            count += 1
        else:
            skipped += 1

print()
print("======================================")
print(f"✅ Berhasil remove : {count} file")
print(f"⏭  Di-skip         : {skipped} file")
print("======================================")
print()
print("Lanjut inject versi baru:")
print("  python inject-widget.py")
