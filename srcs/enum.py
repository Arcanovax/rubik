
from enum import Enum
from ursina import color


class Color_code(Enum):
    U = color.rgb32(255, 255, 0)
    R = color.rgb32(0, 128, 0)
    F = color.rgb32(255, 0, 0)
    D = color.rgb32(255, 255, 255)
    L = color.rgb32(0, 0, 255)
    B = color.rgb32(255, 165, 0)
