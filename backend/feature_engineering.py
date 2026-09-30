import pandas as pd
import os

def feature_engineering(input_path, output_path):
    df = pd.read_csv(input_path)

    # Convert timestamp
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Create new features
    df['hour'] = df['timestamp'].dt.hour
    df['day'] = df['timestamp'].dt.day
    df['month'] = df['timestamp'].dt.month
    df['day_of_week'] = df['timestamp'].dt.dayofweek

    # Drop timestamp (model cannot use datetime directly)
    df = df.drop(columns=['timestamp'])

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)

    print("Feature engineering completed!")
    print(df.head())

    return df


if __name__ == "__main__":
    input_csv = '../output/processed_dataset.csv'
    output_csv = '../output/feature_dataset.csv'
    feature_engineering(input_csv, output_csv)