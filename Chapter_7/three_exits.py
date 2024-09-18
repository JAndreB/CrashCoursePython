prompt = "\nPlease enter the name of a topping you would like added to the pizza"
prompt += "\nEnter 'quit' to quit the program.\n"

toppings = []
no_of_toppings = 0
toppings_full = False   

while toppings_full == False:
    if no_of_toppings == 3:
        print('Max 3 toppings!')
        toppings_full = True
    else:
        topping = input(prompt)

        if topping == 'quit':
            break
        elif no_of_toppings < 4:
            print(f'We are adding {topping} now!')
            toppings.append(topping)
            no_of_toppings += 1
        
print(f'\nWe are adding the following toppings: ')
for top in toppings:
    print(top.title())

note = input("Type 'toppings' if you need to see the toppings again: ")

if note == 'toppings':
    print(toppings)






    


    