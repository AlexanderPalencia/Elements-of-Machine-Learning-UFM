def factorial_normal(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


'''
cuando podamos conceptualizar una lista a un escalar se usa el concpto redux: la reduccion de una lista
Se tiene el acumulador y el valor ambas variables, cada paso de la reduccion se recorrre la lista en orden el acumulador guarda y valor el indice de la lista
ammbos se uilizan para generar una formula

las funciones son 1st class citizen: se pueden pasar como parametros de funcion y como retuns
ls operaciones con listas son 
'''
from functools import reduce

factorial = lambda n: reduce(
    lambda acc, val: acc * val, 
    range(2, n + 1),
    1
) if n > 0 else 0


print(factorial(5))