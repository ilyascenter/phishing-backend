def extract_features(url):
    return [
        len(url),
        url.count('.'),
        1 if 'https' in url else 0,
        1 if '@' in url else 0,
        1 if '-' in url else 0,
        url.count('/'),
    ]