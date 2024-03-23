dog = 'Cockerspaniel'
print("Is dog == 'cockerspaniel', i predict, True.")
print(dog == 'Cockerspaniel')

car = 'tesla'
print("\nIs car == 'tesla'? I predict True!")
print(car == 'tesla')

man = 'terminal'
print("\nIs man == 'horror'? I predict False.")
print(man == 'horror')

me = 'in hell'
print("\nIs me == 'in hell'? i predict True!")
print(me == 'in hell')

inside = 'Cardi B'


print("\nAm i inside Cardi B? I think not!")
print(inside.lower() == 'cardi b')
print(inside)

age1 = 21
age2 = 19

print("\nAre both above age?")
print(age1 > 21 and age2 > 21)

age1 = 23
age2 = 25

print("\nAre both above age now?")
print(age1 > 21 and age2 > 21)

age1 = 23
age2 = 15

print("\nIs at least 1 above age now?")
print(age1 > 21 or age2 > 21)

guests = ["Hannibal", "Lycurgis", "Alforn", "Percival", "Niydbrich"]

print("\nIs Hanlon in the list?")
guest = "Hanlon"
if guest not in guests:
    print(f"Not on the list {guest}, git!")

print("\nIs Lycurgis in the list?")
guest = "Lycurgis"
if guest in guests:
    print(f"Welcommen, {guest}.")