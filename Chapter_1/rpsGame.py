import random, sys

print('ROCK, PAPER, SCISSORS')

# These variable skeep track of the number of wins losses and ties

wins = 0
losses = 0
ties = 0

while True: #This is the main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # THe player input loop.
        print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop
        print('Type one of r, p, s or q.')
    # Display what the player chose:
    if playerMove == 'r':
        print('ROCK vs...')
    elif playerMove == 'p':
        print('PAPER vs...')
    elif playerMove == 's':
        print('SCISSORS vs...')

    #Display want the computer chose:
    randomNumber = random.randint(1, 4)
    if randomNumber == 1:
        computermove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computermove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computermove = 's'
        print('SCISSORS')

    #Display and record win/loss/tie:
    if playerMove == computermove:
        print('It is  a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computermove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computermove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computermove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computermove == 'p':
        print('You lose')
        losses = losses + 1
    elif playerMove == 'p' and computermove == 's':
        print('You lose')
        losses = losses + 1
    elif playerMove == 's' and computermove == 'r':
        print('You lose')
        losses = losses + 1