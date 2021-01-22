import math
def rhombus(n):
    mid = math.ceil(n / 2)
    return '\n'.join([
        f"{' ' * (abs(mid - 1 - i))}{'* ' * (mid - abs(mid - 1 - i))}"
        for i in range(n)
    ])


print(rhombus(7))
print(rhombus(9))
print(rhombus(11))
print(rhombus(13))


