import math
import time
def largest_prime(num):
    '''(int) -> int
Takes an integer and returns the largest prime factor
'''
    tick = time.time()
    prime = 0
    for i in range(3,math.floor(math.sqrt(num))):
        token = True
        if num % i == 0:
            for j in range(2,i):
                if i % j == 0:
                    token = False
            if token == True:
                prime = i
    tock = time.time() - tick
    print('Code took ' + str(tock) + ' seconds to execute.')         
    return prime

print(largest_prime(600851475143))