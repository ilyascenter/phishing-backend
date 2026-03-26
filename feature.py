import re
from urllib.parse import urlparse

SUSPICIOUS_KEYWORDS = [
    "login", "secure", "verify", "update", "bank",
    "confirm", "account", "password", "free", "bonus"
]

FREE_TLD = ["tk", "ml", "ga", "cf"]

def extract_features(url):
    parsed = urlparse(url)
    domain = parsed.netloc.lower()
    path = parsed.path.lower()

    features = []

    # BASIC
    features.append(len(url))
    features.append(url.count('.'))
    features.append(url.count('/'))

    # HTTPS
    features.append(1 if url.startswith("https") else 0)

    # DOMAIN
    features.append(len(domain))
    features.append(1 if '-' in domain else 0)
    features.append(sum(c.isdigit() for c in domain))

    # IP
    features.append(1 if re.match(r'^\d+\.\d+\.\d+\.\d+', domain) else 0)

    # TLD
    tld = domain.split('.')[-1] if '.' in domain else ''
    features.append(1 if tld in FREE_TLD else 0)

    # KEYWORDS
    keyword_count = sum(1 for k in SUSPICIOUS_KEYWORDS if k in url.lower())
    features.append(keyword_count)

    # SPECIAL CHAR
    features.append(1 if '@' in url else 0)
    features.append(1 if '%' in url else 0)

    # DOUBLE SLASH
    features.append(1 if '//' in path else 0)

    # PANJANG URL
    features.append(1 if len(url) > 100 else 0)

    return features