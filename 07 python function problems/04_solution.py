import math

def CircleMeasure(radius):
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    return area,circumference

print(CircleMeasure(5))