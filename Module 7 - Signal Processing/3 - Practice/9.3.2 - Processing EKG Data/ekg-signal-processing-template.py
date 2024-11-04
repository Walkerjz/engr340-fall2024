from signal import signal

import matplotlib.pyplot as plt
import numpy as np

"""
Step 0: Select which database you wish to use.
"""

# database name
database_name = 'mitdb_201'

# path to ekg folder
path_to_folder = "../../../data/ekg/"

# select a signal file to run
signal_filepath = path_to_folder + database_name + ".csv"

"""
Step #1: load data in matrix from CSV file; skip first two rows. Call the data signal.
"""

signal = []
## YOUR CODE HERE ##
data = np.loadtxt(signal_filepath, delimiter= ',', skiprows=2)
time = data[:,0]
volt1 = data[:,1]
signal = volt1
plt.plot(volt1)
plt.xlabel("Time (s)")
plt.ylabel("Volt1")
plt.title("Plot of a ekg data raw")
plt.show()

"""
Step 2: (OPTIONAL) pass data through LOW PASS FILTER (fs=250Hz, fc=15, N=6). These may not be correctly in radians
"""

## YOUR CODE HERE ##

"""
Step 3: Pass data through weighted differentiator
"""

## YOUR CODE HERE ##
signal = np.diff(signal)
plt.plot(signal)
plt.xlabel("Time (s)")
plt.ylabel("Volt1 diff")
plt.title("Plot of a ekg data derivative")
plt.show()

"""
Step 4: Square the results of the previous step
"""
signal = np.square(signal)
plt.plot(signal)
plt.xlabel("Time (s)")
plt.ylabel("Volt1 sqr")
plt.title("Plot of a ekg data squared")
plt.show()
"""
Step 5: Pass a moving filter over your data
"""

signal = np.convolve(signal, np.ones(10)/10)

## YOUR CODE HERE
# make a plot of the results. Can change the plot() parameter below to show different intermediate signals
plt.title('Process Signal for ' + database_name + 'moving average filter applied')
plt.plot(signal)
plt.show()