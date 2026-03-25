import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
from feature import extract_features

# dataset sederhana
data = {
    "url": [
        "google.com",
        "facebook.com",
        "secure-paypal-login.com",
        "bank-login-alert.xyz",
        "github.com",
        "free-money-now.click"
    ],
    "label": [0, 0, 1, 1, 0, 1]
}

df = pd.DataFrame(data)

X, y = [], []

for i in range(len(df)):
    X.append(extract_features(df['url'][i]))
    y.append(df['label'][i])

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open('model.pkl', 'wb'))

print("Model berhasil dibuat!")