# Write a Python program which accepts the radius of a circle from the user and compute the area.
from math import pi, pow;

def run():
    radius = float(input("Enter the radius: "));
    print("The area of a circle is ", pi * pow(radius, 2));