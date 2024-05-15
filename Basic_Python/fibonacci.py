#Using simple iteration

num = 10
n1,n2 = 0,1
print('Fibonacci series is:',n1,n2,end=" ")
for i in range(2,num):
    n3 = n1+n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")
print()

#using recursive function
def fibonacciSeries(i):
    if i <= 1:
        return i
    else:
        return (fibonacciSeries(i - 1) + fibonacciSeries(i-2))
num = 10
if num <= 0:
    print('enter positive number')
else:
    print('fibonacci series:',end='')
for i in range(num):
    print(fibonacciSeries(i), end='')