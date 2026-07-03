from .basic import *
from .advanced import *
from .geometry import *
from .statistics import *
from .randoms import *


class Math:
    # Basic
    add = staticmethod(add)
    subtract = staticmethod(subtract)
    multiply = staticmethod(multiply)
    divide = staticmethod(divide)
    modulus = staticmethod(modulus)
    power = staticmethod(power)
    floor_divide = staticmethod(floor_divide)

    # Advanced
    square_root = staticmethod(square_root)
    cube_root = staticmethod(cube_root)
    factorial = staticmethod(factorial)
    gcd = staticmethod(gcd)
    lcm = staticmethod(lcm)
    absolute = staticmethod(absolute)
    round_number = staticmethod(round_number)

    # Geometry
    circle_area = staticmethod(circle_area)
    circle_circumference = staticmethod(circle_circumference)
    rectangle_area = staticmethod(rectangle_area)
    rectangle_perimeter = staticmethod(rectangle_perimeter)
    triangle_area = staticmethod(triangle_area)

    # Statistics
    average = staticmethod(average)
    median = staticmethod(median)
    mode = staticmethod(mode)
    minimum = staticmethod(minimum)
    maximum = staticmethod(maximum)
    total = staticmethod(total)

    # Random
    random_int = staticmethod(random_int)
    random_float = staticmethod(random_float)
    choice = staticmethod(choice)
    shuffle = staticmethod(shuffle)