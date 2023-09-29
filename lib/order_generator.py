from lib.order import Order

class OrderGenerator:

    def __init__(self):
        pass

    def create_order(self, order_number, name):
        order = Order(order_number, name)
        return order
    
    def print_receipt(self, order):
        item_list = order.items
        total = order.total
        receipt = f"Order number: {order.order_number}\nCustomer name: {order.name}\n"
        for item in item_list:
            receipt += f"{item}: £{order.items[item]}" + "\n"
        receipt += f"The total cost of your order is: £{total}"
        return receipt

