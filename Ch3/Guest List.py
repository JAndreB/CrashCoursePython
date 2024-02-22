guests = ["Hannibal", "Lycurgis", "Alforn", "Percival", "Niydbrich"]

for i in guests:
    print(f'Hello {i.title()}, i am inviting you to dinner.')

print (f"\nSorry {guests[3].title()}, sorry you cannot make it.\n")

del guests[3]

guests.insert(3, "Longinus")

for i in guests:
    print(f'Hello {i.title()}, i am inviting you to dinner.')

