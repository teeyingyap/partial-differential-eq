import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

d = 0.1
alpha = 5.
len_x = 100
len_y = 100
nt = 3000

dx = 1.0
dy = dx
dt = d*(dx**2.)/alpha
grid_x = int(len_x/dx)
grid_y = int(len_y/dy)

x = np.linspace(0,grid_x*dx,grid_x)
y = np.linspace(0,grid_y*dy,grid_y)


def fdm(T):
    T[:,0] = -10. #left
    T[-1,:] = 70.5 #top
    T[:,-1] = 40.5 #right
    #Neumann boundary condition at the bottom
    T[0,1:grid_x-1] = T[0,1:grid_x-1] + d*(T[0,2:grid_x]+T[0,0:grid_x-2] -4*T[0,1:grid_x-1]+T[1,1:grid_x-1]+T[1,1:grid_x-1])
    
    T[1:grid_y-1,1:grid_x-1] = T[1:grid_y-1,1:grid_x-1] + d*(T[1:grid_y-1,2:grid_x]+T[1:grid_y-1,0:grid_x-2] -4*T[1:grid_y-1,1:grid_x-1]+T[2:grid_y,1:grid_x-1]+T[0:grid_y-2,1:grid_x-1])
    return T

T = np.zeros((grid_x,grid_y))



T[:,0] = -10. #left
T[-1,:] = 70.5 #top
T[:,-1] = 40.5 #right


T[10:60,10:60] = 50. #initial cond
T[60:90,60:90] = -20. #initial cond

counter = 0
X,Y = np.meshgrid(x,y)
for n in range(0,nt):
    if n%30==0:
        print(dt*n)
        print(T)
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        hmmmm = ax.plot_surface(X,Y,T,cmap='rainbow',vmin=-22., vmax=72.)
        ax.set_xlim(0.,np.max(x))
        ax.set_ylim(0.,np.max(y))
        ax.set_zlim(-22.,90.)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('Temperature')
        ax.text2D(0.05, 0.95, f"Mixed boundary conditions after %.2f s"%(n*dt), transform=ax.transAxes)
        fig.colorbar(hmmmm)
        plt.savefig('mixbounds_%05.5d.png'%(counter))
        plt.clf()
        plt.cla()
    
    T = fdm(T)
    counter += 1
