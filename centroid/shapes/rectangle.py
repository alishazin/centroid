
from .shape import Shape
from matplotlib.patches import Rectangle as MatRectangle


class Rectangle(Shape):

    name = 'rectangle'

    def __init__(self, xCordinate, yCordinate, length, breadth):
        self.length = length
        self.breadth = breadth
        super().__init__(xCordinate, yCordinate)

    def __str__(self):
        return f"<Rectangle: x={self.xCordinate} y={self.yCordinate} length={self.length} breadth={self.breadth}>"
    
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
    
    def get_graph_patch(self, color=None, edge_clr=None):
        if color:
            return MatRectangle((self.xCordinate, self.yCordinate), self.length, self.breadth, facecolor=color, edgecolor=edge_clr, linewidth=3)
        else:
            return MatRectangle((self.xCordinate, self.yCordinate), self.length, self.breadth)