import csv

with open('housing.csv','r') as file:
     reader = csv.reader(file)
     header = next(reader,None)
     data = []
     for item in reader:
         data.append(item)

     print(f'{header=}')
     print(f'{data=}')
