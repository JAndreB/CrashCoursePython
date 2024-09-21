###def make_pizza(*toppings):
###    """print an arbitraty number oif prarams to represent any number of toppings"""
###    print(toppings)
###
###make_pizza('pepperoni')
###make_pizza('mushrooms', 'green_peppers')###

def make_pizza(*toppings):
    """Summarize the pizza we are about to make"""
    print("\n Making a pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green_peppers') 
