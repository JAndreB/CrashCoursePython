#variable for 1st name
firstname = "ada"

#variable for 2nd name
lastname = "lovelace"

#using "f" to convert variable to string for formatting, creating an 'f string'
full_name = f"{firstname} {lastname}"
print(full_name)

#Creating more complex f string
print(f"Hello, {full_name.title()}!")

#Turning an f String into a variable and then printing it
message = f"Hello, {full_name.title()}!"
print(message)

