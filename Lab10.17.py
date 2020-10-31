# CIS 2348 Homework 3 Fall 2020.
# Dwayne Ellis
# Student ID: 0833810
# Lab 10.17 Warm up: Online shopping cart (Part 1)
# Complete the Team class implementation

# Creating item to purchase
class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        print(self.item_name + " " + str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" +
              str(self.item_price * self.item_quantity))


# Prompt user for two items and creating two object

if __name__ == '__main__':
    print("Item 1")
    item1 = ItemToPurchase()
    item1.item_name = input('Enter the item name:\n')
    item1.item_price = int(input('Enter the item price:\n'))
    item1.item_quantity = int(input('Enter the item quantity:\n'))
    # printing the list details and calculating the total cost
    print("\nItem 2")
    item2 = ItemToPurchase()
    item2.item_name = input('Enter the item name:\n')
    item2.item_price = int(input('Enter the item price:\n'))
    item2.item_quantity = int(input('Enter the item quantity:\n'))

    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()

    total = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)

    print("\nTotal: $" + str(total))
