def simple_interest(amount,rate,year):
	ans = (amount + rate + year) / 100
	print(ans)

amount = int(input('Enter amount:'))
rate = int(input('Enter rate:'))
year = int(input('Enter year:'))

simple_interest(amount,rate,year)