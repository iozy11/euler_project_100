def euler4(x,y):
    '''(int,int) -> int
finds the largest palindromic product of numbers between the ranges of [x,y)
'''
    big = 0
    for i in range(x,y):
        for j in range(x,y):
            if str(i*j) == str(i*j)[::-1] and i * j > big:
                big = i * j
    return big
