import numpy as np
import matplotlib.pyplot as plt

dt = 0.5
dx = 1.
u = 1.
max_x = 100.
nt = 2000
x = np.arange(0.,max_x+dx,dx)
print(x)
print("Courant Number:", u*dt/dx)

f = np.copy(x)
f[:] = 0.
f[(x>=40.)&(x<=60.)] = 1.

#initial distribution of f
#plt.plot(x,f)
#plt.show()


g = (f-np.roll(f,1,axis=0))/dx

if(u>=0):
    iup = -1
    dxiup = -1.0*dx
else:
    iup = 1
    dxiup = 1.0*dx

xi = -1.*u*dt

icounter = 0
for n in range(0,nt):
    if n*dt%10==0:
        plt.clf()
        plt.cla()
        plt.plot(x,f,color='black')
        plt.ylim([0.,1.2])
        plt.xlim([0.,100.])
        plt.title('Time: %04.3f'%(n*dt))
        plt.savefig('CIP2019t_%04d.png'%(n*dt))
    icounter+=1
    a = -2*(np.roll(f,-1*iup,axis=0)-f)/(dxiup)**3.+(g+np.roll(g,-1*iup,axis=0))/(dxiup**2.)
    b = -3*(f-np.roll(f,-1*iup,axis=0))/(dxiup)**2.-(2.*g+np.roll(g,-1*iup,axis=0))/dxiup
    f = a*xi**3.+b*xi**2.+g*xi+f
    g = 3*a*xi**2.+2*b*xi+g
