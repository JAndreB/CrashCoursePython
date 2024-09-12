players = ['charles', 'Louis', 'Jolke', 'Paradan', 'Johnny']
print(players[0:3])

print(players[1:4])

print(players[:4])

print(players[2:])

print(players[-3:])

print(("Here are the first 3 players on my team:"))
for player in players:
    print(player.title())