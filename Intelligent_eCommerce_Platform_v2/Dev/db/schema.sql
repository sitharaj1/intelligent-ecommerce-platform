
-- Schema for Intelligent eCommerce Platform (Silver/Gold subset)

CREATE TABLE IF NOT EXISTS silver_orders (
    order_id TEXT PRIMARY KEY,
    customer_id TEXT,
    order_date TEXT,
    total_amount REAL,
    status TEXT
);

CREATE TABLE IF NOT EXISTS silver_products (
    product_id TEXT PRIMARY KEY,
    name TEXT,
    category TEXT,
    brand TEXT,
    price REAL,
    stock_quantity INTEGER
);

CREATE TABLE IF NOT EXISTS silver_events (
    event_id INTEGER PRIMARY KEY,
    timestamp_utc TEXT,
    user_id TEXT,
    session_id TEXT,
    event_type TEXT,
    source_ip TEXT,
    device_type TEXT,
    url TEXT
);

CREATE TABLE IF NOT EXISTS gold_daily_sales (
    date TEXT PRIMARY KEY,
    total_revenue REAL,
    total_orders INTEGER,
    avg_order_value REAL,
    unique_customers INTEGER,
    refunds INTEGER,
    conversion_rate REAL
);

CREATE TABLE IF NOT EXISTS gold_customer_360 (
    customer_id TEXT PRIMARY KEY,
    lifetime_value REAL,
    num_orders INTEGER,
    avg_order_value REAL,
    days_since_last_purchase INTEGER,
    preferred_category TEXT,
    churn_score REAL
);
