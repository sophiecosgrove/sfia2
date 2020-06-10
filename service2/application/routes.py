from application import app
import random 


@app.route('/randomtime', methods=['GET'])
def time():

    number = random.randint(1,2)
    if number == 1:
        time = ['Next week','Tomorrow','Next weekend','In the next few days','This weekend', 'This month', 'The day after tomorrow',
        'This tuesday', 'This friday', 'This saturday', 'This sunday', 'Next friday']
    elif number == 2:
        time = ['Next month', 'In the next few months', 'Next year', 'In the next 3 years', 'This summer', 'This winter',
        'This autumn', 'This spring', 'Next summer', 'Next winter', 'Next autumn', 'Next spring']
    return time[random.randrange(12)]
