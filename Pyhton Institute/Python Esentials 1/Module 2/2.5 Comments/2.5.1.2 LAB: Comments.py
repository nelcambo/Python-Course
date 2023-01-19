# LAB

# Estimated time
# 5 minutes

# Level of difficulty
# Very Easy

# Objectives
# becoming familiar with the concept of comments in Python;
# using and not using comments;
# replacing comments with code;
# experimenting with Python code.
# Scenario
# The code in the editor contains comments. Try to improve it: add or remove comments where you find it appropriate (yes, sometimes removing a comment can make the code more readable), and change variable names where you think this will improve code comprehension.

# NOTE

# Comments are very important. They are used not only to make your programs easier to understand, but also to disable those pieces of code that are currently not needed (e.g., when you need to test some parts of your code only, and ignore other). Good programmers describe each important piece of code, and give self-commenting names to variables, as sometimes it is simply much better to leave information in the code.

# It's good to use readable variable names, and sometimes it's better to divide your code into named pieces (e.g., functions). In some situations, it's a good idea to write the steps of computations in a clearer way.

# One more thing: it may happen that a comment contains a wrong or incorrect piece of information - you should never do that on purpose!


#--------------------------------------------------------------------------

#this program computes the number of seconds in a given number of hours
# this program has been written two days ago

#a = 2 # number of hours
#seconds = 3600 # number of seconds in 1 hour

#print("Hours: ", a) #printing the number of hours
# print("Seconds in Hours: ", a * seconds) # printing the number of seconds in a given number of hours

#here we should also print "Goodbye", but a programmer didn't have time to write any code
#this is the end of the program that computes the number of seconds in 3 hour

#--------------------------------------------------------------------------

#                          S  O  L  U  T  I  O  N 

#--------------------------------------------------------------------------

#this program computes the number of seconds in a given number of hours
# this program has been written two days ago

numberOfHours = 2 
conversion_rate = 3600 # number of seconds in 1 hour

print("Hours: ", numberOfHours) #printing the number of hours
print(f"Seconds in {numberOfHours} Hours: ", numberOfHours * conversion_rate) # printing the number of seconds in a given number of hours

print ("Thank you for trying our program.","Goodbye", sep="\n")
#this is the end of the program that computes the number of seconds in 2 hours.
