from datetime import datetime
import random
import time


odds = [1, 3, 5, 7, 9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]

times = 5

print("odds = "+str(odds))
for x in range(0, times):
    pauseSecs = random.randint(0, x)
    time.sleep(pauseSecs)
    currSec = datetime.today().second
    print("currSec = "+str(currSec))
    if currSec in odds:
        print("This is an odd moment " + str(x))
    else:
        print("This is not an odd moment " + str (x))

