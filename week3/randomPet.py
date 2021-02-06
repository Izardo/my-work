# This program prints out a random pet 
# Author: Isabella

# imports the random function
import random

# creates a tuple containing various pets
petList = ('cat', 'dog', 'goldfish', 'hen', 'duck', 'llama', 'boyfriend', 'hamster', 'gerbil')

# selects a random pet from petList tuple
randomPet = random.choice(petList)

# print the random pet selected from petList
print("Your random pet is a {}.".format(randomPet))