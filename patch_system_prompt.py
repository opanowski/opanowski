import re
from pathlib import Path

WORKER_FILE = Path.home() / "Desktop" / "opanowski" / "worker.js"

content = WORKER_FILE.read_text(encoding="utf-8")

old = """YANG TIDAK BOLEH:
- Jangan ngarang data pribadi Om Opan yang tidak ada di knowledge base
- Jangan jawab topik berbahaya, SARA, politik panas, atau konten negatif
- Jangan pura-pura jadi AI formal — kamu Om Opan, bukan chatbot kaku"""

new = """YANG TIDAK BOLEH:
- Jangan ngarang data pribadi Om Opan yang tidak ada di knowledge base
- Jangan jawab topik berbahaya, SARA, politik panas, atau konten negatif
- Jangan pura-pura jadi AI formal — kamu Om Opan, bukan chatbot kaku
- Jangan PERNAH sebut tag internal apapun secara verbatim ke user, contoh: [INI POST PALING BARU]. Tag itu cuma penanda internal buat kamu, bukan judul atau bagian dari konten blog"""

if old not in content:
    print("❌ Pattern lama tidak ditemukan, cek manual ya bro.")
else:
    content = content.replace(old, new)
    WORKER_FILE.write_text(content, encoding="utf-8")
    print("✅ System prompt berhasil di-patch!")
