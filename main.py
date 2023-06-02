
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as MatRectangle
from matplotlib.patches import Circle as MatCircle
from matplotlib.patches import Wedge as MatWedge

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


class Env:

    shapes = []

    def add_shape(self, shapeObj):
        self.shapes.append(shapeObj)

    def get_min_max_cordinates(self):
        min_x = 0
        min_y = 0
        max_x = 0
        max_y = 0

        for shape in self.shapes:

            if shape.name == 'rectangle':
                if (shape.xCordinate) > min_x:
                    min_x = shape.xCordinate
                if (shape.yCordinate) > min_y:
                    min_y = shape.yCordinate
                if (shape.xCordinate + shape.length) > max_x:
                    max_x = shape.xCordinate + shape.length
                if (shape.yCordinate + shape.breadth) > max_y:
                    max_y = shape.yCordinate + shape.breadth
            
            elif shape.name == 'circle':
                if (shape.xCordinate - shape.radius) > min_x:
                    min_x = shape.xCordinate - shape.radius
                if (shape.yCordinate - shape.radius) > min_y:
                    min_y = shape.yCordinate - shape.radius
                if (shape.xCordinate + shape.radius) > max_x:
                    max_x = shape.xCordinate + shape.radius
                if (shape.yCordinate + shape.radius) > max_y:
                    max_y = shape.yCordinate + shape.radius
            
            elif shape.name == 'semicircle-t':
                if (shape.xCordinate - shape.radius) > min_x:
                    min_x = shape.xCordinate - shape.radius
                if (shape.yCordinate) > min_y:
                    min_y = shape.yCordinate
                if (shape.xCordinate + shape.radius) > max_x:
                    max_x = shape.xCordinate + shape.radius
                if (shape.yCordinate + shape.radius) > max_y:
                    max_y = shape.yCordinate + shape.radius
            
            elif shape.name == 'semicircle-b':
                if (shape.xCordinate - shape.radius) > min_x:
                    min_x = shape.xCordinate - shape.radius
                if (shape.yCordinate + shape.radius) > min_y:
                    min_y = shape.yCordinate + shape.radius
                if (shape.xCordinate + shape.radius) > max_x:
                    max_x = shape.xCordinate + shape.radius
                if (shape.yCordinate) > max_y:
                    max_y = shape.yCordinate
            
            elif shape.name == 'semicircle-l':
                if (shape.xCordinate - shape.radius) > min_x:
                    min_x = shape.xCordinate - shape.radius
                if (shape.yCordinate - shape.radius) > min_y:
                    min_y = shape.yCordinate - shape.radius
                if (shape.xCordinate) > max_x:
                    max_x = shape.xCordinate
                if (shape.yCordinate + shape.radius) > max_y:
                    max_y = shape.yCordinate + shape.radius
            
            elif shape.name == 'semicircle-r':
                if (shape.xCordinate) > min_x:
                    min_x = shape.xCordinate
                if (shape.yCordinate - shape.radius) > min_y:
                    min_y = shape.yCordinate - shape.radius
                if (shape.xCordinate + shape.radius) > max_x:
                    max_x = shape.xCordinate + shape.radius
                if (shape.yCordinate + shape.radius) > max_y:
                    max_y = shape.yCordinate + shape.radius

        return ([min_x, min_y], [max_x, max_y])
    
    def get_centroid(self):
        
        x = 0
        y = 0
        sum_area = 0

        for shape in self.shapes:
            x += (shape.area() * shape.c_x)
            y += (shape.area() * shape.c_y)
            sum_area += shape.area()

        x /= sum_area
        y /= sum_area

        return (x, y)

    def plot(self):
        fig, ax = plt.subplots()

        min_cor, max_cor = self.get_min_max_cordinates()
        ax.plot([min_cor[0], max_cor[0]],[min_cor[1], max_cor[1]], alpha=0)

        for shape in self.shapes:

            if shape.name == 'rectangle':
                ax.add_patch(MatRectangle((shape.xCordinate, shape.yCordinate), shape.length, shape.breadth))

            elif shape.name == 'circle':
                ax.add_patch(MatCircle((shape.xCordinate, shape.yCordinate), shape.radius))

            elif shape.name == 'semicircle-t':
                ax.add_patch(MatWedge((shape.xCordinate, shape.yCordinate), shape.radius, 0, 180))
            
            elif shape.name == 'semicircle-b':
                ax.add_patch(MatWedge((shape.xCordinate, shape.yCordinate), shape.radius, 180, 360))
            
            elif shape.name == 'semicircle-l':
                ax.add_patch(MatWedge((shape.xCordinate, shape.yCordinate), shape.radius, 90, 270))
            
            elif shape.name == 'semicircle-r':
                ax.add_patch(MatWedge((shape.xCordinate, shape.yCordinate), shape.radius, 270, 90))

        centroid = self.get_centroid()

        plt.plot(centroid[0], centroid[1], marker="o", markerfacecolor="red", markeredgecolor="yellow", label="Centroid")
        plt.legend(loc ="lower right")

        print(centroid)

        plt.show()


def main():
    
    env = Env()
    
    # env.add_shape(Rectangle(0, 0, 10, 5))
    # env.add_shape(Rectangle(8, 4, 10, 5))
    # env.add_shape(Rectangle(0, 10, 10, 5))
    # env.add_shape(Circle(4, 5, 5))
    # env.add_shape(SemiCircle(5, 5, 5, 't'))
    # env.add_shape(SemiCircle(5, 5, 5, 'b'))
    env.add_shape(SemiCircle(5, 5, 5, 'l'))
    env.add_shape(SemiCircle(5, 5, 5, 'r'))

    for i in env.shapes: print(i)

    env.plot()


if __name__ == '__main__':
    main()