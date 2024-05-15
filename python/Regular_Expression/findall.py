import re

str = "the rain in india"
patt = "in"

mylist = re.findall(patt, str)
print(mylist)