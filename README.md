# Activity-Clean-Code-Makeover-and-GitHub-Upload
## I (Ghalyela, Siladan) will create a code of the previous activity of calculating the distance of two points but with CLEAR COMMENTS so others, most of all begginers or non-coders to understand my code.

# Don't Forget to put "import math" or else your math stuff (ex. math.pow) won't work
import math

## Input variables and their values
x_1 = float(input("Enter x_1 : "))
x_2 = float(input("Enter x_2 : "))
y_1 = float(input("Enter y_1 : "))
y_2 = float(input("Enter y_2 : "))

## Use the distance formula (Cartesian Plane)
distance = math.sqrt(math.pow( x_2 - x_1, 2 ) + math.pow( y_2 - y_1, 2 ))

## Print the output
print(distance)
