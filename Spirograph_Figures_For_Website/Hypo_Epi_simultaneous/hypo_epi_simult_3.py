# based on hypo_epi_simult.py excecpt that introuces a phase lag in the hypocycloid


import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

#r = 1.28 #very nice picture
mr1 = 32.0
nr1 = 25.0
mr2 = 7.0
nr2 = 25.0
r1 = mr1/nr1 #32.0/25.0   # hypo with bigger circle
r2 = mr2/nr2 #7.0/25.0   # epicycloid
R = 1.0

fig = plt.figure()
#rR = R
#r = max(r1,r2)
#if r>R:
#    rR = 2.0*r - R

#ax = plt.axes(xlim=(-rR, rR), ylim=(-rR, rR))
rR = 2.0*r1 - R
ax = plt.axes(xlim=(-(rR+0.1), rR+0.1), ylim=(-(rR+0.1), rR+0.1))


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
lobj = ax.plot([],[],linestyle="none",marker="o",markersize=10,color="red")[0]
lines.append(lobj)
lobj = ax.plot([],[],lw=2,color="red")[0]
lines.append(lobj)
#weiter:---------------------
lobj = ax.plot([],[],lw=1,color="blue")[0] #path of the 2nd curve
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",markersize=10,color="green")[0] # point on the 2nd circle
lines.append(lobj)
lobj = ax.plot([],[],lw=2,color="green")[0]  # bewegender kreis
lines.append(lobj)


def init():
    for line in lines:
        line.set_data([],[])
    return lines


pi = np.pi


#x = np.linspace(0, 2, 1000)
#theta = np.linspace(0,20.0*pi,10000)
#############################################################
# for (0,2*pi), i.e. one rotation, take 100 points          #

#theta = np.linspace(pi/4.0,64.0*pi+pi/4.0,1600)
theta = np.linspace(0.0,2.0*mr1*pi,int(mr1*50.0))
xd1    = (R-r1)*np.cos(theta) + r1*np.cos((-1.0+R/r1)*theta)    #
yd1    = (R-r1)*np.sin(theta) - r1*np.sin((-1.0+R/r1)*theta)    #
xc    = np.cos(theta)                                       #
yc    = np.sin(theta)                                       #
#
#theta2 = np.linspace(0,12.0*pi,300)                         #
theta2 = np.linspace(0,2.0*mr2*pi,int(mr1*50.0))
xd2    = (R+r2)*np.cos(theta2) - r2*np.cos((1.0+R/r2)*theta2)    #
yd2    = (R+r2)*np.sin(theta2) - r2*np.sin((1.0+R/r2)*theta2)    #
xc2    = np.cos(theta2)                                       #
yc2    = np.sin(theta2)                                       #

#############################################################
#y0 = np.sin(2 * np.pi * x)
#y1 = np.cos(2 * np.pi * x)




def animate(i):
    #x = np.linspace(0, 2, 1000)
    #y0 = np.sin(2 * np.pi * (x - 0.01 * i))
    #y1 = np.cos(2 * np.pi * (x - 0.01 * i))
    phi = np.linspace(0,2.0*pi,100)
    xco1 = (R-r1)*xc[i]+r1*np.cos(phi)    #moving circle
    yco1 = (R-r1)*yc[i]+r1*np.sin(phi)
    xco2 = (R+r2)*xc2[i]+r2*np.cos(phi)
    yco2 = (R+r2)*yc2[i]+r2*np.sin(phi)

    xlist = [xc,xd1,xd1,xd2,xd2]                   # note
    ylist = [yc,yd1,yd1,yd2,yd2]                   # note
    for lnum,line in enumerate(lines):
        if lnum==0:
            line.set_data(xlist[lnum], ylist[lnum])      #fixed circle
        if lnum==1:
            line.set_data(xlist[lnum][:i], ylist[lnum][:i]) # curve
        if lnum==2:                                       #
            line.set_data(xlist[lnum][i], ylist[lnum][i]) # fixed point on the curve
        if lnum==3:
            line.set_data(xco1,yco1)        # moving circle
        if lnum==4:
            line.set_data(xlist[lnum-1][:i], ylist[lnum-1][:i]) # 2nd curve
        if lnum==5:                                       #
            line.set_data(xlist[lnum-1][i], ylist[lnum-1][i]) # fixed point on the curve
        if lnum==6:
            line.set_data(xco2,yco2)        # moving circle
    return lines

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=theta.size, interval=5, blit=True)


#anim.save('hypo_epi_r1_32by25_r2_7by25_v2.mp4', fps=50, extra_args=['-vcodec', 'libx264'])
#anim.save("hypo_r_2by5_3by5_R_interval5_2pi_50_v2_3.gif",dpi=80,writer='imagemagick')#, fps=30)


plt.show()
