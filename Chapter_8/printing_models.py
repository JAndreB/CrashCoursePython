"""#Start with some designs that need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
finished_designs = []

#Simulate printing each design, until there are none left
# Move each design to completed models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing current design: {current_design}")
    finished_designs.append(current_design)

#display all printed models
print("\nThe following models have been printed:")
for design in finished_designs:
    print(f"{design}")"""

def print_models(unprinted_designs, finished_designs):
    """simulate printing each design until none left"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing current design: {current_design}")
        finished_designs.append(current_design)

def show_finished(finished_designs):
    """display all printed models"""
    print("\nThe following models have been printed:")
    for design in finished_designs:
        print(f"{design}")

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
finished_designs = []

print_models(unprinted_designs, finished_designs)
show_finished(finished_designs)