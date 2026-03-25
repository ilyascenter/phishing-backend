# Phishing URL Detection API

Machine Learning-based phishing URL detection system using Flask.

## Features
- URL classification (Phishing / Safe)
- REST API endpoint
- Deployed on Render

## Tech Stack
- Python
- Flask
- Scikit-learn
- Machine Learning (Random Forest)

## API Endpoint

POST /predict

### Request:
```json
{
  "url": "example.com"
}