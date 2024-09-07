my_foods = ['pizza', 'falafel', 'carrot cake']
friend_food = my_foods[:]

my_foods.append('cannoli')
friend_food.append('ice cream')

print("My favorite foods are:")
for foods in my_foods:
    print(foods.title())

print("\nMy friend's favorite foods are:")
for foods in friend_food:
    print(foods.title())