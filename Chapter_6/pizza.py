#store information about a pizza being ordered.
pizza = {
    'crust':'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

#Summarize the order
print(f"You ordered a {pizza['crust']} crust pizza, with the\
 following toppings:")

for topping in pizza['toppings']:
    print(f'{topping}')

""">>> employee = {
...     "name": "John Doe",
...     "age": 35,
...     "job": "Python Developer",
... }

>>> f"Employee: {employee["name"]}"
  File "<stdin>", line 1
    f"Employee: {employee["name"]}"
                           ^^^^
SyntaxError: f-string: unmatched '['

In this example, you try to interpolate the employee name in your f-strings. \
    However, you get an error because the double quotes around the "name" \
        key break the string literal. To work around this, you need to use \
            a different type of quotation mark to delimit the key:"""