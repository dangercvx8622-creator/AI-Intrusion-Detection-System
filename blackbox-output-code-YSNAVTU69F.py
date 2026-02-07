from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import numpy as np
from scapy.all import sniff  # For real-time capture
import threading
import time

app = Flask(__name__)

# Load models
rf_model = joblib.load('models/rf_model.pkl')
iso_model = joblib.load('models/iso_model.pkl')
scaler = joblib.load('models/scaler.pkl')

# Global variables for real-time data
alerts = []
traffic_data = []

def real_time_capture():
    def packet_callback(packet):
        if packet.haslayer('TCP'):
            # Extract features (simplified; expand to match your feature set)
            features = [packet.time, len(packet), 1, 0]  # Placeholder: duration, bytes, etc.
            features_scaled = scaler.transform([features])
            rf_pred = rf_model.predict(features_scaled)[0]
            iso_pred = iso_model.predict(features_scaled)[0]
            if rf_pred == 1 or iso_pred == -1:
                alerts.append(f"Attack detected at {time.time()}: {packet.summary()}")
    sniff(prn=packet_callback, store=0, timeout=60)  # Capture for 60s, repeat in a loop

@app.route('/')
def index():
    return render_template('index.html', alerts=alerts, traffic=traffic_data)

@app.route('/analyze', methods=['POST'])
def analyze():
    # Simulate analysis of uploaded PCAP or live data
    # For demo, return mock results
    return jsonify({
        'accuracy': 0.96,
        'f1_score': 0.94,
        'alerts': alerts[-5:]  # Last 5 alerts
    })

if __name__ == '__main__':
    threading.Thread(target=real_time_capture, daemon=True).start()
    app.run(debug=True)