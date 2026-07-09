
from main import app

# Homepage showing all files
@app.route('/', methods=['GET'])
def list_files():
    return None

# File upload route
@app.route('/upload', methods=['POST'])
def upload_file():
    return None

# Finds file and downloads it
@app.route('/download/<int:file_id>', methods=['GET'])
def download_file():
    return None