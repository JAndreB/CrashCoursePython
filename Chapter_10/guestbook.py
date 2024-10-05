from pathlib import Path

path = Path('guest_book.txt')

guest_names = []
while True:
    name = input('Name Please: ')
    if name == 'quit':
        break

    print('We are adding you to the list')
    guest_names.append(name)

file_string = ''
for name in guest_names:
    file_string += f'{name}\n'

path.write_text(file_string)