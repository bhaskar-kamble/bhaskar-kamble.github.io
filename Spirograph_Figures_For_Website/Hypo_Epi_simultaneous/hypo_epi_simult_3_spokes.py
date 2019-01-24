# based on hypo_epi_simult.py excecpt that introuces a phase lag in the hypocycloid


import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

#r = 1.28 #very nice picture
mr1 = 8.0
nr1 = 5.0
mr2 = 3.0
nr2 = 5.0
r1 = mr1/nr1 #32.0/25.0   # hypo with bigger circle   # mr1 = mr2 + nr2, nr1 = nr2
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
plotlays, plotcols = [2], ["black","red"]
lines = []

lobj = ax.plot([],[],lw=1,color="black")[0] # fixed circle
lines.append(lobj)
lobj = ax.plot([],[],lw=1,color="black")[0]   # curve 1
lines.append(lobj)



lobj = ax.plot([],[],lw=1,color="black",linestyle="dotted")[0]   # line joining points on the bigger circle
lines.append(lobj)
lobj = ax.plot([],[],lw=1,color="black",linestyle="dotted")[0]   # line joining points on the bigger circle
lines.append(lobj)
lobj = ax.plot([],[],lw=1,color="black",linestyle="dotted")[0]   # line joining points on the bigger circle
lines.append(lobj)
lobj = ax.plot([],[],lw=1,color="black",linestyle="dotted")[0]   # line joining points on the bigger circle
lines.append(lobj)



lobj = ax.plot([],[],linestyle="none",marker="o",markersize=10,color="red")[0] #fixed point on the bigger circle
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",markersize=5,color="red")[0] #fixed point on the bigger circle
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",markersize=5,color="red")[0] #fixed point on the bigger circle
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",markersize=5,color="red")[0] #fixed point on the bigger circle
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",markersize=5,color="red")[0] #fixed point on the bigger circle
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",markersize=5,color="red")[0] #fixed point on the bigger circle
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",markersize=5,color="red")[0] #fixed point on the bigger circle
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",markersize=5,color="red")[0] #fixed point on the bigger circle
lines.append(lobj)





lobj = ax.plot([],[],lw=2,color="red")[0]   #bigger circle
lines.append(lobj)
#weiter:---------------------
lobj = ax.plot([],[],lw=1,color="blue",linestyle="")[0] # curve 2
lines.append(lobj)
lobj = ax.plot([],[],lw=2,color="blue")[0]  # smaller circle
lines.append(lobj)
lobj = ax.plot([],[],lw=1,color="blue")[0]  # line joining points on smaller circle
lines.append(lobj)
lobj = ax.plot([],[],lw=1,color="blue")[0]  # line joining points on smaller circle
lines.append(lobj)
lobj = ax.plot([],[],lw=1,color="blue")[0]  # line joining points on smaller circle
lines.append(lobj)


lobj = ax.plot([],[],linestyle="none",marker="o",markersize=10,color="blue")[0] # point on the 2nd circle
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",markersize=5,color="blue")[0] # point on the 2nd circle
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",markersize=5,color="blue")[0] # point on the 2nd circle
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",markersize=5,color="blue")[0] # point on the 2nd circle
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",markersize=5,color="blue")[0] # point on the 2nd circle
lines.append(lobj)
lobj = ax.plot([],[],linestyle="none",marker="o",markersize=5,color="blue")[0] # point on the 2nd circle
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
theta = np.linspace(0.0,-2.0*mr1*pi,int(mr1*100.0))
xd1    = (R-r1)*np.cos(theta) + r1*np.cos((-1.0+R/r1)*theta)    #
yd1    = (R-r1)*np.sin(theta) - r1*np.sin((-1.0+R/r1)*theta)    #
xd1b    = (R-r1)*np.cos(theta) + r1*np.cos((-1.0+R/r1)*theta+pi/4.0)    #
yd1b    = (R-r1)*np.sin(theta) - r1*np.sin((-1.0+R/r1)*theta+pi/4.0)    #
xd1c    = (R-r1)*np.cos(theta) + r1*np.cos((-1.0+R/r1)*theta+2.0*pi/4.0)    #
yd1c    = (R-r1)*np.sin(theta) - r1*np.sin((-1.0+R/r1)*theta+2.0*pi/4.0)    #
xd1d    = (R-r1)*np.cos(theta) + r1*np.cos((-1.0+R/r1)*theta+3.0*pi/4.0)    #
yd1d    = (R-r1)*np.sin(theta) - r1*np.sin((-1.0+R/r1)*theta+3.0*pi/4.0)    #
xd1e    = (R-r1)*np.cos(theta) + r1*np.cos((-1.0+R/r1)*theta+4.0*pi/4.0)    #
yd1e    = (R-r1)*np.sin(theta) - r1*np.sin((-1.0+R/r1)*theta+4.0*pi/4.0)    #
xd1f    = (R-r1)*np.cos(theta) + r1*np.cos((-1.0+R/r1)*theta+5.0*pi/4.0)    #
yd1f    = (R-r1)*np.sin(theta) - r1*np.sin((-1.0+R/r1)*theta+5.0*pi/4.0)    #
xd1g    = (R-r1)*np.cos(theta) + r1*np.cos((-1.0+R/r1)*theta+6.0*pi/4.0)    #
yd1g    = (R-r1)*np.sin(theta) - r1*np.sin((-1.0+R/r1)*theta+6.0*pi/4.0)    #
xd1h    = (R-r1)*np.cos(theta) + r1*np.cos((-1.0+R/r1)*theta+7.0*pi/4.0)    #
yd1h    = (R-r1)*np.sin(theta) - r1*np.sin((-1.0+R/r1)*theta+7.0*pi/4.0)    #



xc    = np.cos(theta)                                       #
yc    = np.sin(theta)                                       #
#


#theta2 = np.linspace(0,12.0*pi,300)                         #
theta2 = np.linspace(0,2.0*mr2*pi,int(mr1*100.0))
xd2    = (R+r2)*np.cos(theta2) - r2*np.cos((1.0+R/r2)*theta2)    #
yd2    = (R+r2)*np.sin(theta2) - r2*np.sin((1.0+R/r2)*theta2)    #
xd2b    = (R+r2)*np.cos(theta2) - r2*np.cos((1.0+R/r2)*theta2+pi/3.0)    #
yd2b    = (R+r2)*np.sin(theta2) - r2*np.sin((1.0+R/r2)*theta2+pi/3.0)    #
xd2c    = (R+r2)*np.cos(theta2) - r2*np.cos((1.0+R/r2)*theta2+2.0*pi/3.0)    #
yd2c    = (R+r2)*np.sin(theta2) - r2*np.sin((1.0+R/r2)*theta2+2.0*pi/3.0)    #
xd2d    = (R+r2)*np.cos(theta2) - r2*np.cos((1.0+R/r2)*theta2+3.0*pi/3.0)    #
yd2d    = (R+r2)*np.sin(theta2) - r2*np.sin((1.0+R/r2)*theta2+3.0*pi/3.0)    #
xd2e    = (R+r2)*np.cos(theta2) - r2*np.cos((1.0+R/r2)*theta2+4.0*pi/3.0)    #
yd2e    = (R+r2)*np.sin(theta2) - r2*np.sin((1.0+R/r2)*theta2+4.0*pi/3.0)    #
xd2f    = (R+r2)*np.cos(theta2) - r2*np.cos((1.0+R/r2)*theta2+5.0*pi/3.0)    #
yd2f    = (R+r2)*np.sin(theta2) - r2*np.sin((1.0+R/r2)*theta2+5.0*pi/3.0)    #





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

    #    xlist = [xc,xd1,xd1,xd2,xd2]                   # note
    #    ylist = [yc,yd1,yd1,yd2,yd2]                   # note
    for lnum,line in enumerate(lines):
        if lnum==0:
            line.set_data(xc, yc)      #fixed circle
        if lnum==1:
            line.set_data(xd1, yd1) # 1st curve (xd1[:i] for curve traced till now)
        if lnum==2:
            line.set_data((xd1[i],xd1e[i]) , (yd1[i],yd1e[i])) # line joining points on bigger circle
        if lnum==3:
            line.set_data((xd1b[i],xd1f[i]) , (yd1b[i],yd1f[i])) # line joining points on bigger circle
        if lnum==4:
            line.set_data((xd1c[i],xd1g[i]) , (yd1c[i],yd1g[i])) # line joining points on bigger circle
        if lnum==5:
            line.set_data((xd1d[i],xd1h[i]) , (yd1d[i],yd1h[i])) # line joining points on bigger circle
        if lnum==6:
            line.set_data(xd1[i], yd1[i]) # fixed point on the bigger circle
        if lnum==7:
            line.set_data(xd1b[i], yd1b[i]) # fixed point on the bigger circle
        if lnum==8:
            line.set_data(xd1c[i], yd1c[i]) # fixed point on the bigger circle
        if lnum==9:
            line.set_data(xd1d[i], yd1d[i]) # fixed point on the bigger circle
        if lnum==10:
            line.set_data(xd1e[i], yd1e[i]) # fixed point on the bigger circle
        if lnum==11:
            line.set_data(xd1f[i], yd1f[i]) # fixed point on the bigger circle
        if lnum==12:
            line.set_data(xd1g[i], yd1g[i]) # fixed point on the bigger circle
        if lnum==13:
            line.set_data(xd1h[i], yd1h[i]) # fixed point on the bigger circle
        if lnum==14:
            line.set_data(xco1,yco1)        # moving circle
        if lnum==15:
            line.set_data(xd2[:i], yd2[:i]) # 2nd curve
        if lnum==16:
            line.set_data(xco2,yco2)        # smaller moving circle
        if lnum==17:
            line.set_data((xd2[i],xd2d[i]),(yd2[i],yd2d[i]))        # line joining points on smaller moving circle
        if lnum==18:
            line.set_data((xd2b[i],xd2e[i]),(yd2b[i],yd2e[i]))        # line joining points on smaller moving circle
        if lnum==19:
            line.set_data((xd2c[i],xd2f[i]),(yd2c[i],yd2f[i]))        # line joining points on smaller moving circle
        if lnum==20:                                       #
            line.set_data(xd2[i], yd2[i]) # fixed point on the circle
        if lnum==21:                                       #
            line.set_data(xd2b[i], yd2b[i]) # fixed point on the circle
        if lnum==22:                                       #
            line.set_data(xd2c[i], yd2c[i]) # fixed point on the circle
        if lnum==23:                                       #
            line.set_data(xd2d[i], yd2d[i]) # fixed point on the circle
        if lnum==24:                                       #
            line.set_data(xd2e[i], yd2e[i]) # fixed point on the circle
        if lnum==25:                                       #
            line.set_data(xd2f[i], yd2f[i]) # fixed point on the circle




    return lines

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=theta.size, interval=5, blit=True)


#anim.save('hypo_epi_r1_32by25_r2_7by25_v2.mp4', fps=50, extra_args=['-vcodec', 'libx264'])
#anim.save("hypo_r_8by5_3by5_opp.gif",dpi=80,writer='imagemagick')#, fps=30)


plt.show()
