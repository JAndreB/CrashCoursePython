"""try:
    print(5/0)
except ZeroDivisionError:
    print("You cannot divide by zero!")"""

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond Number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('You can not divide by 0!')
    else:
        print(answer)
