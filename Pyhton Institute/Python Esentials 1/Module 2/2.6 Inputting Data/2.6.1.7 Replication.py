# Replication
# The * (asterisk) sign, when applied to a string and number (or a number and string, as it remains commutative in this position) becomes a replication operator:

# string * number
# number * string


# It replicates the string the same number of times specified by the number.

# For example:

# "James" * 3 gives "JamesJamesJames"
# 3 * "an" gives "ananan"
# 5 * "2" (or "2" * 5) gives "22222" (not 10!)

# REMEMBER

# A number less than or equal to zero produces an empty string.


# This simple program "draws" a rectangle, making use of an old operator (+) in a new role:

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")


# Note the way in which we've used the parentheses in the second line of the code.

# Try practicing to create other shapes or your own artwork!

