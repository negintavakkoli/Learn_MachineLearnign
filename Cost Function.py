#matplotlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.arange( -10 , 10.1 , 0.5 )
y = np.arange(-10,10.1,0.5)
print( x.shape )
print( x )

X, Y = np.meshgrid( x , y )
print(X.shape)

Z = X **2 + Y **2

fig = plt.figure(figsize = (12,8))
ax = fig.gca(projection = "3d")
surf = ax.plot_surface (X,Y,Z, cmap=plt.cm.rainbow)
cset = ax.contourf(X,Y,Z, zdir = "z", offset = 0, cmap=plt.cm.rainbow)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()