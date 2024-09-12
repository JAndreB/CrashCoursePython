my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('canolli')

friend_foods.append('ice cream')

print("My favourite foods are: ")
print(my_foods)

print("\nMy friends favourite foods are: ")
print(friend_foods)

print("\nmy favourite foods are: ")
for i in my_foods[:]:    
    print(i.title())

print("\nmy favourite friends foods are: ")
for i in friend_foods[:]:
    print(i.title())