# NAME OF AUTHOR: Declan Seipp  
# NAME OF THE PROGRAM: Q1 Volume 
# DATE OF CREATION: 1/13/2022
# PURPOSE OF PROGRAM: Calculate volume from the length, hight and width of an object


# VARIABLE DEFINITION

hight = 0
length = 0
width = 0
volume = 0

# INPUT

#get hight width and length from user
hight = int(input("please insert your objects hight: "))
length = int(input("please insert your objects length: "))
width = int(input("please insert your objects width: "))

#PROCESSIN

#times length width and hight together to get volume
volume = length * width * hight

# OUTPUT

#Tell user volume of their object
print("the volume of your object is: " + str(volume))