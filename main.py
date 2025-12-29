import os
import time
from database_manager import init_db
from scraper import scrape_books
from alerts import check_for_deals


def run_tracker() -> None:
    """Orchestrates the full price tracking workflow."""

    os.system("cls" if os.name == "nt" else "clear")
    print("🚀 PRICE TRACKER SYSTEM - ACTIVE")
    print("=" * 40)

    init_db()
    URL = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
    print("Scanning for latest prices...")
    scrape_books(URL)

    print("\nAnalyzing trends...")
    time.sleep(1)
    check_for_deals()

    print("=" * 40)
    print("✅ Process completed")


if __name__ == "__main__":
    run_tracker()
