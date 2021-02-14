# The user guesses a number until they guess correctly
# Author: Isabella Doyle

numberToGuess = 25

guess = int(input("Guess a number: "))

while guess != numberToGuess:
    print("Incorrect ")
    guess = int(input("Guess again! "))
else:
    print("That is correct! The number to guess was {}.".format(numberToGuess))

print("Thank you for playing")
