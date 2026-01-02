import sqlite3
from database_manager import get_connection
from typing import Optional


def simulate_price_drop(product_name: str, new_price: float) -> None:
    """
    Manually updates a product's price to simulate a discount for testing.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Using LOWER and % for flexible matching
    cursor.execute(
        "UPDATE products SET last_price = current_price, current_price = ? WHERE LOWER(name) LIKE LOWER(?)",
        (new_price, f"%{product_name}%"),
    )

    if cursor.rowcount > 0:
        print(f"✅ Success: Simulated price drop for '{product_name}' to £{new_price}")
    else:
        print(f"❌ Error: Product '{product_name}' not found.")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    # Example: simulate a drop for a Romance book
    simulate_price_drop("the", 9.99)
