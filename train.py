import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
from feature import extract_features

data = {
    "url": [
        # LEGIT
        "https://google.com",
        "https://facebook.com",
        "https://github.com",
        "https://tokopedia.com",
        "https://bankmandiri.co.id",

        # PHISHING
        "http://secure-login-paypal.com",
        "http://verify-account-bank.xyz",
        "http://free-money-now.click",
        "http://login-facebook-security.com",
        "http://update-account-verify.net",
        "http://192.168.1.1/login",
        "http://paypal-secure-login123.com",
    ],
    "label": [
        0,0,0,0,0,
        1,1,1,1,1,1,1
    ]
}

df = pd.DataFrame(data)

X, y = [], []

for url, label in zip(df['url'], df['label']):
    X.append(extract_features(url))
    y.append(label)

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X, y)

pickle.dump(model, open('model.pkl', 'wb'))

print("🔥 Model berhasil di-upgrade!")