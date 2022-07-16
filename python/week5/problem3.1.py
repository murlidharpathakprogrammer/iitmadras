'''
Problem 3: Write a Python code using functions
which checks whether the input coordinates form a
triangle or not
'''
#Approach 1: Using distance between points

def distance(xi,yi,xj,yj):
    return ((((xj-xi)**2)+((yj-yi)**2))**0.5)

def isTriangle(max, a, b):
    if((a+b)>max):
        print('\nTriangle')
    else:
        print('\nNot a Triangle')
        
x1 = float(input('Enter x coordinate of 1st point: '))
y1 = float(input('Enter y coordinate of 1st point: '))
x2 = float(input('Enter x coordinate of 2nd point: '))
y2 = float(input('Enter y coordinate of 2nd point: '))
x3 = float(input('Enter x coordinate of 3rd point: '))
y3 = float(input('Enter y coordinate of 3rd point: '))
d1 = distance(x1,y1,x2,y2)
print(f'\nDistance between points ({x1}, {y1}) and ({x2}, {y2}) = {d1}')
d2 = distance(x2,y2,x3,y3)
print(f'\nDistance between points ({x2}, {y2}) and ({x3}, {y3}) = {d2}')
d3 = distance(x3, y3, x1,y1)
print(f'\nDistance between points ({x3}, {y3}) and ({x1}, {y1}) = {d3}')
if(d1>d2):
    if(d1>d3):
        isTriangle(d1,d2,d3)
    else:
        isTriangle(d3,d1,d2)
elif(d2>d3):
    isTriangle(d2,d1,d3)
else:
    isTriangle(d3, d1, d2)