responses = {}
#set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    #prompt for a users name and response
    name = input("\nWhat is your name: ")
    response = input("Which mountain would you like to climb some day?")

    #store the response in the dictionary
    responses[name] = response

    #find out if anyone else is taking the pol
    repeat = input("\nWould any one else like to take the poll? (yes/no)")
    if repeat == 'no':
        polling_active = False

#Polling is complete, show the result
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()} Mountain")
