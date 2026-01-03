import os
import logging
from logger_config import setup_logging
import sqlite3
from sqlite3 import Connection
from datetime import datetime
from dotenv import load_dotenv


setup_logging()

load_dotenv()
# Use environment variables for the database path, defaulting to local
# This makes the app "Cloud-ready"

IS_RAILWAY = os.getenv("RAILWAY_ENVIRONMENT_NAME") is not None

if os.path.exists("/data"):
    DB_PATH = "/data/books_tracker.db"
    logging.info(f"Volume detected at: {DB_PATH}")
elif os.getenv("RAILWAY_ENVIRONMENT_NAME"):
    DB_PATH = "/tmp/books_tracker.db"
    logging.info(f"Cloud environment detected. DB Path: {DB_PATH}")
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.getenv("DATABASE_URL", os.path.join(BASE_DIR, "books_tracker.db"))
    logging.info(f"Local environment detected. DB Path: {DB_PATH}")


def get_connection() -> Connection:
    """
    stablishes a connection to the SQLite database using an environment-aware path.
    """
    try:
        return sqlite3.connect(DB_PATH)
    except sqlite3.Error as e:
        logging.error(f"Databasse connection error: {e}")
        raise


def init_db() -> None:
    """
    Initializes the database and creates the products table if it doesn't exist.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            current_price REAL,
            last_price REAL,
            last_updated DATETIME
        )
        """
    )

    conn.commit()
    conn.close()
    logging.info("Database initialized successfully!")


def update_product_price(name: str, price: float) -> None:
    """
    Inserts a new product or updates its price if it already exists.
    Args:
        name (str): The name of the book/product.
        price (float): The current price found.
    """

    conn: Connection = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT current_price FROM products WHERE name = ?", (name,))
    result = cursor.fetchone()

    now: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if result:
        old_price: float = result[0]

        if old_price != price:
            cursor.execute(
                """UPDATE products 
                SET last_price = ?, current_price = ?, last_updated = ?
                WHERE name = ?""",
                (old_price, price, now, name),
            )

            logging.info(f"Update: {name} changed from {old_price} to {price}")
    else:
        cursor.execute(
            """
            INSERT INTO products (name, current_price, last_price, last_updated)
            VALUES (?, ?, ?, ?)
            
            """,
            (name, price, None, now),
        )

        logging.info(f"New product added: {name} at {price}")

    conn.commit()
    conn.close()
