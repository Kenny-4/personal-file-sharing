from flask import Flask
import os
from dotenv import load_dotenv
from db import init_db
load_dotenv()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, 'uploads')

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
import route


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000, ssl_context='adhoc')
    #  127.0.0.1 for localhost
    #  0.0.0.0 for LAN
    #  ssl_context='adhoc' for self-signed certificates (https)