pizza = ['cheesy', 'meat feast', 'pineapple']

for i in pizza:
    print(i.title())
    print(f"I really like {i.title()} pizza!\n")

print('I really like pizza!')

friends_pizza = pizza[:]

pizza.append("macaroni")

friends_pizza.append("chocolate")

print(pizza)
print(friends_pizza)