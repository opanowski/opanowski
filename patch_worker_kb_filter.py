#!/usr/bin/env python3
"""
patch_worker_kb_filter.py — Bunker Opanowski
FIX PERMANEN buat error 413 "Request too large" di Groq API.

Root cause: seluruh KNOWLEDGE_BASE (50+ post) didorong ke system prompt
di SETIAP chat request -> ~18.000 token, padahal limit Groq cuma
12.000 (llama-3.3-70b) / 6.000 (llama-3.1-8b) token per menit.

Fix: filter KNOWLEDGE_BASE jadi cuma entry yang relevan sama pertanyaan
user (keyword matching), bukan dorong semuanya tiap kali.

Jalanin:
  python3 patch_worker_kb_filter.py
"""

from pathlib import Path

WORKER_FILE = Path(__file__).parent / "worker.js"

# ── Patch 1: sisipin KB filtering function setelah KNOWLEDGE_BASE ──
OLD_1 = """`;

// ── SYSTEM PROMPT ────────────────────────────────────────────
function getSystemPrompt() {"""

NEW_1 = """`;

// ── KNOWLEDGE BASE FILTERING (biar gak overload token Groq) ────
function parseKnowledgeBase(raw) {
  return raw
    .split("\\n")
    .filter((l) => l.trim().startsWith("["))
    .map((line) => {
      const match = line.match(/^\\[([^\\]]+)\\]/);
      return { slug: match ? match[1] : "", text: line };
    });
}

const KB_ENTRIES = parseKnowledgeBase(KNOWLEDGE_BASE);

function getRelevantKnowledge(query) {
  const q = (query || "").toLowerCase();
  const words = q.split(/\\s+/).filter((w) => w.length > 2);

  if (words.length === 0) {
    return KB_ENTRIES.slice(0, 5).map((e) => e.text).join("\\n");
  }

  const scored = KB_ENTRIES.map((e) => {
    const lower = e.text.toLowerCase();
    const score = words.reduce((acc, w) => acc + (lower.includes(w) ? 1 : 0), 0);
    return { ...e, score };
  });

  const matched = scored
    .filter((e) => e.score > 0)
    .sort((a, b) => b.score - a.score)
    .slice(0, 5);

  if (matched.length === 0) {
    return "Daftar topik yang ada: " + KB_ENTRIES.map((e) => e.slug).join(", ");
  }

  return matched.map((e) => e.text).join("\\n");
}

// ── SYSTEM PROMPT ────────────────────────────────────────────
function getSystemPrompt(userQuery = "") {"""

# ── Patch 2: ganti dump KNOWLEDGE_BASE penuh -> hasil filter ──
OLD_2 = """KNOWLEDGE BASE (data pribadi Om Opan):
${KNOWLEDGE_BASE}"""

NEW_2 = """KNOWLEDGE BASE (data pribadi Om Opan, HANYA bagian relevan dgn pertanyaan user):
${getRelevantKnowledge(userQuery)}"""

# ── Patch 3: kirim pertanyaan user terakhir ke getSystemPrompt ──
OLD_3 = """      const messages = [
        { role: "system", content: getSystemPrompt() },"""

NEW_3 = """      const lastUserMsg = userMessages[userMessages.length - 1]?.content || "";
      const messages = [
        { role: "system", content: getSystemPrompt(lastUserMsg) },"""


def apply_patch(content, old, new, label):
    if new in content:
        print(f"✅ {label}: udah dipatch sebelumnya, skip.")
        return content
    if old not in content:
        print(f"❌ {label}: pattern lama nggak ketemu — kirim ulang worker.js terbaru ke gw.")
        return content
    print(f"✅ {label}: berhasil dipatch.")
    return content.replace(old, new, 1)


def main():
    if not WORKER_FILE.exists():
        print(f"❌ File tidak ditemukan: {WORKER_FILE}")
        return

    content = WORKER_FILE.read_text(encoding="utf-8")

    content = apply_patch(content, OLD_1, NEW_1, "Patch 1 (KB filtering function)")
    content = apply_patch(content, OLD_2, NEW_2, "Patch 2 (pakai hasil filter di prompt)")
    content = apply_patch(content, OLD_3, NEW_3, "Patch 3 (kirim query user ke filter)")

    WORKER_FILE.write_text(content, encoding="utf-8")

    print("\nLangkah selanjutnya:")
    print("  1. wrangler deploy worker.js --name bunker-omopan")
    print("  2. wrangler tail (di terminal lain)")
    print("  3. Test chat 'tebu gimana??' lagi di website")
    print("  4. Harusnya sekarang Ok, dan token request jauh lebih kecil")


if __name__ == "__main__":
    main()
