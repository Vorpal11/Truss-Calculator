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
