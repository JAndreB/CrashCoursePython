""" Program to demonstrat basic lottery number generator
Pick numbers using the random module, then pick my own set of numbers, and
repeatedly pick numbers in my card until they match!"""

#Import Random
from random import choice

#Esablish the options to pick on the lottery card
num = ['1','2', '3', '4', '5', '6', '7', '8', '9', '10']

let = ['a','b','c','d']

options = num + let

#Initialize the 3 variables, picks represents the lottery numbers, my picks\
#represents my lottery cards and no of try represents the number of tries
#i have made, initialized at 0
picks = []

my_picks = []

No_of_trys = 0

# This while loop checks if the length of picks is less than 5, and if so
#uses pick to pick a random number from options. If that number is in picks,
#it does not add it, if it isn't it does, this way our lottery numbers have
#no repeats as a time  constraint.
while len(picks) < 5:
    pick = choice(options)
    if pick in picks:
        continue
    else:
        picks.append(pick)

#Just confirming what the numbers are
print(f"In order to win you must pick the following: {picks}")

#My logic with the below is to build my lotto card and then check if it
#matches, if it doesn't then my picks list has to be empty by the end of the loop
#because if it isn't then the original while check will pass and then the  
#second while check will fail due to already having 5 numbers,
# skipping building my picks again. Meaning the loop will be inifinite.
# I have updated this so that at some point the first while check will fail
# and the last statement wil lbe printed. The last statement used to be an
#else statement

# Loop to initially check if my lottery card matches lotto numbers, if not
while my_picks != picks:
    #secondary loop to add numbers to my lottery card until we have 5
    while len(my_picks) < 5:
        #randomly pick a number
        my_pick = choice(options)
        # check to see if number has already been chosen, if yes ignore, if no
        #add to list
        if my_pick in my_picks:
            continue
        else:
            my_picks.append(my_pick)
    # compare lotto numbers to my list, if the do not match:
    if my_picks != picks:
        #add one to list of trys
        No_of_trys += 1
        #empty my lotto card to start again
        my_picks = []
    #if my lottory card and lotto numbers do match, print the result

print(f'\nCongrats, you won the lottery!, and it only took {No_of_trys} times!')





    






