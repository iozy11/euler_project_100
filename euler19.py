import time
def sundays():
    '''(none) -> int
Counts the amount of Sundays that fall on the first of the month
during the 20th century
'''
    
    count = 0
    weekD = 3
    day = 1
    month = 1
    year = 1901
    while year < 2001:
        # Check to see if today is Sunday, first of the month
        if day == 1 and weekD == 1:
            count +=1
        #Change the date
        #If the month has 30 days, increment or move to next month
        if month in {4,6,9,11}:
            if day == 30:
                day = 1
                month += 1
            else:
                day += 1
        #If the month has 31 days, increment or move to next month
        elif month in {1,3,5,7,8,10,12}:
            if day == 31:
                day = 1
                #If it's December 31st, move to next year.
                if month == 12:
                    month = 1
                    year += 1
                else:
                    month += 1
            else:
                day += 1
        #February
        else:
            #Increment month after 29th
            if day == 29:
                day = 1
                month += 1
            elif day == 28:
                #Inrement date to 29th on a centenial leap year
                if year % 100 == 0:
                    if year % 400 == 0:
                        day += 1
                    else:
                        day = 1
                        month += 1
                #Increment date to 29th on normal leap year
                elif year % 4 == 0:
                    day += 1
                #Increment months on non leap-year
                else:
                    day = 1
                    month += 1
            #Increment date any other day
            else:
                day += 1
        #Change weekday
        if weekD == 7:
            weekD = 1
        else:
            weekD += 1
    
    return count

tick = time.time()
print('There are ' + str(sundays()) + ' Sundays on the first of the month in the 20th century')
tock = time.time() - tick
print('Code took ' + str(tock) + ' seconds to execute')
    
            
             
