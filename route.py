from __main__ import app, BASE_DIR, UPLOAD_DIR
from flask import abort, redirect, render_template, request, send_from_directory, url_for, session
from db import insert_file, get_files, get_file_by_id, delete_file
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from functools import wraps
import logging
import os

# Configure logging
logging.basicConfig(
    filename='activity.log',
    level=logging.INFO,
    format='%(asctime)s %(message)s'
)

# Login check wrapper
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('authenticated'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# File list route
@app.route('/', methods=['GET'])
@login_required
def list_files():
    files = get_files()
    return render_template('file_list.html', files=files)

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        submitted_password = request.form.get('password')
        stored_hash = os.getenv('PASSWORD')
        if check_password_hash(stored_hash, submitted_password):
            session['authenticated'] = True
            logging.info(f"| IP={request.remote_addr} | Login Success")
            return redirect(url_for('list_files'))
        else:
            logging.info(f"| IP={request.remote_addr} | Login Failure")
            return render_template('login.html', error=True)
    return render_template('login.html')

# File upload route
@app.route('/upload', methods=['POST'])
@login_required
def upload_file():
    sanitized_name = secure_filename(request.files['file'].filename)
    upload_path = os.path.join(UPLOAD_DIR, sanitized_name)
    request.files['file'].save(upload_path)  # Save the file
    insert_file(sanitized_name, os.path.getsize(upload_path)) # Inserts into DB
    logging.info(f"| IP={request.remote_addr} | Upload | {sanitized_name}")
    return redirect(url_for('list_files'))  # Redirect to the list of files

# File download Route
@app.route('/download/<int:file_id>', methods=['GET'])
@login_required
def download_file(file_id):
    file_record = get_file_by_id(file_id)
    if file_record is None:
        abort(404)
    logging.info(f"| IP={request.remote_addr} | Download | {file_record['filename']}")
    return send_from_directory(UPLOAD_DIR, file_record["filename"], as_attachment=True)

# File deletion route
@app.route('/delete/<int:file_id>', methods=['POST'])
@login_required
def purge_file(file_id):
    file_record = get_file_by_id(file_id)
    if file_record is None:
        abort(404)
    os.remove(os.path.join(UPLOAD_DIR, file_record["filename"]))
    delete_file(file_id)
    logging.info(f"| IP={request.remote_addr} | Delete | {file_record['filename']}")
    return redirect(url_for('list_files'))



