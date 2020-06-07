from application import app
from flask import render_template, request, jsonify, Response
import requests
import random
import os

@app.route('/', methods=['GET'])
def home():
    response = requests.get('http://service4:5003/randomfortune')
    sentence = response.text
    return render_template('home.html', sentence = sentence, title = 'Home')

