# NAME OF AUTHOR: Declan Seipp  
# NAME OF THE PROGRAM: Q3 Taxes 
# DATE OF CREATION: 1/13/2022
# PURPOSE OF PROGRAM: Calculate the tax of 10 items 


# VARIABLE DEFINITION

Item1 = 0
Item2 = 0
Item3 = 0
Item4 = 0
Item5 = 0
Item6 = 0
Item7 = 0
Item8 = 0
Item9 = 0
Item10 = 0
Sum_of_items = 0
tax = 0
total = 0

# INPUT

#get price of all items from user
Item1 = int(input("please instert the price of item 1: "))
Item2 = int(input("please instert the price of item 2: "))
Item3 = int(input("please instert the price of item 3: "))
Item4 = int(input("please instert the price of item 4: "))
Item5 = int(input("please instert the price of item 5: "))
Item6 = int(input("please instert the price of item 6: "))
Item7 = int(input("please instert the price of item 7: "))
Item8 = int(input("please instert the price of item 8: "))
Item9 = int(input("please instert the price of item 9: "))
Item10 = int(input("please inster the price of item 10: "))

# PROCESSING

#add price of all items together to get price without tax
Sum_of_items = Item1 + Item2 + Item3 + Item4 + Item5 + Item6 + Item7 + Item8 + Item9 + Item10

#times by 15% to get tax 
tax = Sum_of_items * 0.15

#add tax and sum to get total cost
total = Sum_of_items + tax

# OUTPUT

#tell user the sum, tax, and total cost of all 10 items
print("\nthe sum of all your items is: $" + str(Sum_of_items))
print("\nthe tax on your items is: $" + str(tax))
print("\nthe total cost of your 10 items is: $" + str(total))