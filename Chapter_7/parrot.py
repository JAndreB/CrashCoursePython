prompt = "\nTell me something and i will repeat it back to you!"
prompt += "\nEnter 'quit' to quit the program."

active = True # active fleg set to true, 
"""message = ''"""# initializing an empty list for the while loop to check
while active: #The loop will check if the active flag is true and if not will
#not run the loop
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)