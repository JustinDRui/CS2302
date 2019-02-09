#Justin Ruiloba
#Lab 1 Question 4
#2/7/2019
import numpy as np
import matplotlib.pyplot as plt
import math 
def circle(center,rad):
    n = int(4 * rad * math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad * np.sin(t)
    y = center[1]+rad * np.cos(t)
    return x,y
#end of circle function
def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        #initialize  left right bottom top as 2d array and divide radius by 3 because
		# radius divided by 3 = the inner circles radius
		radius = radius / 3
        left= [0,0]
        right= [0,0]
        bottom= [0,0]
        top= [0,0]
		
        #change left circles center X value by subtracting by radius of inner circle * 2 to the x values only to shift small circle to left of the smaller mid circle.
        left[0]=center[0]-(radius*2)
		#change left circles center Y value to the center of small circle Y value.
        left[1]=center[1]
		#change right circles center X value by adding by radius of inner circle * 2 to the x values only to shift small circle to right of the smaller mid circle.
        right[0]=center[0]+(radius*2)
		#change right circles center Y value to the center of small circle Y values. 
        right[1]=center[1]
		#change bottom center x values to the center of small circle x values.
        bottom[0]=center[0]
		#change bottom circles center  Y value only by subtracting by the radius of the inner circle * 2 to shift bottom below the smaller mid circle.
        bottom[1]=center[1]-(radius*2)
		#change top circles center  x value to the center of small circle x values.
        top[0]=center[0]
		#change top circles Y center value by radius * 2  to shift top above the smaller mid circle 
        top[1]=center[1]+(radius*2)
		#plot all inner circles(mid,left,right,bottom,top)
        ax.plot(x,y,color='k')
		#repeat draw for each inner circle as long as n-1 is greater than 0
        draw_circles(ax,n-1,center,radius,w)
        draw_circles(ax,n-1,left,radius,w)
        draw_circles(ax,n-1,right,radius,w)
        draw_circles(ax,n-1,bottom,radius,w)
        draw_circles(ax,n-1,top,radius,w)
#end of draw_circles function
#closes all plots      
plt.close("all") 
fig, ax = plt.subplots()
#draw circles call(ax,n,center,radius,weight) 
draw_circles(ax, 3, [100,0], 100,.9)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('circlesa.png')
#end of a

plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 4, [100,0], 100,.9)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('circlesb.png')

#end of b 
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 5, [100,0], 100,.9)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('circlesc.png')
exit;