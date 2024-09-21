messages = ['monk','desial','jiminiy', 'pike']
sent_messages = []

def print_messages(messages, sent):
    """print list"""
    messages = messages[:]
    while messages:
        for each in messages:
            each = messages.pop()
            print(f'Sending message: {each}')
            sent.append(each)


print_messages(messages, sent_messages)
print(messages)
print(sent_messages)
