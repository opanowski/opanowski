#!/usr/bin/env python3
"""
patch_worker_logging.py — Bunker Opanowski
Nambahin logging detail di worker.js, biar kelihatan ALASAN ASLI
kenapa fallback "Waduh, lagi error nih gw" muncul (429? context kepanjangan?
invalid key? exception apa?) — bisa diliat lewat `wrangler tail`.

Jalanin:
  python3 patch_worker_logging.py
"""

from pathlib import Path

WORKER_FILE = Path(__file__).parent / "worker.js"

OLD = """          if (groqRes.status === 429 || res?.error) continue;
          groqData = res;
          break;
        } catch (e) {
          continue;
        }"""

NEW = """          if (groqRes.status === 429 || res?.error) {
            console.error(`⚠️ Model ${model} gagal — status: ${groqRes.status}, error:`, JSON.stringify(res?.error || res));
            continue;
          }
          groqData = res;
          break;
        } catch (e) {
          console.error(`⚠️ Model ${model} exception:`, e.message || String(e));
          continue;
        }"""


def main():
    if not WORKER_FILE.exists():
        print(f"❌ File tidak ditemukan: {WORKER_FILE}")
        print("   Pastikan script ini ada di folder yang sama dengan worker.js")
        return

    content = WORKER_FILE.read_text(encoding="utf-8")

    if NEW in content:
        print("✅ worker.js udah dipatch sebelumnya, gak ada yang diubah.")
        return

    if OLD not in content:
        print("❌ Pattern lama nggak ketemu di worker.js — mungkin formatnya udah beda.")
        print("   Kirim ulang worker.js terbaru ya biar gw sesuaikan patch-nya.")
        return

    content = content.replace(OLD, NEW, 1)
    WORKER_FILE.write_text(content, encoding="utf-8")
    print("✅ worker.js berhasil dipatch dengan logging diagnostic!")
    print("\nLangkah selanjutnya:")
    print("  1. wrangler deploy worker.js --name bunker-omopan")
    print("  2. Buka terminal baru, jalanin: wrangler tail")
    print("  3. Test chat 'tebu gimana??' beberapa kali di website")
    print("  4. Lihat error detail yang muncul di tail, screenshot/copy ke gw")


if __name__ == "__main__":
    main()
