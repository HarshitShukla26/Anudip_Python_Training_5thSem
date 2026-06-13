#Module to calculate area and perimeter of 2d figures

#for rectangle
def rectangle_area(length,breadth):
    return length*breadth

def rectangle_perimeter(length,breadth):
    return 2*(length+breadth)

#for square
def square_area(side):
    return side*side

def square_perimeter(side):
    return 4*side

#for cirle
def circle_area(radius):
    return 3.14*radius*radius

def circle_perimeter(radius):
    return 2*3.14*radius

#for triangle
def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c))**0.5
    return area

def triangle_perimeter(a,b,c):
    return a+b+c