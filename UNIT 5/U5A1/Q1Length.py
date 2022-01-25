# NAME OF AUTHOR:Declan Seipp
# NAME OF THE PROGRAM: Q1Length 
# DATE OF CREATION: 1/25/2022
# PURPOSE OF PROGRAM: accept a word from a user and return the length of that word

# VARIABLE DEFINITION

# create variables for word and word length
userInput = 0
wordLen = 0

# INPUT/PROCESSING/OUTPUT

# if userInput is quit, end loop/code
while userInput != "quit":
  userInput = str(input("\nplease insert your word: "))
  wordLen = len(userInput)
  print("the length of your word is: " + str(wordLen))
  