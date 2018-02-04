import numpy as np


def total_energy(lx, ly, T):
        E = 0
        for i in range(lx):
            for j in range(ly):
                
                #impose periodic boundary conditions

                iup = i + 1

                if (i == lx - 1) : iup = 0

                jup = j + 1

                if (j == ly - 1) : jup = 0

                #calculate the energy of the lattice
                E += -T[i, j]*(T[iup, j] + T[i, jup])
        return E


def magnetisation(lx, ly, S):
    M = 0
    for i in range(lx):
        for j in range(ly):
            M += S[i, j]
    return M


def delE(lx, ly, S, x, y):

        #impose periodic boundary conditions

        iup = x + 1
        if x == lx - 1:
            iup = 0

        jup = y + 1
        if y == ly - 1:
            jup = 0

        idown = x -1
        if x == 0:
            idown = lx - 1

        jdown = y - 1
        if y == 0:
            jdown = ly - 1

        #calculate the energy change by performing one flip

        E = 2*S[x,y]*(S[x,jup]+S[x,jdown]+S[iup,y]+S[idown,y])

        return E


def glauber(n, temp, S):
        # create an array that will be used to randomly pick a lattice site
        b = np.arange(n)

        #randomly choose the lattice site
        x = np.random.choice(b)
        y = np.random.choice(b)

        #calculate the energy change in performing a flip at the random x,y

        D = delE(n, n, S, x, y)

        #perform the flip if delta E is negative or with some probability 

        rand = np.random.random_sample()
        prob = np.exp(-D/temp)

        if D <= 0:

                S[x, y] = -S[x, y]

        elif rand <= prob:
        
                S[x, y] = -S[x, y]

        #return the lattice after we have accepted or declined the flip
        
        return S


def kawasaki(n, temp, S):

    b = np.arange(n)
    x = np.random.choice(b)
    y = np.random.choice(b)
    u = np.random.choice(b)
    v = np.random.choice(b)

    delta = 0

    nn = 2 * S[x, y] * S[u, v]

    if (S[x, y] + S[u, v]) == 0:
        if x == u:
            if y == v + 1 or y == v - 1 or (y == 0 and v == n - 1) or (y == n-1 and v == 0):
                #nearest neighbor
                e1 = delE(n, n, S, x, y)
                e2 = delE(n, n, S, u, v)
                delta = e1 + e2 - 2*nn
                #print("nn")
                #return S
            else:
                e1 = delE(n, n, S, x, y)
                e2 = delE(n, n, S, u, v)
                delta = e1 + e2
                #print("same column")
        elif y == v:
            if x == u + 1 or x == u - 1 or (x == 0 and u == n - 1) or (x == n-1 and u == 0):
                #nearest neighbor
                e1 = delE(n, n, S, x, y)
                e2 = delE(n, n, S, u, v)
                delta = e1 + e2 - 2* nn
                #print("nn")
                #return S
            else:
                e1 = delE(n, n, S, x, y)
                e2 = delE(n, n, S, u, v)
                delta = e1 + e2
                #print("same row")
        else:
            e1 = delE(n, n, S, x, y)
            e2 = delE(n, n, S, u, v)
            delta = e1 + e2

        rand = np.random.random_sample()
        prob = np.exp(-delta / temp)

        if delta <= 0:
            S[x, y] = (-1)*S[x, y]
            S[u, v] = (-1)*S[u, v]

        elif rand <= prob:
            S[x, y] = (-1) * S[x, y]
            S[u, v] = (-1) * S[u, v]

        return S

    else:
        return S



