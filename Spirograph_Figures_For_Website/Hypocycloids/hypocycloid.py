#http://stackoverflow.com/questions/28074461/animating-growing-line-plot-in-python-matplotlib
#http://stackoverflow.com/questions/25689238/show-origin-axis-x-y-in-matplotlib-plot
#based on example_02ei.py

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

r = 32.0/25.0#15.0/37.0
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
plotlays, plotcols = [2], ["black","blue"]
lines = []
for index in range(2):  
    lobj = ax.plot([],[],lw=1,color=plotcols[index])[0]
    lines.append(lobj)
# note-
lobj = ax.plot([],[],linestyle="none",marker="o",color="red")[0]
lines.append(lobj)
lobj = ax.plot([],[],lw=2,color="red")[0]
lines.append(lobj)


def init():
    for line in lines:
        line.set_data([],[])
    return lines


pi = np.pi


#x = np.linspace(0, 2, 1000)
#theta = np.linspace(0,20.0*pi,10000)
#theta = np.linspace(0,40.0*pi,20000)
theta = np.linspace(0,64.0*pi,1600)
xd    = (R-r)*np.cos(theta) + r*np.cos((-1.0+R/r)*theta)
yd    = (R-r)*np.sin(theta) - r*np.sin((-1.0+R/r)*theta)
xc    = np.cos(theta)
yc    = np.sin(theta)
#y0 = np.sin(2 * np.pi * x)
#y1 = np.cos(2 * np.pi * x)




def animate(i):
    #x = np.linspace(0, 2, 1000)
    #y0 = np.sin(2 * np.pi * (x - 0.01 * i))
    #y1 = np.cos(2 * np.pi * (x - 0.01 * i))
    phi = np.linspace(0,2.0*pi,1000)
    xco = (R-r)*xc[i]+r*np.cos(phi)
    yco = (R-r)*yc[i]+r*np.sin(phi)
    xlist = [xc,xd,xd]                   # note
    ylist = [yc,yd,yd]                   # note
    for lnum,line in enumerate(lines):
        if lnum==0:
            line.set_data(xlist[lnum], ylist[lnum])
        if lnum==1:
            line.set_data(xlist[lnum][:i], ylist[lnum][:i])
        if lnum==2:                                       # note
            line.set_data(xlist[lnum][i], ylist[lnum][i]) # note
        if lnum==3:
            line.set_data(xco,yco)
    return lines

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=1599, interval=5, blit=True)


anim.save('hypo_r_1pt28_R.mp4', fps=50, extra_args=['-vcodec', 'libx264'])
#anim.save("07_hypo_r_15by37_R.gif",dpi=80,writer='imagemagick')


plt.show()
