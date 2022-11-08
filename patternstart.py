# This script is designed to calculate the start position from an edge for a 
# centered pattern, given overall length, number of instances and spacing.

# Usage: From command prompt in directory where script is located,
# python patternstart.py l q s where:
# l = overall length as a decimal value 
# q = quantity of patterned feature as an integer value 
# s = spacing of patterned feature as a decimal value
# The output of the script is n
# n = distance from edge to place first feature as a decimal value

# Example Usage:
# C:\..\<Folder script is saved in>\python patternstart.py 34.5 17 2.00
# 1.25 <-- Output Value.

# Notes:
# 	1). Script is unit independent.
#	2). It is up to user to keep units consistant. l and s should be in same 
#		units.
#	3). Output will be in same units as inputs l and s.
#	4). q MUST BE A WHOLE NUMBER

import sys

l = float(sys.argv[1])
q = int(sys.argv[2])
s = float(sys.argv[3])
	
# check if pattern is valid
if (q - 1) * s > l:
	print ("Pattern is not valid!")

# check for pattern of 1
elif (q - 1) == 0:
	n = l / 2
	print (n)
			
# Length of pattern
else:
	lp = (q - 1) * s

# Remaining Length
	rl = l - lp

# Calculate Starting Positon
	n = rl / 2

	print (n)