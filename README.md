# AI Smart Home Energy Optimizer

A machine learning project that analyzes household electricity usage, predicts energy consumption and electricity bills, detects abnormal usage, and suggests ways to reduce energy cost.

## Features

- **Energy prediction**: predicts energy consumption from historical usage data
- **Bill prediction**: estimates the electricity bill using a trained model
- **Anomaly detection**: flags unusual energy usage patterns
- **Optimization engine**: gives suggestions to reduce energy consumption
- **Web interface**: simple frontend with input form, results page and graphs

## Project Structure

```
AI_Smart_Home_Energy_Optimizer/
├── backend/
│   ├── app.py                  # Backend server
│   ├── data_preprocessing.py   # Data cleaning
│   ├── feature_engineering.py  # Feature creation
│   ├── train_energy_model.py   # Trains energy prediction model
│   ├── train_bill_model.py     # Trains bill prediction model
│   ├── anomaly_detection.py    # Detects abnormal usage
│   ├── optimization_engine.py  # Energy saving suggestions
│   ├── energy.db               # Database
│   └── models/                 # Saved trained models (.pkl)
├── frontend/
│   ├── index.html              # Input page
│   ├── result.html             # Results page
│   ├── graph.html              # Graphs page
│   ├── script.js
│   └── style.css
├── dataset/
│   └── dataset.xlsx            # Raw dataset
└── output/
    ├── processed_dataset.csv   # Cleaned data
    └── feature_dataset.csv     # Data with engineered features
```

## Tech Stack

- **Language**: Python, JavaScript
- **ML**: scikit-learn, pandas, NumPy
- **Backend**: Flask
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite

## How to Run

1. Clone the repository

   ```bash
   git clone https://github.com/vishvasuresh46/ai-smart-home-energy-optimizer.git
   cd ai-smart-home-energy-optimizer
   ```

2. Install the required libraries

   ```bash
   pip install flask pandas numpy scikit-learn openpyxl joblib
   ```

3. (Optional) Retrain the models

   ```bash
   cd backend
   python data_preprocessing.py
   python feature_engineering.py
   python train_energy_model.py
   python train_bill_model.py
   ```

4. Start the application

   ```bash
   cd backend
   python app.py
   ```

5. Open the frontend in your browser (or the local URL shown in the terminal).

## Workflow

1. Raw data (`dataset.xlsx`) is cleaned and preprocessed
2. Features are engineered from the cleaned data
3. Energy and bill prediction models are trained and saved as `.pkl` files
4. User enters details in the frontend
5. Backend predicts usage and bill, checks for anomalies, and returns optimization suggestions

## Author

**vishvasuresh46**
