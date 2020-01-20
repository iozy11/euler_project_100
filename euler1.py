def euler1():
    '''(none) -> none
Finds the sum of all multiples of 3 or 5 smaller than 1000
'''
    total = 0
    for i in range(0,1000):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    print(total)
