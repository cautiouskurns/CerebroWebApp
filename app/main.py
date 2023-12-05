
from flask import Flask, request, render_template, redirect, url_for
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')

ALLOWED_EXTENSIONS = {'csv'}

# Global variable to store the data
uploaded_data = None

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file and allowed_file(file.filename):
        if file.filename == '':
            return redirect(request.url)
        if file and file.filename.endswith('.csv'):
            df = pd.read_csv(file, encoding='ISO-8859-1')
            return df.to_html(header="true", table_id="table")
        return redirect(request.url)

if __name__ == '__main__':
    app.run(port=5001)