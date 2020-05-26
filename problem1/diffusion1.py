import numpy as np
import matplotlib.pyplot as plt

len_x = 100.
len_y = 100.

dx = 1.
dy = dx
grid_x = int(len_x/dx)
grid_y = int(len_y/dy)

x = np.linspace(0.,grid_x*dx,grid_x)
y = np.linspace(0.,grid_y*dy,grid_y)

#TODO: modifying the RhoT value, the omega value, and the boundary conditions.
#Check if i change the rhot value or omega, how many iterations does it take to get to steady state
g = 9.81
rhoT = 0.001
omega = 1.9 #TODO: Estimate omega by trial and error
nk = 500

T = np.zeros((grid_x,grid_y))
#Set boundary condition
T[-1,:] = -10.  #Top
T[0,:] = 0.   #Bottom
T[:,0] = -10.   #left
T[:,-1] = -10.  #right
#set initial condition
T[50:80,50:80] = 20.


counter = 0
for k in range(0,nk):
    plt.clf()
    plt.cla()
    plt.contourf(x,y,T,cmap='nipy_spectral',levels=np.linspace(-70.,20.,30))
    plt.colorbar()
    plt.title('k=%04.4i'%(k))
    plt.savefig('cooledt_k_effect_%06.6i.png'%(counter))
    counter += 1
    for j in range(1,grid_y-1):
        for i in range(1,grid_x-1):
            R = 0.25*(T[j,i+1]+T[j,i-1]+T[j+1,i]+T[j-1,i]-g*rhoT*dx**2.)-T[j,i]
            T[j,i] = T[j,i]+omega*R
        print(R)


