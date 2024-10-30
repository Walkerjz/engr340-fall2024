from importlib.resources import read_text

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import matplotlib_fname

# import the CSV file using numpy
path = '../../../data/ekg/mitdb_201.csv'

# load data in matrix from CSV file; skip first two rows
data = np.loadtxt(path, delimiter= ',', skiprows=2)
### Your code here ###
# save each vector as own variable

### Your code here ###
time = data[:,0]
volt1 = data[:,1]
volt2 = data[:,2]
pass

# use matplot lib to generate a single

### Your code here ###
plt.plot(time, volt1)
plt.xlabel("Time (s)")
plt.ylabel("Volt1")
plt.title("Plot of a ekg data")
plt.show()

plt.plot(time, volt2)
plt.xlabel("Time ")
plt.ylabel("Volt2")
plt.title("Plot of a ekg data")
plt.show()
pass