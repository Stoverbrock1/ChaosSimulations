from matplotlib import pyplot as plt
import astropy.constants as ac
import numpy as np

def plotPast(xPast, yPast):

    plt.plot(xPast[0], yPast[0], color = 'green')
    plt.plot(xPast[1], yPast[1], color = 'red')

def distEq(coord0, coord1):
    return round(np.sqrt((coord0[0] - coord1[0])**2 + ((coord0[1] - coord1[1])**2)), -2)

def forceEq(m0, m1, coord0, coord1):
    r = distEq(coord0, coord1)
    return -(m0*m1)/(r**2)

def yDist(coord0, coord1):
    return round(coord1[1] - coord0[1], -2)

def xDist(coord0, coord1):
    return round(coord1[0] - coord0[0], -2)


"""
PARAMETERS TO BE EDITED
"""

ANIMATE = True

dt = .5

m0 = 40000
m1 = 40000

x0i = 0
x1i = 800

y0i = 800
y1i = -0

vel0, vel1 = [5, 0], [0, 0]

iterations = 100000

"""
END OF PARAMETERS
"""

if __name__ == "__main__":
    xPast = [[x0i], [x1i]]
    yPast = [[y0i], [y1i]]

    loc0, loc1 = [x0i, y0i], [x1i, y1i]
    newloc0, newloc1 = [x0i, y0i], [x1i, y1i]


    #plt.legend()
    for i in range(iterations):
        r01 = distEq(loc0, loc1)

        a01 = abs(forceEq(m0, m1, loc0, loc1)/m0)

        a01x = a01*((xDist(loc0, loc1))/r01)
        a01y = a01*((yDist(loc0, loc1))/r01)


        a0x = a01x
        a0y = a01y

        vel0[0] += a0x*dt
        vel0[1] += a0y*dt

        newloc0[0] = loc0[0] + vel0[0]*dt
        newloc0[1] = loc0[1] + vel0[1]*dt

        a10 = abs(forceEq(m0, m1, loc0, loc1)/m1)

        a10x = a10*((xDist(loc1, loc0))/r01)
        a10y = a10*((yDist(loc1, loc0))/r01)


        a1x = a10x
        a1y = a10y

        vel1[0] += a1x*dt
        vel1[1] += a1y*dt

        newloc1[0] = loc1[0] + vel1[0]*dt
        newloc1[1] = loc1[1] + vel1[1]*dt


        loc0, loc1 = newloc0, newloc1

        xPast[0].append(loc0[0])
        xPast[1].append(loc1[0])


        yPast[0].append(loc0[1])
        yPast[1].append(loc1[1])

        print(vel1[0], vel1[1])

        # Mention x and y limits to define their range
        if (ANIMATE):
            plt.xlim(-3000, 3000)
            plt.ylim(-3000, 3000)

            # Ploting graph
            plt.plot(xPast[0], yPast[0],  'g-', linewidth=.75, label='m0 = ' + str(m0))
            plt.plot(xPast[1], yPast[1], 'b-', linewidth=.75, label='m1 = ' + str(m1))


            #plt.plot(loc0[0], loc0[1], 'go')
            #plt.plot(loc1[0], loc1[1], 'bo')
            #plt.plot(loc2[0], loc2[1], 'ro')
            #plt.plot(i, i, 'ro')
            plt.pause(0.00001)
    if (ANIMATE == False):
        plt.plot(xPast[0], yPast[0],  'g-', linewidth=.75, label='m0 = ' + str(m0))
        plt.plot(xPast[1], yPast[1], 'b-', linewidth=.75, label='m1 = ' + str(m1))

    plt.show()
