
from package.env import Env
from package.shapes import Rectangle, SemiCircle

def main():
    
    env = Env()

    env.add_shape(Rectangle(5, 5, 5, 5))
    # env.add_shape(SemiCircle(5, 7.5, 2.5, 'l'))
    env.add_shape(SemiCircle(10, 7.5, 2.5, 'r'))
    # env.add_shape(SemiCircle(7.5, 5, 2.5, 'b'))
    env.add_shape(SemiCircle(7.5, 10, 2.5, 't'))

    for i in env.shapes: print(i)

    env.plot()


if __name__ == '__main__':
    main()