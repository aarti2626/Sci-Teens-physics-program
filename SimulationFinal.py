#SimulationFinal.py
import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

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

#instantiate particles based on particle 
def create_t(objecttype):
    tlist = [0]
    if objecttype == 'car':
        end = 5
        step = .01
    elif objecttype == 'ball':
        end = 2
        step = .005
    t = 0
    while t < end:
        t += step
        tlist.append(t)
    return tlist

#Car stuff
#conversion values for dimentional analysis
kmhh_to_mss = 7.2e-5
#Following values are for the Lamborghini Aventador S (base model)
a1_raw = 100/2.8 #km/h/s
a1_raw *= 3600 #km/h/h
a1 = a1_raw*kmhh_to_mss #m/s/s
p_lamborghini = particle(a1, 0, 0)

#Following values are for the Bugatti Veyron
a2_raw = 100/2.5 #km/h/s
a2_raw *= 3600 #km/h/h
a2 = a2_raw*kmhh_to_mss #m/s/s
p_bugatti = particle(a2, 0, 0)


#Ball stuff
#conversion values for dimensional analysis
kmhs_to_mss = .2778
mphs_to_mss = .4470
#Following values are for a baseball being pitched
a3_raw = 95 #km/h/s
a3 = a3_raw*kmhs_to_mss
p_baseball = particle(a3, 0, 0)
#Following values are for a golfball being hit
a4_raw = 211/2 #m/h/s
a4 = a4_raw*mphs_to_mss
p_golfball = particle(a4, 0, 0)
#use particle class to create array of x position based on initial values

# def data_gen(p1, p2, ptype):
#     t = create_t(ptype)
#     x1 = []
#     x2 = []
#     for i in t:
#         x1.append(p1.update(i))
#         x2.append(p2.update(i))

def var_gen(vartype):
    if vartype == 1:
        p1 = p_lamborghini
        p2 = p_bugatti
        end = 5
        step = .01
    elif vartype == 2:
        p1 = p_baseball
        p2 = p_golfball
        end = 2.5
        step = .005
    return p1, p2, end, step

#Based on object, involved, change input to function to 1 for cars and 2 for balls
p1, p2, end, step = var_gen(2)        

def data_gen():
    t = data_gen.t
    while t < end + step:
        t += step
        x1 = p1.update(t)
        x2 = p2.update(t)
        y = 5

        yield t, x1, x2, y
        
        
data_gen.t = 0
        
# create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2,1)

# intialize two line objects (one in each axes)
line1, = ax1.plot([], [], lw=2, color = 'b')
line2, = ax2.plot([], [], lw=2, color='c')
line = [line1, line2]

# the same axes initalizations as before (just now we do it for both of them)
for ax in [ax1, ax2]:
    ax.set_ylim(4.9, 5.1)
    ax.set_xlim(0, 100)
    ax.grid()

# initialize the data arrays 
x1data, x2data, ydata = [], [], []
tdata = []
def run(data):
    # update the data
    t, x1, x2, y = data
    x1data.append(x1)
    x2data.append(x2)
    ydata.append(y)
    tdata.append(t)

    # axis limits checking. Same as before, just for both axes
    for ax in [ax1, ax2]:
        xmin, xmax = ax.get_xlim()
        if t >= xmax:
            ax.set_xlim(xmin, 2*xmax)
            ax.figure.canvas.draw()

    # update the data of both line objects
    line[0].set_data(x1data, ydata)
    line[1].set_data(x2data, ydata)

    return line

ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=10,
    repeat=False)
plt.show()