import pandas as pd

def detect_anomalies(input_path, threshold=2):
    df = pd.read_csv(input_path)

    # Calculate mean & std
    mean = df["energy_consumption"].mean()
    std = df["energy_consumption"].std()

    # Z-score method
    df["anomaly"] = abs(df["energy_consumption"] - mean) > threshold * std

    anomalies = df[df["anomaly"] == True]

    print("Anomaly Detection Completed!")
    print(f"Total anomalies detected: {len(anomalies)}")
    print(anomalies.head())

    return anomalies


if __name__ == "__main__":
    input_csv = "../output/feature_dataset.csv"
    detect_anomalies(input_csv)