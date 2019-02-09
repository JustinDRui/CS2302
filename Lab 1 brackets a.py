import numpy as np
import matplotlib.pyplot as plt


def draw_squares(ax,n,p,w):
    if n>0:
        ax.plot(p[:,0],p[:,1],color='k')
        right=np.divide(p,1.75)
        left=np.divide(p,1.75)
        left[:,0]=left[:,0]-(orig_size*.29) #X Subtracted
        left[:,1]=left[:,1]-orig_size/1.75#math.sqrt(orig_size-(orig_size/2))  #Y Subtracted
        right[:,0]=right[:,0]+orig_size/1.4 #X Added
        right[:,1]=right[:,1]-orig_size/1.75#math.sqrt(orig_size-(orig_size/2))  #Y Subtracted
        #print("p",p)
        #print("left 0",left[:,0])
        #print("left 1",left[:,1])
       # print("right",right)
        draw_squares(ax,n-1,left,w)
        draw_squares(ax,n-1,right,w)

orig_size = 1000
p = np.array([[0,0],[orig_size/2,orig_size],[orig_size,0]])
fig, ax = plt.subplots()
draw_squares(ax,3,p,.5)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('triangles.png')
