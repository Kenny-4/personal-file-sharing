
from flask import abort, redirect, render_template, request, send_from_directory, url_for
from werkzeug.utils import secure_filename
from main import app
from db import insert_file, get_files, get_file_by_id, delete_file
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, 'uploads')

# Homepage showing all files
@app.route('/', methods=['GET'])
def list_files():
    files = get_files()
    return render_template('file_list.html', files=files)


# File upload route
@app.route('/upload', methods=['POST'])
def upload_file():
    sanitized_name = secure_filename(request.files['file'].filename)
    upload_path = os.path.join(UPLOAD_DIR, sanitized_name)
    request.files['file'].save(upload_path)  # Save the file
    insert_file(sanitized_name, os.path.getsize(upload_path)) # Inserts into DB
    return redirect(url_for('list_files'))  # Redirect to the list of files

# File download Route
@app.route('/download/<int:file_id>', methods=['GET'])
def download_file(file_id):
    file_record = get_file_by_id(file_id)
    if file_record is None:
        abort(404)
    return send_from_directory(UPLOAD_DIR, file_record["filename"], as_attachment=True)

# File deletion route
@app.route('/delete/<int:file_id>', methods=['POST'])
def purge_file(file_id):
    file_record = get_file_by_id(file_id)
    if file_record is None:
        abort(404)
    os.remove(os.path.join(UPLOAD_DIR, file_record["filename"]))
    delete_file(file_id)
    return redirect(url_for('list_files'))


