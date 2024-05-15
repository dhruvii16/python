try:
    div = 4//0
    print(div)

except ZeroDivisionError:
    print('Divide by zero')
finally:
    print('Finally code')
