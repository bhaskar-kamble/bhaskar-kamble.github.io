#http://stackoverflow.com/questions/28074461/animating-growing-line-plot-in-python-matplotlib
#http://stackoverflow.com/questions/25689238/show-origin-axis-x-y-in-matplotlib-plot
#based on example_02ei.py

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

r = 2.0/5.0
R = 1.0

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2)
#ax = plt.axes(xlim=(-(R+2.0*r), R+2.0*r), ylim=(-(R+2.0*r), R+2.0*r))
###ax.grid(True,which="both") #for setting grid
#ax.set_aspect("equal")     #for setting equal aspect ratio
#ax.axis("off")              #

R  = 1.0
r1 = R/5.0
r2 = 2.0*R/5.0
r3 = 3.0*R/5.0
r4 = 4.0*R/5.0

ax1.axis("off")
ax2.axis("off")
ax3.axis("off")
ax4.axis("off")
ax1.set_aspect("equal")
ax2.set_aspect("equal")
ax3.set_aspect("equal")
ax4.set_aspect("equal")
ax1.text(1.0,-1.6,'$\copyright$2017, Bhaskar Kamble',fontsize=10,rotation=0)
#ax2.text(-1.5,1.475,'$\copyright$2017, Bhaskar Kamble',fontsize=9,rotation=0)
#ax3.text(-1.5,-2.0,'$\copyright$2017, Bhaskar Kamble',fontsize=9,rotation=0)
#ax4.text(-1.5,-2.0,'$\copyright$2017, Bhaskar Kamble',fontsize=9,rotation=0)
ax1.set_xlim(-(R+2.1*r1), R+2.1*r1)
ax2.set_xlim(-(R+2.1*r2), R+2.1*r2)
ax3.set_xlim(-(R+2.1*r3), R+2.1*r3)
ax4.set_xlim(-(R+2.1*r4), R+2.1*r4)
ax1.set_ylim(-(R+2.1*r1), R+2.1*r1)
ax2.set_ylim(-(R+2.1*r2), R+2.1*r2)
ax3.set_ylim(-(R+2.1*r3), R+2.1*r3)
ax4.set_ylim(-(R+2.1*r4), R+2.1*r4)

lines = []

line11 = ax1.plot([],[],lw=1,color="black")[0] #fixed circle
lines.append(line11)
line12 = ax1.plot([],[],lw=1,color="blue")[0]  #curve
lines.append(line12)
line13 = ax1.plot([],[],linestyle="none",marker="o",color="red")[0] #point on movingcircle
lines.append(line13)
line14 = ax1.plot([],[],lw=1,color="red")[0]   #moving circle
lines.append(line14)
line21 = ax2.plot([],[],lw=1,color="black")[0] #fixed circle
lines.append(line21)
line22 = ax2.plot([],[],lw=1,color="blue")[0]  #curve
lines.append(line22)
line23 = ax2.plot([],[],linestyle="none",marker="o",color="red")[0] #point on movingcircle
lines.append(line23)
line24 = ax2.plot([],[],lw=1,color="red")[0]   #moving circle
lines.append(line24)
line31 = ax3.plot([],[],lw=1,color="black")[0] #fixed circle
lines.append(line31)
line32 = ax3.plot([],[],lw=1,color="blue")[0]  #curve
lines.append(line32)
line33 = ax3.plot([],[],linestyle="none",marker="o",color="red")[0] #point on movingcircle
lines.append(line33)
line34 = ax3.plot([],[],lw=1,color="red")[0]   #moving circle
lines.append(line34)
line41 = ax4.plot([],[],lw=1,color="black")[0] #fixed circle
lines.append(line41)
line42 = ax4.plot([],[],lw=1,color="blue")[0]  #curve
lines.append(line42)
line43 = ax4.plot([],[],linestyle="none",marker="o",color="red")[0] #point on movingcircle
lines.append(line43)
line44 = ax4.plot([],[],lw=1,color="red")[0]   #moving circle
lines.append(line44)

def init():
    for line in lines:
        line.set_data([],[])
    return lines

pi = np.pi

###################################################################
theta1 = np.linspace(0,8.0*pi,800) #fps=50 in anim.save is fine   #
xc1    = np.cos(theta1)                                           #
yc1    = np.sin(theta1)                                           #
xd1    = (R+r1)*np.cos(theta1) - r1*np.cos((1.0+R/r1)*theta1)     #
yd1    = (R+r1)*np.sin(theta1) - r1*np.sin((1.0+R/r1)*theta1)     #
                                                                  #
theta2 = np.linspace(0,8.0*pi,800) #fps=50 in anim.save is fine   #
xc2    = np.cos(theta2)                                           #
yc2    = np.sin(theta2)                                           #
xd2    = (R+r2)*np.cos(theta2) - r2*np.cos((1.0+R/r2)*theta2)     #
yd2    = (R+r2)*np.sin(theta2) - r2*np.sin((1.0+R/r2)*theta2)     #
                                                                  #
theta3 = np.linspace(0,8.0*pi,800) #fps=50 in anim.save is fine   #
xc3    = np.cos(theta3)                                           #
yc3    = np.sin(theta3)                                           #
xd3    = (R+r3)*np.cos(theta3) - r3*np.cos((1.0+R/r3)*theta3)     #
yd3    = (R+r3)*np.sin(theta3) - r3*np.sin((1.0+R/r3)*theta3)     #
                                                                  #
theta4 = np.linspace(0,8.0*pi,800) #fps=50 in anim.save is fine   #
xc4    = np.cos(theta4)                                           #
yc4    = np.sin(theta4)                                           #
xd4    = (R+r4)*np.cos(theta4) - r4*np.cos((1.0+R/r4)*theta4)     #
yd4    = (R+r4)*np.sin(theta4) - r4*np.sin((1.0+R/r4)*theta4)     #
###################################################################

def animate(i):
    phi = np.linspace(0,2.0*pi,100)
    xco1 = (R+r1)*xc1[i]+r1*np.cos(phi)  # moving circle 1
    yco1 = (R+r1)*yc1[i]+r1*np.sin(phi)
    xco2 = (R+r2)*xc2[i]+r2*np.cos(phi)  # moving circle 2
    yco2 = (R+r2)*yc2[i]+r2*np.sin(phi)
    xco3 = (R+r3)*xc3[i]+r3*np.cos(phi)  # moving circle 3
    yco3 = (R+r3)*yc3[i]+r3*np.sin(phi)
    xco4 = (R+r4)*xc4[i]+r4*np.cos(phi)  # moving circle 4
    yco4 = (R+r4)*yc4[i]+r4*np.sin(phi)

    xlist = [xc1,xd1,xd1,xco1,xc2,xd2,xd2,xco2,xc3,xd3,xd3,xco3,xc4,xd4,xd4,xco4]
    ylist = [yc1,yd1,yd1,yco1,yc2,yd2,yd2,yco2,yc3,yd3,yd3,yco3,yc4,yd4,yd4,yco4]

    for lnum,line in enumerate(lines):
        for index in range(4):
            if lnum==4*index:
                line.set_data(xlist[lnum],ylist[lnum])  # fixed circle
            if lnum==4*index+1:
                line.set_data(xlist[lnum][:i],ylist[lnum][:i])  # curve
            if lnum==4*index+2:
                line.set_data(xlist[lnum][i],ylist[lnum][i])  # point on moving circle
            if lnum==4*index+3:
                line.set_data(xlist[lnum],ylist[lnum])  # moving circle
    return lines

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=799, interval=5, blit=True)

# look at http://matplotlib.org/examples/pylab_examples/subplots_demo.html to see why it's not working
#anim.save('epi_r_2by5_R.mp4', fps=100, extra_args=['-vcodec', 'libx264'])
anim.save("epi_subplots_samespeed_dpi50.gif",dpi=50,writer='imagemagick')#, fps=30)


plt.show()
