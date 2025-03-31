import math
from collections import Counter
from utils.text_processing import preprocess_text

class TFIDFCalculator:
    @staticmethod
    def compute_tf(text):
        words = preprocess_text(text)
        word_counts = Counter(words)
        total_words = len(words)
        return {word: count/total_words for word, count in word_counts.items()}

    @staticmethod
    def compute_idf(documents):
        N = len(documents)
        idf = {}
        all_words = set()
        
        for doc in documents:
            words = set(preprocess_text(doc))
            all_words.update(words)
        
        for word in all_words:
            count = sum(1 for doc in documents if word in preprocess_text(doc))
            idf[word] = math.log(N / (count + 1))
        
        return idf