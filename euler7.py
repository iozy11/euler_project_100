def nth_prime(num):
    '''(int) -> int
Shows what the nth prime is, where num is "n"
'''
    count = 1
    prime = 1
    while count < num:
        prime += 2
        token = True
        for i in range (2,prime):
            if prime % i == 0:
                token = False
                break
        if token == True:
            count += 1
    return prime

print(nth_prime(10001))
