#Justin Ruiloba
#Lab 1 
#2/7/2019
import matplotlib.pyplot as plt
import numpy as np
import math 
def circle(center,rad):
    n = int(4 * rad * math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad * np.sin(t)
    y = center[1]+rad * np.cos(t)
    return x,y
#end of circle function
	#draws circles plots circle using center and radius from circle method.
def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
		#plots circle
        ax.plot(x,y,color='k')
		#recursive call to self 
        draw_circles(ax,n-1,center,radius*w,w)
#end of draw_circles function
#makes sure all points are closed      
plt.close("all") 
fig, ax = plt.subplots()
#recursive call ax,n,center, radius ,w 
draw_circles(ax, 3, [10000,0], 100,.5)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('circles.png')
#end of a
#call again but this time change parameters to make picture look like b.
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 400, [10000,0], 100,.88)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('circles2.png')
#end of b
#call again but this time change parameters to make picture look like c.
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 1000, [1000,0], 1000,.99)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('circles3.png')