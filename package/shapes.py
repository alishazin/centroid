
import math


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
    
    def area(self):
        return self.length * self.breadth
    
    @property
    def c_x(self):
        return self.xCordinate + (self.length / 2)
    
    @property
    def c_y(self):
        return self.yCordinate + (self.breadth / 2)

class Circle(Shape):

    name = 'circle'

    def __init__(self, xCordinate, yCordinate, radius):
        self.radius = radius
        super().__init__(xCordinate, yCordinate)

    def __str__(self):
        return f"<Circle: r={self.radius}>"
    
    def area(self):
        return math.pi * self.radius * self.radius
    
    @property
    def c_x(self):
        return self.xCordinate
    
    @property
    def c_y(self):
        return self.yCordinate

class SemiCircle(Shape):

    name = "semicircle-"

    def __init__(self, xCordinate, yCordinate, radius, shape_type):
        self.radius = radius
        self.shape_type = shape_type
        self.name = f"semicircle-{shape_type}"
        super().__init__(xCordinate, yCordinate)

    def __str__(self):
        return f"<Semcircle: r={self.radius} t={self.shape_type}>"
    
    def area(self):
        return (math.pi * self.radius * self.radius) / 2
    
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

class Quadrant(Shape):

    name = "quadrant-"

    def __init__(self, xCordinate, yCordinate, radius, shape_type):
        self.radius = radius
        self.shape_type = shape_type
        self.name = f"quadrant-{shape_type}"
        super().__init__(xCordinate, yCordinate)

    def __str__(self):
        return f"<Quadrant: r={self.radius} t={self.shape_type}>"
    
    def area(self):
        return (math.pi * self.radius * self.radius) / 4
    
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

class RightTriangle(Shape):

    name = "righttriangle-"

    def __init__(self, xCordinate, yCordinate, base, height, shape_type):
        self.base = base
        self.height = height
        self.shape_type = shape_type
        self.name = f"righttriangle-{shape_type}"
        super().__init__(xCordinate, yCordinate)

    def __str__(self):
        return f"<RightTriangle: b={self.base} h={self.height} t={self.shape_type}>"
    
    def area(self):
        return (1/2) * self.base * self.height
    
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

class EquilateralTriangle(Shape):

    name = "equilateraltriangle-"

    def __init__(self, xCordinate, yCordinate, side, shape_type):
        self.side = side
        self.shape_type = shape_type
        self.name = f"equilateraltriangle-{shape_type}"
        super().__init__(xCordinate, yCordinate)

    def __str__(self):
        return f"<EquilateralTriangle: s={self.side} t={self.shape_type}>"
    
    def area(self):
        return (math.sqrt(3) * self.side * self.side) / 4
    
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