#Justin Ruiloba
#Lab 1 
#2/7/2019
#Import library numpy to create arrays.
import numpy as np
#Import matplotlib library to plot and create figures.
import matplotlib.pyplot as plt
#The method draw_squares takes in the axis(ax),
#The number of times to call recursive call(n),
#The points of the figure we are drawing four for square(p) + start point again to make sure figure is closed,and
#The weight of each point(w)
def draw_squares(ax,n,p,w):
    #Will run as long as n is greater than 0 
    if n>0:
        #      
        i1 = [1,2,3,0,1]
        #This line applies a  weight to each point.
        q = p*w + p[i1]*(1-w)
        #Plot the points as well as assign color
        ax.plot(p[:,0],p[:,1],color='k')
        #Recursive call q is now the new point values
        draw_squares(ax,n-1,q,w)

plt.close("all") 
orig_size =1000
#P the original points of figure
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
#Draws Figure
fig, ax = plt.subplots()
#Call to method
draw_squares(ax,10,p,.2)
#The scale of the figure
ax.set_aspect(1.0)
plt.show()
fig.savefig('squares.png')
#end of first fig
plt.close("all") 
orig_size =1000
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,10,p,.1)
ax.set_aspect(1.0)
plt.show()
fig.savefig('squares2.png')
#end of second fig
plt.close("all") 
orig_size =1000
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,150,p,.1)
ax.set_aspect(1.0)
plt.show()
fig.savefig('squares3.png')






