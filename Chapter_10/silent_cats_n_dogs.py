from pathlib import Path

def listnames(path):
    try:
        names = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        print(names)

path = Path('cats1.txt')
listnames(path)

path = Path('dogs.txt')
listnames(path)
