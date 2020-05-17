#!/usr/bin/python3
import tkinter as tk
tkinter = tk # Make is easier to reference tkinter

shift = False # Indicates if shift is held down
jointLocation = [] # Stores a list of all joint locations

def leftClick(event):
    x, y = event.x, event.y
    # Only create a joint if the shiftkey is not being held down
    if(shift == True):
        # Create the joint with the given location and append the center to the
        # list of joint locations
        makeJoint(x,y)
        global jointLocation
        jointLocation += (x,y)
    else:
        for i, joint in enumerate(jointLocation):
            if(joint == (x, y)):
                pass

def motion(event):
    x, y = event.x, event.y

def shift(event):
    # Invert shift detection when clicked
    global shift
    shift = not shift
    print("shift")

def rightClick(event):
    pass

def middleClick(event):
    pass

# Draw a circle on the canvas representing a singular joint in the truss
# with a set radius centered on the mouse position
def makeJoint(x,y):
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
canvas.bind('<Motion>', motion) # Mouse motion
canvas.bind('<Button-1>', leftClick) # Primary mouse click
canvas.bind('<ButtonRelease-1>', rightClick) # Primary mouse release
canvas.bind('<Button-2>', rightClick) # Secondary mouse click
canvas.bind('<ButtonRelease-2>', rightClick) # Secondary mouse release
canvas.bind('<Button-3>', middleClick) # Middle mouse click
canvas.bind('<ButtonRelease-3>', middleClick) # Middle mouse release
canvas.bind('<Shift_L>', shift) # Left shift click
canvas.bind('<KeyRelease-Shift_L>', shift) # Left shift release

# Execute the program
root.mainloop() # Nothing below this line gets executed
