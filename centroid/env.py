import matplotlib.pyplot as plt

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
            min_x, min_y, max_x, max_y = shape.get_min_max_cordinates(min_x, min_y, max_x, max_y)

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
            ax.add_patch(shape.get_graph_patch())

        centroid = self.get_centroid()

        ax.plot([min_cor[0], max_cor[0]], [centroid[1], centroid[1]], color='yellow', alpha=0.3, linewidth=0.6)
        ax.plot([centroid[0], centroid[0]], [min_cor[1], max_cor[1]], color='yellow', alpha=0.3, linewidth=0.6)

        plt.plot(centroid[0], centroid[1], marker="o", markerfacecolor="red", markeredgecolor="yellow", label="Centroid")
        plt.legend(loc ="lower right")


        plt.show()
    
    def view_shapes(self):

        count = 0
        colors = ['#C46210', '#2E5894', '#9C2542', '#A57164', '#58427C', '#4A646C', '#85754E', '#319177', '#8D4E85'] 

        fig, ax = plt.subplots()

        min_cor, max_cor = self.get_min_max_cordinates()


        for shape in self.shapes:
            ax.add_patch(shape.get_graph_patch(color=colors[count]))
            count += 1
            count = count % len(colors)

        centroid = self.get_centroid()

        ax.plot([min_cor[0], max_cor[0]], [centroid[1], centroid[1]], alpha=0)
        ax.plot([centroid[0], centroid[0]], [min_cor[1], max_cor[1]], alpha=0)

        plt.show()
