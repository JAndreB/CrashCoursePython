user = ['maggie', 'suzy', 'suzie', 'admin', 'carlos']

if user:
    for name in user:
        if name == 'admin':
            print(f'\ngreetings {name.title()}, would you like your martini with access?')
        else:
            print(f'\ngreetings {name.title()}.')
else:
    print("\nIs there a user to log in?")