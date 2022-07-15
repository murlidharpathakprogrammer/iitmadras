'''
Problem 2: Write a Python code using functions
to calculate area and perimeter of circle and
rectangle
'''
#Approach 1: Standard code:

from turtle import pen


PI = 22/7

def circle_area(r):
    return (PI*r*r)

def circle_perimeter(r):
    return (2*PI*r)

def rect_area(l,b):
    return (l*b)

def rect_perimeter(l,b):
    return (2*(l+b))

radius = float(input("Enter the radius of the circle: "))
cArea = circle_area(radius)
print(f'\nThe area of the circle: {cArea}')
cPerimeter = circle_perimeter(radius)
print(f'\nThe perimeter of the circle: {cPerimeter}')
l = float(input("\nEnter the length of the rectangle: "))
b = float(input("Enter the breadth of the rectangle: "))
rArea = rect_area(l,b)
rPerimeter = rect_perimeter(l,b)
print(f'The area of the rectangle: {rArea}')
print(f'The perimeter of the rectangle: {rPerimeter}')