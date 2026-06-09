#!/usr/bin/env python3
"""
PageSpeed Audit - Bunker Opanowski
Jalanin: python3 pagespeed_audit.py
"""

import urllib.request
import urllib.parse
import json
import ssl
import certifi
import sys
from datetime import datetime

SSL_CTX = ssl.create_default_context(cafile=certifi.where())

# ── Config ─────────────────────────────────────────────────────────────────
URL = "https://opanowski.github.io/opanowski/"
API_KEY = ""  # Opsional - kosongkan dulu, cukup untuk basic audit
# Daftar gratis di https://developers.google.com/speed/docs/insights/v5/get-started
# kalau mau rate limit lebih longgar

# ── Fungsi ─────────────────────────────────────────────────────────────────
def fetch_psi(url, strategy, api_key=""):
    base = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
    params = f"?url={urllib.parse.quote(url)}&strategy={strategy}"
    if api_key:
        params += f"&key={api_key}"
    full_url = base + params

    try:
        with urllib.request.urlopen(full_url, context=SSL_CTX, timeout=30) as resp:
            return json.loads(resp.read())
    except Exception as e:
        print(f"  ⚠️  Gagal fetch {strategy}: {e}")
        return None

def get_score(data, category="performance"):
    try:
        return int(data["lighthouseResult"]["categories"][category]["score"] * 100)
    except:
        return None

def get_metric(data, metric_id):
    try:
        val = data["lighthouseResult"]["audits"][metric_id]["displayValue"]
        return val
    except:
        return "N/A"

def score_emoji(score):
    if score is None:
        return "❓"
    if score >= 90:
        return "🟢"
    if score >= 50:
        return "🟡"
    return "🔴"

def print_result(label, data):
    perf = get_score(data, "performance")
    seo  = get_score(data, "seo")
    acc  = get_score(data, "accessibility")
    bp   = get_score(data, "best-practices")

    lcp  = get_metric(data, "largest-contentful-paint")
    tbt  = get_metric(data, "total-blocking-time")
    cls  = get_metric(data, "cumulative-layout-shift")
    fcp  = get_metric(data, "first-contentful-paint")
    si   = get_metric(data, "speed-index")
    ttfb = get_metric(data, "server-response-time")

    print(f"\n  {'─'*40}")
    print(f"  📱 {label}")
    print(f"  {'─'*40}")
    print(f"  {score_emoji(perf)} Performance  : {perf}%")
    print(f"  {score_emoji(seo)}  SEO          : {seo}%")
    print(f"  {score_emoji(acc)}  Accessibility: {acc}%")
    print(f"  {score_emoji(bp)}  Best Practice: {bp}%")
    print(f"  {'─'*40}")
    print(f"  ⏱  LCP   : {lcp}")
    print(f"  ⏱  TBT   : {tbt}")
    print(f"  ⏱  CLS   : {cls}")
    print(f"  ⏱  FCP   : {fcp}")
    print(f"  ⏱  SI    : {si}")
    print(f"  ⏱  TTFB  : {ttfb}")

def print_opportunities(data, top_n=3):
    try:
        audits = data["lighthouseResult"]["audits"]
        opps = []
        for key, audit in audits.items():
            if audit.get("details", {}).get("type") == "opportunity":
                savings = audit.get("details", {}).get("overallSavingsMs", 0)
                if savings > 0:
                    opps.append((savings, audit.get("title", key)))
        opps.sort(reverse=True)
        if opps:
            print(f"\n  🔧 Top Issues:")
            for ms, title in opps[:top_n]:
                print(f"     • {title} (~{int(ms)}ms savings)")
    except:
        pass

# ── Main ───────────────────────────────────────────────────────────────────
def main():
    import urllib.parse

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\n{'═'*46}")
    print(f"  🚀 PageSpeed Audit — Bunker Opanowski")
    print(f"  🕐 {now}")
    print(f"  🌐 {URL}")
    print(f"{'═'*46}")

    strategies = [("MOBILE", "mobile"), ("DESKTOP", "desktop")]

    for label, strategy in strategies:
        print(f"\n  ⏳ Fetching {label}...")
        data = fetch_psi(URL, strategy, API_KEY)
        if data:
            print_result(label, data)
            print_opportunities(data)
        else:
            print(f"  ❌ Gagal fetch {label}")

    print(f"\n{'═'*46}\n")

if __name__ == "__main__":
    main()
