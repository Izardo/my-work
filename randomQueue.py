# This program outputs a list of 10 random integers
# using the pop function, it removes the int at index 0 
# printing the current list after each pop
# Author: Isabella Doyle

import random           # imports 'random' module
queue = []              # creates empty list
amountOfNumber = 10     # variable equals 10

# using a for loop and the random int generator to produce 10 random numbers
for i in range(0, 10):  
    queue.append(random.randint(0, 100))
# prints the list of random numbers    
print("The queue is {}".format(queue))

# using the while loop and pop module to remove the integer at index 0 and 
# print the current number and remaining numbers in the queue after each pop
while len(queue) != 0:        # while loop ends when list is empty
    currentNum = queue.pop(0) # assigns the popped number to a variable
    print("The current number is {} and the queue is {}".format(currentNum, queue))

print("The queue is now empty.")


