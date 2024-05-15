import re

#meta characters
# ^ Start
# $ End
# {} length
# + 1 or more
# . one char
# 0 or more
#[] allowed what you write in given square brackets

#pattern - ^[a-zA-Z]{2,10}$

#pattern = ^[0-9]{10}$

#RE Functions:- match search findall split sub

name = input('Enter Your Name:')
#patt = "^[a-zA-Z]{2,10}$"
patt = "^[a...d]{2,10}$"

# patt = "^ax+$"

#comapre name with pattern
result = re.match(patt,name)

if result is None:
	print('Invalid Name')
else:
	print('Your Name is:',name)