#Start with users to be verified,
# and an empty list to hold confirmed users
unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_user = []

#verify each user until there are no more unconfirmed users.
#move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_user.append(current_user)

#Display all confirmed users
print("\nThe list of confirmed users is:")
for confirmed in confirmed_user:
    print(confirmed.title())
