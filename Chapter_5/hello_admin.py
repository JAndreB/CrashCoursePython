usernames = ['Monty', 'Rick', 'Python', 'Pickle', 'admin', 'Joe', 'Kid']


if usernames:

    for username in usernames:
        if username == 'admin':
            print(f'\nGreetings {username}, admin privileges have been granted...')
        else:
            print(f'\nGreetings {username}, welcome back to HUB')
        
else:
    print('\nWe will need some users to build the HUB.')