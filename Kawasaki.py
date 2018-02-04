import numpy as np
from Ising import kawasaki
from Ising import total_energy
import matplotlib.pyplot as plt


def vis(S, n):
    plt.ion()
    X, Y = np.meshgrid(range(n + 1), range(n + 1))
    plt.pcolormesh(X, Y, S, cmap=plt.cm.RdBu)
    plt.draw()
    plt.pause(0.00000000000001)
    plt.clf()


def run_kawasaki(S, v, n, temp, num):

    sweep = n * n
    #number of spin flips
    spins = num*sweep
    #number of measurements to be taken
    meas = int((num-100)/10)
    # initialise an array of size meas = number of measurements we will take
    #energy = [0] * num
    #use j as a means to break the loop
    #j = 0
    plt.ion()
    energy = float(0)
    energysq = float(0)
    # run over measurements (no. sweeps*how many measurements in a sweep)
    for t in range(spins):
        # apply the glauber method which will return the revised lattice
        S = kawasaki(n, temp, S)

        #if asked, run the visualisation
        if v is True:
            # every so many sweeps plot the spins
            if t % 100 * n * n == 0:
                vis(S, n)

        #start recording the magnetisation after 100 sweeps
        if t == 100*sweep:
            E = total_energy(n, n, S)
            energy += np.absolute(E)
            energysq += np.square(E)
           # energy[j] = total_energy(n, n, S)
            #iterate the counting variable j
        #    j = j + 1

        #record magnetisation every 10 sweeps after the 100th sweep
        elif t > 100*sweep and t % 10 * sweep == 0:
            E = total_energy(n, n, S)
            energy += np.absolute(E)
            energysq += np.square(E)
            #energy[j] = total_energy(n, n, S)
        #    j = j + 1

        #break when we have recorded sufficient data
        #if j == meas:
        #    break

    #calculate susceptibility
    avenergy = energy / meas
    avenergysq = energysq / meas
    specific = (avenergysq - np.square(avenergy)) / (spins * np.square(temp))

    kawadat = [avenergy, specific]

    return kawadat

