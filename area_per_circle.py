#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Nov. 25, 2021
# This program calculates the area and perimeter of a circle with
# a radius of 15mm


import math

# Radius of the circle.
rad = 15

# Calculate the area.
per_circle = 2 * rad * math.pi

# Calculate the perimeter
area_circle = math.pi * (rad ** 2)

# Print the final values
print("The area would be: {}".format(area_circle) + " mm^2")
print("The circumference would be: {}".format(per_circle) + " mm")
