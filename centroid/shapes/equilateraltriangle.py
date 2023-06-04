
import math

from .shape import Shape
from matplotlib.patches import Polygon as MatPolygon


class EquilateralTriangle(Shape):

    name = "equilateraltriangle"

    def __init__(self, xCordinate, yCordinate, side, shape_type):
        self.side = side
        self.shape_type = shape_type
        super().__init__(xCordinate, yCordinate)

    def __str__(self):
        return f"<EquilateralTriangle: x={self.xCordinate} y={self.yCordinate} side={self.side} type={self.shape_type}>"
    
    @property
    def median(self):
        return math.sqrt((self.side**2) - ((self.side/2)**2))
    
    @property
    def c_x(self):
        if self.shape_type in ['t', 'b']:
            return self.xCordinate
        elif self.shape_type == 'r':
            return self.xCordinate + ((self.median) / 3)
        elif self.shape_type == 'l':
            return self.xCordinate - ((self.median) / 3)
    
    @property
    def c_y(self):
        if self.shape_type in ['l', 'r']:
            return self.yCordinate
        elif self.shape_type == 't':
            return self.yCordinate + ((self.median) / 3)
        elif self.shape_type == 'b':
            return self.yCordinate - ((self.median) / 3)
    
    def area(self):
        return (math.sqrt(3) * self.side * self.side) / 4
    
    def get_min_max_cordinates(self, min_x, min_y, max_x, max_y):
        
        if self.shape_type == 't':
            if min_x == None: min_x = self.xCordinate - (self.side / 2)
            if min_y == None: min_y = self.yCordinate
            if max_x == None: max_x = self.xCordinate + (self.side / 2)
            if max_y == None: max_y = self.yCordinate + (self.median)
            if (self.xCordinate - (self.side / 2)) < min_x:
                min_x = self.xCordinate - (self.side / 2)
            if (self.yCordinate) < min_y:
                min_y = self.yCordinate
            if (self.xCordinate + (self.side / 2)) > max_x:
                max_x = self.xCordinate + (self.side / 2)
            if (self.yCordinate + self.median) > max_y:
                max_y = self.yCordinate + (self.median)
        
        elif self.shape_type == 'b':
            if min_x == None: min_x = self.xCordinate - (self.side / 2)
            if min_y == None: min_y = self.yCordinate - self.median
            if max_x == None: max_x = self.xCordinate + (self.side / 2)
            if max_y == None: max_y = self.yCordinate
            if (self.xCordinate - (self.side / 2)) < min_x:
                min_x = self.xCordinate - (self.side / 2)
            if (self.yCordinate - self.median) < min_y:
                min_y =self.yCordinate - self.median
            if (self.xCordinate + (self.side / 2)) > max_x:
                max_x = self.xCordinate + (self.side / 2)
            if (self.yCordinate) > max_y:
                max_y = self.yCordinate
        
        elif self.shape_type == 'l':
            if min_x == None: min_x = self.xCordinate - (self.median)
            if min_y == None: min_y = self.yCordinate - (self.side / 2)
            if max_x == None: max_x = self.xCordinate
            if max_y == None: max_y = self.yCordinate + (self.side / 2)
            if (self.xCordinate - (self.median)) < min_x:
                min_x = self.xCordinate - (self.median)
            if (self.yCordinate - (self.side / 2)) < min_y:
                min_y =self.yCordinate - (self.side / 2)
            if (self.xCordinate) > max_x:
                max_x = self.xCordinate
            if (self.yCordinate + (self.side / 2)) > max_y:
                max_y = self.yCordinate + (self.side / 2)
        
        elif self.shape_type == 'r':
            if min_x == None: min_x = self.xCordinate
            if min_y == None: min_y = self.yCordinate - (self.side / 2)
            if max_x == None: max_x = self.xCordinate + (self.median)
            if max_y == None: max_y = self.yCordinate + (self.side / 2)
            if (self.xCordinate) < min_x:
                min_x = self.xCordinate
            if (self.yCordinate - (self.side / 2)) < min_y:
                min_y =self.yCordinate - (self.side / 2)
            if (self.xCordinate + (self.median)) > max_x:
                max_x = self.xCordinate + (self.median)
            if (self.yCordinate + (self.side / 2)) > max_y:
                max_y = self.yCordinate + (self.side / 2)

        return (min_x, min_y, max_x, max_y)
    
    def get_graph_patch(self, color=None):

        if color:

            if self.shape_type == 't':
                return MatPolygon([[self.xCordinate - (self.side / 2), self.yCordinate], [self.xCordinate + (self.side / 2), self.yCordinate], [self.xCordinate, self.yCordinate + self.median]], color=color)
            
            elif self.shape_type == 'b':
                return MatPolygon([[self.xCordinate - (self.side / 2), self.yCordinate], [self.xCordinate + (self.side / 2), self.yCordinate], [self.xCordinate, self.yCordinate - self.median]], color=color, alpha=0.6)
            
            elif self.shape_type == 'l':
                return MatPolygon([[self.xCordinate, self.yCordinate - (self.side / 2)], [self.xCordinate, self.yCordinate + (self.side / 2)], [self.xCordinate - self.median, self.yCordinate]], color=color, alpha=0.6)
            
            elif self.shape_type == 'r':
                return MatPolygon([[self.xCordinate, self.yCordinate - (self.side / 2)], [self.xCordinate, self.yCordinate + (self.side / 2)], [self.xCordinate + self.median, self.yCordinate]], color=color, alpha=0.6)
        
        else:

            if self.shape_type == 't':
                return MatPolygon([[self.xCordinate - (self.side / 2), self.yCordinate], [self.xCordinate + (self.side / 2), self.yCordinate], [self.xCordinate, self.yCordinate + self.median]])
            
            elif self.shape_type == 'b':
                return MatPolygon([[self.xCordinate - (self.side / 2), self.yCordinate], [self.xCordinate + (self.side / 2), self.yCordinate], [self.xCordinate, self.yCordinate - self.median]])
            
            elif self.shape_type == 'l':
                return MatPolygon([[self.xCordinate, self.yCordinate - (self.side / 2)], [self.xCordinate, self.yCordinate + (self.side / 2)], [self.xCordinate - self.median, self.yCordinate]])
            
            elif self.shape_type == 'r':
                return MatPolygon([[self.xCordinate, self.yCordinate - (self.side / 2)], [self.xCordinate, self.yCordinate + (self.side / 2)], [self.xCordinate + self.median, self.yCordinate]])