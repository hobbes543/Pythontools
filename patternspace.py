# This script is to calculate the pattern spacing given a desired start, length 
# and number of instances.

# Usage: From command prompt in directory where script is located,
# python patternspace.py l q n where:
# l = overall length as a decimal value 
# q = quantity of patterned feature as an integer value
# n = distance from edge to place first feature as a decimal value 
# The output of the script is s
# s = spacing of patterned feature as a decimal value

# Example Usage:
# C:\..\<Folder script is saved in>\python patternspace.py 34.5 17 1.25
# 2.0 <-- Output Value.

# Notes:
# 	1). Script is unit independent.
#	2). It is up to user to keep units consistant. l and n should be in same 
#		units.
#	3). Output will be in same units as inputs l and n.
#	4). q MUST BE A WHOLE NUMBER

import sys

l = float(sys.argv[1])
q = int(sys.argv[2])
n = float(sys.argv[3])

# Calculate length of pattern

pl = l - (n * 2)

# Calculate Spacing

s = pl / (q - 1)

print (s)