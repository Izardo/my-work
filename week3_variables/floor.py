# Outputs a number rounded down to the nearest integer
# Author: Isabella Doyle

import math                             # imports math module

num = float(input("Enter a number:"))   # requests number input from user
floor = math.floor(num)                 # converts num to floored number

# prints the floored number
print("The floored number for {} is {}.".format(num, floor))