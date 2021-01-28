"""  Es una libreria que hace operaciones aritmeticas, alebraicas, y matriciales
optimizado a codigo fuente, aprovecha para hacer pararelismo,

los arrays son en numpy en python son listas,
"""
import numpy as np

print(np.arange(10))
print(type(np.arange(10)))
print(type(list(np.arange(10))))

# para hacer arrays arange, array
print(np.array(10, 20, -2))
print(type(np.array(10, 20, -2))

# Dimensiones de un array de un solo eje
my_array = np.array(
    [
        [1, 5, -2]
    ]
)


# Array de dos ejes
my_array_two_ejes = np.array(
    [
        [1, 5, -2],
        [6, 0, 2]
    ]
)
print(my_array_two_ejes.shape)

# una tupla es una secuencia inmutable
# ipython

# un array con 10 ejes con tuplas
array_zeros = np.zeros((10, 10))
ones = np.ones()10, 10))

# Un array con 0 y 1 son necesarios

# Una matriz pensarlo como un cubo
my_array = np.ones((10, 10, 2))

# funcion reshape transforma de una dimension a otra
# en el siguiente ejemplo de una simple la pasa a 25 de 8 elementos
r = np.arrange(200).reshape(25,8)

# se le puede pasar un condicional a cada elemento del array
bool_array = np.arrange(200).reshape(25,8) % 5 == 0

# todos los numeros de 0 a 2, devuele arrays tambien se le puede pasar un condicional
linspace_array = np.linspace(0, 2, 1000).reshape(100,10)




linspace_array = np.full((3,3), 2).reshape(100,10)


# matriz identidad

eyearry = np.eye(8)


a = np.array([
    [1,2,3],
    [1,2,3],
    [1,2,3],
    [1,2,3]
])

# REPASAR MATRICES
# multiplicacion de matrices se hace con @ o hacerlo con .dot
# operacion matricial, matrices con formas distintas la operacion multiplicación
# La multiplicacion matricial no es conmutativa la propiedad matrix.T
# Descargar un sheet cheat
# Resolver un sistema de ecuaciones en numpy

Sistema de ecuacuiones, donde 


# funciones vstack y hstack


