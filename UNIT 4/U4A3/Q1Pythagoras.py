# NAME OF AUTHOR: Declan Seipp  
# NAME OF THE PROGRAM: Q1 Pythagoras
# DATE OF CREATION: 1/13/2022
# PURPOSE OF PROGRAM: calculate hypotenuse from two sides of a right angle trianlge

import math

# VARIABLE DEFINITION

# create variables for each side (including hypotenuse)
sideA = 0
sideB = 0
hyp = 0

# INPUT

# receive side lengths from user
sideA = int(input("please insert the first sides length: "))
sideB = int(input("please insert the second sides length: "))



# PROCESSING

# multiply each side by an exponent of 2, then add together
sideC = (sideA ** 2) + (sideB ** 2) 
# square root the sum of the last equation
hyp = math.sqrt(sideC)

# OUTPUT

# print the length of thehypotenuse
print("\nthe hypotenuse of your triangle is: " + str(hyp))