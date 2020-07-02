from application import app
import requests


@app.route('/randomfortune', methods=['GET'])
def sentence():
    time = requests.get('http://localhost:5001/randomtime')
    phrase = requests.get('http://localhost:5002/randomphrase')
    response = time.text + " " + phrase.text
    return response