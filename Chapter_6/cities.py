cities = {
    'london': {
        'name':'london',
        'population': 8.982,
        'country':'united kingdom',
        'fact':'London could be classified as a forest',
    },
    'paris': {
        'name':'paris',
        'population': 2.161,
        'country':'france',
        'fact':"The French capital is home to the Eiffel Tower and the \
world's largest museum in the Louvre",
    },
    'madrid': {
        'name':'madrid',
        'population': 3.223,
        'country':'spain',
        'fact':'was once controlled by the Moors',
    },
}

for key_name, factoids in cities.items():
    print(f'\nHere are the facts for {key_name.title()}: ')
    for factoid_key, factoid_val in factoids.items():
        if isinstance(factoid_val, float): # to check if the value is a specific type
            print(f"{factoid_key} : {factoid_val} million.")
        else:
            print(f"{factoid_key.title()} : {factoid_val.title()}.")

        """if factoid_key['population']:
            print(f"{factoid_val} million")
        else:"""