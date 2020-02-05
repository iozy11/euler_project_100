import time
def fib_even_sum(num):
    '''(int) -> int
Finds sum of even numbers for fibbonaci numbers below a number (num)
    '''
    tick = time.time()
    f1 = 0
    f2 = 1
    total = 0

    while f2 <= num:
        if f2 % 2 == 0:
            total += f2
        f2 += f1
        f1 = f2 - f1
    tock = time.time() - tick
    print('Code took ' + str(tock) + ' seconds to execute.')
    return total

print(fib_even_sum(4000000))