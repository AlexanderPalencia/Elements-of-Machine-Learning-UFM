'''
The function first generate a set of cronological numbers, the most efficient way to search the primes numbers is to generate a set of the multiples of each number in the set for later with the difference_update function only keep the numbers that are not repeated in both lists.

reference:https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
'''
def list_primes(n):
    list_numbers = set(range(2, n + 1, 1))
    list_numbers.difference_update(set(range(0, n + 1, 2)))
    primes = [1]
    while list_numbers:
        eval_num = list_numbers.pop()
        primes.append(eval_num)
        list_numbers.difference_update(set(range(eval_num * 2, n + 1, eval_num)))
    return primes
