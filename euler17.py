import time
def letterCount():
    '''(none) -> int
Hard coded, function returns the sum of all letters used to write
numbers from one to one thousand. Does not include hyphens or spaces,
does include use of the word "and"
'''
    tick = time.time()
    units = ['one','two','three','four','five','six','seven','eight','nine']
    tenTwenty = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    tens = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    total = 0
    count = 0
    #length of units
    for i in range(len(units)):
        total += len(units[i])
    
    #length of the weird numbers between ten and twenty
    for i in range(len(tenTwenty)):
        total += len(tenTwenty[i])
        
    #length of the tens
    for i in range(len(tens)):
        total += len(tens[i])
        
    #length of the other numbers between one and one hundred
    for i in range(len(tens)):
        for j in range(len(units)):
            total += (len(units[j]) + len(tens[i]))

    #length of just the hundreds
    for i in range(len(units)):
        total += len(units[i]) + len('hundred')   
    
    #length of numbers for all hundreds from x00->x09
    for i in range(len(units)):
        for j in range(len(units)):
            total += len(units[i]) + len('hundred') + len('and') + len(units[j])     
    
    #length of the weird numbers between ten and twenty, but for hundreds
    for i in range(len(units)):
        for j in range(len(tenTwenty)):
               total += len(units[i]) + len('hundred') + len('and') + len(tenTwenty[j])
    
    #length of the tens, for each hundred
    for i in range(len(units)):
        for j in range(len(tens)):
            total += len(units[i]) + len('hundred') + len('and') + len(tens[j])
            
    #length of all the other numbers for the hundreds
    for i in range(len(units)):
        for j in range(len(tens)):
            for k in range(len(units)):
                total += len(units[i]) + len('hundred') + len('and') + len(tens[j]) + len(units[k])
                
    
    total += len('onethousand')
    tock = time.time() - tick
    print('Code took ' + str(tock) + ' seconds to execute.')
    return total

print(letterCount())
