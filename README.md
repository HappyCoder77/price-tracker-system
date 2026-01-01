# 🚀 Price Tracker System

A professional Python-based web scraper that monitors book prices, stores them in a SQLite database, and alerts you when prices drop.

## ✨ Features

- **Automated Scraping**: Fetches the latest prices from "Books to Scrape".
- **Historical Tracking**: Stores price history to detect real discounts.
- **Instant Alerts**: Visual terminal alerts with price drop calculations.
- **CSV Export**: Automatically records all deals in `detected_deals.csv` with timestamps.
- **Type Safety**: 100% static type checking coverage with mypy.
- **Enhanced UX**: Real-time visual progress monitoring via tqdm.

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Libraries**: Requests, BeautifulSoup4, tqdm
- **Dev Tools**: Mypy (Type Checking), Flake8 (Linting)
- **Workflow**: Git Flow with atomic, feature-based commits.

## 🛠️ Installation

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

## 🚀 Usage

Run the main orchestrator to start tracking:

```bash
python3 main.py
```

To simulate a price drop for testing:

```bash
python3 simulate_drop.py
```

## 🛡️ Quality Assurance

Run type checking to ensure code integrity:

```bash
mypy .
```

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
- **Scheduled Execution**: Set up a `cron` job or use the `schedule` library to run the tracker every 24 hours.
