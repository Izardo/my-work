# Generates 10 randomly generated numbers and 
# prints the top 3
# Author: Isabella Doyle

import random                               # imports the random function

numbers = []                                # list to append random numbers to

for r in range(0,10):
    numbers.append(random.randint(0, 100))  # random function chooses 10 random integers from 1 - 100
print("{} random numbers\t {}".format(10, numbers)) # prints the 10 random numbers

topList = numbers                           # copies the numbers list and stores in new variable - top3
sortedList = sorted(numbers)                # sorts the numbers 
amount = 3                                  # amount of objects I will select from the top3 list

print ("The top {} are \t\t {}".format(amount,topList[0:amount])) # prints the list of random numbers
                                                                  # followed by the top three numbers