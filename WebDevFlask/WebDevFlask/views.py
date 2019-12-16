"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, flash, request, redirect, url_for, make_response, render_template
from WebDevFlask import app



@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )



@app.route('/LoginRegister')
def LoginRegister():
    """Renders the about page."""
    return render_template(
        'LoginRegister.html',
        title='LoginRegister',
        year=datetime.now().year,
        message='Your application description page.'
    )





@app.route('/processfile')
def upload_file():
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''



@app.route('/uploadfile')
def form():
    return render_template('upload_file.html')

@app.route('/read', methods=["POST"])
def transform_view():
    request_file = request.files['data_file']
    if not request_file:
        return "No file"
    found_keywords = []
    file_contents = request_file.read()
    list_of_words = file_contents.split()
    keywords = ['Pedro','book','nice']
    found_keywords = [e for e in keywords if e in '\n'.join(list_of_words)]
    a = found_keywords
    return render_template('read_file.html', filetext = file_contents, found_keys = a)
     
   
