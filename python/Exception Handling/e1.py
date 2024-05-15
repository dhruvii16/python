mylist = ['Orange','Banana','Apple','Bluebarry']
# print(mylist[4])
try:
    print(mylist[4])
except:
    print("index Error")


# name error -- variable does not exist
# index error --list if not avaliable value 
# number error -- factorial if we are given number in negative so give error

# try and Except
# if any errors than go to Except    
print("---------Factorial---------")

from math import factorial

num=int(input('enter a number :'))

try:
    ans = factorial(num)
    print(ans)
except NameError as msg:
    print(msg)
except IndexError as e:
    print(e)
except ValueError as v:
    print(v)
except Exception as ex:
    print(ex)   
    