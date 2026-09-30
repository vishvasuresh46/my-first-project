import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import os

def train_energy_model(input_path, model_path):
    df = pd.read_csv(input_path)

    target = "energy_consumption"

    X = df.drop(columns=[target])
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    print("Model Training Completed!")
    print("MAE:", round(mean_absolute_error(y_test, predictions), 3))
    print("R2 Score:", round(r2_score(y_test, predictions), 3))

    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)
    print(f"Model saved at {model_path}")

if __name__ == "__main__":
    input_csv = "../output/feature_dataset.csv"
    model_file = "./models/energy_model.pkl"
    train_energy_model(input_csv, model_file)