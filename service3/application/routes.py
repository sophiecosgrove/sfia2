from application import app
import random


@app.route('/randomphrase', methods=['GET'])
def phrase():
    number = random.randint(0,2)
    if number == 1 or number == 0:
        fortune = ['you will meet your soul mate','a close friend will turn into a lover', 'an important person will step into your life'
        , 'you will gain a lifelong friend', 'a long-lost relative will return', 'a long-lost friend will return',
        'you will recieve great news','you will travel to Europe','a door will close and another one will open', 'your prayers will be answered']
        return fortune[random.randrange(10)]
    elif number ==2:
        fortune = ['you will recieve bad news','you will face your worst fear', 'you will face great uncertainty',
        'an unwelcome change will occur', 'you will encounter your biggest challenge yet']
        return fortune[random.randrange(5)]
