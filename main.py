
from centroid.env import Env
from centroid.shapes import (
    Rectangle, 
    Circle,
    SemiCircle, 
    Quadrant, 
    RightTriangle, 
    EquilateralTriangle
)


def pause():
    input("Press enter to continue: ")

def get_one_lettered_shape_type():
    
    while True:
        print("\nt = top\nb = bottom\nl = left\nr = right")
        shape_type = input("Enter shape type: ").strip().lower()

        if shape_type not in ['t', 'b', 'l', 'r']:
            print("Invalid shape type")
            continue
        break

    return shape_type


def get_two_lettered_shape_type():
    
    while True:
        print("\ntr = top right\ntl = top left\nbr = bottom right\nbl = bottom left")
        shape_type = input("Enter shape type: ").strip().lower()

        if shape_type not in ['tr', 'tl', 'br', 'bl']:
            print("Invalid shape type")
            continue
        break

    return shape_type


def input_number(text, field):

    while True:
        num = input(text)
        try:
            float(num)
        except:
            print(f"{field.capitalize()} should a number")
            continue
        break

    return float(num)


def input_pos_number(text, field):

    while True:
        num = input(text)
        try:
            num = float(num)
        except:
            print(f"{field.capitalize()} should a number")
            continue
        else:
            if float(num) < 0:
                print(f"{field.capitalize()} should a positive number")
                continue
        break

    return num


def get_cordinates():

    x = input_number("Enter X Cordinate: ", "X Cordinate")
    y = input_number("Enter Y Cordinate: ", "Y Cordinate")

    return x, y
    

def home_page():
    print("\n")

    print("------------ Home ------------")
    print("1. Add Shape")
    print("2. View Shapes")
    print("3. Remove Shape")
    print("4. Remove All Shapes")
    print("5. Calculate Centroid")
    print("6. Exit")
    choice = input("Enter Choice: ").strip()

    if choice == '1':
        add_shape_page()
    elif choice == '2':
        view_shapes()
    elif choice == '3':
        remove_shape_page()
    elif choice == '4':
        remove_all_shapes()
    elif choice == '5':
        calculate_centroid()
    elif choice == '6':
        return None
    else:
        print("Invalid choice")
        pause()
        home_page()


def add_shape_page():
    print("\n")
    
    print("--------- Add Shapes ---------")
    print("1. Add Rectangle")
    print("2. Add Circle")
    print("3. Add Semicircle")
    print("4. Add Quadrant")
    print("5. Add Right Triangle")
    print("6. Add Equilateral Triangle")
    print("7. Back to Home Page")
    choice = input("Enter Choice: ").strip()

    if choice == '1':
        add_rectangle_page()
    elif choice == '2':
        add_circle_page()
    elif choice == '3':
        add_semicircle_page()
    elif choice == '4':
        add_quadrant_page()
    elif choice == '5':
        add_righttriangle_page()
    elif choice == '6':
        add_equilateraltriangle_page()
    elif choice == '7':
        home_page()
    else:
        print("Invalid choice")
        pause()
        add_shape_page()


def add_rectangle_page():
    print("\n")
    
    xCor, yCor = get_cordinates()
    length = input_number("Enter length: ", "length")
    breadth = input_pos_number("Enter breadth: ", "breadth")

    shape = Rectangle(xCor, yCor, length, breadth)
    env.add_shape(shape)
    print(f"\nShape Added: {shape}")

    pause()
    add_shape_page()


def add_circle_page():
    print("\n")
    
    xCor, yCor = get_cordinates()
    radius = input_pos_number("Enter radius: ", "radius")

    shape = Circle(xCor, yCor, radius)
    env.add_shape(shape)
    print(f"\nShape Added: {shape}")

    pause()
    add_shape_page()


def add_semicircle_page():
    print("\n")
    
    xCor, yCor = get_cordinates()
    radius = input_pos_number("Enter radius: ", "radius")
    shape_type = get_one_lettered_shape_type()

    shape = SemiCircle(xCor, yCor, radius, shape_type)
    env.add_shape(shape)
    print(f"\nShape Added: {shape}")

    pause()
    add_shape_page()


def add_quadrant_page():
    print("\n")
    
    xCor, yCor = get_cordinates()
    radius = input_pos_number("Enter radius: ", "radius")
    shape_type = get_two_lettered_shape_type()

    shape = Quadrant(xCor, yCor, radius, shape_type)
    env.add_shape(shape)
    print(f"\nShape Added: {shape}")

    pause()
    add_shape_page()


def add_righttriangle_page():
    print("\n")
    
    xCor, yCor = get_cordinates()
    base = input_pos_number("Enter base: ", "base")
    height = input_pos_number("Enter height: ", "height")
    shape_type = get_two_lettered_shape_type()

    shape = RightTriangle(xCor, yCor, base, height, shape_type)
    env.add_shape(shape)
    print(f"\nShape Added: {shape}")

    pause()
    add_shape_page()


def add_equilateraltriangle_page():
    print("\n")
    
    xCor, yCor = get_cordinates()
    side = input_pos_number("Enter side: ", "side")
    shape_type = get_one_lettered_shape_type()

    shape = EquilateralTriangle(xCor, yCor, side, shape_type)
    env.add_shape(shape)
    print(f"\nShape Added: {shape}")

    pause()
    add_shape_page()


def view_shapes():
    print("\n")

    if (len(env.shapes) > 0):
        for i in env.shapes: print(i)
        env.view_shapes()
    else:
        print("No shapes added yet!")


    pause()
    home_page()


def remove_shape_page():
    print("\n")

    if (len(env.shapes) == 0):

        print("No shapes added yet!")
        pause()
        home_page()

    else:

        count = 1
        for i in env.shapes:
            print(f"{count}. {i}")
            count += 1

        choice = input("Enter the shape index to remove (enter e to exit): ")
        
        if choice.lower() == 'e':
            home_page()
        else:
            try:
                if int(choice) <= 0:
                    print("Invalid choice")
                    pause()
                    remove_shape_page()

                elif env.shapes[int(choice) - 1] is None:
                    print("Invalid choice")
                    pause()
                    remove_shape_page()
                else:
                    print(f"Removed {env.shapes[int(choice) - 1]}")
                    env.shapes.pop(int(choice) - 1)
                    pause()
                    home_page()

            except:
                print("Invalid choice")
                pause()
                remove_shape_page()


def remove_all_shapes():
    print("\n")

    if (len(env.shapes) == 0):

        print("No shapes added yet!")
        pause()
        home_page()

    else:

        env.shapes = []
        print("Removed all shapes.")
        pause()
        home_page()


def calculate_centroid():
    print("\n")

    if (len(env.shapes) == 0):

        print("No shapes added yet!")
        pause()
        home_page()

    else:

        print(f"Centroid: {env.get_centroid()}")
        env.plot()
        home_page()



env = None

def main():

    global env
    env = Env()

    print("\n- Find Centroid of a 2D Shape -")
    home_page()


if __name__ == '__main__':
    main()