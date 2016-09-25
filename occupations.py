from flask import Flask, render_template
from random import choice, uniform
import csv

app = Flask(__name__)

myDict = {}

with open('occupations.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        job = row['Job Class']
        percent = float(row['Percentage'])
        if (job != 'Total'): myDict[job] = percent

def randOcc():
    benchmark = uniform(0, sum(myDict.itervalues())) #random number between 0 and the sum of the values of each key 
    total = 0.0
    for key in myDict:
        total+=myDict[key]
        #print "index:" + str(index) + "total:" + str(total)
        if benchmark < total:
            #print "WINN"
            return key
    return key
 
@app.route("/occupations")
def occupations():
  return render_template('occupationsTemplate.html', title = "Occupations", collection = myDict, occ = randOcc())

if __name__ == '__main__':
    app.debug = True
    app.run()
