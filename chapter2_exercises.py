# Exercises for chapter 2:

# Name: Jenna Gopilan
# Github username: gynarchy10

#Chapter 2.1 
# Figure out what happens when an integer with a leading zero is printed, the result is not the same as the value entered.
#	Investigating the hint: 01, 010, 0100 = type is int
#	Using the hint: 
#		when 01 is entered, the result is 1; 
#		when 010 is entered, the result is 8; 
#		when 0100 is entered, the result is 64;  
#		when 01000 is entered, the result is 512
#	From the hint: It seems depending on the number (n) of zeros after 1, 8 is raised to the power of (n)
#	So: 
#		1 is 8**0 = 1; 
#		010 is 8**1 = 8; 
#		0100 is 8**2 = 64; 
#		01000 is 8***3 = 512
#	And: 
#		2 is 2(8**0) = 2; 
#		020 is 2(8**1) = 16; 
#		0200 is 2(8**2) = 128; 
#		02000 is 2(8**3) = 1024
#	With additional numbers on the 3rd index: 
#		011 is 1+(8**1) = 9; 
#		0101 is 1+(8**2) = 65
#	Continue to test other numbers: 
#		when 8 and 9 are entered after a leading 0, an error is returned
#	Observation: Using this system - one can count from 0 to a huge number
#	Hypothesis: Using the "0" at a start of the integer prompts base 8 numerical count
#	************
#	***ANSWER***
#	************
#	The leading 0 initializes a base 8 count (or Octal) 



#Chapter 2.2
# when typed in an interpreter:
#	5: the output is 5
#	x = 5: there is no output
#	x + 1: the output is 6
#when typed into a script and ran
#	there is no output
#when script is modified and added a print statement, the output is:
#	5
#	6



#Chapter 2.3
#Assignments:
#	width = 17
#	height = 12.0
#	delimiter = '.'
#Note: variables adopt the type of the assignments
#Types of the assignment:
#	width is int
#	height is float
#	delimiter is string
#Exercise:
#1. width/2
#		value: 8
#		type: int
#2. width/2.0
#		value:8.5
#		type: float
#3. height/3
#		value: 4.0
#		type: float
#4. 1 + 2 * 5
#		value: 11
#		type: string
#5. delimiter * 5
#		value: '.....'
#		type: string


#Chapter 2.4
#1. The volume of the sphere with radius r is 4/3(pi r^3). What is the volume of a sphere with radius 5?
# #	Hint: 392.7 is wrong (from: 4/3*3.14*125)
# r = 5
# volume = (4.0/3.0)*3.14*(r**3)
# print "Chapter 2.4, Q1: volume of the sphere with radius 5 is " + repr(volume)
# Another approach:
from math import pi
r = 5
volume = (4.0/3.0)*pi*(r**3)
print "Chapter 2.4, Q1: volume of the sphere with radius 5 is " + repr(volume)



#2. cover price for book is $24.95
#	bookstores get 40% off
#	shipping costs $3 for the first copy and 75 cents for additional copy
#	cost for 60 copies?
#Answer:
n = 60
book = 24.95-(24.95*.4)
ship = (3*(n-(n-1))) + (.75*(n-1))
total = (book * n) + ship
print "Chapter 2.4, Q2: total price in dollars is " + repr(total)




#3. leave at 6:52 am
#	run 1 mile at 8:15/mile
#	run 3 miles at 7:12/mile
#	run 1 mile at 8:15/mile
#	time of arrival at home?
#	give answer in hour, minute, and seconds
#Answer:
minute = 60
hour = 60*minute
start = (6*hour) + (52*minute)
run = (2*((8*minute)+15)) + (3*((7*minute)+12))
arrive = start + run
arrivehour= arrive/hour
arriveminute = (arrive%hour)/minute
arrivesecond = arrive%arriveminute
print "Chapter 2.4, Q3: arrive back home at " + repr(arrivehour) +":"+repr(arriveminute)+ ":" + repr(arrivesecond) +" am"



