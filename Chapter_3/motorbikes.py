"""motorbikes = ['honda', 'yamaha', 'suzuki']
print(motorbikes)

motorbikes[0] = 'ducati'
print(motorbikes)

motorbikes.append('ducati')
print(motorbikes)"""

motorbikes = []

motorbikes.append('worse')
motorbikes.append('nodens')
motorbikes.append('ritual')

print(motorbikes)

"""motorbikes.insert(0, 'lunch')
print(motorbikes)

del motorbikes[0]
print(motorbikes)

del motorbikes[1]
print(motorbikes)"""

"""popped_motorbike = motorbikes.pop()
print(motorbikes)
print(popped_motorbike)

print(f"The last motorbike i owned was a {popped_motorbike.title()}.")

first_owned = motorbikes.pop(0)
print(f"The first motorbike i owned was a {first_owned.title()}.")

print(motorbikes)"""

"""motorbikes.remove('worse')
print(motorbikes)"""

too_expensive = 'worse'
motorbikes.remove(too_expensive)
print(motorbikes)
print(f"\nA {too_expensive.title()} is to expensive for me.")