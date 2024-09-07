"""squares = []
for value  in range(1, 101):
    square = value ** 2
    squares.append(square)

print(squares)

#OR

square = []
for value in range (0, 100):
    square.append(value**2)

print(square)"""

squares = [value**2 for value in range(0, 100)]
print(squares)
