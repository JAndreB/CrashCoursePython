def describe_city(city, country='USA'):
    """Describe a city and a country"""
    print(f"{city.title()} is in {country.title()}")

describe_city('new york')
describe_city('new orleans')
describe_city('paris', 'france')