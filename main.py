
from package.env import Env
from package.shapes import Rectangle, SemiCircle, Quadrant, RightTriangle, EquilateralTriangle

def main():
    
    env = Env()

    env.add_shape(Rectangle(0, 0, 2, 2))    
    env.add_shape(EquilateralTriangle(1, 2, 2, 't'))    
    env.add_shape(EquilateralTriangle(1, 0, 2, 'b'))    
    env.add_shape(EquilateralTriangle(0, 1, 2, 'l'))    
    env.add_shape(EquilateralTriangle(2, 1, 2, 'r'))    

    for i in env.shapes: print(i)

    env.plot()


if __name__ == '__main__':
    main()