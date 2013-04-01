# Exercises for chapter 3:

# Name: Jenna Gopilan
# Github username: gynarchy10





# Exercise 3.1 
# Move the last line of this program to the top, so the function call appears before the definitions. Run the program and see what error message you get.

# def repeat_lyrics():
	# print_lyrics()
	# print_lyrics()

# def print_lyrics():
	# print "I'm a lumberjack, and I'm okay."
	# print "I sleep all night, and I work all day."

# repeat_lyrics()
	
#Error if the last line is place to the top:
# Traceback (most recent call last):
  # File "C:\Users\Jenna Gopilan\Documents\RampUp\10DayChallenge\dev-challenge\chapter3_exercises.py", line 6, in <module>
    # repeat_lyrics()
# NameError: name 'repeat_lyrics' is not defined	

#Reason for error:
#The function 'repeat_lyrics' is not defined yet - this is due to the flow of execution.





# Exercise 3.2 
# Move the function call back to the bottom and move the definition of print_lyrics after the definition of repeat_lyrics. What happens when you run this program?
# Result: it prints out the lyrics twice like below:

# I'm a lumberjack, and I'm okay.
# I sleep all night, and I work all day.
# I'm a lumberjack, and I'm okay.
# I sleep all night, and I work all day.

#Reason: The order of the function definitions does not matter as long as it is called for execution at the end.





# Exercise 3.3
# Write a function definition that right justifies a string, where the last letter is on the 70th column

# def right_justify(s):
	# length = len(s)
	# spaces = (70 - length) * " "
	# print spaces + s
	
# right_justify('allen')





# Exercise 3.4
# 1.Type example and test it

# def do_twice(f):
	# f()
	# f()

# def print_spam():
	# print 'spam'
	
# do_twice(print_spam)

# 2.modify the functions to have do_twice take two argument

# def do_twice(f,v):
	# f(v)
	# f(v)

# def print_spam(v):
	# print 'spam'
	
# do_twice(print_spam,'what')

# 3. make print spam more general

# def do_twice(f,v):
	# f(v)
	# f(v)

# def print_twice(v):
	# print v
	# print v
	
# do_twice(print_twice,'what')

# 4. 
# def do_twice(f,v):
	# f(v)
	# f(v)

# def print_twice(v):
	# print v
	# print v
	
# do_twice(print_twice,'spam')

5.
def do_twice(f,v):
	f(v)
	f(v)

def print_twice(v):
	print v
	print v

def do_four(f,v):
	do_twice(f,v)
	do_twice(f,v)
	
do_four(print_twice,'spam')
