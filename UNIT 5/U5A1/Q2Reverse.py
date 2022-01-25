# NAME OF AUTHOR:Declan Seipp
# NAME OF THE PROGRAM: Q2Reverse 
# DATE OF CREATION: 1/25/2022
# PURPOSE OF PROGRAM: accept a word and output the word one letter at a time in reverse

# VARIABLE DEFINITION

# create variable for word/input
userInput = 0

# INPUT

# recieve word/input from user (put into str)
userInput = str(input("please insert your word: "))

# PROCESSING/OUPUT

# reverse word/input
userInput = userInput[::-1]
# for every letter in userInput, print the letter
for let in userInput:
    print(let)