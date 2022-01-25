# NAME OF AUTHOR:Declan Seipp
# NAME OF THE PROGRAM: Q3WordTriangle
# DATE OF CREATION: 1/25/2022
# PURPOSE OF PROGRAM:  prompt the user for a word, and return a 'word triangle'

# VARIABLE DEFINITION

# create variable for word/input
userInput = 0

# INPUT

# recieve word/input from suer
userInput = str(input("please insert your word: "))

# PROCESSING/OUPUT

# create word triangle
for row in range(len(userInput)):
  # after each print, add 1 row/letter
    for col in range(row+1):
        print(userInput[col],end=' ')
    print()