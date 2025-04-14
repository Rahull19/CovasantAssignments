import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor
import os

def download_url(url):
    try:
        response = requests.get(url, timeout=10)
        filename = urlparse(url).path.replace('/', '_') or 'index.html'
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {url}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

def get_all_links(base_url):
    try:
        response = requests.get(base_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = []
        for a_tag in soup.find_all('a', href=True):
            full_url = urljoin(base_url, a_tag['href'])
            if full_url.startswith("http"):
                links.append(full_url)
        return links
    except Exception as e:
        print(f"Failed to parse links from {base_url}: {e}")
        return []

def download_all_links_from_page(base_url):
    print(f"Parsing and downloading links from: {base_url}")
    links = get_all_links(base_url)
    print(f"Found {len(links)} links.")

    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_url, links)

if __name__ == "__main__":
    base_url = "https://books.toscrape.com/" 
    download_all_links_from_page(base_url)
