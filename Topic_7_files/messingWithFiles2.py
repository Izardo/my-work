# This program checks to see if a specific file exists
# if the file does not exist a file with that name is created

# Author: Isabella Doyle

import os.path
filename = "file.txt"

if os.path.isfile("file.txt"):
    print("This file already exists")
else:
    f = open(filename, "w+")
    print("New file created")

