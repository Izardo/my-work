# This program divides one number by a second number and outputs an integer and the remainder
# Author: Isabella Doyle

num1 = int(input("Enter first number:"))
num2 = int(input("Enter first number:"))

divSum = int(num1 // num2)
modulusSum = int(num1 % num2)

print("{} divided by {} equals {} with remainder {}.".format(num1, num2, divSum, modulusSum))