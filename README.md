# 🚀 Price Tracker System

A professional Python-based API and web scraper that monitors book prices, stores them in a persistent SQLite database, and provides a RESTful interface for data access.

## ✨ Features

- **Automated Internal Scheduler**: Background worker that executes the scraper every 6 hours using the `schedule` library.
- **RESTful API**: Built with **FastAPI** to expose real-time product data and price trends.
- **Cloud Persistent Storage**: Integrated with **Railway Volumes** for durable SQLite data storage.
- **Historical Tracking**: Stores price history to detect discounts and market changes.
- **Security**: Protected endpoints via **X-API-KEY** header authentication.
- **Reliable Architecture**: Monolithic design ensuring the scraper and API share the same database state seamlessly.

## 🛠️ Tech Stack

- **Framework**: FastAPI (Asynchronous API).
- **Server**: Uvicorn (ASGI).
- **Scraper**: Requests & BeautifulSoup4.
- **Database**: SQLite with Persistent Volumes.
- **Automation**: Internal Python `threading` & `schedule` library.

## 🏗️ Cloud Infrastructure (Railway)

The system is designed to run in a cloud container with the following mount configuration:

- **Mount Path**: `/data`.
- **DB Location**: `/data/books_tracker.db` (Persistent) .

## 🛠️ Installation & Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/HappyCoder77/price-tracker-system
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv price-tracker-env
   source price-tracker-env/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Environment Variables: Create a .env file (or set in Railway, except DEBUG):

   ```text
   DEBUG=True
   DATABASE_URL=books_tracker.db
   API_KEY=your_secure_key_here
   ```

## 🚀 Usage

Local development

```bash
uvicorn api:app --reload
```

API Endpoints

- **GET** `/`: Welcome message and status.

- **GET** `/products`: Retrieve all tracked books (Requires X-API-KEY).

- **GET** `/docs`: Interactive Swagger UI documentation.

## 🛡️ Quality Assurance

- **Type Safety**: 100% coverage with `mypy`.
- **Git Workflow**: Branch-based development (`feature/*`) before merging to `main`.

## 🛠️ Technical Details: Database Schema

The system uses **SQLite** for lightweight, serverless data storage. The core logic relies on a single table that tracks price changes between scraping sessions.

### Table: `products`

| Column          | Type      | Description                                                |
| :-------------- | :-------- | :--------------------------------------------------------- |
| `name`          | TEXT (PK) | Unique name of the book.                                   |
| `current_price` | REAL      | The most recently scraped price.                           |
| `last_price`    | REAL      | The price from the previous session (used for comparison). |

### Price Detection Logic

When the scraper runs, the system follows these steps:

1. It checks if the book already exists in the database.
2. If it exists, it moves the value from `current_price` to `last_price`.
3. It updates `current_price` with the newly scraped value.
4. An alert is triggered only if `current_price < last_price`.

## 🔮 Future Improvements

- **Email Notifications**: Integrate `smtplib` to send automated emails when a deal is found.
- **Web Dashboard**: Create a simple UI using **Streamlit** or **Flask** to visualize price trends.
- **Multi-Category Support**: Expand the scraper to monitor different genres or even other websites.
