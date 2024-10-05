from pathlib import Path


def wordcount(path):
    try:
        text = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"{str(path).removesuffix('.txt')} does not exist, please try again.")
    else:
        word = (input(f"Enter a word you would like to count in {str(path).removesuffix('.txt')}: ") + ' ')
        no_of_words = text.lower().count(word)
        print(f"The number of times the word '{word.strip()}' appears in\
 '{str(path).removesuffix('.txt')}' is {no_of_words}.")




path = Path(input('What text would you like to search: '))
wordcount(path)



    


