import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

def train_bill_model(input_path, model_path):
    df = pd.read_csv(input_path)

    # Predict 'bill_amount'
    target = 'bill_amount'
    if target not in df.columns:
        print(f"Column '{target}' not found!")
        return

    X = df.drop(columns=[target])
    y = df[target]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save model
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)
    print(f"Bill model saved at {model_path}")

if __name__ == "__main__":
    input_csv = '../output/feature_dataset.csv'
    model_file = './models/bill_model.pkl'
    train_bill_model(input_csv, model_file)