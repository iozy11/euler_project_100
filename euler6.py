import time
def sum_square_dif(num):
    '''(int) -> int
finds the difference between the sum of the squares and the square
of the sum of natural numbers between 1 and num
'''
    tick = time.time()
    sumS = 0
    squareS = 0

    for i in range(1,num+1):
        squareS += i
    squareS = squareS ** 2

    for j in range(1,num + 1):
        sumS += j ** 2
    
    tock = time.time() - tick
    print('Code took ' + str(tock) + ' seconds to execute.')
       
    return squareS - sumS

print(sum_square_dif(100))
