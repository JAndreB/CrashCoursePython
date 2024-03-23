""" requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!") """

requested_toppings = ['mushrooms', 'green peppers',  'extra cheese']

""" for requested_topping in requested_toppings:
    if requested_topping =='green peppers':
        print("\nSorry, we are out of green peppers right now!")
    else:
        print(f"\nAdding {requested_topping}")

print("\nFinished making you pizza!") """

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"\nAdding {requested_topping}")
    print("\nFinished making you pizza!")

else:
    print("\nAre you sure you want a plain pizza?")
        

