import numpy as np

A = np.array([[1,2],[3,4],[5,6]])
B = np.array([[11,12],[13,14],[15,16]])
C = np.array([[1,1],[2,2]])

mult = np.dot(A,C)
mult = np.matmul(A,C)
mult = A@C
print(mult)

Element_wise = A*B
print(Element_wise)