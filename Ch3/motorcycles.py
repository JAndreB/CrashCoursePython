motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

#motorcycles[0] = "ducati"
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducati')
print(motorcycles)

#motorcycles.insert(0, 'ducati')
#print(motorcycles)

#del motorcycles[0]
#print(motorcycles)

#del motorcycles[1]
#print(motorcycles)

#popped_motorcycles = motorcycles.pop()
#print(motorcycles)
#print(popped_motorcycles)

#motorcycles.remove('honda')
#print (motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")