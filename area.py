# to find area of a circle
import math # here math module is imported
r = float(input('Enter the radius: '))
area = math.pi * r**2 # pi is a constant in math module
print('Area of circle= ', area)
print('Area of circle= {:0.2f}'.format(area))
