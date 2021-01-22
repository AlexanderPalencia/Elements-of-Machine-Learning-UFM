inverse_triangule = lambda n: '\n'.join([
    f"{' ' * (n - i - 1)}{'*' * (2 * i + 1)}"
    for i in range(n - 1, -1, -1)
])

print(inverse_triangule(5))