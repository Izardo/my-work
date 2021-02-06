# This program takes in a string and strips
# any leading or trailing spaces

original = (input("Enter a string:"))
normal = original.strip()

lenOriginal = len(original)
lenNormal = len(normal)

print("The original string was reduced from {} to {} characters.".format(lenOriginal, lenNormal))