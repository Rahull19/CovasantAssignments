import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os
os.makedirs("downloads", exist_ok=True)
async def download_page(session, url):
    try:
        async with session.get(url, timeout=10) as response:
            content = await response.read()
            filename = urlparse(url).path.replace('/', '_') or 'index.html'
            filepath = os.path.join("downloads", filename)
            with open(filepath, 'wb') as f:
                f.write(content)
            print(f"Downloaded: {url}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

async def get_links(session, base_url):
    try:
        async with session.get(base_url, timeout=10) as response:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            links = []
            for a in soup.find_all('a', href=True):
                full_url = urljoin(base_url, a['href'])
                if full_url.startswith("http"):
                    links.append(full_url)
            return links
    except Exception as e:
        print(f"Failed to parse links from {base_url}: {e}")
        return []
async def main(base_url):
    async with aiohttp.ClientSession() as session:
        print(f"Fetching and parsing main page: {base_url}")
        links = await get_links(session, base_url)
        print(f"Found {len(links)} links")

        tasks = [download_page(session, url) for url in links]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    test_url = "https://books.toscrape.com/"
    asyncio.run(main(test_url))
