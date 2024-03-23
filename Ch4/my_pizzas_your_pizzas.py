my_pizza = ['pepperoni', 'double Chese', 'american']
friends_pizza = my_pizza[:]

my_pizza.append('mushroom')
friends_pizza.append('pineapple')

print('My favourite pizzas are:')
for value in my_pizza:
    print(f"{value.title()}")

print('\nYour favourite pizzas are:')
for value in friends_pizza:
    print(f"{value.title()}")

#for i in Pizza:
#    print(f"I'm a big fan of {i.title()} Pizza.\n")
#
#print("In fact, i like ALL Pizza")