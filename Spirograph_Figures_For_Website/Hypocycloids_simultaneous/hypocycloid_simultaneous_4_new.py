#based on hypocycloid_simultaneous_2.py in this folder
#adds spokes and additional points on the circles
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

m_rad1=2.0
m_rad2=3.0
r1 = m_rad1/5.0   #2/5 and 3/5 give the same picture! 1/5 and 4/5 give the same picture!
r2 = m_rad2/5.0
R = 1.0

fig = plt.figure()
rR = R
r = max(r1,r2)
if r>R:
    rR = 2.0*r - R

ax = plt.axes(xlim=(-rR-0.1, rR+0.1), ylim=(-rR-0.1, rR+0.1))


#ax.grid(True,which="both")
ax.set_aspect("equal")
ax.text(-0.6,-0.5,'$\copyright$2017, Bhaskar Kamble',fontsize=10,rotation=0)
ax.axis("off")          
plotlays, plotcols = [2], ["black","blue"]
lines = []


lobj = ax.plot([],[],lw=1,color="black")[0]  #complete hypocycloid
lines.append(lobj)


lobj = ax.plot([],[],lw=1,color="black")[0]  #fixed circle
lines.append(lobj)
lobj = ax.plot([],[],lw=1,color="black",linestyle="")[0]   #hypocycloid 1
lines.append(lobj)

lobj = ax.plot([],[],linestyle="none",marker="o",markersize=10,color="blue")[0] #point on circle with radius r1
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",markersize=5,color="blue")[0] #point on circle with radius r1
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",markersize=5,color="blue")[0] #point on circle with radius r1
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",markersize=5,color="blue")[0] #point on circle with radius r1
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",markersize=5,color="blue")[0] #point on circle with radius r1
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",markersize=5,color="blue")[0] #point on circle with radius r1
lines.append(lobj)
lobj = ax.plot([],[],lw=1,color="blue")[0] #line joining fixed points on circle 1
lines.append(lobj)
lobj = ax.plot([],[],lw=1,color="blue")[0] #line joining fixed points on circle 1
lines.append(lobj)
lobj = ax.plot([],[],lw=1,color="blue")[0] #line joining fixed points on circle 1
lines.append(lobj)
lobj = ax.plot([],[],lw=1,color="blue")[0] #circle with radius r1 
lines.append(lobj)



lobj = ax.plot([],[],lw=1,color="black",linestyle="")[0] #hypocycloid 2
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",markersize=10,color="red")[0] # point on the 2nd circle
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",markersize=5,color="red")[0] # point on the 2nd circle
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",markersize=5,color="red")[0] # point on the 2nd circle
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",markersize=5,color="red")[0] # point on the 2nd circle
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",markersize=5,color="red")[0] # point on the 2nd circle
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",markersize=5,color="red")[0] # point on the 2nd circle
lines.append(lobj)
lobj = ax.plot([],[],lw=1,color="red")[0] #line joining fixed points on circle 2
lines.append(lobj)
lobj = ax.plot([],[],lw=1,color="red")[0] #line joining fixed points on circle 2
lines.append(lobj)
lobj = ax.plot([],[],lw=1,color="red")[0] #line joining fixed points on circle 2
lines.append(lobj)





lobj = ax.plot([],[],lw=1,color="red")[0]  # circle with radius r2
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
# circle 1
theta = np.linspace(0,2.0*m_rad1*pi,int(m_rad2*100.0))
xd1    = (R-r1)*np.cos(theta) + r1*np.cos((-1.0+R/r1)*theta)    #
yd1    = (R-r1)*np.sin(theta) - r1*np.sin((-1.0+R/r1)*theta)    #
xd1b    = (R-r1)*np.cos(theta) + r1*np.cos((-1.0+R/r1)*theta+np.pi/3.0)    #
yd1b    = (R-r1)*np.sin(theta) - r1*np.sin((-1.0+R/r1)*theta+np.pi/3.0)    #
xd1c    = (R-r1)*np.cos(theta) + r1*np.cos((-1.0+R/r1)*theta+2.0*np.pi/3.0)    #
yd1c    = (R-r1)*np.sin(theta) - r1*np.sin((-1.0+R/r1)*theta+2.0*np.pi/3.0)    #
xd1d    = (R-r1)*np.cos(theta) + r1*np.cos((-1.0+R/r1)*theta+np.pi)    #
yd1d    = (R-r1)*np.sin(theta) - r1*np.sin((-1.0+R/r1)*theta+np.pi)    #
xd1e    = (R-r1)*np.cos(theta) + r1*np.cos((-1.0+R/r1)*theta+4.0*np.pi/3.0)    #
yd1e    = (R-r1)*np.sin(theta) - r1*np.sin((-1.0+R/r1)*theta+4.0*np.pi/3.0)    #
xd1f    = (R-r1)*np.cos(theta) + r1*np.cos((-1.0+R/r1)*theta+5.0*np.pi/3.0)    #
yd1f    = (R-r1)*np.sin(theta) - r1*np.sin((-1.0+R/r1)*theta+5.0*np.pi/3.0)    #
xc    = np.cos(theta)                                       #
yc    = np.sin(theta)                                       #
#
#circle 2
theta2 = np.linspace(0,2.0*m_rad2*pi,int(m_rad2*100.0))
xd2    = (R-r2)*np.cos(theta2) + r2*np.cos((-1.0+R/r2)*theta2)    #
yd2    = (R-r2)*np.sin(theta2) - r2*np.sin((-1.0+R/r2)*theta2)    #
xd2b    = (R-r2)*np.cos(theta2) + r2*np.cos((-1.0+R/r2)*theta2+np.pi/3.0)    #
yd2b    = (R-r2)*np.sin(theta2) - r2*np.sin((-1.0+R/r2)*theta2+np.pi/3.0)    #
xd2c    = (R-r2)*np.cos(theta2) + r2*np.cos((-1.0+R/r2)*theta2+2.0*np.pi/3.0)    #
yd2c    = (R-r2)*np.sin(theta2) - r2*np.sin((-1.0+R/r2)*theta2+2.0*np.pi/3.0)    #
xd2d    = (R-r2)*np.cos(theta2) + r2*np.cos((-1.0+R/r2)*theta2+3.0*np.pi/3.0)    #
yd2d    = (R-r2)*np.sin(theta2) - r2*np.sin((-1.0+R/r2)*theta2+3.0*np.pi/3.0)    #
xd2e    = (R-r2)*np.cos(theta2) + r2*np.cos((-1.0+R/r2)*theta2+4.0*np.pi/3.0)    #
yd2e    = (R-r2)*np.sin(theta2) - r2*np.sin((-1.0+R/r2)*theta2+4.0*np.pi/3.0)    #
xd2f    = (R-r2)*np.cos(theta2) + r2*np.cos((-1.0+R/r2)*theta2+5.0*np.pi/3.0)    #
yd2f    = (R-r2)*np.sin(theta2) - r2*np.sin((-1.0+R/r2)*theta2+5.0*np.pi/3.0)    #

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
    xco2 = (R-r2)*xc2[i]+r2*np.cos(phi)
    yco2 = (R-r2)*yc2[i]+r2*np.sin(phi)

    for lnum,line in enumerate(lines):
        if lnum==0:
            line.set_data(xd1,yd1)      #complete hypocycloid
        if lnum==1:
            line.set_data(xc,yc)      #fixed circle
        if lnum==2:
            line.set_data(xd1[:i], yd1[:i]) # curve 1
        if lnum==3:                                       #
            line.set_data(xd1[i], yd1[i]) # fixed point on the circle 1
        if lnum==4:                                       #
            line.set_data(xd1b[i], yd1b[i]) # fixed point on the circle 1
        if lnum==5:                                       #
            line.set_data(xd1c[i], yd1c[i]) # fixed point on the circle 1
        if lnum==6:                                       #
            line.set_data(xd1d[i], yd1d[i]) # fixed point on the circle 1
        if lnum==7:                                       #
            line.set_data(xd1e[i], yd1e[i]) # fixed point on the circle 1
        if lnum==8:                                       #
            line.set_data(xd1f[i], yd1f[i]) # fixed point on the circle 1
        if lnum==9:
            line.set_data(np.array([xd1[i],xd1d[i]]),np.array([yd1[i],yd1d[i]])) #line joining fixed points on circle 1
        if lnum==10:
            line.set_data(np.array([xd1b[i],xd1e[i]]),np.array([yd1b[i],yd1e[i]])) #line joining fixed points on circle 1
        if lnum==11:
            line.set_data(np.array([xd1c[i],xd1f[i]]),np.array([yd1c[i],yd1f[i]])) #line joining fixed points on circle 1
        if lnum==12:
            line.set_data(xco1,yco1)        # moving circle 1
        if lnum==13:
            line.set_data(xd2[:i], yd2[:i]) # 2nd curve
        if lnum==14:                                       #
            line.set_data(xd2[i], yd2[i]) # fixed point on circle 2
        if lnum==15:                                       #
            line.set_data(xd2b[i], yd2b[i]) # fixed point on circle 2
        if lnum==16:                                       #
            line.set_data(xd2c[i], yd2c[i]) # fixed point on circle 2
        if lnum==17:                                       #
            line.set_data(xd2d[i], yd2d[i]) # fixed point on circle 2
        if lnum==18:                                       #
            line.set_data(xd2e[i], yd2e[i]) # fixed point on circle 2
        if lnum==19:                                       #
            line.set_data(xd2f[i], yd2f[i]) # fixed point on circle 2
        if lnum==20:
            line.set_data(np.array([xd2[i],xd2d[i]]),np.array([yd2[i],yd2d[i]])) #line joining fixed points on circle 2
        if lnum==21:
            line.set_data(np.array([xd2b[i],xd2e[i]]),np.array([yd2b[i],yd2e[i]])) #line joining fixed points on circle 2
        if lnum==22:
            line.set_data(np.array([xd2c[i],xd2f[i]]),np.array([yd2c[i],yd2f[i]])) #line joining fixed points on circle 2
        if lnum==23:
            line.set_data(xco2,yco2)        # moving circle 2
    return lines

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=int(m_rad2*100.0), interval=5, blit=True)


#anim.save('epi_r_1p6_R.mp4', fps=500, extra_args=['-vcodec', 'libx264'])
anim.save("hypo_r_2by5_3by5_R.gif",dpi=80,writer='imagemagick')#, fps=30)


plt.show()
