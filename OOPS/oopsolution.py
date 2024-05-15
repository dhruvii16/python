class Shopping:

	def __init__(self):
	self.items=[]

	def add_items(self,itemname,qty):
		item=(itemname,qty)
		self.items.append(item)
	def remove_items(self,itemname):
		for item in self.items:
			if item[0] == itemname:
				self.items.remove(item)
				break
	def calculate_total(self): 
 		total = 0 
 		for item in self.items: 
 			total += item[1] 
 			return total 

cart=Shopping()
cart.add_item("Papaya", 100) 
cart.add_item("Guava", 200) 
cart.add_item("Orange", 150) 

# Display the current items in the cart and calculate the total quantity 

print("Current Items in Cart:") 
for item in cart.items: 
 	print(item[0], "-", item[1]) 
total_qty = cart.calculate_total() 
print("Total Quantity:", total_qty) 
		 
# Remove an item from the cart, display the updated items, and recalculate the 
		 
	total quantity 
	cart.remove_item("Orange") 
	print("\nUpdated Items in Cart after removing Orange:") 
		for item in cart.items: 
 			print(item[0], "-", item[1]) 
			total_qty = cart.calculate_total() 
		print("Total Quantity:", total_qty) 
