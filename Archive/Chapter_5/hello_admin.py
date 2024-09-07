usernames = []

"""'jenny', 'suzi', 'mike', 'alice', 'jonah', 'admin'"""

for username in usernames:
    if username == 'admin':
        print(f'Hello {username.title()}, would you like to see a report?')
    else:
        print(f"Hello, {username.title()}, thank you for logging in again...")

if usernames == []:
    print("We need to find some users!")