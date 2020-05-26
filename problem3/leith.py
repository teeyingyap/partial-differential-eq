import numpy as np
import matplotlib.pyplot as plt

dt = 0.5
dx = 1. #fixed
u = 1. #fixed
max_x = 100.
nt = 10000
x = np.arange(0.,max_x+dx,dx)
#print(x)
print("Courant Number:", u*dt/dx)
#exit()
f = np.copy(x)
f[:] = 0.
f[(x>=40.)&(x<=60.)] = 1.


icounter = 0
for n in range(0,nt):
    if n*dt%10==0:
        plt.clf()
        plt.cla()
        plt.plot(x,f,color='black')
        plt.ylim([0.,1.2])
        plt.xlim([0.,100.])
        plt.title('Time: %04.3f'%(n*dt))
        plt.savefig('leith2019t_%04d.png'%(n*dt))
    icounter+=1
    c = f
    b = (np.roll(f,-1,axis=0)-np.roll(f,1,axis=0))/(2*dx)
    a = (np.roll(f,-1,axis=0)-2*f+np.roll(f,1,axis=0))/(2*dx**2)
    f = a*(u*dt)**2-b*(u*dt)+c
