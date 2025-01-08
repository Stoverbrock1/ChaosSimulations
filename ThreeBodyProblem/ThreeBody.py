from matplotlib import pyplot as plt
import astropy.constants as ac
import numpy as np

def plotPast(xPast, yPast):

    plt.plot(xPast[0], yPast[0], color = 'green')
    plt.plot(xPast[1], yPast[1], color = 'red')
    plt.plot(xPast[2], yPast[2], color = 'blue')

#def distEq(coord0, coord1):
#    return round(np.sqrt((coord0[0] - coord1[0])**2 + ((coord0[1] - coord1[1])**2)) + 51, -2)

def distEq(coord0, coord1):
    return np.sqrt((coord0[0] - coord1[0])**2 + ((coord0[1] - coord1[1])**2))

def forceEq(m0, m1, coord0, coord1):
    r = distEq(coord0, coord1)
    #return -(ac.G.value*m0*m1)/(r**2)
    return -(m0*m1)/(r**2)

def yDist(coord0, coord1):
    return coord1[1] - coord0[1]

#def yDist(coord0, coord1):
#    return round(coord1[1] - coord0[1] + 51, -2)

def xDist(coord0, coord1):
    return coord1[0] - coord0[0]

#def xDist(coord0, coord1):
#    return round(coord1[0] - coord0[0] + 51, -2)

"""
PARAMETERS TO BE EDITED
"""

ANIMATE = True

#dt = 8640
dt = 1

#m0 = ac.M_sun.value
m0 = 1
#m1 = ac.M_earth.value
m1 = .5
#m2 = 7.34767309 * (10)**22
m2 = 1

#x0i = 0
x0i = 0
#x1i = 150e9
x1i =  6.135
#x2i = x1i
x2i = 15

y0i = 0
#y1i = -0
y1i =  5.7
#y2i = 384400000
y2i = 0

vel0, vel1, vel2 = [0, 0], [0, 30000], [1000, 30000]
#vel0, vel1, vel2 = [.932/2, .865/2], [-.932, -.865], [.932/2, .865/2]
vel0, vel1, vel2 = [0, 0], [0, 0], [0, 0]

SET_BOUNDS = True

XBounds = [-30, 30]
YBounds = [-30, 30]

tail_len = 10

iterations = 1000

save_img = False
img_name = 'FigEight1000Iterations.png'

"""
END OF PARAMETERS
"""

if __name__ == "__main__":
    xPast = [[x0i], [x1i], [x2i]]
    yPast = [[y0i], [y1i], [y2i]]

    loc0, loc1, loc2 = [x0i, y0i], [x1i, y1i], [x2i, y2i]
    newloc0, newloc1, newloc2 = [x0i, y0i], [x1i, y1i], [x2i, y2i]


    #plt.legend()
    for i in range(iterations):

        d01 = distEq(loc0, loc1)
        d02 = distEq(loc0, loc2)

        d12 = distEq(loc1, loc2)
        d10 = d01

        d20 = d02
        d21 = d12

        a0x = ((m1/(d01**3))*(loc1[0] - loc0[0]) + (m2/(d02**3))*(loc2[0] - loc0[0]))
        a0y = ((m1/(d01**3))*(loc1[1] - loc0[1]) + (m2/(d02**3))*(loc2[1] - loc0[1]))


        a1x = ((m2/(d12**3))*(loc2[0] - loc1[0]) + (m0/(d10**3))*(loc0[0] - loc1[0]))
        a1y = ((m2/(d12**3))*(loc2[1] - loc1[1]) + (m0/(d10**3))*(loc0[1] - loc1[1]))


        a2x = ((m0/(d20**3))*(loc0[0] - loc2[0]) + (m1/(d21**3))*(loc1[0] - loc2[0]))
        a2y = ((m0/(d20**3))*(loc0[1] - loc2[1]) + (m1/(d21**3))*(loc1[1] - loc2[1]))



        vel0[0] += a0x*dt
        vel0[1] += a0y*dt

        vel1[0] += a1x*dt
        vel1[1] += a1y*dt

        vel2[0] += a2x*dt
        vel2[1] += a2y*dt


        newloc0[0] = loc0[0] + vel0[0]*dt
        newloc0[1] = loc0[1] + vel0[1]*dt

        newloc1[0] = loc1[0] + vel1[0]*dt
        newloc1[1] = loc1[1] + vel1[1]*dt

        newloc2[0] = loc2[0] + vel2[0]*dt
        newloc2[1] = loc2[1] + vel2[1]*dt

        loc0, loc1, loc2 = newloc0, newloc1, newloc2
        xPast[0].append(loc0[0])
        xPast[1].append(loc1[0])
        xPast[2].append(loc2[0])

        yPast[0].append(loc0[1])
        yPast[1].append(loc1[1])
        yPast[2].append(loc2[1])
        print(len(xPast[0]))
        #print(vel1[0], vel1[1])

        # Mention x and y limits to define their range
        if (ANIMATE):
            #plt.xlim(-160e9, 160e9)
            #plt.ylim(-160e9, 160e9)
            if (SET_BOUNDS):
                plt.xlim(XBounds[0], XBounds[1])
                plt.ylim(YBounds[0], YBounds[1])

            # Ploting graph
            #include point for current location
            plt.scatter(xPast[0][-1:], yPast[0][-1:], color='green', s=4.5, label='m0 = ' + str(m0))
            plt.scatter(xPast[1][-1:], yPast[1][-1:], color='blue',  s=4.5, label='m1 = ' + str(m1))
            plt.scatter(xPast[2][-1:], yPast[2][-1:], color='red',   s=4.5, label='m2 = ' + str(m2))


            plt.plot(xPast[0][-tail_len:], yPast[0][-tail_len:],  'g-', linewidth=.75, label='m0 = ' + str(m0))
            plt.plot(xPast[1][-tail_len:], yPast[1][-tail_len:], 'b-', linewidth=.75, label='m1 = ' + str(m1))
            plt.plot(xPast[2][-tail_len:], yPast[2][-tail_len:], 'r-', linewidth=.75, label='m2 = ' + str(m2))


            #plt.plot(loc0[0], loc0[1], marker='.', markersize=.25, color='yellow')
            #plt.plot(loc1[0], loc1[1], marker='.', markersize=.25, color='.8')
            #plt.plot(loc2[0], loc2[1], marker='.', markersize=.25, color='black')
            #plt.plot(i, i, 'ro')
            plt.pause(0.00001)
            plt.cla()
    if (ANIMATE == False):
        plt.plot(xPast[0], yPast[0],  'g-', linewidth=.75, label='m0 = ' + str(m0))
        plt.plot(xPast[1], yPast[1], 'b-', linewidth=.75, label='m1 = ' + str(m1))
        plt.plot(xPast[2], yPast[2], 'r-', linewidth=.75, label='m2 = ' + str(m2))
        if (save_img):
            plt.savefig('./Images/' + img_name)
    plt.show()
