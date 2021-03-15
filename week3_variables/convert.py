# This program converts dollars to cents
# Author: Isabella Doyle

amount = round(float(input("Enter amount(USD):")),2)    # requests input of dollar amount & rounds to two dec. places
cents = int(amount * 100)   # converts dollars to integer and asssigns it to the variable cent

print(" {} dollars is {} cents.".format(amount, cents))