from application import app
import random


@app.route('/randomphrase', methods=['GET'])
def phrase():

	list = ['you will meet your soul mate','you will recieve great news','you will travel to Europe','you will recieve bad news','a door will close and another one will open','your prayers will be answered','a person from your past will return']
	
	return list[random.randrange(6)]