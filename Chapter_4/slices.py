magicians = ['alice', 'david', 'carolina', 'jane', 'michael', 'trina']
for magic in magicians:
    print(f"{magic.title()}, that was a great trick.")
    print(f"I can't wait to see your next trick {magic.title()}.\n")

print("Thank you, everyone. That was a great magic show!")

print("\nThe first 3 items in the list are:")
print(magicians[:3])


print("Three items in the middle of the list are: ")
print(magicians[1:4])

print("The three last items in the list are: ")
print(magicians[-3:])