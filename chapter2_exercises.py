# Exercises for chapter 2:

# Name: Jenna Gopilan
# Github username: gynarchy10

#Chapter 2.1 Figure out what happens when an integer with a leading zero is printed, the result is not the same as the value entered.
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




#Chapter 2.4