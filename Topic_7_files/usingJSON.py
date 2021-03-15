# This program will store a simple Dict to a file as JSON
# Author: Isabella Doyle

import json                 # imports the json module
import os                   # imports the os module

# Assigns a text file name to a variable 
fileName = "testDict.json" 
# Creates list and converts it to a dictionary
sampleDict = dict(name = "Isabella", surname = "Doyle", email = "isa@gmail.com") 

# If/else statement checks to see if the file specified in fileName exists
# If the file does not exist, it creates one by that name and opens it
if os.path.isfile("testDict.json"): 
    print("File already exists")
else:
    f = open("testDict.json", "w+")

# Defines a function which takes in one argument: obj
def jsonDump(obj):          
    with open(fileName, 'wt') as f:    # Opens file saved in the variable fileName in write text mode
        json.dump(obj, f)              # Takes in the values in sampleDict and saves them in the json file

# Calls the function with specified parameter
jsonDump(sampleDict)                  