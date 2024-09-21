def make_pizza(size, *toppings):
    """Summarize the size and pizza we are about to make"""
    print(f"Making a {size}' pizza with the following toppings: ")
    for each in toppings:
        print(f' - {each}')

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green_peppers') 