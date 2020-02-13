import math, time
def lattice(x,y):
    '''(int, int) -> int
Finds the number of shortest routes through an m by n matrix
'''
    tick = time.time()
    n = math.factorial(x+y)
    m = math.factorial(x)
    k = math.factorial(y)
    ans = n/(m*k)
    tock = time.time() - tick
    print('Code took ' + str(tock) + ' seconds to execute.')
    return int(ans)

print(lattice(20,20))
