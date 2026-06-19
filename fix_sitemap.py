#!/usr/bin/env python3
"""
fix_sitemap.py — Bunker Opanowski
Nambahin blog post yang ada di folder blog/ tapi belum terdaftar di sitemap.json.
Jalanin dari ~/Desktop/opanowski/:
    python3 fix_sitemap.py
"""

import json
from pathlib import Path

SITEMAP_FILE = Path("sitemap.json")
BLOG_DIR = Path("blog")

def main():
    if not SITEMAP_FILE.exists():
        print("❌ sitemap.json gak ketemu. Jalanin script ini dari ~/Desktop/opanowski/")
        return

    sitemap = json.loads(SITEMAP_FILE.read_text(encoding="utf-8"))
    listed = set(p.split("/")[-1] for p in sitemap.get("blog", []))

    actual_files = sorted(
        f.name for f in BLOG_DIR.glob("*.html") if f.name != "index.html"
    )

    missing = [f for f in actual_files if f not in listed]

    if not missing:
        print("✅ sitemap.json udah lengkap, gak ada yang ketinggalan.")
        return

    print(f"📋 Ketemu {len(missing)} blog post yang belum terdaftar:")
    for m in missing:
        print(f"   - {m}")
        sitemap["blog"].append(f"blog/{m}")

    sitemap["blog"] = sorted(set(sitemap["blog"]))

    SITEMAP_FILE.write_text(
        json.dumps(sitemap, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"\n✅ sitemap.json updated! Total blog post sekarang: {len(sitemap['blog'])}")
    print("➡️  Lanjut jalanin: python3 update_knowledge.py")

if __name__ == "__main__":
    main()
