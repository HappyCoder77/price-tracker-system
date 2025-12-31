# 🚀 Price Tracker System

A professional Python-based web scraper that monitors book prices, stores them in a SQLite database, and alerts you when prices drop.

## ✨ Features

- **Automated Scraping**: Fetches the latest prices from "Books to Scrape".
- **Historical Tracking**: Stores price history to detect real discounts.
- **Instant Alerts**: Visual terminal alerts with price drop calculations.
- **CSV Export**: Automatically records all deals in `detected_deals.csv` with timestamps.

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

## 🔮 Future Improvements

- **Email Notifications**: Integrate `smtplib` to send automated emails when a deal is found.
- **Web Dashboard**: Create a simple UI using **Streamlit** or **Flask** to visualize price trends.
- **Multi-Category Support**: Expand the scraper to monitor different genres or even other websites.
- **Scheduled Execution**: Set up a `cron` job or use the `schedule` library to run the tracker every 24 hours.
