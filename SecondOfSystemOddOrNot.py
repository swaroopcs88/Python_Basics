# check whether the current second is odd or even based on the system time stamp
from datetime import datetime
import random
import time

# declare a variable odds
odds = [1,2,3,4,9,11,23,13,42,34,53,44]

# number of times you want to iterate over
times = 5

print('odds = '+str(odds))
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
