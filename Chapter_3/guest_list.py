guests = ['kain', 'akuji', 'chan']

for i in guests:
    print(f"\nHey, {i.title()}, i am inviting you to dinner!")

no_makey = guests.pop()
print(f"\nIt appears {no_makey.title()} cannot make it!")

for i in guests:
    print(f"\nHey, {i.title()}, i am inviting you to dinner!")


guests.append('cool J')
guests.insert(0, 'drunk monk')
guests.insert(1, 'wu tang')

for i in guests:
    print(f"\nHey, {i.title()}, i am inviting you to dinner!")

print("\nUnfortunately i can only eat 2 people!")

if len(guests) > 2:
    for i in guests:
        no_makey = guests.pop()
        print(f"\nUnfortunately i am going to have to tell {no_makey.title()} to go home!")

print(guests)

for i in guests:
    print(f"\nHey, {i.title()}, i am STILL inviting you to dinner!")

del guests[0]
del guests[0]

print(guests)

print(f"i have {len(guests)} guests on my dinner list!")