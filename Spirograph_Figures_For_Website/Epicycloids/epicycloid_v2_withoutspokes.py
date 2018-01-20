#http://stackoverflow.com/questions/28074461/animating-growing-line-plot-in-python-matplotlib
#http://stackoverflow.com/questions/25689238/show-origin-axis-x-y-in-matplotlib-plot
#based on example_02ei.py

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

mr = 2.0
nr = 7.0
r = mr/nr    # = (mr/nr)*R
R = 1.0

fig = plt.figure()
ax = plt.axes(xlim=(-(R+2.0*r)-0.08, R+2.0*r+0.08), ylim=(-(R+2.0*r)-0.08, R+2.0*r+0.08))
#ax.grid(True,which="both") #for setting grid
ax.set_aspect("equal")     #for setting equal aspect ratio
ax.text(-1.5,-2.0,'$\copyright$2017, Bhaskar Kamble',fontsize=10,rotation=0)
ax.axis("off")              #
plotlays, plotcols = [2], ["black","blue"]
lines = []
for index in range(2):  
    lobj = ax.plot([],[],lw=1,color=plotcols[index])[0]
    lines.append(lobj)
# note-
lobj = ax.plot([],[],linestyle="none",marker="o",color="red")[0]
lines.append(lobj)
lobj = ax.plot([],[],lw=1,color="red")[0]
lines.append(lobj)


def init():
    for line in lines:
        line.set_data([],[])
    return lines


pi = np.pi

###################################################################
theta = np.linspace(0,2.0*mr*pi,100*int(mr)) 
xd    = (R+r)*np.cos(theta) - r*np.cos((1.0+R/r)*theta)           #
yd    = (R+r)*np.sin(theta) - r*np.sin((1.0+R/r)*theta)           #
xc    = np.cos(theta)                                             #
yc    = np.sin(theta)                                             #
###################################################################



def animate(i):
    phi = np.linspace(0,2.0*pi,100) # DO NOT CHANGE !!!
    xco = (R+r)*xc[i]+r*np.cos(phi)
    yco = (R+r)*yc[i]+r*np.sin(phi)
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
                               frames=100*int(mr), interval=5, blit=True)


#anim.save('epi_r_2by5_R.mp4', fps=100, extra_args=['-vcodec', 'libx264'])
anim.save("epi_r_2by7.gif",dpi=80,writer='imagemagick')#, fps=30)


plt.show()
