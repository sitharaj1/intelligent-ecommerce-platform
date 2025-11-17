
# Intelligent eCommerce Platform

This is a **portfolio-friendly end-to-end data project** that simulates an intelligent eCommerce analytics platform.

It demonstrates:

- Ingestion of **Sentinel-style logs** (synthetic)
- **Medallion-style** data layout (Bronze / Silver / Gold)
- **Python ETL** to transform and aggregate data
- Loading curated data into a **SQLite database** as a serving layer
- A simple **ML model** (customer churn-style score)
- A static **HTML dashboard** prototype (Bootstrap + Chart.js)

You can put this repo directly on GitHub to show skills in:
data engineering, SQL, Python, basic ML, and dashboarding.

---

## 1. Folder Structure

```text
Intelligent_eCommerce_Platform/
├── README.md
├── requirements.txt
└── Dev/
    ├── sentinel/
    │   └── sentinel_logs_raw.json
    ├── synthetic_data/
    │   ├── bronze/
    │   │   ├── bronze_orders.json
    │   │   ├── bronze_products.json
    │   │   ├── bronze_customers.json
    │   │   └── bronze_sentinel_logs.json
    │   ├── silver/
    │   │   ├── silver_orders.csv
    │   │   ├── silver_products.csv
    │   │   └── silver_events.csv
    │   └── gold/
    │       ├── gold_daily_sales.csv
    │       └── gold_customer_360.csv
    ├── scripts/
    │   ├── etl_transform.py
    │   └── load_to_db.py
    ├── ml/
    │   └── train_churn_model.py
    ├── db/
    │   ├── schema.sql
    │   └── intelligent_ecommerce.db
    └── dashboard/
        └── sample_dashboard.html
```

---

## 2. Quick Start

### 2.1. Install dependencies

From the project root:

```bash
pip install -r requirements.txt
```

### 2.2. (Optional) Regenerate Silver / Gold from Bronze

To show the ETL flow, you can re-run the transforms that take Bronze JSON and create Silver/Gold CSVs:

```bash
cd Dev/scripts
python etl_transform.py
```

This will recreate:

- `Dev/synthetic_data/silver/*.csv`
- `Dev/synthetic_data/gold/gold_daily_sales.csv`

### 2.3. (Optional) Rebuild the SQLite database

```bash
cd Dev/scripts
python load_to_db.py
```

This will:

- Create / overwrite `Dev/db/intelligent_ecommerce.db`
- Create tables using `Dev/db/schema.sql`
- Load Silver & Gold CSVs into:
  - `silver_orders`
  - `silver_products`
  - `silver_events`
  - `gold_daily_sales`
  - `gold_customer_360`

---

## 3. ML Example – Churn-style Model

In `Dev/ml/train_churn_model.py` a very small **RandomForestClassifier** is trained on the synthetic `gold_customer_360.csv`:

- Uses features:
  - `lifetime_value`
  - `num_orders`
  - `avg_order_value`
  - `days_since_last_purchase`
- Derives a label:
  - `is_high_churn = churn_score > 0.5`
- Prints:
  - ROC-AUC score
  - Classification report

Run it via:

```bash
cd Dev/ml
python train_churn_model.py
```

> This is intentionally tiny and synthetic – it’s for showing the pattern, not for real modelling.

---

## 4. Dashboard

The dashboard is a **static HTML mock** that pretends to be powered by the serving DB:

- File: `Dev/dashboard/sample_dashboard.html`
- Stack:
  - [Bootstrap](https://getbootstrap.com/) for layout
  - [Chart.js](https://www.chartjs.org/) for charts

Open it by double-clicking it or using:

```bash
# From project root on many systems:
open Dev/dashboard/sample_dashboard.html    # macOS
xdg-open Dev/dashboard/sample_dashboard.html  # Linux
start Dev\dashboard\sample_dashboard.html  # Windows
```

It displays:

- KPI cards (Total Revenue, Orders, Conversion Rate, Anomalies)
- Line chart for **daily revenue**
- Bar chart for a **session funnel**

You can mention in your CV / interview that a real implementation would bind this to the DB.

---

## 5. How to Talk About This Project

Suggested wording for your **CV / LinkedIn / GitHub description**:

> Built an end-to-end Intelligent eCommerce data platform using a Medallion-style architecture (Bronze/Silver/Gold). Ingested synthetic Sentinel-style logs and transactional data, developed Python-based ETL pipelines to produce curated Silver and Gold datasets, and loaded them into a SQLite serving database. Implemented a simple churn-style machine learning model and exposed business KPIs through a static dashboard prototype using Bootstrap and Chart.js.

You can also link directly to:

- `/Dev/scripts` to highlight **ETL & DB loading**
- `/Dev/ml` to highlight **ML**
- `/Dev/dashboard` to highlight **visualisation**.

---

## 6. Requirements

`requirements.txt` currently includes only:

```text
pandas
```

If you want to run the ML script, also install scikit-learn:

```bash
pip install scikit-learn
```

(You can also add `scikit-learn` to requirements.txt if you like.)

---

## 7. Notes

- All data is synthetic and safe to publish publicly.
- Structure is deliberately simple and readable for recruiters and reviewers.
