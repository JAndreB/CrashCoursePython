def city_country(city, country):
    """A city: country dic generator"""
    pair = {'City':city.title(), 'Country':country}
    if pair['Country'] == 'usa':
        pair = {'City':city.title(), 'Country':country.upper()}
    elif pair['Country'] == 'uk':
        pair = {'City':city.title(), 'Country':country.upper()}
    elif pair['Country'] == 'uae':
        pair = {'City':city.title(), 'Country':country.upper()}
    else:
        pair = {'City':city.title(), 'Country':country.title()}

    return pair

citycountry = city_country('paris', 'france')
print(citycountry)

citycountry = city_country('london', country='uk')
print(citycountry)

citycountry = city_country('new york', country='usa')
print(citycountry)

