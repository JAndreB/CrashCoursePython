number = int(input("Input a number and i will tell you if it is even or odd: \n"))

modded = number % 2

if modded == 0:
    print('\nAh, see, this number is even!')
else:
    print(f'\nAh, see, this number is odd! I know because the remainder is not\
 0, it is {modded}!')