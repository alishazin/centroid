
import math

from .shape import Shape
from matplotlib.patches import Circle as MatCircle


class Circle(Shape):

    name = 'circle'

    def __init__(self, xCordinate, yCordinate, radius):
        self.radius = radius
        super().__init__(xCordinate, yCordinate)

    def __str__(self):
        return f"<Circle: r={self.radius}>"
    
    @property
    def c_x(self):
        return self.xCordinate
    
    @property
    def c_y(self):
        return self.yCordinate
    
    def area(self):
        return math.pi * self.radius * self.radius
    
    def get_min_max_cordinates(self, min_x, min_y, max_x, max_y):
        
        if min_x == None: min_x = self.xCordinate - self.radius
        if min_y == None: min_y = self.yCordinate - self.radius
        if max_x == None: max_x = self.xCordinate + self.radius
        if max_y == None: max_y = self.yCordinate + self.radius
        if (self.xCordinate - self.radius) < min_x:
            min_x = self.xCordinate - self.radius
        if (self.yCordinate - self.radius) < min_y:
            min_y = self.yCordinate - self.radius
        if (self.xCordinate + self.radius) > max_x:
            max_x = self.xCordinate + self.radius
        if (self.yCordinate + self.radius) > max_y:
            max_y = self.yCordinate + self.radius

        return (min_x, min_y, max_x, max_y)
    
    def get_graph_patch(self):
        return MatCircle((self.xCordinate, self.yCordinate), self.radius)