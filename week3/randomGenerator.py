# this program prints out a random number betwen 1 and 10
# author Isabella Doyle

import random                                       # imports "random" module

num1 = int(input("Enter minimum number:"))          # requests input from use
num2 = int(input("Enter maximum number:"))

random = random.randint(num1, num2)                 # calls "random" function

print("Your random number is {}".format(random))    # prints random number