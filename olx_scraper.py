import requests
from bs4 import BeautifulSoup
import json

def scrape_olx_car_covers():
    url = "https://www.olx.in/items/q-car-cover"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed to fetch OLX page")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    items = []

    for product in soup.find_all("li", {"data-aut-id": "itemBox"}):
        title = product.find("span")
        price = product.find("span", {"data-aut-id": "itemPrice"})
        link = product.find("a", href=True)

        items.append({
            "title": title.text.strip() if title else "N/A",
            "price": price.text.strip() if price else "N/A",
            "link": "https://www.olx.in" + link['href'] if link else "N/A"
        })

    with open("olx_car_covers.json", "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=4)

    print("Data saved to olx_car_covers.json")

if __name__ == "__main__":
    scrape_olx_car_covers()
