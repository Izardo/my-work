# This program reads a students mark in percent and outputs
# the corresponding grade
# Author: Isabella Doyle

import math 

percentGrade = float(input("Enter your grade:"))

finalGrade = math.ceil(percentGrade)

if finalGrade < 0 or percentGrade > 100:
    print("Please enter a value between 1 and 100.")
elif finalGrade >= 70:
    print("Your grade is a Distinction.")
elif finalGrade >= 60:
    print("Your grade is a Merit.")
elif finalGrade >= 50:
    print("Your grade is a Merit 2.")
elif finalGrade >= 40:
    print("Your grade is a Pass.")
else:
    print("Your grade is a Fail.")