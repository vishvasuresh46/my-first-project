import pandas as pd

def suggest_optimization(input_path):
    df = pd.read_csv(input_path)

    avg_energy = df["energy_consumption"].mean()

    def suggestion(row):
        if row["energy_consumption"] > avg_energy:
            return "Reduce appliance usage during peak hours"
        else:
            return "Energy usage is normal"

    df["suggestion"] = df.apply(suggestion, axis=1)

    print("Optimization Suggestions Generated!")
    print(df[["energy_consumption", "suggestion"]].head())

    return df


if __name__ == "__main__":
    input_csv = "../output/feature_dataset.csv"
    suggest_optimization(input_csv)