def fuzzy_bizz(num):
    '''(int) -> int
Finds the sum of all multiples of 3 or 5 smaller than 1000
'''
    total = 0
    for i in range(0,num):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

print(fuzzy_bizz(1000))