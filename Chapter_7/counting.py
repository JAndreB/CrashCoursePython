current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue #tells python to return to the top of the loop instead of continuing
    #in this case it is telling python to skip even numbers
    print(current_number)

x = 1
while x <= 5:
    print(x)
    x += 1

# open loop, while x is one it does nothing with the number and just prints it:
x = 1
while x <= 5:
    print(x)