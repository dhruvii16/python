class Shopping:

    def __init__(self):
        self.items = []

    def add_item(self, itemname, qty):
        item = (itemname, qty)
        self.items.append(item)

    def remove_item(self, itemname):
        for item in self.items:
            if item[0] == itemname:
                self.items.remove(item)
                break

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total

cart = Shopping()

# Get user input for items and quantities
while True:
    item_name = input("Enter item name (or type 'done' to finish): ")
    if item_name.lower() == 'done':
        break
    quantity = int(input("Enter quantity for {}: ".format(item_name)))
    cart.add_item(item_name, quantity)

# Display the current items in the cart and calculate the total quantity
print("\nCurrent Items in Cart:")
for item in cart.items:
    print(item[0], "-", item[1])
total_qty = cart.calculate_total()
print("Total Quantity:", total_qty)

# Remove an item from the cart, display the updated items, and recalculate the total quantity
item_to_remove = input("\nEnter an item to remove from the cart: ")
cart.remove_item(item_to_remove)
print("\nUpdated Items in Cart after removing {}:".format(item_to_remove))
for item in cart.items:
    print(item[0], "-", item[1])
total_qty = cart.calculate_total()
print("Total Quantity:", total_qty)
