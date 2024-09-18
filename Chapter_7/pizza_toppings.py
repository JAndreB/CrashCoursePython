prompt = "\nPlease enter the name of a topping you would like added to the pizza"
prompt += "\nEnter 'quit' to quit the program.\n"

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f'We are adding {topping.title()} to your Pizza!')