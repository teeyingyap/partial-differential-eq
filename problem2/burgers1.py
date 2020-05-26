import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
#Investigate by modelling the differences when a (linear) is a constant and when a is u (non-linear) for a cyclic condition.
#set u to a small value like 2
#Decide on your own initial conditions and values for v
#advection is moving the thing
# for nonlinear the peak is faster 
a = 30.0 #constant a
v = 1. # this is the diffusion speed
lenx = 100
leny = 100
nt = 5000
dx = 1.0
dy = dx
dt = 0.01
d = (v*dt)/(dx**2) # for neumann stability i need to consider 0 to 0.25
#d= 0.01
#print(d)
f = (a*dt)/dx # f also has a range that you have to consider, which is will explained on thursday (less than 0.5)
# f = 0.3
#print(f)
#exit()
grid_x = int(lenx/dx)
grid_y = int(leny/dy)

x = np.linspace(0,grid_x*dx,grid_x)
y = np.linspace(0,grid_y*dy,grid_y)


def fdm(T):
#    f = (T*dt)/dx
    T = T + d*(np.roll(T,-1,axis=1) -4*T + np.roll(T,+1,axis=1) + np.roll(T,-1,axis=0) + np.roll(T,+1,axis=0)) -f*(2*T -np.roll(T,+1,axis=1) -np.roll(T,+1,axis=0))
    return T

#Initialization
T = np.zeros((grid_x,grid_y))

#Set initial condition
T[50:80,50:80] = 20.

counter = 0
X,Y = np.meshgrid(x,y)
for n in range(0,nt):
    if n%10==0:
#        print(dt*n)
#        print(T)
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        hmmmm = ax.plot_surface(X,Y,T,cmap='rainbow',vmin=0., vmax=25., rstride=3,cstride=3, linewidth=0.)
        ax.set_xlim(0.,np.max(x))
        ax.set_ylim(0.,np.max(y))
        ax.set_zlim(0.,25.)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('Velocity')
        ax.text2D(0.05, 0.95, f"Burgers' Equation Solution after %.2f s"%(n*dt), transform=ax.transAxes)
        fig.colorbar(hmmmm)
        plt.savefig('LINEARtestingshock_%05.5d.png'%(counter))
        plt.clf()
        plt.cla()

    T = fdm(T)
    counter += 1
