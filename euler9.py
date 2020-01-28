import math as m
def triplet(num):
    '''(int) -> str
Finds the pythagorean triplet that equals num, if any exists
'''
    
    for i in range(1,num):
        for j in range(1,num):
            c = m.sqrt(i ** 2 + j ** 2)
            if c == m.floor(c):
                if i + j + c == num:
                    return str(i) + ',' + str(j) + ',' + str(int(c))
    return 'No triplet found for' + str(num)

print(triplet(1000))
