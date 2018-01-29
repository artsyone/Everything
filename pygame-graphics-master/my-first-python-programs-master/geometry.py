# This program contains functions that evaluate formulas used in geometry.
#
# Your Name
# August 22, 2014

import math

def triangle_area(b, h):
    a = (1/2) * b * h
    return a

def circle_area(r):
    a = math.pi * r**2
    return a

def parallelogram_area(b,h):
    a = b * h
    return a
def trapezoid_area(a,b,h):
    a = (a + b)/2 * h
    return a

def rectangularprism_volume(w,h,l):
    v = w*h*l
    return v

def cone_volume(r,h):
    
    v = 3.14 * r ** 2 /h/3
    return v

def sphere_volume(r):
    v = 4/3 * 3.14 * r ** 3
    return v

def surfacearea_sphere(r):
    a = 4 * 3.14 * r ** 2
    return a

def hypo_right(b,c):
    a = b ** 2 + c ** 2
    
    return a


def rectangular_surfacearea(w,h,l):
    v = 2 *( w*l + h * l + h * w )
    return v

 
# function calls
print(triangle_area(4,9))
print(circle_area(5))

print(parallelogram_area(3,5))
print(trapezoid_area(6,5,4 ))
print(rectangularprism_volume(6,5,4 ))
print(cone_volume(5,3))
print(sphere_volume(5))
print(surfacearea_sphere(4))
print(hypo_right(8,3))
print(rectangular_surfacearea(6,5,4 ))
