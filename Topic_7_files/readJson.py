# This program will read in a dict object from a json file
# Author: Isabella Doyle

import json

fileName = "testDict.json"

def readDict():
    with open(fileName) as f:
        return json.load(f)

# Test
read = readDict()
print(read)