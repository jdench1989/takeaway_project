from lib.order import *

class OrderGenerator:

    def __init__(self):
        self.used_order_numbers = []
    
    def create_order(self, order_number, name):
        order = Order(order_number, name)
        return order
    
    def print_receipt(self, order):
        item_list = order.items
        total = order.total
        receipt = ""
        for item in item_list:
            receipt += f"{item}: £{order.items[item]}" + "\n"
        receipt += f"The total cost of your order is: £{total}"
        return receipt
