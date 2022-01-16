# NAME OF AUTHOR: Declan Seipp  
# NAME OF THE PROGRAM: Q2 RandomRange
# DATE OF CREATION: 1/13/2022
# PURPOSE OF PROGRAM: generate random number between two inputs

import random

# VARIABLE DEFINITION

# create variables for user inputs and random number
number1 = 0
number2 = 0
randomNumber = 0

# INPUT

# receive two numbers from user
numner1 = int(input("please insert your first number: "))
number2 = int(input("please insert your second number: "))


# PROCESSING

# generate random number betweem users two inputs
randomNumber = random.randint(number1, number2)


# OUTPUT

# print random number
print("your random number is: " + str(randomNumber))