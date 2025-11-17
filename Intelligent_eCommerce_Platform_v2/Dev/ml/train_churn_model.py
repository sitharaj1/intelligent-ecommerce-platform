
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, classification_report

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GOLD_DIR = os.path.join(BASE_DIR, "synthetic_data", "gold")

def load_data():
    path = os.path.join(GOLD_DIR, "gold_customer_360.csv")
    df = pd.read_csv(path)
    df["is_high_churn"] = (df["churn_score"] > 0.5).astype(int)
    feature_cols = ["lifetime_value", "num_orders", "avg_order_value", "days_since_last_purchase"]
    X = df[feature_cols]
    y = df["is_high_churn"]
    return X, y

def train_model():
    X, y = load_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, y_pred_proba)
    print(f"ROC-AUC: {auc:.3f}")
    print("Classification report:")
    y_pred = (y_pred_proba > 0.5).astype(int)
    print(classification_report(y_test, y_pred))
    return model

if __name__ == "__main__":
    train_model()
