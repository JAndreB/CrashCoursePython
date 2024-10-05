

while True:
    try:
        num1 = int(input("Please provide a number: "))
        num2 = int(input("Please provide a second number: "))
    except ValueError:
        print('You cannot add a letter and a number')
    else:
        total = num1 + num2
        print(total)