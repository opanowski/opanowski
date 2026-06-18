#!/usr/bin/env python3
"""
update_knowledge.py — Bunker Opanowski
Auto-update KNOWLEDGE_BASE di worker.js dari semua blog & project HTML
Jalanin setelah git push blog baru:
  python3 update_knowledge.py

Requirements: pip3 install requests beautifulsoup4

PATCH NOTE: versi ini escape karakter backtick (`) dan ${...} di konten
yang di-scrape, biar gak ngerusak template literal JS di worker.js.
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

MONTH_MAP = {
    "januari": 1, "februari": 2, "maret": 3, "april": 4, "mei": 5, "juni": 6,
    "juli": 7, "agustus": 8, "september": 9, "oktober": 10, "november": 11, "desember": 12,
}

def parse_indo_date(text):
    """Parse tanggal Indonesia kayak '12 Juni 2026' atau 'Mei 2026' -> (year, month, day) buat sorting."""
    if not text:
        return (0, 0, 0)
    parts = text.strip().lower().split()
    day, month, year = 0, 0, 0
    for p in parts:
        if p.isdigit():
            if len(p) == 4:
                year = int(p)
            else:
                day = int(p)
        elif p in MONTH_MAP:
            month = MONTH_MAP[p]
    return (year, month, day)

def extract_content(url):
    """Extract judul + konten penting + tanggal publish dari satu halaman HTML."""
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

        # Ambil tanggal publish dari span.updated-tag SEBELUM elemen lain dibuang
        date_text = ""
        date_span = soup.find("span", class_="updated-tag")
        if date_span:
            date_text = date_span.get_text(strip=True)
        date_key = parse_indo_date(date_text)

        # Hapus elemen yang tidak relevan (termasuk script biar kode JS gak ketarik)
        for tag in soup(["script", "style", "nav", "footer", "header", "noscript"]):
            tag.decompose()

        # Ambil semua paragraf & heading artikel
        parts = []
        for tag in soup.find_all(["h2", "h3", "p", "li"]):
            text = tag.get_text(strip=True)
            if len(text) > 30:  # filter teks terlalu pendek
                parts.append(text)

        content = " | ".join(parts[:8])  # ambil 8 bagian pertama biar ringkas
        return title, content, date_key

    except Exception as e:
        return "", f"(gagal fetch: {e})", (0, 0, 0)

def sanitize_for_template_literal(text):
    """
    Escape karakter yang bisa merusak template literal JS (`...`):
    - backslash harus diescape dulu sebelum yang lain
    - backtick (`) -> \\`
    - ${ -> \\${  (biar gak ke-interpolasi sebagai JS expression)
    """
    text = text.replace("\\", "\\\\")
    text = text.replace("`", "\\`")
    text = text.replace("${", "\\${")
    return text

def build_knowledge_base(sitemap):
    """Build string knowledge base dari semua halaman."""
    print("🔍 Fetching semua halaman blog & project...")
    lines = []
    lines.append("=== KONTEN BLOG & PROJECT BUNKER OPANOWSKI ===")
    lines.append(f"Website: {BASE_URL}\n")

    # Blog posts — fetch semua dulu, urutkan TERBARU di paling atas
    print("📅 Sorting blog berdasarkan tanggal publish...")
    blog_entries = []
    for path in sitemap.get("blog", []):
        url = f"{BASE_URL}/{path}"
        slug = Path(path).stem
        title, content, date_key = extract_content(url)
        blog_entries.append((date_key, slug, title, content))
        print(f"  ✅ {slug} (tgl: {date_key})")

    blog_entries.sort(key=lambda e: e[0], reverse=True)

    lines.append("--- BLOG POSTS (diurutkan TERBARU di paling atas) ---")
    for i, (date_key, slug, title, content) in enumerate(blog_entries):
        tag = "[INI POST PALING BARU] " if i == 0 else ""
        entry = f"{tag}[{slug}] {title}: {content}"
        lines.append(entry)

    # Projects
    lines.append("\n--- PROJECTS ---")
    for path in sitemap.get("projects", []):
        url = f"{BASE_URL}/{path}"
        slug = Path(path).stem
        title, content, _ = extract_content(url)
        entry = f"[{slug}] {title}: {content}"
        lines.append(entry)
        print(f"  ✅ {slug}")

    raw_kb = "\n".join(lines)
    return sanitize_for_template_literal(raw_kb)

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

    # Pakai function replacement (bukan string) biar backslash di new_kb
    # gak ditafsirkan ulang sama mesin regex (\g<1> dkk).
    def _replace(m):
        return f"{m.group(1)}\n{new_kb}\n{m.group(3)}"

    new_content, count = re.subn(pattern, _replace, content, flags=re.DOTALL)

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

    # 2. Build knowledge base baru dari semua halaman (sudah disanitize)
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
