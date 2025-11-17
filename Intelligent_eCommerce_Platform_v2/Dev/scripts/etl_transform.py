
import os
import json
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRONZE_DIR = os.path.join(BASE_DIR, "synthetic_data", "bronze")
SILVER_DIR = os.path.join(BASE_DIR, "synthetic_data", "silver")
GOLD_DIR = os.path.join(BASE_DIR, "synthetic_data", "gold")

os.makedirs(SILVER_DIR, exist_ok=True)
os.makedirs(GOLD_DIR, exist_ok=True)

def load_bronze_json(filename):
    path = os.path.join(BRONZE_DIR, filename)
    with open(path, "r") as f:
        return json.load(f)

def transform_orders():
    orders = load_bronze_json("bronze_orders.json")
    df = pd.DataFrame(orders)
    df["order_date"] = df["created_at"].str.slice(0, 10)
    silver = df[["order_id", "user_id", "order_date", "amount", "status"]].rename(
        columns={"user_id": "customer_id", "amount": "total_amount"}
    )
    silver.to_csv(os.path.join(SILVER_DIR, "silver_orders.csv"), index=False)
    print("silver_orders.csv created.")

def transform_products():
    products = load_bronze_json("bronze_products.json")
    df = pd.DataFrame(products)
    df.to_csv(os.path.join(SILVER_DIR, "silver_products.csv"), index=False)
    print("silver_products.csv created.")

def transform_sentinel_to_events():
    logs = load_bronze_json("bronze_sentinel_logs.json")
    df = pd.DataFrame(logs)
    df["event_id"] = range(1, len(df) + 1)
    df = df.rename(columns={
        "timestamp": "timestamp_utc",
        "ip_address": "source_ip",
        "device": "device_type"
    })
    cols = ["event_id", "timestamp_utc", "user_id", "session_id", "event_type", "source_ip", "device_type", "url"]
    df[cols].to_csv(os.path.join(SILVER_DIR, "silver_events.csv"), index=False)
    print("silver_events.csv created.")

def build_gold_daily_sales():
    silver_orders = pd.read_csv(os.path.join(SILVER_DIR, "silver_orders.csv"))
    grouped = silver_orders.groupby("order_date").agg(
        total_revenue=("total_amount", "sum"),
        total_orders=("order_id", "count")
    ).reset_index().rename(columns={"order_date": "date"})
    grouped["avg_order_value"] = grouped["total_revenue"] / grouped["total_orders"]
    grouped["unique_customers"] = grouped["total_orders"]
    grouped["refunds"] = (silver_orders["status"] == "refunded").groupby(silver_orders["order_date"]).sum().values
    grouped["conversion_rate"] = 2.0  # dummy value
    grouped.to_csv(os.path.join(GOLD_DIR, "gold_daily_sales.csv"), index=False)
    print("gold_daily_sales.csv created.")

if __name__ == "__main__":
    transform_orders()
    transform_products()
    transform_sentinel_to_events()
    build_gold_daily_sales()
