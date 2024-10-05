from pathlib import Path

path = Path('learning Python.txt')
contents = path.read_text()

for line in contents.splitlines():
    print(line)
    print(line)