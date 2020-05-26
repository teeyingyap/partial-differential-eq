import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


a = 30.0 #constant a
v = 1.0 # this is the diffusion speed
lenx = 100
leny = 100
nt = 5000
dx = 0.9
dy = dx
dt = 0.01
d = (v*dt)/(dx**2) # for neumann stability i need to consider 0 to 0.25
# d = 0.01
#print(d)
f = (a*dt)/dx # must be less than 0.5
# f = 0.3
#print(f)
#exit()

grid_x = int(lenx/dx)
grid_y = int(leny/dy)

x = np.linspace(0,grid_x*dx,grid_x)
y = np.linspace(0,grid_y*dy,grid_y)


def fdm(T):
    #Set Dirichlet boundary condition at the bottom side
    T[0,:] = 5.
    # Neumann at the top
    #    f = (T[grid_y-1,:]*dt)/dx #this work because T[grid_y-1,:] shape is (100), and f is also (100)
    f = (T*dt)/dx
    #    print(T.shape)
    #    print(T[1:grid_y-1,:].shape)
    T[grid_y-1,:] = T[grid_y-1,:] + d*(T[grid_y-1,:] -4*T[grid_y-1,:] + T[grid_y-1,:] + T[grid_y-2,:] + T[grid_y-2,:]) -f[grid_y-1,:]*(2*T[grid_y-1,:] -T[grid_y-1,:] - T[grid_y-2,:])
    
    T[1:grid_y-1,:] = T[1:grid_y-1,:] + d*(np.roll(T[1:grid_y-1,:],-1,axis=1) -4*T[1:grid_y-1,:] + np.roll(T[1:grid_y-1,:],+1,axis=1) + np.roll(T[2:grid_y,:],-1,axis=0) + np.roll(T[0:grid_y-2,:],+1,axis=0)) -f[1:grid_y-1,:]*(2*T[1:grid_y-1,:] -np.roll(T[1:grid_y-1,:],+1,axis=1) - np.roll(T[0:grid_y-2,:],+1,axis=0))
    return T
#    T[1:grid_y-1,1:grid_x-1] = T[1:grid_y-1,1:grid_x-1] + d*(T[1:grid_y-1,2:grid_x] -4*T[1:grid_y-1,1:grid_x-1] + T[1:grid_y-1,0:grid_x-2] + T[2:grid_y,1:grid_x-1] + T[0:grid_y-2,1:grid_x-1]) -f*(2*T[1:grid_y-1,1:grid_x-1] -T[1:grid_y-1,0:grid_x-2] -T[0:grid_y-2,1:grid_x-1])

#Initialization
T = np.zeros((grid_x,grid_y))
#Set initial condition
T[50:80,50:80] = 20.
T[0,:] = 5.

counter = 0
X,Y = np.meshgrid(x,y)
for n in range(0,nt):
    if n%10==0:
        print(dt*n)
        print(T)
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        hmmmm = ax.plot_surface(X,Y,T,cmap='rainbow',vmin=0., vmax=25., rstride=3,cstride=3, linewidth=0.)
        ax.set_xlim(0.,np.max(x))
        ax.set_ylim(0.,np.max(y))
        ax.set_zlim(0.,25.)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('Velocity')
        ax.text2D(0.05, 0.95, f"Non-Linear, dx = 0.9, a = 30., After %.2f s"%(n*dt), transform=ax.transAxes)
        fig.colorbar(hmmmm)
        plt.savefig('betternonlinresolution_%05.5d.png'%(counter))
        plt.clf()
        plt.cla()
    
    T = fdm(T)
    counter += 1

