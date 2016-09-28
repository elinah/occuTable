from flask import Flask, render_template
from utils import occupations

app = Flask(__name__)

@app.route("/occupations")
def randOccupations():
  return render_template('occupationsTemplate.html', title = "Occupations", collection = occupations.myDict, occ = occupations.randOcc())

if __name__ == '__main__':
    app.debug = True
    app.run()
