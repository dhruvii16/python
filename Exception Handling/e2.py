# def add(a,b):
#     sum=a+b
#     print("addition -" ,add)

# above program has limitation of passing of arguments sometimes user need to 10 numbers as input to sum 

def add(*a): # *args that means tuple and **args that means Dictionary
    print(a)

add(10,20)
add(20,50,30)