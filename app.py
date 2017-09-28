'''
Adam Abbas & Yuyang Zhang 
SoftDev1 pd07
HW5 -- Jinja Tuning
2017-09-27
'''

import random
from collections import defaultdict
from flask import Flask, render_template

app = Flask(__name__)



def formattedOccs():
    fyle = open("data/occupations.csv", "r") #Open up our csv file so we can get to working on it
    lest = fyle.readlines() #Read the file in a way that each line is a list item
    fyle.close()
    dicsha = {} #Close up the file
    i = 1 #this is going to be the index of our list!!
    lest = lest[:len(lest)-1]

    while (i<len(lest)):
         thisLine = lest[i] #Let's grab the current line
         comma = thisLine.rfind(",") #Let's also find the right comma - the one that seperates the number and value
         dicsha[thisLine[:comma].strip('"')] = thisLine[comma + 1:].strip('\n').strip("\r") #Add the stuff before the comma (occupation) to the dictionary as a key, then add the stuff after the comma as a value!
         i += 1 #Wouldn't want an infinite loop now would we
    return dicsha

def random_occupation():
    dicsha = formattedOccs()
    c = 0 #counter for while loop
    random_float = random.uniform(0.0, 99.8) #float within range
    #print random_float
    cumulative_probability = 0.0
    while (c < len(dicsha)):
        cumulative_probability += float(dicsha.values()[c])
        if (cumulative_probability>random_float):
            return dicsha.keys()[c]
        c += 1

@app.route("/")
def fillerpage(): #used as home page
    return "<br><br><center><h1><a href='/occupations'> Click here for the good stuff </a> </h1></center>"

@app.route("/occupations")
def occuWorked():
    return render_template("skeleeto`n.html", tl = "Occupations", heading = "Future Occupation Options", d = formattedOccs(), r = random_occupation()) #define variables




if __name__ == "__main__": #keeps code running after changes
    app.debug = True
    app.run()
