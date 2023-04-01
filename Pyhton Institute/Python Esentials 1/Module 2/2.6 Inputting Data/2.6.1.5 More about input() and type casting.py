# More about input() and type casting
# Having a team consisting of the trio input()-int()-float() opens up lots of new possibilities.

# You'll eventually be able to write complete programs, accepting data in the form of numbers, processing them and displaying the results.

# Of course, these programs will be very primitive and not very usable, as they cannot make decisions, and consequently are not able to react differently to different situations.

# This is not really a problem, though; we'll show you how to overcome it soon.

# Our next example refers to the earlier program to find the length of a hypotenuse. Let's rewrite it and make it able to read the lengths of the legs from the console.

# Check out the editor window - this is how it looks now.

# The program asks the user twice for both legs' lengths, evaluates the hypotenuse and prints the result.

# Run it and try to input some negative values.

# The program - unfortunately - doesn't react to this obvious error.

# Let's ignore this weakness for now. We'll come back to it soon.

# Note that in the program that you can see in the editor, the hypo variable is used for only one purpose - to save the calculated value between the execution of the adjoining line of code.

# As the print() function accepts an expression as its argument, you can remove the variable from the code.

# Just like this:


leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = round((leg_a**2 + leg_b**2) ** .5, 2)
# hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)
