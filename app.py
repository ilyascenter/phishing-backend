from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "API jalan"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    return jsonify({"url": data.get("url")})

app.run()