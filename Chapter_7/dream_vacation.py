vacation = {}

polling_active = True

while polling_active:

    name = input("\nWhat is your name? ")
    destination = input("Where would you like to go some day? ")

    vacation[name] = destination

    answer = input("\n Is there anyone else who wants to answer? (yes/no) ")
    if answer == 'no':
        polling_active = False

print("--- poll results ---")
for name, dest in vacation.items():
    print(f"Ah, {dest.title()}, i knew {name.title()} would want to go there...")
        
        