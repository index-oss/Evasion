import aiohttp
import asyncio
from bs4 import BeautifulSoup
from utils import normalize_url, is_valid_url
from config import HEADERS, TIMEOUT, MAX_PAGES

async def fetch(session, url):
    try:
        async with session.get(url, timeout=TIMEOUT) as r:
            return await r.text()
    except:
        return ""

async def crawl(start_url):
    visited = set()
    to_visit = [start_url]

    async with aiohttp.ClientSession(headers=HEADERS) as session:
        while to_visit and len(visited) < MAX_PAGES:
            url = to_visit.pop(0)
            if url in visited:
                continue

            html = await fetch(session, url)
            visited.add(url)

            soup = BeautifulSoup(html, "html.parser")

            for tag in soup.find_all("a", href=True):
                link = normalize_url(url, tag["href"])
                if is_valid_url(link) and link not in visited:
                    to_visit.append(link)

    return list(visited)