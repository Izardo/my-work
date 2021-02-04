# This program takes in a string and removes its 
# leading and trailing characters.
# It also converts the string to lower case characters.
# Finally, it outputs the length of both the original 
# string and the normalised string.

rawStr = input("Enter a string:")    # requests user for string input
normStr = rawStr.strip().lower()     # normalises inputed string

rawLen = len(rawStr)                 # calculates length of raw string
lenNorm = len(normStr)               # calculates length of normalised string

# prints normalised string
print("That String normalised is :{}".format(normStr))

# prints the amount of characters removed from raw string to normalised string
print("we reduced the input string from {} to {} characters".format(
rawLen, lenNorm ))