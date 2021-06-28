import numpy as np
from numpy.linalg import pinv


np.set_printoptions(precision = 2, sign = ' ', suppress = True)

X = np.array([[1,2014,5,1,45],
             [1,1416,3,2,40],
             [1,1534,3,2,30],
             [1,852,2,1,36]])

print(X)

Y = np.array([[460.],
              [232.],
              [315.],
              [178.]])

print(Y)

theta = pinv(X)@Y
print(X @ theta)
print(X @ theta == Y)
np.allclose(X @ theta, Y)
