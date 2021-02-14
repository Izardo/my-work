# This program determines whether or not a number is even 
# Author: Isabella Doyle

num = int(input("Enter a integer number: "))             # Requests the user to input number

if num % 2 == 0:                                        # Simple sum to determine whether the number is even
    print("The number {} is even." .format(num))        # This is printed if the statement is True
else:
    print("The number {} is not even." .format(num))    # This is printed if the statement is False