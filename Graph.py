import matplotlib.pyplot as plt
import numpy as np


# load the data file
file = np.loadtxt('glauber.txt')

# get the temp, magnetism and susceptibility from the file
temp = file[:,0]
mag = file[:,1]
sus = file[:,2]

# plot the graph
plt.plot(temp, sus)
plt.show()
