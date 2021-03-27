# creating my first plot
# Author: Isabella Doyle

import matplotlib.pyplot as plt
import numpy as np

# creates a numpy array
x = np.array(range(1, 101))
y = x * x   # multiplies each item by itself ( y = x(2) )

# specifies the data to display in plot
plt.plot(x, y)
# opens new window with the plot
plt.show()