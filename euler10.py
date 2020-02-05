import time
def prime_sieve(num):
    '''(int) -> array
Finds the sum of all primes smaller than num
'''
    tick = time.time()
    #Create an array of "True" 2 through num
    arrT = [True for i in range(2,num+1)]
    arrP = []
    p = 2
    #Primes beneath a certain num all fall between 2 and sqrt(num)
    while p * p < num:
        #Set false all multiples of number p
        for i in range(2*p,len(arrT),p):
            arrT[i] = False
        p += 1
        #any number that is still "True" is prime
    #Create an array, starting with 2, of all True indices(the index == a prime)
    for i in range(2,len(arrT)):
        if arrT[i] == True:
            arrP.append(i)
    tock = time.time() - tick
    print('Code took ' + str(tock) + ' seconds to execute.')
    return arrP

print(sum(prime_sieve(2000000)))
