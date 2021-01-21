# Nivel patito
def square_of_list(x):
    list_double = []
    for i in x:
        list_double.append(i**2)
    return list_double


# array Comprenhension, descripcion del conjunto
def square_of_list(x):
    return [i **2 for i in x]


# First level citizens (las funciones en python ss pueden almacenar en variables)
square_of_list1 = lambda ilist: [i **2 for i in x]


# Transformacioens
square = lambda n: n ** 2
cube  = lambda n: n ** 3


# Second order: functions (toma de parametro un funcion (transformacion))
# devuelvo una funcion de salida
def gen_list_transformer(transformation):
    transformer = lambda ilist: [transformation(i) for i in x]
    return transformer

square_of_list = gen_list_transformer(square)
square_of_list = gen_list_transformer(lambda n: n ** 2)

print(square_of_list1([1,2,3,4,5]))





def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))