import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as MatRectangle
from matplotlib.patches import Circle as MatCircle
from matplotlib.patches import Wedge as MatWedge
from matplotlib.patches import Polygon as MatPolygon

import math

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
                    max_y = shape.yCordinate + shape.radius
            
            elif shape.name == 'quadrant-tr':
                if min_x == None: min_x = shape.xCordinate
                if min_y == None: min_y = shape.yCordinate
                if max_x == None: max_x = shape.xCordinate + shape.radius
                if max_y == None: max_y = shape.yCordinate + shape.radius
                if (shape.xCordinate) < min_x:
                    min_x = shape.xCordinate
                if (shape.yCordinate) < min_y:
                    min_y = shape.yCordinate
                if (shape.xCordinate + shape.radius) > max_x:
                    max_x = shape.xCordinate + shape.radius
                if (shape.yCordinate + shape.radius) > max_y:
                    max_y = shape.yCordinate + shape.radius
            
            elif shape.name == 'quadrant-tl':
                if min_x == None: min_x = shape.xCordinate - shape.radius
                if min_y == None: min_y = shape.yCordinate
                if max_x == None: max_x = shape.xCordinate
                if max_y == None: max_y = shape.yCordinate + shape.radius
                if (shape.xCordinate - shape.radius) < min_x:
                    min_x = shape.xCordinate - shape.radius
                if (shape.yCordinate) < min_y:
                    min_y = shape.yCordinate
                if (shape.xCordinate) > max_x:
                    max_x = shape.xCordinate
                if (shape.yCordinate + shape.radius) > max_y:
                    max_y = shape.yCordinate + shape.radius
            
            elif shape.name == 'quadrant-br':
                if min_x == None: min_x = shape.xCordinate 
                if min_y == None: min_y = shape.yCordinate - shape.radius
                if max_x == None: max_x = shape.xCordinate + shape.radius
                if max_y == None: max_y = shape.yCordinate
                if (shape.xCordinate) < min_x:
                    min_x = shape.xCordinate
                if (shape.yCordinate - shape.radius) < min_y:
                    min_y = shape.yCordinate - shape.radius
                if (shape.xCordinate + shape.radius) > max_x:
                    max_x = shape.xCordinate + shape.radius
                if (shape.yCordinate) > max_y:
                    max_y = shape.yCordinate
            
            elif shape.name == 'quadrant-bl':
                if min_x == None: min_x = shape.xCordinate - shape.radius
                if min_y == None: min_y = shape.yCordinate - shape.radius
                if max_x == None: max_x = shape.xCordinate
                if max_y == None: max_y = shape.yCordinate
                if (shape.xCordinate - shape.radius) < min_x:
                    min_x = shape.xCordinate - shape.radius
                if (shape.yCordinate - shape.radius) < min_y:
                    min_y = shape.yCordinate - shape.radius
                if (shape.xCordinate) > max_x:
                    max_x = shape.xCordinate
                if (shape.yCordinate) > max_y:
                    max_y = shape.yCordinate
            
            elif shape.name == 'righttriangle-tr':
                if min_x == None: min_x = shape.xCordinate
                if min_y == None: min_y = shape.yCordinate
                if max_x == None: max_x = shape.xCordinate + shape.base
                if max_y == None: max_y = shape.yCordinate + shape.height
                if (shape.xCordinate) < min_x:
                    min_x = shape.xCordinate
                if (shape.yCordinate) < min_y:
                    min_y = shape.yCordinate
                if (shape.xCordinate + shape.base) > max_x:
                    max_x = shape.xCordinate + shape.base
                if (shape.yCordinate + shape.height) > max_y:
                    max_y = shape.yCordinate + shape.height
            
            elif shape.name == 'righttriangle-tl':
                if min_x == None: min_x = shape.xCordinate - shape.base
                if min_y == None: min_y = shape.yCordinate
                if max_x == None: max_x = shape.xCordinate
                if max_y == None: max_y = shape.yCordinate + shape.height
                if (shape.xCordinate - shape.base) < min_x:
                    min_x = shape.xCordinate - shape.base
                if (shape.yCordinate) < min_y:
                    min_y = shape.yCordinate
                if (shape.xCordinate) > max_x:
                    max_x = shape.xCordinate
                if (shape.yCordinate + shape.height) > max_y:
                    max_y = shape.yCordinate + shape.height
            
            elif shape.name == 'righttriangle-br':
                if min_x == None: min_x = shape.xCordinate
                if min_y == None: min_y = shape.yCordinate - shape.height
                if max_x == None: max_x = shape.xCordinate + shape.base
                if max_y == None: max_y = shape.yCordinate
                if (shape.xCordinate) < min_x:
                    min_x = shape.xCordinate
                if (shape.yCordinate - shape.height) < min_y:
                    min_y = shape.yCordinate - shape.height
                if (shape.xCordinate + shape.base) > max_x:
                    max_x = shape.xCordinate + shape.base
                if (shape.yCordinate) > max_y:
                    max_y = shape.yCordinate
            
            elif shape.name == 'righttriangle-bl':
                if min_x == None: min_x = shape.xCordinate - shape.base
                if min_y == None: min_y = shape.yCordinate - shape.height
                if max_x == None: max_x = shape.xCordinate
                if max_y == None: max_y = shape.yCordinate
                if (shape.xCordinate - shape.base) < min_x:
                    min_x = shape.xCordinate - shape.base
                if (shape.yCordinate - shape.height) < min_y:
                    min_y = shape.yCordinate - shape.height
                if (shape.xCordinate) > max_x:
                    max_x = shape.xCordinate
                if (shape.yCordinate) > max_y:
                    max_y = shape.yCordinate
            
            elif shape.name == 'equilateraltriangle-t':
                if min_x == None: min_x = shape.xCordinate - (shape.side / 2)
                if min_y == None: min_y = shape.yCordinate
                if max_x == None: max_x = shape.xCordinate + (shape.side / 2)
                if max_y == None: max_y = shape.yCordinate + (shape.median)
                if (shape.xCordinate - (shape.side / 2)) < min_x:
                    min_x = shape.xCordinate - (shape.side / 2)
                if (shape.yCordinate) < min_y:
                    min_y = shape.yCordinate
                if (shape.xCordinate + (shape.side / 2)) > max_x:
                    max_x = shape.xCordinate + (shape.side / 2)
                if (shape.yCordinate + shape.median) > max_y:
                    max_y = shape.yCordinate + (shape.median)
            
            elif shape.name == 'equilateraltriangle-b':
                if min_x == None: min_x = shape.xCordinate - (shape.side / 2)
                if min_y == None: min_y = shape.yCordinate - shape.median
                if max_x == None: max_x = shape.xCordinate + (shape.side / 2)
                if max_y == None: max_y = shape.yCordinate
                if (shape.xCordinate - (shape.side / 2)) < min_x:
                    min_x = shape.xCordinate - (shape.side / 2)
                if (shape.yCordinate - shape.median) < min_y:
                    min_y =shape.yCordinate - shape.median
                if (shape.xCordinate + (shape.side / 2)) > max_x:
                    max_x = shape.xCordinate + (shape.side / 2)
                if (shape.yCordinate) > max_y:
                    max_y = shape.yCordinate
            
            elif shape.name == 'equilateraltriangle-l':
                if min_x == None: min_x = shape.xCordinate - (shape.median)
                if min_y == None: min_y = shape.yCordinate - (shape.side / 2)
                if max_x == None: max_x = shape.xCordinate
                if max_y == None: max_y = shape.yCordinate + (shape.side / 2)
                if (shape.xCordinate - (shape.median)) < min_x:
                    min_x = shape.xCordinate - (shape.median)
                if (shape.yCordinate - (shape.side / 2)) < min_y:
                    min_y =shape.yCordinate - (shape.side / 2)
                if (shape.xCordinate) > max_x:
                    max_x = shape.xCordinate
                if (shape.yCordinate + (shape.side / 2)) > max_y:
                    max_y = shape.yCordinate + (shape.side / 2)
            
            elif shape.name == 'equilateraltriangle-r':
                if min_x == None: min_x = shape.xCordinate
                if min_y == None: min_y = shape.yCordinate - (shape.side / 2)
                if max_x == None: max_x = shape.xCordinate + (shape.median)
                if max_y == None: max_y = shape.yCordinate + (shape.side / 2)
                if (shape.xCordinate) < min_x:
                    min_x = shape.xCordinate
                if (shape.yCordinate - (shape.side / 2)) < min_y:
                    min_y =shape.yCordinate - (shape.side / 2)
                if (shape.xCordinate + (shape.median)) > max_x:
                    max_x = shape.xCordinate + (shape.median)
                if (shape.yCordinate + (shape.side / 2)) > max_y:
                    max_y = shape.yCordinate + (shape.side / 2)

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
            
            elif shape.name == 'quadrant-tr':
                ax.add_patch(MatWedge((shape.xCordinate, shape.yCordinate), shape.radius, 0, 90))
            
            elif shape.name == 'quadrant-tl':
                ax.add_patch(MatWedge((shape.xCordinate, shape.yCordinate), shape.radius, 90, 180))
            
            elif shape.name == 'quadrant-br':
                ax.add_patch(MatWedge((shape.xCordinate, shape.yCordinate), shape.radius, 270, 360))
            
            elif shape.name == 'quadrant-bl':
                ax.add_patch(MatWedge((shape.xCordinate, shape.yCordinate), shape.radius, 180, 270))
            
            elif shape.name == 'righttriangle-tr':
                ax.add_patch(MatPolygon([[shape.xCordinate, shape.yCordinate], [shape.xCordinate + shape.base, shape.yCordinate], [shape.xCordinate, shape.yCordinate + shape.height]]))
            
            elif shape.name == 'righttriangle-tl':
                ax.add_patch(MatPolygon([[shape.xCordinate, shape.yCordinate], [shape.xCordinate - shape.base, shape.yCordinate], [shape.xCordinate, shape.yCordinate + shape.height]]))
            
            elif shape.name == 'righttriangle-br':
                ax.add_patch(MatPolygon([[shape.xCordinate, shape.yCordinate], [shape.xCordinate + shape.base, shape.yCordinate], [shape.xCordinate, shape.yCordinate - shape.height]]))
            
            elif shape.name == 'righttriangle-bl':
                ax.add_patch(MatPolygon([[shape.xCordinate, shape.yCordinate], [shape.xCordinate - shape.base, shape.yCordinate], [shape.xCordinate, shape.yCordinate - shape.height]]))
            
            elif shape.name == 'equilateraltriangle-t':
                ax.add_patch(MatPolygon([[shape.xCordinate - (shape.side / 2), shape.yCordinate], [shape.xCordinate + (shape.side / 2), shape.yCordinate], [shape.xCordinate, shape.yCordinate + shape.median]]))
            
            elif shape.name == 'equilateraltriangle-b':
                ax.add_patch(MatPolygon([[shape.xCordinate - (shape.side / 2), shape.yCordinate], [shape.xCordinate + (shape.side / 2), shape.yCordinate], [shape.xCordinate, shape.yCordinate - shape.median]]))
            
            elif shape.name == 'equilateraltriangle-l':
                ax.add_patch(MatPolygon([[shape.xCordinate, shape.yCordinate - (shape.side / 2)], [shape.xCordinate, shape.yCordinate + (shape.side / 2)], [shape.xCordinate - shape.median, shape.yCordinate]]))
            
            elif shape.name == 'equilateraltriangle-r':
                ax.add_patch(MatPolygon([[shape.xCordinate, shape.yCordinate - (shape.side / 2)], [shape.xCordinate, shape.yCordinate + (shape.side / 2)], [shape.xCordinate + shape.median, shape.yCordinate]]))

        centroid = self.get_centroid()
        print(min_cor, max_cor)

        ax.plot([min_cor[0], max_cor[0]], [centroid[1], centroid[1]], color='yellow', alpha=0.3, linewidth=0.6)
        ax.plot([centroid[0], centroid[0]], [min_cor[1], max_cor[1]], color='yellow', alpha=0.3, linewidth=0.6)

        plt.plot(centroid[0], centroid[1], marker="o", markerfacecolor="red", markeredgecolor="yellow", label="Centroid")
        plt.legend(loc ="lower right")

        print(centroid)

        plt.show()
