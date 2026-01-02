import os
import time
import logging
from logger_config import setup_logging
from database_manager import init_db
from scraper import scrape_books
from alerts import check_for_deals

setup_logging()


def run_tracker() -> None:
    """Orchestrates the full price tracking workflow."""

    os.system("cls" if os.name == "nt" else "clear")

    logging.info("🚀 PRICE TRACKER SYSTEM - ACTIVE")

    try:
        logging.debug("Starting connection to the source website...")

        init_db()
        URL = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
        logging.info("Scanning for latest prices...")
        scrape_books(URL)

        logging.info("\nAnalyzing trends...")
        time.sleep(1)
        check_for_deals()

        logging.info("✅ Process completed successfully")

    except Exception as e:
        logging.error(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    run_tracker()
