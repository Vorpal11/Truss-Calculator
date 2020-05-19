#!/usr/bin/python3 

import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Joint:
    def setRadius(radius):
        Joint.radius = radius

    def __init__(self, location):
        self.id = str(random.randint(1, 10000))
        self.location = location
        
    def fromCoords(x, y):
        return Joint(Point(x, y))

    def draw(self, canvas):
        radius = Joint.radius
        canvas.create_oval(self.location.x - radius, self.location.y - radius, self.location.x + radius, self.location.y+radius, tag=self.id, fill='#F00')

    def select(self, canvas):
        radius = Joint.radius
        canvas.create_oval(self.location.x - radius, self.location.y - radius, self.location.x + radius, self.location.y+radius, tag=self.id, fill='#e67300b')
        
    def unselect(location):
        pass

class Beam:
    color = 'black'
    selectedColor = 'pink'
    def __init__(self, start, end):
        self.id = str(random.randint(1, 10000))
        self.start = start
        self.end = end
        self.force = None

    def draw(self, canvas):
        # Implement later

        # Blue = inward
        # Red = outward
        # Compression
        start = self.start.location
        end = self.end.location
        self.id = canvas.create_line(start.x, start.y, end.x, end.y, tag=self.id, fill=Beam.color)

    def select(self, canvas):
        canvas.itemconfig(self.id, fill=Beam.selectedColor)

    def unselect(self, canvas):
        canvas.itemconfig(self.id, fill=Beam.color)
