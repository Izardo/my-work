# Messing around with numpy
# Author: Isabella Doyle

# imports mnumpy module
import numpy as np         # imports the numpy module
import matplotlib.pyplot as plt

# sets variables which will be input as parameters in randint generator
minSalary = 20000
maxSalary = 80000
count = 10

# seed method makes random numbers predictable
np.random.seed(0)        
# using the numpy randint method to produce 10 random numbers
salaries = np.random.randint(minSalary, maxSalary, count) 
print("Random salaries:")
print(salaries)   

# creates a new list which adds 5000 to each item in the salaries list
salariesPlus = salaries + 5000
print("Salaries with added 5000:")
print(salariesPlus)

# increases the salaries by 5 percent and floors each item to int array
salaryIncrease = (salaries * 1.05)
newSalaries = salaryIncrease.astype(int)
print("New salaries:")
print(newSalaries)

# seed modules ensures predictability of results
np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, count)# returns random integers based on the input parameters
# specifies the data to show on histogram
plt.hist(salaries)
# opens window which displays plot
plt.show()
