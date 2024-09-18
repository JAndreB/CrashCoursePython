favourite_places = {
    'mike': ['djenne', 'macau', 'porto'],
    'alex': ['porto', 'cordoba', 'madrid'],
    'jackson': ['alexandria', 'brasillia', 'rome'],
}

for name, places in favourite_places.items():
    print(f"\n{name.title()}'s favourite places are: ")
    for place in places:
        print(f'{place.title()}')
    