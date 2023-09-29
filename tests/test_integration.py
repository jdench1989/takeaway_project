from lib.order_generator import OrderGenerator
from lib.order import Order
import twilio

"""
Given a customer name and order number
creates an order for that customer with assigned order number
"""

def test_create_order_with_number_and_name():
    takeaway = OrderGenerator()
    order_1 = takeaway.create_order(1, "Jack")
    assert order_1.order_number == 1
    assert order_1.name == "Jack"

"""
Given a menu dict of item:cost pairs
get_menu() returns correctly
"""

def test_get_menu():
    takeaway = OrderGenerator()
    order1 = takeaway.create_order(1, "Jack")
    assert order1.get_menu() == {"Cheeseburger": 6, "Fries": 3, "Hotdog": 5,
                                 "Pizza": 8, "Fried chicken": 7, "Milkshake": 4, "Coke": 2}

"""
Given an order of multiple items
print_receipt correctly returns a formatted list of the items including the total
"""

def test_print_receipt_correctly_returns_formatted_receipt():
    generator = OrderGenerator()
    order1234 = generator.create_order(1234, "Jack Dench")
    order1234.add("Cheeseburger")
    order1234.add("Milkshake")
    order1234.add("Coke")
    receipt = order1234.print_receipt()
    assert receipt == ("Order number: 1234\n"
                       "Customer name: Jack Dench\n"
                       "Cheeseburger: £6\n"
                       "Milkshake: £4\n"
                       "Coke: £2\n"
                       "The total cost of your order is: £12")

"""
Given an order of multiple items
confirm_order() sends an SMS via Twilio including an expected delivery time
and a receipt for the order
"""
def test_confirm_order_send_SMS():
    generator = OrderGenerator()
    order1234 = generator.create_order(1234, "Jack Dench")
    order1234.add("Cheeseburger")
    order1234.add("Milkshake")
    order1234.add("Coke")
    message_sid = generator.confirm_order(order1234)
    # assert message_sid != None
    assert message_sid is not None