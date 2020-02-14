import math, time

def powerDigitSum(num):
    '''(int) -> int
Finds 2 to the power of a number (num) then finds the sum of
all the digits in that number
'''
    tick = time.time()
    x = pow(2,num)
    s = str(x)
    total = 0
    for i in range(len(s)):
        total += int(s[i])

    tock = time.time() - tick
    print('Code took ' + str(tock) + ' seconds to execute.')
    return total

print(powerDigitSum(1000))
