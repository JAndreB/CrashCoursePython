"""requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, out of green peppers')
    else:
        print(f"Adding the {requested_topping}.")

print("\nFinished making pizza!")"""

"""requested_toppings = []

if requested_toppings:

    for requested_topping in requested_toppings:
        print(f"Adding the {requested_topping}.")
    print("\n Finished prepping pizza!")
else:
    print('\nDo you want a pizaa that is plain!')"""

available_toppings = ['mushrooms', 'olives', 'black peppers', 'pepperoni',\
                       'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'olives']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'\nAdding {requested_topping}!')
    else:
        print(f"\nSorry we don't have {requested_topping}!")
print('\nFinished making your pizza!')




    