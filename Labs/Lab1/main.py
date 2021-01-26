import time
import problema1
import problema2
import problema3
import problema4

print('Problema 1 \n')
print(problema1.inverse_triangule(4))
print(problema1.inverse_triangule(5))
print(problema1.inverse_triangule(6))

print('\n'*2 + 'Problema 2 \n')
print(problema2.recurrence_relation(50, 35))
print(problema2.recurrence_relation(100, 85))

print('\n'*2 + 'Problema 3 \n')
print(problema3.rhombus(7))
print(problema3.rhombus(9))
print(problema3.rhombus(11))



print('\n'*2 + 'Problema 4 \n')
start = time.time()
x = problema4.list_primes(100000)
print('Computed in: ', time.time() - start)
print('\n \n To print the prime numbers uncomment the line below. \n')
# print(x)
