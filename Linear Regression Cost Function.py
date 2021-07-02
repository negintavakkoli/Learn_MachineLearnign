import numpy as np

def sse (X,y, theta):
    predictions = X @ theta
    errors =  predictions - y
    return 0.5 * np.sum(errors ** 2)
