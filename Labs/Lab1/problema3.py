import math
def rhombus(n):
    mid = math.ceil(n / 2)
    return '\n'.join([
        f"{' ' * (abs(mid - 1 - i))}{'* ' * (mid - abs(mid - 1 - i))}"
        for i in range(n)
    ])


