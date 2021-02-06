# This program converts dollars to cents
# Author: Isabella Doyle

amount = float(input("Enter amount(USD):"))  # requests input of dollar amount
cents = int(amount * 100)                    # convert dollars to cent

print(" {} dollars is {} cents.".format(amount, cents))