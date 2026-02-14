import asyncio
from recon import crawl
from risk import score_url
from audit import analyze_response
from db import save_scan, save_finding

target = input("Enter target URL: ")

print("Crawling...")
urls = asyncio.run(crawl(target))

for url in urls:
    risk = score_url(url)
    save_scan(url, risk)

    try:
        import requests
        html = requests.get(url, timeout=5).text
        findings = analyze_response(url, html)

        for f in findings:
            save_finding(url, f)

    except:
        pass

print("Scan completed")
print("URLs scanned:", len(urls))