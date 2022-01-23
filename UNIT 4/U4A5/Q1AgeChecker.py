# NAME OF AUTHOR: Declan Seipp
# NAME OF THE PROGRAM: Q1AgeChecker  
# DATE OF CREATION: 1/21/2022 
# PURPOSE OF PROGRAM: tell person what part of school they are in (elementary, intermediate, etc)

# VARIABLE DEFINITION

# create varaiable for age of user
age = 0

# INPUT

# recieve age from user via input
age = int(input("Please insert your age: "))

# PROCESSING/OUTPUT

# use if statement and range command to determine what age group user is in (must create statement for last year of school (11, 14, 18, etc))
if age > 19:
   print("You aren't in school anymore")
if age == 19:
   print("You are in university/college")
if age == 18:
   print("you are in high school")
if age in range(15,18):
   print("you are in high school")
if age == 14:
   print("you are in intermediate school")
if age in range(12,14):
   print("you are in intermediate school")
if age == 11:
   print("You are in elementary school")
if age in range(5,11):
   print("You are in elementary school")
