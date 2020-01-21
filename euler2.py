def euler2():
    '''(none) -> none
Finds sum of even numbers for fibbonaci numbers below 1 000 000
    '''
    f1 = 0
    f2 = 1
    total = 0

    while f2 <= 4000000:
        if f2 % 2 == 0:
            total += f2
        f2 += f1
        f1 = f2 - f1
    print(total)

euler2()