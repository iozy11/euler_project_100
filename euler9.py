import math as m
import time
def triplet(num):
    '''(int) -> str
Finds the pythagorean triplet that equals num, if any exists
'''
    tick = time.time()
    for i in range(1,num):
        for j in range(1,num):
            c = m.sqrt(i ** 2 + j ** 2)
            if c == m.floor(c):
                if i + j + c == num:
                    tock = time.time() - tick
                    print('Code took ' + str(tock) + ' seconds to execute.')
                    return str(i) + ',' + str(j) + ',' + str(int(c))
    tock = time.time() - tick
    print('Code took ' + str(tock) + ' seconds to execute.')
    return 'No triplet found for' + str(num)

print(triplet(1000))
