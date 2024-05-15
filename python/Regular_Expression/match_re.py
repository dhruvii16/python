import re

msg = input("Enter your message:")
patt = "pet:\w\w\w"

#match example
#result = re.match(patt,msg)
#print(result)
#print(result.span())
#print(result.string)

#search example
result = re.search(patt,msg)
print(result)
print(result.group())
print(result.span())
print(result.string)