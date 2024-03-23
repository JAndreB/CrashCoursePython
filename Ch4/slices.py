players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("the first 3 players in my team are:")
for player in players[:3]:
    print(player.title())

print("Here are the middle three players on my team:")
for player in players[1:-1]:
    print(player.title())

print("Here are the last three players on my team:")
for player in players[2:]:
    print(player.title())
