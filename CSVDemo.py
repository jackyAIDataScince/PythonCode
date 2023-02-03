import csv

with open('housing.csv','r') as file:
     reader = csv.reader(file)
     
     for row in reader:
         print(row)
