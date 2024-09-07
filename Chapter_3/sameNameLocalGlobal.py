def spam():
    global eggs
    eggs = 'spam' # this is the global
def bacon():
    eggs = 'bacon' # this is a local
def ham():
    print(eggs) # this is the global 
eggs = 42 # this is the global
spam()
print(eggs)

# IN short global scope eggs has been defined as spam, so when eggs is define elsewhere
# this does not matter. So eggs is declared as 42 and then spam declares global eggs
# so when we print eggs, we get spam.