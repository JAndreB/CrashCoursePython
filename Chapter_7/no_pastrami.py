sandwich_order = ['ham','pastrami', 'beef', 'cheese triple', 'chicken triple',\
    'pastrami', 'american triple','pastrami', 'heat attack']
finished_sandwiches = []

print("\nThe deli has run out of pastrami")

while 'pastrami' in sandwich_order:
    sandwich_order.remove('pastrami')

while sandwich_order:
    finished = sandwich_order.pop()
    
    print(f"Finishing order: {finished.title()}.")
    finished_sandwiches.append(finished)

#display finished sandwiches
print("\nThe following sandwiches are ready: ")
for each in finished_sandwiches:
    print(each.title())