import pandas as pd
import os

def preprocess_data(input_path, output_path):
    # Load Excel dataset
    df = pd.read_excel(input_path)
    print("Dataset loaded successfully!")
    print(df.head())

    # Drop missing values
    df = df.dropna()
    print(f"Dataset after cleaning: {df.shape}")

    # Convert timestamp column
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Save as CSV for next steps
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Processed dataset saved at {output_path}")

    return df


if __name__ == "__main__":
    input_excel = '../dataset/dataset.xlsx'
    output_csv = '../output/processed_dataset.csv'
    preprocess_data(input_excel, output_csv)