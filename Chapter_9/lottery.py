from random import choice

num = ['1','2', '3', '4', '5', '6', '7', '8', '9', '10']

let = ['a','b','c','d']

options = num + let

picks = []

while len(picks) < 5:
    pick = choice(options)
    picks.append(pick)

print(f"In order to win you must pick te following: {picks}")
