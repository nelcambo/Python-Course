# The input() function - prohibited operations
# Look at the code in the editor. Run it, enter any number, and press Enter.

# What happens?

# Python should have given you the following output:

# Traceback (most recent call last):
# File ".main.py", line 4, in <module>
# something = anything ** 2.0
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'
# output


# The last line of the sentence explains everything - you tried to apply the ** operator to 'str' (string) accompanied with 'float'.

# This is prohibited.

# This should be obvious - can you predict the value of "to be or not to be" raised to the power of 2?

# We can't. Python can't either.

# Have we fallen into a deadlock? Is there a solution to this issue? Of course there is.


# Testing TypeError message.

anything = input("Enter a number: ")
something = anything ** 2.0
print(anything, "to the power of 2 is", something)
