# combines hypo_epi_simult_2.py and epicycloid_subplots_try.py
# makes animations as in hypo_epi_simult_2.py and shows 2 of them side-by-side as subplots as in epicycloid_subplots_try.py

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

r1 = 32.0/25.0   # hypo with bigger circle
r2 = 7.0/25.0   # epicycloid
r3 = 32.0/25.0
r4 = 7.1/25.0
R = 1.0

fig, (ax1,ax2) = plt.subplots(1,2)
ax1.axis("off")
ax2.axis("off")
ax1.set_aspect("equal")
ax2.set_aspect("equal")
ax1.text(1.0,-0.5,'$\copyright$2017, Bhaskar Kamble',fontsize=10,rotation=0)
rR = 2.0*r1 - R
ax1.set_xlim(-(rR+0.1), rR+0.1)
ax1.set_ylim(-(rR+0.1), rR+0.1)
ax2.set_xlim(-(rR+0.1), rR+0.1)
ax2.set_ylim(-(rR+0.1), rR+0.1)

lines = []

line11 = ax1.plot([],[],lw=1,color="black")[0] #fixed circle
lines.append(line11)
line12 = ax1.plot([],[],lw=1,color="blue")[0]       #curve 1
lines.append(line12)
line13 = ax1.plot([],[],linestyle="none",marker="o",markersize=10,color="red")[0] #point on movingcircle 1
lines.append(line13)
line14 = ax1.plot([],[],lw=2,color="red")[0]        #moving circle 1
lines.append(line14)
line15 = ax1.plot([],[],lw=1,color="blue")[0]        #curve 2
lines.append(line15)
line16 = ax1.plot([],[],linestyle="none",marker="o",markersize=10,color="green")[0] # point on movingcircle 2
lines.append(line16)
line17 = ax1.plot([],[],lw=2,color="green")[0]       #movingcircle 2
lines.append(line17)
line21 = ax2.plot([],[],lw=1,color="black")[0] #fixed circle
lines.append(line21)
line22 = ax2.plot([],[],lw=1,color="blue")[0]       #curve 1
lines.append(line22)
line23 = ax2.plot([],[],linestyle="none",marker="o",markersize=10,color="red")[0] #point on movingcircle 1
lines.append(line23)
line24 = ax2.plot([],[],lw=2,color="red")[0]        #moving circle 1
lines.append(line24)
line25 = ax2.plot([],[],lw=1,color="blue")[0]        #curve 2
lines.append(line25)
line26 = ax2.plot([],[],linestyle="none",marker="o",markersize=10,color="green")[0] # point on movingcircle 2
lines.append(line26)
line27 = ax2.plot([],[],lw=2,color="green")[0]       #movingcircle 2
lines.append(line27)

def init():
    for line in lines:
        line.set_data([],[])
    return lines

pi = np.pi

##################################################################
theta1 = np.linspace(pi/4.0,64.0*pi+pi/4.0,1600)                 #
xc1    = np.cos(theta1)                                          #
yc1    = np.sin(theta1)                                          #
xd1    = (R-r1)*np.cos(theta1) + r1*np.cos((-1.0+R/r1)*theta1)   #
yd1    = (R-r1)*np.sin(theta1) - r1*np.sin((-1.0+R/r1)*theta1)   #
#                                                                #
theta2 = np.linspace(0,14.0*pi,1600)                             #
xc2    = np.cos(theta2)                                          #
yc2    = np.sin(theta2)                                          #
xd2    = (R+r2)*np.cos(theta2) - r2*np.cos((1.0+R/r2)*theta2)    #
yd2    = (R+r2)*np.sin(theta2) - r2*np.sin((1.0+R/r2)*theta2)    #
#                                                                #
theta3 = np.linspace(pi/4.0,64.0*pi+pi/4.0,1600)                 #
xc3    = np.cos(theta3)                                          #
yc3    = np.sin(theta3)                                          #
xd3    = (R-r3)*np.cos(theta3) + r3*np.cos((-1.0+R/r3)*theta3)   #
yd3    = (R-r3)*np.sin(theta3) - r3*np.sin((-1.0+R/r3)*theta3)   #
#                                                                #
theta4 = np.linspace(0,14.0*pi,1600)                             #
xc4    = np.cos(theta4)                                          #
yc4    = np.sin(theta4)                                          #
xd4    = (R+r4)*np.cos(theta4) - r4*np.cos((1.0+R/r4)*theta4)    #
yd4    = (R+r4)*np.sin(theta4) - r4*np.sin((1.0+R/r4)*theta4)    #
##################################################################

def animate(i):
    phi = np.linspace(0,2.0*pi,100)
    xco1 = (R-r1)*xc1[i]+r1*np.cos(phi)  # moving circle 1
    yco1 = (R-r1)*yc1[i]+r1*np.sin(phi)
    xco2 = (R+r2)*xc2[i]+r2*np.cos(phi)  # moving circle 2
    yco2 = (R+r2)*yc2[i]+r2*np.sin(phi)
    xco3 = (R-r3)*xc3[i]+r3*np.cos(phi)  # moving circle 3
    yco3 = (R-r3)*yc3[i]+r3*np.sin(phi)
    xco4 = (R+r4)*xc4[i]+r4*np.cos(phi)  # moving circle 4
    yco4 = (R+r4)*yc4[i]+r4*np.sin(phi)

    xlist = [xc1,xd1,xd1,xco1,xd2,xd2,xco2,xc3,xd3,xd3,xco3,xd4,xd4,xco4]
    ylist = [yc1,yd1,yd1,yco1,yd2,yd2,yco2,yc3,yd3,yd3,yco3,yd4,yd4,yco4]

    for lnum,line in enumerate(lines):
        if lnum==0:
            line.set_data(xlist[lnum], ylist[lnum])      #fixed circle
        if lnum==1:
            line.set_data(xlist[lnum][:i], ylist[lnum][:i]) # curve
        if lnum==2:                                       #
            line.set_data(xlist[lnum][i], ylist[lnum][i]) # point on the curve
        if lnum==3:
            line.set_data(xlist[lnum],ylist[lnum])  # moving circle
        if lnum==4:
            line.set_data(xlist[lnum][:i],ylist[lnum][:i]) #curve
        if lnum==5:                                       #
            line.set_data(xlist[lnum][i], ylist[lnum][i]) # point on the curve
        if lnum==6:
            line.set_data(xlist[lnum],ylist[lnum])  # moving circle
        if lnum==7:
            line.set_data(xlist[lnum], ylist[lnum])      #fixed circle
        if lnum==8:
            line.set_data(xlist[lnum][:i], ylist[lnum][:i]) # curve
        if lnum==9:                                       #
            line.set_data(xlist[lnum][i], ylist[lnum][i]) # point on the curve
        if lnum==10:
            line.set_data(xlist[lnum],ylist[lnum])  # moving circle
        if lnum==11:
            line.set_data(xlist[lnum][:i],ylist[lnum][:i]) #curve
        if lnum==12:                                       #
            line.set_data(xlist[lnum][i], ylist[lnum][i]) # point on the curve
        if lnum==13:
            line.set_data(xlist[lnum],ylist[lnum])  # moving circle
    return lines


anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=1600, interval=5, blit=True)

anim.save('hypo_epi_r1_32by25_r2_7by25_7p1_by_25.mp4', fps=50, extra_args=['-vcodec', 'libx264'])
#anim.save("hypo_r_2by5_3by5_R_interval5_2pi_50_v2_3.gif",dpi=80,writer='imagemagick')#, fps=30)
plt.show()
