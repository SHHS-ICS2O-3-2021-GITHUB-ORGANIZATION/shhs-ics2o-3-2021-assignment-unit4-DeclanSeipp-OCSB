# NAME OF AUTHOR: Declan Seipp
# NAME OF THE PROGRAM: Q3Primes  
# DATE OF CREATION: 1/21/2022 
# PURPOSE OF PROGRAM: output all prime numbers between two user inputs

# VARIABLE DEFINITION

# create varaiables for each number the user will input
number1 = 0
number2 = 0

# INPUT

# receive both numbers from user
number1 = int(input("please insert your first number: "))
number2 = int(input("please insert your second number: "))

# PROCESSING/OUPUT

# (must print before processing) 
print("\nPrime numbers between " + str(number1) + " and " + str(number2) + " are: ")

# print all prime numbers betwen the two user inputs 
for num in range(number1, number2 + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)