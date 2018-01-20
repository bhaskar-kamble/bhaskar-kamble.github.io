#http://stackoverflow.com/questions/28074461/animating-growing-line-plot-in-python-matplotlib
#http://stackoverflow.com/questions/25689238/show-origin-axis-x-y-in-matplotlib-plot
#based on example_02ei.py

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

mr = 3.0
nr = 5.0
r = mr/nr    # = (mr/nr)*R
R = 1.0

fig = plt.figure()
ax = plt.axes(xlim=(-(R+2.0*r)-0.08, R+2.0*r+0.08), ylim=(-(R+2.0*r)-0.08, R+2.0*r+0.08))
#ax.grid(True,which="both") #for setting grid
ax.set_aspect("equal")     #for setting equal aspect ratio
ax.text(-1.5,-2.0,'$\copyright$2017, Bhaskar Kamble',fontsize=10,rotation=0)
ax.axis("off")              #

lines = []

lobj = ax.plot([],[],lw=1,color="black")[0]       # fixed circle
lines.append(lobj)
lobj = ax.plot([],[],lw=1,color="blue")[0]        # curve
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",color="red",markersize=10)[0] # fixed point on moving circle
lines.append(lobj)

lobj = ax.plot([],[],linestyle="none",marker="o",color="red",markersize=5)[0] # fixed point on moving circle
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",color="red",markersize=5)[0] # fixed point on moving circle
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",color="red",markersize=5)[0] # fixed point on moving circle
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",color="red",markersize=5)[0] # fixed point on moving circle
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",color="red",markersize=5)[0] # fixed point on moving circle
lines.append(lobj)


lobj = ax.plot([],[],lw=1,color="red")[0] #line joining fixed points on circle 
lines.append(lobj)
lobj = ax.plot([],[],lw=1,color="red")[0] #line joining fixed points on circle
lines.append(lobj)
lobj = ax.plot([],[],lw=1,color="red")[0] #line joining fixed points on circle
lines.append(lobj)








lobj = ax.plot([],[],lw=1,color="red")[0]         # moving circle
lines.append(lobj)


def init():
    for line in lines:
        line.set_data([],[])
    return lines


pi = np.pi

###################################################################
theta = np.linspace(0,2.0*mr*pi,200*int(mr)) 
xd    = (R+r)*np.cos(theta) - r*np.cos((1.0+R/r)*theta)           #
yd    = (R+r)*np.sin(theta) - r*np.sin((1.0+R/r)*theta)           #
xdb    = (R+r)*np.cos(theta) - r*np.cos((1.0+R/r)*theta+np.pi/3.0)           #
ydb    = (R+r)*np.sin(theta) - r*np.sin((1.0+R/r)*theta+np.pi/3.0)           #
xdc    = (R+r)*np.cos(theta) - r*np.cos((1.0+R/r)*theta+2.0*np.pi/3.0)           #
ydc    = (R+r)*np.sin(theta) - r*np.sin((1.0+R/r)*theta+2.0*np.pi/3.0)           #
xdd    = (R+r)*np.cos(theta) - r*np.cos((1.0+R/r)*theta+3.0*np.pi/3.0)           #
ydd    = (R+r)*np.sin(theta) - r*np.sin((1.0+R/r)*theta+3.0*np.pi/3.0)           #
xde    = (R+r)*np.cos(theta) - r*np.cos((1.0+R/r)*theta+4.0*np.pi/3.0)           #
yde    = (R+r)*np.sin(theta) - r*np.sin((1.0+R/r)*theta+4.0*np.pi/3.0)           #
xdf    = (R+r)*np.cos(theta) - r*np.cos((1.0+R/r)*theta+5.0*np.pi/3.0)           #
ydf    = (R+r)*np.sin(theta) - r*np.sin((1.0+R/r)*theta+5.0*np.pi/3.0)           #




xc    = np.cos(theta)                                             #
yc    = np.sin(theta)                                             #
###################################################################



def animate(i):
    phi = np.linspace(0,2.0*pi,100) # DO NOT CHANGE !!!
    xco = (R+r)*xc[i]+r*np.cos(phi)
    yco = (R+r)*yc[i]+r*np.sin(phi)
    for lnum,line in enumerate(lines):
        if lnum==0:
            line.set_data(xc, yc)  #fixed circle
        if lnum==1:
            line.set_data(xd[:i], yd[:i]) #curve
        if lnum==2:                          
            line.set_data(xd[i], yd[i]) #point on moving circle
        if lnum==3:                          
            line.set_data(xdb[i], ydb[i]) #point on moving circle
        if lnum==4:                          
            line.set_data(xdc[i], ydc[i]) #point on moving circle
        if lnum==5:                          
            line.set_data(xdd[i], ydd[i]) #point on moving circle
        if lnum==6:                          
            line.set_data(xde[i], yde[i]) #point on moving circle
        if lnum==7:                          
            line.set_data(xdf[i], ydf[i]) #point on moving circle
        if lnum==8:
            line.set_data(np.array([xd[i],xdd[i]]),np.array([yd[i],ydd[i]])) #line joining fixed points on circle
        if lnum==9:
            line.set_data(np.array([xdb[i],xde[i]]),np.array([ydb[i],yde[i]])) #line joining fixed points on circle
        if lnum==10:
            line.set_data(np.array([xdc[i],xdf[i]]),np.array([ydc[i],ydf[i]])) #line joining fixed points on circle
        if lnum==11:
            line.set_data(xco,yco) #moving circle
    return lines

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=theta.size, interval=5, blit=True)


#anim.save('epi_r_2by5_R.mp4', fps=100, extra_args=['-vcodec', 'libx264'])
#anim.save("epi_r_2by7.gif",dpi=80,writer='imagemagick')#, fps=30)


plt.show()
