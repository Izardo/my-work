
import numpy as np
import matplotlib.pyplot as plt

# salary values
minSalary = 20000
maxSalary = 80000
count = 100

# age values
lowAge = 21
highAge = 65

# y = x(2)
x = np.array(range(1, 101))
y = x * x

# randominsing
np.random.seed(1)
randomSalaries = np.random.randint(minSalary, maxSalary, count)
randomAges = np.random.randint(lowAge, highAge, count) # another option: np.random.randint(low = 21, high = 65, size = 100)

# plotting data
plt.scatter(randomAges, randomSalaries, )
plt.plot(x, y, color = 'g')

# titling the plot
plt.title("Salary and Age")

# labelling the axes
plt.xlabel("Age")
plt.ylabel("Salary")

# adding a legend
plt.legend(["age", "salary"])

# display plot
plt.show()


plt.savefig('prettier-plot.png')
