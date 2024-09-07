# list of elements in list 'bicycle'
bicycles = ['trek', 'dumb', 'goose', 'lucky']
#print the list 'bicycles'
print(bicycles)
#print the 3rd element in 'bicycles'
print(bicycles[2])
#print and element from bicycles with the string element 'title()' attached
print(bicycles[3].title())

#Places in an element start at 0, not one
print(bicycles[0])
print(bicycles[1])

#Reversse indexes are alo an option and start at minues one
print(bicycles[-1])

#Youi can also use values in a list to compose formatted messages
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)