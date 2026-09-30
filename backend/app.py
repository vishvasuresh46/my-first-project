from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# DB INIT
def init_db():
    conn = sqlite3.connect("energy.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperature REAL,
            appliances REAL,
            usage REAL,
            occupancy REAL,
            energy REAL,
            bill REAL
        )
    """)

    conn.commit()
    conn.close()

init_db()

# 🔥 PREDICT
@app.route('/predict_energy', methods=['POST'])
def predict_energy():
    data = request.json

    temp = float(data['temperature'])
    usage = float(data['usage_hours'])
    occupancy = float(data['occupancy'])

    lights = float(data['lights'])
    fans = float(data['fans'])
    ac = float(data['ac'])
    tv = float(data['tv'])
    fridge = float(data['fridge'])

    appliances = lights + fans + ac + tv + fridge

    energy = (temp*0.5) + (appliances*2) + (usage*1.5) + occupancy
    bill = energy * 5

    conn = sqlite3.connect("energy.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO history (temperature, appliances, usage, occupancy, energy, bill)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (temp, appliances, usage, occupancy, energy, bill))

    conn.commit()
    conn.close()

    return jsonify({
        "prediction": round(energy,2),
        "bill": round(bill,2)
    })

# 📊 HISTORY
@app.route('/history', methods=['GET'])
def history():
    conn = sqlite3.connect("energy.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history")
    rows = cursor.fetchall()
    conn.close()
    return jsonify({"history": rows})

# =========================
# 🔥 ADD THESE FEATURES APIs
# =========================

# 🔧 FAULT DETECTION
@app.route('/fault')
def fault():
    return jsonify({
        "fault": "✅ Appliances working fine"
    })

# ⚡ OPTIMIZATION
@app.route('/optimize')
def optimize():
    return jsonify({
        "tips": "💡 Use appliances in off-peak hours"
    })

# 📊 USER BEHAVIOR
@app.route('/behavior')
def behavior():
    return jsonify({
        "behavior": "📊 Evening usage is high"
    })

# 🚗 EV SUGGESTION
@app.route('/ev')
def ev():
    return jsonify({
        "ev": "🚗 Charge EV at night"
    })

# 🚨 ANOMALY DETECTION
@app.route('/anomaly', methods=['POST'])
def anomaly():
    data = request.json
    usage = float(data['usage'])

    if usage > 20:
        return jsonify({
            "status": "⚠ High energy usage detected"
        })
    else:
        return jsonify({
            "status": "✅ Normal usage"
        })

# =========================

# RUN
if __name__ == '__main__':
    app.run(debug=True)