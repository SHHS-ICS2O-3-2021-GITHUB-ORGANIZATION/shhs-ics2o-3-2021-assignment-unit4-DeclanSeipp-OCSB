# NAME OF AUTHOR: Declan Seipp  
# NAME OF THE PROGRAM: Q1Counting
# DATE OF CREATION: 1/18/2022
# PURPOSE OF PROGRAM: count up by a user input to a user input


# VARIABLE DEFINITION

# create variables for user inputs and random number
userinput =  0
count = 0
counter = 0

# INPUT

# receive numbers from user
userinput = int(input("Welcome to Q1Counting, please insert a large number: "))
count = int(input("please insert the number you would like to count by: "))

# Used to reverse the counting process, and count down
negativeCount = count * -1

# PROCESSING/OUTPUT

# count up by the users input, to the users input
print("")
for counter in range(0, userinput + 1, count):
    print (counter)
print("")
for counter in range(userinput, -1, negativeCount):
    print (counter)



