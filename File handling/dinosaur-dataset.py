import csv
import math
Leg , stride = {}, {}

with open('dataset1.csv','r') as file:
    for row in csv.reader(file):
        if len(row)>2 and row[0].strip() != 'NAME':
            Leg[row[0].strip()] = float(row[1].strip())
            # print (Leg)

with open('dataset2.csv','r') as file:
    for row in csv.reader(file):
        if len(row)>2 and row[0].strip() != 'NAME':
            stride[row[0].strip()] = (float(row[1].strip()), row[2].strip())

res = []
g = 9.8
for dinosaur, (stride_length, pedal) in stride.items():
    if dinosaur in Leg:
        speed = ((stride_length / Leg[dinosaur])-1) * math.sqrt(Leg[dinosaur]*g)
        res.append([dinosaur, speed])

res.sort(key=lambda s: s[1])

for s in res:
    print (s)
