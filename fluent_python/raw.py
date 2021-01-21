import math

class Vectors:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Vector({self.x},{self.y})'
    def __add__(self, other):
        x, y = self.x+other.x, self.y+other.y
        return Vector(x,y)
    def __abs__(self):
        return abs(self)
    def __bool__(self):
        
