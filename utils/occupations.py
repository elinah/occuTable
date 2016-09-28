from random import choice, uniform
import csv

myDict = {}

with open('data/occupations.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        job = row['Job Class']
        percent = float(row['Percentage'])
        link = row['Links']
        if (job != 'Total'): myDict[job] = [percent, link]

def randOcc():
    sumPer = 0.0
    for key in myDict:
        sumPer+=myDict[key][0]
    benchmark = uniform(0, sumPer) #random number between 0 and the sum of the values of each key 
    total = 0.0
    for key in myDict:
        total+=myDict[key][0]
        #print "index:" + str(index) + "total:" + str(total)
        if benchmark < total:
            #print "WINN"
            return key
    return key
print randOcc()
