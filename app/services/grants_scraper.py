import httpx
from bs4 import BeautifulSoup

URL = "https://bstu.uz/malumot/stipendiyalar-va-grantlar"

headers = {
    "User-Agent": "Mozilla/5.0"
}


async def get_grants_data():
    async with httpx.AsyncClient(headers=headers) as client:
        response = await client.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    figures = soup.find_all("figure", class_="table")

    results = []

    for fig in figures:
        table = fig.find("table")
        if not table:
            continue

        rows = table.find_all("tr")

        # 🔥 faqat 3 ustunli jadvalni olamiz
        if len(rows) < 2:
            continue

        first_row_cols = rows[0].find_all("td")

        if len(first_row_cols) != 3:
            continue  # kerakli jadval emas

        # 🎯 shu bizga kerakli jadval
        for row in rows[1:]:
            cols = row.find_all("td")

            if len(cols) < 3:
                continue

            index = cols[0].get_text(strip=True)
            status = cols[1].get_text(strip=True)
            amount = cols[2].get_text(strip=True)

            results.append({
                "id": index,
                "status": status,
                "amount": amount
            })

        break  # faqat bitta jadval yetadi

    return results