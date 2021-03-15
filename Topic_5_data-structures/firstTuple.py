# The first tuple stores the months of the year
# The second tuple store summer months the contents of 
# which are printed out one at a time using a for loop
# Author: Isabella Doyle 

# the variable "year" stores 12 months in a tuple
year = ("January", 
                "February", 
                "March", 
                "April", 
                "May", 
                "June", 
                "July", 
                "August", 
                "September", 
                "October", 
                "November", 
                "December")

# the summer variable contains the summer months indicated
# at index 4 through to 7 in the 'year' tuple
summer = year[4:7]
# uses the for loop to iterate through the summer months 
# and prints each out individually
for month in summer:
    print(month)