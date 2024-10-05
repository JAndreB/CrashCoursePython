from pathlib import Path

path = Path('guest.txt')

guestname = input("Please provide your name: ")

path.write_text(guestname)

