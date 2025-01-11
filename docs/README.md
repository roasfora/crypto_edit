#Crypto Project
This project is a data pipeline designed to collect and manage cryptocurrency data. It integrates with the Coinbase API to fetch Bitcoin price data and scrapes the EUR to USD exchange rate from the web. The collected data is stored locally in CSV files and can be further uploaded to a PostgreSQL database for analysis. Additionally, this project leverages dbt for data transformation and analytics.

##Project Overview
The project automates the collection of cryptocurrency and exchange rate data. It consists of two main components:

###API Integration:

Connects to the Coinbase API to fetch real-time Bitcoin price data.
Ensures accurate timestamping of the data for historical tracking.

###Web Scraping:

Scrapes the EUR to USD exchange rate from x-rates.com.
Provides an up-to-date exchange rate for financial analysis.
The pipeline is built using Python and includes functionality for storing the data in local CSV files and uploading it to a PostgreSQL database.

##Project Structure

plaintext
Copy code
Crypto_Project/
│
├── src/                      # Source code for the project
│   ├── api_client.py         # Fetches Bitcoin price data from Coinbase API
│   ├── web_scraping.py       # Scrapes EUR to USD exchange rate data
│   ├── postgresql.py         # Handles uploading CSV data to PostgreSQL
│   ├── main.py               # Orchestrates data collection and saving processes
│   └── __init__.py           # Marks src as a package
│
├── data/                     # Contains raw and processed CSV files
│   ├── bitcoin_prices.csv    # Bitcoin price data
│   ├── eur_to_usd_rates.csv  # EUR to USD exchange rates
│
├── tests/                    # Unit tests for the project
│   ├── test_api_client.py    # Tests for API integration
│   ├── test_web_scraping.py  # Tests for web scraping
│   ├── __init__.py           # Marks tests as a package
│
├── docs/                     # Documentation files
│   └── README.md             # Project documentation
│
└── .github/
    └── workflows/
        └── test_pipeline.yml # GitHub Actions configuration for CI pipeline

##How It Works

###1. Bitcoin Price Data Collection
The api_client.py script connects to the Coinbase API to fetch the current Bitcoin price. The data includes:

Timestamp: When the price was fetched (in UTC).
Price: Current price of Bitcoin in USD.
Currency: Currency code (e.g., "USD").
The data is saved in a CSV file (data/bitcoin_prices.csv) for further use.

###2. EUR to USD Exchange Rate Scraping
The web_scraping.py script scrapes the EUR to USD exchange rate from x-rates.com. The data includes:

Timestamp: The time of scraping (in UTC).
Exchange Rate: Current EUR to USD rate.
The data is saved in a CSV file (data/eur_to_usd_rates.csv) for later analysis.

###3. Data Storage and Analysis
CSV Files: The data is stored locally in CSV files.
PostgreSQL: Data can be uploaded to a PostgreSQL database for further analysis using the postgresql.py script.
DBT: Enables transformation and analytics on the stored data.


##Setup and Prerequisites
###Prerequisites
Python 3.8 or higher
PostgreSQL database
pip (Python package manager)
Recommended: Virtual environment for managing dependencies

###Installation

Clone the repository:

bash
Copy code
git clone https://github.com/roasfora/crypto_edit.git
cd crypto_edit
Set up a virtual environment:

bash
Copy code
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt