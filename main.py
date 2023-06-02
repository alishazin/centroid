
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as MatRectangle

class Shape:

    def __init__(self, xCordinate, yCordinate):
        self.xCordinate = xCordinate  
        self.yCordinate = yCordinate  

class Rectangle(Shape):

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
            if (shape.xCordinate) > min_x:
                min_x = shape.xCordinate
            if (shape.yCordinate) > min_y:
                min_y = shape.yCordinate
            if (shape.xCordinate + shape.length) > max_x:
                max_x = shape.xCordinate + shape.length
            if (shape.yCordinate + shape.breadth) > max_y:
                max_y = shape.yCordinate + shape.breadth

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
            ax.add_patch(MatRectangle((shape.xCordinate, shape.yCordinate), shape.length, shape.breadth))

        centroid = self.get_centroid()

        plt.plot(centroid[0], centroid[1], marker="o", markerfacecolor="red", markeredgecolor="yellow", label="Centroid")
        plt.legend(loc ="lower right")

        print(centroid)

        plt.show()


def main():
    
    env = Env()
    
    env.add_shape(Rectangle(0, 0, 10, 5))
    env.add_shape(Rectangle(8, 4, 10, 5))

    for i in env.shapes: print(i)

    env.plot()


if __name__ == '__main__':
    main()