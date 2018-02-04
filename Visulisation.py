import numpy as np
from Glauber import run_glauber
import os


# set initial conditions for now
n = 50
delT = 0.1
temp = np.arange(0.1, 3, delT)

vis = False

# remove the glauber data file if it exists
os.remove('glauber.txt')

# randomly assign spins to the lattice
#a = [1, 1]
#S = np.random.choice(a, size=(n, n))
S = np.ones((n, n))
# define the number of sweeps that will be run at every temperature
num = 10000

# initialise the starting temperature
T = 0.1

# open the glauber data file
file = open("glauber.txt", "a")


# run the glauber method over a range of temperatures
for T in temp:
#    totmag = 0
#    totsus = 0
    # repeat the glauber method at every temperature
    #for i in range(3):
    print(T)
    dat = run_glauber(S, vis, n, T, num)
    #print("here")
    totmag = dat[0]
    totsus = dat[1]
    i = i + 1


    # average the results of mag and susceptibility
    avmag = totmag
    avsus = totsus

    # write the averages to the data file
    file.write("%s %s %s\n" % (float(T), float(avmag), float(avsus)))
    T = T + delT

# close the file
file.close()
exit()
