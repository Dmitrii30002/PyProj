import re

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zа-яё\s]', '', text)
    return text.split()