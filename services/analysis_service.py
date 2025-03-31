from services.tfidf_service import TFIDFCalculator

class AnalysisService:
    def __init__(self):
        self.documents = []

    def analyze_text(self, text):
        self.documents.append(text)
        tf = TFIDFCalculator.compute_tf(text)
        idf = TFIDFCalculator.compute_idf(self.documents)
        
        words_data = [{
            'word': word,
            'tf': tf_val,
            'idf': idf.get(word, 0)
        } for word, tf_val in tf.items()]
        
        return sorted(words_data, key=lambda x: x['idf'], reverse=True)[:50]