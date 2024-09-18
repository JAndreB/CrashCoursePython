"""name  = input("What's your name: ")
print(f"\n Hellur, {name.title()}!")"""

prompt = "If you share a name with someone else, we can personalise the \
messages you see."
prompt += '\n What is your name: '

name = input(prompt)
print(f'\nHello, {name.title()}!')