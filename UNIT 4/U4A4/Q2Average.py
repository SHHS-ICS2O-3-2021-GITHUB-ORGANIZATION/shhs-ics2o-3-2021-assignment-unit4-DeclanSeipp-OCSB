# NAME OF AUTHOR: Declan Seipp  
# NAME OF THE PROGRAM: Q2Average
# DATE OF CREATION: 1/18/2022
# PURPOSE OF PROGRAM: Calculate the sum, and average of a group of numbers


# VARIABLE DEFINITION
numbers = 0
sum_numbers = 0
average_numbers = 0

# INPUT

#receive numbers from the user, and put into list
numbers = list(map(int, input('Please enter your numbers, make sure to add a space between each one:\n ').split())) 

# PROCESSING

# find the amount of numbers input by the user
amount_numbers = len(numbers)
# add up all numbers to find the sum
sum_numbers = sum(numbers)
# divide the sum by the amount of numbers to get the average
average_numbers = sum_numbers / amount_numbers


# OUTPUT

#show user the sum and average of their numbers
print("\nthe average of all your numbers is: " + str(average_numbers))
print("the sum of your numbers is: " + str(sum_numbers))