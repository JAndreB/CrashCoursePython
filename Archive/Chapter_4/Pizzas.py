pizzas = ['pepperoni', 'meat feast', 'spicy', 'cheesy']
'''for pizza in pizzas:
    print(f'I love {pizza.title()} pizza!')
print('\nAs you can see, i really like Pizza!')'''

friends_pizzas = pizzas[:]
print(friends_pizzas)

pizzas.append('pineapple')
print(pizzas)

friends_pizzas.append('chocolate')
print(friends_pizzas)

print('\nMy favourite pizzas are:')
for pizza in pizzas:
    print(pizza.title())

print('\nMy friends favourite pizzas are: ')
for pizza in friends_pizzas:
    print(pizza.title())