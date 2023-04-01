# String operators - introduction
# It's time to return to these two arithmetic operators: + and *.

# We want to show you that they have a second function. They are able to do something more than just add and multiply.

# We've seen them in action where their arguments are numbers (floats or integers, it doesn't matter).

# Now we're going to show you that they can handle strings, too, albeit in a very specific way.


# Concatenation
# The + (plus) sign, when applied to two strings, becomes a concatenation operator:

# string + string

# It simply concatenates (glues) two strings into one. Of course, like its arithmetic sibling, it can be used more than once in one expression, and in such a context it behaves according to left-sided binding.

# In contrast to its arithmetic sibling, the concatenation operator is not commutative, i.e., "ab" + "ba" is not the same as "ba" + "ab".

# Don't forget - if you want the + sign to be a concatenator, not an adder, you must ensure that both its arguments are strings.

# You cannot mix types here.

# This simple program shows the + sign in its second use:

fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")


# Note: using + to concatenate strings lets you construct the output in a more precise way than with a pure print() function, even if enriched with the end= and sep= keyword arguments.

# Run the code and see if the output matches your predictions.