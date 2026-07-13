from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, 'uploads')

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
import route

if __name__ == '__main__':
    app.run(debug=True, host = '127.0.0.1', port=5000)