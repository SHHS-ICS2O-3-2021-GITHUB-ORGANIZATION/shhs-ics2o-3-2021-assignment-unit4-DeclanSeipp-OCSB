# NAME OF AUTHOR: Declan Seipp  
# NAME OF THE PROGRAM: number guessing game
# DATE OF CREATION: 1/24/2022
# PURPOSE OF PROGRAM: guess the random number between two user inputs

import random 

# VARIABLE DEFINITION ---------------------------------------

# create variables for the users inputs, users attempts, \the users guess, and the randomly generated number
number1 = 0
number2 = 0
randNum = 0
userAttemps = 0
userGuess = 0

# INPUT -----------------------------------------------------

# welcome user to the game (must do this before receiving user inputs)
print("welcome to the number game, where you will guess a random number. The number will be randomly generated in a range of your choice")
print("Hint: the larger the range, the harder it gets")
# receive inputs from user, put into variables
number1 = int(input("\nStart by entering your first number: "))
number2 = int(input("\nNow your second number: "))

# PROCESSING ------------------------------------------------

# generate random number from both user inputs
randNum = random.randint(number1, number2)

# receive first guess from user
userGuess = int(input("\nPlease enter your first guess: "))

# if user input does not equal randNum, act accordingly
while userGuess != randNum:
    if userGuess > randNum:
        # if user input is too high, tell user its too high, if too low, tell user its too low 
        print("\nToo high!")
        # receive new input/guess from user
        userGuess = int(input("\nPlease try again: "))
        # add 1 to userAttemps after every guess so we can display how many try's it took to guess the number
        userAttemps = userAttemps + 1
        
        # repeat last block of code for when userGuess is less than randNum
    if userGuess < randNum:
        print("\nToo low!")
        userGuess = int(input("\nPlease try again: "))
        userAttemps = userAttemps + 1 
        
# OUTPUT ----------------------------------------------------
        
# if user input is equal to randNum, tell user they won, and how many attempts it took
if userGuess == randNum:
    # add 1 to userAttemps to avoid getting an inaccurate attempt score/number
    userAttemps = userAttemps + 1
    # create special line of code for first attempt wins in order to maintain proper grammar
    if userAttemps == 1:
        print("\nCongratulations! you guessed the number " + str(randNum) + " on your first try! ")
    else: 
        print("\nCongratulations! you guessed the number " + str(randNum) + " in " + str(userAttemps) + " trys! ")