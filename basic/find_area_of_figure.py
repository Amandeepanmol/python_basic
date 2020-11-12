#WAP to find the area of figure 

import math
def square(l):
    area=l*l
    return area

def rectangle(l,b):
    area=l*b
    return area

def circle(r):
    area=math.pi*r*r
    return area

def triangle(b,h):
    area=0.5*b*h
    return area


    
while 1:
    print("Enter ur choice 1.Square,2.Reactangle,3.Circle,4.Traingle,5.Quit")
    choice=int(input())
    if(choice==1):
        l=float(input("Enter length:"))
        area=square(l)
        print("Area of squrae is :",area)
    elif(choice==2):
        l=float(input("Enter length:"))
        b=float(input("Enter breadth:"))
        area=rectangle(l,b)
        print("Area of rectangle is :",area)
    elif(choice==3):
        r=float(input("Enter radius:"))
        area=circle(r)
        print("Area of circle is :",area)
    elif(choice==4):
        b=float(input("Enter breadth:"))
        h=float(input("Enter height:"))
        area=triangle(b,h)
        print("Area of triangle is :",area)
    elif(choice==5):
        break
    else:
        print("Please enter correct choice")
