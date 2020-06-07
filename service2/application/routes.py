from application import app
import random 


@app.route('/randomtime', methods=['GET'])
def time():

	list = ['Next week','Next month','Tomorrow','Next weekend','In the next few days','Next year','This weekend']
	
	return list[random.randrange(6)]