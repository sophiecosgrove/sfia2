from application import app
from flask import render_template, request

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', sentence = "Sample Text", title = 'Home')
