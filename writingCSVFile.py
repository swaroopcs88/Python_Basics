# writing a CSV File
import csv

# open the file in the write mode

with open(r'c:/Users/swaro/Downloads/Untitled spreadsheet.xlsx', 'w', newline='') as file:

# create the csv writer
    writer = csv.writer(file)
"""
# write a row to the csv file
    writer.writerow(["SN", "Movie", "Protaganist"])
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])
"""
# writing multiple rows with writerows()
csv_rowlist = [["SN", "Books", "Author"], [1, "My Experiments with truth", "M K Gandhi"], [2, "Wings of Fire", "APJ Abdul Kalam"], [3, "Americadhalli Goruru", "Goruru Ramaswamy Aiyangar"], [4, "Facing Up", "Bear Grylls"]]
with open(r'c:/Users/swaro/Downloads/Untitled spreadsheet.xlsx', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_rowlist)

