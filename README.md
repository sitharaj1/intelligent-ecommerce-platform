## 📌 About This Project

This project replicates an **industry-style data platform** for an eCommerce business.  
It shows how raw operational logs and transactional data can be transformed into trusted analytics datasets and machine-learning features.

The pipeline includes:

1. **Sentinel-style Logs (raw)**  
   Web events, failed logins, product views, cart actions.

2. **Medallion Architecture**  
   - **Bronze** → raw JSON files  
   - **Silver** → cleaned, normalized CSV tables  
   - **Gold** → aggregated business metrics (daily sales, customer 360)

3. **ETL Scripts (Python)**  
   Scripts under `Dev/scripts/`:
   - `etl_transform.py` → from Bronze to Silver/Gold CSVs  
   - `load_to_db.py` → loads Silver/Gold data into a SQLite DB  

4. **Serving Database (SQLite)**  
   `Dev/db/intelligent_ecommerce.db` holds:
   - `silver_orders`, `silver_products`, `silver_events`
   - `gold_daily_sales`, `gold_customer_360`

5. **Machine Learning**  
   A small churn-style classifier trained from `gold_customer_360.csv` in `Dev/ml/train_churn_model.py`.

6. **Dashboard Prototype**  
   `Dev/dashboard/sample_dashboard.html` is a static HTML dashboard built with Bootstrap + Chart.js.
