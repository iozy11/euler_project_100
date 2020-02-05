import time
def find_factors(num):
    '''(int) -> array
Finds all the factors for number (num) and returns them as an array
'''
    arr = []
    for i in range(1,num+1):
        if num % i == 0:
            arr.append(i)

    return arr


def triangle_factors(target):
    '''(int) -> int
Finds the first triangle number that has (target) factors
'''
    tick = time.time()
    t = 1
    n = 1
    while tau(t) < target:
        t = 0
        for i in range(n+1):
            t += i
        n += 1
    tock = time.time() - tick
    print('Code took ' + str(tock) + ' seconds to execute.')
    return t

            
def tau(num):
    '''(int) -> int
Returns how many divisors a number has
'''
    if num == 1:
        return 1
    
    n = num
    d = 2
    p = 1
    while d * d <= n:
        e = 1
        while n % d == 0:
            n /= d
            e += 1
        d += 1
        p *= e

    if n == num or n > 1:
        p *= 2
    return p

print(triangle_factors(500))
