import random

def getAnswer(answeerNumber):
    if answeerNumber == 1:
        return 'It is certain'
    elif answeerNumber == 2:
        return 'It is decidedly so'
    elif answeerNumber == 3:
        return 'Yes'
    elif answeerNumber == 4:
        return 'Hazy, try again'
    elif answeerNumber == 5:
        return 'Ask again later'
    elif answeerNumber == 6:
        return 'Concentrate and try again'
    elif answeerNumber == 7:
        return ' My reply is no'
    elif answeerNumber == 8:
        return 'Outlook not so good'
    elif answeerNumber == 9:
        return 'Very doubtful'
    
'''r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)'''

print(getAnswer(random.randint(1, 9)))