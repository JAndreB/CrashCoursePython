prompt = "\nPlease enter your age:"
#prompt += "\nEnter 'quit' to quit the program.\n"

while True:
    age = int(input(prompt))

    if age >= 3 and age <= 12:
        ticket = 10
    elif age > 12:
        ticket = 15
    
    print(f'Your ticket is £{ticket}')