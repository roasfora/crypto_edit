# 📈 Crypto Project – Automated Data Pipeline for Bitcoin & FX Rates

This project implements an automated data pipeline to collect, store, and analyze cryptocurrency price data (Bitcoin) and EUR/USD exchange rates. It integrates with the **Coinbase API** and performs **web scraping** from *x-rates.com*. The pipeline supports **local CSV storage**, **PostgreSQL integration**, and **dbt transformations** for analytics. CI/CD is handled via **GitHub Actions**.

---

## 🚀 Project Overview

This pipeline is split into two main components:

### 🔗 1. API Integration (Coinbase)

- Fetches real-time Bitcoin price data.
- Records timestamps and price in USD.
- Stores the data locally in CSV.

### 🕸️ 2. Web Scraping (x-rates.com)

- Extracts current EUR to USD exchange rate.
- Includes timestamping for historical analysis.
- Stores the data in CSV for further transformation or upload.

---

## 📁 Project Structure

```
Crypto_Project/
│
├── src/                    # Source code for pipeline
│   ├── api_client.py       # Bitcoin price fetcher
│   ├── web_scraping.py     # FX rate scraper
│   ├── postgresql.py       # Upload logic for PostgreSQL
│   ├── main.py             # Pipeline orchestrator
│   └── __init__.py
│
├── data/                   # Raw + processed CSV files
│   ├── bitcoin_prices.csv
│   └── eur_to_usd_rates.csv
│
├── tests/                  # Unit tests
│   ├── test_api_client.py
│   ├── test_web_scraping.py
│   └── __init__.py
│
├── docs/                   # Documentation
│   └── README.md
│
└── .github/
    └── workflows/
        └── test_pipeline.yml  # GitHub Actions for CI
```

---

## ⚙️ How It Works

### 🪙 Bitcoin Price Collection

- Script: `src/api_client.py`
- Output: `data/bitcoin_prices.csv`
- Columns:
  - `timestamp` (UTC)
  - `price` (USD)
  - `currency` (e.g., USD)

### 💱 EUR to USD Exchange Rate Scraping

- Script: `src/web_scraping.py`
- Output: `data/eur_to_usd_rates.csv`
- Columns:
  - `timestamp` (UTC)
  - `exchange_rate` (EUR → USD)

### 🧱 Data Storage & Transformation

- **Local**: CSV format
- **PostgreSQL**: Use `postgresql.py` to upload to DB
- **dbt**: For transformations and business logic modeling

---

## 🔧 Setup & Installation

### ✅ Prerequisites

- Python ≥ 3.8
- PostgreSQL database (local or hosted)
- `pip` (Python package installer)
- (Optional) `virtualenv` or `venv`

### 📦 Installation Steps

```bash
# Clone the repo
git clone https://github.com/roasfora/crypto_edit.git
cd crypto_edit

# Set up virtual environment
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
# OR
.venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 🧪 Running the Project

### 1. Run API Client
```bash
python src/api_client.py
```

### 2. Run Web Scraper
```bash
python src/web_scraping.py
```

### 3. Upload to PostgreSQL (if configured)
```bash
python src/postgresql.py
```

### 4. Run full pipeline
```bash
python src/main.py
```

---

## 📈 Analytics with dbt (Optional)

If you're using `dbt`:

```bash
cd dbt_project/
dbt run
```

---

## ✅ CI/CD

- GitHub Actions automatically tests scripts on push.
- Located in `.github/workflows/test_pipeline.yml`.

---

## 📃 License

This project is licensed under the **MIT License** — feel free to use and modify with attribution.

---

## 🙋‍♂️ Author

**Rodrigo Moutinho**  
📧 [roasfora@hotmail.com](mailto:roasfora@hotmail.com)  
🔗 [GitHub](https://github.com/roasfora) | [LinkedIn](https://www.linkedin.com/in/rodrigo-moutinho-31a03778/)  

---

> 🚀 Built for learning, experimentation, and production-ready ETL workflows.
