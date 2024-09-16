
car = 'amw 35'
print('Is car == "humma"? I predict false')
print(car == 'humma')

print('\nIs car == "cougar", i predict false!')
print(car == 'cougar')

print('\n Is car == "pol poz", i predict false!')
print(car == 'pol poz')

print('\n Is car == "big bertha?", i predict false!')
print(car == 'big bertha')

print('\nIs car == "AMW 35?", i predict true!')
print(car == 'amw 35')

car = 'humma'
print('\nIs car == "humma"? I predict true!')
print(car == 'humma')

car = 'cougar'
print('\nIs car == "cougar", i predict true!')
print(car == 'cougar')

car = 'pol poz'
print('\n Is car == "pol poz", i predict true!')
print(car == 'pol poz')

car = 'big bertha'
print('\n Is car == "big bertha?", i predict true!')
print(car == 'big bertha')

car = 'NOCT NINETY ONE'
print('\nIs car == "NOCT NINETY ONE"? I predict true!')
print(car.lower() == 'noct ninety one')

dad = 32
kid = 10

if dad < 55 and kid > 5:
    print('\nOut of touch!')

if dad < 90 or kid < 20:
    print('\nMore rhymin!')

fam = ['dad', 'mom', 'son', 'daughter', 'cat', 'dog']

if 'dog' in fam:
    print("\nI guess you guys eat dog!")

if 'parrot' not in fam:
    print('\nWhere is that god damn parrot!')

