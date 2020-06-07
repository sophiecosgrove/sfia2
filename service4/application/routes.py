from application import app
import requests


@app.route('/randomfortune', methods=['GET'])
def sentence():
    time = requests.get('http://service2:5001/randomtime')
    phrase = requests.get('http://service3:5002/randomphrase')
    response = time.text + " " + phrase.text
    return response