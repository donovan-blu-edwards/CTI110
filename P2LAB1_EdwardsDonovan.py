# Donovan Edwards
# Apr. 9th 2026
# P2LAB1
# Python script for calculating the properties of a circle based on it's radius

import math

PI = math.pi

print("What is the radius of the circle?", end=" ")
circleRadius = float(input())

circleDiameter = circleRadius * 2.0
circleCircumference = 2.0 * PI * circleRadius
circleArea = PI * circleRadius**2.0

print("The diameter of the circle is", f"{circleDiameter:.1f}")
print("The circumference of the circle is", f"{circleCircumference:.2f}")
print("The area of the circle is", f"{circleArea:.3f}")
