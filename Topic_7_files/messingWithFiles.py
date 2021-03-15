# This program reads in the number from a .txt file and adds one to the number
# everytime the program is run

# Author: Isabella Doyle

fileName = "count.txt"

def readCount():
    with open("count.txt", "r") as f:
        count = f.read()
        return count

def writeNum(num):
    with open ("count.txt", "wt") as f: # write takes a string
        f.write(str(num))               # must be converted to string
        return num

count = readCount()
count = int(count) + 1
currentCount = writeNum(count)
print("The program has been run {} times.".format(currentCount))