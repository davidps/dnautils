from flask import render_template, request, session
from app import app
import os
import uuid
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'txt'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
@app.route('/index')
def index():
    session['user'] = str(uuid.uuid4())
    print( session)
    return render_template('index.html', nofile=True)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    print('uploading..')
    if request.method == 'POST':
        f = request.files.get('file')
        os.makedirs(os.path.join(app.instance_path, session['user']), exist_ok=True)
        f.save(os.path.join(app.instance_path, session['user'], secure_filename(f.filename)))
        print('file saved to ' + os.path.join(app.instance_path, session['user'], secure_filename(f.filename)))
        nofile = False
    
    return render_template('loading.html')
