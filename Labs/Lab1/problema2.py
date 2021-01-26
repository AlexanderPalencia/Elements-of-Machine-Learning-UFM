cache = {}
def recurrence_relation(n,m):
    if (n, m) in cache:
        return cache[(n, m)]
    if m == n:
        cache[(n, m)] = 1
        return 1
    if m == 0:
        cache[(n, m)] = 1
        return 1
    if (n >=  m) and (m > 0):
        cache[(n, m)] = recurrence_relation(n - 1, m) + recurrence_relation(n - 1, m - 1)
        return cache[(n, m)]
    
