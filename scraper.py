import sys
import requests
import logging
from logger_config import setup_logging
from bs4 import BeautifulSoup
from tqdm import tqdm
from database_manager import update_product_price, init_db


setup_logging()


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

        logging.info(f"Found {len(books)} books. Updating database...")

        is_tty = sys.stdout.isatty()

        for book in tqdm(books, desc="Processing books", disable=not is_tty):
            h3_tag = book.find("h3")

            if h3_tag and h3_tag.a:
                title_attr = h3_tag.a.get("title")
                title = str(title_attr).strip() if title_attr else "Unknown Title"
            else:
                title = "Unknown Title"

            price_tag = book.find("p", class_="price_color")

            if price_tag:
                # Now mypy knows price_tag is not None
                price_str = price_tag.text
            else:
                price_str = "£0.00"
            clean_price_str: str = "".join(
                char for char in price_str if char.isdigit() or char == "."
            )

            price: float = float(clean_price_str)

            update_product_price(name=title, price=price)

    except Exception as e:
        logging.error(f"Error during scraping. {e}")


if __name__ == "__main__":
    init_db()

    TARGET_URL: str = (
        "http://books.toscrape.com/catalogue/category/books/romance_8/index.html"
    )

    scrape_books(TARGET_URL)
