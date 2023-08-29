# An alteration of Al Sweigart's Rotating Cube in The Big Book Of Small Python Projects, Project #62
# NOTE: If you want to use this as an import, make sure to create a newline after the animation is cancelled
# NOTE: This program can only be imported to other programs. If you want to run the program alone, remove the cube() func and take away the extra indent

import math
import time
import os

# Set up the constants:
PAUSE_AMOUNT = 0.01  # Pause length of one-tenth of a second.
WIDTH, HEIGHT = 80, 24
SCALEX = (WIDTH - 4) // 8
SCALEY = (HEIGHT - 4) // 8
SCALEY *= 2
TRANSLATEX = (WIDTH - 4) // 2
TRANSLATEY = (HEIGHT - 4) // 2
LINE_CHAR = chr(9608)  # Character 9608 is a solid block.
X_ROTATE_SPEED = 0.03
Y_ROTATE_SPEED = 0.08
Z_ROTATE_SPEED = 0.13
X = 0
Y = 1
Z = 2

def line(x1, y1, x2, y2):
    # Returns a list of points in a line between the given points.
    points = []  # Contains the points of the line.
    # "Steep" means the slope of the line is greater than 45 degrees or
    # less than -45 degrees:

    # Check for the special case where the start and end points are
    # certain neighbors, which this function doesn't handle correctly,
    # and return a hard coded list instead:
    if (x1 == x2 and y1 == y2 + 1) or (y1 == y2 and x1 == x2 + 1):
        return [(x1, y1), (x2, y2)]

    isSteep = abs(y2 - y1) > abs(x2 - x1)
    if isSteep:
        # This algorithm only handles non-steep lines, so let's change
        # the slope to non-steep and change it back later.
        x1, y1 = y1, x1  # Swap x1 and y1
        x2, y2 = y2, x2  # Swap x2 and y2
    isReversed = x1 > x2  # True if the line goes right-to-left.

    if isReversed:  # Get the points on the line going right-to-left.
        x1, x2 = x2, x1  # Swap x1 and x2
        y1, y2 = y2, y1  # Swap y1 and y2

        deltax = x2 - x1
        deltay = abs(y2 - y1)
        extray = int(deltax / 2)
        currenty = y2
        if y1 < y2:
            ydirection = 1
        else:
            ydirection = -1
        # Calculate the y for every x in this line:
        for currentx in range(x2, x1 - 1, -1):
            if isSteep:
                points.append((currenty, currentx))
            else:
                points.append((currentx, currenty))
            extray -= deltay
            if extray <= 0:  # Only change y once extray <= 0.
                currenty -= ydirection
                extray += deltax
    else:  # Get the points on the line going left to right.
        deltax = x2 - x1
        deltay = abs(y2 - y1)
        extray = int(deltax / 2)
        currenty = y1
        if y1 < y2:
            ydirection = 1
        else:
            ydirection = -1
        # Calculate the y for every x in this line:
        for currentx in range(x1, x2 + 1):
            if isSteep:
                points.append((currenty, currentx))
            else:
                points.append((currentx, currenty))
            extray -= deltay
            if extray < 0:  # Only change y once extray < 0.
                currenty += ydirection
                extray += deltax
    return points

def rotatePoint(x, y, z, ax, ay, az):
    """Returns an (x, y, z) tuple of the x, y, z arguments rotated.

    The rotation happens around the 0, 0, 0 origin by angles
    ax, ay, az (in radians).
        Directions of each axis:
         -y
          |
          +-- +x
         /
        +z
    """

    # Rotate around x axis:
    rotatedX = x
    rotatedY = (y * math.cos(ax)) - (z * math.sin(ax))
    rotatedZ = (y * math.sin(ax)) + (z * math.cos(ax))
    x, y, z = rotatedX, rotatedY, rotatedZ

    # Rotate around y axis:
    rotatedX = (z * math.sin(ay)) + (x * math.cos(ay))
    rotatedY = y
    rotatedZ = (z * math.cos(ay)) - (x * math.sin(ay))
    x, y, z = rotatedX, rotatedY, rotatedZ

    # Rotate around z axis:
    rotatedX = (x * math.cos(az)) - (y * math.sin(az))
    rotatedY = (x * math.sin(az)) + (y * math.cos(az))
    rotatedZ = z

    return (rotatedX, rotatedY, rotatedZ)

def adjustPoint(point):
    """Adjusts the 3D XYZ point to a 2D XY point fit for displaying on
    the screen. This resizes this 2D point by a scale of SCALEX and
    SCALEY, then moves the point by TRANSLATEX and TRANSLATEY."""
    return (int(point[X] * SCALEX + TRANSLATEX),
            int(point[Y] * SCALEY + TRANSLATEY))

def cube():
    CUBE_CORNERS = [[-1, -1, -1], [1, -1, -1], [-1, -1, 1], [1, -1, 1],
                    [-1, 1, -1], [1, 1, -1], [-1, 1, 1], [1, 1, 1]]
    rotatedCorners = [None, None, None, None, None, None, None, None]
    xRotation = 0.0
    yRotation = 0.0
    zRotation = 0.0

    try:
        while True:  # Main program loop.
            xRotation += X_ROTATE_SPEED
            yRotation += Y_ROTATE_SPEED
            zRotation += Z_ROTATE_SPEED
            for i in range(len(CUBE_CORNERS)):
                x = CUBE_CORNERS[i][X]
                y = CUBE_CORNERS[i][Y]
                z = CUBE_CORNERS[i][Z]
                rotatedCorners[i] = rotatePoint(x, y, z, xRotation,
                                                yRotation, zRotation)

            cubePoints = []
            for fromCornerIndex, toCornerIndex in ((0, 1), (1, 3), (3, 2), (2, 0),
                                                   (0, 4), (1, 5), (2, 6), (3, 7),
                                                   (4, 5), (5, 7), (7, 6), (6, 4)):
                fromX, fromY = adjustPoint(rotatedCorners[fromCornerIndex])
                toX, toY = adjustPoint(rotatedCorners[toCornerIndex])
                pointsOnLine = line(fromX, fromY, toX, toY)
                cubePoints.extend(pointsOnLine)

            cubePoints = tuple(frozenset(cubePoints))

            for y in range(HEIGHT):
                for x in range(WIDTH):
                    if (x, y) in cubePoints:
                        print(LINE_CHAR, end='', flush=False)
                    else:
                        print(' ', end='', flush=False)
                print(flush=False)
            print('Press Ctrl-C to quit.', end='', flush=True)
            time.sleep(PAUSE_AMOUNT)

            os.system('cls')

    except KeyboardInterrupt:
        pass  # When Ctrl-C is pressed, end the program.