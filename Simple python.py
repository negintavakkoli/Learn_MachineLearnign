import math

import numpy as np

a = math.pi
# print(a)
# print("PI = %.2f" % a)
# print("PI = {:.6f}".format(a))
# print(dir(math))
# help(math.factorial)
A = np.array([[1,2],[3,4],[5,6]])
print(A[2,1])
print(A[:,:])
A[:,1] = [10,11,12]
print("----------------------------")
print(A[:,:])
v = np.array([[100 ,101]])
A = np.concatenate((A,v), axis = 0)
print(A)
print(A.ravel(order = "F"))