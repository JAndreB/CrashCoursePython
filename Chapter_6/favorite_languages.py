favourite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }

#Declares the key and values in favourite_languages
for name, languages in favourite_languages.items():
    #If length of list in value languages is more than 2
    if len(languages) > 1:
        #print the below
        print(f'\n{name.title()} favourite languages are:')
        #for each item in the list that is languages, print this
        for language in languages:
            print(f"{language.title()}")
    #if the length of the list in teh value languages is less than 2 print this
    else:
        print(f'\n{name.title()} favourite language is:')
        print(f'{language.title()}')

"""language = favourite_languages['sarah'].title()
print(f"\nSarah's favourite language is {language}.")"""

"""for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")

for name in favourite_languages.keys():
    print(name.title())"""

"""friends = ['phil', 'sarah']
for name in favourite_languages:
    print(f"Hi {name.title()}")
    if name in friends:
        language = favourite_languages[name].title()
        print(f"\t{name.title()}, i can see that you like {language}")#

if 'erin' not in favourite_languages.keys():
    print('Please Erin, take out poll!')

for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll!")"""

"""print("The following languages have been mentioned:")
for langauge in set(favourite_languages.values()):
    print(langauge.title())
"""


