#/bin/pyton3.10
from xml.etree.ElementTree import PI
import enroll
enroll.print_enroll.enroll()

class area:
    def find_area(self,*args):
        if len(args) == 0:
            return "Invalid Input"
        elif len(args) == 2:
            if args[0] == "square":
                return (args[1]**2)
            elif args[0] == "circle":
                PI = 3.141
                return (PI*(args[1]**2))
        elif len(args) == 3:
            if args[0] == "triangle":
                return ((args[1]*args[2])/2)
            elif args[0] == "rectangle":
                return (args[1]*args[2])
            
shape_area = area()
square_area = shape_area.find_area("square",5)
circle_area = shape_area.find_area("circle",10)
triangle_area = shape_area.find_area("triangle",5,2)
rectangle_area = shape_area.find_area("rectangle",5,10)
print("Area of square :",square_area)        
print("Area of circle :",circle_area)        
print("Area of triangle :",triangle_area)
print("Area of recrtangle :",rectangle_area)        