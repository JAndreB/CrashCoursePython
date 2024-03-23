current_users = ['mike', 'jamie', 'ben', 'carlos', 'Paul']

new_users = ['mike', 'paul', 'TERRY', 'john', 'seb']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user in current_users_lower:
        print(f"\nYou will need to use a new name " + new_user + "!")
    else:
        print(f"\nGreat, " + new_user + ", this name is still available!")