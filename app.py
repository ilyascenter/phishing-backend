from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import time
from feature import extract_features

app = Flask(__name__)
CORS(app)

model = pickle.load(open("model.pkl", "rb"))

# RATE LIMIT
request_log = {}
LIMIT_SECONDS = 2

@app.route('/')
def home():
    return jsonify({"status": "API jalan"})

@app.route('/predict', methods=['POST'])
def predict():

    # RATE LIMIT
    ip = request.remote_addr
    now = time.time()

    if ip in request_log:
        if now - request_log[ip] < LIMIT_SECONDS:
            return jsonify({"error": "Terlalu banyak request"}), 429

    request_log[ip] = now

    data = request.get_json()
    url = data.get("url")

    features = extract_features(url)

    proba = model.predict_proba([features])[0]
    phishing_score = proba[1]

    # PREDICTION
    if phishing_score > 0.7:
        prediction = "Phishing"
    elif phishing_score > 0.4:
        prediction = "Suspicious"
    else:
        prediction = "Legit"

    confidence = round(phishing_score * 100, 2)

    # EXPLANATION
    reasons = []

    if "login" in url.lower():
        reasons.append("Mengandung kata 'login'")

    if "secure" in url.lower():
        reasons.append("Mengandung kata 'secure'")

    if "verify" in url.lower():
        reasons.append("Mengandung kata 'verify'")

    if "@" in url:
        reasons.append("Mengandung simbol @")

    if "-" in url:
        reasons.append("Mengandung dash (-)")

    if len(url) > 100:
        reasons.append("URL terlalu panjang")

    return jsonify({
        "url": url,
        "prediction": prediction,
        "confidence": confidence,
        "reasons": reasons
    })

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)