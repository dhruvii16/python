voterid = input('Do you have voterid:')

try:
	if voterid == 'yes':
		print('You can vote now')
	else:
		raise NameError('You are not elligible for votting.')

except NameError as e:
	print(e)

except IndexError as e:
	print(e)

except ValueError as e:
	print(e)

except Exception as e:
	print(e)

finally:
	print('Thanks for visit')
