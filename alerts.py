import sqlite3
from database_manager import get_connection
from typing import List, Tuple


def check_for_deals() -> None:
    """
    Queries the database for products where current price < last price.
    """

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT name, last_price, current_price
        FROM products
        WHERE current_price < last_price
        AND last_price is NOT NULL
    """

    cursor.execute(query)
    deals: List[Tuple[str, float, float]] = cursor.fetchall()

    if not deals:
        print("🔍 Not deals found yet")
    else:
        print(f"📢 Alert: found {len(deals)} price drops!")

        for name, old_price, new_price in deals:
            savings = old_price - new_price
            print(f"💎 {name}: £{old_price} -> £{new_price} (Save: £{savings:.2f})")

    conn.close()
