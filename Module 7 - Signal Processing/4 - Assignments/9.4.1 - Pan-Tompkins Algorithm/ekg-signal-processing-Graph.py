from signal import signal

import matplotlib.pyplot as plt
import numpy as np

"""
Step 0: Select which database you wish to use.
"""

# database name
database_name = 'mitdb_201'
database_name2 = 'nstdb_118e00'

# path to ekg folder
path_to_folder = "../../../data/ekg/"

# select a signal file to run
signal_filepath = path_to_folder + database_name + ".csv"
signal_filepath2 = path_to_folder + database_name2 + ".csv"
"""
Step #1: load data in matrix from CSV file; skip first two rows. Call the data signal.
"""

## YOUR CODE HERE ##
data = np.loadtxt(signal_filepath, delimiter= ',', skiprows=2)
signal = data[:,1]


data = np.loadtxt(signal_filepath2, delimiter= ',', skiprows=2)
signal2 = data[:,1]


signal = np.diff(signal)
signal2 = np.diff(signal2)


signal = np.square(signal)
signal2 = np.square(signal2)

signal = np.convolve(signal, np.ones(10)/10)
signal2 = np.convolve(signal2, np.ones(10)/10)
## YOUR CODE HERE
# make a plot of the results. Can change the plot() parameter below to show different intermediate signals
plt.ylabel("Volts")
plt.title('Process Signal for mitdb_201 (blue) and nstdb_118e00 (orange)' ) # + 'moving average filter applied')
plt.plot(signal)
plt.plot(signal2)
plt.show()