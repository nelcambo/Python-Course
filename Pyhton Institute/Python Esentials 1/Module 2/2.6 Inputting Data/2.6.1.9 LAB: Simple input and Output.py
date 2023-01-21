# LAB

# Estimated time
# 5-10 minutes

# Level of difficulty
# Easy

# Objectives
# becoming familiar with the inputting and outputting of data in Python;
# evaluating simple expressions.
# Scenario
# Your task is to complete the code in order to evaluate the results of four basic arithmetic operations.

# The results have to be printed to the console.

# You may not be able to protect the code from a user who wants to divide by zero. That's okay, don't worry about it for now.

# Test your code - does it produce the results you expect?

# We won't show you any test data - that would be too simple.


 
# Sandbox
# Code

# input a float value for variable a here
# input a float value for variable b here

# output the result of addition here
# output the result of subtraction here
# output the result of multiplication here
# output the result of division here

# print("\nThat's all, folks!")
# input a float value for variable a here


#--------------------------------------------------------------------------

#                          S  O  L  U  T  I  O  N 

#--------------------------------------------------------------------------


a = float(input("Enter a float number here: "))
b = float(input("Enter another float number here: "))

print(f"The result of the addition of a={a} and b={b} is: {a+b}")
print(f"The result of the subtraction of a={a} and b={b} is: {a-b}")
print(f"The result of the multiplication of a={a} and b={b} is: {a*b}")
print(f"The result of the division of a={a} and b={b} is: {a/b}")

print("\nThat's all, folks!")


