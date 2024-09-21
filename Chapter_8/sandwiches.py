def make_sandwich(*fillings):
    print("\nMaking your sandwich now, your fillings are: ")
    for each in fillings:
        print(f"- {each}")

make_sandwich('rice', 'beans', 'clutter')
make_sandwich('ham', 'cheese', 'mayo')
make_sandwich('apple slice', 'chicken', 'tomato')