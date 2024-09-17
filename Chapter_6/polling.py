favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

should = ['mike', 'donna', 'jen', 'phil', 'carrot top', 'niles']

for name in should:
    if name in favourite_languages.keys():
        print(f"Thanks for taking the poll, {name.title()}")
    else:
        print(f'Please take the poll, {name.title()}.')
