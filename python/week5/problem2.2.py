'''
Problem 2: Write a Python code using functions
to calculate area and perimeter of circle and
rectangle
'''
# Approach 2: Menu driven code

from ast import While
import math

PI = math.pi

def circle_area(r):
    return (PI*r*r)

def circle_perimeter(r):
    return (2*PI*r)

def rect_area(l,b):
    return (l*b)

def rect_perimeter(l,b):
    return (2*(l+b))

polygon = ''
while(polygon!='exit'):
    print('\nPOLYGONS\ncircle\nrectangle\nexit')
    polygon = input('\nChoose the polygon type or exit: ')
    property = ''
    if(polygon=='circle'):
        r = float(input('\nEnter the radius of the circle: '))
        while(property==''):
            print("\nCIRCLE PROPERTIES\narea\nperimeter\nback")
            property  = input('\nChoose the circle property or go back: ')
            if(property=='area'):
                cArea = circle_area(r)
                print(f'Area of circle with radius {r} = {cArea} sq. units')
                property=''
            elif(property=='perimeter'):
                cPerimeter = circle_perimeter(r)
                print(f'Perimeter of circle with radius {r} = {cPerimeter} units')
                property=''
            elif(property=='back'):
                break
            else:
                print('Please select the correct polygon property')
                property=''
    elif(polygon=='rectangle'):
        l = float(input("\nEnter the length of the rectangle: "))
        b = float(input("Enter the breadth of the rectangle: "))
        while(property==''):
            print('\nRECTANGLE PROPERTIES\narea\nperimeter\nback')
            property = input('\nChoose the rectangle property or go back: ')
            if(property=='area'):
                rArea = rect_area(l,b)
                print(f'Area of rectangle with length {l} and breadth {b} is = {rArea}')
                property = ''
            elif(property=='perimeter'):
                rPerimeter = rect_perimeter(l,b)
                print(f'Perimeter of rectangle with length {l} and breadth {b} = {rPerimeter}')
                property = ''
            elif(property=='back'):
                break
            else:
                print('Please select the correct polygon property')
                property = ''
    elif(polygon=='exit'):
        break
    else:
        print('Please select the correct polygon type or exit')