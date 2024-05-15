class CustomError(Exception):
	message = ''

	def __init__(self, *args):
		if args:
			self.message = args[0]
		else:
			self.message = None

	def __str__(self):
		if self.message is None:
			return 'There is an error in your code'
		else:
			return self.message
