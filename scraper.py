import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from database_manager import update_product_price, init_db
from typing import List, Dict, Any


def scrape_books(url: str) -> None:
    """
    Scrapes book data from the provided URL and updates the database.
    Args:
        url (str): The target URL to scrape.
    """

    try:
        response = requests.get(url=url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article", class_="product_pod")

        print(f"Found {len(books)} books. Updating database...")

        for book in tqdm(books, desc="Processings books"):
            title: str = book.h3.a["title"]
            raw_price_str: str = book.find("p", class_="price_color").text
            clean_price_str: str = "".join(
                char for char in raw_price_str if char.isdigit() or char == "."
            )
            price: float = float(clean_price_str)

            update_product_price(name=title, price=price)

    except Exception as e:
        print(f"Error during scraping. {e}")


if __name__ == "__main__":
    init_db()

    TARGET_URL: str = (
        "http://books.toscrape.com/catalogue/category/books/romance_8/index.html"
    )

    scrape_books(TARGET_URL)
