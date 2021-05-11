import csv
file = open('data/data.csv','r')
csv_data = csv.reader(file, delimiter=";")
for data in csv_data:
    print(f'Zeit: {data[5]} Temp: {data[6]}')
    
#    for d in data:
#        print(d)
