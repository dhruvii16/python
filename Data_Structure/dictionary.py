mydict = {
	'Name':'Het',
	'Enrollment No':12,
	'College Name':'BGKV'
}
print(mydict)
print(mydict['Name'])

#add or update
mydict['Company'] = 'TCS'
print(mydict)\

#get
print(mydict['Name'])

#clear
mydict.clear()
print(mydict)

#delete
del mydict['Company']
print(mydict)