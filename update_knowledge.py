#!/usr/bin/env python3
"""
update_knowledge.py — Bunker Opanowski
Auto-update KNOWLEDGE_BASE di worker.js dari semua blog & project HTML
Jalanin setelah git push blog baru:
  python3 update_knowledge.py

Requirements: pip3 install requests beautifulsoup4
"""

import json
import re
import sys
import subprocess
from pathlib import Path

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("📦 Install dependencies dulu...")
    subprocess.run([sys.executable, "-m", "pip", "install", "requests", "beautifulsoup4"], check=True)
    import requests
    from bs4 import BeautifulSoup

# ── CONFIG ───────────────────────────────────────────────────
SITEMAP_URL   = "https://opanowski.github.io/opanowski/sitemap.json"
WORKER_FILE   = Path(__file__).parent / "worker.js"   # sesuaikan path kalau perlu
WORKER_NAME   = "bunker-omopan"
BASE_URL      = "https://opanowski.github.io/opanowski"
# ─────────────────────────────────────────────────────────────

def fetch_sitemap():
    """Ambil sitemap.json dari GitHub Pages."""
    print("📋 Fetching sitemap.json...")
    try:
        res = requests.get(SITEMAP_URL, timeout=10)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        print(f"❌ Gagal fetch sitemap: {e}")
        sys.exit(1)

def extract_content(url):
    """Extract judul + konten penting dari satu halaman HTML."""
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")

        # Ambil judul
        title = ""
        if soup.find("h1"):
            title = soup.find("h1").get_text(strip=True)
        elif soup.find("title"):
            title = soup.find("title").get_text(strip=True)

        # Hapus elemen yang tidak relevan
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()

        # Ambil semua paragraf & heading artikel
        parts = []
        for tag in soup.find_all(["h2", "h3", "p", "li"]):
            text = tag.get_text(strip=True)
            if len(text) > 30:  # filter teks terlalu pendek
                parts.append(text)

        content = " | ".join(parts[:8])  # ambil 8 bagian pertama biar ringkas
        return title, content

    except Exception as e:
        return "", f"(gagal fetch: {e})"

def build_knowledge_base(sitemap):
    """Build string knowledge base dari semua halaman."""
    print("🔍 Fetching semua halaman blog & project...")
    lines = []
    lines.append("=== KONTEN BLOG & PROJECT BUNKER OPANOWSKI ===")
    lines.append(f"Website: {BASE_URL}\n")

    # Blog posts
    lines.append("--- BLOG POSTS ---")
    for path in sitemap.get("blog", []):
        url = f"{BASE_URL}/{path}"
        slug = Path(path).stem
        title, content = extract_content(url)
        entry = f"[{slug}] {title}: {content}"
        lines.append(entry)
        print(f"  ✅ {slug}")

    # Projects
    lines.append("\n--- PROJECTS ---")
    for path in sitemap.get("projects", []):
        url = f"{BASE_URL}/{path}"
        slug = Path(path).stem
        title, content = extract_content(url)
        entry = f"[{slug}] {title}: {content}"
        lines.append(entry)
        print(f"  ✅ {slug}")

    return "\n".join(lines)

def update_worker_js(new_kb):
    """Replace KNOWLEDGE_BASE di worker.js dengan konten baru."""
    print(f"\n📝 Update {WORKER_FILE}...")

    if not WORKER_FILE.exists():
        print(f"❌ File tidak ditemukan: {WORKER_FILE}")
        print("   Pastikan update_knowledge.py ada di folder yang sama dengan worker.js")
        sys.exit(1)

    content = WORKER_FILE.read_text(encoding="utf-8")

    # Cari dan replace bagian KNOWLEDGE_BASE (antara backtick pertama dan terakhir di const KNOWLEDGE_BASE)
    pattern = r'(const KNOWLEDGE_BASE = `)(.*?)(`\s*;)'
    replacement = rf'\g<1>\n{new_kb}\n\g<3>'

    new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)

    if count == 0:
        print("❌ Tidak bisa menemukan KNOWLEDGE_BASE di worker.js")
        print("   Pastikan formatnya: const KNOWLEDGE_BASE = `...`;")
        sys.exit(1)

    WORKER_FILE.write_text(new_content, encoding="utf-8")
    print("✅ worker.js berhasil diupdate!")

def deploy_worker():
    """Deploy worker ke Cloudflare via wrangler."""
    print(f"\n🚀 Deploy ke Cloudflare ({WORKER_NAME})...")
    try:
        result = subprocess.run(
            ["wrangler", "deploy", str(WORKER_FILE), "--name", WORKER_NAME],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            print("✅ Deploy berhasil!")
            print(result.stdout)
        else:
            print("❌ Deploy gagal:")
            print(result.stderr)
            sys.exit(1)
    except FileNotFoundError:
        print("❌ wrangler tidak ditemukan. Jalanin: npm install -g wrangler")
        sys.exit(1)

def main():
    print("=" * 50)
    print("🏚️  Bunker Opanowski — Auto Update Knowledge Base")
    print("=" * 50)

    # 1. Fetch sitemap
    sitemap = fetch_sitemap()
    total = len(sitemap.get("blog", [])) + len(sitemap.get("projects", []))
    print(f"   Ditemukan: {len(sitemap.get('blog', []))} blog + {len(sitemap.get('projects', []))} project ({total} halaman)\n")

    # 2. Build knowledge base baru dari semua halaman
    new_kb = build_knowledge_base(sitemap)

    # 3. Update worker.js
    update_worker_js(new_kb)

    # 4. Deploy ke Cloudflare
    deploy_worker()

    print("\n" + "=" * 50)
    print("🎉 Selesai! Om Opan chatbot sudah up-to-date.")
    print("=" * 50)

if __name__ == "__main__":
    main()
