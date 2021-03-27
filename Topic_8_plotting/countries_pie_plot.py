# Author: Isabella Doyle

import numpy as np
import matplotlib.pyplot as plt

country = "Ireland", "England", "Scotland", "Wales", "France", "Germany"

# random selection of countries
np.random.seed(1)
randomCountry = np.random.choice (
    country , 
    p = [0.1, 0.2, 0.15, 0.05, 0.2, 0.3] ,
    size = (100)
)

# shows the unique items and frequency
unique, counts = np.unique(randomCountry, return_counts = True)

# creates a pie chart of the unique items and the frequency returned
plt.pie(counts, labels = unique)
plt.show()

'''# creates a bar plot
plt.bar(unique, counts)
plt.show()'''
