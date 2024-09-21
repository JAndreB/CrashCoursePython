sandwich_order = ['ham', 'beef', 'cheese triple', 'chicken triple', 'american\
 triple', 'heat attack']
finished_sandwiches = []

while sandwich_order:
    finished = sandwich_order.pop()
    
    print(f"Finishing order: {finished.title()}.")
    finished_sandwiches.append(finished)

#display finished sandwiches
print("\nThe following sandwiches are ready: ")
for each in finished_sandwiches:
    print(each.title())
