import re

msg = input("Enter your message:")
patt = "pet:\w\w\w"

# Search example
result = re.search(patt, msg)

if result:
    print(result)
    print(result.group())
    print(result.span())
    print(result.string)
else:
    print("No match found.")
