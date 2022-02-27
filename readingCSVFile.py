# reading csv files in python

import csv

# opening the CSV file

with open(r"c:\Users\swaro\Downloads\sample1.csv", mode="r") as file:

    # reading the CSV file
    csvFile = csv.reader(file)

    # displaying the contents of the CSV file
    for lines in csvFile:
        print(lines)


    
