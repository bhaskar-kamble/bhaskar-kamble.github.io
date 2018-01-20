#http://stackoverflow.com/questions/28074461/animating-growing-line-plot-in-python-matplotlib
#http://stackoverflow.com/questions/25689238/show-origin-axis-x-y-in-matplotlib-plot
#based on example_02ei.py

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

r = 15.0/37.0 #32.0/25.0#15.0/37.0
R = 1.0

fig = plt.figure()
if r<R:
   ax = plt.axes(xlim=(-R-0.1, R+0.1), ylim=(-R-0.1, R+0.1))
if r>R:
   ax = plt.axes( xlim=(-(2.0*r-R)-0.1, (2.0*r-R)+0.1), ylim=(-(2.0*r-R)-0.1, (2.0*r-R)+0.1))
#ax.grid(True,which="both") #for setting grid
ax.set_aspect("equal")     #for setting equal aspect ratio
ax.text(-0.6,-0.5,'$\copyright$2017, Bhaskar Kamble',fontsize=10,rotation=0)
ax.axis("off")              #

lines = []
# note-
lobj = ax.plot([],[],lw=1,color="black")[0] #fixed circle
lines.append(lobj)
lobj = ax.plot([],[],lw=2,color="red")[0]  #the hypocycloid
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",markersize=10,color="blue")[0] #fixed point
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",color="blue")[0] #fixed point
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",color="blue")[0] #fixed point
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",color="blue")[0] #fixed point
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",color="blue")[0] #fixed point
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",color="blue")[0] #fixed point
lines.append(lobj)
lobj = ax.plot([],[],lw=1,color="blue")[0] #line joining fixed points on circle
lines.append(lobj)
lobj = ax.plot([],[],lw=1,color="blue")[0] #line joining fixed points on circle
lines.append(lobj)
lobj = ax.plot([],[],lw=1,color="blue")[0] #line joining fixed points on circle
lines.append(lobj)








lobj = ax.plot([],[],lw=2,color="blue")[0] #moving circle
lines.append(lobj)


def init():
    for line in lines:
        line.set_data([],[])
    return lines


pi = np.pi


#x = np.linspace(0, 2, 1000)
#theta = np.linspace(0,20.0*pi,10000)
#theta = np.linspace(0,40.0*pi,20000)
#theta = np.linspace(0,64.0*pi,1600)
theta = np.linspace(0,30.0*pi,1500)
xd    = (R-r)*np.cos(theta) + r*np.cos((-1.0+R/r)*theta)
yd    = (R-r)*np.sin(theta) - r*np.sin((-1.0+R/r)*theta)
xdb    = (R-r)*np.cos(theta) + r*np.cos((-1.0+R/r)*theta+np.pi/3.0)
ydb    = (R-r)*np.sin(theta) - r*np.sin((-1.0+R/r)*theta+np.pi/3.0)
xdc    = (R-r)*np.cos(theta) + r*np.cos((-1.0+R/r)*theta+2.0*np.pi/3.0)
ydc    = (R-r)*np.sin(theta) - r*np.sin((-1.0+R/r)*theta+2.0*np.pi/3.0)
xdd    = (R-r)*np.cos(theta) + r*np.cos((-1.0+R/r)*theta+3.0*np.pi/3.0)
ydd    = (R-r)*np.sin(theta) - r*np.sin((-1.0+R/r)*theta+3.0*np.pi/3.0)
xde    = (R-r)*np.cos(theta) + r*np.cos((-1.0+R/r)*theta+4.0*np.pi/3.0)
yde    = (R-r)*np.sin(theta) - r*np.sin((-1.0+R/r)*theta+4.0*np.pi/3.0)
xdf    = (R-r)*np.cos(theta) + r*np.cos((-1.0+R/r)*theta+5.0*np.pi/3.0)
ydf    = (R-r)*np.sin(theta) - r*np.sin((-1.0+R/r)*theta+5.0*np.pi/3.0)


xc    = np.cos(theta)
yc    = np.sin(theta)
#y0 = np.sin(2 * np.pi * x)
#y1 = np.cos(2 * np.pi * x)




def animate(i):
    #x = np.linspace(0, 2, 1000)
    #y0 = np.sin(2 * np.pi * (x - 0.01 * i))
    #y1 = np.cos(2 * np.pi * (x - 0.01 * i))
    phi = np.linspace(0,2.0*pi,200)
    xco = (R-r)*xc[i]+r*np.cos(phi)
    yco = (R-r)*yc[i]+r*np.sin(phi)
    for lnum,line in enumerate(lines):
        if lnum==0:
            line.set_data(xc, yc)         #fixed circle
        if lnum==1:
            line.set_data(xd[:i], yd[:i]) #hypocycloid
        if lnum==2:                                       
            line.set_data(xd[i], yd[i]) # point fixed on circle
        if lnum==3:                                       
            line.set_data(xdb[i], ydb[i]) # point fixed on circle
        if lnum==4:                                       
            line.set_data(xdc[i], ydc[i]) # point fixed on circle
        if lnum==5:                                       
            line.set_data(xdd[i], ydd[i]) # point fixed on circle
        if lnum==6:                                       
            line.set_data(xde[i], yde[i]) # point fixed on circle
        if lnum==7:                                       
            line.set_data(xdf[i], ydf[i]) # point fixed on circle
        if lnum==8:
            line.set_data(np.array([xd[i],xdd[i]]),np.array([yd[i],ydd[i]])) #line joining fixed points on circle
        if lnum==9:
            line.set_data(np.array([xdb[i],xde[i]]),np.array([ydb[i],yde[i]])) #line joining fixed points on circle
        if lnum==10:
            line.set_data(np.array([xdc[i],xdf[i]]),np.array([ydc[i],ydf[i]])) #line joining fixed points on circle
        if lnum==11:
            line.set_data(xco,yco)                         # moving circle
    return lines

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=1499, interval=5, blit=True)


anim.save('hypo_r_15by37_spokes.mp4', fps=50, extra_args=['-vcodec', 'libx264'])
#anim.save("hypo_r_15by37_spokes.gif",dpi=80,writer='imagemagick')


plt.show()
