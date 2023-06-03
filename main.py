
from package.env import Env
from package.shapes import Rectangle, SemiCircle, Quadrant

def main():
    
    env = Env()

    # env.add_shape(Rectangle(5, 5, 5, 5))
    # env.add_shape(SemiCircle(5, 7.5, 2.5, 'l'))
    # env.add_shape(SemiCircle(10, 7.5, 2.5, 'r'))
    # env.add_shape(SemiCircle(7.5, 5, 2.5, 'b'))
    # env.add_shape(SemiCircle(7.5, 10, 2.5, 't'))
    env.add_shape(Quadrant(0, 0, 5, 'tr'))
    env.add_shape(Quadrant(0, 0, 5, 'tl'))
    env.add_shape(Quadrant(0, 0, 5, 'br'))
    env.add_shape(Quadrant(0, 0, 5, 'bl'))

    for i in env.shapes: print(i)

    env.plot()


if __name__ == '__main__':
    main()