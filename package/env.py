import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as MatRectangle
from matplotlib.patches import Circle as MatCircle
from matplotlib.patches import Wedge as MatWedge

class Env:

    shapes = []

    def add_shape(self, shapeObj):
        self.shapes.append(shapeObj)

    def get_min_max_cordinates(self):
        min_x = None
        min_y = None
        max_x = None
        max_y = None

        for shape in self.shapes:
            print(shape.name)

            if shape.name == 'rectangle':
                if min_x == None: min_x = shape.xCordinate
                if min_y == None: min_y = shape.yCordinate
                if max_x == None: max_x = shape.xCordinate + shape.length
                if max_y == None: max_y = shape.yCordinate + shape.breadth
                if (shape.xCordinate) < min_x:
                    min_x = shape.xCordinate
                if (shape.yCordinate) < min_y:
                    min_y = shape.yCordinate
                if (shape.xCordinate + shape.length) > max_x:
                    max_x = shape.xCordinate + shape.length
                if (shape.yCordinate + shape.breadth) > max_y:
                    max_y = shape.yCordinate + shape.breadth

                print(min_x)
            
            elif shape.name == 'circle':
                if min_x == None: min_x = shape.xCordinate - shape.radius
                if min_y == None: min_y = shape.yCordinate - shape.radius
                if max_x == None: max_x = shape.xCordinate + shape.radius
                if max_y == None: max_y = shape.yCordinate + shape.radius
                if (shape.xCordinate - shape.radius) < min_x:
                    min_x = shape.xCordinate - shape.radius
                if (shape.yCordinate - shape.radius) < min_y:
                    min_y = shape.yCordinate - shape.radius
                if (shape.xCordinate + shape.radius) > max_x:
                    max_x = shape.xCordinate + shape.radius
                if (shape.yCordinate + shape.radius) > max_y:
                    max_y = shape.yCordinate + shape.radius
            
            elif shape.name == 'semicircle-t':
                if min_x == None: min_x = shape.xCordinate - shape.radius
                if min_y == None: min_y = shape.yCordinate
                if max_x == None: max_x = shape.xCordinate + shape.radius
                if max_y == None: max_y = shape.yCordinate + shape.radius
                if (shape.xCordinate - shape.radius) < min_x:
                    min_x = shape.xCordinate - shape.radius
                if (shape.yCordinate) < min_y:
                    min_y = shape.yCordinate
                if (shape.xCordinate + shape.radius) > max_x:
                    max_x = shape.xCordinate + shape.radius
                if (shape.yCordinate + shape.radius) > max_y:
                    max_y = shape.yCordinate + shape.radius
            
            elif shape.name == 'semicircle-b':
                if min_x == None: min_x = shape.xCordinate - shape.radius
                if min_y == None: min_y = shape.yCordinate - shape.radius
                if max_x == None: max_x = shape.xCordinate + shape.radius
                if max_y == None: max_y = shape.yCordinate
                if (shape.xCordinate - shape.radius) < min_x:
                    min_x = shape.xCordinate - shape.radius
                if (shape.yCordinate - shape.radius) < min_y:
                    min_y = shape.yCordinate - shape.radius
                if (shape.xCordinate + shape.radius) > max_x:
                    max_x = shape.xCordinate + shape.radius
                if (shape.yCordinate) > max_y:
                    max_y = shape.yCordinate
            
            elif shape.name == 'semicircle-l':
                if min_x == None: min_x = shape.xCordinate - shape.radius
                if min_y == None: min_y = shape.yCordinate - shape.radius
                if max_x == None: max_x = shape.xCordinate
                if max_y == None: max_y = shape.yCordinate + shape.radius
                if (shape.xCordinate - shape.radius) < min_x:
                    min_x = shape.xCordinate - shape.radius
                if (shape.yCordinate - shape.radius) < min_y:
                    min_y = shape.yCordinate - shape.radius
                if (shape.xCordinate) > max_x:
                    max_x = shape.xCordinate
                if (shape.yCordinate + shape.radius) > max_y:
                    max_y = shape.yCordinate + shape.radius
            
            elif shape.name == 'semicircle-r':
                if min_x == None: min_x = shape.xCordinate
                if min_y == None: min_y = shape.yCordinate - shape.radius
                if max_x == None: max_x = shape.xCordinate + shape.radius
                if max_y == None: max_y = shape.yCordinate + shape.radius
                if (shape.xCordinate) < min_x:
                    min_x = shape.xCordinate
                if (shape.yCordinate - shape.radius) < min_y:
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
        print(min_cor, max_cor)

        ax.plot([min_cor[0], max_cor[0]], [centroid[1], centroid[1]], color='yellow', alpha=0.3, linewidth=0.6)
        ax.plot([centroid[0], centroid[0]], [min_cor[1], max_cor[1]], color='yellow', alpha=0.3, linewidth=0.6)

        plt.plot(centroid[0], centroid[1], marker="o", markerfacecolor="red", markeredgecolor="yellow", label="Centroid")
        plt.legend(loc ="lower right")

        print(centroid)

        plt.show()
