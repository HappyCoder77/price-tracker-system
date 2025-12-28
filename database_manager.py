import sqlite3
from sqlite3 import Connection
from datetime import datetime
from typing import Optional


def get_connection() -> Connection:
    """
    Creates and returns a connection to the SQLite database.
    """

    return sqlite3.connect("tracker.db")


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
    print("Database initialized successfully!")


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
                SET last_price = ?, current_price = ?, last_udpated WHERE name = ?""",
                (old_price, price, now, name),
            )

            print(f"Update: {name} changed from {old_price} to {price}")
    else:
        cursor.execute(
            """
            INSERT INTO products (name, current_price, last_price, last_updated)
            VALUES (?, ?, ?, ?)
            
            """,
            (name, price, None, now),
        )

        print(f"New product added: {name} at {price}")

    conn.commit()
    conn.close()
