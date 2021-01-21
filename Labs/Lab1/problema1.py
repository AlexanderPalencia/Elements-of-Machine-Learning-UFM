inverse_triangule = lambda n: '\n'.join([
    f"{'-' * (i)}{'*' * (2 * i + 1)}"
    for i in range(8, 0, -1)
])

print(inverse_triangule(5))
