# Activity: Clean Code Makeover and GitHub Upload
# Author: Ghalyela Rois BD O. Siladan | Grade & Section: 8-Narra
# Description: Calculates the distance of two points with clear comments.

import math

# Input variables and their values
x_1 = float(input("Enter x_1 : "))
x_2 = float(input("Enter x_2 : "))
y_1 = float(input("Enter y_1 : "))
y_2 = float(input("Enter y_2 : "))

# Use the distance formula (Cartesian Plane)
distance = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))

# Print the output to the console
print("The distance is:", distance)
