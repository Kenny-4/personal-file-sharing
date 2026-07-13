import flask
import os
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, 'uploads')

app = flask.Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

app.run(debug=True)