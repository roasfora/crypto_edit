import pandas as pd
import psycopg2
import os

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT"))
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


# Paths to your CSV files
BITCOIN_PRICES_CSV = r"C:\Users\isabe\Desktop\EDIT\EDIT\Data Ops\Crypto_Project\data\bitcoin_prices.csv"
EUR_TO_USD_RATES_CSV = r"C:\Users\isabe\Desktop\EDIT\EDIT\Data Ops\Crypto_Project\data\eur_to_usd_rates.csv"

# Function to upload a CSV to a PostgreSQL table
def upload_csv_to_db(csv_file, table_name, conn):
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(csv_file)

        # Create a cursor object
        cur = conn.cursor()

        # Create the table if it doesn't exist
        columns = ", ".join([f"{col} TEXT" for col in df.columns])
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});"
        cur.execute(create_table_query)
        conn.commit()

        # Insert data into the table
        for _, row in df.iterrows():
            values = ", ".join([f"'{value}'" for value in row.values])
            insert_query = f"INSERT INTO {table_name} VALUES ({values});"
            cur.execute(insert_query)

        # Commit the transaction
        conn.commit()
        print(f"Data from {csv_file} uploaded to {table_name} successfully.")
    except Exception as e:
        print(f"Error uploading {csv_file} to {table_name}: {e}")
    finally:
        cur.close()

# Main function to upload both CSVs
def main():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
        )
        print("Connected to the database.")

        # Upload the CSV files to their respective tables
        upload_csv_to_db(BITCOIN_PRICES_CSV, "bitcoin_prices", conn)
        upload_csv_to_db(EUR_TO_USD_RATES_CSV, "eur_to_usd_rates", conn)

    except Exception as e:
        print(f"Error connecting to the database: {e}")
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    main()
