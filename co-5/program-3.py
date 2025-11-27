import csv
with open('Student.csv','r')as file1:
    reader=csv.reader(file1)
    for row in reader:
        print(row)
