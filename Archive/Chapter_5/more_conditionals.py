posthuman = 'Vertigo'

print("Is Vertigo a posthuman? I predict the answer is yes!")
print(posthuman == "Vertigo")

print("\nIs Lucas a posthuman? I predict the answer is no!")
print(posthuman == 'Lucas')

posthuman2 = 'Pyrol'

print("\nAre bother Vertigo and Pyrol Posthumans?")
print(posthuman == 'Vertigo' and posthuman2 == 'Pyrol')

print("\nAre both Vertigo and Lysan posthumans? I predict no!")
print(posthuman == 'Vertigo' and posthuman2 == 'Lysan')

print("\nAre either Vertigo or Praxis posthuman? I predict yes!")
print(posthuman == 'Vertigo' or posthuman2 == 'Praxis')

print('\nIs Nodens or Prakka post human? i predict No!')
print(posthuman == 'Prakka' or posthuman2 == 'Nodens' )


list = ['monkey1', 'monkey2', 'monkey3']

print('monkey1' in list)
print('monkey3' not in list)