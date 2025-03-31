from flask import Flask, render_template, request, redirect, url_for
from config import Config
from utils.file_handlers import save_uploaded_file
from services.analysis_service import AnalysisService

app = Flask(__name__)
app.config.from_object(Config)
Config.init_app(app)

analysis_service = AnalysisService()

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        
        filepath = save_uploaded_file(file)
        if filepath:
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()
            
            top_words = analysis_service.analyze_text(text)
            return render_template('results.html', words=top_words)
    
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)