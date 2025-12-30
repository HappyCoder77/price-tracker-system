import csv
from datetime import datetime
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

    save_to_csv(deals=deals)
    conn.close()


def save_to_csv(deals: List[Tuple[str, float, float]]) -> None:
    """Saves the detected deals into a CSV file with a timestamp."""

    filename = "detected_deals.csv"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with open(filename, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if file.tell() == 0:
                writer.writerow(
                    ["Timestamp", "Product name", "Old Price", "New Price", "Savings"]
                )

            for name, old_price, new_price in deals:
                savings = round(old_price - new_price, 2)
                writer.writerow(
                    [timestamp, name, f"£{old_price}", f"£{new_price}", f"£{savings}"]
                )

        print(f"\n📂 Deals automatically exported to {filename}")

    except Exception as e:
        print(f"❌ Error exporting to CSV: {e}")
