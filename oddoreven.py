from datetime import datetime

currSec = datetime.today().second

odds = [1,3,5,7,9,11,13,15,17,29,21,23,25,27,29]

if currSec in odds:
    print("This moment is odd!")
else:
    print("This moment is not so odd at all")
    
