from flask import Flask, flash, render_template, redirect, request, url_for
from werkzeug.utils import secure_filename
import os
from pathlib import Path
import sqlite3

def get_db():
    db = sqlite3.connect('db.sqlite3')
    db.row_factory = sqlite3.Row
    return db

def create_db():
    db = get_db()
    db.execute('CREATE TABLE post (title TEXT NOT NULL, body TEXT, image TEXT, document TEXT)')
    db.close()

if not os.path.isfile('db.sqlite3'):
    create_db()

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png', 'docx', 'xlsx', 'pdf', 'doc', 'xls', 'ppt', 'pptx'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

UPLOAD_FOLDER = 'static/uploads'
path = Path(UPLOAD_FOLDER)
path.parent.mkdir(parents=True, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/posts')
def read_all():
    db = get_db()
    posts = db.execute('SELECT rowid, * FROM post').fetchall()
    db.close()
    return render_template('read-all.html', posts=posts)

@app.route('/')
def index():
    return redirect(url_for('read_all'))

@app.route('/posts/create', methods=['post', 'get'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    
    title = request.form['title']
    body = request.form['body']
    if title == '':
        return render_template('400.html', reasons=['Title is not present.']), 400
    
    image = request.files['image'] if 'image' in request.files else None
    if image and allowed_file(image.filename):
        image_filename = secure_filename(image.filename)
        image_filename = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
        image.save(image_filename)
    else:
        image_filename = None

    document = request.files['document'] if 'document' in request.files else None
    if document and allowed_file(document.filename):
        doc_filename = secure_filename(document.filename)
        doc_filename = os.path.join(app.config['UPLOAD_FOLDER'], doc_filename)
        document.save(doc_filename)
    else:
        doc_filename = None

    db = get_db()
    with db:
        db.execute('INSERT INTO post(title, body, image, document) VALUES (?,?,?,?)',
                (title, body, image_filename, doc_filename))
    db.close()

    return redirect(url_for('index'))

@app.route('/posts/<id>')
def read_single(id):
    db = get_db()
    post = db.execute('SELECT * from post WHERE rowid=?', (id)).fetchone()
    db.close()
    return render_template('read-single.html', post=post)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

app.run(debug=True)
