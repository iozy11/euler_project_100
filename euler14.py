import time
def long_collatz(num):
    '''(int) -> int
Takes a number and finds the longest Collatz chain
below that number
'''
    tick = time.time()
    n = num
    long = 0
    digit = 0
    while n > 1:
        c = n
        chain = 0
        while c > 1:
            chain += 1
            if c % 2 == 0:
                c /= 2
            else:
                c = c * 3 + 1
        if chain > long:
            long = chain
            digit = n
        n -= 1
    tock = time.time() - tick
    print("Code took " + str(tock) + " seconds to execute")
    return digit

print(long_collatz(1000000))
