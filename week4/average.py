# Reads in numbers until 0 is input by user
# outputs the average of all input numbers
# Author: Isabella Doyle

numbers = []
number = int(input("Enter a number (Press 0 to quit): "))

while number != 0:
    numbers.append(number)
    number = int(input("Enter another number (Press 0 to quit): "))

for value in numbers:
    print(value)

average = float(sum(numbers)) / len(numbers)
print("The average of all number inputs is {}.".format(average))