# NAME OF AUTHOR: Declan Seipp
# NAME OF THE PROGRAM: Q2Quiz
# DATE OF CREATION: 1/26/2022
# PURPOSE OF PROGRAM: read the file and pose the question to the user

# VARIABLE DEFINITION

# open file with question and answers
infile = open('Questions.txt', 'r')
questions = str(infile.read())
infile.close()
# open file with correct answer (must open with str)
infile = open('answer.txt', 'r')
answer = str(infile.read())
infile.close()
# create variables for the users input, and amount of guesses
userInput = 0
guesses = 0

# INPUT/PROCESSING/OUTPUT

# display question to user
print(questions)
# receive first input from user(must be before while statement)
userInput = str(input("answer: "))
# create while statement for when incorrect answer is input
while userInput != answer:
    if userInput != answer:
        print("sorry, please try again")
        userInput = str(input("\nAnswer: "))
        # add 1 to guesses for guess counter 
        guesses = guesses + 1
        
# when correct answer is input
if userInput == answer:
    # add 1 to guesses to get correct number of attempts
    guesses = guesses + 1
    if guesses == 1:
        # create custom winning statement for first try wins
        print("\nCongratulations, you did it on your first try!")
    else:
        print("\nCorrect! you did it in " + str(guesses) + " trys!")









