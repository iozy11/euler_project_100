import time
def smallest_multiple(num):
    '''(int) -> int
Finds the lowest number that has all numbers from 1 to num as factors
'''
    tick = time.time()
    small = num
    while True:
        
        for i in range(2,num+1):
            if small % i == 0 and i == num:
                tock = time.time() - tick
                print('Code took ' + str(tock) + ' seconds to execute.')
                return small
            if small % i != 0:
                small += num
                break
    

print(smallest_multiple(20))
    
        
