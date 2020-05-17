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

# Draw a circle on the canvas representing a singular joint in the truss
# with a set radius centered on the mouse position
def makeJoint(x,y):
    global radius 
    radius = 15
    canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill='#000')

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
