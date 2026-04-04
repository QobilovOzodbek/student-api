import requests
from bs4 import BeautifulSoup

BASE_URL = "https://bstu.uz"


def get_news():
    url = f"{BASE_URL}/articles/yangilik"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    news_list = []

    items = soup.find_all("div", class_="tt_newsitem")

    for item in items:
        try:
            title_tag = item.find("h3").find("a")
            title = title_tag.text.strip()
            link = title_tag["href"]

            img_tag = item.find("img")
            image = img_tag["src"] if img_tag else None

            date_tag = item.find("span", class_="dates")
            date = date_tag.text.strip() if date_tag else None

            news_list.append({
                "title": title,
                "link": link,
                "image": image,
                "date": date
            })

        except Exception as e:
            print("Error parsing item:", e)

    return news_list

def get_news_detail(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # TITLE
    title_tag = soup.find("h1")
    title = title_tag.text.strip() if title_tag else None

    # CONTENT
    paragraphs = soup.select("article.post-content p")
    content = "\n".join([p.text.strip() for p in paragraphs if p.text.strip()])

    # IMAGES
    images = []
    slides = soup.select(".mySlides img")

    for img in slides:
        src = img.get("src")
        if src:
            if src.startswith("/"):
                src = BASE_URL + src
            images.append(src)

    return {
        "title": title,
        "content": content,
        "images": images
    }