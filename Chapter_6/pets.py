
pet_1 = {
    'animal':'dog',
    'owner':'mike',
    'name':'bet',
    'age':9,
    'sex':'male',
    'neutered':'no'
}

pet_2 = {
    'animal':'cat',
    'owner':'jen',
    'name':'cob',
    'age':12,
    'sex':'female',
    'neutered':'yes'
}

pet_3 = {
    'animal':'bat',
    'owner':'jill',
    'name':'incy',
    'age':4,
    'sex':'female',
    'neutered':'no'
}

pet_4 = {
    'animal':'cat',
    'owner':'maxime',
    'name':'boris',
    'age':4,
    'sex':'female',
    'neutered':'no'
}

pet_5 = {
    'animal':'dog',
    'owner':'bill',
    'name':'mikey',
    'age':6,
    'sex':'male',
    'neutered':'yes'
}

pets = [pet_1, pet_2, pet_3, pet_4, pet_5]

for pet in pets:
    print(f"\nHere is pet - {pet['name'].title()}:")
    for k, v in pet.items():
        print(f"{k.title()} : {v}")