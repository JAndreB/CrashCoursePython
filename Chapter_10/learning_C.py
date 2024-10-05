from pathlib import Path

path = Path('learning Python.txt')
contents = path.read_text()

contents = contents.replace('python', 'C')

for line in contents.splitlines():
    print(line)
    print(line)