import numpy as np
from Ising import glauber
from Ising import magnetisation
import matplotlib.pyplot as plt


def vis(S, n):
    plt.ion()
    X, Y = np.meshgrid(range(n + 1), range(n + 1))
    plt.pcolormesh(X, Y, S, cmap=plt.cm.RdBu)
    plt.draw()
    plt.pause(0.00000000000001)
    plt.clf()


def run_glauber(S, v, n, temp, num):

    # size of one sweep
    sweep = n * n

    # number of spin flips
    spins = num*sweep

    # number of measurements to be taken
    meas = int((num-100)/10)

    # use j as a means to break the loop
    j = 0

    # initialise floats for magnetism and mangetism^2
    #mag = float(0)
    #magsq = float(0)
    mag = 0
    magsq = 0
    mag = np.zeros(meas)

    # run over total number of spins
    for t in range(spins):
        # apply the glauber method which will return the revised lattice
        #print("before")
        S = glauber(n, temp, S)
       # print("after")
        # if asked, run the visualisation
        #if v is True:
            # make the plot interactive
         #   plt.ion()
            # every so many sweeps plot the spins
          #  if t % 100 * n * n == 0:
           #     vis(S, n)

        # start recording the magnetisation after 100 sweeps
        if t == 100*sweep:
            # find the magnetisation
            M = np.sum(S)
            # record to mag/magsq
            mag[j] = np.abs(M)
            magsq += (M*M)
            # iterate the counting variable j
            j = j + 1

        # record magnetisation every 10 sweeps after the 100th sweep
        elif t > 100*sweep and t % (1 * sweep) == 0:
            M = magnetisation(n, n, S)
            mag[j] = np.abs(M)
            magsq += (M*M)
            j = j + 1
            #print(j)
        # break when we have recorded sufficient data (not necessary-->check)
        if j == meas:
            break

    # calculate susceptibility
    print("calculations")
    avmag = np.sum(mag) / meas
    avmagsq = magsq / meas
    suscep = (avmagsq - (avmag*avmag)) / (sweep * temp)

    # make an array of the useful data
    glaudat = [avmag, suscep]

    # output useful data
    return glaudat

