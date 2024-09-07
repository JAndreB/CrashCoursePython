#initiate list ''guests
guests = ['johnny silverhand', ' midas mulligan', 'dirty harry', 'JC Denton', 'biophage', 'MF Doom', 'Dr Doom']

#loop to generate invitations for each member in lists
for i in guests:
    print(f"\nGreetings {i.title()}, i am inviting youy to dinner, RSVP?")

#Looks like JC can't make it, removing him from the list and reprinting the loop
print(f'\nUnfortunately it appears that {guests[3].title()} cannot make it!')

guests.remove('JC Denton')

for i in guests:
    print(f"\nGreetings {i.title()}, i am inviting youy to dinner, RSVP?")


#found a bigger table, using insert at the beginning and middle and then append to make bigger list
print(f'\n{guests}, looks like i have found a bigger table!')

guests.insert(0, 'Kassius klinsman')
guests.insert(3, 'Dom Perry')
guests.append('ghostface')

for i in guests:
    print(f"\nGreetings {i.title()}, i have found a biogger table and i am still inviting youy to dinner, RSVP?")

#REemoving people from the list using a variable the contains a popped value from the list multiple times
print('Actually, i can only invite 4 more people')

guest_Gone = guests.pop()
print(f'\n{guest_Gone.title()}, Sorry, youy are no longer invited')

guest_Gone = guests.pop()
print(f'\n{guest_Gone.title()}, Sorry, youy are no longer invited')

guest_Gone = guests.pop()
print(f'\n{guest_Gone.title()}, Sorry, youy are no longer invited')

guest_Gone = guests.pop()
print(f'\n{guest_Gone.title()}, Sorry, youy are no longer invited')

guest_Gone = guests.pop()
print(f'\n{guest_Gone.title()}, Sorry, youy are no longer invited')

print(guests)

# A loop to print greertings for the remaining list elements
for i in guests:
    print(f"\nGreetings {i.title()}, i am still inviting youy to dinner, RSVP?")

#removing the last 2 elements from the list
del guests[-1]
del guests[-1]

print(guests)

