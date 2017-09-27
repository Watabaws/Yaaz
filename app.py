import random
from collections import defaultdict
from flask import Flask, render_template

app = Flask(__name__)



def formattedOccs():
    cool_file = open("data/occupations.csv", "r") #Open up our csv file so we can get to working on it
    cool_list = cool_file.readlines() #Read the file in a way that each line is a list item
    cool_file.close()
    cool_dic = {} #Close up the file
    i = 1 #this is going to be the index of our list!!
    cool_list = cool_list[:len(cool_list)-1]

    while (i<len(cool_list)):
         thisLine = cool_list[i] #Let's grab the current line
         comma = thisLine.rfind(",") #Let's also find the right comma - the one that seperates the number and value
         cool_dic[thisLine[:comma].strip('"')] = thisLine[comma + 1:].strip('\n').strip("\r") #Add the stuff before the comma (occupation) to the dictionary as a key, then add the stuff after the comma as a value!
         i += 1 #Wouldn't want an infinite loop now would we
    return cool_dic

def random_occupation():
    cool_dic = formattedOccs()
    c = 0 #counter for while loop
    random_float = random.uniform(0.0, 99.8) #float within range
    #print random_float
    cumulative_probability = 0.0
    while (c < len(cool_dic)):
        cumulative_probability += float(cool_dic.values()[c])
        if (cumulative_probability>random_float):
            return cool_dic.keys()[c]
        c += 1

@app.route("/occupations")
def occuWorked():
    return render_template("skeleeto`n.html", tl = "Occupations", heading = "Future Occupation Options", d = formattedOccs(), r = random_occupation())




if __name__ == "__main__":
    app.debug = True
    app.run()


