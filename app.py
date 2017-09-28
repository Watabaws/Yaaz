'''
Adam Abbas & Yuyang Zhang 
SoftDev1 pd07
HW5 -- Jinja Tuning
2017-09-27
'''
from flask import Flask, render_template
from utilities import occupations

app = Flask(__name__)

@app.route("/")
def filler_page(): #used as home page
    return "<br><br><center><h1><a href='/occupations'> Click here for the good stuff </a> </h1></center>"

@app.route("/occupations")
def occu_worked():
    return render_template("skeleeto`n.html", tl = "Occupations", heading = "Future Occupation Options", d = occupations.formatted_occs(), r = occupations.random_occupation()) #define variables

if __name__ == "__main__": #keeps code running after changes
    app.debug = True
    app.run()
