# CIS 2348 Homework 3 Fall 2020.
# Dwayne Ellis
# Student ID: 0833810
# Lab 10.19 Online shopping (Part 2)
# This program extends the earlier "Online shopping cart" program.

class ItemToPurchase:

    def __init__(self, name='none', price=0, quantity=0, description='none'):
        self.item_name = name

        self.item_description = description

        self.item_price = price

        self.item_quantity = quantity

    def print_item_cost(self):
        total = self.item_price * self.item_quantity

        print('%s %d @ $%d = $%d' % (self.item_name, self.item_quantity, self.item_price, total))

    def print_item_description(self):
        print('%s: %s' % (self.item_name, self.item_description))


class ShoppingCart:

    def __init__(self, customer_name='none', date='January 1, 2016', cart_items=[]):

        self.customer_name = customer_name

        self.current_date = date

        self.cart_items = cart_items

    def add_item(self, item_to_purchase):

        self.cart_items.append(item_to_purchase)

    def tremove_item(self, item_name):

        tremove_item = False

        for item in self.cart_items:

            if item.item_name == item_name:
                self.cart_items.remove(item)

                tremove_item = True

                break

        if not tremove_item:
            print('Item not found in the cart. Nothing removed')

    def tmodify_item(self, item_to_purchase):

        tmodify_item = False

        for i in range(len(self.cart_items)):

            if self.cart_items[i].item_name == item_to_purchase.item_name:

                tmodify_item = True

                # check for default values

                if (
                        item_to_purchase.item_price == 0 and item_to_purchase.item_quantity == 0 and
                        item_to_purchase.item_description == 'none'):

                    break

                else:

                    if item_to_purchase.item_price != 0:
                        self.cart_items[i].item_price = item_to_purchase.item_price

                    if item_to_purchase.item_quantity != 0:
                        self.cart_items[i].item_quantity = item_to_purchase.item_quantity

                    if item_to_purchase.item_description != 'none':
                        self.cart_items[i].item_description = item_to_purchase.item_description

                    break

        if not tmodify_item:
            print('Item not found in the cart. Nothing modified')

    def get_num_items_in_cart(self):

        num_items = 0

        for item in self.cart_items:
            num_items = num_items + item.item_quantity

        return num_items

    def get_cost_of_cart(self):

        total_cost = 0

        cost = 0

        for item in self.cart_items:
            cost = (item.item_quantity * item.item_price)

            total_cost += cost

        return total_cost

    def print_total(self):

        total_cost = self.get_cost_of_cart()

        if total_cost == 0:

            print('SHOPPING CART IS EMPTY')

        else:

            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))

            print('Number of Items: %d\n' % self.get_num_items_in_cart())

            for item in self.cart_items:
                item.print_item_cost()

            print('\nTotal: $%d' % total_cost)

    def print_descriptions(self):

        if len(self.cart_items) == 0:

            print('SHOPPING CART IS EMPTY')

        else:

            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))

            print('\nItem Descriptions')

            for item in self.cart_items:
                item.print_item_description()


def print_menu(new_cart):
    customer_cart = new_cart

    menu = ('\nMENU\n'

            'a - Add item to cart\n'

            'r - Remove item from cart\n'

            'c - Change item quantity\n'

            "i - Output items' descriptions\n"

            'o - Output shopping cart\n'

            'q - Quit\n')

    command = ''

    while command != 'q':

        print(menu)

        command = input('Choose an option:\n')
        command = input('Choose an option:\n')
        command = input('Choose an option:\n')


        while (
                command != 'a' and command != 'o' and command != 'i' and command != 'q'
                and command != 'r' and command != 'c'):
            command = input('Choose an option:\n')

        if command == 'a':

            print("\nADD ITEM TO CART")

            item_name = input('Enter the item name:\n')

            item_description = input('Enter the item description:\n')

            item_price = int(input('Enter the item price:\n'))

            item_quantity = int(input('Enter the item quantity:\n'))

            item_to_purchase = ItemToPurchase(item_name, item_price, item_quantity, item_description)

            customer_cart.add_item(item_to_purchase)

        elif command == 'o':

            print('\nOUTPUT SHOPPING CART')

            customer_cart.print_total()

        elif command == 'i':

            print('\nOUTPUT ITEMS\' DESCRIPTIONS')

            customer_cart.print_descriptions()

        elif command == 'r':

            print('REMOVE ITEM FROM CART')

            item_name = input('Enter the name of the item to remove :\n')

            customer_cart.remove_item(item_name)

        elif command == 'c':

            print('\nCHANGE ITEM QUANTITY')

            item_name = input('Enter the name of the item :\n')

            qty = int(input('Enter the new quantity :\n'))

            item_to_purchase = ItemToPurchase(item_name, 0, qty)

            customer_cart.modify_item(item_to_purchase)


if __name__ == "__main__":
    customer_name = input("Enter customer's name:\n")

    current_date = input("Enter today's date:\n")

    print("\nCustomer name: %s" % customer_name)

    print("Today's date: %s" % current_date)

    new_cart = ShoppingCart(customer_name, current_date)

    print_menu(new_cart)
