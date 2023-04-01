# Equality: the equal to operator (==)
# The == (equal to) operator compares the values of two operands. If they are equal, the result of the comparison is True. If they are not equal, the result of the comparison is False.

# Look at the equality comparison below - what is the result of this operation?

#var == 0

# Note that we cannot find the answer if we do not know what value is currently stored in the variable var.

# If the variable has been changed many times during the execution of your program, or its initial value is entered from the console, the answer to this question can be given only by Python and only at runtime.

# Now imagine a programmer who suffers from insomnia, and has to count black and white sheep separately as long as there are exactly twice as many black sheep as white ones.

# The question will be as follows:

#black_sheep == 2 * white_sheep

# Due to the low priority of the == operator, the question shall be treated as equivalent to this one:

var = 0  # Assigning 0 to var
print(var == 0)

var = 1  # Assigning 1 to var
print(var == 0)

# Run the code and check if you were right.

# Inequality: the not equal to operator (!=)
# The != (not equal to) operator compares the values of two operands, too. Here is the difference: if they are equal, the result of the comparison is False. If they are not equal, the result of the comparison is True.

# Now take a look at the inequality comparison below - can you guess the result of this operation?

var = 0  # Assigning 0 to var
print(var != 0)

var = 1  # Assigning 1 to var
print(var != 0)

# Run the code and check if you were right.