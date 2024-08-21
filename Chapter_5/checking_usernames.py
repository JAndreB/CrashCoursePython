current_users = ['jenny', 'suzi', 'mike', 'alice', 'jonah', 'admin']

current_users_lower = [x.lower() for x in current_users]

new_users = ['joe', 'max', 'elise', 'jenny', 'MIKE']

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"\nSorry, {new_user} is already taken, please try a new name.")
    else:
        print(f'\n{new_user} is available for use.')