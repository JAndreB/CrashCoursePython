age = int((input('\nHow old are you?')))

if age < 2:
    print('\nYou are a baby!')
elif age >= 2 and age < 4:
    print('\nYou are a toddler!')
elif age >= 4 and age < 13:
    print('\nYou are a  kid!')
elif age >=13 and age < 20:
    print('\nYou are a teenager!')
elif age >= 20 and age < 65:
    print('\nYou are an adult!')
elif age >= 65:
    print('\nYou are dying soon!')

