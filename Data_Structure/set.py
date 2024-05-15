myset = {'a','b','c','d'} #unorderd list
#print(myset)

#add
myset.add('F')
print(myset)

#one set into another
myset1 = {'F','G','H'}
myset.update(myset1)
print(myset)

#delete
myset.remove('d')
print(myset)

myset.pop()
print(myset)

myset.clear()
print(myset)

del myset
print(myset)