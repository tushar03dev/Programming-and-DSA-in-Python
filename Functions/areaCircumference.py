import math

def area_stats(radius):
    area = round (math.pi * radius ** 2,2)
    circumference = round (math.pi * radius * 2,2)
    return area, circumference

area, circumference = area_stats(4)
print(area)
print(circumference)