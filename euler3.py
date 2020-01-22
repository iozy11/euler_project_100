import math

def euler3(num):
    '''(int) -> int
Takes an integer and returns the largest prime factor
'''
    prime = 0
    for i in range(3,math.floor(math.sqrt(num))):
        token = True
        if num % i == 0:
            for j in range(2,i):
                if i % j == 0:
                    token = False
            if token == True:
                prime = i
            
                
    return prime
