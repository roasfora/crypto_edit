# Crypto Project

This project collects Bitcoin price data from the Coinbase API and the EUR to USD exchange rate through web scraping. The data is stored locally in CSV files and uploaded to a PostgreSQL database for analysis. Additionally, the project leverages dbt for data transformation and analytics.

## Project Structure

src/: Source code for the project, including data collection and database upload scripts.
api_client.py: Fetches Bitcoin price data from the Coinbase API.
web_scraping.py: Scrapes EUR to USD exchange rate data.
main.py: Orchestrates the data collection and saving processes.
postgresql.py: Handles uploading CSV data to the PostgreSQL database.
data/: Contains raw and processed CSV files.
bitcoin_prices.csv: Bitcoin price data.
eur_to_usd_rates.csv: EUR to USD exchange rates.
tests/: Unit tests for the project.
docs/: Documentation files.
crypto_project/dbt_project.yml: dbt project configuration for data transformation and analytics.

## Getting Started

## Prerequisites
Python 3.8 or higher
PostgreSQL database
pip (Python package manager)
Recommended: Virtual environment for managing dependencies