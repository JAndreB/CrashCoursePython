from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
    pi_string += line.strip()

birthday = input('Enter your birthday please in the format mmddyy: ')
if birthday in pi_string:
    print("Your birthday is in the first million digits of Pi!")
else:
    print("Your birthday is not in the first million digits of Pi...")

#print(f"{pi_string[:52]}...")
#print(len(pi_string))