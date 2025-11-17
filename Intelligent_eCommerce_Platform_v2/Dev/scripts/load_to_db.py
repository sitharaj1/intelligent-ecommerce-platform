
import os
import sqlite3
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SILVER_DIR = os.path.join(BASE_DIR, "synthetic_data", "silver")
GOLD_DIR = os.path.join(BASE_DIR, "synthetic_data", "gold")
DB_DIR = os.path.join(BASE_DIR, "db")
DB_PATH = os.path.join(DB_DIR, "intelligent_ecommerce.db")
SCHEMA_PATH = os.path.join(DB_DIR, "schema.sql")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    with open(SCHEMA_PATH, "r") as f:
        schema_sql = f.read()
    conn.executescript(schema_sql)
    conn.commit()
    conn.close()
    print("Database initialized with schema.")

def load_csv_to_table(csv_path, table_name):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    print(f"Loaded {csv_path} into {table_name}.")

if __name__ == "__main__":
    init_db()
    load_csv_to_table(os.path.join(SILVER_DIR, "silver_orders.csv"), "silver_orders")
    load_csv_to_table(os.path.join(SILVER_DIR, "silver_products.csv"), "silver_products")
    load_csv_to_table(os.path.join(SILVER_DIR, "silver_events.csv"), "silver_events")
    load_csv_to_table(os.path.join(GOLD_DIR, "gold_daily_sales.csv"), "gold_daily_sales")
    load_csv_to_table(os.path.join(GOLD_DIR, "gold_customer_360.csv"), "gold_customer_360")
