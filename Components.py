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
        
    def fromcoords(x, y):
        return Joint(Point(x, y))

    def draw(self, location):
        radius = Joint.radius
        canvas.create_oval(location.x - radius, location.y - radius, location.x + radius, location.y+radius, tag=self.id, fill='#F00')

    def select(self, location):
        radius = Joint.radius
        canvas.create_oval(location.x - radius, location.y - radius, location.x + radius, location.y+radius, tag=self.id, fill='#e67300b')
        
    def unselect(location):
        pass
point1 = Point(250, 250)
joint1 = Joint(point1)
joint2 = Joint.fromcoords(260, 260)



