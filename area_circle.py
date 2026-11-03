import math

def area(radius):
    area = math.pi * radius**2
    print(f"The area of circle is {area}")

def start():
    radius = float(input("Enter the radius"))
    area(radius)

start()