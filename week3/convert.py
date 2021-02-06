# This program converts dollars to cents
# Author: Isabella Doyle

amount = round(float(input("Enter amount(USD):")),2)  # requests input of dollar amount
cents = int(amount * 100)                             # convert dollars to cent

print(" {} dollars is {} cents.".format(amount, cents))