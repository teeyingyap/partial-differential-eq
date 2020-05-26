import numpy as np
import matplotlib.pyplot as plt

dt = 1.
dx = 1.
u = 1.
max_x = 100.
nt = 2000
x = np.arange(0.,max_x+dx,dx)
# print(x)
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
        plt.savefig('analytical2019t_%04d.png'%(n*dt))
    icounter+=1
    f = np.roll(f,int(u*dt),axis=0)
