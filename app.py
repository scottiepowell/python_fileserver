import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template, flash
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

load_dotenv()

# Set the folder where uploaded files will be stored
UPLOAD_FOLDER = 'UPLOAD_FOLDER'
# Set the allowed file extensions for uploads
# For Windows use this syntax UPLOAD_FOLDER = 'C:\\Users\\YourUsername\\upload_folder' 
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','md','py'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    # Check if there's a period ('.') in the filename, indicating the presence of a file extension
    # and verify that the extension is in the list of ALLOWED_EXTENSIONS
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# route and function for the index page
@app.route('/')
def index():
    return render_template('index.html')

# Route decorator for the '/upload' endpoint, accepting GET and POST requests
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    <a href="{{ url_for('index') }}">Back to Home</a>
    '''

# New route and function for downloading files
@app.route('/download', methods=['GET', 'POST'])
def download_file():
    # Check if the request method is POST
    if request.method == 'POST':
        # Get the selected filename from the form
        filename = request.form['filename']
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

    # If the request method is GET, display the download form with a list of files
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('download.html', files=files)

# Run the Flask application
if __name__ == '__main__':
    host = os.environ.get('FLASK_HOST', 'localhost')
    port = int(os.environ.get('FLASK_PORT', 5000))
    app.run(host=host, port=port)


# To use this file server on a Windows 10 system:
# 1. Save this code to a file with a .py extension, e.g. file_server.py
# 2. Install Flask by running 'pip install flask' in a command prompt or terminal
# 3. Run the file server by navigating to its directory in a command prompt or terminal and running 'python file_server.py'
# 4. Clients can access the file server by navigating to http://localhost:5000/upload to upload a file, or http://localhost:5000/download/filename to download a file

# To use this file server on an Ubuntu system:
# 1. Save this code to a file with a .py extension, e.g. file_server.py
# 2. Install Flask by running 'sudo apt-get install python3-flask' in a terminal
# 3. Run the file server by navigating to its directory in a terminal and running 'python3 file_server.py'
# 4. Clients can access the file server by navigating to http://localhost:5000/upload to upload a file, or http://localhost:5000/download/filename to download a file
