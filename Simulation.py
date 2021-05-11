import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import matplotlib

class particle():
    def __init__(self, a, v0, y0):
        self.a = a
        self.v0 = v0
        self.v = v0
        self.y = y0
        self.y0 = y0
 
    def geta(self):
        return self.a
 
    def getv(self):
        return self.v
 
    def gety(self):
        return self.y
    
    def gett(self):
        return self.t

    def seta(self, a):
        self.a = a

    def setv(self,v):
        self.v = v
  
    def sety(self,y):
        self.y = y
    
   
    def update(self, t):
        self.sety((.5*self.a*t*t) + (self.v0*t) + (self.y0))
        return self.y

p1 = particle(-9.8, 25, 0)
x = np.arange(0, 10, 0.01)
y = p1.update(x)

fig = plt.figure()
ax = plt.subplot(1, 1, 1)

data_skip = 50


def init_func():
    ax.clear()
    plt.xlabel('time (seconds)')
    plt.ylabel('y position (m)')
    plt.xlim((x[0], x[-1]))
    plt.ylim((np.min(y), np.max(y)))


def update_plot(i):
    ax.plot(x[i:i+data_skip], y[i:i+data_skip], color='k')
    ax.scatter(x[i], y[i], marker='o', color='c')



anim = FuncAnimation(fig,
                     update_plot,
                     frames=np.arange(0, len(x), data_skip),
                     init_func=init_func,
                     interval=20)

matplotlib.animation.PillowWriter("Simulation1")

