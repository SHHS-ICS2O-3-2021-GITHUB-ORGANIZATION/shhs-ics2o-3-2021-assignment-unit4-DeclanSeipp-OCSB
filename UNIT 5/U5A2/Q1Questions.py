# NAME OF AUTHOR:Declan Seipp
# NAME OF THE PROGRAM: Q1Questions
# DATE OF CREATION: 1/25/2022
# PURPOSE OF PROGRAM:  accept a multiple choice question, four answers, and the letter of correct answer

# VARIABLE DEFINITION

# create variables for the question, 4 answers, and correct answer
question = 0
answer = 0
a = 0
b = 0
c = 0
d = 0

# INPUT

# receive each input from user, put into variables
question = str(input("please type your question: "))
a = str(input("please type answer a: "))
b = str(input("please type answer b: "))
c = str(input("please type answer c: "))
d = str(input("please type answer d: "))
answer = str(input("what is the correct answer?: "))

# PROCESSING

# open file 
filehandle = open("Questions.txt", 'w')
# put each part of quiz on different line (makes it easier in part 2)
filehandle.write(question + '\n')
filehandle.write(a +'\n')
filehandle.write(b +'\n')
filehandle.write(c +'\n')
filehandle.write(d +'\n')
# close/save file
filehandle.close()

# open file 
filehandle = open("answer.txt", 'w')
filehandle.write(answer)
# close/save file
filehandle.close()
