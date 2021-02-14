# User guesses a randomly generated number, if 
# the guess is incorrect, the program gives hints
# Author: Isabella Doyle

from numpy import random

numberToGuess = random.randint(1, 100)

guess = int(input("Guess a number: "))

while guess != numberToGuess:
    print("You guessed wrong")
    if guess > numberToGuess:
        print("You need to guess lower")
    elif guess < numberToGuess:
        print("You need to guess higher")
    guess = int(input("Guess a number: "))

print("Yay! {} is the correct guess!".format(numberToGuess))