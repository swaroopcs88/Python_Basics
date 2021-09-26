# python program to check whether the current second is odd or not based on the system time stamp
# import datetime from the datetime module
from datetime import datetime
# importing the modules which are used in this program
import random
import time

# declaring the variable odds
odds = [1,2,3,4,9,11,23,13,42,34,53,44]

# number of times you are going to check whether the current second is odd or even
times = 5

print('odds = '+str(odds))
# number of times x is going to iterate 
for x in range(0, times):   
    pauseSecs = random.randint(0,x)
    time.sleep(pauseSecs)
    currSec = datetime.today().second
    print('currSec = '+str(currSec))
    if currSec in odds:
        print('this is an odd moment ' +str(x))
    else:
        print('this is not an odd moment! '+str(x))
 
print('done')
