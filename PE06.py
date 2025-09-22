squares = []
integers = []

for i in range(1,101):
    integers.append(i)
    squares.append(i**2)

print(sum(integers)**2 - sum(squares))

