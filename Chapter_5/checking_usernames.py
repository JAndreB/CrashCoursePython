usernames = ['Monty', 'Rick', 'Python', 'Pickle', 'admin', 'Joe', 'Kid']

#List comprehension to convert all list items to lowercase
username_lower = [username.lower() for username in usernames]

new_users = ['monty', 'jack', 'title', 'gon', 'pickle']

if username_lower:

    for new_user in new_users:
        if new_user.lower() in username_lower:
            print(f'\n{new_user} is already taken, try again!')
        else:
            print(f'\n{new_user},your username is novel, continue the application!')
else:
    print('Find us som new users, bucko!')
