# 🚀 Price Tracker System

A professional Python-based API and web scraper that monitors book prices, stores them in a persistent SQLite database, and provides a RESTful interface for data access.

## ✨ Features

- **Automated Internal Scheduler**: Background worker that executes the scraper every 6 hours using the `schedule` library [cite: 2026-01-03].
- **RESTful API**: Built with **FastAPI** to expose real-time product data and price trends [cite: 2026-01-02].
- **Cloud Persistent Storage**: Integrated with **Railway Volumes** for durable SQLite data storage [cite: 2026-01-03].
- **Historical Tracking**: Stores price history to detect discounts and market changes.
- **Security**: Protected endpoints via **X-API-KEY** header authentication [cite: 2026-01-02].
- **Reliable Architecture**: Monolithic design ensuring the scraper and API share the same database state seamlessly [cite: 2026-01-03].

## 🛠️ Tech Stack

- **Framework**: FastAPI (Asynchronous API) [cite: 2026-01-02].
- **Server**: Uvicorn (ASGI) [cite: 2026-01-02].
- **Scraper**: Requests & BeautifulSoup4.
- **Database**: SQLite with Persistent Volumes [cite: 2026-01-03].
- **Automation**: Internal Python `threading` & `schedule` library [cite: 2026-01-03].

## 🏗️ Cloud Infrastructure (Railway)

The system is designed to run in a cloud container with the following mount configuration:

- **Mount Path**: `/data` [cite: 2026-01-03].
- **DB Location**: `/data/books_tracker.db` (Persistent) [cite: 2026-01-03].

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

- **GET** `/products`: Retrieve all tracked books (Requires X-API-KEY) [cite: 2026-01-02].

- **GET** `/docs`: Interactive Swagger UI documentation [cite: 2026-01-02].

## 🛡️ Quality Assurance

- **Type Safety**: 100% coverage with `mypy`.
- **Git Workflow**: Branch-based development (`feature/*`) before merging to `main`.

## 🛠️ Technical Details: Database Schema

The system uses **SQLite** for lightweight, serverless data storage. The core logic relies on a single table that tracks price changes between scraping sessions.

### Table: `products`

| Column          | Type      | Description                                                                   |
| :-------------- | :-------- | :---------------------------------------------------------------------------- |
| `name`          | TEXT (PK) | Unique name of the book [cite: 2025-12-28].                                   |
| `current_price` | REAL      | The most recently scraped price [cite: 2025-12-28].                           |
| `last_price`    | REAL      | The price from the previous session (used for comparison) [cite: 2025-12-28]. |

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
