# For the segment'modifying elements in a list' onwards
games = ['cyberpunk 2077', 'elden ring', 'deus ex']
print(games)

#replacing an element in the list
games[0] = 'forza'

print(games)

# adding an elemnt to the list
games.append('PES 2014')
print(games)

#clearing the list
games = []
print(games)

#Adding more elements
games.append('snake')
games.append('metal gear solid')
games.append('splinter cell')
print(games)

#insert elements into lists
games.insert(1, 'CTR')
print(games)

#deleting an element from a list
del games [0]
print(games)

#deleting from a specific index
del games [2]
print(games)

games = ['cyberpunk 2077', 'elden ring', 'deus ex']
games.append('snake')
games.append('metal gear solid')
games.append('splinter cell')
print(games)

#using the pop() method to pop the last element from the list
games_popped = games.pop()
print(games_popped)
print(games)

# using pop() to generate a formatted sentence
last_brought = games.pop()
print(f"The last game i brought was {last_brought.title()}.")

#A loop that removes the last value from the list and adds it to the end of the sentence 'the next item from the beginning of
# the list is betther than the value in pop(), the loop moves from the beginning of the list and the .pop() method' cuts it do
#n from the end., shortening the list from both sides
games = ['cyberpunk 2077', 'elden ring', 'deus ex']
games.append('snake')
games.append('metal gear solid')
games.append('splinter cell')
print(games)

for i in games:
    print(f'{i} is better than {games.pop()}')

print(games)

#remove item from a list via its name
games = ['cyberpunk 2077', 'elden ring', 'deus ex']
games.append('snake')
games.append('metal gear solid')
games.append('splinter cell')
print(games)

games.remove('deus ex')
print(games)

#using remove() wuith a variable to generate a formatted sentence
games = ['cyberpunk 2077', 'elden ring', 'deus ex']
games.append('snake')
games.append('metal gear solid')
games.append('splinter cell')
print(games)

too_Expensive = 'elden ring'
games.remove(too_Expensive)
print(f'\n{too_Expensive} is too expensive, so I a removing it from my list')
print(games)