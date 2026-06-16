#!/usr/bin/env python3
"""
inject_jsonld.py — Bunker Opanowski
Inject JSON-LD BlogPosting schema ke semua file HTML blog post.
Jalankan dari: ~/Desktop/opanowski/
"""

import os
import re
import json

BLOG_DIR = os.path.expanduser("~/Desktop/opanowski/blog")
BASE_URL = "https://opanowski.github.io/opanowski/blog"
AUTHOR_NAME = "Opanowski"
AUTHOR_URL = "https://opanowski.github.io/opanowski/"
PUBLISHER_NAME = "Bunker Opanowski"
PUBLISHER_LOGO = "https://opanowski.github.io/opanowski/assets/logo.png"

# ── Data post: href → (datePublished ISO, title) ─────────────────────────────
# Tanggal diambil dari blog/index.html, dikonversi ke ISO 8601
BULAN = {
    "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
    "Mei": "05", "Jun": "06", "Jul": "07", "Agu": "08",
    "Sep": "09", "Okt": "10", "Nov": "11", "Des": "12"
}

def parse_date(raw):
    """Konversi 'Rabu, 11 Jun 2026' atau '11 Jun 2026' ke '2026-06-11'"""
    raw = raw.strip()
    # Buang nama hari jika ada
    if "," in raw:
        raw = raw.split(",", 1)[1].strip()
    # Buang "Jum'at" style
    raw = re.sub(r"^[A-Za-z']+,?\s*", "", raw).strip()
    parts = raw.split()
    if len(parts) == 3:
        day, mon, year = parts
        mon_num = BULAN.get(mon, "01")
        return f"{year}-{mon_num}-{int(day):02d}T00:00:00+07:00"
    elif len(parts) == 2:
        # e.g. "Mei 2026" — pakai tanggal 01
        mon, year = parts
        mon_num = BULAN.get(mon, "01")
        return f"{year}-{mon_num}-01T00:00:00+07:00"
    return "2026-05-01"

# Map: filename → {date_iso, title}
POST_DATA = {
    "blog-panas-jakarta.html":              {"date": parse_date("11 Jun 2026"),   "title": "Ngoding Rasa Sauna: Jakarta 35° dan Semangat yang Gak Kendor"},
    "blog-anggur-bali-veraison.html":       {"date": parse_date("3 Jun 2026"),    "title": "Anggur Bali Masuk Fase Veraison — Deg-degan Nunggu yang Siap"},
    "blog-tanya-om-opan.html":              {"date": parse_date("29 Mei 2026"),   "title": "Dari Nol Sampai \"Tanya Om Opan\" Bisa Ngobrol Sendiri"},
    "blog-labu-botol.html":                 {"date": parse_date("26 Mei 2026"),   "title": "Labu Botol: Eksperimen Buah Kampung di Lahan 150m²"},
    "blog-senam-otak-setengah-abad.html":   {"date": parse_date("25 Mei 2026"),   "title": "Senam Otak Usia Setengah Abad: Dari Ciracas Tembus Kutub Utara!"},
    "blog-swasembada-kreatif-otodidak.html":{"date": parse_date("26 Mei 2026"),   "title": "Esensi Swasembada Kreatif: Menikmati Proses Otodidak Tanpa Harus Terbawa Arus"},
    "blog-siasat-urban-farming.html":       {"date": parse_date("23 Mei 2026"),   "title": "Siasat Urban Farming ala Bunker Opanowski: Angkat Konblok, Bio-Canopy Pare Liar"},
    "blog-pengangguran-super-sibuk.html":   {"date": parse_date("21 Mei 2026"),   "title": "Pengangguran tapi Super Sibuk: Mengubah MacBook Jadul Jadi Mesin Kreatif Organik"},
    "blog-pare-hutan-manis-biji-merah.html":{"date": parse_date("17 Mei 2026"),   "title": "Pare Hutan: Buah Paling Menipu, Pahit di Luar Manis di Dalam"},
    "blog-tebu-hitam-tabulampot.html":      {"date": parse_date("19 Mei 2026"),   "title": "Tebu Hitam Manis Tabulampot: Bukti Lahan Sempit Bukan Halangan"},
    "blog-konversi-m4a-mp3.html":           {"date": parse_date("18 Mei 2026"),   "title": "Konversi M4A ke MP3 di Mac — Gratis, Cepat, Tanpa Drama"},
    "blog-website-ai-3hari.html":           {"date": parse_date("17 Mei 2026"),   "title": "Website Pribadi Ala Opanowski — 3 Hari, 3 AI, Tanpa Coding"},
    "blog-lalat-hijau-kedondong-mini.html": {"date": parse_date("17 Mei 2026"),   "title": "Lalat Hijau Itu Lagi Ngurusin Bunga Gue — dan Gue Hampir Ngusirnya"},
    "blog-panen-telur-batang-pisang.html":  {"date": parse_date("3 Mei 2026"),    "title": "4 Bulan Mandiri Telur & Zero Waste Batang Pisang — Villa Ciracas"},
    "blog-latte-tts-ffmpeg.html":           {"date": parse_date("13 Mei 2026"),   "title": "Digitalisasi Si Latte: Produksi Video Otomatis dengan Python & FFmpeg"},
    "blog-eznet-10mbps-bunker-opanowski.html":{"date": parse_date("13 Mei 2026"), "title": "Filosofi 10Mbps: Alur Kerja Efisien Bunker Opanowski"},
    "blog-mancing-bambu-apus.html":         {"date": parse_date("13 Mei 2026"),   "title": "Setoran Mujair Nila dari Bambu Apus"},
    "blog-anak-kelinci-jetpump.html":       {"date": parse_date("11 Mei 2026"),   "title": "Log Anabul: Tidur Nyenyak Level Dewa di Tengah Kebisingan!"},
    "blog-meta-ai-bunker-opanowski.html":   {"date": parse_date("10 Mei 2026"),   "title": "Ketika AI Meta Ngacak Bunker"},
    "blog-kenangan-bandung-nyokap-bayu.html":{"date": parse_date("10 Mei 2026"),  "title": "Jejak Memori di Bandung: Tentang Ramen, Nyokap, dan Kepergian sang Bontot"},
    "blog-tablet-mac-workflow.html":        {"date": parse_date("9 Mei 2026"),    "title": "Dua Device, Satu Bunker: Update Web dari Tablet Linux & Mac Jadul Bergantian"},
    "blog-log-009-mac-survival.html":       {"date": parse_date("9 Mei 2026"),    "title": "Mac Jadul Survival Kit: Setup Kerja di Bunker Opanowski"},
    "blog-log-008-vscode-workflow.html":    {"date": parse_date("8 Mei 2026"),    "title": "Upgrade Workflow: Dari Terminal Buta ke VSCode + Live Server"},
    "blog-digital-legacy-bayu.html":        {"date": parse_date("8 Mei 2026"),    "title": "Digital Legacy: Jurus Amankan Kenangan Si Bontot Biar Abadi di Dunia Maya"},
    "blog-log-006-analisis-dapur.html":     {"date": parse_date("7 Mei 2026"),    "title": "Analisis Dapur Bunker Opanowski — Dari Ciracas Menuju Global"},
    "blog-pasang-tombol-donasi.html":       {"date": parse_date("7 Mei 2026"),    "title": "Digital Swasembada: Traktir Kopi di Bunker Opanowski!"},
    "blog-coretax-registrasi-drama.html":   {"date": parse_date("5 Mei 2026"),    "title": "Drama Registrasi CoreTax: Ketika 'Valid' Menjadi 'Gagal'"},
    "blog-log086-pisang-telur.html":        {"date": parse_date("3 Mei 2026"),    "title": "Tebang Pisang, Mulsa Organik & Panen Telur — Distribusi ke Belasan Grup Urban Farming"},
    "blog-evolusi-digital-swasembada.html": {"date": parse_date("3 Mei 2026"),    "title": "Evolusi Digital & Swasembada: Dari Ciracas ke Lingkar Arktik"},
    "blog-evolusi-swasembada.html":         {"date": parse_date("3 Mei 2026"),    "title": "Evolusi Digital & Swasembada Ciracas"},
    "blog-brand-konsistensi.html":          {"date": parse_date("Mei 2026"),      "title": "Konsistensi Brand & Optimasi Kerja Digital"},
    "blog-seledri-organik.html":            {"date": parse_date("4 Mei 2026"),    "title": "Seledri di Pot, Healing di Pagi Hari"},
    "blog-log05-bye-kabel.html":            {"date": parse_date("2 Mei 2026"),    "title": "Bye-bye Kabel! Optimasi Transfer Data & Branding Baru"},
    "blog-evolusi-digital.html":            {"date": parse_date("Mei 2026"),      "title": "Evolusi Digital & Markas Global di GitHub"},
    "blog-log-001-peresmian-markas.html":   {"date": parse_date("1 Mei 2026"),    "title": "Peresmian Markas Digital"},
    "blog-pindah-gambar-ganti-warna.html":  {"date": parse_date("5 Mei 2026"),    "title": "2 Hari Berperang dengan Kode & Warna"},
}

# ── Ambil description dari meta tag ──────────────────────────────────────────
def get_meta_description(content):
    m = re.search(r'<meta\s+name="description"\s+content="([^"]+)"', content)
    if m:
        return m.group(1)
    m = re.search(r'<meta\s+content="([^"]+)"\s+name="description"', content)
    if m:
        return m.group(1)
    return ""

# ── Ambil OG image jika ada ───────────────────────────────────────────────────
def get_og_image(content):
    m = re.search(r'<meta\s+property="og:image"\s+content="([^"]+)"', content)
    if m:
        return m.group(1)
    return ""

# ── Build JSON-LD string ──────────────────────────────────────────────────────
def build_jsonld(filename, content):
    data = POST_DATA.get(filename, {})
    date_iso = data.get("date", "2026-05-01")
    title = data.get("title", "")
    description = get_meta_description(content)
    og_image = get_og_image(content)
    url = f"{BASE_URL}/{filename}"

    schema = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": title,
        "description": description,
        "url": url,
        "datePublished": date_iso,
        "dateModified": date_iso,
        "author": {
            "@type": "Person",
            "name": AUTHOR_NAME,
            "url": AUTHOR_URL
        },
        "publisher": {
            "@type": "Organization",
            "name": PUBLISHER_NAME,
            "url": AUTHOR_URL,
            "logo": {
                "@type": "ImageObject",
                "url": PUBLISHER_LOGO
            }
        },
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": url
        }
    }

    if og_image:
        schema["image"] = og_image

    json_str = json.dumps(schema, ensure_ascii=False, indent=2)
    return f'<script type="application/ld+json">\n{json_str}\n</script>'

# ── Inject ke file ────────────────────────────────────────────────────────────
def inject_file(filepath, filename):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip jika sudah ada JSON-LD
    if '"@type": "BlogPosting"' in content or '"BlogPosting"' in content:
        print(f"  [SKIP] sudah ada JSON-LD: {filename}")
        return False

    jsonld_block = build_jsonld(filename, content)

    # Inject sebelum </head>
    if "</head>" not in content:
        print(f"  [WARN] tidak ada </head>: {filename}")
        return False

    new_content = content.replace("</head>", f"{jsonld_block}\n</head>", 1)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    html_files = [f for f in os.listdir(BLOG_DIR)
                  if f.endswith(".html") and f != "index.html" and f.startswith("blog-")]
    html_files.sort()

    print(f"Ditemukan {len(html_files)} file blog post\n")

    injected = 0
    skipped = 0
    warned = 0

    for filename in html_files:
        filepath = os.path.join(BLOG_DIR, filename)
        if filename not in POST_DATA:
            print(f"  [WARN] tidak ada di POST_DATA: {filename}")
            warned += 1
            continue
        result = inject_file(filepath, filename)
        if result:
            print(f"  [OK]   {filename}")
            injected += 1
        else:
            skipped += 1

    print(f"\nSelesai: {injected} diinject, {skipped} di-skip, {warned} tidak dikenal")

if __name__ == "__main__":
    main()
