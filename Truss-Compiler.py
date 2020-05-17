#!/usr/bin/python3
import tkinter as tk
from math import *
tkinter = tk # Make is easier to reference tkinter

isShifted = False # Indicates if shift is held down
jointLocation = [] # Stores a list of all joint locations
joinSelectionCount = 0


def leftClick(event):
    x, y = event.x, event.y
    # Only create a joint if the shiftkey is not being held down
    if(isShifted == False):
        # Create the joint with the given location and append the center to the
        # list of joint locations
        makeJoint(x,y)
        global jointLocation
        jointLocation.append((x,y))
    else:
        if(whichJoint(x, y) is not None):
            initializeBeamSelection(whichJoint(x, y))

def whichJoint(curX, curY):
    for i, joint in enumerate(jointLocation):
        distanceX = (curX - joint[0])**2
        distanceY = (curY - joint[1])**2
        distance = sqrt(distanceX + distanceY)
        if(radius > distance):
            return joint         

def initializeBeamSelection(joint):
    print("you good")
    '''
    


    '''

def shift(event):
    # Invert shift detection when clicked
    global isShifted
    isShifted = not isShifted
    print("shift")

def getDistance(locationOne, locationTwo):
    xDistance = (locationOne[0] - locationTwo[0]) ** 2
    yDistance = (locationOne[1] - locationTwo[1]) ** 2
    return sqrt(xDistance + yDistance)


def getNearestGridLocation(x, y):
    radius = 15 # Remove after merge

    potentialXPositions = getGridLines(x)
    potentialYPositions = getGridLines(y)

    shortestDistance = getDistance((x, y), (potentialXPositions[0], potentialYPositions[0]))
    shortestPosition = (potentialXPositions[0], potentialYPositions[0])

    for potentialX in potentialXPositions: 
        for potentialY in potentialYPositions:
            potentialDistance = getDistance((x, y), (potentialX, potentialY))
            if potentialDistance < shortestDistance:
                shortestDistance = potentialDistance
                shortestPosition = (potentialX, potentialY)
    x, y = shortestPosition[0], shortestPosition[1]
    canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill='#F00')

def getGridLines(pos):
    gridSquareSize = 42
    pos -= (pos % gridSquareSize)
    return (pos, pos + gridSquareSize)

# Draw a circle on the canvas representing a singular joint in the truss
# with a set radius centered on the mouse position
def makeJoint(x,y):
    global radius 
    getNearestGridLocation(x,y)
    radius = 15
    # canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill='#000')

# Initialize the root window
root = tk.Tk()
root.wm_title("Truss Solver")

# Create the canvas and load it onto the root
canvas = tkinter.Canvas(root, width=850, height=850, background='gray')
canvas.grid(row=0, rowspan=2, column=1)
canvas.focus_set() # Capture key events on the canvas

# Bind events on the canvas
canvas.bind('<Button-1>', leftClick) # Primary mouse click
canvas.bind('<Shift_L>', shift) # Left shift click
canvas.bind('<KeyRelease-Shift_L>', shift) # Left shift release

# Execute the program
root.mainloop() # Nothing below this line gets executed
