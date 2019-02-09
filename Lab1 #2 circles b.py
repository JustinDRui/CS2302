import matplotlib.pyplot as plt
import numpy as np
import math 
def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        #add more radius/center = more separation
        newcenter=[0,0]
        newcenter[0]=center[0]/1.13
        newradius = radius/1.12
        draw_circles(ax,n-1,newcenter,newradius*w,w)
      
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 50, [100,0], 100,.99)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('circles.png')

 
