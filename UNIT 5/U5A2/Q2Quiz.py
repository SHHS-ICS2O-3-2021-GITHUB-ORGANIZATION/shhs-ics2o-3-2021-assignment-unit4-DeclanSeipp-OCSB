fileHandle = open ("Questions.txt", 'r')
contents = fileHandle.readline(100)
q1 = fileHandle.readline(10)
q2 = fileHandle.readline(10)
q3 = fileHandle.readline(10)
q4 = fileHandle.readline(10)
answer = fileHandle.readline(10)
print(contents)
print(q1)
print(q2)
print(q3)
print(q4)

userInput = input("answer: ")

if userInput == answer:
  print("congratulations")