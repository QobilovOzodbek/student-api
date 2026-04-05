import requests
from bs4 import BeautifulSoup

BASE_URL = "https://bstu.uz"

headers = {
    "User-Agent": "Mozilla/5.0"
}


def parse_management_page(url: str):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # POSITION (lavozim)
    position_tag = soup.find("h3", class_="widget-head")
    position = position_tag.text.strip() if position_tag else None

    # IMAGE
    img_tag = soup.find("img")
    image = img_tag["src"] if img_tag else None

    # NAME
    name_tag = soup.find("h4", class_="my-name")
    name = name_tag.text.strip() if name_tag else None

    # INFO (qabul vaqti, telefon, email)
    info_list = soup.select("ul.list li")

    reception = None
    phone = None
    email = None

    for item in info_list:
        text = item.text.strip().lower()

        if "qabul" in text:
            reception = item.text.strip()

        elif "telefon" in text:
            phone = item.text.strip()

        elif "email" in text:
            email = item.text.strip()

    # BIO / VAZIFALAR
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

def get_all_management():
    urls = [
        "https://bstu.uz/rahbariyat/rektor",
        "https://bstu.uz/rahbariyat/o-quv-ishlari-bo-yicha-birinchi-prorektor",
        "http://bstu.uz/rahbariyat/yoshlar-bilan-ishlash-bo-yicha-prorektor",
        "https://bstu.uz/rahbariyat/ilmiy-ishlar-va-innovatsiyalar-bo-yicha-prorektor",
        "https://bstu.uz/rahbariyat/moliya-va-iqtisod-ishlari-bo-yicha-prorektor",
    ]

    data = []

    for url in urls:
        try:
            person = parse_management_page(url)
            data.append(person)
        except Exception as e:
            print("Error:", url, e)

    return data