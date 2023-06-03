
from centroid.env import Env
from centroid.shapes import (
    Rectangle, 
    Circle,
    SemiCircle, 
    Quadrant, 
    RightTriangle, 
    EquilateralTriangle
)

def main():
    
    env = Env()

    # env.add_shape(Rectangle(0, 0, 2, 2))
    # env.add_shape(Circle(0, 0, 2))
    env.add_shape(SemiCircle(0, 0, 2, 't'))
    env.add_shape(SemiCircle(0, 0, 2, 'b'))
    # env.add_shape(Quadrant(0, 0, 2, 'bl'))
    # env.add_shape(RightTriangle(0, 0, 2, 1, 'br'))  
    # env.add_shape(EquilateralTriangle(0, 0, 2, 'r'))

    for i in env.shapes: print(i)

    env.plot()


if __name__ == '__main__':
    main()