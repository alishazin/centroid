
from .shape import Shape
from matplotlib.patches import Polygon as MatPolygon


class RightTriangle(Shape):

    name = "righttriangle"

    def __init__(self, xCordinate, yCordinate, base, height, shape_type):
        self.base = base
        self.height = height
        self.shape_type = shape_type
        super().__init__(xCordinate, yCordinate)

    def __str__(self):
        return f"<RightTriangle: x={self.xCordinate} y={self.yCordinate} base={self.base} height={self.height} type={self.shape_type}>"
    
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
    
    def get_graph_patch(self, color=None, edge_clr=None):

        if color:
        
            if self.shape_type == 'tr':
                return MatPolygon([[self.xCordinate, self.yCordinate], [self.xCordinate + self.base, self.yCordinate], [self.xCordinate, self.yCordinate + self.height]], facecolor=color, edgecolor=edge_clr, linewidth=3)
            
            elif self.shape_type == 'tl':
                return MatPolygon([[self.xCordinate, self.yCordinate], [self.xCordinate - self.base, self.yCordinate], [self.xCordinate, self.yCordinate + self.height]], facecolor=color, edgecolor=edge_clr, linewidth=3)
            
            elif self.shape_type == 'br':
                return MatPolygon([[self.xCordinate, self.yCordinate], [self.xCordinate + self.base, self.yCordinate], [self.xCordinate, self.yCordinate - self.height]], facecolor=color, edgecolor=edge_clr, linewidth=3)
            
            elif self.shape_type == 'bl':
                return MatPolygon([[self.xCordinate, self.yCordinate], [self.xCordinate - self.base, self.yCordinate], [self.xCordinate, self.yCordinate - self.height]], facecolor=color, edgecolor=edge_clr, linewidth=3)
        
        else:

            if self.shape_type == 'tr':
                return MatPolygon([[self.xCordinate, self.yCordinate], [self.xCordinate + self.base, self.yCordinate], [self.xCordinate, self.yCordinate + self.height]])
            
            elif self.shape_type == 'tl':
                return MatPolygon([[self.xCordinate, self.yCordinate], [self.xCordinate - self.base, self.yCordinate], [self.xCordinate, self.yCordinate + self.height]])
            
            elif self.shape_type == 'br':
                return MatPolygon([[self.xCordinate, self.yCordinate], [self.xCordinate + self.base, self.yCordinate], [self.xCordinate, self.yCordinate - self.height]])
            
            elif self.shape_type == 'bl':
                return MatPolygon([[self.xCordinate, self.yCordinate], [self.xCordinate - self.base, self.yCordinate], [self.xCordinate, self.yCordinate - self.height]])
