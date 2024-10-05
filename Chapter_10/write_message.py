from pathlib import Path

path = Path('programming.txt')
line  = (input('Write a line!!!'))
path.write_text(line)