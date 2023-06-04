
import math

from .shape import Shape
from matplotlib.patches import Wedge as MatWedge


class Quadrant(Shape):

    name = "quadrant"

    def __init__(self, xCordinate, yCordinate, radius, shape_type):
        self.radius = radius
        self.shape_type = shape_type
        super().__init__(xCordinate, yCordinate)

    def __str__(self):
        return f"<Quadrant: x={self.xCordinate} y={self.yCordinate} r={self.radius} type={self.shape_type}>"
    
    @property
    def c_x(self):
        if self.shape_type in ['tr', 'br']:
            return self.xCordinate + ((4*self.radius)/(3*math.pi))
        elif self.shape_type in ['tl', 'bl']:
            return self.xCordinate - ((4*self.radius)/(3*math.pi))
    
    @property
    def c_y(self):
        if self.shape_type in ['tr', 'tl']:
            return self.yCordinate + ((4*self.radius)/(3*math.pi))
        elif self.shape_type in ['br', 'bl']:
            return self.yCordinate - ((4*self.radius)/(3*math.pi))
    
    def area(self):
        return (math.pi * self.radius * self.radius) / 4
    
    def get_min_max_cordinates(self, min_x, min_y, max_x, max_y):
        
        if self.shape_type == 'tr':
            if min_x == None: min_x = self.xCordinate
            if min_y == None: min_y = self.yCordinate
            if max_x == None: max_x = self.xCordinate + self.radius
            if max_y == None: max_y = self.yCordinate + self.radius
            if (self.xCordinate) < min_x:
                min_x = self.xCordinate
            if (self.yCordinate) < min_y:
                min_y = self.yCordinate
            if (self.xCordinate + self.radius) > max_x:
                max_x = self.xCordinate + self.radius
            if (self.yCordinate + self.radius) > max_y:
                max_y = self.yCordinate + self.radius
        
        elif self.shape_type == 'tl':
            if min_x == None: min_x = self.xCordinate - self.radius
            if min_y == None: min_y = self.yCordinate
            if max_x == None: max_x = self.xCordinate
            if max_y == None: max_y = self.yCordinate + self.radius
            if (self.xCordinate - self.radius) < min_x:
                min_x = self.xCordinate - self.radius
            if (self.yCordinate) < min_y:
                min_y = self.yCordinate
            if (self.xCordinate) > max_x:
                max_x = self.xCordinate
            if (self.yCordinate + self.radius) > max_y:
                max_y = self.yCordinate + self.radius
        
        elif self.shape_type == 'br':
            if min_x == None: min_x = self.xCordinate 
            if min_y == None: min_y = self.yCordinate - self.radius
            if max_x == None: max_x = self.xCordinate + self.radius
            if max_y == None: max_y = self.yCordinate
            if (self.xCordinate) < min_x:
                min_x = self.xCordinate
            if (self.yCordinate - self.radius) < min_y:
                min_y = self.yCordinate - self.radius
            if (self.xCordinate + self.radius) > max_x:
                max_x = self.xCordinate + self.radius
            if (self.yCordinate) > max_y:
                max_y = self.yCordinate
        
        elif self.shape_type == 'bl':
            if min_x == None: min_x = self.xCordinate - self.radius
            if min_y == None: min_y = self.yCordinate - self.radius
            if max_x == None: max_x = self.xCordinate
            if max_y == None: max_y = self.yCordinate
            if (self.xCordinate - self.radius) < min_x:
                min_x = self.xCordinate - self.radius
            if (self.yCordinate - self.radius) < min_y:
                min_y = self.yCordinate - self.radius
            if (self.xCordinate) > max_x:
                max_x = self.xCordinate
            if (self.yCordinate) > max_y:
                max_y = self.yCordinate

        return (min_x, min_y, max_x, max_y)
    
    def get_graph_patch(self, color=None):
        
        if color:

            if self.shape_type == 'tr':
                return MatWedge((self.xCordinate, self.yCordinate), self.radius, 0, 90, color=color, alpha=0.6)
            
            elif self.shape_type == 'tl':
                return MatWedge((self.xCordinate, self.yCordinate), self.radius, 90, 180, color=color, alpha=0.6)
            
            elif self.shape_type == 'br':
                return MatWedge((self.xCordinate, self.yCordinate), self.radius, 270, 360, color=color, alpha=0.6)
            
            elif self.shape_type == 'bl':
                return MatWedge((self.xCordinate, self.yCordinate), self.radius, 180, 270, color=color, alpha=0.6)
 
        else:

            if self.shape_type == 'tr':
                return MatWedge((self.xCordinate, self.yCordinate), self.radius, 0, 90)
            
            elif self.shape_type == 'tl':
                return MatWedge((self.xCordinate, self.yCordinate), self.radius, 90, 180)
            
            elif self.shape_type == 'br':
                return MatWedge((self.xCordinate, self.yCordinate), self.radius, 270, 360)
            
            elif self.shape_type == 'bl':
                return MatWedge((self.xCordinate, self.yCordinate), self.radius, 180, 270)
