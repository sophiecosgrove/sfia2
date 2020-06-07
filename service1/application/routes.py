from application import app, db
from flask import render_template, request, jsonify, Response
from application.models import Fortunes
import requests
import os

@app.route('/', methods=['GET', 'POST'])
def home():
    response = requests.get('http://service4:5003/randomfortune')
    sentence = response.text
    fortuneData = Fortunes(
        fortune = sentence
        )
    db.session.add(fortuneData)
    db.session.commit()

    return render_template('home.html', sentence = sentence, title = 'Home')

@app.route('/fortunes', methods=['GET'])
def fortunes():
    fortuneData = Fortunes.query.all()
    return render_template('fortunes.html', fortunes = fortuneData)

