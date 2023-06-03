
import math

from matplotlib.patches import Rectangle as MatRectangle
from matplotlib.patches import Circle as MatCircle
from matplotlib.patches import Wedge as MatWedge
from matplotlib.patches import Polygon as MatPolygon


class Shape:

    def __init__(self, xCordinate, yCordinate):
        self.xCordinate = xCordinate  
        self.yCordinate = yCordinate  

class Rectangle(Shape):

    name = 'rectangle'

    def __init__(self, xCordinate, yCordinate, length, breadth):
        self.length = length
        self.breadth = breadth
        super().__init__(xCordinate, yCordinate)

    def __str__(self):
        return f"<Rectangle: l={self.length} b={self.breadth}>"
    
    @property
    def c_x(self):
        return self.xCordinate + (self.length / 2)
    
    @property
    def c_y(self):
        return self.yCordinate + (self.breadth / 2)
    
    def area(self):
        return self.length * self.breadth
    
    def get_min_max_cordinates(self, min_x, min_y, max_x, max_y):

        if min_x == None: min_x = self.xCordinate
        if min_y == None: min_y = self.yCordinate
        if max_x == None: max_x = self.xCordinate + self.length
        if max_y == None: max_y = self.yCordinate + self.breadth
        if (self.xCordinate) < min_x:
            min_x = self.xCordinate
        if (self.yCordinate) < min_y:
            min_y = self.yCordinate
        if (self.xCordinate + self.length) > max_x:
            max_x = self.xCordinate + self.length
        if (self.yCordinate + self.breadth) > max_y:
            max_y = self.yCordinate + self.breadth

        return (min_x, min_y, max_x, max_y)
    
    def get_graph_patch(self):
        return MatRectangle((self.xCordinate, self.yCordinate), self.length, self.breadth)


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

class SemiCircle(Shape):

    name = "semicircle"

    def __init__(self, xCordinate, yCordinate, radius, shape_type):
        self.radius = radius
        self.shape_type = shape_type
        super().__init__(xCordinate, yCordinate)

    def __str__(self):
        return f"<Semcircle: r={self.radius} t={self.shape_type}>"
    
    @property
    def c_x(self):
        if self.shape_type in ['t', 'b']:
            return self.xCordinate
        elif self.shape_type == 'r':
            return self.xCordinate + ((4*self.radius)/(3*math.pi))
        elif self.shape_type == 'l':
            return self.xCordinate - ((4*self.radius)/(3*math.pi))
    
    @property
    def c_y(self):
        if self.shape_type in ['l', 'r']:
            return self.yCordinate
        elif self.shape_type == 't':
            return self.yCordinate + ((4*self.radius)/(3*math.pi))
        elif self.shape_type == 'b':
            return self.xCordinate - ((4*self.radius)/(3*math.pi))
    
    def area(self):
        return (math.pi * self.radius * self.radius) / 2
    
    def get_min_max_cordinates(self, min_x, min_y, max_x, max_y):

        if self.shape_type == 't':
            if min_x == None: min_x = self.xCordinate - self.radius
            if min_y == None: min_y = self.yCordinate
            if max_x == None: max_x = self.xCordinate + self.radius
            if max_y == None: max_y = self.yCordinate + self.radius
            if (self.xCordinate - self.radius) < min_x:
                min_x = self.xCordinate - self.radius
            if (self.yCordinate) < min_y:
                min_y = self.yCordinate
            if (self.xCordinate + self.radius) > max_x:
                max_x = self.xCordinate + self.radius
            if (self.yCordinate + self.radius) > max_y:
                max_y = self.yCordinate + self.radius
        
        elif self.shape_type == 'b':
            if min_x == None: min_x = self.xCordinate - self.radius
            if min_y == None: min_y = self.yCordinate - self.radius
            if max_x == None: max_x = self.xCordinate + self.radius
            if max_y == None: max_y = self.yCordinate
            if (self.xCordinate - self.radius) < min_x:
                min_x = self.xCordinate - self.radius
            if (self.yCordinate - self.radius) < min_y:
                min_y = self.yCordinate - self.radius
            if (self.xCordinate + self.radius) > max_x:
                max_x = self.xCordinate + self.radius
            if (self.yCordinate) > max_y:
                max_y = self.yCordinate
        
        elif self.shape_type == 'l':
            if min_x == None: min_x = self.xCordinate - self.radius
            if min_y == None: min_y = self.yCordinate - self.radius
            if max_x == None: max_x = self.xCordinate
            if max_y == None: max_y = self.yCordinate + self.radius
            if (self.xCordinate - self.radius) < min_x:
                min_x = self.xCordinate - self.radius
            if (self.yCordinate - self.radius) < min_y:
                min_y = self.yCordinate - self.radius
            if (self.xCordinate) > max_x:
                max_x = self.xCordinate
            if (self.yCordinate + self.radius) > max_y:
                max_y = self.yCordinate + self.radius
        
        elif self.shape_type == 'r':
            if min_x == None: min_x = self.xCordinate
            if min_y == None: min_y = self.yCordinate - self.radius
            if max_x == None: max_x = self.xCordinate + self.radius
            if max_y == None: max_y = self.yCordinate + self.radius
            if (self.xCordinate) < min_x:
                min_x = self.xCordinate
            if (self.yCordinate - self.radius) < min_y:
                min_y = self.yCordinate - self.radius
            if (self.xCordinate + self.radius) > max_x:
                max_x = self.xCordinate + self.radius
            if (self.yCordinate + self.radius) > max_y:
                max_y = self.yCordinate + self.radius
                max_y = self.yCordinate + self.radius

        return (min_x, min_y, max_x, max_y)

    def get_graph_patch(self):

        if self.shape_type == 't':
            return MatWedge((self.xCordinate, self.yCordinate), self.radius, 0, 180)
        
        elif self.shape_type == 'b':
            return MatWedge((self.xCordinate, self.yCordinate), self.radius, 180, 360)
        
        elif self.shape_type == 'l':
            return MatWedge((self.xCordinate, self.yCordinate), self.radius, 90, 270)
        
        elif self.shape_type == 'r':
            return MatWedge((self.xCordinate, self.yCordinate), self.radius, 270, 90)
    
class Quadrant(Shape):

    name = "quadrant"

    def __init__(self, xCordinate, yCordinate, radius, shape_type):
        self.radius = radius
        self.shape_type = shape_type
        super().__init__(xCordinate, yCordinate)

    def __str__(self):
        return f"<Quadrant: r={self.radius} t={self.shape_type}>"
    
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
    
    def get_graph_patch(self):
        
        if self.shape_type == 'tr':
            return MatWedge((self.xCordinate, self.yCordinate), self.radius, 0, 90)
        
        elif self.shape_type == 'tl':
            return MatWedge((self.xCordinate, self.yCordinate), self.radius, 90, 180)
        
        elif self.shape_type == 'br':
            return MatWedge((self.xCordinate, self.yCordinate), self.radius, 270, 360)
        
        elif self.shape_type == 'bl':
            return MatWedge((self.xCordinate, self.yCordinate), self.radius, 180, 270)

class RightTriangle(Shape):

    name = "righttriangle"

    def __init__(self, xCordinate, yCordinate, base, height, shape_type):
        self.base = base
        self.height = height
        self.shape_type = shape_type
        super().__init__(xCordinate, yCordinate)

    def __str__(self):
        return f"<RightTriangle: b={self.base} h={self.height} t={self.shape_type}>"
    
    @property
    def c_x(self):
        if self.shape_type in ['tr', 'br']:
            return self.xCordinate + (self.base / 3)
        elif self.shape_type in ['tl', 'bl']:
            return self.xCordinate - (self.base / 3)
    
    @property
    def c_y(self):
        if self.shape_type in ['tr', 'tl']:
            return self.yCordinate + (self.height / 3)
        elif self.shape_type in ['br', 'bl']:
            return self.yCordinate - (self.height / 3)
    
    def area(self):
        return (1/2) * self.base * self.height
    
    def get_min_max_cordinates(self, min_x, min_y, max_x, max_y):
        
        if self.shape_type == 'tr':
            if min_x == None: min_x = self.xCordinate
            if min_y == None: min_y = self.yCordinate
            if max_x == None: max_x = self.xCordinate + self.base
            if max_y == None: max_y = self.yCordinate + self.height
            if (self.xCordinate) < min_x:
                min_x = self.xCordinate
            if (self.yCordinate) < min_y:
                min_y = self.yCordinate
            if (self.xCordinate + self.base) > max_x:
                max_x = self.xCordinate + self.base
            if (self.yCordinate + self.height) > max_y:
                max_y = self.yCordinate + self.height
        
        elif self.shape_type == 'tl':
            if min_x == None: min_x = self.xCordinate - self.base
            if min_y == None: min_y = self.yCordinate
            if max_x == None: max_x = self.xCordinate
            if max_y == None: max_y = self.yCordinate + self.height
            if (self.xCordinate - self.base) < min_x:
                min_x = self.xCordinate - self.base
            if (self.yCordinate) < min_y:
                min_y = self.yCordinate
            if (self.xCordinate) > max_x:
                max_x = self.xCordinate
            if (self.yCordinate + self.height) > max_y:
                max_y = self.yCordinate + self.height
        
        elif self.shape_type == 'br':
            if min_x == None: min_x = self.xCordinate
            if min_y == None: min_y = self.yCordinate - self.height
            if max_x == None: max_x = self.xCordinate + self.base
            if max_y == None: max_y = self.yCordinate
            if (self.xCordinate) < min_x:
                min_x = self.xCordinate
            if (self.yCordinate - self.height) < min_y:
                min_y = self.yCordinate - self.height
            if (self.xCordinate + self.base) > max_x:
                max_x = self.xCordinate + self.base
            if (self.yCordinate) > max_y:
                max_y = self.yCordinate
        
        elif self.shape_type == 'bl':
            if min_x == None: min_x = self.xCordinate - self.base
            if min_y == None: min_y = self.yCordinate - self.height
            if max_x == None: max_x = self.xCordinate
            if max_y == None: max_y = self.yCordinate
            if (self.xCordinate - self.base) < min_x:
                min_x = self.xCordinate - self.base
            if (self.yCordinate - self.height) < min_y:
                min_y = self.yCordinate - self.height
            if (self.xCordinate) > max_x:
                max_x = self.xCordinate
            if (self.yCordinate) > max_y:
                max_y = self.yCordinate

        return (min_x, min_y, max_x, max_y)
    
    def get_graph_patch(self):
        
        if self.shape_type == 'tr':
            return MatPolygon([[self.xCordinate, self.yCordinate], [self.xCordinate + self.base, self.yCordinate], [self.xCordinate, self.yCordinate + self.height]])
        
        elif self.shape_type == 'tl':
            return MatPolygon([[self.xCordinate, self.yCordinate], [self.xCordinate - self.base, self.yCordinate], [self.xCordinate, self.yCordinate + self.height]])
        
        elif self.shape_type == 'br':
            return MatPolygon([[self.xCordinate, self.yCordinate], [self.xCordinate + self.base, self.yCordinate], [self.xCordinate, self.yCordinate - self.height]])
        
        elif self.shape_type == 'bl':
            return MatPolygon([[self.xCordinate, self.yCordinate], [self.xCordinate - self.base, self.yCordinate], [self.xCordinate, self.yCordinate - self.height]])

class EquilateralTriangle(Shape):

    name = "equilateraltriangle"

    def __init__(self, xCordinate, yCordinate, side, shape_type):
        self.side = side
        self.shape_type = shape_type
        super().__init__(xCordinate, yCordinate)

    def __str__(self):
        return f"<EquilateralTriangle: s={self.side} t={self.shape_type}>"
    
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
    
    def get_graph_patch(self):

        if self.shape_type == 't':
            return MatPolygon([[self.xCordinate - (self.side / 2), self.yCordinate], [self.xCordinate + (self.side / 2), self.yCordinate], [self.xCordinate, self.yCordinate + self.median]])
        
        elif self.shape_type == 'b':
            return MatPolygon([[self.xCordinate - (self.side / 2), self.yCordinate], [self.xCordinate + (self.side / 2), self.yCordinate], [self.xCordinate, self.yCordinate - self.median]])
        
        elif self.shape_type == 'l':
            return MatPolygon([[self.xCordinate, self.yCordinate - (self.side / 2)], [self.xCordinate, self.yCordinate + (self.side / 2)], [self.xCordinate - self.median, self.yCordinate]])
        
        elif self.shape_type == 'r':
            return MatPolygon([[self.xCordinate, self.yCordinate - (self.side / 2)], [self.xCordinate, self.yCordinate + (self.side / 2)], [self.xCordinate + self.median, self.yCordinate]])