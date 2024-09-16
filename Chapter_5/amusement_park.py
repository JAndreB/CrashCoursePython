age = 700
"""if age < 4:
    print('Your admissions is £4.')
elif age < 18:
    print("Your admission is £12.")
else:
    print('Your admission is £20.')"""

if age < 4:
    price = 0
elif age  < 18:
    price = 12
elif age  < 65:
    price = 40
elif age >= 65:
    price = 20
"""else:
    price = 20"""




print(f"Your admission price is £{price}")