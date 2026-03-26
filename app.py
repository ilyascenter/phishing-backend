from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
from feature import extract_features
import os

app = Flask(__name__)
CORS(app)

# load model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model.pkl')
model = pickle.load(open(MODEL_PATH, 'rb'))

@app.route('/')
def home():
    return jsonify({"status": "API jalan"})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        url = data.get("url")

        if not url:
            return jsonify({"error": "URL kosong"}), 400

        features = extract_features(url)

        prediction = model.predict([features])[0]
        probability = model.predict_proba([features])[0]

        confidence = max(probability) * 100

        result = "Phishing" if prediction == 1 else "Legit"

        return jsonify({
            "url": url,
            "prediction": result,
            "confidence": round(confidence, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)