import numpy as np

a = [-1,1]
S = np.random.choice(a, size=(3,3))
T = S.copy()
print S
S[1,1] = 5

print S
print T
