import httpx
from bs4 import BeautifulSoup
import asyncio

BASE_URL = "https://bstu.uz"

headers = {
    "User-Agent": "Mozilla/5.0"
}


async def fetch_page(client, url):
    response = await client.get(url)
    return response.text


def parse_html(html, url):
    soup = BeautifulSoup(html, "html.parser")

    # POSITION
    position_tag = soup.find("h3", class_="widget-head")
    position = position_tag.text.strip() if position_tag else None

    # IMAGE
    img_tag = soup.select_one(".my-details img")
    image = img_tag["src"] if img_tag else None

    # NAME
    name_tag = soup.find("h4", class_="my-name")
    name = name_tag.text.strip() if name_tag else None

    # INFO
    info_list = soup.select("ul.list li")

    reception = None
    phone = None
    email = None

    for item in info_list:
        text = item.text.lower()

        if "qabul" in text:
            reception = item.text.strip()
        elif "telefon" in text:
            phone = item.text.strip()
        elif "email" in text:
            email = item.text.strip()

    # BIO
    bio_tag = soup.find("div", class_="panel")
    bio = bio_tag.text.strip() if bio_tag else None

    return {
        "name": name,
        "position": position,
        "image": image,
        "reception": reception,
        "phone": phone,
        "email": email,
        "bio": bio,
        "url": url
    }

async def get_all_management_async():
    urls = [
        "https://bstu.uz/rahbariyat/rektor",
        "https://bstu.uz/rahbariyat/o-quv-ishlari-bo-yicha-birinchi-prorektor",
        "http://bstu.uz/rahbariyat/yoshlar-bilan-ishlash-bo-yicha-prorektor",
        "https://bstu.uz/rahbariyat/ilmiy-ishlar-va-innovatsiyalar-bo-yicha-prorektor",
        "https://bstu.uz/rahbariyat/moliya-va-iqtisod-ishlari-bo-yicha-prorektor",
    ]

    async with httpx.AsyncClient(headers=headers, timeout=20) as client:
        tasks = [fetch_page(client, url) for url in urls]
        pages = await asyncio.gather(*tasks)

    results = []

    for html, url in zip(pages, urls):
        try:
            data = parse_html(html, url)
            results.append(data)
        except Exception as e:
            print("Parse error:", url, e)

    return results