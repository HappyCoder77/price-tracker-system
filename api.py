from fastapi import FastAPI, HTTPException
from database_manager import get_connection
import logging


app = FastAPI(
    title="Price Tracker API",
    description="Professional API to monitor book prices and deals",
    version="1.0.0",
)


@app.get("/")
def read_root():
    """Welcome endpoint for the API."""
    return {
        "message": "Welcome to the Price Tracker API",
        "status": "online",
        "documentation": "/docs",
    }


@app.get("/products")
def get_all_products():
    """Returns every book being tracked."""

    try:
        conn = get_connection()
        conn.row_factory = lambda cursor, row: {
            col[0]: row[i] for i, col in enumerate(cursor.description)
        }

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        data = cursor.fetchall()
        conn.close()

        return {"count": len(data), "products": data}
    except Exception as e:
        logging.error(f"API Error: {e}")
        raise HTTPException(status_code=500, detail="Database error")


@app.get("/deals")
def get_deals():
    """
    Returns only the books where the current price is lower than the previous one,
    indicating a real discount.
    """

    try:
        conn = get_connection()
        conn.row_factory = lambda cursor, row: {
            col[0]: row[i] for i, col in enumerate(cursor.description)
        }

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE current_price < last_price")
        deals = cursor.fetchall()
        conn.close()

        return {"status": "success", "deals_found": len(deals), "data": deals}
    except Exception as e:
        logging.error(f"Error fetching deals: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
